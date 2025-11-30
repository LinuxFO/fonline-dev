---
title: triggers.fos
description: " FOnline: 2238 Rotators  triggers.fos ..."
---

# triggers.fos


FOnline: 2238
Rotators

triggers.fos


## Includes

- `_macros.fos`
- `triggers_h.fos`
- `triggers_funcs.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __TRIGGERS__ |  |  |

## Functions

### _Trigger

Trigger initialization 

```angelscript
void _Trigger(Item& tr, bool firstTime)
```

### TriggerInit

```angelscript
void TriggerInit(Item@ tr, uint funcId, uint settings, uint delay, uint nextTick)
```

### hexHasTrigger

Returns true if hex has a trigger of specific type 

```angelscript
bool hexHasTrigger(Map@ map, uint16 x, uint16 y, int func, int settings)
```

### _TriggerStep

Called when critter steps on a trigger 

```angelscript
void _TriggerStep(Item& tr, Critter& cr, bool entered, uint8 dir)
```

### e_TriggerTick

Trigger tick - calling the trigger function 

```angelscript
uint e_TriggerTick(array<uint>@ values)
```


