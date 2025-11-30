---
title: repair.fos
description: " FOnline: 2238 Rotators  repair.fos ..."
---

# repair.fos


FOnline: 2238
Rotators

repair.fos


## Includes

- `_macros.fos`
- `MsgStr.h`
- `utils_h.fos`

## Functions

### RepairCallback

with item - either a tool, or another item of the same type

```angelscript
void RepairCallback(Critter& cr, uint n, string& s)
```

### TryRepairItem

```angelscript
bool TryRepairItem(Critter& cr, Item& item)
```

### TryRepairItemCall

```angelscript
bool TryRepairItemCall(Critter& cr, Item@ item, Item@ with_item)
```

### WearItem

```angelscript
void WearItem(Critter& cr, Item& item, int wearCount)
```

### WearHandsOnDeath

```angelscript
void WearHandsOnDeath(Critter& cr)
```

### SetWear

```angelscript
void SetWear(Item& item, int wearProcent)
```

### SetMinWear

```angelscript
void SetMinWear(Item& item, int wearProcent)
```

### GetWearProcent

```angelscript
int GetWearProcent(Item& item)
```

### CompleteRepair

```angelscript
void CompleteRepair(Item& item)
```

### CloneWear

```angelscript
void CloneWear(Item& to, Item& from)
```

### test

```angelscript
void test(Critter& cr, int, int, int)
```


