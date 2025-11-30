import os
import subprocess
import argparse
import sys
from pathlib import Path
import concurrent.futures

def check_file(uncrustify_path, config_path, file_path, fix_mode):
    """Run uncrustify on a single file"""
    try:
        cmd = [str(uncrustify_path), '-c', str(config_path)]
        
        if fix_mode:
            cmd.extend(['--no-backup', str(file_path)])
        else:
            cmd.extend(['--check', str(file_path)])
            
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=False
        )
        
        # Check if uncrustify command failed (e.g., not found)
        if result.returncode != 0 and result.returncode != 1:
            return {
                'file': file_path.name,
                'success': False,
                'error': True,
                'output': f"Command failed with exit code {result.returncode}: {result.stderr}"
            }
        
        # Uncrustify exit codes: 0 = clean/success, 1 = error/dirty
        return {
            'file': file_path.name,
            'success': result.returncode == 0,
            'error': False,
            'output': result.stdout + result.stderr
        }
    except FileNotFoundError:
        return {
            'file': file_path.name,
            'success': False,
            'error': True,
            'output': f"Error: '{uncrustify_path}' not found. Please install uncrustify and add it to PATH."
        }
    except Exception as e:
        return {
            'file': file_path.name,
            'success': False,
            'error': True,
            'output': str(e)
        }

def main():
    parser = argparse.ArgumentParser(description='Check or fix code style of FOnline scripts using uncrustify.')
    parser.add_argument('--uncrustify', '-u', default=r"uncrustify", help='Path to uncrustify executable')
    parser.add_argument('--config', '-c', default=r"PReloaded\Server\scripts\uncrustify.cfg", help='Path to uncrustify.cfg')
    parser.add_argument('--scripts', '-s', default=r"PReloaded\Server\scripts", help='Directory containing .fos scripts')
    parser.add_argument('--fix', action='store_true', help='Apply fixes to files (default is check-only)')
    parser.add_argument('--parallel', '-p', type=int, default=4, help='Number of parallel checks')
    parser.add_argument('--files', nargs='+', help='Specific files to check (optional)')
    
    args = parser.parse_args()
    
    # Resolve paths
    # If uncrustify is just "uncrustify", assume it's in PATH, otherwise resolve it
    if args.uncrustify == "uncrustify":
        uncrustify_path = "uncrustify"
    else:
        uncrustify_path = Path(args.uncrustify).resolve()
        if not uncrustify_path.exists():
             print(f"Error: Uncrustify not found at {uncrustify_path}")
             return

    config_path = Path(args.config).resolve()
    scripts_dir = Path(args.scripts).resolve()
    
    print(f"Uncrustify: {uncrustify_path}")
    print(f"Config: {config_path}")
    print(f"Mode: {'FIX' if args.fix else 'CHECK'}")
    
    if not config_path.exists():
        print(f"Error: Config file not found at {config_path}")
        return

    # Find files to check
    fos_files = []
    if args.files:
        # Check specific files
        for f in args.files:
            path = Path(f).resolve()
            if path.exists() and path.suffix == '.fos':
                fos_files.append(path)
            else:
                print(f"Warning: File not found or not a .fos file: {f}")
    else:
        # Check all files in scripts directory
        if not scripts_dir.exists():
            print(f"Error: Scripts directory not found at {scripts_dir}")
            return
        print(f"Scripts Directory: {scripts_dir}")
        fos_files = list(scripts_dir.rglob('*.fos'))
    
    print(f"Found {len(fos_files)} .fos files.\n")
    
    dirty_files = []
    
    print("Starting style check...")
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.parallel) as executor:
        future_to_file = {
            executor.submit(check_file, uncrustify_path, config_path, f, args.fix): f 
            for f in fos_files
        }
        
        completed = 0
        total = len(fos_files)
        
        for future in concurrent.futures.as_completed(future_to_file):
            completed += 1
            result = future.result()
            
            if result['success']:
                status = "OK"
            else:
                status = "DIRTY" if not args.fix else "FIXED"
                dirty_files.append(result)
            
            # Print progress for all files
            print(f"[{completed}/{total}] {status} {result['file']}")

    print("\n=== Style Summary ===")
    print(f"Total Files: {total}")
    print(f"Clean: {total - len(dirty_files)}")
    print(f"Dirty/Fixed: {len(dirty_files)}")
    
    if dirty_files:
        print("\n=== Files Requiring Attention ===")
        for item in dirty_files[:10]: # Show top 10
            print(f"- {item['file']}")
        if len(dirty_files) > 10:
            print(f"... and {len(dirty_files) - 10} more.")
            
        if not args.fix:
            print("\nRun with --fix to apply changes.")
        sys.exit(1)
    else:
        print("\nAll files match the style guide!")
        sys.exit(0)

if __name__ == '__main__':
    main()
