---
title: map_modoc.fos
description: " FOnline: 2238 Rotators  map_modoc.fos ..."
---

# map_modoc.fos


FOnline: 2238
Rotators

map_modoc.fos


## Includes

- `_macros.fos`
- `_town.fos`
- `mapdata_h.fos`
- `logging_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| NORMAL_ENTRANCE | `(0)` |  |
| SIDE_ENTRANCE | `(1)` |  |

## Functions

### map_init

```angelscript
void map_init(Map& map, bool firstTime)
```

### _Finish

```angelscript
void _Finish(Map& map, bool deleted)
```

### entrance_modoc

Will be called for every entrance.

```angelscript
bool entrance_modoc(array<Critter@>& critters, uint8 entrance)
```


