---
title: player_dungeonlacity.fos
---

# player_dungeonlacity.fos

## Includes

- `utils_h.fos`
- `worldmap_h.fos`
- `npc_planes_h.fos`
- `entire.fos`
- `_colors.fos`
- `quest_killmobs_h.fos`
- `messages_h.fos`
- `npc_common_h.fos`
- `npc_planes_h.fos`
- `utils_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| QUEST_FAILED | `(0)` |  |
| ROLE_DEFAULT | `(0)` |  |
| ROLE_AGRESSIVE | `(1)` |  |
| IDLE_NORMAL | `(5000)` |  |
| IDLE_ALERTED | `(1000)` |  |
| NPC_HUMAN_COUNT | `(Random(45, 60))` |  |

## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| npcHumanPids | `array<uint>` | `{ 590, 591, 567, 568, 569, 570, 571, 546, 547, 548 }` |  |
| npcHumanBags | `array<uint>` | `{ 194, 192, 192, 195, 199, 203, 392, 396, 201, 390 }` |  |

## Functions

### r_SpawnLoc

function called as request from dialog to spawn quest location

```angelscript
void r_SpawnLoc(Critter& player, Critter@ npc)
```

### r_DeleteLoc

dialog function used in request to delete quest location (after player report finishing the quest)

```angelscript
void r_DeleteLoc(Critter& player, Critter@ npc)
```

### _MobNPC

```angelscript
void _MobNPC(Critter& mob, bool firstTime)
```

### _MobIdle

```angelscript
void _MobIdle(Critter& mob)
```

### GetDistance

```angelscript
uint GetDistance(Critter& cr)
```

### _MobAttacked

```angelscript
bool _MobAttacked(Critter& cr, Critter& attacker)
```

### _MobAttacking

```angelscript
bool _MobAttacking(Critter& cr, Critter& attacker)
```

### _MobOnMessage

```angelscript
void _MobOnMessage(Critter& cr, Critter& fromCr, int message, int value)
```

### _MobSmthDead

```angelscript
void _MobSmthDead(Critter& cr, Critter& killed, Critter@ killer)
```


