import os
import re

SOURCE_DIR = r"PReloaded\Server\scripts"
DEST_DIR = r"docs\files"

os.makedirs(DEST_DIR, exist_ok=True)

KEYWORDS = {
    'return', 'if', 'else', 'while', 'for', 'switch', 'case', 'break', 'continue', 
    'import', 'include', 'define', 'class', 'interface', 'mixin', 'shared', 'private', 
    'protected', 'public'
}

def parse_file(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        lines = f.readlines()

    doc = {
        'filename': os.path.basename(filepath),
        'description': [],
        'includes': [],
        'defines': [],
        'constants': [],
        'variables': [],
        'functions': [],
        'classes': []
    }

    # Regex patterns
    re_include = re.compile(r'^\s*#include\s+["<](.*)[">]')
    re_define = re.compile(r'^\s*#define\s+(\w+)(?:\s+(.*))?')
    re_class = re.compile(r'^\s*(?:shared\s+|interface\s+|mixin\s+)?class\s+(\w+)')
    re_func = re.compile(r'^\s*(?:import\s+)?([A-Za-z0-9_<>]+(?:@[A-Za-z0-9_]*)?)\s+([A-Za-z0-9_]+)\s*\((.*)\)')
    re_var = re.compile(r'^\s*(const\s+)?([A-Za-z0-9_<>]+(?:@[A-Za-z0-9_]*)?)\s+([A-Za-z0-9_]+)(?:\s*=\s*(.*))?;')

    pending_comment = []
    element_comment = []
    
    in_class = None # Reference to current class dict
    brace_depth = 0
    
    in_function = False # Track if we are inside a function
    function_brace_depth = 0
    
    # Track if we are inside a multiline comment
    in_multiline_comment = False

    for line in lines:
        stripped = line.strip()
        
        # --- Comment Handling ---
        if not stripped:
            # Blank line
            if pending_comment:
                # If we have a pending comment and hit a blank line, 
                # check if it's the file header (first comment of file)
                if not doc['description'] and not doc['includes'] and not doc['defines'] and not doc['classes'] and not doc['functions']:
                     doc['description'] = pending_comment
                else:
                    # Otherwise, it's a detached comment, discard it or maybe it belongs to the next block?
                    # Standard style: Blank line breaks the link between comment and code.
                    pass
                pending_comment = []
            continue

        # Handle // comments
        if stripped.startswith('//'):
            content = stripped[2:].strip()
            if content.startswith('/'): content = content[1:].strip()
            pending_comment.append(content)
            continue
            
        # Handle /* */ comments (simplified, assumes start on new line)
        if stripped.startswith('/*'):
            in_multiline_comment = True
            content = stripped[2:].strip()
            if content.endswith('*/'):
                in_multiline_comment = False
                content = content[:-2].strip()
            pending_comment.append(content)
            continue
            
        if in_multiline_comment:
            content = stripped
            if content.endswith('*/'):
                in_multiline_comment = False
                content = content[:-2].strip()
            pending_comment.append(content)
            continue

        # If we are here, it's code. 
        # Assign pending_comment to element_comment
        element_comment = pending_comment
        pending_comment = []
        
        # --- Brace Counting for Scope ---
        # This is very basic and can be fooled by strings/comments containing braces, 
        # but for a doc generator it's usually "good enough".
        # We already stripped comments above (if the whole line was comment).
        # If line has code + comment, we should strip the comment part for regex matching but keep braces?
        # Let's strip trailing comments for regex matching.
        
        code_part = stripped.split('//')[0].strip()
        
        open_braces = code_part.count('{')
        close_braces = code_part.count('}')
        
        # Check if we are exiting a function (must be before class check)
        if in_function:
            function_brace_depth += open_braces - close_braces
            if function_brace_depth <= 0:
                in_function = False
                function_brace_depth = 0
        
        # Check if we are exiting a class
        if in_class:
            brace_depth += open_braces - close_braces
            if brace_depth <= 0:
                in_class = None
                brace_depth = 0

        # --- Matching ---

        # Includes
        m = re_include.match(code_part)
        if m:
            doc['includes'].append(m.group(1))
            continue

        # Defines
        m = re_define.match(code_part)
        if m:
            doc['defines'].append({
                'name': m.group(1), 
                'value': m.group(2) if m.group(2) else '',
                'desc': element_comment
            })
            continue

        # Classes
        m = re_class.match(code_part)
        if m:
            new_class = {
                'name': m.group(1), 
                'members': [], 
                'methods': [],
                'desc': element_comment
            }
            doc['classes'].append(new_class)
            in_class = new_class
            brace_depth = code_part.count('{') - code_part.count('}')
            
            # If it's a forward declaration "class Foo;", it ends with ; and has no {
            if '{' not in code_part and code_part.endswith(';'):
                in_class = None
            continue

        # Functions
        m = re_func.match(code_part)
        if m and not code_part.endswith(';'): 
            ret_type = m.group(1)
            func_name = m.group(2)
            
            if ret_type not in KEYWORDS and func_name not in KEYWORDS:
                func_obj = {
                    'return_type': ret_type,
                    'name': func_name,
                    'params': m.group(3),
                    'signature': code_part.rstrip('{').strip(),
                    'desc': element_comment
                }
                
                if in_class:
                    in_class['methods'].append(func_obj)
                else:
                    doc['functions'].append(func_obj)
                    # Mark that we're entering a function (only for global functions)
                    in_function = True
                    function_brace_depth = open_braces - close_braces
                continue

        # Variables / Constants
        m = re_var.match(code_part)
        if m:
            is_const = bool(m.group(1))
            dtype = m.group(2)
            name = m.group(3)
            value = m.group(4)
            
            if dtype not in KEYWORDS and name not in KEYWORDS:
                item = {
                    'type': dtype, 
                    'name': name, 
                    'value': value if value else '',
                    'desc': element_comment
                }
                
                # Only capture if:
                # 1. Global variable: brace_depth == 0 AND not in_function AND not in_class
                # 2. Class member: in_class AND brace_depth == 1 AND not in_function
                
                if in_class:
                    # Class member - only if at class level (not inside a method)
                    if brace_depth == 1 and not in_function:
                        in_class['members'].append(item)
                elif brace_depth == 0 and not in_function:
                    # Global variable or constant
                    if is_const:
                        doc['constants'].append(item)
                    else:
                        doc['variables'].append(item)
            continue

    return doc

def format_desc(lines):
    if not lines:
        return ""
    return " ".join(lines)

def link_type(type_str, type_map):
    # Handle array<Type> or Type@ or Type&
    # Simple regex to find words and link them if they exist in type_map
    
    def replace_match(match):
        word = match.group(0)
        if word in type_map:
            return f"[{word}]({type_map[word]})"
        return word

    return re.sub(r'\b\w+\b', replace_match, type_str)

def generate_md(doc, type_map):
    filename = doc['filename']
    md_filename = filename + ".md"
    path = os.path.join(DEST_DIR, md_filename)
    
    with open(path, 'w', encoding='utf-8') as f:
        # Frontmatter
        f.write("---\n")
        f.write(f"title: {filename}\n")
        desc_summary = format_desc(doc['description']).replace('"', '\\"')
        if desc_summary:
            f.write(f"description: \"{desc_summary[:150]}...\"\n")
        f.write("---\n\n")
        
        f.write(f"# {filename}\n\n")
        
        if doc['description']:
            for line in doc['description']:
                f.write(f"{line}\n")
            f.write("\n")
        
        if doc['includes']:
            f.write("## Includes\n\n")
            for inc in doc['includes']:
                f.write(f"- `{inc}`\n")
            f.write("\n")

        if 'included_by' in doc and doc['included_by']:
            f.write("## Included By\n\n")
            for inc in doc['included_by']:
                f.write(f"- [{inc}]({inc}.md)\n")
            f.write("\n")

        if doc['defines']:
            f.write("## Defines\n\n")
            f.write("| Name | Value | Description |\n")
            f.write("| :--- | :--- | :--- |\n")
            for d in doc['defines']:
                val = f"`{d['value']}`" if d['value'] else ""
                desc = format_desc(d['desc'])
                f.write(f"| {d['name']} | {val} | {desc} |\n")
            f.write("\n")

        if doc['constants']:
            f.write("## Constants\n\n")
            f.write("| Name | Type | Value | Description |\n")
            f.write("| :--- | :--- | :--- | :--- |\n")
            for c in doc['constants']:
                val = f"`{c['value']}`" if c['value'] else ""
                desc = format_desc(c['desc'])
                linked_type = link_type(c['type'], type_map)
                f.write(f"| {c['name']} | `{linked_type}` | {val} | {desc} |\n")
            f.write("\n")

        if doc['classes']:
            f.write("## Classes\n\n")
            for c in doc['classes']:
                f.write(f"### {c['name']}\n\n")
                if c['desc']:
                    f.write(f"{format_desc(c['desc'])}\n\n")
                
                if c['members']:
                    f.write("**Properties**\n\n")
                    f.write("| Name | Type | Value | Description |\n")
                    f.write("| :--- | :--- | :--- | :--- |\n")
                    for m in c['members']:
                        val = f"`{m['value']}`" if m['value'] else ""
                        desc = format_desc(m['desc'])
                        linked_type = link_type(m['type'], type_map)
                        f.write(f"| {m['name']} | `{linked_type}` | {val} | {desc} |\n")
                    f.write("\n")
                
                if c['methods']:
                    f.write("**Methods**\n\n")
                    for method in c['methods']:
                        f.write(f"#### {method['name']}\n")
                        if method['desc']:
                            f.write(f"{format_desc(method['desc'])}\n\n")
                        # We could also link types in signature, but it's harder to parse safely without breaking code block syntax
                        # For now, keep signature as code block
                        f.write(f"```angelscript\n{method['signature']}\n```\n\n")
            f.write("\n")

        if doc['variables']:
            f.write("## Variables\n\n")
            f.write("| Name | Type | Value | Description |\n")
            f.write("| :--- | :--- | :--- | :--- |\n")
            for v in doc['variables']:
                val = f"`{v['value']}`" if v['value'] else ""
                desc = format_desc(v['desc'])
                linked_type = link_type(v['type'], type_map)
                f.write(f"| {v['name']} | `{linked_type}` | {val} | {desc} |\n")
            f.write("\n")

        if doc['functions']:
            f.write("## Functions\n\n")
            for func in doc['functions']:
                f.write(f"### {func['name']}\n\n")
                if func['desc']:
                    f.write(f"{format_desc(func['desc'])}\n\n")
                f.write(f"```angelscript\n{func['signature']}\n```\n\n")
            f.write("\n")

    return md_filename

    return md_filename

    return md_filename

all_docs = []

# Recursive search
files = []
for root, dirs, files_in_dir in os.walk(SOURCE_DIR):
    # Skip docs-todo itself to avoid recursion if run multiple times
    if "docs-todo" in root:
        continue
        
    for f in files_in_dir:
        if f.endswith('.fos'):
            full_path = os.path.join(root, f)
            rel_path = os.path.relpath(full_path, SOURCE_DIR)
            files.append(rel_path)

files.sort()

print(f"Found {len(files)} scripts.")

# First pass: Parse all files and build type map & include graph
parsed_docs = []
type_map = {}
included_by = {} # filename -> list of relative paths that include it

for rel_path in files:
    fpath = os.path.join(SOURCE_DIR, rel_path)
    try:
        doc = parse_file(fpath)
        doc['rel_path'] = rel_path # Store relative path
        parsed_docs.append(doc)
        
        # Register classes as types
        # We map ClassName -> RelativePath.md
        # Note: If multiple files define same class, last one wins (AngelScript usually doesn't allow duplicates globally)
        doc_rel_path = rel_path + ".md"
        for c in doc['classes']:
            type_map[c['name']] = doc_rel_path
        
        # Build include graph
        for inc in doc['includes']:
            inc_name = os.path.basename(inc)
            if inc_name not in included_by:
                included_by[inc_name] = []
            included_by[inc_name].append(rel_path)
            
    except Exception as e:
        print(f"Error parsing {rel_path}: {e}")

def get_relative_link(from_rel_path, to_rel_path):
    # Calculate relative path from one doc file to another
    # from_rel_path: path/to/A.fos
    # to_rel_path: path/to/B.fos.md
    
    # We are generating A.fos.md in docs-todo/path/to/
    # We want to link to docs-todo/path/to/B.fos.md
    
    # os.path.relpath(target, start)
    # start is the directory of from_rel_path
    
    from_dir = os.path.dirname(from_rel_path)
    link = os.path.relpath(to_rel_path, from_dir)
    return link.replace("\\", "/")

# Update link_type to use relative paths
def link_type_rel(type_str, type_map, current_rel_path):
    def replace_match(match):
        word = match.group(0)
        if word in type_map:
            target_md = type_map[word]
            link = get_relative_link(current_rel_path, target_md)
            return f"[{word}]({link})"
        return word
    return re.sub(r'\b\w+\b', replace_match, type_str)

# Update generate_md to handle relative paths and subdirectories
def generate_md_rel(doc, type_map, included_by):
    rel_path = doc['rel_path']
    filename = doc['filename']
    
    # Output path: docs-todo/rel_path.md
    md_rel_path = rel_path + ".md"
    full_dest_path = os.path.join(DEST_DIR, md_rel_path)
    
    # Ensure directory exists
    os.makedirs(os.path.dirname(full_dest_path), exist_ok=True)
    
    with open(full_dest_path, 'w', encoding='utf-8') as f:
        # Frontmatter
        f.write("---\n")
        f.write(f"title: {filename}\n")
        desc_summary = format_desc(doc['description']).replace('"', '\\"')
        if desc_summary:
            f.write(f"description: \"{desc_summary[:150]}...\"\n")
        f.write("---\n\n")
        
        f.write(f"# {filename}\n\n")
        
        if doc['description']:
            for line in doc['description']:
                f.write(f"{line}\n")
            f.write("\n")
        
        if doc['includes']:
            f.write("## Includes\n\n")
            for inc in doc['includes']:
                f.write(f"- `{inc}`\n")
            f.write("\n")

        if 'included_by' in doc and doc['included_by']:
            f.write("## Included By\n\n")
            for inc_rel in doc['included_by']:
                # inc_rel is path/to/file.fos
                # We want to link to path/to/file.fos.md
                target_md = inc_rel + ".md"
                link = get_relative_link(rel_path, target_md)
                name = os.path.basename(inc_rel)
                f.write(f"- [{name}]({link})\n")
            f.write("\n")

        if doc['defines']:
            f.write("## Defines\n\n")
            f.write("| Name | Value | Description |\n")
            f.write("| :--- | :--- | :--- |\n")
            for d in doc['defines']:
                val = f"`{d['value']}`" if d['value'] else ""
                desc = format_desc(d['desc'])
                f.write(f"| {d['name']} | {val} | {desc} |\n")
            f.write("\n")

        if doc['constants']:
            f.write("## Constants\n\n")
            f.write("| Name | Type | Value | Description |\n")
            f.write("| :--- | :--- | :--- | :--- |\n")
            for c in doc['constants']:
                val = f"`{c['value']}`" if c['value'] else ""
                desc = format_desc(c['desc'])
                linked_type = link_type_rel(c['type'], type_map, rel_path)
                f.write(f"| {c['name']} | `{linked_type}` | {val} | {desc} |\n")
            f.write("\n")

        if doc['classes']:
            f.write("## Classes\n\n")
            for c in doc['classes']:
                f.write(f"### {c['name']}\n\n")
                if c['desc']:
                    f.write(f"{format_desc(c['desc'])}\n\n")
                
                if c['members']:
                    f.write("**Properties**\n\n")
                    f.write("| Name | Type | Value | Description |\n")
                    f.write("| :--- | :--- | :--- | :--- |\n")
                    for m in c['members']:
                        val = f"`{m['value']}`" if m['value'] else ""
                        desc = format_desc(m['desc'])
                        linked_type = link_type_rel(m['type'], type_map, rel_path)
                        f.write(f"| {m['name']} | `{linked_type}` | {val} | {desc} |\n")
                    f.write("\n")
                
                if c['methods']:
                    f.write("**Methods**\n\n")
                    for method in c['methods']:
                        f.write(f"#### {method['name']}\n")
                        if method['desc']:
                            f.write(f"{format_desc(method['desc'])}\n\n")
                        f.write(f"```angelscript\n{method['signature']}\n```\n\n")
            f.write("\n")

        if doc['variables']:
            f.write("## Variables\n\n")
            f.write("| Name | Type | Value | Description |\n")
            f.write("| :--- | :--- | :--- | :--- |\n")
            for v in doc['variables']:
                val = f"`{v['value']}`" if v['value'] else ""
                desc = format_desc(v['desc'])
                linked_type = link_type_rel(v['type'], type_map, rel_path)
                f.write(f"| {v['name']} | `{linked_type}` | {val} | {desc} |\n")
            f.write("\n")

        if doc['functions']:
            f.write("## Functions\n\n")
            for func in doc['functions']:
                f.write(f"### {func['name']}\n\n")
                if func['desc']:
                    f.write(f"{format_desc(func['desc'])}\n\n")
                f.write(f"```angelscript\n{func['signature']}\n```\n\n")
            f.write("\n")

    return md_rel_path

# Second pass: Generate MD
for doc in parsed_docs:
    try:
        fname = doc['filename']
        # Match included_by using filename (heuristic)
        doc['included_by'] = included_by.get(fname, [])
        
        md_path = generate_md_rel(doc, type_map, included_by)
        all_docs.append({'name': doc['rel_path'], 'md': md_path, 'desc': format_desc(doc['description'])})
    except Exception as e:
        print(f"Error generating {doc['filename']}: {e}")

# README
with open(os.path.join(DEST_DIR, "README.md"), 'w', encoding='utf-8') as f:
    f.write("# Script Documentation\n\n")
    f.write("| Script | Description |\n")
    f.write("| :--- | :--- |\n")
    for item in all_docs:
        desc = item['desc'].split('\n')[0] if item['desc'] else ""
        # Link in README is relative to docs-todo root
        f.write(f"| [{item['name']}]({item['md']}) | {desc} |\n")

print("Documentation generation complete.")
