---
title: poison.fos
description: " FOnline: 2238 Rotators  poison.fos ..."
---

# poison.fos


FOnline: 2238
Rotators

poison.fos


## Includes

- `_macros.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| POISON_BASE_DURATION | `(505)` |  |
| POISON_DURATION_SUB | `(5)` |  |
| STR_POISON_GAIN | `(12810)` |  |
| STR_POISON_PROCESS | `(12811)` |  |
| STR_POISON_REDUCE | `(12812)` |  |
| STR_POISON_FREE | `(12813)` |  |
| STR_POISON_DEATH | `(12814)` |  |

## Functions

### AffectPoison

```angelscript
void AffectPoison(Critter& cr, int value)
```

### DropPoison

```angelscript
void DropPoison(Critter& cr)
```

### cte_Poison

```angelscript
uint cte_Poison(Critter& cr, int identifier, uint& rate)
```

### GetPoisonDuration

```angelscript
uint GetPoisonDuration(Critter& cr)
```


