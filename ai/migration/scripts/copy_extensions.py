import os
import shutil

source_base = r"c:\Games\fodev\fonline-dev\migration-todo\fonline-2258\Server\extensions"
target_base = r"c:\Games\fodev\fonline-dev\PReloaded\Server\extensions"

extensions_to_copy = ['Backend', '3rdParty']

def copy_extensions():
    print("Copying extensions...")
    
    for ext in extensions_to_copy:
        src = os.path.join(source_base, ext)
        dst = os.path.join(target_base, ext)
        
        if os.path.exists(dst):
            print(f"Destination {dst} already exists. Merging/Overwriting...")
        
        # shutil.copytree requires destination to not exist usually, or use dirs_exist_ok=True in newer python
        # Let's use a custom copy function to be safe and verbose
        
        count = 0
        for root, dirs, files in os.walk(src):
            rel_path = os.path.relpath(root, src)
            dst_dir = os.path.join(dst, rel_path)
            
            os.makedirs(dst_dir, exist_ok=True)
            
            for file in files:
                src_file = os.path.join(root, file)
                dst_file = os.path.join(dst_dir, file)
                
                shutil.copy2(src_file, dst_file)
                count += 1
                
        print(f"Copied {count} files for {ext}")

    print("Extension copy complete.")

if __name__ == "__main__":
    copy_extensions()
