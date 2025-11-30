---
title: quest_bos_initiate.fos
description: " FOnline: 2238 Rotators  quest_bos_initiate.fos ..."
---

# quest_bos_initiate.fos


FOnline: 2238
Rotators

quest_bos_initiate.fos


## Includes

- `_colors.fos`
- `_macros.fos`
- `_vars.fos`
- `_maps.fos`
- `_dialogs.fos`
- `groups_h.fos`
- `utils_h.fos`
- `mapdata_h.fos`
- `MSGSTR.h`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| HUMMER_REPAIR_DIFFICULTY | `(75)` |  |

## Functions

### spawn

```angelscript
void spawn(Critter& player, int, int, int)
```

### r_SpawnBunker

```angelscript
void r_SpawnBunker(Critter& player, Critter@ npc)
```

### _InjuredSoldier

```angelscript
void _InjuredSoldier(Critter& cr, bool firstTime)
```

### _InjuredItem

```angelscript
bool _InjuredItem(Critter& cr, Critter& who, Item& item)
```

### _InjuredSkill

```angelscript
bool _InjuredSkill(Critter& cr, Critter& who, int skill)
```

### InjuredDialog

```angelscript
bool InjuredDialog(Critter& player, Critter& npc)
```

### r_HealSoldier

```angelscript
void r_HealSoldier(Critter& player, Critter@ npc, int val)
```

### r_RetireMap

```angelscript
void r_RetireMap(Critter& player, Critter@ npc)
```

### e_HummerAway

```angelscript
uint e_HummerAway(array<uint>@ values)
```

### _Hummer

```angelscript
void _Hummer(Item& item, bool firstTime)
```

### _HummerUseOnMe

```angelscript
bool _HummerUseOnMe(Item& hummer, Critter& crit, Item@ item)
```

### _HummerSkill

```angelscript
bool _HummerSkill(Item& hummer, Critter& crit, int skill)
```

### _MapHummer

```angelscript
void _MapHummer(Map& map, bool firstTime)
```

### _MapBattleground

```angelscript
void _MapBattleground(Map& map, bool firstTime)
```

### _GhostFarmCritterIn

```angelscript
void _GhostFarmCritterIn(Map& map, Critter& cr)
```

### r_GiveKey

```angelscript
void r_GiveKey(Critter& player, Critter@ npc)
```

### _Chris

```angelscript
void _Chris(Critter& cr, bool firstTime)
```

### _ChrisUseSkillOn

```angelscript
void _ChrisUseSkillOn(Critter& cr, Critter& fromCr, int skill, Critter@ onCritter, Item@ onItem, Scenery@ onScenery)
```

### _ChrisDead

```angelscript
void _ChrisDead(Critter& cr, Critter@ killer)
```

### _FenceDoor

```angelscript
void _FenceDoor(Item& item, bool firstTime)
```

### _FenceDoorSkill

```angelscript
bool _FenceDoorSkill(Item& item, Critter& crit, int skill)
```

### t_NukaColaMachine

```angelscript
void t_NukaColaMachine(Critter& player, Scenery& trigger, bool entered, uint8 dir)
```

### e_ResetVar

```angelscript
uint e_ResetVar(array<uint>@ values)
```


