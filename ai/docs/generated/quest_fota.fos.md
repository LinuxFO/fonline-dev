---
title: quest_fota.fos
---

# quest_fota.fos

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
| DIALOG | `(1104)` |  |

## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| fotaPids | `array<uint16>` | `{ 875, 876 }` |  |

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

### _fotaIdle

```angelscript
void _fotaIdle(Critter& mob)
```

### _fotaShowCritter

```angelscript
void _fotaShowCritter(Critter& mob, Critter& showCrit)
```

### _fotaDead

check if all Vipers are killed, if yes, than set quest lvar to QUEST_ALL_KILLED value

```angelscript
void _fotaDead(Critter& cr, Critter@ killer)
```

### _fotaAttacked

```angelscript
bool _fotaAttacked(Critter& cr, Critter& attacker)
```

### _fotaOnMessage

```angelscript
void _fotaOnMessage(Critter& cr, Critter& fromCr, int message, int value)
```


