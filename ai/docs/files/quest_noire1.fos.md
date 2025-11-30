---
title: quest_noire1.fos
---

# quest_noire1.fos

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
| QUEST_ALL_KILLED | `(4)` |  |
| QUEST_FAILED | `(2)` |  |
| DIALOG | `(0)` |  |

## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| noir1Pids | `array<uint16>` | `{ 938, 939, 940 }` |  |

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

### _noir1Idle

```angelscript
void _noir1Idle(Critter& mob)
```

### _noir1ShowCritter

```angelscript
void _noir1ShowCritter(Critter& mob, Critter& showCrit)
```

### _noir1Dead

check if all Vipers are killed, if yes, than set quest lvar to QUEST_ALL_KILLED value

```angelscript
void _noir1Dead(Critter& cr, Critter@ killer)
```

### _noir1Attacked

```angelscript
bool _noir1Attacked(Critter& cr, Critter& attacker)
```

### _noir1OnMessage

```angelscript
void _noir1OnMessage(Critter& cr, Critter& fromCr, int message, int value)
```


