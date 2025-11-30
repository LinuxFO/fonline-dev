import re
from collections import defaultdict

error_file = r"c:\Games\fodev\fonline-dev\PReloaded\Server\scripts\compilation_errors.txt"

def analyze_errors():
    print("Parsing compilation_errors.txt...")
    
    try:
        with open(error_file, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
    except:
        with open(error_file, 'r', encoding='utf-16-le',errors='ignore') as f:
            content = f.read()
    
    # Split by module sections
    # Handle both literal \n (from compile_all.py) and actual newlines
    modules = re.split(r'(?:\\n|\n)===\s+(\w+)\s+===(?:\\n|\n)', content)
    
    error_patterns = defaultdict(list)
    module_errors = {}
    
    # Skip first element (before first module)
    for i in range(1, len(modules), 2):
        if i+1 >= len(modules):
            break
            
        module_name = modules[i]
        module_content = modules[i+1]
        
        errors = []
        
        # Extract error lines
        for line in module_content.split('\n'):
            if 'ERROR' in line or 'Error' in line:
                errors.append(line.strip())
        
        if errors:
            module_errors[module_name] = errors
            
            # Categorize errors
            for error in errors:
                if 'is not declared' in error or 'not declared' in error:
                    error_patterns['Undefined/Not Declared'].append(module_name)
                elif 'No matching signatures' in error:
                    error_patterns['Function Signature Mismatch'].append(module_name)
                elif "Can't implicitly convert" in error:
                    error_patterns['Type Conversion Error'].append(module_name)
                elif 'Expression must be of boolean type' in error:
                    error_patterns['Boolean Type Error'].append(module_name)
                elif 'Could not open file' in error or 'Unable to preprocess' in error:
                    error_patterns['Missing Include/File'].append(module_name)
                elif 'Identifier' in error and 'is declared' in error:
                    error_patterns['Redeclaration Error'].append(module_name)
                else:
                    error_patterns['Other/Unknown'].append(module_name)
    
    # Deduplicate
    for pattern in error_patterns:
        error_patterns[pattern] = list(set(error_patterns[pattern]))
    
    # Sort by frequency
    sorted_patterns = sorted(error_patterns.items(), key=lambda x: len(x[1]), reverse=True)
    
    print(f"\nTotal failing modules: {len(module_errors)}")
    print("\n=== ERROR PATTERNS (by frequency) ===\n")
    
    for pattern, modules in sorted_patterns:
        print(f"{pattern}: {len(modules)} modules")
        print(f"  Examples: {', '.join(modules[:5])}")
        print()
    
    # Save detailed report
    with open(r"c:\Games\fodev\fonline-dev\migration-todo\error-analysis-report.txt", "w", encoding="utf-8") as f:
        f.write("COMPILATION ERROR ANALYSIS\n")
        f.write("="*60 + "\n\n")
        
        f.write(f"Total failing modules: {len(module_errors)}\n\n")
        
        for pattern, modules in sorted_patterns:
            f.write(f"\n{pattern}: {len(modules)} modules\n")
            f.write("-" * 40 + "\n")
            for mod in sorted(modules):
                f.write(f"  - {mod}\n")
            f.write("\n")
        
        f.write("\n\nDETAILED MODULE ERRORS\n")
        f.write("="*60 + "\n\n")
        
        for module in sorted(module_errors.keys()):
            f.write(f"\n{module}:\n")
            for error in module_errors[module][:5]:  # First 5 errors per module
                f.write(f"  {error}\n")
            if len(module_errors[module]) > 5:
                f.write(f"  ... and {len(module_errors[module]) - 5} more errors\n")
    
    print("Detailed report saved to: error-analysis-report.txt")
    return sorted_patterns, module_errors

if __name__ == "__main__":
    analyze_errors()
