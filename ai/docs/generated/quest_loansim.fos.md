---
title: quest_loansim.fos
---

# quest_loansim.fos

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
| QUEST_ALL_KILLED | `(5)` |  |
| QUEST_FAILED | `(0)` |  |
| DIALOG | `(0)` |  |

## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| loanPids | `array<uint16>` | `{ 2001 }` |  |

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

### _loanIdle

```angelscript
void _loanIdle(Critter& mob)
```

### _loanShowCritter

```angelscript
void _loanShowCritter(Critter& mob, Critter& showCrit)
```

### _loanDead

check if all Vipers are killed, if yes, than set quest lvar to QUEST_ALL_KILLED value

```angelscript
void _loanDead(Critter& cr, Critter@ killer)
```

### _loanAttacked

```angelscript
bool _loanAttacked(Critter& cr, Critter& attacker)
```

### _loanOnMessage

```angelscript
void _loanOnMessage(Critter& cr, Critter& fromCr, int message, int value)
```


