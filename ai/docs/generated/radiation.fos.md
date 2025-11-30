---
title: radiation.fos
description: " FOnline: 2238 Rotators  radiation.fos ..."
---

# radiation.fos


FOnline: 2238
Rotators

radiation.fos


## Includes

- `_macros.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| RADIATION_STAGES | `(6)` |  |
| RADIATION_STATS | `(8)` |  |
| RADIATION_DURATION | `(10080)` |  |
| RADIATION_DAMAGE_VALUE | `(66)` |  |
| RADIATION_HIGH_DOSE | `(66)` |  |
| RADIATION_DEAD_DOSE | `(1800)` |  |
| STR_RADIATION_STAGE | `# (stage) (12799 + (stage))` |  |
| STR_RADIATION_DIE | `(12806)` |  |
| STR_RADIATION_HIGH_DOSE | `(12807)` |  |
| TABLE_STAGE_VALUE | `# (stage)          RadiationEffects[(stage) - 1]` | Table offsets |
| TABLE_STAT_INDEX | `# (stat)            RadiationEffects[6 + (stat) * 7]` |  |
| TABLE_STAT_AMOUNT | `# (stat, stage)RadiationEffects[6 + (stat) * 7 + (stage)]` |  |

## Functions

### AffectRadiation

```angelscript
void AffectRadiation(Critter& cr, int value)
```

### DropRadiation

```angelscript
void DropRadiation(Critter& cr)
```


