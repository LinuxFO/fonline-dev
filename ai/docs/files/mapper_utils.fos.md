---
title: mapper_utils.fos
description: " FOnline: 2238 Rotators  mapper_utils.fos ..."
---

# mapper_utils.fos


FOnline: 2238
Rotators

mapper_utils.fos


## Includes

- `_mapper_defines.fos`
- `_mapper_macros.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __MAPPER_UTILS__ |  |  |

## Functions

### GetActiveMap

Returns handle to active map 

```angelscript
MapperMap@ GetActiveMap()
```

### HexOffset

Returns an offset between hexes in some direction, in screen pixels. There might be a better way to do it... 

```angelscript
void HexOffset(uint8 dir, int& x, int& y)
```

### GetHexWidth

```angelscript
uint GetHexWidth()
```

### GetZoom

Returns current zoom level, in %. Not very precise :P 

```angelscript
uint GetZoom()
```

### GetMonitorHexSigh

"Patch" 

```angelscript
bool GetMonitorHexSigh(int x, int y, uint16& hx, uint16& hy, bool ignoreInterface = false)
```


