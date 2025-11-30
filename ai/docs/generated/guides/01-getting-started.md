# Tutorial 1: Getting Started

This guide will walk you through creating your first FOnline script that prints "Hello FOnline!" to the game console.

## Prerequisites

- FOnline server installed and configured
- Text editor (VS Code, Notepad++, or any code editor)
- Basic understanding of file navigation

## Step-by-Step Guide

### Step 1: Create the Script File

1. Navigate to your FOnline scripts directory:
   ```
   PReloaded/Server/scripts/
   ```

2. Create a new file named `hello_world.fos`

3. Open the file in your text editor

### Step 2: Write the Script

Add the following code to `hello_world.fos`:

```angelscript
// hello_world.fos
// A simple "Hello FOnline!" script

// This function will be called when the server starts
void HelloWorld()
{
    Log("Hello FOnline!");
}
```

**Code Explanation:**
- `//` - Comments (ignored by the script engine)
- `void HelloWorld()` - Function declaration (returns nothing)
- `Log("Hello FOnline!");` - Prints text to the server console
- `{ }` - Code block containing the function body

### Step 3: Register the Script

To make the script available to the server, you need to register it in the main configuration.

**Option A: Call from main.fos (Recommended for testing)**

1. Open `PReloaded/Server/scripts/main.fos`

2. Add the include at the top of the file:
   ```angelscript
   #include "hello_world.fos"
   ```

3. Find the `start()` function (called when server starts)

4. Add a call to your function inside `start()`:
   ```angelscript
   bool start()
   {
       // ... existing code ...
       
       HelloWorld();  // Call our new function
       
       // ... rest of the code ...
       return true;
   }
   ```

**Option B: Create a standalone module (Advanced)**

If you want to make it a proper module, add module binding in `scripts.cfg`:

1. Open `Server/scripts.cfg`

2. Add your script to the module list:
   ```
   @ server module hello_world
   ```

3. Modify your script to use module initialization:
   ```angelscript
   void ModuleInit()
   {
       Log("Hello FOnline!");
   }
   ```

### Step 4: Test the Script

1. **Start the FOnline server**
   - Run `FOnlineServer.exe` (or your server executable)

2. **Check the console output**
   - Look for the line: `Hello FOnline!`
   - It should appear in the server console window

3. **Check the log file**
   - Open `Server/Logs/FOnline.log`
   - Search for "Hello FOnline!"

### Step 5: Verify Success

If everything worked correctly, you should see:

```
[12:34:56] Hello FOnline!
```

The timestamp will vary based on when the server started.

## Common Issues & Solutions

### Issue 1: Script not found
**Error**: `Script 'hello_world.fos' not found`

**Solution**: 
- Check that the file is in `PReloaded/Server/scripts/`
- Verify the filename is exactly `hello_world.fos`
- Make sure you included it in `main.fos`

### Issue 2: Syntax error
**Error**: `Parse error in hello_world.fos`

**Solution**:
- Check for missing semicolons `;`
- Verify brackets `{ }` are balanced
- Make sure function name matches exactly

### Issue 3: Function not called
**Error**: No output in console

**Solution**:
- Verify you added `HelloWorld();` in `start()` function
- Check that the server actually started successfully
- Look in the log file instead of console

## Next Steps

Now that you have a working script, try these exercises:

### Exercise 1: Multiple Messages
Modify the function to print multiple lines:

```angelscript
void HelloWorld()
{
    Log("Hello FOnline!");
    Log("This is my first script!");
    Log("Server is running...");
}
```

### Exercise 2: Add Parameters
Create a function that takes a parameter:

```angelscript
void PrintMessage(string message)
{
    Log(message);
}

void HelloWorld()
{
    PrintMessage("Hello FOnline!");
    PrintMessage("Welcome to scripting!");
}
```

### Exercise 3: Use Variables
Store and print variables:

```angelscript
void HelloWorld()
{
    string serverName = "My FOnline Server";
    int playerCount = 0;
    
    Log("Server: " + serverName);
    Log("Players online: " + playerCount);
}
```

## Understanding the Basics

### AngelScript Language
FOnline uses **AngelScript**, a scripting language similar to C++/JavaScript:

- **Statically typed**: Variables must have a type (`int`, `string`, `bool`)
- **Semicolons required**: End statements with `;`
- **Case-sensitive**: `HelloWorld` ≠ `helloworld`

### Common Data Types

| Type | Description | Example |
|:-----|:------------|:--------|
| `int` | Integer number | `42`, `-10`, `0` |
| `uint` | Unsigned integer | `100`, `0` |
| `float` | Decimal number | `3.14`, `0.5` |
| `string` | Text | `"Hello"`, `"FOnline"` |
| `bool` | True/False | `true`, `false` |

### Useful Functions

| Function | Purpose | Example |
|:---------|:--------|:--------|
| `Log(string)` | Print to console | `Log("Debug info");` |
| `Random(min, max)` | Random number | `Random(1, 100);` |
| `GetFullSecond()` | Current time | `GetFullSecond();` |

## Further Learning

**Recommended reading order:**
1. [main.fos](../main.fos.md) - Server entry point and event handlers
2. [utils.fos](../utils.fos.md) - Common utility functions
3. [_defines.fos](../_defines.fos.md) - Global constants and definitions
4. [_macros.fos](../_macros.fos.md) - Macro definitions

**Documentation sections:**
- [Core & Utilities](../categories/core.md) - Essential scripts
- [Browse all categories](../index.md) - Full documentation index

## Complete Example Script

Here's a more complete example with comments:

```angelscript
// hello_world.fos
// Author: Your Name
// Description: My first FOnline script

// Include necessary headers
#include "_macros.fos"

// Global variable (accessible throughout the script)
string g_ServerName = "My FOnline Server";

// Function: Initialize and print welcome message
void HelloWorld()
{
    // Print header
    Log("================================");
    Log("  " + g_ServerName);
    Log("================================");
    
    // Print welcome message
    Log("Hello FOnline!");
    Log("Server started successfully!");
    
    // Print current time
    uint currentTime = GetFullSecond();
    Log("Server time: " + currentTime);
    
    // Print footer
    Log("================================");
}

// Function: Print custom message
void PrintCustomMessage(string message)
{
    Log("[CUSTOM] " + message);
}
```

**To use this script:**
1. Save as `hello_world.fos`
2. Include in `main.fos`: `#include "hello_world.fos"`
3. Call in `start()`: `HelloWorld();`
4. Start the server and check the console!

---

**Congratulations!** You've created your first FOnline script. Keep experimenting and exploring the documentation to learn more!

[← Back to Documentation Index](../index.md)
