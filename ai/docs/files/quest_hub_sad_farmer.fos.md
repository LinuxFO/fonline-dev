---
title: quest_hub_sad_farmer.fos
---

# quest_hub_sad_farmer.fos

## Includes

- `_colors.fos`
- `_macros.fos`
- `_npc_pids.fos`
- `mapdata_h.fos`
- `utils_h.fos`
- `quest_killmobs_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| Q_NOT_STARTED | `(0)` |  |
| Q_STARTED | `(1)` |  |
| Q_FINISHED | `(2)` |  |
| Q_OVER | `(3)` |  |

## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| enemiesPid | `array<uint>` | `{ 11, 12, 16, 80, 81, 83, 86, 111, 113, 116, 117, 118, 240, 241, 383 }` |  |

## Functions

### r_SpawnFarmhouse

```angelscript
void r_SpawnFarmhouse(Critter& player, Critter@ npc)
```

### r_RemoveFarmhouse

```angelscript
void r_RemoveFarmhouse(Critter& player, Critter@ npc)
```

### _Enemy

```angelscript
void _Enemy(Critter& cr, bool firstTime)
```

### _EnemyDead

```angelscript
void _EnemyDead(Critter& cr, Critter@ killer)
```

### _EnemyIdle

```angelscript
void _EnemyIdle(Critter& mob)
```

### _EnemyShowCritter

```angelscript
void _EnemyShowCritter(Critter& mob, Critter& showCrit)
```


