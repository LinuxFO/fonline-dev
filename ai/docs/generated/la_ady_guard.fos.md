---
title: la_ady_guard.fos
description: " FOnline: 2238 Rotators  la_ady_guard.fos ..."
---

# la_ady_guard.fos


FOnline: 2238
Rotators

la_ady_guard.fos


## Includes

- `_macros.fos`
- `factions_h.fos`
- `npc_roles_h.fos`
- `guard_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| DIALOG_ID | `(9421)` |  |

## Functions

### critter_init

```angelscript
void critter_init(Critter& guard, bool firstTime)
```

### _OnMessage

```angelscript
void _OnMessage(Critter& npc, Critter& player, int num, int val)
```

### _OnShowCritter

```angelscript
void _OnShowCritter(Critter& guard, Critter& critter)
```

### _OnSomeoneSteal

```angelscript
void _OnSomeoneSteal(Critter& guard, Critter& target, Critter& thief, bool success, Item& item, uint count)
```


