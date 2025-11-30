---
title: smart_cursor.fos
---

# smart_cursor.fos

## Includes

- `../_defines.fos`
- `../_macros.fos`
- `../ITEMPID.H`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __SMARTCURSOR__ |  |  |
| FONT_TYPE_DEFAULT | `5` |  |
| FONT_FLAG_BORDERED | `0x0200` |  |
| SMART_TEXT | `(TEXTMSG_TEXT)` |  |
| SMART_EXTRACT_ORE | `(1801)` |  |
| SMART_EXTRACT_ORE2 | `(1802)` |  |
| SMART_EXTRACT_MINERALS | `(1803)` |  |
| SMART_EXTRACT_MINERALS2 | `(1804)` |  |
| SMART_EXTRACT_URANIUM | `(1805)` |  |
| SMART_EXTRACT_GOLD | `(1806)` |  |
| SMART_EXTRACT_FIBRES | `(1807)` |  |
| SMART_SHOVEL_DUNG | `(1808)` |  |
| SMART_CHOP_WOOD | `(1809)` |  |
| SMART_DIG_GRAVE | `(1810)` |  |
| SMART_MEAT | `(1811)` |  |
| SMART_SCAVENGE | `(1812)` |  |

## Classes

### SmartCollection

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| Items | `array<uint16>` |  |  |
| Tools | `array<uint16>` |  |  |
| Slots | `array<uint8>` |  |  |
| Text | `string` |  |  |
| FuncValidate | `SmartValidate@` | `null` |  |

### SmartCursor

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| drawLayer | `uint` |  |  |
| drawInfo | `bool` |  | configurable via DrawInfo() |
| drawInfoTool | `bool` |  |  |
| drawInfoOffsetX | `int` |  |  |
| drawInfoOffsetY | `int` |  |  |
| drawInfoColor | `uint` |  |  |
| drawInfoFont | `int` |  |  |
| drawInfoFlags | `int` |  |  |
| drawTool | `bool` |  | configurable via DrawTool() |
| drawToolOffsetX | `int` |  |  |
| drawToolOffsetY | `int` |  |  |
| drawToolSize | `uint` |  |  |
| collections | `array<[SmartCollection](smart_cursor.fos.md)>` |  | collections |

**Methods**

#### DrawInfo
```angelscript
void DrawInfo( bool enable, bool toolName = true, int offsetX = 2, int offsetY = -12, uint color = 0, int font = FONT_TYPE_DEFAULT, int flags = FONT_FLAG_BORDERED )
```

#### DrawTool
```angelscript
void DrawTool( bool enable, int offsetX = 3, int offsetY = 5, uint size = 45 )
```

#### Add
```angelscript
void Add( SmartCollection& collection ) final
```

#### Draw
```angelscript
void Draw( uint layer )
```

#### Draw
```angelscript
void Draw( uint layer, CritterCl& chosen )
```

#### ClickReset
```angelscript
void ClickReset()
```

#### Click
```angelscript
bool Click( int click )
```


## Functions

### ValidateGrave

```angelscript
bool ValidateGrave( ItemCl& item, ItemCl@ tool )
```

### InitSmartCursor

```angelscript
void InitSmartCursor()
```

### SmartCursorDraw

```angelscript
void SmartCursorDraw( uint layer )
```

### SmartCursorClick

```angelscript
bool SmartCursorClick( int click )
```


