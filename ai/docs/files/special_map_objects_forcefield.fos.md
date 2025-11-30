---
title: special_map_objects_forcefield.fos
description: " FOnline: 2238 Rotators  special_map_objects_forcefield.fos ..."
---

# special_map_objects_forcefield.fos


FOnline: 2238
Rotators

special_map_objects_forcefield.fos


## Included By

- [special_map_objects.fos](special_map_objects.fos.md)

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| FORCEFIELD_ON | `(0x01)` | forceField flags |
| FORCEFIELD_HALF_INTEGRITY | `(0x02)` |  |
| FORCEFIELD_DESTROYED | `(0x04)` |  |
| FORCEFIELD_DISRUPTED | `(0x08)` |  |
| FORCEFIELD_FLICKERED | `(0x10)` |  |
| FORCEFIELD_REPAIRABLE_WHENOFF | `(0x20)` |  |
| FORCEFIELD_FULL_OFF | `(0x00)` | forceField values |
| FORCEFIELD_FULL_ON | `(0x01)` |  |
| FORCEFIELD_HALVED_OFF | `(0x02)` |  |
| FORCEFIELD_HALVED_ON | `(0x03)` |  |
| FORCEFIELD_DEFAULT_RESPAWN_INTERVAL | `(120)` |  |
| EMITTER_COMPLEXITY | `# (emitter) (emitter.Val1)` |  |
| DEFAULT_EMITTER_COMPLEXITY | `(60)` |  |
| FORCEFIELD_BACKAGAIN_INTERVAL | `(10)` |  |
| FORCEFIELD1_SPAWNER_PID | `(10002)` | protos |
| FORCEFIELD1_FULL_PID | `(PID_FORCEFIELD_YELLOW_1)` |  |
| FORCEFIELD1_HALVED_PID | `(10000)` |  |
| FORCEFIELD2_SPAWNER_PID | `(10003)` |  |
| FORCEFIELD2_FULL_PID | `(PID_FORCEFIELD_YELLOW_2)` |  |
| FORCEFIELD2_HALVED_PID | `(10001)` |  |
| FORCEFIELD_TYPE_1 | `(0)` |  |
| FORCEFIELD_TYPE_2 | `(1)` |  |
| FORCEFIELD_DAMAGE | `(Random(15, 30))` |  |

## Classes

### CForceFieldSearcher

**Methods**

#### FindTogglableSMOs
```angelscript
uint FindTogglableSMOs(array<ITogglableSMO@>& list, Map& map, int globalId)
```

#### FindForceFieldObjects
```angelscript
uint FindForceFieldObjects(array<MapForceFieldObject@>& list, Map& map, int id)
```

#### FindSingleForceField
```angelscript
MapForceFieldObject@ FindSingleForceField(Map& map, int id)
```

### MapForceFieldObject

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| spawner | `Item@` |  |  |
| map | `Map@` |  |  |
| fullFieldPid | `uint` |  |  |
| halvedFieldPid | `uint` |  |  |

**Methods**

#### GetRespawnInterval
```angelscript
uint GetRespawnInterval()
```

#### IsOn
```angelscript
bool IsOn()
```

#### IsOff
```angelscript
bool IsOff()
```

#### IsFlickered
```angelscript
bool IsFlickered()
```

#### IsDisrupted
```angelscript
bool IsDisrupted()
```

#### IsNotDisrupted
```angelscript
bool IsNotDisrupted()
```

#### IsDestroyed
```angelscript
bool IsDestroyed()
```

#### IsNotDestroyed
```angelscript
bool IsNotDestroyed()
```

#### IsFull
```angelscript
bool IsFull()
```

#### IsHalved
```angelscript
bool IsHalved()
```

#### IsRepairableWhenOff
```angelscript
bool IsRepairableWhenOff()
```

#### IsRepairableWhenOff
```angelscript
void IsRepairableWhenOff(bool repairable)
```

#### GetCurPid
```angelscript
uint GetCurPid()
```

#### Toggle
```angelscript
void Toggle()
```

#### ForceOn
```angelscript
void ForceOn()
```

#### TurnOn
```angelscript
void TurnOn()
```

#### TurnOff
```angelscript
void TurnOff()
```

#### UseDisruptSkill
```angelscript
bool UseDisruptSkill(Critter& player, int skill, int complexity)
```

