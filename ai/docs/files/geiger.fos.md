---
title: geiger.fos
description: " FOnline: 2238 Rotators  geiger.fos ..."
---

# geiger.fos


FOnline: 2238
Rotators

geiger.fos


## Includes

- `_macros.fos`
- `_colors.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| GEIGER_DURATION | `(REAL_SECOND(12))` |  |
| GEIGER_HEX_RANGE | `(20)` |  |
| GEIGER_ENERGY_CHARGE | `(10)` |  |
| GEIGER_FUSION_CHARGE | `(50)` |  |
| STR_GEIGER_NO_CHARGES | `(10350)` |  |
| STR_GEIGER_ON | `(10351)` |  |
| STR_GEIGER_OFF | `(10352)` |  |
| STR_GEIGER_FIRST_CHECK | `(10353)` |  |
| STR_GEIGER_LOOP_CHECK | `(10354)` |  |
| STR_GEIGER_NOTHING | `(10355)` |  |
| STR_GEIGER_ADD_CHARGE | `(10356)` |  |
| STR_GEIGER_CUR_CHARGE | `(10357)` |  |

## Functions

### _GeigerInit

```angelscript
void _GeigerInit(Item& item, bool firstTime)
```

### _UseGeiger

```angelscript
bool _UseGeiger(Item& geiger, Critter& cr, Critter@ onCritter, Item@ onItem, Scenery@ onScenery)
```

### _UseItemOnGeiger

```angelscript
bool _UseItemOnGeiger(Item& geiger, Critter& cr, Item@ item)
```

### _UseSkillOnGeiger

```angelscript
bool _UseSkillOnGeiger(Item& geiger, Critter& cr, int skill)
```

### e_Geiger

```angelscript
uint e_Geiger(array<uint>@ values)
```


