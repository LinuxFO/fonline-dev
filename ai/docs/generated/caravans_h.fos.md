---
title: caravans_h.fos
description: " FOnline: 2238 Rotators  caravans_h.fos ..."
---

# caravans_h.fos


FOnline: 2238
Rotators

caravans_h.fos


## Includes

- `_macros.fos`
- `_math.fos`
- `_dialogs.fos`
- `utils_h.fos`
- `serializator.fos`
- `groups_h.fos`
- `debug_h.fos`
- `economy_h.fos`
- `npc_common_h.fos`

## Included By

- [caravans.fos](caravans.fos.md)

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| CARAVAN_ENTIRE | `(125)` |  |
| CARAVAN_TRADER | `(67)` | Caravan trader |
| CARAVAN_LEVEL | `(10)` |  |
| CARAVAN_BAG | `(1)` |  |
| WAGON1 | `(2527)` |  |
| STATE_WAITING | `(0)` |  |
| STATE_PREPARE | `(1)` |  |
| STATE_RUNNING | `(2)` |  |
| _ID | `# (item)     (item.Val1)` | item's (caravan spawnpoint) field that denotes id of assigned caravan |

## Classes

### CCaravanNpc

* * Descriptor for caravan npc. 

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| Pid | `uint16` |  |  |
| DialogId | `uint` |  |  |
| BagId | `uint` |  |  |
| Level | `uint` |  |  |

### Coord

* * Route coordinate 

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| X | `uint16` |  |  |
| Y | `uint16` |  |  |

### CRoute

**Methods**

#### GetId
```angelscript
uint GetId()     { return Id; }
```

#### GetHeadId
```angelscript
uint GetHeadId() { return HeadId; }
```

#### GetTailId
```angelscript
uint GetTailId() { return TailId; }
```

#### NodesCount
```angelscript
uint  NodesCount()                         { return X.length(); }
```

#### GetX
```angelscript
float GetX(uint node)                      { return X[node]; }
```

#### GetY
```angelscript
float GetY(uint node)                      { return Y[node]; }
```

#### GetXY
```angelscript
void  GetXY(uint node, float& x, float& y) { x = X[node]; y = Y[node]; }
```

#### AddNode
```angelscript
void  AddNode(float x, float y)            { X.insertLast(x); Y.insertLast(y); }
```

#### IsLast
```angelscript
bool  IsLast(uint idx)                     { return idx + 1 == NodesCount(); }
```

### CCaravanStation

**Methods**

#### GetId
```angelscript
uint      GetId()       { return Id; }
```

#### GetX
```angelscript
float     GetX()        { return LocPtr.WorldX; }
```

#### GetY
```angelscript
float     GetY()        { return LocPtr.WorldY; }
```

#### GetMap
```angelscript
Map@      GetMap()      { return MapPtr; }
```

#### GetLocation
```angelscript
Location@ GetLocation() { return LocPtr; }
```

### CaravanManager

**Methods**

#### GetStation
```angelscript
CCaravanStation@ GetStation(uint id)
```

#### GetCaravan
```angelscript
ICaravan@ GetCaravan(uint id)
```

#### GetRoute
```angelscript
CRoute@ GetRoute(uint id)
```

#### Load
```angelscript
void Load(string& filename)
```

### CCaravan

* * Holds the caravan info 

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| id | `uint` |  | index of the caravan |
| mgr | `[CaravanManager](caravans_h.fos.md)@` |  |  |
| players | `array<uint>` |  | * Ids of the players that joined caravan |
| critters | `array<uint>` |  | * Ids of the npcs that run caravan (leader first). |
| npcs | `array<[CCaravanNpc](caravans_h.fos.md)>` |  | npcs descriptors |
| wagon | `uint` |  | caravan wagon (item pid) |
| routeIndex | `uint` |  |  |
| routePosition | `uint` |  |  |
| originStationId | `uint` |  |  |
| destinationStationId | `uint` |  |  |
| destLoc | `uint16` |  | * Caravan destination's location pid. |
| destMap | `uint8` |  | * Map in destination location (index to the location maps list) |
| origLoc | `uint16` |  | * Origin location |
| origMap | `uint8` |  |  |
| currLoc | `uint` |  | * Current location. Either origin or destination, or 0 (worldmap). |
| currMap | `uint8` |  |  |
| entire | `uint` |  |  |
| timeInTown | `uint` |  |  |
| timeEvent | `uint` |  |  |
| departure | `uint` |  |  |
| state | `uint` |  |  |
| target | `int` |  | * Actual target (index to the routes table). |
| route | `array<[Coord](caravans_h.fos.md)>` |  |  |
| routes | `array<int>@` |  |  |
| rewards | `array<int>@` |  |  |
| name | `string` |  |  |
| townDlg | `uint` |  |  |
| wmDlg | `uint` |  |  |
| townLeaderPid | `uint` |  |  |
| townLeaderBag | `uint` |  |  |
| leaderPid | `uint` |  |  |
| leaderBag | `uint` |  |  |
| factionId | `uint` |  |  |
| guardPids | `array<uint>@` |  |  |
| guardBags | `array<uint>@` |  |  |
| serializer | `[Serializator](serializator.fos.md)` |  |  |

