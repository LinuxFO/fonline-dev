---
title: quest_dailyfarm1.fos
---

# quest_dailyfarm1.fos

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
| QUEST_ALL_KILLED | `(18)` |  |
| QUEST_FAILED | `(0)` |  |
| DIALOG | `(0)` |  |

## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| sextPids | `array<uint16>` | `{ 2005, 2006, 2007, 2008, 2009, 2010 }` |  |

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

### _sextIdle

```angelscript
void _sextIdle(Critter& mob)
```

### _sextShowCritter

```angelscript
void _sextShowCritter(Critter& mob, Critter& showCrit)
```

### _sextDead

check if all Vipers are killed, if yes, than set quest lvar to QUEST_ALL_KILLED value

```angelscript
void _sextDead(Critter& cr, Critter@ killer)
```

### _sextAttacked

```angelscript
bool _sextAttacked(Critter& cr, Critter& attacker)
```

### _sextOnMessage

```angelscript
void _sextOnMessage(Critter& cr, Critter& fromCr, int message, int value)
```


