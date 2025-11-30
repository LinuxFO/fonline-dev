import re

source_file = r"c:\Games\fodev\fonline-dev\migration-todo\fonline-2258\Server\scripts\_vars.fos"
target_file = r"c:\Games\fodev\fonline-dev\PReloaded\Server\scripts\_vars.fos"

def extract_lvars(filepath):
    """Extract all LVAR definitions from a file."""
    lvars = {}
    pattern = re.compile(r'#define\s+(LVAR_\w+)\s+\((\d+)\)')
    
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            match = pattern.search(line)
            if match:
                name = match.group(1)
                value = match.group(2)
                lvars[name] = value
                
    return lvars

def migrate_lvars():
    print("Extracting LVARs from source...")
    source_lvars = extract_lvars(source_file)
    print(f"Found {len(source_lvars)} LVARs in fonline-2258")
    
    print("\nExtracting LVARs from target...")
    target_lvars = extract_lvars(target_file)
    print(f"Found {len(target_lvars)} LVARs in PReloaded")
    
    # Find missing LVARs
    missing = {}
    for name, value in source_lvars.items():
        if name not in target_lvars:
            missing[name] = value
        elif target_lvars[name] != value:
            print(f"WARNING: {name} has different values: {target_lvars[name]} (PReloaded) vs {value} (2258)")
            
    print(f"\nFound {len(missing)} missing LVARs")
    
    if missing:
        print("\nAppending missing LVARs to PReloaded...")
        with open(target_file, 'a', encoding='utf-8') as f:
            f.write("\n\n// ====== Migrated from fonline-2258 ======\n")
            for name in sorted(missing.keys()):
                value = missing[name]
                f.write(f"#define {name:<45} ({value})\n")
                
        print(f"Added {len(missing)} LVAR definitions")
        
        # Show first 10 as examples
        print("\nExamples of added LVARs:")
        for name in sorted(missing.keys())[:10]:
            print(f"  {name} ({missing[name]})")
    else:
        print("No missing LVARs found!")
        
    return len(missing)

if __name__ == "__main__":
    count = migrate_lvars()
    print(f"\n✓ Migration complete. Added {count} LVAR definitions.")
