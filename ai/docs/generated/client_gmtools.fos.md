---
title: client_gmtools.fos
description: " FOnline: 2238 Rotators  client_gmtools.fos ..."
---

# client_gmtools.fos


FOnline: 2238
Rotators

client_gmtools.fos


## Includes

- `gmtools_h.fos`
- `client_utils_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __CLIENT_GMTOOLS__ |  |  |
| __CLIENT |  |  |

## Classes

### CGMTConfig

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| Enabled | `bool` |  |  |
| Access | `uint` |  |  |
| AccessCheck | `uint` |  |  |
| OSD | `uint` |  |  |
| Draw | `bool` |  |  |
| Menu | `bool` |  |  |
| Motto | `string` |  |  |
| ChatX | `uint` |  |  |
| ChatY | `uint` |  |  |
| ChatDelay | `uint` |  |  |
| ChatBorder | `uint` |  |  |
| ButtonsFile | `string` |  |  |
| CritterInfo | `uint` |  |  |
| ItemInfo | `uint` |  |  |
| MapInfo | `uint` |  |  |
| LocationInfo | `uint` |  |  |
| LastMapPid | `int` |  |  |
| LastLocationPid | `int` |  |  |
| Possess | `uint` |  |  |
| CSCdebug | `bool` |  | internal |


## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| GMTconfig | `[CGMTConfig](client_gmtools.fos.md)` |  |  |

## Functions

### GMToolsLoadConfig

```angelscript
void GMToolsLoadConfig()
```

### GMToolsProcess

* * Process all sub-packages. * * @note called by: @a @e loop() * * @sa GMToolsProcessChat, GMToolsProcessMacros * @sa GMToolsDraw 

```angelscript
void GMToolsProcess()
```

### GMToolsProcessKey

```angelscript
bool GMToolsProcessKey(uint8 key)
```

### GMToolsDraw

* * Call all sub-packages Draw* functions * * @param layer * @param mouseX * @param mouseY * * @note called by @a @e render_iface() * * @sa GMToolsDrawChat, GMToolsDrawMacros * @sa GMToolsProcess 

```angelscript
void GMToolsDraw(uint layer, int mouseX, int mouseY)
```

### check_timers

```angelscript
void check_timers()
```

### draw

* * Draw @e text on monitor at position @e x,y using default color and size * * @param text	text to display * @param x		X position * @param y		Y position * * @return new Y position 

```angelscript
int draw(string& text, int x, int y)
```

### draw

```angelscript
int draw(string& text, int x, int y, int y_fix)
```

### draw

```angelscript
int draw(string& text, int x, int y, int y_fix, uint color)
```

### draw_critterinfo_screen

```angelscript
void draw_critterinfo_screen(CritterCl& critter)
```

### DisableGMTools

* * Disable GM Tools, reset access, clean last visited map/location PIDs, etc. 

```angelscript
void DisableGMTools()
```

### GMToolsCommand

* * @note called by @e out_message() * @note grab messages starting with: @e "~gmtools" @e "~getaccess" @e "@" 

```angelscript
int GMToolsCommand(string& message)
```

### GMToolsPossess

* * @return ID of currently possessed critter, or 0 

```angelscript
int GMToolsPossess()
```

### GMToolsPossess

* * Possess given critter and save its ID. * * @param critter	ID of critter that should be possessed * * @return @e true:  success * @return @e false: @a GetCritter() failed 

```angelscript
bool GMToolsPossess(int critter)
```

### GMToolsPossessRotate

```angelscript
void GMToolsPossessRotate(bool a)
```

### GMToolsUnPossess

```angelscript
void GMToolsUnPossess()
```

### GMToolsAccess

* * Check if client can use GMT * @note for @e client_main.fos 

```angelscript
bool GMToolsAccess()
```

### GMToolsMenu

* * Check if client can use GMT menu * @note for @e client_main.fos 

```angelscript
bool GMToolsMenu()
```


