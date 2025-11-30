---
title: caravans.fos
description: " FOnline: 2238 Rotators  caravans.fos ..."
---

# caravans.fos


FOnline: 2238
Rotators

caravans.fos


## Includes

- `_macros.fos`
- `caravans_h.fos`
- `groups_h.fos`
- `worldmap_h.fos`
- `debug_h.fos`
- `npc_planes_h.fos`
- `npc_common_h.fos`
- `reputations_h.fos`
- `_maps.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __MODULE__ |  |  |
| CARAVAN_CFG | `"config\\Caravans.cfg"` |  |

## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| mgr | `[CaravanManager](caravans_h.fos.md)` |  |  |
| caravansInitialized | `bool` | `false` |  |

## Functions

### InitCaravans

* * Initializes caravans and their routes. Should be made safe to be called anytime! 

```angelscript
void InitCaravans()
```

### init

* * Initializes caravans runtime, should be safe to be called anytime. 

```angelscript
void init(Critter& cr, int p0, int p1, int p2)
```

### _CaravanTownNpc

```angelscript
void _CaravanTownNpc(Critter& cr, bool firstTime)
```

### GetCaravan

* * Gets caravan, that given critter is assigned to. 

```angelscript
ICaravan@ GetCaravan(Critter& cr)
```

### GetCaravan

* * Gets caravan with given id number. 

```angelscript
ICaravan@ GetCaravan(uint id)
```

### r_Start

```angelscript
void r_Start(Critter& player, Critter@ npc)
```

### r_ResetReputation

```angelscript
void r_ResetReputation(Critter& player, Critter@ npc)
```

### d_CheckReputationTooLow

```angelscript
bool d_CheckReputationTooLow(Critter& player, Critter@ npc, int reputationNeeded)
```

### d_CheckPlayerGearNot

```angelscript
bool d_CheckPlayerGearNot(Critter& player, Critter@ npc)
```

### d_CheckPlayerGear

```angelscript
bool d_CheckPlayerGear(Critter& player, Critter@ npc)
```

### _CaravanGuard

```angelscript
void _CaravanGuard(Critter& cr, bool firstTime)
```

### _GuardAttacked

```angelscript
bool _GuardAttacked(Critter& cr, Critter& attacker)
```

### _GuardSmthAttacked

```angelscript
void _GuardSmthAttacked(Critter& cr, Critter& fromCr, Critter& attacker)
```

### _GuardSmthDied

```angelscript
void _GuardSmthDied(Critter& cr, Critter& killed, Critter@ killer)
```

### _DriverAttacked

```angelscript
bool _DriverAttacked(Critter& leader, Critter& attacker)
```

### _DriverSmthAttacked

```angelscript
void _DriverSmthAttacked(Critter& leader, Critter& fromCr, Critter& attacker)
```

### _DriverSmthDied

```angelscript
void _DriverSmthDied(Critter& leader, Critter& killed, Critter@ killer)
```

### _OnIdleEncounter

```angelscript
void _OnIdleEncounter(Critter& cr)
```

### e_CheckWeapon

```angelscript
uint e_CheckWeapon(array<uint>@ values)
```

### _OnSmthMoveItemEncounter

```angelscript
void _OnSmthMoveItemEncounter(Critter& crit, Critter& fromCrit, Item& item, uint8 fromSlot)
```

### _CaravanDriver

```angelscript
void _CaravanDriver(Critter& cr, bool firstTime)
```

### _DriverPlaneStart

```angelscript
int _DriverPlaneStart(Critter& npc, NpcPlane& plane, int reason, Critter@ someCr, Item@ someItem)
```

### _DriverDead

```angelscript
void _DriverDead(Critter& cr, Critter@ killer)
```

### e_Clean

```angelscript
uint e_Clean(array<uint>@ values)
```

### e_RespawnCaravan

```angelscript
uint e_RespawnCaravan(array<uint>@ values)
```

### _DriverIdle

```angelscript
void _DriverIdle(Critter& cr)
```

### e_Leave

```angelscript
uint e_Leave(array<uint>@ values)
```

### _DriverMapEnter

```angelscript
bool _DriverMapEnter(Critter& driver, Map& map)
```

### e_LateEnterFunc

```angelscript
uint e_LateEnterFunc(array<uint>@ values)
```

### e_PrepareCaravan

```angelscript
uint e_PrepareCaravan(array<uint>@ values)
```

### e_DepartCaravan

```angelscript
uint e_DepartCaravan(array<uint>@ values)
```

### d_IsPreparing

```angelscript
bool d_IsPreparing(Critter& player, Critter@ npc)
```

### d_IsNotPreparing

```angelscript
bool d_IsNotPreparing(Critter& player, Critter@ npc)
```

### d_IsFull

```angelscript
bool d_IsFull(Critter& player, Critter@ npc)
```

### r_JoinCaravan

```angelscript
void r_JoinCaravan(Critter& player, Critter@ npc)
```

### r_KillCaravanDriver

```angelscript
void r_KillCaravanDriver(Critter& player, Critter@ npc, int carNr)
```

### dlg_CaravanName

```angelscript
void dlg_CaravanName(Critter& player, Critter@ npc, string@ text)
```

### dlg_CaravanTime

```angelscript
void dlg_CaravanTime(Critter& player, Critter@ npc, string@ text)
```

### dlg_CaravanLocation1

```angelscript
void dlg_CaravanLocation1(Critter& player, Critter@ npc, string@ text)
```

### dlg_CaravanLocation2

```angelscript
void dlg_CaravanLocation2(Critter& player, Critter@ npc, string@ text)
```

### dlg_CaravanLocation3

```angelscript
void dlg_CaravanLocation3(Critter& player, Critter@ npc, string@ text)
```

### dlg_CaravanLocation4

```angelscript
void dlg_CaravanLocation4(Critter& player, Critter@ npc, string@ text)
```

### dlg_CaravanLocation5

```angelscript
void dlg_CaravanLocation5(Critter& player, Critter@ npc, string@ text)
```

### dlg_CaravanLocation6

```angelscript
void dlg_CaravanLocation6(Critter& player, Critter@ npc, string@ text)
```

### dlg_CaravanLocation7

```angelscript
void dlg_CaravanLocation7(Critter& player, Critter@ npc, string@ text)
```

### checkCaravanPosition

```angelscript
string checkCaravanPosition(uint carNr)
```

### dlg_CaravanPayment

```angelscript
void dlg_CaravanPayment(Critter& player, Critter@ npc, string@ text)
```

### _LeaderMapEnter

```angelscript
bool _LeaderMapEnter(Critter& leader, Map& map)
```

### _GlobalProcessDriver

```angelscript
bool        _GlobalProcessDriver(Critter& cr, int type, Item@ car, float& x, float& y, float& toX, float& toY, float& speed, uint& encounterDescriptor, bool& waitForAnswer)
```


