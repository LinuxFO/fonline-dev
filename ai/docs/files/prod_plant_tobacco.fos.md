---
title: prod_plant_tobacco.fos
description: " FOnline: 2238 Rotators  prod_plant_tobacco.fos ..."
---

# prod_plant_tobacco.fos


FOnline: 2238
Rotators

prod_plant_tobacco.fos


## Includes

- `_macros.fos`
- `production_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| TEXT | `(3009)` |  |
| TEXT_EMPTY | `(3053)` |  |

## Classes

### GatherCallback

**Methods**

#### Callback
```angelscript
void Callback(Item& item, Critter&, Item@)
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

### UpdatePic

```angelscript
void UpdatePic(Item& item)
```

### _UseSkill

```angelscript
bool _UseSkill(Item& item, Critter& cr, int skill)
```

### test

```angelscript
void test(Critter& cr, int, int, int)
```