**Methods**

#### SetBagsAndPids
```angelscript
void SetBagsAndPids(uint townLeaderPid, uint townLeaderBag, uint leaderPid, uint leaderBag, array<uint>@ guardPids, array<uint>@ guardBags)
```

#### LoadData
 Loads caravan data from anydata array 

```angelscript
void LoadData()
```

#### SetDefault
```angelscript
void SetDefault()
```

#### SaveData
 Stores caravan data 

```angelscript
void SaveData()
```

#### SetId
* * Sets the caravan id. 

```angelscript
void SetId(uint id)
```

#### Init
* * Initializes caravan. * 

```angelscript
void Init()
```

#### ClearCaravan
```angelscript
void ClearCaravan()
```

#### SpawnCaravan
* * Spawns caravan on current map, at the point marked by spawnpoint item. 

```angelscript
void SpawnCaravan()
```

#### PrepareDeparture
```angelscript
void PrepareDeparture(uint departTime)
```

#### GetCurrentCoords
```angelscript
void GetCurrentCoords(float& x, float& y)
```

#### EndOfTrack
```angelscript
bool EndOfTrack()
```

#### IncRoutePosition
```angelscript
void IncRoutePosition()
```

#### GetLeaderId
* * Caravan leader's id 

```angelscript
uint GetLeaderId()
```

#### GetWMLeaderId
```angelscript
uint GetWMLeaderId()
```

#### IsCaravanMember
```angelscript
bool IsCaravanMember(Critter& crit)
```

#### Route
* * Sets origin/destination. 

```angelscript
ICaravan@ Route(uint16 origLoc, uint8 origMap, uint16 destLoc, uint8 destMap)
```

#### Route
* * Adds coordinate to the caravan route. * First and last are not needed, as they're taken from origin/destination locations. 

```angelscript
ICaravan@ Route(uint16 x, uint16 y)
```

#### _AddNpc
* * Adds npc to caravan. * * @remarks Leader is first. 

```angelscript
ICaravan@ _AddNpc(uint16 pid, uint dialogId, uint bagId, uint level)
```

#### Assign
* * Assigns critter to caravan. 

```angelscript
void Assign(Critter& cr)
```

#### Leave
* * Remove critter from caravan. 

```angelscript
void Leave(Critter& cr)
```

#### GetState
```angelscript
uint GetState()
```

#### GetName
```angelscript
string GetName()
```

#### GetNextDestinationName
```angelscript
string GetNextDestinationName()
```

#### GetActPay
```angelscript
uint GetActPay()
```

#### GetDepartTime
```angelscript
uint GetDepartTime()
```

#### Start
* * Starts the caravan route to the next target (destination, or way back to origin). 

```angelscript
void Start()
```

#### Reward
```angelscript
void Reward()
```

#### Arrive
```angelscript
void Arrive()
```

#### PrepareRespawn
```angelscript
void PrepareRespawn()
```

#### Respawn
```angelscript
void Respawn()
```


## Functions

### IsCaravanLeader

* * Checks if given critter is leader of some caravan. 

```angelscript
bool IsCaravanLeader(Critter& cr)
```

### CaravanStart

* * Starts the caravan (sends it to the worldmap). * * @param leader        Npc that's the leader of the caravan. 

```angelscript
void CaravanStart(Critter& leader)
```

### CaravanProcessStartFast

```angelscript
void CaravanProcessStartFast()
```

### CaravanProcessMove

```angelscript
void CaravanProcessMove()
```


