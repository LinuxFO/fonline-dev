---
title: item_misc.fos
description: " FOnline: 2238 Rotators  item_misc.fos ..."
---

# item_misc.fos


FOnline: 2238
Rotators

item_misc.fos


## Includes

- `_defines.fos`
- `_macros.fos`
- `_dialogs.fos`
- `MsgStr.h`
- `lexems_h.fos`
- `item_misc_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __ITEM_MISC__ |  |  |

## Functions

### _Waterpipe

```angelscript
void _Waterpipe(Item& item, bool firstTime)
```

### _SkillWaterpipe

```angelscript
bool _SkillWaterpipe(Item& item, Critter& cr, int skill)
```

### _UseWaterpipe

```angelscript
bool _UseWaterpipe(Item& item, Critter& cr, Critter@ onCritter, Item@ onItem, Scenery@ onScenery)
```

### _WaterpipeReal

```angelscript
bool _WaterpipeReal(Critter& cr)
```

### _Charge

template for rechargeable items with start value set in proto

```angelscript
void _Charge(Item& item, bool firstTime)
```

### _NpcSkinArmor

```angelscript
void _NpcSkinArmor(Item& item, bool firstTime)
```

### CreateMapTo

```angelscript
Item@ CreateMapTo(Critter& cr, Location& location, uint flags)
```

### CreateMapTo

```angelscript
Item@ CreateMapTo(Critter& cr, Location& location, uint flags, string& info)
```

### _MapToLocation

```angelscript
void _MapToLocation(Item& item, bool firstTime)
```

### _MapToLocationUse

```angelscript
bool _MapToLocationUse(Item& item, Critter& cr, Critter@ onCritter, Item@ onItem, Scenery@ onScenery)
```


