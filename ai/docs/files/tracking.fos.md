---
title: tracking.fos
description: " FOnline: 2238 Rotators  tracking.fos ..."
---

# tracking.fos


FOnline: 2238
Rotators

tracking.fos


## Includes

- `_macros.fos`
- `utils_h.fos`
- `worldmap_h.fos`

## Included By

- [globalmap_group.fos](globalmap_group.fos.md)

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| MAX_AVAILABLE_DIST | `(24)` | if group is in that range, it is available to be tracked |
| MAX_AVAILABLE_LEN | `(10)` | maximum length of array of available players |
| MAX_AVAILABLE_TIME | `(REAL_MINUTE(1))` | maximum time player is available to be tracked (ingame minutes) |

## Classes

### CTrackedGroup

 Stores info about tracked group 

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| LeaderId | `uint` |  |  |
| TrackerId | `uint` |  |  |
| X | `float` |  |  |
| Y | `float` |  |  |
| Trackers | `uint` |  | some sort of 'reference counter' |


## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| TrackedList | `array<[CTrackedGroup](tracking.fos.md)>` |  | list of groups that are tracked |
| Trackers | `array<uint>` |  | list of groups leaders that are waiting to track someone |

## Functions

### Roll

TODO: penalty for tracked group size?

```angelscript
void Roll(array<Critter@>@ group, Critter@ tracked, int& out trackerRoll, int& out trackedRoll)
```

### SetTrackingCoords

 It's called in WORLDMAP_PROCESS_MOVE and GLOBAL_PROCESS_STOP - it updates coords of tracking/tracked groups 

```angelscript
void SetTrackingCoords(array<Critter@>@ group, float x, float y, float& toX, float& toY)
```

### SetTrackingCoords

another overload to be used in global_invite

```angelscript
void SetTrackingCoords(array<Critter@>@ group, float x, float y)
```

### TrackLocation

 When tracked player enters location, it can be discovered by tracker so update their coords (it is invoked in global map in handler) 

```angelscript
void TrackLocation(Critter& player)
```

### TrackLocation

 If group stopped, and the tracked player is in location beneath mark it as known location 

```angelscript
bool TrackLocation(array<Critter@>@ group, float x, float y)
```

### repro

```angelscript
void repro(Critter& cr, int p0, int p1, int p2)
```

### track

```angelscript
void track(Critter& cr, int p0, int p1, int p2)
```

### answer_Enter

```angelscript
void answer_Enter(Critter& tracker, uint i, string& s)
```

### AskAboutAvailable

```angelscript
void AskAboutAvailable(Critter@ askedLeader)
```

### answer_ChooseTracked

 Callback that will set the tracked group 

```angelscript
void answer_ChooseTracked(Critter& player, uint answerI, string& answerS)
```

### Track

 Track the given leader - it creates new TrackedGroup object / increases the 'refcount' 

```angelscript
void Track(Critter@ tracker, Critter@ tracked)
```

### LooseTrack

 Tracker loose track  if canceled is true, it means player canceled it otherwise player lost track due to other circumstances

```angelscript
void LooseTrack(Critter@ tracker, bool canceled)
```


