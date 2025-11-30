---
title: quest_advent2.fos
---

# quest_advent2.fos

## Includes

- `quest_killmobs_h.fos`
- `utils_h.fos`
- `worldmap_h.fos`
- `npc_planes_h.fos`
- `entire.fos`
- `_colors.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| QUEST_ALL_KILLED | `(10)` |  |
| QUEST_FAILED | `(8)` |  |
| DIALOG | `(0)` |  |

## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| advent2Pids | `array<uint16>` | `{ 919, 920, 922 }` |  |

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

### critter_init

set functions for basic critter events

```angelscript
void critter_init(Critter& cr, bool firstTime)
```

### _advent2Idle

```angelscript
void _advent2Idle(Critter& mob)
```

### _advent2ShowCritter

```angelscript
void _advent2ShowCritter(Critter& mob, Critter& showCrit)
```

### _advent2Dead

check if all Vipers are killed, if yes, than set quest lvar to QUEST_ALL_KILLED value

```angelscript
void _advent2Dead(Critter& cr, Critter@ killer)
```

### _advent2Attacked

```angelscript
bool _advent2Attacked(Critter& cr, Critter& attacker)
```

### _advent2OnMessage

```angelscript
void _advent2OnMessage(Critter& cr, Critter& fromCr, int message, int value)
```


