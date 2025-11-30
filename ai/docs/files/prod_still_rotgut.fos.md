---
title: prod_still_rotgut.fos
description: " FOnline: 2238 Rotators  prod_still_rotgut.fos ..."
---

# prod_still_rotgut.fos


FOnline: 2238
Rotators

prod_still_rotgut.fos


## Includes

- `_macros.fos`
- `production_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| FIREWOODS | `# (it) (it.Val1)` |  |
| FRUITS | `# (it) (it.Val2)` |  |

## Functions

### item_init

```angelscript
void item_init(Item& item, bool firstTime)
```

### _Skill

 Using still 

```angelscript
bool _Skill(Item& item, Critter& crit, int skill)
```

### _Item

 Using item on still (inserting ingredients) 

```angelscript
bool _Item(Item& item, Critter& crit, Item@ usedItem)
```

### IsReady

 Checks if still is ready to be used 

```angelscript
bool IsReady(Item& item)
```

### IngredientsReady

```angelscript
bool IngredientsReady(Item& item)
```

### FireReady

```angelscript
bool FireReady(Item& item)
```