#### Disrupt
```angelscript
void Disrupt()
```

#### Undisrupt
```angelscript
void Undisrupt()
```

#### Flicker
```angelscript
void Flicker(uint id)
```

#### DamageCritter
```angelscript
void DamageCritter()
```

#### Explode
```angelscript
void Explode(Item& emitter)
```

#### SetRespawnEvent
```angelscript
void SetRespawnEvent(Item@ emitter)
```

#### Respawn
```angelscript
void Respawn(Item@ emitter)
```

#### SetFull
```angelscript
void SetFull()
```

#### SetHalved
```angelscript
void SetHalved()
```


## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| blankHash | `uint` | `GetStrHash("art/items/blank.png")` |  |
| ForceFieldSearcher | `[CForceFieldSearcher](special_map_objects_forcefield.fos.md)@` | `CForceFieldSearcher()` |  |

## Functions

### _InitNSEmitter

// mapper objects inits

```angelscript
void _InitNSEmitter(Item& emitter, bool first)
```

### e_InitNSEmitter

```angelscript
uint e_InitNSEmitter(array<uint>@ values)
```

### _InitWEEmitter

```angelscript
void _InitWEEmitter(Item& emitter, bool first)
```

### e_InitWEEmitter

```angelscript
uint e_InitWEEmitter(array<uint>@ values)
```

### GetEmitterOnHex

```angelscript
Item@ GetEmitterOnHex(Map& map, uint16 hexX, uint16 hexY)
```

### ExplodeEmitterOnHex

```angelscript
void ExplodeEmitterOnHex(Map& map, uint16 hexX, uint16 hexY)
```

### _InitForceFieldSpawner1

```angelscript
void _InitForceFieldSpawner1(Item& spawner, bool firstTime)
```

### _InitForceFieldSpawner2

```angelscript
void _InitForceFieldSpawner2(Item& spawner, bool firstTime)
```

### _InitHalvedField

```angelscript
void _InitHalvedField(Item& item, bool firstTime)
```

### _HalvedFieldWalk

```angelscript
void _HalvedFieldWalk(Item& trap, Critter& cr, bool entered, uint8 dir)
```

### GetForceFieldTypeBySpawnerPid

```angelscript
int GetForceFieldTypeBySpawnerPid(uint pid)
```

### GetBrokenEmitterPid

```angelscript
uint GetBrokenEmitterPid(uint workingPid)
```

### GetWorkingEmitterPid

```angelscript
uint GetWorkingEmitterPid(uint brokenPid)
```

### DisableForceFieldTemporarily

```angelscript
void DisableForceFieldTemporarily(Map@ map, Item& emitter)
```

### _InitEmitter

```angelscript
void _InitEmitter(Item& item, bool first)
```

### _ForceFieldEmitterUse

```angelscript
bool _ForceFieldEmitterUse(Item& emitter, Critter& player, int skill)
```

### e_TurnOnAgain

```angelscript
uint e_TurnOnAgain(array<uint>@ values)
```

### d_IsForceFieldOn

```angelscript
bool d_IsForceFieldOn(Critter& player, Critter@ npc, int id)
```

### d_IsForceFieldOn

```angelscript
bool d_IsForceFieldOn(Critter& player, Critter@ npc, int id, int mapPid)
```

### d_IsForceFieldOff

```angelscript
bool d_IsForceFieldOff(Critter& player, Critter@ npc, int id)
```

### d_IsForceFieldOff

```angelscript
bool d_IsForceFieldOff(Critter& player, Critter@ npc, int id, int mapPid)
```

### d_IsForceFieldFullIntegrity

```angelscript
bool d_IsForceFieldFullIntegrity(Critter& player, Critter@ npc, int id)
```

### d_IsForceFieldFullIntegrity

```angelscript
bool d_IsForceFieldFullIntegrity(Critter& player, Critter@ npc, int id, int mapPid)
```

### d_IsForceFieldHalvedIntegrity

```angelscript
bool d_IsForceFieldHalvedIntegrity(Critter& player, Critter@ npc, int id)
```

### d_IsForceFieldHalvedIntegrity

```angelscript
bool d_IsForceFieldHalvedIntegrity(Critter& player, Critter@ npc, int id, int mapPid)
```

### r_ForceFieldToggle

```angelscript
void r_ForceFieldToggle(Critter& player, Critter@ npc, int id)
```

