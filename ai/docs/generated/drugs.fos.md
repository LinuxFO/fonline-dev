---
title: drugs.fos
description: "FOnline: 2238 Rotators  drugs.fos ..."
---

# drugs.fos

FOnline: 2238
Rotators

drugs.fos


## Includes

- `_macros.fos`
- `MsgStr.h`
- `drugs_data.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| DRUG_EFFECT_DIV2_DURATION | `(8)` |  #define DRUG_EFFECT_DIV2_WITHDRAWAL    (1) #define DRUG_EFFECT_MUL2_ADDICTION     (2) #define DRUG_EFFECT_DIV2_ADDICTION     (4)  |
| DRUG_EFFECT_MUL2_DURATION | `(16)` |  |
| DRUG_EFFECT_ADDICTION_INFINITE | `(32)` |  |
| DRUG_EFFECT_ADDICTION_IGNORE | `(64)` |  |
| RATE_TO_STAGE | `# (rate)          ((rate) & 0xFFFFFF)` |  |
| RATE_TO_FLAGS | `# (rate)          ((rate) >> 24)` |  |
| FORM_RATE | `# (stage, flags)((((flags) & 0xFF) << 24) | ((stage) & 0xFFFFFF))` |  |
| TABLE_DRUG_ADDICT | `(0)` | Table offsets |
| TABLE_DRUG_PROC | `(1)` |  |
| TABLE_DURATION | `# (stage)      (2 + (stage))` |  |
| TABLE_STAT | `# (stat)           (6 + (stat) * 6)` |  |
| TABLE_AMOUNT | `# (stat, stage)(7 + (stage) + (stat) * 6)` |  |
| SPECIAL_DRUG | `# (_pid) ((_pid) == PID_MENTATS || (_pid) == PID_BUFFOUT || (_pid) == PID_PSYCHO || (_pid) == PID_JET || (_pid) == PID_BEER || (_pid) == PID_NUKA_COLA || (_pid) == PID_CIGARETTES || (_pid) == PID_RAD_X)` | Dumbed Down Drugs (only two stages) |

## Functions

### UseDrug

```angelscript
void UseDrug(Critter& cr, Item& drug)
```

### UseDrugOn

```angelscript
void UseDrugOn(Critter& cr, Critter& onCr, Item& drug)
```

### DropDrugsEffectsHinkley

```angelscript
void DropDrugsEffectsHinkley(Critter& cr)
```

### DropDrugEffects

```angelscript
void DropDrugEffects(Critter& cr)
```

### DropDrugEffects

```angelscript
void DropDrugEffects(Critter& cr, bool dropAddictions)
```

### SetDrug

```angelscript
void SetDrug(Critter& cr, uint16 drugPid)
```

### ProcessDrug

```angelscript
uint ProcessDrug(Critter& cr, uint16 drugPid, uint& rate)
```

### DropDrug

```angelscript
void DropDrug(Critter& cr, uint16 drugPid, uint stage)
```

### cte_Drug

```angelscript
uint cte_Drug(Critter& cr, int identifier, uint& rate)
```

### SetDrugTimer

```angelscript
void SetDrugTimer(Critter& cr, uint16 drugPid, uint timer)
```

### UpdateDrugs

```angelscript
void UpdateDrugs(Critter& cr)
```

### RefreshDrug

```angelscript
bool RefreshDrug(Critter& cr, uint16 drugPid, uint& rate)
```


