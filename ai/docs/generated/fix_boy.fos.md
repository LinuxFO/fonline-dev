---
title: fix_boy.fos
description: " FOnline: 2238 Rotators  fix_boy.fos ..."
---

# fix_boy.fos


FOnline: 2238
Rotators

fix_boy.fos


## Includes

- `_macros.fos`
- `MsgStr.h`
- `utils_h.fos`
- `_vals.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| FIX_SUCCESS | `(FIXBOY_DEFAULT)` |  |
| FIX_TIMEOUT | `(FIXBOY_DEFAULT ^ FIXBOY_SET_TIMEOUT)` |  |
| FIX_FAIL | `(FIXBOY_DEFAULT ^ FIXBOY_ALLOW_CRAFT)` |  |
| FIX_FAIL_NO_MESSAGE | `(FIXBOY_DEFAULT ^ FIXBOY_ALLOW_CRAFT ^ FIXBOY_SEND_FAIL_MESSAGE)` |  |
| FIX_TIMEOUT_NO_ITEM | `(FIXBOY_DEFAULT ^ FIXBOY_SET_TIMEOUT ^ FIXBOY_ADD_CRAFT_ITEMS)` |  |
| FIX_FILTER_ALL | `(0)` |  |
| FIX_FILTER_WEAPONS | `(1)` |  |
| FIX_FILTER_ARMORS | `(2)` |  |
| FIX_FILTER_AMMO | `(3)` |  |
| FIX_FILTER_DRUGS | `(4)` |  |
| FIX_FILTER_MISC | `(5)` |  |
| SHORT_TO | `(300)` | Timeout modifiers |
| MEDIUM_TO | `(900)` |  |
| LONG_TO | `(2700)` |  |
| ETERNITY_TO | `(7100)` |  |
| LUCK_TO | `(Random(6, 60) / (5 + player.Stat[ST_LUCK]))` | Luck modifier. Shit happens, even when crafting. |
| CUMULATIVE_TIMEOUT | `int(REAL_MINUTE(360))` |  |
| WS_UNARMED | `(1)` | ////////////////////////// Disassembly ////////////////////////// |
| WS_MELEE | `(2)` |  |
| WS_THROWING | `(3)` |  |
| WS_GUN | `(4)` |  |
| SALV_FACTOR | `# (_cr)  (_cr.Perk[PE_DISMANTLER] > 0 ? 0.2 : 0.1)` |  |

## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| PidRecipe | `array<uint>` |  |  |

## Functions

### AddCraftingExperience

```angelscript
void AddCraftingExperience(Critter& player, uint exp, int mult)
```

### AddScienceExperience

```angelscript
void AddScienceExperience(Critter& player, uint exp)
```

### GetProfessionLevel

 Checks if player has given profession at a desired level 

```angelscript
int GetProfessionLevel(Critter& player, uint lvar)
```

### MapCheck

 Checks if the player is on the map with given proto id 

```angelscript
bool MapCheck(Critter& player, uint mapPid)
```

### FixboyCheck

 Check if player is near workbench 

```angelscript
bool FixboyCheck(Critter& player)
```

### WorkbenchCheck

```angelscript
bool WorkbenchCheck(Critter& player)
```

### MfcCheck

in Mariposa, near crafting system

```angelscript
bool MfcCheck(Critter& player)
```

### MedCheck

```angelscript
bool MedCheck(Critter& player)
```

### AmmoCheck

```angelscript
bool AmmoCheck(Critter& player)
```

### IsResource

* * Checks if item is a resource, i.e. item created only to be part of craft recipe. * Items that are part of recipe to be upgraded (i.e. CA -> CA2) are not resources. 

```angelscript
bool IsResource(Item& item)
```

### IsHighQualityResource

* * Checks if resource is high quality. 

```angelscript
bool IsHighQualityResource(Item& item)
```

### IsWorkedResource

* * Checks if item is resource that is crafted, not gathered. 

```angelscript
bool IsWorkedResource(Item& item)
```

### ApplyTimeout

 Timeouts  assumes: upgrade items give only one result item

```angelscript
void ApplyTimeout(array<Item@>& items, array<uint>& itemsCount, array<Item@>& resources, Critter& crafter)
```

### TimeoutCheck

called for FIXBOY_CRAFT stage to check cumulative timeout

```angelscript
int TimeoutCheck(Critter& player)
```

### GetItemType

```angelscript
uint GetItemType(uint pid)
```

### FilterItems

```angelscript
bool FilterItems(Critter& player, uint pid)
```

### CheckMultiplierResources

```angelscript
bool CheckMultiplierResources(Critter& player, CraftItem& craft)
```

### GetItemRecipe

```angelscript
uint GetItemRecipe(uint16 itemPid, array<uint16>& pids, array<uint>& cnt)
```

### fix_Resource

no timeout for mid-resources, no timeout check too

```angelscript
int fix_Resource(Critter& player, int stage, CraftItem& craft)
```

### fix_Generic

```angelscript
int fix_Generic(Critter& player, int stage, CraftItem& craft)
```

### fix_Blueprint

checks if player has consumed blueprint, to determine whether to list item

```angelscript
int fix_Blueprint(Critter& player, int stage, CraftItem& craft)
```

### fix_Lock

```angelscript
int fix_Lock(Critter& player, int stage, CraftItem& craft)
```

### Add

helper

```angelscript
bool Add(Critter& cr, array<int>& pids, int value, int sk)
```

### ReversableItem

```angelscript
bool ReversableItem(Item& item)
```

### InitReverseItem

```angelscript
void InitReverseItem()
```

### ReverseAllItems

```angelscript
bool ReverseAllItems(Critter& cr, array<Item@>& items, uint cnt, uint max)
```

### ReverseItem

```angelscript
bool ReverseItem(Critter& cr, Item& item, bool isMassScience)
```

### ReverseItem

```angelscript
bool ReverseItem(Critter& cr, Item& item)
```

### ReverseItemCrafted

```angelscript
bool ReverseItemCrafted(Critter& cr, Item& item, bool isMassScience)
```

### ReverseItemGeneric

```angelscript
bool ReverseItemGeneric(Critter& cr, Item& item, bool isMassScience)
```

### ReverseItemCustom

special cases

```angelscript
bool ReverseItemCustom(Critter& cr, Item& item, bool isMassScience)
```

### unsafe_counter

```angelscript
void unsafe_counter( Critter& player, int cnt, int, int, string@, int[]@ )
```

### unsafe_fixall

```angelscript
void unsafe_fixall( Critter& player, int cnt, int, int, string@, int[]@ )
```

### unsafe_filter

```angelscript
void unsafe_filter( Critter& player, int flt, int, int, string@, int[]@ )
```

### IsItemCraftable

```angelscript
bool IsItemCraftable(uint16 pid)
```


