---
title: prod_rocks_uranium.fos
description: " FOnline: 2238 Rotators  prod_rocks_uranium.fos ..."
---

# prod_rocks_uranium.fos


FOnline: 2238
Rotators

prod_rocks_uranium.fos


## Includes

- `_macros.fos`
- `production_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| STR_TEXT | `(3031)` |  |

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
| TotalCount | `int` | `0` |  |
| Callback | `[GatherCallback](prod_tree_firewood.fos.md)` |  |  |

## Functions

### item_init

```angelscript
void item_init(Item& item, bool firstTime)
```

### _Finish

```angelscript
void _Finish(Item& item, bool)
```

### e_Regen

```angelscript
uint e_Regen(array<uint>@ values)
```

### _UseItem

```angelscript
bool _UseItem(Item& item, Critter& cr, Item@ usedItem)
```


