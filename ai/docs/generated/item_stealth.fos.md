---
title: item_stealth.fos
description: " FOnline: 2238 Rotators  item_stealth.fos ..."
---

# item_stealth.fos


FOnline: 2238
Rotators

item_stealth.fos


## Includes

- `_macros.fos`
- `MsgStr.h`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| STR_STEALTHBOY_DEPLETED | `(4800)` |  |
| STR_STEALTHBOY_ON | `(4801)` |  |
| STR_STEALTHBOY_OFF | `(4802)` |  |
| STR_STEALTHBOY_CHARGED | `(4803)` |  |
| STR_STEALTHBOY_CHARGES_LEFT | `(4804)` |  |
| STR_SENSOR_DEPLETED | `(4900)` |  |
| STR_SENSOR_ON | `(4901)` |  |
| STR_SENSOR_OFF | `(4902)` |  |
| STR_SENSOR_CHARGED | `(4903)` |  |
| STR_SENSOR_CHARGES_LEFT | `(4904)` |  |
| DEVICE_SEC_TIME | `(12)` |  |
| DEVICE_MFC_TIME | `(30)` |  |

## Functions

### _StealthBoyInit

stealth boy vals: 1 - on/off, 3 - event id

```angelscript
void _StealthBoyInit(Item& item, bool firstTime)
```

### _StealthBoyUse

```angelscript
bool _StealthBoyUse(Item& item, Critter& crit, Critter@ onCritter, Item@ onItem, Scenery@ onScenery)
```

### e_StealthBoy

```angelscript
uint e_StealthBoy(array<uint>@ values)
```

### OnStealthBoyOn

```angelscript
void OnStealthBoyOn(Item& item)
```

### OnStealthBoyOff

```angelscript
void OnStealthBoyOff(Item& item)
```

### _MotionSensorInit

motion sensor vals: 1 - on/off, 3 - event id

```angelscript
void _MotionSensorInit(Item& item, bool firstTime)
```

### _MotionSensorUse

```angelscript
bool _MotionSensorUse(Item& item, Critter& crit, Critter@ onCritter, Item@ onItem, Scenery@ onScenery)
```

### e_MotionSensor

```angelscript
uint e_MotionSensor(array<uint>@ values)
```

### OnMotionSensorOn

```angelscript
void OnMotionSensorOn(Item& item)
```

### OnMotionSensorOff

```angelscript
void OnMotionSensorOff(Item& item)
```

### _DeviceUseOnMe

```angelscript
bool _DeviceUseOnMe(Item& item, Critter& cr, Item@ usedItem)
```

### _DeviceSkill

```angelscript
bool _DeviceSkill(Item& device, Critter& cr, int skill)
```

### TryRechargeItem

```angelscript
bool TryRechargeItem(Critter& cr, Item& item)
```

### RechargeCallback

```angelscript
void RechargeCallback(Critter& cr, uint n, string& s)
```


