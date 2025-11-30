---
title: elevators.fos
description: " FOnline: 2238 Rotators  elevators.fos ..."
---

# elevators.fos


FOnline: 2238
Rotators

elevators.fos


## Includes

- `elevators_h.fos`
- `MsgStr.h`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __ELEVATORS_MODULE__ |  |  |

## Functions

### GetElevator

 Retrieves elevator player is in 

```angelscript
IElevator@ GetElevator(Critter& player)
```

### AddElevator

```angelscript
void AddElevator(IElevator@ elevator)
```

### HandleElevator

 Helper function for elevator triggers 

```angelscript
void HandleElevator(IElevator@ elevator, Critter& critter, bool entered)
```

### answer_Elevator

 Elevator window handler (for ShowScreen, deprecated) 

```angelscript
void answer_Elevator(Critter& player, uint floor, string& answerS)
```

### unsafe_Transit

handler for RunServerScriptUnsafe

```angelscript
void unsafe_Transit(Critter& player, int floor, int p1, int p2, string@ param3, array<int>@ param4)
```

### unsafe_PlayStartSound

plays elevator start sound in the map where it was used

```angelscript
void unsafe_PlayStartSound(Critter& player, int p0, int p1, int p2, string@ param3, array<int>@ param4)
```

### unsafe_PlayArrivingSound

plays elevator sound on level it actually passess by

```angelscript
void unsafe_PlayArrivingSound(Critter& player, int floor, int p1, int p2, string@ param3, array<int>@ param4)
```

### debug_elevators

debug info

```angelscript
void debug_elevators(Critter& player, int p0, int p1, int p2)
```


