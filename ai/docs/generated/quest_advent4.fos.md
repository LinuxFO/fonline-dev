---
title: quest_advent4.fos
---

# quest_advent4.fos

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
| QUEST_ALL_KILLED | `(25)` |  |
| QUEST_FAILED | `(23)` |  |
| DIALOG | `(0)` |  |

## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| advent4Pids | `array<uint16>` | `{ 924 }` |  |

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

### _advent4Idle

```angelscript
void _advent4Idle(Critter& mob)
```

### _advent4ShowCritter

```angelscript
void _advent4ShowCritter(Critter& mob, Critter& showCrit)
```

### _advent4Dead

check if all Vipers are killed, if yes, than set quest lvar to QUEST_ALL_KILLED value

```angelscript
void _advent4Dead(Critter& cr, Critter@ killer)
```

### _advent4Attacked

```angelscript
bool _advent4Attacked(Critter& cr, Critter& attacker)
```

### _advent4OnMessage

```angelscript
void _advent4OnMessage(Critter& cr, Critter& fromCr, int message, int value)
```


