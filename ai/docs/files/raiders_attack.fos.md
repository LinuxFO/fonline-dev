---
title: raiders_attack.fos
description: " FOnline: 2238 Rotators  raiders_attack.fos ..."
---

# raiders_attack.fos


FOnline: 2238
Rotators

raiders_attack.fos


## Includes

- `_macros.fos`
- `npc_common_h.fos`
- `entire.fos`
- `_ai.fos`
- `npc_planes_h.fos`
- `groups_h.fos`
- `utils_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| ATK_GARBAGER_TIME | `(REAL_MINUTE(30))` |  |
| STATE_MOP_UP | `(0)` |  |
| STATE_GATHER | `(1)` |  |
| STATE_MOP_UP_INSIDE | `(2)` |  |
| STATE_GATHER_INSIDE | `(3)` |  |
| STATE_RETREAT | `(4)` |  |
| STATE_PANIC | `(5)` |  |
| SSTATE_PRE | `(0)` |  |
| SSTATE_GO | `(1)` |  |
| SSTATE_READY | `(2)` |  |
| SSTATE_PRE_INSIDE | `(3)` |  |
| SSTATE_GO_INSIDE | `(4)` |  |
| SSTATE_READY_INSIDE | `(5)` |  |
| SSTATE_WENT_OUTSIDE | `(6)` |  |
| SSTATE_RETREATING | `(7)` |  |
| _GetState | `# (cr)   (attacks[cr.Stat[ST_VAR0]].state)` |  |
| _CrAttack | `# (cr)   attacks[cr.Stat[ST_VAR0]]` |  |
| GO_IN_X | `(52)` |  |
| GO_IN_Y | `(29)` |  |
| GO_OUT_X | `(71)` |  |
| GO_OUT_Y | `(119)` |  |
| CHECKPOINT_OUT_X | `(57)` |  |
| CHECKPOINT_OUT_Y | `(39)` |  |
| CHECKPOINT_IN_X | `(69)` |  |
| CHECKPOINT_IN_Y | `(105)` |  |

## Classes

### CRaidersAttack

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| startNumbers | `uint` |  |  |
| numbers | `uint` |  |  |
| killed | `uint` |  |  |
| lastenemies | `uint` |  |  |
| map_out | `uint` |  |  |
| map_in | `uint` |  |  |
| crits | `array<uint>` |  |  |
| id | `uint` |  |  |
| timeid | `uint` |  |  |
| state | `uint` |  |  |
| finished | `uint` |  |  |
| go_exit_x | `uint` |  |  |
| go_exit_y | `uint` |  |  |

**Methods**

#### Destroy
```angelscript
void Destroy()
```

#### AddCritter
```angelscript
IRaidersAttack@ AddCritter(Critter& cr)
```

#### AddEnemy
```angelscript
void AddEnemy(uint id)
```

#### IsMember
```angelscript
bool IsMember(Critter& cr)
```

#### DeleteCritter
```angelscript
bool DeleteCritter(Critter& cr, bool waskilled)
```

#### SetState
```angelscript
void SetState(uint nstate)
```

#### GatherFinished
```angelscript
void GatherFinished()
```

#### TransferCritter
```angelscript
void TransferCritter(Critter& cr)
```

#### GotoCheckpoint
```angelscript
void GotoCheckpoint(Critter& cr)
```

#### GotoExit
```angelscript
void GotoExit(Critter& cr)
```

#### ReportCritter
```angelscript
void ReportCritter(Critter& cr, Map& map)
```

#### Process
```angelscript
void Process()
```


## Functions

### GravityCentre

```angelscript
void GravityCentre(uint16& hx, uint16& hy, array<Critter@> crits)
```

### GetClosestCritter

```angelscript
Critter@ GetClosestCritter(uint16 hx, uint16 hy, array<Critter@>& crits)
```

### GetFreeAttackNumber

```angelscript
uint GetFreeAttackNumber()
```

### CreateAttack

```angelscript
CRaidersAttack@ CreateAttack()
```

### e_ProcessAttack

```angelscript
uint e_ProcessAttack(array<uint>@ values)
```

### e_GarbageAttacks

```angelscript
uint e_GarbageAttacks(array<uint>@ values)
```

### IsAttackingRaider

```angelscript
bool IsAttackingRaider(Critter& cr)
```

### InitRaidersAttacks

```angelscript
bool InitRaidersAttacks()
```

### RaidersAttack

```angelscript
bool RaidersAttack(Location& loc)
```

### critter_init

```angelscript
void critter_init(Critter& cr, bool firstTime)
```

### _RaiderIdle

```angelscript
void _RaiderIdle(Critter& cr)
```

### _RaiderDead

```angelscript
void _RaiderDead(Critter& cr, Critter@ killer)
```

### _RaiderFinish

```angelscript
void _RaiderFinish(Critter& cr, bool deleted)
```

### _RaiderPlaneEnd

```angelscript
bool _RaiderPlaneEnd(Critter& cr, NpcPlane& plane, int reason, Critter@ someCr, Item@ item)
```

### _RaiderShowCritter

```angelscript
void _RaiderShowCritter(Critter& cr, Critter& showCrit)
```

### commence

```angelscript
void commence(Critter& cr, int p0, int p1, int p2)
```


