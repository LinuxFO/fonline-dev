---
title: generic_guard.fos
description: " FOnline: 2238 Rotators  generic_guard.fos ..."
---

# generic_guard.fos


FOnline: 2238
Rotators

generic_guard.fos


## Includes

- `_macros.fos`
- `groups_h.fos`
- `guard_h.fos`
- `mapdata_h.fos`
- `reputations_h.fos`
- `npc_planes_h.fos`
- `utils_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| SHOWCRITTER1_TOWNGUARD | `(5)` |  |

## Functions

### critter_init

```angelscript
void critter_init(Critter& guard, bool firstTime)
```

### _FactionGuard

```angelscript
void _FactionGuard(Critter& guard, bool firstTime)
```

### _OnShowCritter

```angelscript
void _OnShowCritter(Critter& cr, Critter& target)
```

### _OnShowCritter1

```angelscript
void _OnShowCritter1(Critter& cr, Critter& target)
```

### _OnIdle

```angelscript
void _OnIdle(Critter& cr)
```

### e_CheckWeapon

```angelscript
uint e_CheckWeapon(array<uint>@ values)
```


