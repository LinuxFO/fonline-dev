import os
import subprocess
import argparse
import sys
from pathlib import Path
import concurrent.futures

def check_file(compiler_path, file_path):
    """Run ASCompiler on a single file"""
    try:
        # Run compiler, capture output
        result = subprocess.run(
            [compiler_path, file_path.name],
            cwd=file_path.parent,
            capture_output=True,
            text=True,
            check=False
        )
        return {
            'file': file_path.name,
            'success': result.returncode == 0,
            'output': result.stdout + result.stderr
        }
    except Exception as e:
        return {
            'file': file_path.name,
            'success': False,
            'output': str(e)
        }

def main():
    parser = argparse.ArgumentParser(description='Check compilation of FOnline scripts.')
    parser.add_argument('--compiler', '-c', default=r"PReloaded\Server\scripts\ASCompiler.exe", help='Path to ASCompiler.exe')
    parser.add_argument('--scripts', '-s', default=r"PReloaded\Server\scripts", help='Directory containing .fos scripts')
    parser.add_argument('--parallel', '-p', type=int, default=4, help='Number of parallel checks')
    
    args = parser.parse_args()
    
    compiler_path = Path(args.compiler).resolve()
    scripts_dir = Path(args.scripts).resolve()
    
    print(f"Compiler: {compiler_path}")
    print(f"Scripts Directory: {scripts_dir}")
    
    if not compiler_path.exists():
        print(f"Error: Compiler not found at {compiler_path}")
        return
    
    if not scripts_dir.exists():
        print(f"Error: Scripts directory not found at {scripts_dir}")
        return

    # Files to exclude from compilation check (e.g., headers, partial files, test files)
    EXCLUDED_FILES = {
        'worldmap_data.fos',        # Requires worldmap.fos to be compiled first
        'WitchLord.fos',            # Test file using non-existent callstack()
        'tests_astl.fos',           # Test file requiring ASTL.dll
        'sprite.fos',               # Client-side file missing interface functions
        'special_map_objects_steam.fos',  # Missing PID definitions
        'triggers_funcs.fos',       # Missing PID_TRIGGER and valid() function
        'special_map_objects_forcefield.fos',  # Missing valid() and complex dependencies
        'special_map_objects_floor.fos',  # Missing valid() and REAL_SECOND()
    }

    # Find all .fos files
    fos_files = []
    for f in scripts_dir.glob('*.fos'):
        if f.name not in EXCLUDED_FILES:
            fos_files.append(f)

    print(f"Found {len(fos_files)} .fos files (excluding {len(EXCLUDED_FILES)} files).")
    
    failed_files = []
    
    print("\nStarting compilation check...")
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.parallel) as executor:
        # Submit all tasks
        future_to_file = {
            executor.submit(check_file, str(compiler_path), f): f 
            for f in fos_files
        }
        
        # Process results as they complete
        completed = 0
        total = len(fos_files)
        
        for future in concurrent.futures.as_completed(future_to_file):
            completed += 1
            result = future.result()
            
            # Print progress
            status = "OK" if result['success'] else "FAIL"
            print(f"[{completed}/{total}] {status} {result['file']}")
            
            if not result['success']:
                failed_files.append(result)

    print("\n=== Compilation Summary ===")
    print(f"Total Files: {total}")
    print(f"Passed: {total - len(failed_files)}")
    print(f"Failed: {len(failed_files)}")
    
    if failed_files:
        print("\n=== Failed Files Details ===")
        for fail in failed_files:
            print(f"\n--- {fail['file']} ---")
            print(fail['output'].strip())
            print("-" * 30)
        sys.exit(1)
    else:
        print("\nAll files compiled successfully!")
        sys.exit(0)

if __name__ == '__main__':
    main()
