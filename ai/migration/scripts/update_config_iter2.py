import os

config_file = r"c:\Games\fodev\fonline-dev\PReloaded\Server\scripts\scripts.cfg"

# List of scripts I know I copied in Phase 1 of Iteration 2
# I can just scan the directory and add anything not in scripts.cfg?
# That might be safer.

def update_config():
    print("Updating scripts.cfg...")
    
    with open(config_file, 'r') as f:
        content = f.read()
        
    existing_modules = set()
    for line in content.splitlines():
        if '=' in line and not line.strip().startswith('#'):
            module = line.split('=')[0].strip()
            existing_modules.add(module)
            
    # Scan directory for .fos files
    scripts_dir = r"c:\Games\fodev\fonline-dev\PReloaded\Server\scripts"
    all_scripts = [f for f in os.listdir(scripts_dir) if f.endswith('.fos')]
    
    new_modules = []
    for f in all_scripts:
        if f.endswith('_h.fos'): continue
        module = os.path.splitext(f)[0]
        if module not in existing_modules:
            new_modules.append(module)
            
    if new_modules:
        print(f"Found {len(new_modules)} scripts not in config.")
        with open(config_file, 'a') as f:
            f.write("\n# Iteration 2 Migrated Scripts\n")
            for m in sorted(new_modules):
                f.write(f"{m} = load\n")
                print(f"Added {m}")
    else:
        print("No new scripts to add.")

if __name__ == "__main__":
    update_config()
