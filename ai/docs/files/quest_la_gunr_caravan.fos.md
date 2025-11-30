---
title: quest_la_gunr_caravan.fos
description: " FOnline: 2238 Rotators  quest_la_gunr_caravan.fos ..."
---

# quest_la_gunr_caravan.fos


FOnline: 2238
Rotators

quest_la_gunr_caravan.fos


## Includes

- `_colors.fos`
- `_maps.fos`
- `_vars.fos`
- `_macros.fos`
- `entire.fos`
- `mapdata_h.fos`
- `messages_h.fos`
- `guard_h.fos`
- `npc_common_h.fos`
- `npc_planes_h.fos`
- `utils_h.fos`
- `logging_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| DIALOG_ID | `(10277)` |  |
| ROLE_DEFAULT | `(0)` | npc roles (defines distance mob will attack from)) |
| ROLE_AGRESSIVE | `(1)` |  |
| ROLE_PASSIVE | `(2)` |  |
| ALERTED | `# (cr)           (cr.StatBase[ST_VAR1])` | useful variables |
| IDLE_NORMAL | `(5000)` | idle time in milseconds (normal is slower for performance issues) |
| IDLE_ALERTED | `(1000)` |  |
| STR_MUTANT_ENTRANCE_ATTACK | `(1)` |  |

## Functions

### r_SpawnLocation

```angelscript
void r_SpawnLocation(Critter& player, Critter@ npc)
```

### _CritterInMap

```angelscript
void _CritterInMap(Map& map, Critter& cr)
```

### e_WearWeapons

```angelscript
uint e_WearWeapons(uint[] @ values)
```

### r_DeleteLocation

```angelscript
void r_DeleteLocation(Critter& player, Critter@ npc)
```

### GetOwner

```angelscript
Critter@ GetOwner(Map& map)
```

### t_EntranceAttack

```angelscript
void t_EntranceAttack(Critter& cr, Scenery& trigger, bool entered, uint8 dir)
```

### _Mutant

```angelscript
void _Mutant(Critter& cr, bool firstTime)
```

### _Attacked

```angelscript
bool _Attacked(Critter& cr, Critter& attacker)
```

### _OnMessage

```angelscript
void _OnMessage(Critter& cr, Critter& fromCr, int message, int value)
```

### _MobIdle

 Checks if critter is within attack distance 

```angelscript
void _MobIdle(Critter& cr)
```

### MoveMob

```angelscript
void MoveMob(Critter& cr, bool run)
```

### GetDistance

 Gets distance after which critter becomes agressive 

```angelscript
uint GetDistance(Critter& cr)
```

### _MobShowCritter

 Alerts that oponent is near 

```angelscript
void _MobShowCritter(Critter& cr, Critter& showCrit)
```

### _MobHideCritter

```angelscript
void _MobHideCritter(Critter& cr, Critter& hideCrit)
```

### r_QuestCD

 30-08-2013 Cubik: dodany CD dla gracza na ponowne wybranie questu : 6-9 real-time godzin 

```angelscript
void r_QuestCD(Critter& player, Critter@ npc)
```

### e_reset_quest_var

```angelscript
uint e_reset_quest_var(array<uint>@ values)
```


