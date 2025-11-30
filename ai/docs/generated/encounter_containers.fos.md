---
title: encounter_containers.fos
description: " FOnline: 2238 Rotators  encounter_containers.fos ..."
---

# encounter_containers.fos


FOnline: 2238
Rotators

encounter_containers.fos


## Includes

- `_entires.fos`
- `_macros.fos`
- `entire.fos`
- `spawner_container_h.fos`
- `traps_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| EC_TYPE_NONE | `(0)` |  |
| EC_TYPE_CONTAINER | `(1)` |  |
| EC_TYPE_GRAVE | `(2)` |  |
| EC_BASE_CHANCE | `(40)` |  |
| EC_CONT_LOW_THRESHOLD | `(7)` |  |
| EC_CONT_MED_THRESHOLD | `(9)` |  |
| EC_CONT_HIGH_THRESHOLD | `(10)` |  |
| EC_GRAVE_LOW_THRESHOLD | `(8)` |  |
| EC_GRAVE_HIGH_THRESHOLD | `(10)` |  |
| EC_FLAG_SPAWN | `(0x1)` |  |
| EC_FLAG_FILL | `(0x2)` |  |
| ED_TRAPS_RADIUS | `(5)` |  |

## Functions

### GetContainerType

```angelscript
uint GetContainerType(Map& map)
```

### GetEntire

```angelscript
Entire@ GetEntire(Map& map, uint type)
```

### GetContainerPid

```angelscript
uint16 GetContainerPid(uint cont)
```

### GetSpawnerType

```angelscript
uint GetSpawnerType(uint type)
```

### GetTrapsLevel

```angelscript
uint GetTrapsLevel(uint spawner)
```

### RollFlags

```angelscript
uint RollFlags(uint type)
```

### MakeTraps

```angelscript
void MakeTraps(Map& map, uint16 hx, uint16 hy, int trapslevel)
```

### AddEncounterContainers

It is of utmost importance that this function never fails to execute

```angelscript
void AddEncounterContainers(Map@ map, array<Critter@>@ critters)
```


