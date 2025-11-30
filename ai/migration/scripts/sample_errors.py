import subprocess
import re

# Sample 15 failing modules to identify error patterns
sample_modules = [
    "worldmap_data",
    "weather_rain_table",
    "map_vcity_bank_vault",
    "map_vault13",
    "quest_mb",
    "quest_tanker",
    "npc_schedules",
    "prices_server_client",
    "mob_wave_data",
    "multihex_data",
    "special_map_objects_floor",
    "sprites",
    "tests_astl",
    "mapper_generators",
    "scypior_radiation"
]

def compile_and_analyze():
    compiler = r"c:\Games\fodev\fonline-dev\PReloaded\Server\scripts\ASCompiler.exe"
    prep_file = r"c:\Games\fodev\fonline-dev\PReloaded\Server\scripts\prep.txt"
    script_dir = r"c:\Games\fodev\fonline-dev\PReloaded\Server\scripts"
    error_patterns = {}
    
    print("Compiling sample modules to identify error patterns...\n")
    
    for module in sample_modules:
        print(f"Compiling {module}...")
        fos_file = f"{script_dir}\\{module}.fos"
        cmd = [compiler, fos_file, "-p", prep_file, "-d", "__SERVER"]
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if "Error" in result.stdout or "ERROR" in result.stdout:
            errors = []
            for line in result.stdout.split('\n'):
                if 'ERROR' in line or 'Error' in line:
                    errors.append(line.strip())
            
            error_patterns[module] = errors
            
            # Print first 3 errors
            print(f"  Errors found:")
            for err in errors[:3]:
                print(f"    {err}")
            if len(errors) > 3:
                print(f"    ... and {len(errors) - 3} more")
            print()
    
    # Categorize errors
    print("\n=== ERROR CATEGORIZATION ===\n")
    
    categories = {
        "Missing Class/Type": [],
        "Undefined Constant": [],
        "Undefined Function": [],
        "API Signature Mismatch": [],
        "Type Conversion": [],
        "Boolean Type": [],
        "Missing Include": [],
        "Other": []
    }
    
    for module, errors in error_patterns.items():
        for error in errors:
            if "is not a data type" in error or "is not declared" in error and "class" in error.lower():
                categories["Missing Class/Type"].append((module, error))
            elif "is not declared" in error:
                categories["Undefined Constant"].append((module, error))
            elif "No matching signatures" in error:
                categories["API Signature Mismatch"].append((module, error))
            elif "Can't implicitly convert" in error:
                categories["Type Conversion"].append((module, error))
            elif "Expression must be of boolean type" in error:
                categories["Boolean Type"].append((module, error))
            elif "Could not open file" in error:
                categories["Missing Include"].append((module, error))
            else:
                categories["Other"].append((module, error))
    
    for category, items in categories.items():
        if items:
            print(f"{category}: {len(items)} occurrences")
            # Show 2 examples
            for module, error in items[:2]:
                print(f"  {module}: {error[:80]}...")
            print()
    
    return categories

if __name__ == "__main__":
    compile_and_analyze()
