---
title: quest_advent.fos
---

# quest_advent.fos

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
| QUEST_ALL_KILLED | `(3)` |  |
| QUEST_FAILED | `(1)` |  |
| DIALOG | `(0)` |  |

## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| adventPids | `array<uint16>` | `{ 919 }` |  |

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

### _adventIdle

```angelscript
void _adventIdle(Critter& mob)
```

### _adventShowCritter

```angelscript
void _adventShowCritter(Critter& mob, Critter& showCrit)
```

### _adventDead

check if all Vipers are killed, if yes, than set quest lvar to QUEST_ALL_KILLED value

```angelscript
void _adventDead(Critter& cr, Critter@ killer)
```

### _adventAttacked

```angelscript
bool _adventAttacked(Critter& cr, Critter& attacker)
```

### _adventOnMessage

```angelscript
void _adventOnMessage(Critter& cr, Critter& fromCr, int message, int value)
```


