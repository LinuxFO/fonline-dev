---
title: globalmap_group.fos
description: " FOnline: 2238 Rotators  globalmap_group.fos ..."
---

# globalmap_group.fos


FOnline: 2238
Rotators

globalmap_group.fos


## Includes

- `_macros.fos`
- `_math.fos`
- `follower_h.fos`
- `logging_h.fos`
- `MSGSTR.h`
- `npc_common_h.fos`
- `tracking.fos`
- `worldmap_h.fos`

## Constants

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| maxx | `int` | `__GlobalMapWidth * __GlobalMapZoneLength` |  |
| maxy | `int` | `__GlobalMapHeight * __GlobalMapZoneLength` |  |
| maxx | `int` | `__GlobalMapWidth * __GlobalMapZoneLength` |  |
| maxy | `int` | `__GlobalMapHeight * __GlobalMapZoneLength` |  |

## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| func | `FGlobalProcessFunc@` | `GlobalProcessFunctions[processType]` | Main processing is done here |
| curXi | `int` | `int(curX)` |  |
| curYi | `int` | `int(curY)` |  |
| oldXi | `int` | `curXi` |  |
| oldYi | `int` | `curYi` |  |
| leader | `Critter@` | `group[0]` |  |
| groupIgnore | `int` | `0` |  |
| players | `uint` | `0` |  |
| movementType | `int` | `(valid(car) ? car.Proto.Car_MovementType : WORLDMAP_WALK_GROUND)` |  |
| curXi | `int` | `int(curX)` |  |
| curYi | `int` | `int(curY)` |  |
| landFounded | `bool` | `false` | Find land |
| xx | `int` | `curXi + ox` |  |
| yy | `int` | `curYi + oy` |  |
| curZoneX | `int` | `int(curX) / __GlobalMapZoneLength` |  |
| curZoneY | `int` | `int(curY) / __GlobalMapZoneLength` |  |
| strangers | `bool` | `false` | cr.Say(SAY_NETMSG, "Group length: " + group.length()); |
| leader | `Critter@` | `group[0]` |  |
| curXi | `int` | `int(curX)` |  |
| curYi | `int` | `int(curY)` |  |
| toXi | `int` | `int(toX)` |  |
| toYi | `int` | `int(toY)` |  |
| strNum | `uint` | `0` |  |
| xx | `int` | `curXi + ox[j] * i` |  |
| yy | `int` | `curYi + oy[j] * i` |  |
| leader | `Critter@` | `group[0]` |  |
| curXi | `int` | `int(curX)` |  |
| curYi | `int` | `int(curY)` |  |

## Functions

### RejoinMaster

```angelscript
void RejoinMaster(Critter& cr, bool TeleportToMap)
```

### e_AskAboutAvailable

 Asks player that just enter global if he wants to track nearby available groups 

```angelscript
uint e_AskAboutAvailable(array<uint>@ values)
```

### global_invite

///////////////////////////////////////////////////////////////////////////////////////////////// Call on invite to encaunter. If mapId != 0 than group enter to it.

```angelscript
void global_invite(Critter& leader, Item@ car, uint encounterDescriptor, int combatMode, uint& mapId, uint16& hexX, uint16& hexY, uint8& dir)
```

### ScanZone

```angelscript
void ScanZone(array<Critter@>& group, int zx, int zy)
```

### MoveGlobalGroup

```angelscript
void MoveGlobalGroup(Critter& cr, Item@ car, float& curX, float& curY, float& toX, float& toY, float& speed)
```


