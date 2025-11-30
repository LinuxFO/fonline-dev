---
title: map_encounter.fos
description: " FOnline: 2238 Rotators  map_encounter.fos ..."
---

# map_encounter.fos


FOnline: 2238
Rotators

map_encounter.fos


## Includes

- `_macros.fos`
- `economy_h.fos`
- `entire.fos`
- `mapdata_h.fos`
- `town_h.fos`
- `utils_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| TRANSFER_RADIUS | `(500)` |  |
| GARBAGE_TIMEOUT | `(REAL_DAY(7))` |  |

## Functions

### map_init

```angelscript
void map_init(Map& map, bool firstTime)
```

### Scatter

 Scatters gathering items 

```angelscript
void Scatter(Map& map, uint16 pid, string@ script)
```

### HasCars

```angelscript
bool HasCars(Critter& cr, uint locid)
```

### _CritterDead

make player forget this location

```angelscript
void _CritterDead(Map& map, Critter& cr, Critter@)
```

### _CritterIn

```angelscript
void _CritterIn(Map& map, Critter& cr)
```

### _Finish

* * When encounter map is deleted, all items left out got converted to encounter's store.  note: it's commented out in map_init

```angelscript
void _Finish(Map& map, bool deleted)
```

### HideProductionFacility

 Hiding production facilities to give maps more randomness 

```angelscript
void HideProductionFacility(Map& map, array<uint>& pids, bool block)
```

### ShowProductionFacility

```angelscript
void ShowProductionFacility(Map& map, array<uint>& pids, bool block)
```

### e_DeleteEncounter

```angelscript
uint e_DeleteEncounter(array<uint>@ values)
```


