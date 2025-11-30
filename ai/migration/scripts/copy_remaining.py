import os
import shutil

source_dir = r"c:\Games\fodev\fonline-dev\migration-todo\fonline-2258\Server\scripts"
target_dir = r"c:\Games\fodev\fonline-dev\PReloaded\Server\scripts"
config_file = r"c:\Games\fodev\fonline-dev\PReloaded\Server\scripts\scripts.cfg"

def copy_remaining_scripts():
    print("Copying remaining scripts...")
    
    source_files = {f for f in os.listdir(source_dir) if f.endswith('.fos')}
    target_files = {f for f in os.listdir(target_dir) if f.endswith('.fos')}
    
    missing = source_files - target_files
    print(f"Found {len(missing)} missing scripts.")
    
    copied = []
    for f in missing:
        src = os.path.join(source_dir, f)
        dst = os.path.join(target_dir, f)
        shutil.copy2(src, dst)
        copied.append(f)
        print(f"Copied {f}")
        
    if copied:
        print("Updating scripts.cfg...")
        with open(config_file, 'a') as cfg:
            cfg.write("\n# Migrated Remaining Scripts\n")
            for f in sorted(copied):
                if f.endswith('_h.fos'): continue
                module_name = os.path.splitext(f)[0]
                cfg.write(f"{module_name} = load\n")
                
    print("Copy complete.")

if __name__ == "__main__":
    copy_remaining_scripts()
