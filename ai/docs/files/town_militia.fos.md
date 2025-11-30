---
title: town_militia.fos
description: " FOnline: 2238 Rotators  town_militia.fos ..."
---

# town_militia.fos


FOnline: 2238
Rotators

town_militia.fos


## Includes

- `_macros.fos`
- `_basetypes.fos`
- `_town.fos`
- `entire.fos`
- `factions_h.fos`
- `follower_common_h.fos`
- `follower_h.fos`
- `guard_h.fos`
- `messages_h.fos`
- `npc_common_h.fos`
- `npc_planes_h.fos`
- `reputations_h.fos`
- `town_h.fos`
- `utils_h.fos`
- `world_common_h.fos`

## Functions

### r_BecomeMilitia

```angelscript
void r_BecomeMilitia(Critter& player, Critter@ cr)
```

### GetMilitiaTeamByLoc

```angelscript
uint GetMilitiaTeamByLoc(Location@ loc)
```

### AssignMilitiaTeam

```angelscript
void AssignMilitiaTeam(Critter& cr)
```

### critter_init

```angelscript
void critter_init(Critter& cr, bool firstTime)
```

### MilitiaMoveToFreeHex

```angelscript
void MilitiaMoveToFreeHex(Critter& cr)
```

### _Dead

```angelscript
void _Dead(Critter& cr, Critter@ killer)
```

### _Idle

```angelscript
void _Idle(Critter& cr)
```

### _Attacked

```angelscript
bool _Attacked(Critter& follower, Critter& attacker)
```

### _SomeoneAttacked

```angelscript
void _SomeoneAttacked(Critter& cr, Critter& fromCrit, Critter& target)
```

### _OnSomeoneSteal

```angelscript
void _OnSomeoneSteal(Critter& militia, Critter& target, Critter& thief, bool success, Item& item, uint count)
```

### IsFriend

```angelscript
bool IsFriend(Critter& cr, Critter& target)
```


