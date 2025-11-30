import os

def get_all_files(root_dir):
    file_set = set()
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            # Get path relative to the root_dir
            rel_path = os.path.relpath(os.path.join(root, file), root_dir)
            file_set.add(rel_path)
    return file_set

def compare_full_structure(source_dir, target_dir):
    source_files = get_all_files(source_dir)
    target_files = get_all_files(target_dir)

    missing_in_target = source_files - target_files
    
    # Group by top-level directory
    grouped_missing = {}
    for f in missing_in_target:
        top_dir = f.split(os.sep)[0]
        if top_dir not in grouped_missing:
            grouped_missing[top_dir] = []
        grouped_missing[top_dir].append(f)

    return grouped_missing

source = r"c:\Games\fodev\fonline-dev\migration-todo\fonline-2258\Server"
target = r"c:\Games\fodev\fonline-dev\PReloaded\Server"

missing = compare_full_structure(source, target)

print(f"Total missing files in target: {sum(len(v) for v in missing.values())}")

for top_dir in sorted(missing.keys()):
    files = missing[top_dir]
    print(f"\n--- {top_dir} ({len(files)} missing) ---")
    # Print first 20 missing files as examples
    for f in sorted(files)[:20]:
        print(f"  {f}")
    if len(files) > 20:
        print(f"  ... and {len(files) - 20} more")
