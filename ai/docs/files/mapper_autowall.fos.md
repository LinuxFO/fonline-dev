---
title: mapper_autowall.fos
description: " FOnline: 2238 Rotators  mapper_autowall.fos ..."
---

# mapper_autowall.fos


FOnline: 2238
Rotators

mapper_autowall.fos


## Includes

- `_mapper_macros.fos`
- `_defines.fos`
- `mapper_gui.fos`
- `setentry.fos`
- `strtoint_h.fos`
- `mapper_plugin_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| SECTION_NONE | `(0)` | ini sections |
| SECTION_TILE_GROUPS | `(1)` |  |
| SECTION_ROOF_GROUPS | `(2)` |  |
| SECTION_WALL_SECTIONS | `(3)` |  |
| SECTION_HORIZONTAL_INCIDENTS | `(4)` |  |
| SECTION_VERTICAL_INCIDENTS | `(5)` |  |
| SECTION_SET | `(6)` |  |
| DIK_AUTOWALL | `(DIK_A)` |  |
| WALL_NW | `(0)` |  |
| WALL_SE | `(1)` |  |
| WALL_NE | `(2)` |  |
| WALL_SW | `(3)` |  |
| AUTOWALL_WALLS | `(0)` |  |
| AUTOWALL_PATH | `(1)` |  |
| SGN_ODD | `# (x) ((x) > 0 ? ((x) % 2 == 1 ? 1 : 0) : ((-(x)) % 2 == 1 ? -1 : 0))` |  |
| SECT_WALL_H1 | `(5001)` |  |
| SECT_WALL_H2 | `(5003)` |  |
| SECT_WALL_V1 | `(5018)` |  |
| SECT_WALL_V2 | `(5015)` |  |

## Classes

### CContextButton

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| hexX | `uint16` |  |  |
| hexY | `uint16` |  |  |
| tileX | `uint16` |  |  |
| tileY | `uint16` |  |  |
| object | `MapperObject@` |  |  |

**Methods**

#### SetHex
 Assign hex 

```angelscript
void SetHex(uint16 x, uint16 y)
```

#### SetTile
```angelscript
void SetTile(uint16 x, uint16 y)
```

#### SetObject
```angelscript
void SetObject(MapperObject@ obj)
```

### CSomeButton

**Methods**

#### Click
```angelscript
void Click()
```

### CContextMenu

 Left-click context menu 

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| title | `[CButton](mapper_gui.fos.md)@` |  |  |
| some | `[CSomeButton](mapper_autowall.fos.md)@` |  |  |

**Methods**

#### Show
```angelscript
void Show(int x, int y)
```

#### MouseUp
```angelscript
bool MouseUp(int click)
```

### CAutowall

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| buttonPressed | `bool` |  |  |
| lClick | `bool` |  |  |
| autowallSet | `bool` |  |  |
| autowallUsed | `bool` |  |  |
| autowallHoriz | `bool` |  |  |
| autowallRoom | `bool` |  |  |
| autowallX | `uint16` |  |  |
| autowallY | `uint16` |  |  |
| autowallMode | `int` |  |  |
| entrynames | `dictionary` |  |  |
| entrycount | `uint` |  |  |
| horizincident | `array<uint>` |  |  |
| vertincident | `array<uint>` |  |  |
| wallset | `int` |  |  |
| context | `[CContextMenu](mapper_autowall.fos.md)@` |  |  |

**Methods**

#### Draw
```angelscript
void Draw()
```

#### MouseDown
```angelscript
bool MouseDown(int click)
```

#### MouseUp
```angelscript
bool MouseUp(int click)
```

#### MouseMove
```angelscript
void MouseMove(int x, int y)
```

#### KeyDown
```angelscript
bool KeyDown(uint8 key)
```

#### KeyUp
```angelscript
bool KeyUp(uint8 key)
```

#### InputLost
```angelscript
void InputLost()
```

#### RegisterEntry
```angelscript
bool RegisterEntry(string name, CSetEntry& entry)
```

#### GetEntry
```angelscript
CSetEntry@ GetEntry(string name)
```

#### GetEntry
```angelscript
CSetEntry@ GetEntry(uint num)
```

#### SetRoles
```angelscript
void SetRoles(array<uint> numbers, uint role)
```

#### LogEntry
```angelscript
void LogEntry(uint n)
```

#### AddIncidents
```angelscript
void AddIncidents(uint num1, uint num2, bool verti)
```

#### ParseSets
```angelscript
bool ParseSets()
```

#### SetWallset
```angelscript
void SetWallset(uint n)
```

#### SetWallsetById
```angelscript
void SetWallsetById(uint id)
```

#### SetWallsetByName
```angelscript
void SetWallsetByName(string name)
```

#### MakeWall
tile-based drawing itself

```angelscript
void MakeWall(uint16 tx, uint16 ty, uint length, uint8 type, bool justblank)
```

### CAutowallPlugin

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| autowall | `[CAutowall](mapper_autowall.fos.md)@` |  |  |

**Methods**

#### Render
```angelscript
void Render(uint layer)
```

#### MouseDown
```angelscript
bool MouseDown(int click)                { return autowall.MouseDown(click); }
```

#### MouseUp
```angelscript
bool MouseUp(int click)                  { return autowall.MouseUp(click); }
```

#### MouseMove
```angelscript
void MouseMove(int x, int y)             { autowall.MouseMove(x, y); }
```

#### KeyDown
```angelscript
bool KeyDown(uint8 key,string& keyText)  { return autowall.KeyDown(key); }
```

#### KeyUp
```angelscript
bool KeyUp(uint8 key,string& keyText)    { return autowall.KeyUp(key); }
```

#### InputLost
```angelscript
void InputLost()                         { autowall.InputLost(); }
```

#### Loop
```angelscript
void Loop()                              {}
```

#### Message
```angelscript
bool Message(string&)                    { return false; }
```

#### RenderMap
```angelscript
void RenderMap()                         {}
```


## Functions

### RegisterAutowall

```angelscript
void RegisterAutowall()
```


