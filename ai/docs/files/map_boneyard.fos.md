---
title: map_boneyard.fos
description: " FOnline: 2238 Rotators  map_boneyard.fos ..."
---

# map_boneyard.fos


FOnline: 2238
Rotators

map_boneyard.fos


## Includes

- `_macros.fos`
- `_maps.fos`
- `economy_h.fos`
- `reinforcements_h.fos`

## Functions

### map_init

```angelscript
void map_init(Map& map, bool firstTime)
```

### _Finish

```angelscript
void _Finish(Map& map, bool deleted)
```

### s_WaterPump

```angelscript
bool s_WaterPump(Critter& player, Scenery& table, int skill, Item@ item)
```

### s_Well

Player trying to repair the well instead of the water pump will be informed by Montag that he is doing something wrong. 

```angelscript
bool s_Well(Critter& player, Scenery& table, int skill, Item@ item)
```


