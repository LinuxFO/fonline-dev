---
title: talchem.fos
description: " FOnline: 2238 Rotators  talchem.fos ..."
---

# talchem.fos


FOnline: 2238
Rotators

talchem.fos


## Includes

- `_macros.fos`
- `MsgStr.h`
- `_npc_pids.fos`
- `_animation.fos`

## Constants

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| doorCloseInterval | `uint32` | `5` |  |
| chanceToJam | `uint32` | `20` |  |
| criticalFailChance | `uint32` | `5` |  |
| repairCheckBottom | `uint32` | `80` |  |
| repairCheckTop | `uint32` | `150` |  |
| doorCloseInterval2 | `uint32` | `5` |  |
| chanceToJam2 | `uint32` | `25` |  |
| hackVarId | `uint32` | `9210` |  |
| dialogId | `uint32` | `22120` |  |
| doorCloseInterval3 | `uint32` | `5` |  |
| chanceToJam3 | `uint32` | `20` |  |
| criticalFailChance3 | `uint32` | `5` |  |
| lockpickCheckBottom | `uint32` | `100` |  |
| lockpickCheckTop | `uint32` | `150` |  |
| doorCloseInterval4 | `uint32` | `5` |  |
| chanceToJam4 | `uint32` | `25` |  |
| hackVarId1 | `uint32` | `9211` |  |
| dialogId1 | `uint32` | `22121` |  |

## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| innerGateEntire | `uint` | `10` |  |
| outerLeftGateEntire | `uint` | `11` |  |
| outerRightGateEntire | `uint` | `12` |  |
| jammedMessage | `string` | `"The door is jammed... electronically."` |  |
| doorOkMessage | `string` | `"The door is working fine... for now."` |  |
| repairFailMessage | `string` | `"You didn't manage to repair the door."` |  |
| repairCritFailMessage | `string` | `"You almost had it."` |  |
| repairSuccessMessage | `string` | `"You successfully repair the door."` |  |
| jammedMessage3 | `string` | `"The door is locked."` |  |
| doorOkMessage3 | `string` | `"The door isn't locked."` |  |
| lockpickFailMessage | `string` | `"You didn't manage to unlock the door."` |  |
| lockpickCritFailMessage | `string` | `"You almost had it."` |  |
| lockpickSuccessMessage | `string` | `"You successfully unlock the door."` |  |

## Functions

### s_TerminalDial

```angelscript
bool s_TerminalDial(Critter& player, Scenery& terminal, int skill, Item@ item, int dialNum)
```

### s_InnerTerminalA

pripichnout k Acku

```angelscript
bool s_InnerTerminalA(Critter& player, Scenery& terminal, int skill, Item@ item)
```

### s_MiddleTerminalB

pripichnout k Bcku

```angelscript
bool s_MiddleTerminalB(Critter& player, Scenery& terminal, int skill, Item@ item)
```

### s_OuterTerminalC

pripichnout k Ccku

```angelscript
bool s_OuterTerminalC(Critter& player, Scenery& terminal, int skill, Item@ item)
```

### s_TerminalAirlock

```angelscript
bool s_TerminalAirlock(Critter& player, Scenery& terminal, int skill, Item@ item, int whichTerm)
```

### _AutoDoorInit

```angelscript
void _AutoDoorInit(Item& door, bool firstTime)
```

### _AutoDoorOpen

```angelscript
bool _AutoDoorOpen(Item& item, Critter& crit, int skill)
```

### e_AutoCloseDoor

```angelscript
uint e_AutoCloseDoor(array<uint>@ vals)
```

### tryJamDoor

```angelscript
void tryJamDoor(Item@ door)
```

### _HackDoorInit

```angelscript
void _HackDoorInit(Item& door, bool firstTime)
```

### _HackDoorOpen

```angelscript
bool _HackDoorOpen(Item& item, Critter& crit, int skill)
```

### e_HackCloseDoor

```angelscript
uint e_HackCloseDoor(array<uint>@ vals)
```

### tryJamHackDoor

```angelscript
void tryJamHackDoor()
```

### s_HackDoorOpen

```angelscript
bool s_HackDoorOpen(Critter& player, Scenery& terminal, int skill, Item@ item)
```

### r_HackDoorOpen

```angelscript
void r_HackDoorOpen(Critter& player, Critter@ victim, int entireNum)
```

### _AutoDoorInit3

```angelscript
void _AutoDoorInit3(Item& door, bool firstTime)
```

### _AutoDoorOpen3

```angelscript
bool _AutoDoorOpen3(Item& item, Critter& crit, int skill)
```

### e_AutoCloseDoor3

```angelscript
uint e_AutoCloseDoor3(array<uint>@ vals)
```

### tryJamDoor3

```angelscript
void tryJamDoor3(Item@ door)
```

### _HackDoorInit1

```angelscript
void _HackDoorInit1(Item& door, bool firstTime)
```

### _HackDoorOpen1

```angelscript
bool _HackDoorOpen1(Item& item, Critter& crit, int skill)
```

### e_HackCloseDoor1

```angelscript
uint e_HackCloseDoor1(array<uint>@ vals)
```

### tryJamHackDoor1

```angelscript
void tryJamHackDoor1()
```

### s_HackDoorOpen1

```angelscript
bool s_HackDoorOpen1(Critter& player, Scenery& terminal, int skill, Item@ item)
```

### r_HackDoorOpen1

```angelscript
void r_HackDoorOpen1(Critter& player, Critter@ victim, int entireNum)
```


