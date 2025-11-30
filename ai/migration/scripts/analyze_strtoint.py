import os
import re

scripts_dir = r"c:\Games\fodev\fonline-dev\PReloaded\Server\scripts"

def find_strtoint_usage():
    print("Scanning for StrToInt usage...")
    
    files_with_strtoint = []
    pattern = re.compile(r'StrToInt\s*\([^)]+\)')
    
    for filename in os.listdir(scripts_dir):
        if not filename.endswith('.fos'):
            continue
            
        filepath = os.path.join(scripts_dir, filename)
        
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                
            matches = pattern.findall(content)
            if matches:
                files_with_strtoint.append({
                    'file': filename,
                    'matches': matches,
                    'count': len(matches)
                })
        except Exception as e:
            print(f"Error reading {filename}: {e}")
            
    print(f"\nFound StrToInt usage in {len(files_with_strtoint)} files:")
    for item in sorted(files_with_strtoint, key=lambda x: x['count'], reverse=True)[:20]:
        print(f"  {item['file']}: {item['count']} occurrences")
        for match in item['matches'][:3]:
            print(f"    {match}")
            
    return files_with_strtoint

if __name__ == "__main__":
    find_strtoint_usage()
