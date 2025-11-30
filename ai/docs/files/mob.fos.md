---
title: mob.fos
description: " FOnline: 2238 Rotators  mob.fos ..."
---

# mob.fos


FOnline: 2238
Rotators

mob.fos


## Includes

- `_macros.fos`
- `npc_planes_h.fos`
- `npc_roles_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| ROLE_DEFAULT | `(0)` | npc roles (defines distance mob will attack from)) |
| ROLE_AGRESSIVE | `(1)` |  |
| ROLE_PASSIVE | `(2)` |  |
| ALERTED | `# (cr)           (cr.StatBase[ST_VAR1])` | useful variables |
| IDLE_NORMAL | `(5000)` | idle time in milseconds (normal is slower for performance issues) |
| IDLE_ALERTED | `(1000)` |  |
| IDLE_ALERTED_2 | `(200)` |  |

## Functions

### critter_init

```angelscript
void critter_init(Critter& mob, bool firstTime)
```

### critter_init_aggr

```angelscript
void critter_init_aggr(Critter& mob, bool firstTime)
```

### _DontMove

```angelscript
void _DontMove(Critter& mob, bool firstTime)
```

### _MineMob

```angelscript
void _MineMob(Critter& mob, bool firstTime)
```

### critter_init_half_agro

```angelscript
void critter_init_half_agro(Critter& mob, bool firstTime)
```

### _MobIdleHalfAgro

```angelscript
void _MobIdleHalfAgro(Critter& mob)
```

### _MineMobIdle

```angelscript
void _MineMobIdle(Critter& mob)
```

### _MobIdle

```angelscript
void _MobIdle(Critter& mob)
```

### _MobIdle2

Critter stays on his spot, does not move randomly around.

```angelscript
void _MobIdle2(Critter& mob)
```

### _MobDead

```angelscript
void _MobDead(Critter& mob, Critter@ killer)
```

### MoveMob

```angelscript
void MoveMob(Critter& mob, bool run)
```

### GetDistance

 Gets distance after which critter becomes agressive 

```angelscript
uint GetDistance(Critter& mob)
```

### _MobShowCritter

 Alerts that oponent is near 

```angelscript
void _MobShowCritter(Critter& mob, Critter& showCrit)
```

### _MobHideCritter

```angelscript
void _MobHideCritter(Critter& mob, Critter& hideCrit)
```

### _MobDead

```angelscript
void _MobDead(Critter& mob)
```

### _MobIdleAggr

```angelscript
void _MobIdleAggr(Critter& mob)
```

### _MobShowCritterAggr

```angelscript
void _MobShowCritterAggr(Critter& mob, Critter& showCrit)
```


