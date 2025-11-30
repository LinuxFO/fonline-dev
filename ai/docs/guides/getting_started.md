# Getting Started with FOnline Development Tools

This guide explains how to use the Python tooling scripts in the `ai/scripts` directory to analyze, check, and improve FOnline AngelScript code.

## Available Tools

### 1. Code Compilation Check (`check_compilation.py`)

Automatically compiles all `.fos` files to identify syntax errors and missing dependencies.

**Usage:**
```bash
# Check all files
python ai/scripts/check_compilation.py

# Specify custom paths
python ai/scripts/check_compilation.py --compiler path/to/ASCompiler.exe --scripts path/to/scripts
```

**What it does:**
- Scans for all `.fos` files in `PReloaded/Server/scripts`
- Compiles each file using `ASCompiler.exe`
- Reports compilation errors with file names and error details
- Excludes known problematic files (tests, client-side files, etc.)

**Exit codes:**
- `0`: All files compiled successfully
- `1`: One or more files failed to compile

---

### 2. Code Style Check (`check_style.py`)

Checks and optionally fixes code style issues using Uncrustify.

**Usage:**
```bash
# Check all files (report only)
python ai/scripts/check_style.py

# Check specific file
python ai/scripts/check_style.py --files PReloaded/Server/scripts/utils.fos

# Fix all files automatically
python ai/scripts/check_style.py --fix

# Fix specific file
python ai/scripts/check_style.py --files PReloaded/Server/scripts/utils.fos --fix
```

**What it does:**
- Scans `.fos` files in `PReloaded/Server/scripts` recursively
- Checks code style against `uncrustify.cfg` configuration
- Can automatically apply style fixes with `--fix` flag
- Reports which files need attention

**Requirements:**
- `uncrustify` must be installed and in PATH (or specify path with `--uncrustify`)
- Configuration file exists at `PReloaded/Server/scripts/uncrustify.cfg`

---

### 3. Unit Test Runner (`run_tests.py`)

Runs AngelScript unit tests using the TestRunner framework.

**Usage:**
```bash
# Run unit tests
python ai/scripts/run_tests.py
```

**What it does:**
- Currently verifies that `TestRunner.fos` compiles correctly
- Future: Will execute unit tests in a headless server mode

**Writing Tests:**
Create test files in `PReloaded/Server/scripts/tests/`:

```cpp
#include "TestRunner.fos"
#include "utils_h.fos"

class Test_MyFunction : ITest
{
    string@ GetName() { return "Test_MyFunction"; }
    
    void Run(TestRunner@ runner)
    {
        // Your test assertions
        runner.Assert(true, "This should pass");
        runner.AssertEquals(2 + 2, 4, "Math works");
    }
}

void RunAllTests()
{
    TestRunner@ runner = TestRunner();
    Test_MyFunction@ test = Test_MyFunction();
    runner.AddTest(test);
    runner.RunAll();
    runner.LogResults();
}
```

---

### 4. Documentation Generation (`generate_docs.py`)

Generates Markdown documentation from AngelScript source files.

**Usage:**
```bash
# Generate docs for all files
python ai/scripts/generate_docs.py

# Specify custom paths
python ai/scripts/generate_docs.py --source path/to/scripts --dest path/to/docs
```

**What it does:**
- Parses `.fos` files to extract functions, classes, defines, and constants
- Generates individual Markdown files for each script
- Creates an index file with links to all documentation
- Outputs to `ai/docs/files/`

---

### 5. Script Analysis (`analyze_scripts.py`)

Analyzes documentation to extract metadata and statistics.

**Usage:**
```bash
python ai/scripts/analyze_scripts.py
```

**What it does:**
- Reads generated Markdown documentation
- Extracts metadata (functions, classes, includes, etc.)
- Categorizes scripts by naming patterns
- Outputs `analysis.json` with detailed statistics

---

### 6. Overview Generation (`generate_overview.py`)

Creates high-level overview pages from analysis data.

**Usage:**
```bash
python ai/scripts/generate_overview.py
```

**What it does:**
- Reads `analysis.json`
- Generates category-specific overview pages
- Creates metrics dashboard
- Outputs to `ai/docs/`

---

## Workflow Example

Here's a typical workflow for improving code quality:

### 1. Check for Compilation Errors
```bash
python ai/scripts/check_compilation.py
```
Fix any errors reported before proceeding.

### 2. Apply Code Style
```bash
# Check what needs fixing
python ai/scripts/check_style.py

# Apply fixes
python ai/scripts/check_style.py --fix
```

### 3. Run Unit Tests
```bash
python ai/scripts/run_tests.py
```

### 4. Update Documentation
```bash
python ai/scripts/generate_docs.py
python ai/scripts/analyze_scripts.py
python ai/scripts/generate_overview.py
```

---

## Configuration

### Excluded Files

Some files are excluded from compilation checks (`check_compilation.py`):
- `worldmap_data.fos` - Partial file requiring other files
- `WitchLord.fos` - Test file with non-standard functions
- `tests_astl.fos` - Test file requiring external DLL
- `sprite.fos` - Client-side file
- `special_map_objects_steam.fos` - Missing dependencies
- `triggers_funcs.fos` - Partial file

### Uncrustify Configuration

Code style is defined in `PReloaded/Server/scripts/uncrustify.cfg`. Key settings:
- 4-space indentation
- LF line endings
- Specific brace and spacing rules

---

## Troubleshooting

### `uncrustify` not found
Install Uncrustify from https://github.com/uncrustify/uncrustify or specify path:
```bash
python ai/scripts/check_style.py --uncrustify path/to/uncrustify.exe
```

### Compilation errors in known-good files
Some files may have intentional errors or require specific compilation order. Check if the file is in the exclusion list.

### Unicode errors on Windows
The scripts should handle Unicode correctly. If you encounter issues, ensure your terminal supports UTF-8.

---

## Next Steps

- Expand unit test coverage by creating more test files
- Review and update `uncrustify.cfg` if style rules need adjustment
- Set up continuous integration to run these checks automatically
- Create more comprehensive documentation for critical systems
