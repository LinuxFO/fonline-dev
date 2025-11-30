---
title: mob_quest.fos
---

# mob_quest.fos

## Includes

- `_macros.fos`
- `_vars.fos`
- `messages_h.fos`
- `npc_common_h.fos`
- `npc_planes_h.fos`
- `utils_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| ROLE_DEFAULT | `(0)` | npc roles (defines distance mob will attack from)) |
| ROLE_AGRESSIVE | `(1)` |  |
| ROLE_AGRESSIVE_NO_MOVE | `(2)` |  |
| ROLE_PASSIVE | `(3)` |  |
| ROLE_PASSIVE_NO_MOVE | `(4)` |  |
| IDLE_NORMAL | `(5000)` | idle time in milseconds (normal is slower for performance issues) |
| IDLE_ALERTED | `(1000)` |  |
| ITEM_DROP_CHANCE | `20` |  |

## Functions

### _MobInit

```angelscript
void _MobInit(Critter& mob, bool firstTime)
```

### _MobInitNoLoot

```angelscript
void _MobInitNoLoot(Critter& mob, bool firstTime)
```

### _MobIdle

```angelscript
void _MobIdle(Critter& mob)
```

### GetDistance

```angelscript
uint GetDistance(Critter& cr)
```

### _MobAttacked

```angelscript
bool _MobAttacked(Critter& cr, Critter& attacker)
```

### _MobAttacking

```angelscript
bool _MobAttacking(Critter& cr, Critter& attacker)
```

### _MobOnMessage

```angelscript
void _MobOnMessage(Critter& cr, Critter& fromCr, int message, int value)
```

### _MobDead

```angelscript
void _MobDead(Critter& cr, Critter@ killer)
```

### _MobSmthDead

```angelscript
void _MobSmthDead(Critter& cr, Critter& killed, Critter@ killer)
```


