---
title: prod_plant_fiber.fos
description: " FOnline: 2238 Rotators  prod_plant_fiber.fos ..."
---

# prod_plant_fiber.fos


FOnline: 2238
Rotators

prod_plant_fiber.fos


## Includes

- `_macros.fos`
- `production_h.fos`
- `prod_plant_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| TEXT | `(3045)` |  |
| TEXT_EMPTY | `(3049)` |  |

## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| TotalCount | `int` | `0` |  |

## Functions

### item_init

```angelscript
void item_init(Item& item, bool firstTime)
```

### _EncPlant

```angelscript
void _EncPlant(Item& item, bool firstTime)
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
bool _UseSkill(Item&, Critter& cr, int)
```

### _UseItemOnPlant

```angelscript
bool _UseItemOnPlant(Item& item, Critter& cr, Item@ usedItem)
```


