---
title: quest_advent6.fos
---

# quest_advent6.fos

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
| QUEST_ALL_KILLED | `(33)` |  |
| QUEST_FAILED | `(32)` |  |
| DIALOG | `(0)` |  |

## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| advent6Pids | `array<uint16>` | `{ 936 }` |  |

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

### _advent6Idle

```angelscript
void _advent6Idle(Critter& mob)
```

### _advent6ShowCritter

```angelscript
void _advent6ShowCritter(Critter& mob, Critter& showCrit)
```

### _advent6Dead

check if all Vipers are killed, if yes, than set quest lvar to QUEST_ALL_KILLED value

```angelscript
void _advent6Dead(Critter& cr, Critter@ killer)
```

### _advent6Attacked

```angelscript
bool _advent6Attacked(Critter& cr, Critter& attacker)
```

### _advent6OnMessage

```angelscript
void _advent6OnMessage(Critter& cr, Critter& fromCr, int message, int value)
```


