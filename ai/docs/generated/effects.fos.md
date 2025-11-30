---
title: effects.fos
description: " FOnline: 2238 Rotators  effects.fos ..."
---

# effects.fos


FOnline: 2238
Rotators

effects.fos


## Includes

- `_macros.fos`
- `world_common_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| QUAKE_NOISE | `(8)` | Default values |
| QUAKE_TIME | `(800)` |  |

## Functions

### FlushScreen

```angelscript
void FlushScreen(Critter& cr, bool fadeOut, uint timeMs)
```

### FlushScreen

```angelscript
void FlushScreen(Critter& cr, uint fromColor, uint toColor, uint timeMs)
```

### FlushScreen

```angelscript
void FlushScreen(Map& map, bool fadeOut, uint timeMs)
```

### FlushScreen

```angelscript
void FlushScreen(Map& map, uint fromColor, uint toColor, uint timeMs)
```

### QuakeScreen

```angelscript
void QuakeScreen(Critter& cr)
```

### QuakeScreen

```angelscript
void QuakeScreen(Critter& cr, uint noise, uint timeMs)
```

### QuakeScreen

```angelscript
void QuakeScreen(Map& map)
```

### QuakeScreen

```angelscript
void QuakeScreen(Map& map, uint noise, uint timeMs)
```

### TattooSignLights

```angelscript
void TattooSignLights(Item& item, bool firstTime)
```

### e_SwitchSign

```angelscript
uint e_SwitchSign(array<uint>@ values)
```


