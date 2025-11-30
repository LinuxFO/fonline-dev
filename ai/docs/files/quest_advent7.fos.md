---
title: quest_advent7.fos
---

# quest_advent7.fos

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
| QUEST_ALL_KILLED | `(42)` |  |
| QUEST_FAILED | `(40)` |  |
| DIALOG | `(0)` |  |

## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| advent7Pids | `array<uint16>` | `{ 937 }` |  |

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

### _advent7Idle

```angelscript
void _advent7Idle(Critter& mob)
```

### _advent7ShowCritter

```angelscript
void _advent7ShowCritter(Critter& mob, Critter& showCrit)
```

### _advent7Dead

check if all Vipers are killed, if yes, than set quest lvar to QUEST_ALL_KILLED value

```angelscript
void _advent7Dead(Critter& cr, Critter@ killer)
```

### _advent7Attacked

```angelscript
bool _advent7Attacked(Critter& cr, Critter& attacker)
```

### _advent7OnMessage

```angelscript
void _advent7OnMessage(Critter& cr, Critter& fromCr, int message, int value)
```


