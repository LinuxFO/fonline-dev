import os
import re
import argparse
import json
from pathlib import Path

# Category definitions
CATEGORIES = {
    'client': {
        'name': 'Client Scripts',
        'pattern': r'^client_',
        'keywords': ['client', 'gui', 'interface', 'screen'],
        'description': 'Client-side UI, rendering, and input handling'
    },
    'quests': {
        'name': 'Quest System',
        'pattern': r'^quest',
        'keywords': ['quest', 'mission'],
        'description': 'Quest management, assignment, and tracking'
    },
    'combat': {
        'name': 'Combat System',
        'pattern': r'(^combat|hexShot|hexThrow|throwing|explode|traps)',
        'keywords': ['combat', 'damage', 'attack', 'weapon'],
        'description': 'Combat mechanics and damage calculation'
    },
    'economy': {
        'name': 'Economy',
        'pattern': r'(^economy|^trader|recycler|prices)',
        'keywords': ['economy', 'trade', 'bank', 'caps', 'money'],
        'description': 'Trading, banking, and item pricing'
    },
    'factions': {
        'name': 'Factions',
        'pattern': r'^factions',
        'keywords': ['faction', 'reputation'],
        'description': 'Faction management and reputation system'
    },
    'maps': {
        'name': 'Maps',
        'pattern': r'^map_',
        'keywords': ['map', 'location'],
        'description': 'Map initialization, events, and spawning'
    },
    'npcs': {
        'name': 'NPCs',
        'pattern': r'(^npc_|_guard$|^follower|^guard$)',
        'keywords': ['npc', 'critter', 'ai', 'dialog'],
        'description': 'NPC AI, behavior, and dialogue'
    },
    'items': {
        'name': 'Items',
        'pattern': r'^item_',
        'keywords': ['item', 'inventory'],
        'description': 'Item-specific behaviors and interactions'
    },
    'production': {
        'name': 'Production',
        'pattern': r'(^prod_|^production|workbench)',
        'keywords': ['craft', 'production', 'resource', 'gather'],
        'description': 'Crafting and resource gathering systems'
    },
    'world': {
        'name': 'World Management',
        'pattern': r'(^worldmap|^town|trains)',
        'keywords': ['world', 'town', 'travel'],
        'description': 'World map, towns, and travel systems'
    },
    'mapper': {
        'name': 'Mapper Tools',
        'pattern': r'^mapper_',
        'keywords': ['mapper', 'editor'],
        'description': 'Map editor tools and utilities'
    },
    'minigames': {
        'name': 'Minigames',
        'pattern': r'(^blackjack|^slots|^minigames)',
        'keywords': ['game', 'casino', 'gambling'],
        'description': 'Casino games and entertainment'
    },
    'core': {
        'name': 'Core & Utilities',
        'pattern': r'(^_|^main$|^utils)',
        'keywords': ['util', 'helper', 'define', 'macro'],
        'description': 'Core systems, utilities, and definitions'
    }
}

def categorize_script(filename):
    """Categorize a script based on filename and patterns"""
    categories = []
    
    for cat_id, cat_info in CATEGORIES.items():
        if re.search(cat_info['pattern'], filename, re.IGNORECASE):
            categories.append(cat_id)
    
    # Default to 'core' if no category found
    if not categories:
        categories = ['core']
    
    return categories

def count_section_items(content, section_header):
    """Count items in a markdown section"""
    # Find the section
    pattern = rf'^{re.escape(section_header)}\s*$'
    match = re.search(pattern, content, re.MULTILINE)
    
    if not match:
        return 0
    
    # Get content after the section header until next ## header
    start = match.end()
    next_section = re.search(r'\n## ', content[start:])
    
    if next_section:
        section_content = content[start:start + next_section.start()]
    else:
        section_content = content[start:]
    
    # Count ### headers (classes/functions) or table rows (variables)
    if '###' in section_content:
        return len(re.findall(r'^### ', section_content, re.MULTILINE))
    elif '|' in section_content:
        # Count table rows (excluding header rows)
        rows = re.findall(r'^\|[^-]', section_content, re.MULTILINE)
        return max(0, len(rows) - 2)  # Subtract header and separator
    
    return 0

def extract_includes(content):
    """Extract include files from Includes section"""
    includes = []
    pattern = r'^## Includes\s*$'
    match = re.search(pattern, content, re.MULTILINE)
    
    if match:
        start = match.end()
        next_section = re.search(r'\n## ', content[start:])
        
        if next_section:
            section_content = content[start:start + next_section.start()]
        else:
            section_content = content[start:]
        
        # Extract filenames from list items
        includes = re.findall(r'- `([^`]+)`', section_content)
    
    return includes

