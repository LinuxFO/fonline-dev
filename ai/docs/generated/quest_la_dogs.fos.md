---
title: quest_la_dogs.fos
description: " FOnline: 2238 Rotators  quest_la_dogs.fos ..."
---

# quest_la_dogs.fos


FOnline: 2238
Rotators

quest_la_dogs.fos


## Includes

- `_colors.fos`
- `quest_killmobs_h.fos`
- `worldmap_h.fos`
- `utils_h.fos`
- `npc_planes_h.fos`
- `entire.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| ALL_KILLED | `(2)` |  |
| IDLE_NORMAL | `(3000)` |  |
| DIALOG | `(9471)` |  |
| PID | `(82)` |  |
| GROUP_RESPAWN_TIME | `(REAL_HOUR(Random(20, 30)))` | the time after dog group is added to the zone it's been removed from |

## Functions

### d_CheckDogs

check if there is some group of dog roaming on the worldmap near LA

```angelscript
bool d_CheckDogs(Critter& player, Critter@ npc)
```

### d_NoDogs

```angelscript
bool d_NoDogs(Critter& player, Critter@ npc)
```

### r_SpawnLoc

```angelscript
void r_SpawnLoc(Critter& player, Critter@ npc)
```

### test

```angelscript
void test(Critter& cr, int, int, int)
```

### r_DeleteLoc

```angelscript
void r_DeleteLoc(Critter& player, Critter@ npc)
```

### critter_init

```angelscript
void critter_init(Critter& cr, bool firstTime)
```

### _DogIdle

```angelscript
void _DogIdle(Critter& mob)
```

### _DogShowCritter

```angelscript
void _DogShowCritter(Critter& mob, Critter& showCrit)
```

### _DogDead

```angelscript
void _DogDead(Critter& cr, Critter@ killer)
```

### e_SpawnDogGroup

```angelscript
uint e_SpawnDogGroup(array<uint>@ values)
```

### _DogAttacked

```angelscript
bool _DogAttacked(Critter& cr, Critter& attacker)
```

### _DogOnMessage

```angelscript
void _DogOnMessage(Critter& cr, Critter& fromCr, int message, int value)
```


