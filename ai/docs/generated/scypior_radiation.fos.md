---
title: scypior_radiation.fos
description: " FOnline: 2238 Rotators  scypior_radiation.fos ..."
---

# scypior_radiation.fos


FOnline: 2238
Rotators

scypior_radiation.fos


## Includes

- `_macros.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| RADIATION_DEATH_TIMEOUT | `(REAL_SECOND(180))` |  |

## Classes

### CEffect

 Effect regarding stat loss 

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| stats | `array<uint>` |  |  |
| values | `array<int>` |  |  |
| level | `uint` |  | radiation level after which effect is applied |
| message | `uint` |  | message index |

**Methods**

#### Stat
 Adds stat to the effect 

```angelscript
CEffect@ Stat(uint stat, int val)
```

#### Apply
 Apply effect to given critter 

```angelscript
void Apply(Critter& cr)
```

#### Remove
 Remove effect from given critter 

```angelscript
void Remove(Critter& cr)
```

#### _apply
 Helper 

```angelscript
void _apply(Critter& cr, uint stat, int val, bool remove)
```


## Functions

### Irradiate

 Irradiate/decrease radiation level of the critter 

```angelscript
void Irradiate(Critter& cr, int dose)
```

### HealRadiation

 Called after replication 

```angelscript
void HealRadiation(Critter& cr)
```

### list_levels

```angelscript
void list_levels(Critter& crit, int p0, int p1, int p2)
```

### InitRadiationEffects

 Initializes radiation effects table; 

```angelscript
void InitRadiationEffects()
```

### GetEffect

 Retrieves effect that should be applied for given level 

```angelscript
CEffect@ GetEffect(uint level)
```

### RadiationDirectEffects

 Handles direct effects(stat loss etc)  prevLevel - previous radiation level currLevel - current radiation level

```angelscript
void RadiationDirectEffects(Critter& cr, uint prevLevel, uint currLevel)
```

### RadiationDamage

 Damages critter basing on radiation level 

```angelscript
void RadiationDamage(Critter& cr)
```

### SideEffectChance

 Determines whether side effect should occur Period is average seconds interval, for the minimum effect threshold period is shorter if radiation level is higher than effect threshold 

```angelscript
bool SideEffectChance(Critter& cr, uint threshold, uint period)
```

### Vomit

```angelscript
void Vomit(Critter& cr)
```

### vomit_test

```angelscript
void vomit_test(Critter& cr, int p0, int p1, int p2)
```

### _BarfSkill

```angelscript
bool _BarfSkill(Item& item, Critter& crit, int skill)
```

### _BarfWalk

```angelscript
void _BarfWalk(Item& item, Critter& crit, bool entered, uint8 dir)
```

### e_BarfRemove

```angelscript
uint e_BarfRemove(array<uint>@ values)
```

### RadiationSideEffects

```angelscript
void RadiationSideEffects(Critter& cr)
```


