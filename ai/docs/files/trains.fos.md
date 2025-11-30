---
title: trains.fos
description: " FOnline: 2238 Rotators  trains.fos ..."
---

# trains.fos


FOnline: 2238
Rotators

trains.fos


## Includes

- `_macros.fos`
- `_dialogs.fos`
- `follower_common_h.fos`
- `MsgStr.h`
- `polygon_h.fos`
- `entire.fos`
- `_entires.fos`
- `_vals.fos`
- `debug_h.fos`
- `messages_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| TRAINS_CFG | `"config\\Trains.cfg"` |  |
| STR_LOCATION_NAME | `# (_pid) ((100 + (_pid)) * 1000)` |  |
| STATE_WAITING | `(0)` |  |
| STATE_RUNNING | `(1)` |  |
| WAGON_CAPACITY | `(9)` |  |

## Classes

### TrainStop

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| Destination | `uint` |  |  |
| Hour | `uint8` |  |  |

**Methods**

#### Less
```angelscript
bool Less(TrainStop& other)
```

#### Swap
```angelscript
void Swap(TrainStop& stop)
```

### CSchedule

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| Id | `uint` |  | friend class CStation; oh wait. |
| Stops | `array<[TrainStop](trains.fos.md)>` |  |  |

**Methods**

#### SortStops
```angelscript
void SortStops()
```

### CStation

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

#### WaitingCount
```angelscript
uint WaitingCount()     { return WaitingArray.length(); }
```

#### GetWaiting
```angelscript
uint GetWaiting(uint i) { return WaitingArray[i]; }
```

#### Inbound
```angelscript
void Inbound(CTrain& train)
```

#### Enter
```angelscript
void Enter(CTrain& train)
```

#### Leave
```angelscript
void Leave(CTrain& train)
```

#### OnTrainEnter
```angelscript
void OnTrainEnter()
```

#### OnTrainLeave
```angelscript
void OnTrainLeave()
```

#### AddTrainSchedule
```angelscript
void AddTrainSchedule(uint id, array<uint8>& hours, array<uint>& destinations)
```

#### MakeSchedulesStrings
```angelscript
void MakeSchedulesStrings()
```

#### GetNameTag
```angelscript
string GetNameTag()
```

### CTrack

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

### CLane

**Methods**

#### GetId
```angelscript
uint      GetId()              { return Id; }
```

#### StationsCount
```angelscript
uint      StationsCount()      { return Stations.length(); }
```

#### GetStation
```angelscript
CStation@ GetStation(uint idx) { return Mgr.GetStation(Stations[idx]); }
```

#### GetHour
```angelscript
uint8     GetHour(uint idx)    { return Hours[idx]; }
```

#### AddStop
```angelscript
void      AddStop(uint station, uint8 hour)
```

### CTrain

**Methods**

#### GetId
```angelscript
uint GetId()        { return Id; }
```

#### GetLaneIndex
```angelscript
uint GetLaneIndex() { return LaneIndex; }
```

#### GetLane
```angelscript
CLane@ GetLane()
```

#### WagonCount
```angelscript
uint WagonCount() { return Wagons.length(); }
```

#### GetWagon
```angelscript
Critter@ GetWagon(uint n)
```

#### GetState
```angelscript
uint GetState(uint wagon)
```

#### GetState
```angelscript
uint GetState()
```

#### GetName
```angelscript
string GetName() { return Name; }
```

#### GetStartStation
```angelscript
uint GetStartStation()
```

#### GetCurrentStation
```angelscript
CStation@ GetCurrentStation()
```

#### NextLaneIndex
```angelscript
uint NextLaneIndex()
```

#### GetNextStation
```angelscript
CStation@ GetNextStation()
```

#### Init
```angelscript
void Init()
```

#### GetDepartureHour
```angelscript
uint8 GetDepartureHour()
```

#### CheckDeparture
```angelscript
void CheckDeparture()
```

#### Depart
```angelscript
void Depart()
```

#### Inbound
```angelscript
void Inbound(CStation& station) { station.Inbound(this); }
```

#### Enter
```angelscript
void Enter(CStation& station)   { station.Enter(this); }
```

#### Leave
```angelscript
void Leave(CStation& station)   { station.Leave(this); }
```

#### AllArrived
```angelscript
void AllArrived()
```

#### CheckArrival
```angelscript
void CheckArrival()
```

### TrainManager

**Methods**

#### GetTrack
```angelscript
CTrack@ GetTrack(uint id)
```

#### GetLane
```angelscript
CLane@ GetLane(uint id)
```

#### GetStation
```angelscript
CStation@ GetStation(uint id)
```

#### GetTrain
```angelscript
CTrain@ GetTrain(uint id)
```

#### MakeWagon
```angelscript
Critter@ MakeWagon(Map@ map)
```

#### StartTrains
```angelscript
void StartTrains()
```

#### FindTrack
```angelscript
CTrack@ FindTrack(uint start_id, uint end_id)
```

#### MakeSchedule
```angelscript
void MakeSchedule(uint train_id, uint station_id)
```

