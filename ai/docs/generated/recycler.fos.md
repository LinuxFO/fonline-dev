---
title: recycler.fos
description: " FOnline: 2238 Rotators  recycler.fos ..."
---

# recycler.fos


FOnline: 2238
Rotators

recycler.fos


## Includes

- `_macros.fos`
- `_vals.fos`
- `debug_h.fos`
- `mapdata_h.fos`
- `recycler_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __RECYCLER__ |  |  |

## Functions

### _InitEncounterRecycler

ENCOUNTER_RECYCLER 

```angelscript
void _InitEncounterRecycler(Item& item, bool firstTime)
```

### RecycleEncounter

```angelscript
void RecycleEncounter(Location@ loc)
```

### _InitTentRecycler

TENT_RECYCLER 

```angelscript
void _InitTentRecycler(Item& item, bool firstTime)
```

### RecycleTent

```angelscript
void RecycleTent(Location@ loc)
```

### e_Recycle

Moves an item from recycler to one of target containers. 

```angelscript
uint e_Recycle(array<uint>@ data)
```

### ConnectRecycler

Makes an item a target of a recycler. 

```angelscript
void ConnectRecycler(Item@ item, uint recyclerIndex)
```

### DisconnectRecycler

Removes item from the list of the targets of a recycler. 

```angelscript
void DisconnectRecycler(Item@ item, uint recyclerIndex)
```

### PurgeRecycler

Purge over-filled recycler 

```angelscript
void PurgeRecycler(uint recyclerType, uint maxLevel, uint minLevel)
```

### RecycleMap

```angelscript
void RecycleMap(Map@ map, uint recyclerType, array<int>& itemTypes, int recycle)
```

### RecycleLocation

```angelscript
void RecycleLocation(Location@ loc, uint recyclerType, array<int>& itemTypes, int recycle)
```

### ValidRecyclerType

```angelscript
bool ValidRecyclerType(int type)
```

### GetRecycler

```angelscript
Item@ GetRecycler(int recyclerType)
```

### GetRecyclers

```angelscript
uint GetRecyclers(array<int> recyclersTypes, array<Item@>& recyclers)
```

### GetRecyclers

```angelscript
uint GetRecyclers(array<Item@>& recyclers)
```

### GetRecycledItem

```angelscript
Item@ GetRecycledItem(int recyclerType, uint16 pid)
```

### GetRecycledItems

```angelscript
uint GetRecycledItems(int recyclerType, uint16 pid, array<Item@>& items)
```

### GetRecycledItems

```angelscript
uint GetRecycledItems(int recyclerType, array<uint16> pids, array<bool>& pidFound, array<Item@>& items)
```

### encounter_recycler

Spawn Encounter Recycler... 

```angelscript
void encounter_recycler(Critter& cr, int, int, int)
```

### tent_recycler

Spawn Tent Recycler... 

```angelscript
void tent_recycler(Critter& cr, int, int, int)
```

### info

```angelscript
void info(Critter& cr, int, int, int)
```


