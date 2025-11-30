---
title: quest_evil.fos
---

# quest_evil.fos

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
| DIALOG | `(40)` |  |

## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| evilPids | `array<uint16>` | `{ 50, 51 }` |  |

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

### _evilIdle

```angelscript
void _evilIdle(Critter& mob)
```

### _evilShowCritter

```angelscript
void _evilShowCritter(Critter& mob, Critter& showCrit)
```

### _evilDead

check if all Vipers are killed, if yes, than set quest lvar to QUEST_ALL_KILLED value

```angelscript
void _evilDead(Critter& cr, Critter@ killer)
```

### _evilAttacked

```angelscript
bool _evilAttacked(Critter& cr, Critter& attacker)
```

### _evilOnMessage

```angelscript
void _evilOnMessage(Critter& cr, Critter& fromCr, int message, int value)
```


