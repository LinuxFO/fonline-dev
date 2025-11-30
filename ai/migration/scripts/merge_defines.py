import re

# Migrate MAP_ definitions
source_maps = r"c:\Games\fodev\fonline-dev\migration-todo\fonline-2258\Server\scripts\_maps.fos"
target_maps = r"c:\Games\fodev\fonline-dev\PReloaded\Server\scripts\_maps.fos"

# Migrate DIALOG_ definitions  
source_dialogs = r"c:\Games\fodev\fonline-dev\migration-todo\fonline-2258\Server\scripts\_dialogs.fos"
target_dialogs = r"c:\Games\fodev\fonline-dev\PReloaded\Server\scripts\_dialogs.fos"

def extract_defines(filepath, prefix):
    """Extract all #define statements with given prefix."""
    defines = {}
    pattern = re.compile(rf'#define\s+({prefix}\w+)\s+\((\d+)\)')
    
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            match = pattern.search(line)
            if match:
                name = match.group(1)
                value = match.group(2)
                defines[name] = (value, line.strip())
    return defines

def merge_defines():
    print("Extracting MAP_ definitions...")
    source_map_defs = extract_defines(source_maps, 'MAP_')
    target_map_defs = extract_defines(target_maps, 'MAP_')
    
    missing_maps = {k: v for k, v in source_map_defs.items() if k not in target_map_defs}
    print(f"Found {len(missing_maps)} missing MAP_ definitions")
    
    if missing_maps:
        with open(target_maps, 'a', encoding='utf-8') as f:
            f.write("\n\n// ====== Migrated MAP_ definitions from fonline-2258 ======\n")
            for name in sorted(missing_maps.keys()):
                value, line = missing_maps[name]
                f.write(line + "\n")
        print(f"Appended {len(missing_maps)} MAP_ definitions to _maps.fos")
    
    print("\nExtracting DIALOG_ definitions...")
    source_dialog_defs = extract_defines(source_dialogs, 'DIALOG_')
    target_dialog_defs = extract_defines(target_dialogs, 'DIALOG_')
    
    missing_dialogs = {k: v for k, v in source_dialog_defs.items() if k not in target_dialog_defs}
    print(f"Found {len(missing_dialogs)} missing DIALOG_ definitions")
    
    if missing_dialogs:
        with open(target_dialogs, 'a', encoding='utf-8') as f:
            f.write("\n\n// ====== Migrated DIALOG_ definitions from fonline-2258 ======\n")
            for name in sorted(missing_dialogs.keys()):
                value, line = missing_dialogs[name]
                f.write(line + "\n")
        print(f"Appended {len(missing_dialogs)} DIALOG_ definitions to _dialogs.fos")
    
    print(f"\n✓ Migration complete!")
    print(f"Total definitions added: {len(missing_maps) + len(missing_dialogs)}")
    return len(missing_maps) + len(missing_dialogs)

if __name__ == "__main__":
    merge_defines()
