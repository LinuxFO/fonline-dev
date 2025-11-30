---
title: item_brahmin_dung.fos
description: " FOnline: 2238 Rotators  item_brahmin_dung.fos ..."
---

# item_brahmin_dung.fos


FOnline: 2238
Rotators

item_brahmin_dung.fos


## Includes

- `_macros.fos`
- `production_h.fos`
- `town_h.fos`
- `npc_planes_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| TEXT | `(3015)` |  |

## Functions

### item_init

```angelscript
void item_init(Item& item, bool firstTime)
```

### _DungSkill

```angelscript
bool _DungSkill(Item& item, Critter& crit, int skill)
```

### _DungWalk

```angelscript
void _DungWalk(Item& item, Critter& crit, bool entered, uint8 dir)
```

### _UseOnDung

```angelscript
bool _UseOnDung(Item& item, Critter& crit, Item@ usedItem)
```


