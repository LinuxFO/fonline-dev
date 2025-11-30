---
title: quest_hubo.fos
---

# quest_hubo.fos

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
| DIALOG | `(23094)` |  |

## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| huboPids | `array<uint16>` | `{ 877, 878 }` |  |

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

### _huboIdle

```angelscript
void _huboIdle(Critter& mob)
```

### _huboShowCritter

```angelscript
void _huboShowCritter(Critter& mob, Critter& showCrit)
```

### _huboDead

check if all Vipers are killed, if yes, than set quest lvar to QUEST_ALL_KILLED value

```angelscript
void _huboDead(Critter& cr, Critter@ killer)
```

### _huboAttacked

```angelscript
bool _huboAttacked(Critter& cr, Critter& attacker)
```

### _huboOnMessage

```angelscript
void _huboOnMessage(Critter& cr, Critter& fromCr, int message, int value)
```