### r_ForceFieldToggle

```angelscript
void r_ForceFieldToggle(Critter& player, Critter@ npc, int id, int mapPid)
```

### r_ForceFieldOn

```angelscript
void r_ForceFieldOn(Critter& player, Critter@ npc, int id)
```

### r_ForceFieldOn

```angelscript
void r_ForceFieldOn(Critter& player, Critter@ npc, int id, int mapPid)
```

### r_ForceFieldOff

```angelscript
void r_ForceFieldOff(Critter& player, Critter@ npc, int id)
```

### r_ForceFieldOff

```angelscript
void r_ForceFieldOff(Critter& player, Critter@ npc, int id, int mapPid)
```

### r_ForceFieldFullIntegrity

```angelscript
void r_ForceFieldFullIntegrity(Critter& player, Critter@ npc, int id)
```

### r_ForceFieldFullIntegrity

```angelscript
void r_ForceFieldFullIntegrity(Critter& player, Critter@ npc, int id, int mapPid)
```

### r_ForceFieldHalvedIntegrity

```angelscript
void r_ForceFieldHalvedIntegrity(Critter& player, Critter@ npc, int id)
```

### r_ForceFieldHalvedIntegrity

```angelscript
void r_ForceFieldHalvedIntegrity(Critter& player, Critter@ npc, int id, int mapPid)
```

### r_ForceFieldAllToggle

```angelscript
void r_ForceFieldAllToggle(Critter& player, Critter@ npc)
```

### r_ForceFieldAllToggle

```angelscript
void r_ForceFieldAllToggle(Critter& player, Critter@ npc, int mapPid)
```

### r_ForceFieldAllOn

```angelscript
void r_ForceFieldAllOn(Critter& player, Critter@ npc)
```

### r_ForceFieldAllOn

```angelscript
void r_ForceFieldAllOn(Critter& player, Critter@ npc, int mapPid)
```

### r_ForceFieldAllOff

```angelscript
void r_ForceFieldAllOff(Critter& player, Critter@ npc)
```

### r_ForceFieldAllOff

```angelscript
void r_ForceFieldAllOff(Critter& player, Critter@ npc, int mapPid)
```

### r_ForceFieldAllFullIntegrity

```angelscript
void r_ForceFieldAllFullIntegrity(Critter& player, Critter@ npc)
```

### r_ForceFieldAllFullIntegrity

```angelscript
void r_ForceFieldAllFullIntegrity(Critter& player, Critter@ npc, int mapPid)
```

### r_ForceFieldAllHalvedIntegrity

```angelscript
void r_ForceFieldAllHalvedIntegrity(Critter& player, Critter@ npc)
```

### r_ForceFieldAllHalvedIntegrity

```angelscript
void r_ForceFieldAllHalvedIntegrity(Critter& player, Critter@ npc, int mapPid)
```

### InitForceFieldSpawner

```angelscript
void InitForceFieldSpawner(Item& spawner, bool firstTime, uint fullForceFieldPid, uint halvedForceFieldPid)
```

### e_StartUpForceField

```angelscript
uint e_StartUpForceField(array<uint>@ values)
```

### ToggleForceField

```angelscript
void ToggleForceField(Map@ map, int id)
```

### SetForceFieldOn

```angelscript
void SetForceFieldOn(Map@ map, int id)
```

### SetForceFieldOff

```angelscript
void SetForceFieldOff(Map@ map, int id)
```

### SetForceFieldFullIntegrity

```angelscript
void SetForceFieldFullIntegrity(Map@ map, int id)
```

### SetForceFieldHalvedIntegrity

```angelscript
void SetForceFieldHalvedIntegrity(Map@ map, int id)
```

### IsForceFieldOn

```angelscript
bool IsForceFieldOn(Map@ map, int id)
```

### IsForceFieldOff

```angelscript
bool IsForceFieldOff(Map@ map, int id)
```

### IsForceFieldFullIntegrity

```angelscript
bool IsForceFieldFullIntegrity(Map@ map, int id)
```

### IsForceFieldHalvedIntegrity

```angelscript
bool IsForceFieldHalvedIntegrity(Map@ map, int id)
```

### e_Flicker

```angelscript
uint e_Flicker(array<uint>@ values)
```

### e_Respawn

```angelscript
uint e_Respawn(array<uint>@ values)
```


