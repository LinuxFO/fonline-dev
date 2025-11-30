---
title: mapper_tilemap.fos
description: " FOnline: 2238 Rotators  mapper_tilemap.fos ..."
---

# mapper_tilemap.fos


FOnline: 2238
Rotators

mapper_tilemap.fos


## Includes

- `_mapper_defines.fos`
- `_macros.fos`
- `mapper_plugin_h.fos`
- `_colors.fos`
- `mapper_utils_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| COLOR_NORMAL | `(0x60FF0000)` |  |
| COLOR_WIDE | `(0x6000FF00)` |  |

## Classes

### Tile

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| Hash | `int` |  |  |

**Methods**

#### Draw
```angelscript
void Draw(uint16 hx)
```

### CTileMapPlugin

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| Active | `bool` |  |  |

**Methods**

#### Render
```angelscript
void Render(uint layer)
```

#### Init
```angelscript
bool Init()
```

#### RenderMap
```angelscript
void RenderMap()                 {}
```

#### MouseDown
```angelscript
bool MouseDown(int)              { return false; }
```

#### MouseUp
```angelscript
bool MouseUp(int)                { return false; }
```

#### MouseMove
```angelscript
void MouseMove(int, int)         {}
```

#### KeyDown
```angelscript
bool KeyDown(uint8,string&)      { return false; }
```

#### KeyUp
```angelscript
bool KeyUp(uint8,string&)        { return false; }
```

#### InputLost
```angelscript
void InputLost()                 {}
```

#### Loop
```angelscript
void Loop()                      {}
```

#### Message
```angelscript
bool Message(string&)            { return false; }
```


## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| offX | `int` | `0` |  |
| offY | `int` | `0` |  |
| Plugin | `[CTileMapPlugin](mapper_tilemap.fos.md)@` | `null` |  |
| Init | `bool` | `false` |  |

## Functions

### DrawHexRect2

```angelscript
void DrawHexRect2(uint16 x1, uint16 y1, uint16 x2, uint16 y2, int color, uint16 offsetX)
```

### DrawHexRect

```angelscript
void DrawHexRect(uint16 x1, uint16 y1, uint16 x2, uint16 y2, int color)
```

### UpdateOffsets

```angelscript
void UpdateOffsets()
```

### FillDataHex

```angelscript
void FillDataHex(array<int>& data, uint16 x, uint16 y, int& index, int color)
```

### RegisterTilemap

```angelscript
void RegisterTilemap()
```

### toggle

```angelscript
string toggle(string)
```


