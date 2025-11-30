---
title: raiders_gomes.fos
description: " FOnline: 2238 Rotators  raiders_gomes.fos ..."
---

# raiders_gomes.fos


FOnline: 2238
Rotators

raiders_gomes.fos


## Includes

- `_macros.fos`
- `npc_common_h.fos`
- `messages_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| POS_INSIDE | `(0)` |  |
| POS_OUTSIDE | `(1)` |  |

## Functions

### d_ScheduleTime

Is it time to go out ?

```angelscript
bool d_ScheduleTime()
```

### GetPos

```angelscript
uint GetPos(Critter& critter)
```

### SetPos

```angelscript
void SetPos(Critter& critter, uint pos)
```

### critter_init

```angelscript
void critter_init(Critter& critter, bool firstTime)
```

### _OnMessage

```angelscript
void _OnMessage(Critter& npc, Critter& critter, int num, int val)
```

### _Idle

```angelscript
void _Idle(Critter& critter)
```


