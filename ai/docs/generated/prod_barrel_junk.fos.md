---
title: prod_barrel_junk.fos
description: " FOnline: 2238 Rotators  prod_barrel_junk.fos ..."
---

# prod_barrel_junk.fos


FOnline: 2238
Rotators

prod_barrel_junk.fos


## Includes

- `_macros.fos`
- `production_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| TEXT_JUNK | `(3014)` |  |
| OBJECT_USE_TIMES | `(Random(1, 3))` |  |
| PROD_REGEN_TIME | `(REAL_SECOND(Random(60, 120)))` |  |
| PROD_MAX_JUNK | `(30)` |  |

## Classes

### GatherCallback

**Methods**

#### Callback
```angelscript
void Callback(Item& item, Critter& cr, Item@)
```


## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| Callback | `[GatherCallback](prod_tree_firewood.fos.md)` |  |  |

## Functions

### item_init

```angelscript
void item_init(Item& item, bool firstTime)
```

### _Drop

```angelscript
void _Drop(Item& item, Critter& cr)
```

### _Skill

```angelscript
bool _Skill(Item& item, Critter& cr, int skill)
```

### e_Regen

```angelscript
uint e_Regen(array<uint>@ values)
```

### _Junk

```angelscript
void _Junk(Item& item, bool firstTime)
```

### _Gather

```angelscript
bool _Gather(Item& item, Critter& crit, int skill)
```


