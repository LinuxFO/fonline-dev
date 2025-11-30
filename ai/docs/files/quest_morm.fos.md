---
title: quest_morm.fos
---

# quest_morm.fos

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
| QUEST_FAILED | `(0)` |  |
| DIALOG | `(23095)` |  |

## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| mormPids | `array<uint16>` | `{ 883, 884 }` |  |

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

### _mormIdle

```angelscript
void _mormIdle(Critter& mob)
```

### _mormShowCritter

```angelscript
void _mormShowCritter(Critter& mob, Critter& showCrit)
```

### _mormDead

check if all Vipers are killed, if yes, than set quest lvar to QUEST_ALL_KILLED value

```angelscript
void _mormDead(Critter& cr, Critter@ killer)
```

### _mormAttacked

```angelscript
bool _mormAttacked(Critter& cr, Critter& attacker)
```

### _mormOnMessage

```angelscript
void _mormOnMessage(Critter& cr, Critter& fromCr, int message, int value)
```


