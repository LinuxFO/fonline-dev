---
title: car.fos
description: " FOnline: 2238 Rotators  car.fos ..."
---

# car.fos


FOnline: 2238
Rotators

car.fos


## Includes

- `_macros.fos`
- `MsgStr.h`
- `debug_h.fos`
- `entire.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| STR_CAR_INFO | `(2100)` |  |

## Functions

### GetCarCost

```angelscript
uint GetCarCost(uint16 protoCar)
```

### CarMessage

```angelscript
void CarMessage(Critter@ cr, Item@ car, int msg)
```

### UseItemOnCar

```angelscript
bool UseItemOnCar(Critter& cr, Item& car, Item& item)
```

### GetFumbleThreshold

```angelscript
int GetFumbleThreshold(Item& car)
```

### RemoveTool

```angelscript
void RemoveTool(Item& tool)
```

### RepairCar

```angelscript
void RepairCar(Critter& cr, Item& car, Item& tool)
```

### UseSkillOnCar

```angelscript
bool UseSkillOnCar(Critter& cr, Item& car, int skill)
```

### DriveToGlobal

```angelscript
void DriveToGlobal(Critter& cr, Item& car, bool requestGroup)
```

### IsCaravan

```angelscript
bool IsCaravan(Item@ car)
```

### IsBarge

```angelscript
bool IsBarge(Item@ car)
```

### IsFiretruck

```angelscript
bool IsFiretruck(Item@ car)
```

### IsTardis

```angelscript
bool IsTardis(Item@ car)
```

### IsCarTrunk

```angelscript
bool IsCarTrunk(Item@ item)
```

### GetCarTrunkComplexity

```angelscript
int GetCarTrunkComplexity(Item@ item)
```

### MoveCars

```angelscript
void MoveCars(Map& from, Map& to)
```

### GetCartValue

```angelscript
uint GetCartValue(Item& car, uint16 locId)
```

### e_UnlockLockpicking

```angelscript
uint e_UnlockLockpicking(array<uint>@ values)
```

### entrance_city

```angelscript
bool entrance_city(Location& Loc, array<Critter@>& critters, uint8 entrance)
```


