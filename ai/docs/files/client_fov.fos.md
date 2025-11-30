---
title: client_fov.fos
description: " FOnline: 2238 Rotators  client_fov.fos ..."
---

# client_fov.fos


FOnline: 2238
Rotators

client_fov.fos


## Includes

- `client_gui_h.fos`
- `_macros.fos`
- `polygon_h.fos`
- `_client_defines.fos`
- `_globalvars.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| MS_FOV_BORDER | `(0x77BBBBBB)` |  |

## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| Triangles | `array<uint16>` |  | bool FogEnabled=false; int FogColor=int(0xA0000000); |
| MapChanged | `bool` | `true` |  |
| LastDir | `uint8` | `uint8(-1)` |  |
| LastHexX | `uint16` | `uint16(-1)` |  |
| LastHexY | `uint16` | `uint16(-1)` |  |
| LastSight | `uint` | `uint(-1)` |  |

## Functions

### DrawFog

```angelscript
void DrawFog()
```

### RebuildFog

```angelscript
void RebuildFog(CritterCl& cr)
```

### RemoveDuplicates

helper

```angelscript
void RemoveDuplicates(array<uint16>& hexes)
```

### EnumHexes

helper

```angelscript
void EnumHexes(array<uint16>& hexes)
```

### GetFovHexes

```angelscript
uint GetFovHexes(uint16 cX, uint16 cY, uint8 cDir, uint cSight, uint maxRange, bool ccw, array<uint16>& hexes)
```

### GetRelativeDirModifier

```angelscript
uint8 GetRelativeDirModifier(uint8 dir)
```

### CalculateFovSextantHexes

```angelscript
void CalculateFovSextantHexes(uint16 x, uint16 y, uint8 dir, uint sight, uint maxRange, bool ccw, array<uint16>& hexes)
```

### DrawMsFov

```angelscript
void DrawMsFov()
```

### DrawCustomBorder

```angelscript
void DrawCustomBorder()
```


