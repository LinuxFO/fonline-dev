---
title: prod_tree_firewood.fos
description: " FOnline: 2238 Rotators  prod_tree_firewood.fos ..."
---

# prod_tree_firewood.fos


FOnline: 2238
Rotators

prod_tree_firewood.fos


## Includes

- `_macros.fos`
- `production_h.fos`
- `utils_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| TEXT_CHOPPED | `(3016)` |  |
| TEXT_NONE_LEFT | `(3051)` |  |

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
| RegenerableCount | `int` | `0` |  |
| Callback | `[GatherCallback](prod_tree_firewood.fos.md)` |  |  |

## Functions

### item_init

normal, regenerable

```angelscript
void item_init(Item& item, bool firstTime)
```

### _FinishRegenerable

```angelscript
void _FinishRegenerable(Item& item, bool)
```

### _EncTree

non regenerable, for encounters

```angelscript
void _EncTree(Item& item, bool firstTime)
```

### e_Regen

```angelscript
uint e_Regen(array<uint>@ values)
```

### ChangePic

```angelscript
void ChangePic(Item& item)
```

### _UseItemOnTree

```angelscript
bool _UseItemOnTree(Item& item, Critter& cr, Item@ usedItem)
```

### _UseSkill

```angelscript
bool _UseSkill(Item& item, Critter& cr, int skill)
```


