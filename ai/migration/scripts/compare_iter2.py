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

# Filter out some noise if needed, or just show counts by folder
grouped_missing = {}
for f in missing:
    top_dir = f.split(os.sep)[0]
    if top_dir not in grouped_missing:
        grouped_missing[top_dir] = []
    grouped_missing[top_dir].append(f)

print(f"Total missing files: {len(missing)}")
for top_dir in sorted(grouped_missing.keys()):
    count = len(grouped_missing[top_dir])
    print(f"{top_dir}: {count} missing files")
    # Show extensions if it's the extensions folder
    if top_dir == 'extensions':
        for f in sorted(grouped_missing[top_dir])[:10]:
            print(f"  - {f}")
