---
title: quest_mutar.fos
---

# quest_mutar.fos

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
| mutarPids | `array<uint16>` | `{ 116, 113 }` |  |

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

### _mutarIdle

```angelscript
void _mutarIdle(Critter& mob)
```

### _mutarShowCritter

```angelscript
void _mutarShowCritter(Critter& mob, Critter& showCrit)
```

### _mutarDead

check if all Vipers are killed, if yes, than set quest lvar to QUEST_ALL_KILLED value

```angelscript
void _mutarDead(Critter& cr, Critter@ killer)
```

### _mutarAttacked

```angelscript
bool _mutarAttacked(Critter& cr, Critter& attacker)
```

### _mutarOnMessage

```angelscript
void _mutarOnMessage(Critter& cr, Critter& fromCr, int message, int value)
```


