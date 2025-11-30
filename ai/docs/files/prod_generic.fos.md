---
title: prod_generic.fos
description: " FOnline: 2238 Rotators  prod_generic.fos ..."
---

# prod_generic.fos


FOnline: 2238
Rotators

prod_generic.fos


## Includes

- `_macros.fos`
- `production_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| TEXT_NONE_LEFT | `(3052)` |  |
| TEXT_CHEMICALS | `(3075)` |  |
| TEXT_CHEMICALS_HINT | `(3076)` |  |
| TEXT_CHEMICALS2 | `(3091)` |  |
| TEXT_CHEMICALS2_HINT |  |  |
| TEXT_COMPUTER | `(3070)` |  |
| TEXT_COMPUTER_HINT | `(3072)` |  |
| TEXT_COMPUTER2 | `(3089)` |  |
| TEXT_COMPUTER2_HINT | `(3090)` |  |
| USE_SKILL | `\` |  |

## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| ComputerCount | `int` | `0` |  |
| Computer2Count | `int` | `0` |  |
| ChemicalsCount | `int` | `0` |  |
| Chemicals2Count | `int` | `0` |  |

## Functions

### _Chemicals

```angelscript
void _Chemicals(Item& item, bool firstTime)
```

### _SkillChemicals

```angelscript
bool _SkillChemicals(Item& item, Critter& cr, int skill)
```

### _FinishChemicals

```angelscript
void _FinishChemicals(Item& item, bool)
```

### e_RegenChemicals

```angelscript
uint e_RegenChemicals(array<uint>@ values)
```

### _Chemicals2

```angelscript
void _Chemicals2(Item& item, bool firstTime)
```

### _SkillChemicals2

```angelscript
bool _SkillChemicals2(Item& item, Critter& cr, int skill)
```

### _FinishChemicals2

```angelscript
void _FinishChemicals2(Item& item, bool)
```

### e_RegenChemicals2

```angelscript
uint e_RegenChemicals2(array<uint>@ values)
```

### _Computer

```angelscript
void _Computer(Item& item, bool firstTime)
```

### _SkillComputer

```angelscript
bool _SkillComputer(Item& item, Critter& cr, int skill)
```

### _FinishComputer

```angelscript
void _FinishComputer(Item& item, bool)
```

### e_RegenComputer

```angelscript
uint e_RegenComputer(array<uint>@ values)
```

### _Computer2

```angelscript
void _Computer2(Item& item, bool firstTime)
```

### _SkillComputer2

```angelscript
bool _SkillComputer2(Item& item, Critter& cr, int skill)
```

### _FinishComputer2

```angelscript
void _FinishComputer2(Item& item, bool)
```

### e_RegenComputer2

```angelscript
uint e_RegenComputer2(array<uint>@ values)
```


