import os

def get_all_files(root_dir):
    file_set = set()
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            rel_path = os.path.relpath(os.path.join(root, file), root_dir)
            file_set.add(rel_path)
    return file_set

source = r"c:\Games\fodev\fonline-dev\migration-todo\fonline-2258\Server"
target = r"c:\Games\fodev\fonline-dev\PReloaded\Server"

source_files = get_all_files(source)
target_files = get_all_files(target)
missing = source_files - target_files

missing_fos = [f for f in missing if f.endswith('.fos') and f.startswith('scripts')]
print(f"Missing .fos scripts: {len(missing_fos)}")
for f in sorted(missing_fos):
    print(f)
