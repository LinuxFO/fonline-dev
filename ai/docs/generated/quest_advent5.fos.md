---
title: quest_advent5.fos
---

# quest_advent5.fos

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
| QUEST_ALL_KILLED | `(30)` |  |
| QUEST_FAILED | `(28)` |  |
| DIALOG | `(0)` |  |

## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| advent5Pids | `array<uint16>` | `{ 925, 926, 927, 928, 929 }` |  |

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

### _advent5Idle

```angelscript
void _advent5Idle(Critter& mob)
```

### _advent5ShowCritter

```angelscript
void _advent5ShowCritter(Critter& mob, Critter& showCrit)
```

### _advent5Dead

check if all Vipers are killed, if yes, than set quest lvar to QUEST_ALL_KILLED value

```angelscript
void _advent5Dead(Critter& cr, Critter@ killer)
```

### _advent5Attacked

```angelscript
bool _advent5Attacked(Critter& cr, Critter& attacker)
```

### _advent5OnMessage

```angelscript
void _advent5OnMessage(Critter& cr, Critter& fromCr, int message, int value)
```


