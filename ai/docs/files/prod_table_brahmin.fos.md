---
title: prod_table_brahmin.fos
description: " FOnline: 2238 Rotators  prod_table_brahmin.fos ..."
---

# prod_table_brahmin.fos


FOnline: 2238
Rotators

prod_table_brahmin.fos


## Includes

- `_macros.fos`
- `production_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| TEXT_BUTCHERED | `(3010)` |  |
| TEXT_NEED_KNIFE | `(3047)` |  |
| TEXT_NONE_LEFT | `(3050)` |  |

## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| TotalCount | `int` | `0` |  |

## Functions

### item_init

```angelscript
void item_init(Item& item, bool firstTime)
```

### e_Regen

```angelscript
uint e_Regen(array<uint>@ values)
```

### _Finish

```angelscript
void _Finish(Item& item, bool)
```

### _UseItem

```angelscript
bool _UseItem(Item& item, Critter& cr, Item@ itemUsed)
```

### _Skill

```angelscript
bool _Skill(Item& item, Critter& cr, int)
```


