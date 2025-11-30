---
title: client_gmtools_macro.fos
description: " FOnline: 2238 Rotators  client_gmtools_macro.fos ..."
---

# client_gmtools_macro.fos


FOnline: 2238
Rotators

client_gmtools_macro.fos


## Classes

### CGMTMacro

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| name | `string` |  |  |
| lines | `array<string>` |  |  |
| all | `uint` |  |  |
| current | `uint` |  |  |
| fixcritter | `bool` |  |  |
| wait | `uint` |  |  |
| swait | `bool` |  |  |
| critter | `uint` |  | for menu |
| item | `uint` |  |  |
| hexX | `uint` |  |  |
| hexY | `uint` |  |  |

**Methods**

#### add
* * Add @e line to macro commands. 

```angelscript
void add(string line)
```


## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| GMTmacro | `array<[CGMTMacro](client_gmtools_macro.fos.md)>` |  |  |
| GMTmacro_current | `int` | `-1` | * currently processed macro (@a GMTMacro index) |

## Functions

### GMToolsAddMacro

* * Load and add macro to stack. * * @param filename		@copydoc CGMTMacro::name * @param critter		@copydoc CGMTMacro::critter * @param item			@copydoc CGMTMacro::item * @param hexX			@copydoc CGMTMacro::hexX * @param hexY			@copydoc CGMTMacro::hexY * @param fixcritter	@copydoc CGMTMacro::fixcritter * * @return @e true: macro added to @a GMTMacro * @return @e false: macro file can't opened (or empty) 

```angelscript
bool GMToolsAddMacro(string& filename, uint critter, uint item, uint hexX, uint hexY, bool fixcritter)
```

### GMToolsProcessMacros

* * @note called by: @a @e loop() -> @a @e GMToolsProcess() 

```angelscript
void GMToolsProcessMacros()
```

### GMToolsDrawMacros

* * Display informations about running/suspended macros. * * @param x		current X position * @param y		current Y position * @note                called by: @a @e render_iface() -> @a @e GMToolsDraw() * * @return new Y position 

```angelscript
int GMToolsDrawMacros(int x, int y)
```

### SendCommand

* * Final process of macro line before sending to server. * * @param command		command to execute/send (raw form) * @param critter		@copydoc CGMTMacro::critter * @param item			@copydoc CGMTMacro::item * @param hexX			@copydoc CGMTMacro::hexX * @param hexY			@copydoc CGMTMacro::hexY 

```angelscript
void SendCommand(string command, uint& critter, uint& item, uint& hexX, uint& hexY)
```

### GMToolsStopMacros

* * Stop all running macros. 

```angelscript
void GMToolsStopMacros()
```

### GetVars

* * Translate all $[Vars] in macro file to real values. * * @return Translated line. 

```angelscript
string GetVars(string raw, uint cr, uint it, uint hexX, uint hexY)
```

### ReplaceTextCalc

* * Helper function for GetVars - translate vars like @e $[Var+N] * * @note allowed operations: @e "+" @e "-" @e "*" @e "/". * @note N: @e 0 - @e 9999 * * @return real value 

```angelscript
string ReplaceTextCalc(string text, string begin, string end, int var)
```


