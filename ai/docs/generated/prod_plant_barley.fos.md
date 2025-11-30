---
title: prod_plant_barley.fos
description: " FOnline: 2238 Rotators  prod_plant_barley.fos ..."
---

# prod_plant_barley.fos


FOnline: 2238
Rotators

prod_plant_barley.fos


## Includes

- `_macros.fos`
- `production_h.fos`
- `logging_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| TEXT_GATHERED | `(3008)` |  |
| TEXT_EMPTY | `(3053)` |  |

## Classes

### GatherCallback

**Methods**

#### Callback
```angelscript
void Callback(Item& item, Critter& cr, Item@ used_item)
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

### _UseSkill

```angelscript
bool _UseSkill(Item& item, Critter& cr, int skill)
```

### UpdatePic

```angelscript
void UpdatePic(Item& item)
```


