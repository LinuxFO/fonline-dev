---
title: prod_chemicals.fos
description: " FOnline: 2238 Rotators  prod_chemicals.fos ..."
---

# prod_chemicals.fos


FOnline: 2238
Rotators

prod_chemicals.fos


## Includes

- `_macros.fos`
- `production_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| TEXT | `(3075)` |  |
| TEXT_USE_SCIENCE | `(3076)` | #define TEXT_LOW_SKILLS	(3071) |
| PILE_CAPACITY_CHEMICALS | `(6)` |  |
| PILE_CAPACITY_CHEMICALS2 | `(1)` |  |
| PILE_BATCH_CHEMICALS | `(2)` |  |
| PILE_BATCH_CHEMICALS2 | `(2)` |  |

## Functions

### _InitPileChemicals

```angelscript
void _InitPileChemicals(Item& item, bool firstTime)
```

### _SkillPileChemicals

```angelscript
bool _SkillPileChemicals(Item& item, Critter& cr, int skill)
```

### _InitPileChemicals2

```angelscript
void _InitPileChemicals2(Item& item, bool firstTime)
```

### _SkillPileChemicals2

```angelscript
bool _SkillPileChemicals2(Item& item, Critter& cr, int skill)
```

### s_Use

```angelscript
bool s_Use(Critter& crit, Scenery& sc, int skill, Item@ item)
```