def extract_metadata(md_file):
    """Extract metadata from a markdown documentation file"""
    try:
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {md_file}: {e}")
        return None
    
    filename = md_file.stem.replace('.fos', '')
    
    # Extract description from frontmatter or first paragraph
    description = ""
    desc_match = re.search(r'description:\s*"([^"]+)"', content)
    if desc_match:
        description = desc_match.group(1)
    
    metadata = {
        'filename': filename,
        'filepath': str(md_file),
        'classes': count_section_items(content, '## Classes'),
        'functions': count_section_items(content, '## Functions'),
        'variables': count_section_items(content, '## Variables'),
        'constants': count_section_items(content, '## Constants'),
        'defines': count_section_items(content, '## Defines'),
        'includes': extract_includes(content),
        'size_kb': round(md_file.stat().st_size / 1024, 2),
        'categories': categorize_script(filename),
        'description': description
    }
    
    return metadata

def analyze_documentation(docs_path):
    """Analyze all .md files in docs directory"""
    docs_dir = Path(docs_path)
    scripts = []
    
    print(f"Analyzing documentation files in {docs_dir}...")
    
    if not docs_dir.exists():
        print(f"Error: Directory {docs_dir} does not exist.")
        return []

    for md_file in sorted(docs_dir.rglob('*.fos.md')):
        metadata = extract_metadata(md_file)
        if metadata:
            scripts.append(metadata)
            # print(f"  Analyzed: {metadata['filename']}")
    
    print(f"\nTotal scripts analyzed: {len(scripts)}")
    
    return scripts

def calculate_statistics(scripts):
    """Calculate overall statistics"""
    stats = {
        'total_scripts': len(scripts),
        'total_classes': sum(s['classes'] for s in scripts),
        'total_functions': sum(s['functions'] for s in scripts),
        'total_variables': sum(s['variables'] for s in scripts),
        'total_constants': sum(s['constants'] for s in scripts),
        'total_defines': sum(s['defines'] for s in scripts),
        'largest_scripts': sorted(scripts, key=lambda x: x['size_kb'], reverse=True)[:10],
        'most_classes': sorted(scripts, key=lambda x: x['classes'], reverse=True)[:10],
        'most_functions': sorted(scripts, key=lambda x: x['functions'], reverse=True)[:10],
        'most_included': [],  # Will calculate based on includes
        'by_category': {}
    }
    
    # Count scripts by category
    for cat_id in CATEGORIES.keys():
        cat_scripts = [s for s in scripts if cat_id in s['categories']]
        stats['by_category'][cat_id] = {
            'count': len(cat_scripts),
            'name': CATEGORIES[cat_id]['name'],
            'scripts': [s['filename'] for s in cat_scripts]
        }
    
    # Calculate most included scripts
    include_counts = {}
    for script in scripts:
        for include in script['includes']:
            include_name = include.replace('.fos', '')
            include_counts[include_name] = include_counts.get(include_name, 0) + 1
    
    most_included = sorted(include_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    stats['most_included'] = [{'name': name, 'count': count} for name, count in most_included]
    
    return stats

def save_results(scripts, stats, output_file):
    """Save analysis results to JSON file"""
    output = {
        'scripts': scripts,
        'statistics': stats,
        'categories': CATEGORIES
    }
    
    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2)
    
    print(f"\nResults saved to {output_path}")

def main():
    parser = argparse.ArgumentParser(description='Analyze FOnline script documentation.')
    parser.add_argument('--docs', '-d', default=r"ai\docs\files", help='Directory containing generated .md documentation')
    parser.add_argument('--output', '-o', default=r"ai\docs\analysis.json", help='Output JSON file for analysis results')
    
    args = parser.parse_args()
    
    scripts = analyze_documentation(args.docs)
    if not scripts:
        return

    stats = calculate_statistics(scripts)
    save_results(scripts, stats, args.output)
    
    print("\n=== Statistics Summary ===")
    print(f"Total Scripts: {stats['total_scripts']}")
    print(f"Total Classes: {stats['total_classes']}")
    print(f"Total Functions: {stats['total_functions']}")
    print(f"Total Variables: {stats['total_variables']}")
    print(f"\nScripts by Category:")
    for cat_id, cat_data in sorted(stats['by_category'].items(), key=lambda x: x[1]['count'], reverse=True):
        print(f"  {cat_data['name']}: {cat_data['count']}")

if __name__ == '__main__':
    main()
