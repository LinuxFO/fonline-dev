---
title: prod_plant_fruit.fos
description: " FOnline: 2238 Rotators  prod_plant_fruit.fos ..."
---

# prod_plant_fruit.fos


FOnline: 2238
Rotators

prod_plant_fruit.fos


## Includes

- `_macros.fos`
- `production_h.fos`
- `prod_plant_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| TEXT | `(3011)` |  |
| TEXT_NONE | `(3048)` |  |

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

### _EncPlant

```angelscript
void _EncPlant(Item& item, bool firstTime)
```

### UpdatePic

```angelscript
void UpdatePic(Item& item)
```

### _UsePlant

```angelscript
bool _UsePlant(Item& item, Critter& cr, int skill)
```

### test

```angelscript
void test(Critter& cr, int p0, int p1, int p2)
```


