---
title: quest_boss2.fos
---

# quest_boss2.fos

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
| QUEST_ALL_KILLED | `(2)` |  |
| QUEST_FAILED | `(0)` |  |
| DIALOG | `(0)` |  |

## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| zombPids | `array<uint16>` | `{ 954 }` |  |

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

### _zombIdle

```angelscript
void _zombIdle(Critter& mob)
```

### _zombShowCritter

```angelscript
void _zombShowCritter(Critter& mob, Critter& showCrit)
```

### _zombDead

check if all Vipers are killed, if yes, than set quest lvar to QUEST_ALL_KILLED value

```angelscript
void _zombDead(Critter& cr, Critter@ killer)
```

### _zombAttacked

```angelscript
bool _zombAttacked(Critter& cr, Critter& attacker)
```

### _zombOnMessage

```angelscript
void _zombOnMessage(Critter& cr, Critter& fromCr, int message, int value)
```


