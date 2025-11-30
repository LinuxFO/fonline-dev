---
title: quest_advent3.fos
---

# quest_advent3.fos

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
| QUEST_ALL_KILLED | `(17)` |  |
| QUEST_FAILED | `(15)` |  |
| DIALOG | `(0)` |  |

## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| advent3Pids | `array<uint16>` | `{ 923 }` |  |

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

### _advent3Idle

```angelscript
void _advent3Idle(Critter& mob)
```

### _advent3ShowCritter

```angelscript
void _advent3ShowCritter(Critter& mob, Critter& showCrit)
```

### _advent3Dead

check if all Vipers are killed, if yes, than set quest lvar to QUEST_ALL_KILLED value

```angelscript
void _advent3Dead(Critter& cr, Critter@ killer)
```

### _advent3Attacked

```angelscript
bool _advent3Attacked(Critter& cr, Critter& attacker)
```

### _advent3OnMessage

```angelscript
void _advent3OnMessage(Critter& cr, Critter& fromCr, int message, int value)
```


