---
title: critter_description.fos
description: " FOnline: 2238 Rotators  critter_description.fos ..."
---

# critter_description.fos


FOnline: 2238
Rotators

critter_description.fos


## Includes

- `_defines.fos`
- `_macros.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __CRITTER_DESCRIPTION__ |  |  |
| CRD_MINSPECIAL | `(0)` |  |
| CRD_MAXSPECIAL | `(3)` |  |
| CRD_MAXRANGE | `(99)` |  |
| CRD_MAXINDEX | `(99)` |  |

## Functions

### numDigits

```angelscript
uint numDigits(int number)
```

### extractDigit

```angelscript
uint extractDigit(int number, int pos)
```

### BestSpecial

```angelscript
array<uint> BestSpecial(Critter& player, uint count)
```

### WorstSpecial

```angelscript
array<uint> WorstSpecial(Critter& player, uint count)
```

### BestWorstSpecial

```angelscript
array<uint> BestWorstSpecial(Critter& player, int count, bool best)
```

### info

```angelscript
void       info(Critter& player, int, int, int)
```

### CritterDescription_CheckTable

```angelscript
bool CritterDescription_CheckTable()
```

### CritterDescription_Get

```angelscript
string@ CritterDescription_Get(uint description1, uint description2)
```

### CritterDescription_Set

```angelscript
void CritterDescription_Set(Critter& player, int& description1, int& description2)
```

### say_description

```angelscript
void say_description(Critter& player, int d1, int d2)
```

### set_test

```angelscript
void set_test(Critter& player, int, int, int)
```

### get

```angelscript
void get(Critter& player, int d1, int d2, int)
```


