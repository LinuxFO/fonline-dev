---
title: quest_indec.fos
---

# quest_indec.fos

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
| QUEST_ALL_KILLED | `(6)` |  |
| QUEST_FAILED | `(0)` |  |
| DIALOG | `(0)` |  |

## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| clawPids | `array<uint16>` | `{ 941, 942, 943 }` |  |

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

### _clawIdle

```angelscript
void _clawIdle(Critter& mob)
```

### _clawShowCritter

```angelscript
void _clawShowCritter(Critter& mob, Critter& showCrit)
```

### _clawDead

check if all Vipers are killed, if yes, than set quest lvar to QUEST_ALL_KILLED value

```angelscript
void _clawDead(Critter& cr, Critter@ killer)
```

### _clawAttacked

```angelscript
bool _clawAttacked(Critter& cr, Critter& attacker)
```

### _clawOnMessage

```angelscript
void _clawOnMessage(Critter& cr, Critter& fromCr, int message, int value)
```


