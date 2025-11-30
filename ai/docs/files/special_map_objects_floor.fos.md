---
title: special_map_objects_floor.fos
description: " FOnline: 2238 Rotators  special_map_objects_floor.fos ..."
---

# special_map_objects_floor.fos


FOnline: 2238
Rotators

special_map_objects_floor.fos


## Included By

- [special_map_objects.fos](special_map_objects.fos.md)

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| FLOOR_ON | `(0x01)` |  |
| ELECTRO_CONTROLLER_PID | `(10012)` |  |
| MINEFIELD_CONTROLLER_PID | `(10013)` |  |
| ELECTRO_FLOOR_PLATE_PID | `(10010)` |  |
| MINEFIELD_FLOOR_PLATE_PID | `(10011)` |  |
| FLOOR_TYPE_ELECTRO | `(0)` |  |
| FLOOR_TYPE_MINEFIELD | `(1)` |  |

## Classes

### CFloorSearcher

**Methods**

#### FindTogglableSMOs
```angelscript
uint FindTogglableSMOs(array<ITogglableSMO@>& list, Map& map, int globalId)
```

#### FindFloorObjects
```angelscript
uint FindFloorObjects(array<MapFloorObject@>& list, Map& map, int type)
```

#### FindSingleFloor
```angelscript
MapFloorObject@ FindSingleFloor(Map& map, int id, int type)
```

### MapFloorObject

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| controller | `Item@` |  |  |
| floorInitialized | `bool` |  |  |
| map | `Map@` |  |  |

**Methods**

#### LazyInitFloor
```angelscript
void LazyInitFloor(uint platePid)
```

#### ForceOn
```angelscript
void ForceOn() {}
```

#### IsOn
```angelscript
bool IsOn()    { return false; }
```

#### TurnOn
```angelscript
void TurnOn()  {}
```

#### IsOff
```angelscript
bool IsOff()   { return false; }
```

#### TurnOff
```angelscript
void TurnOff() {}
```

#### Toggle
```angelscript
void Toggle()
```

### MapMineFieldFloorObject

**Methods**

#### TurnOn
```angelscript
void TurnOn()
```

#### ForceOn
```angelscript
void ForceOn()
```

#### GetComplexity
```angelscript
uint GetComplexity()
```

#### SetComplexity
```angelscript
void SetComplexity(uint complexity)
```

#### GetHideSkill
```angelscript
uint GetHideSkill()
```

#### SetHideSkill
```angelscript
void SetHideSkill(uint hideSkill)
```

#### GetBonusDamage
```angelscript
uint GetBonusDamage()
```

#### SetBonusDamage
```angelscript
void SetBonusDamage(uint damage)
```

#### GetBonusRadius
```angelscript
uint GetBonusRadius()
```

#### SetBonusRadius
```angelscript
void SetBonusRadius(uint radius)
```

#### TurnOff
```angelscript
void TurnOff()
```

#### IsOn
```angelscript
bool IsOn()
```

#### IsOff
```angelscript
bool IsOff()
```

### MapElectroFloorObject

**Methods**

#### Zap
```angelscript
void Zap()
```

#### TurnOn
```angelscript
void TurnOn()
```

#### ForceOn
```angelscript
void ForceOn()
```

#### SetDamage
```angelscript
void SetDamage(uint damage)
```

#### GetDamage
```angelscript
uint GetDamage()
```

#### SetShockInterval
```angelscript
void SetShockInterval(uint interval)
```

#### GetShockInterval
```angelscript
uint GetShockInterval()
```

#### TurnOff
```angelscript
void TurnOff()
```

#### IsOn
```angelscript
bool IsOn()
```

#### IsOff
```angelscript
bool IsOff()
```


## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| FloorSearcher | `[CFloorSearcher](special_map_objects_floor.fos.md)@` | `CFloorSearcher()` |  |

## Functions

### d_IsElectroFloorOn

```angelscript
bool d_IsElectroFloorOn(Critter& player, Critter@ npc, int controllerId)
```

### d_IsElectroFloor2On

```angelscript
bool d_IsElectroFloor2On(Critter& player, Critter@ npc, int controllerId, int mapPid)
```

### d_IsElectroFloorOff

```angelscript
bool d_IsElectroFloorOff(Critter& player, Critter@ npc, int controllerId)
```

### d_IsElectroFloorOff

```angelscript
bool d_IsElectroFloorOff(Critter& player, Critter@ npc, int controllerId, int mapPid)
```

### r_ElectroFloorToggle

```angelscript
void r_ElectroFloorToggle(Critter& player, Critter@ npc, int controllerId)
```

### r_ElectroFloorToggle

```angelscript
void r_ElectroFloorToggle(Critter& player, Critter@ npc, int controllerId, int mapPid)
```

### r_ElectroFloorOn

```angelscript
void r_ElectroFloorOn(Critter& player, Critter@ npc, int controllerId)
```