#### GetStationByMapId
```angelscript
CStation@ GetStationByMapId(uint map_id)
```

#### Load
```angelscript
void Load(string& filename)
```


## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| Mgr | `[TrainManager](trains.fos.md)` |  |  |
| CreatingTrains | `bool` | `false` |  |

## Functions

### PassengersCount

```angelscript
uint PassengersCount(Critter& cr)               { return cr.Stat[ST_VAR0]; }
```

### ResetPassengersCount

```angelscript
void ResetPassengersCount(Critter& cr)          { cr.StatBase[ST_VAR0] = 0; }
```

### IncPassengersCount

```angelscript
void IncPassengersCount(Critter& cr, int count) { cr.StatBase[ST_VAR0] += count; }
```

### TrainState

```angelscript
int  TrainState(Critter& cr)                  { return cr.Stat[ST_VAR1]; }
```

### ChangeTrainState

```angelscript
void ChangeTrainState(Critter& cr, int state) { cr.StatBase[ST_VAR1] = state; }
```

### CurrTrack

```angelscript
int  CurrTrack(Critter& cr)             { return cr.Stat[ST_VAR2]; }
```

### SetCurrTrack

```angelscript
void SetCurrTrack(Critter& cr, int idx) { cr.StatBase[ST_VAR2] = idx; }
```

### CurrTarget

```angelscript
int  CurrTarget(Critter& cr)             { return cr.Stat[ST_VAR3]; }
```

### SetCurrTarget

```angelscript
void SetCurrTarget(Critter& cr, int idx) { cr.StatBase[ST_VAR3] = idx; }
```

### IncCurrTarget

```angelscript
void IncCurrTarget(Critter& cr)          { cr.StatBase[ST_VAR3] += 1; }
```

### TrainId

```angelscript
int  TrainId(Critter& cr)             { return cr.Stat[ST_VAR4]; }
```

### SetTrainId

```angelscript
void SetTrainId(Critter& cr, int idx) { cr.StatBase[ST_VAR4] = idx; }
```

### NextHour

```angelscript
uint NextHour() { return (__Hour + 1) % 24; }
```

### AddBlocker

```angelscript
void AddBlocker(Map@ map, uint16 hx, uint16 hy)
```

### AddTrainBlockers

```angelscript
void AddTrainBlockers(Map@ map, Item@ train)
```

### RemoveTrainBlockers

```angelscript
void RemoveTrainBlockers(Map@ map)
```

### _Conductor

```angelscript
void _Conductor(Critter& cr, bool firstTime)
```

### _StationConductor

```angelscript
void _StationConductor(Critter& cr, bool firstTime)
```

### _YellingIdle

```angelscript
void _YellingIdle(Critter& cr)
```

### _Idle

```angelscript
void _Idle(Critter& cr)
```

### _GlobalProcess

```angelscript
bool _GlobalProcess(Critter& cr, int type, Item@ car, float& x, float& y, float& toX, float& toY, float& speed, uint& encounterDescriptor, bool& waitForAnswer)
```

### UnloadPassangers

```angelscript
void UnloadPassangers(Critter& cr)
```

### e_StartTrains

```angelscript
uint e_StartTrains(array<uint>@ values)
```

### InitTrains

```angelscript
void InitTrains()
```

### GetCurrentCoords

Wagon

```angelscript
void GetCurrentCoords(Critter& cr, float& x, float& y)
```

### EndOfTrack

```angelscript
bool EndOfTrack(Critter& cr)
```

### TakeNextLine

```angelscript
bool TakeNextLine(file& f, string& line)
```

### TakeNextNumLine

```angelscript
array<int>@ TakeNextNumLine(file & f)
```

### ArrToString

```angelscript
string@ ArrToString(array<int>@ arr)
```

### d_ShowNode

dialog stuff var0-3 are used to store train ids referenced, var4 has their number

```angelscript
bool d_ShowNode(Critter& cr, Critter@ npc, int node)
```

### r_IfNoTrains

```angelscript
uint r_IfNoTrains(Critter& cr, Critter@ npc, int noTrains)
```

### r_HereIsMyTicket

```angelscript
uint r_HereIsMyTicket(Critter& cr, Critter@ npc, int notHere, int trainFull, int animalsNotAllowed, int notEnoughTickets, int trainNum)
```

### r_GetIntoTrain

```angelscript
uint r_GetIntoTrain(Critter& player, Critter@ npc, int notHere, int trainFull, int notEnoughTickets)
```

### dlg_TrainInfo

```angelscript
void dlg_TrainInfo(Critter& player, Critter@ npc, string@ text)
```

### dlg_TrainInfo2

```angelscript
void dlg_TrainInfo2(Critter& player, Critter@ npc, string@ text)
```

### dlg_TrainInfo3

```angelscript
void dlg_TrainInfo3(Critter& player, Critter@ npc, string@ text)
```

### load

```angelscript
void load(Critter&, int, int, int)
```

### init

```angelscript
void init(Critter&, int, int, int)
```


