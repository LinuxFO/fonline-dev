---
title: quest_copsim.fos
---

# quest_copsim.fos

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
| QUEST_ALL_KILLED | `(7)` |  |
| QUEST_FAILED | `(0)` |  |
| DIALOG | `(0)` |  |

## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| copPids | `array<uint16>` | `{ 2002}` |  |

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

### _copIdle

```angelscript
void _copIdle(Critter& mob)
```

### _copShowCritter

```angelscript
void _copShowCritter(Critter& mob, Critter& showCrit)
```

### _copDead

check if all Vipers are killed, if yes, than set quest lvar to QUEST_ALL_KILLED value

```angelscript
void _copDead(Critter& cr, Critter@ killer)
```

### _copAttacked

```angelscript
bool _copAttacked(Critter& cr, Critter& attacker)
```

### _copOnMessage

```angelscript
void _copOnMessage(Critter& cr, Critter& fromCr, int message, int value)
```


