---
title: prod_rocks_ore.fos
description: " FOnline: 2238 Rotators  prod_rocks_ore.fos ..."
---

# prod_rocks_ore.fos


FOnline: 2238
Rotators

prod_rocks_ore.fos


## Includes

- `_macros.fos`
- `production_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| STR_TEXT_ORE | `(3012)` |  |

## Classes

### GatherCallback

**Methods**

#### Callback
```angelscript
void Callback(Item& item, Critter& cr, Item@ usedItem)
```


## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| OreCount | `int` | `0` |  |
| Ore2Count | `int` | `0` |  |
| Callback | `[GatherCallback](prod_tree_firewood.fos.md)` |  |  |

## Functions

### item_init

```angelscript
void item_init(Item& item, bool firstTime)
```

### _NormalDepletable

```angelscript
void _NormalDepletable(Item& item, bool firstTime)
```

### _Advanced

```angelscript
void _Advanced(Item& item, bool firstTime)
```

### _AdvancedDepletable

```angelscript
void _AdvancedDepletable(Item& item, bool firstTime)
```

### _FinishOre

```angelscript
void _FinishOre(Item& item, bool)
```

### _FinishOre2

```angelscript
void _FinishOre2(Item& item, bool)
```

### e_RegenOre

```angelscript
uint e_RegenOre(array<uint>@ values)
```

### e_RegenOre2

```angelscript
uint e_RegenOre2(array<uint>@ values)
```

### _UseItemOre

```angelscript
bool _UseItemOre(Item& item, Critter& cr, Item@ usedItem)
```

### _UseItemOre2

```angelscript
bool _UseItemOre2(Item& item, Critter& cr, Item@ usedItem)
```


