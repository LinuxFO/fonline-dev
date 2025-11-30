---
title: mapper_main.fos
description: " FOnline: 2238 Rotators  mapper_main.fos ..."
---

# mapper_main.fos


FOnline: 2238
Rotators

mapper_main.fos


## Includes

- `_mapper_defines.fos`
- `config_h.fos`
- `_macros.fos`
- `ITEMPID.H`
- `strtoint_h.fos`
- `mapper_plugin_h.fos`
- `mapper_utils_h.fos`
- `_colors.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| CHECK_PARAM | `\` | index operator, damnit |
| TRY_ASSIGN_PARAM | `# (__s) if(cr.__s == -1) { cr.__s = param; return true; }` |  |

## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| ShowDoorScript | `bool` | `false, ShowContainerScript = false` |  |

## Functions

### new_instance

///////////////////////////////////////////////////////////////////////////////////////////////// Call on new mapper instance creating. Return true to handle event and close new instance or return false to allow creating of new mapper instance.

```angelscript
bool new_instance(string commandLine)
```

### start

///////////////////////////////////////////////////////////////////////////////////////////////// Call on mapper loaded.

```angelscript
void start()
```

### finish

```angelscript
void finish()
```

### InitializePlugins

```angelscript
void InitializePlugins()
```

### _SetTab

helper

```angelscript
void _SetTab(int tab, string& name, array<uint16>@ pids)
```

### InitializeTabs

```angelscript
void InitializeTabs()
```

### LoadTabsConfig

```angelscript
void LoadTabsConfig()
```

### loop

///////////////////////////////////////////////////////////////////////////////////////////////// Main loop function. Returned time of next call in milliseconds.

```angelscript
uint loop()
```

### console_message

///////////////////////////////////////////////////////////////////////////////////////////////// Call on console message. Return true to disable engine processing.

```angelscript
bool console_message(string& message)
```

### render_iface

///////////////////////////////////////////////////////////////////////////////////////////////// Render interface function. You can use Draw* functions only there. Layer specification: 0 Game map 1 Mapper interface 2 Console, Messbox 3 Mapper object interface 4 Cursor 5

```angelscript
void render_iface(uint layer)
```

### render_map

///////////////////////////////////////////////////////////////////////////////////////////////// Render map function. You can use DrawMap* functions only there. This drawing before 1 iface layer.

```angelscript
void render_map()
```

### mouse_down

///////////////////////////////////////////////////////////////////////////////////////////////// Mouse behaviours. Click states look in _client_defines.fos, Mouse click states. Return true to disable engine events.

```angelscript
bool mouse_down(int click)
```

### mouse_up

```angelscript
bool mouse_up(int click)
```

### mouse_move

```angelscript
void mouse_move(int x, int y)
```

### key_down

///////////////////////////////////////////////////////////////////////////////////////////////// Keyboard behaviours. Key codes look in _mapper_defines.fos DirectInput keyboard scan codes. Return true to disable engine events.

```angelscript
bool key_down(uint8 key,string& keyText)
```

### key_up

```angelscript
bool key_up(uint8 key,string& keyText)
```

### input_lost

///////////////////////////////////////////////////////////////////////////////////////////////// Called on mouse/keyboard input lost (alt-tab, minimize, lost focus).

```angelscript
void input_lost()
```

### DrawMenu

```angelscript
void DrawMenu()
```

### DrawDescForItems

```angelscript
void DrawDescForItems()
```

### cmc

```angelscript
string cmc(string str)
```

### ClearTiles

Keep only one tile per hex

```angelscript
string ClearTiles(string str)
```

### MapTime

Map parameters

```angelscript
string MapTime(string str)
```

### MapNoLogOut

```angelscript
string MapNoLogOut(string str)
```

### MapScriptModule

```angelscript
string MapScriptModule(string str)
```

### MapScriptFunc

```angelscript
string MapScriptFunc(string str)
```

### AssignParam

```angelscript
bool AssignParam(MapperObject& cr, int param)
```

### AddParam

```angelscript
string AddParam(string str)
```

### ChangeParams

```angelscript
string ChangeParams(string str)
```

### FixWorldEntires

```angelscript
string FixWorldEntires(string args)
```

### FixMapEntires

```angelscript
string FixMapEntires(string args)
```

### FixEntires

```angelscript
string FixEntires(string num)
```

### PortMap

```angelscript
string PortMap(string)
```

### TrimToFileName

```angelscript
void TrimToFileName(string@ s)
```

### RenderTileName

```angelscript
void RenderTileName()
```

### RenderZoom

```angelscript
void RenderZoom()
```

### proc

```angelscript
string proc(string s)
```

### goto

```angelscript
string goto (string s)
```

### getsize

```angelscript
string getsize(string)
```

### chopchopchop

```angelscript
string chopchopchop(string)
```

### FixLockers

```angelscript
string FixLockers(string)
```

### CleanTech

```angelscript
string CleanTech(string s)
```

### RLD

```angelscript
string RLD(string)
```

### ReplaceHex

```angelscript
string ReplaceHex(string s)
```

### ClearClones

```angelscript
string ClearClones( string str )
```