### r_ElectroFloorOn

```angelscript
void r_ElectroFloorOn(Critter& player, Critter@ npc, int controllerId, int mapPid)
```

### r_ElectroFloorOff

```angelscript
void r_ElectroFloorOff(Critter& player, Critter@ npc, int controllerId)
```

### r_ElectroFloorOff

```angelscript
void r_ElectroFloorOff(Critter& player, Critter@ npc, int controllerId, int mapPid)
```

### r_ElectroFloorAllToggle

```angelscript
void r_ElectroFloorAllToggle(Critter& player, Critter@ npc)
```

### r_ElectroFloorAllToggle

```angelscript
void r_ElectroFloorAllToggle(Critter& player, Critter@ npc, int mapPid)
```

### r_ElectroFloorAllOn

```angelscript
void r_ElectroFloorAllOn(Critter& player, Critter@ npc)
```

### r_ElectroFloorAllOn

```angelscript
void r_ElectroFloorAllOn(Critter& player, Critter@ npc, int mapPid)
```

### r_ElectroFloorAllOff

```angelscript
void r_ElectroFloorAllOff(Critter& player, Critter@ npc)
```

### r_ElectroFloorAllOff

```angelscript
void r_ElectroFloorAllOff(Critter& player, Critter@ npc, int mapPid)
```

### d_IsMineFieldFloorOn

```angelscript
bool d_IsMineFieldFloorOn(Critter& player, Critter@ npc, int controllerId)
```

### d_IsMineFieldFloor2On

```angelscript
bool d_IsMineFieldFloor2On(Critter& player, Critter@ npc, int controllerId, int mapPid)
```

### d_IsMineFieldFloorOff

```angelscript
bool d_IsMineFieldFloorOff(Critter& player, Critter@ npc, int controllerId)
```

### d_IsMineFieldFloorOff

```angelscript
bool d_IsMineFieldFloorOff(Critter& player, Critter@ npc, int controllerId, int mapPid)
```

### r_MineFieldFloorToggle

```angelscript
void r_MineFieldFloorToggle(Critter& player, Critter@ npc, int controllerId)
```

### r_MineFieldFloorToggle

```angelscript
void r_MineFieldFloorToggle(Critter& player, Critter@ npc, int controllerId, int mapPid)
```

### r_MineFieldFloorOn

```angelscript
void r_MineFieldFloorOn(Critter& player, Critter@ npc, int controllerId)
```

### r_MineFieldFloorOn

```angelscript
void r_MineFieldFloorOn(Critter& player, Critter@ npc, int controllerId, int mapPid)
```

### r_MineFieldFloorOff

```angelscript
void r_MineFieldFloorOff(Critter& player, Critter@ npc, int controllerId)
```

### r_MineFieldFloorOff

```angelscript
void r_MineFieldFloorOff(Critter& player, Critter@ npc, int controllerId, int mapPid)
```

### r_MineFieldFloorAllToggle

```angelscript
void r_MineFieldFloorAllToggle(Critter& player, Critter@ npc)
```

### r_MineFieldFloorAllToggle

```angelscript
void r_MineFieldFloorAllToggle(Critter& player, Critter@ npc, int mapPid)
```

### r_MineFieldFloorAllOn

```angelscript
void r_MineFieldFloorAllOn(Critter& player, Critter@ npc)
```

### r_MineFieldFloorAllOn

```angelscript
void r_MineFieldFloorAllOn(Critter& player, Critter@ npc, int mapPid)
```

### r_MineFieldFloorAllOff

```angelscript
void r_MineFieldFloorAllOff(Critter& player, Critter@ npc)
```

### r_MineFieldFloorAllOff

```angelscript
void r_MineFieldFloorAllOff(Critter& player, Critter@ npc, int mapPid)
```

### SetFloorOn

```angelscript
void SetFloorOn(Map@ map, int controllerId, uint floorType)
```

### SetFloorOff

```angelscript
void SetFloorOff(Map@ map, int controllerId, uint floorType)
```

### ToggleFloor

```angelscript
void ToggleFloor(Map@ map, int controllerId, uint floorType)
```

### IsFloorOn

```angelscript
bool IsFloorOn(Map@ map, int floorControllerId, uint floorType)
```

### IsFloorOff

```angelscript
bool IsFloorOff(Map@ map, int floorControllerId, uint floorType)
```

### _InitElectroFloorController

```angelscript
void _InitElectroFloorController(Item& controller, bool firstTime)
```

### _InitMineFieldFloorController

```angelscript
void _InitMineFieldFloorController(Item& controller, bool firstTime)
```

### e_StartFloor

```angelscript
uint e_StartFloor(array<uint>@ values)
```

### e_StartMineFieldFloor

```angelscript
uint e_StartMineFieldFloor(array<uint>@ values)
```

### e_ShockFloor

```angelscript
uint e_ShockFloor(array<uint>@ values)
```


