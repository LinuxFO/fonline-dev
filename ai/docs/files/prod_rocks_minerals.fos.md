---
title: prod_rocks_minerals.fos
description: " FOnline: 2238 Rotators  prod_rocks_minerals.fos ..."
---

# prod_rocks_minerals.fos


FOnline: 2238
Rotators

prod_rocks_minerals.fos


## Includes

- `_macros.fos`
- `production_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| STR_TEXT_MINERALS | `(3013)` |  |

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
| MineralsCount | `int` | `0` |  |
| Minerals2Count | `int` | `0` |  |
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

### _FinishMinerals

```angelscript
void _FinishMinerals(Item& item, bool)
```

### _FinishMinerals2

```angelscript
void _FinishMinerals2(Item& item, bool)
```

### e_RegenMinerals

```angelscript
uint e_RegenMinerals(array<uint>@ values)
```

### e_RegenMinerals2

```angelscript
uint e_RegenMinerals2(array<uint>@ values)
```

### _UseItemMinerals

```angelscript
bool _UseItemMinerals(Item& item, Critter& cr, Item@ usedItem)
```

### _UseItemMinerals2

```angelscript
bool _UseItemMinerals2(Item& item, Critter& cr, Item@ usedItem)
```


