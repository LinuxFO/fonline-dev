---
title: quest_first_tent.fos
description: " FOnline: 2238 Rotators  quest_first_tent.fos ..."
---

# quest_first_tent.fos


FOnline: 2238
Rotators

quest_first_tent.fos


## Includes

- `_colors.fos`
- `_macros.fos`
- `_npc_pids.fos`
- `mapdata_h.fos`
- `utils_h.fos`
- `logging_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| Q_FIRST_TENT_NOT_STARTED | `(0)` |  |
| Q_FIRST_TENT_STARTED | `(1)` |  |
| Q_FIRST_TENT_ACCEPTED | `(2)` |  |
| Q_FIRST_TENT_RATS_KILLED | `(3)` |  |
| Q_FIRST_TENT_FINISHED | `(4)` |  |
| Q_FIRST_TENT_FAILED | `(5)` |  |

## Functions

### StartFirstTentQuest

```angelscript
void StartFirstTentQuest(Critter& player)
```

### r_SpawnFarmhouse

```angelscript
void r_SpawnFarmhouse(Critter& player, Critter@ npc)
```

### r_FamilyLeave

Transit all non-true npcs to "abandoned tent" map. 

```angelscript
void r_FamilyLeave(Critter& player, Critter@ npc)
```

### _InitAbandonedTent

```angelscript
void _InitAbandonedTent(Map& map, bool firstTime)
```

### _InTent

```angelscript
void _InTent(Map& map, Critter& cr)
```

### _OutAbandonedTent

```angelscript
void _OutAbandonedTent(Map& map, Critter& cr)
```

### _Rat

```angelscript
void _Rat(Critter& cr, bool firstTime)
```

### _RatDead

```angelscript
void _RatDead(Critter& cr, Critter@ killer)
```


