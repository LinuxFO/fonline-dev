---
title: noob_camp_guard.fos
---

# noob_camp_guard.fos

## Includes

- `_macros.fos`
- `factions_h.fos`
- `guard_h.fos`
- `npc_common_h.fos`
- `npc_planes_h.fos`
- `npc_roles_h.fos`

## Functions

### critter_init

```angelscript
void critter_init(Critter& guard, bool firstTime)
```

### _Idle

```angelscript
void _Idle(Critter& guard)
```

### _OnMessage

```angelscript
void _OnMessage(Critter& npc, Critter& player, int num, int val)
```

### _OnSomeoneSteal

```angelscript
void _OnSomeoneSteal(Critter& guard, Critter& target, Critter& thief, bool success, Item& item, uint count)
```

### _OnShowCritter

```angelscript
void _OnShowCritter(Critter& guard, Critter& player)
```


