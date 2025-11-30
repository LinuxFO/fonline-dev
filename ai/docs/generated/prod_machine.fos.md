---
title: prod_machine.fos
description: " FOnline: 2238 Rotators  prod_machine.fos ..."
---

# prod_machine.fos


FOnline: 2238
Rotators

prod_machine.fos


## Includes

- `_macros.fos`
- `production_h.fos`
- `prod_ingredients_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| INTERVAL | `(10)` |  |
| MACHINE_ROTGUT | `(0)` |  |
| MACHINE_BEER | `(1)` |  |
| MACHINE_NUKACOLA | `(2)` |  |
| MACHINE_CIGARETTES | `(3)` |  |
| MACHINE_FIBER2 | `(4)` |  |
| MACHINE_IDX | `# (item)     (item.Val5)` |  |
| WORKING | `# (item) (item.Val6)` |  |

## Classes

### Machine

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| resource | `uint16` |  |  |
| batch | `int` |  |  |
| cap | `int` |  |  |
| text | `uint` |  | text displayed after obtaining rsource |
| textWorking | `uint` |  | text if busy |
| textSound | `uint` |  | sounds |
| fromFrame | `uint8` |  | use animation frames |
| toFrame | `uint8` |  |  |
| ingredients | `array<int>` |  | required ingredients (pid, required amount, text_required, text_inserted) |
| time | `int` |  | working time, seconds |

**Methods**

#### Require
 #ifndef __DEBUG__ // scyp' void Require(uint16 pid, int count, int text_required, int text_inserted) { ingredients.insertLast(pid); #endif 

```angelscript
void Require(uint8 ingredient, int count, int text_required, int text_inserted)
```

#### Animation
```angelscript
void Animation(uint8 fromFrame, uint8 toFrame)
```

#### Animate
```angelscript
void Animate(Item& item)
```

#### UseSkill
```angelscript
bool UseSkill(Item& item, Critter& cr, int skill)
```

#### SpawnResources
```angelscript
void SpawnResources(Item& item, int ntimes)
```

#### SaySound
```angelscript
void SaySound(Item& item)
```


## Functions

### InitMachines

```angelscript
void InitMachines()
```

### _Rotgut

```angelscript
void _Rotgut(Item& item, bool firstTime)
```

### _Beer

```angelscript
void _Beer(Item& item, bool firstTime)
```

### _NukaCola

```angelscript
void _NukaCola(Item& item, bool firstTime)
```

### _Cigarettes

```angelscript
void _Cigarettes(Item& item, bool firstTime)
```

### _Fiber2

```angelscript
void _Fiber2(Item& item, bool firstTime)
```

### _UseSkill

```angelscript
bool _UseSkill(Item& item, Critter& cr, int skill)
```

### e_Brew

```angelscript
uint e_Brew(array<uint>@ values)
```

### test

```angelscript
void test(Critter& player, int type, int, int)
```


