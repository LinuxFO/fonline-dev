import re

# Files to check and merge
source_vars = r"c:\Games\fodev\fonline-dev\migration-todo\fonline-2258\Server\scripts\_vars.fos"
target_vars = r"c:\Games\fodev\fonline-dev\PReloaded\Server\scripts\_vars.fos"

source_defines = r"c:\Games\fodev\fonline-dev\migration-todo\fonline-2258\Server\scripts\_defines.fos"
target_defines = r"c:\Games\fodev\fonline-dev\PReloaded\Server\scripts\_defines.fos"

def extract_all_defines(filepath):
    """Extract all #define statements."""
    defines = {}
    pattern = re.compile(r'#define\s+(\w+)\s+\((.*?)\)')
    
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            for line_num, line in enumerate(f, 1):
                match = pattern.search(line)
                if match:
                    name = match.group(1)
                    value = match.group(2)
                    defines[name] = (value, line.strip(), line_num)
    except FileNotFoundError:
        print(f"File not found: {filepath}")
        return {}
    return defines

def merge_missing_defines():
    print("Extracting all defines from fonline-2258 _vars.fos...")
    source_vars_defs = extract_all_defines(source_vars)
    print(f"Found {len(source_vars_defs)} defines in source")
    
    print("Extracting all defines from PReloaded _vars.fos...")
    target_vars_defs = extract_all_defines(target_vars)
    print(f"Found {len(target_vars_defs)} defines in target")
    
    print("\nExtracting all defines from fonline-2258 _defines.fos...")
    source_defines_defs = extract_all_defines(source_defines)
    print(f"Found {len(source_defines_defs)} defines in source")
    
    print("Extracting all defines from PReloaded _defines.fos...")
    target_defines_defs = extract_all_defines(target_defines)
    print(f"Found {len(target_defines_defs)} defines in target")
    
    # Find missing in _vars.fos
    missing_vars = {k: v for k, v in source_vars_defs.items() if k not in target_vars_defs}
    print(f"\nMissing in _vars.fos: {len(missing_vars)}")
    
    # Find missing in _defines.fos
    missing_defines = {k: v for k, v in source_defines_defs.items() if k not in target_defines_defs}
    print(f"Missing in _defines.fos: {len(missing_defines)}")
    
    total_added = 0
    
    if missing_vars:
        with open(target_vars, 'a', encoding='utf-8') as f:
            f.write("\n\n// ====== Additional definitions migrated from fonline-2258 ======\n")
            for name in sorted(missing_vars.keys()):
                value, line, line_num = missing_vars[name]
                f.write(line + "\n")
        print(f"Appended {len(missing_vars)} definitions to _vars.fos")
        total_added += len(missing_vars)
    
    if missing_defines:
        with open(target_defines, 'a', encoding='utf-8') as f:
            f.write("\n\n// ====== Additional definitions migrated from fonline-2258 ======\n")
            for name in sorted(missing_defines.keys()):
                value, line, line_num = missing_defines[name]
                f.write(line + "\n")
        print(f"Appended {len(missing_defines)} definitions to _defines.fos")
        total_added += len(missing_defines)
    
    print(f"\nTotal definitions added: {total_added}")
    return total_added

if __name__ == "__main__":
    merge_missing_defines()
