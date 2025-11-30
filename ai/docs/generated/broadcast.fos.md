---
title: broadcast.fos
description: " FOnline: 2238 Rotators  broadcast.fos ..."
---

# broadcast.fos


FOnline: 2238
Rotators

broadcast.fos


## Includes

- `_macros.fos`
- `logging_h.fos`
- `utils_h.fos`
- `broadcast_h.fos`
- `gmtools_h.fos`
- `_time.fos`
- `_maps.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __BROADCAST__ |  |  |
| BROADCAST_SCRIPT | `"client_broadcast@_Receive"` |  |
| BROADCAST_SCRIPTDUMP | `"client_broadcast@_ReceiveDump"` |  |

## Classes

### CBroadcastBuffer

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| type | `int` |  | for RunClientScript |
| time | `int` |  |  |
| setup | `int` |  |  |
| message | `string` |  |  |
| data | `array<int>` |  |  |
| started | `int` |  | internal |
| lifetime | `int` |  |  |
| filters | `int` |  |  |
| filter_level | `int` |  |  |
| filter_location | `int` |  |  |
| filter_map | `int` |  |  |
| filter_faction | `int` |  |  |
| gm | `int` |  |  |
| toDelete | `bool` |  |  |

**Methods**

#### GetString
```angelscript
string GetString()
```

#### SetType
```angelscript
void SetType(int type)
```

#### GetType
```angelscript
int GetType()
```

#### SetTime
```angelscript
void SetTime(int time)
```

#### GetTime
```angelscript
int GetTime()
```

#### SetSetup
```angelscript
void SetSetup(int setup)
```

#### GetSetup
```angelscript
int GetSetup()
```

#### SetMessage
```angelscript
void SetMessage(string message)
```

#### AppendMessage
```angelscript
void AppendMessage(string message)
```

#### GetMessage
```angelscript
string GetMessage()
```

#### SetData
```angelscript
void SetData(array<int> data)
```

#### SetStart
```angelscript
void SetStart(int time)
```

#### ResetStart
```angelscript
void ResetStart()
```

#### SetLifetime
```angelscript
void SetLifetime(int lifetime)
```

#### SetFilters
```angelscript
void SetFilters(int filters)
```

#### SetFilter
```angelscript
void SetFilter(int filter)
```

#### SetFilter
```angelscript
void SetFilter(int filter, int data)
```

#### UnsetFilter
```angelscript
void UnsetFilter(int filter)
```

#### Filter
```angelscript
bool Filter(int filter)
```

#### CheckFilters
```angelscript
bool CheckFilters(Critter@ player)
```

#### Send
```angelscript
bool Send(Critter@ player)
```

#### SendToAll
```angelscript
uint SendToAll()
```

#### SetGM
```angelscript
void SetGM(int id)
```

#### UnsetGM
```angelscript
void UnsetGM()
```

#### ToDelete
```angelscript
void ToDelete()
```


## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| BroadcastBuffer | `array<[CBroadcastBuffer](broadcast.fos.md)>` |  |  |
| LockState | `bool` | `true` | locations that shouldn't be faked via ~runscript/GMT, mostly TC cities |
| influence | `IBroadcastBuffer@` | `Broadcast_Influence(location, time, "Influence " + __FullSecond)` |  |

## Functions

### AddBroadcastBuffer

```angelscript
IBroadcastBuffer@ AddBroadcastBuffer(int t, int i, int s, string& m, array<int>& d, int l, int f)
```

### DumpBroadcastBuffer

```angelscript
void DumpBroadcastBuffer(Critter@ player)
```

### dump

```angelscript
void dump(Critter& player, int, int, int)
```

### FindBroadcastBufferByType

```angelscript
uint FindBroadcastBufferByType(int type, array<IBroadcastBuffer@>& buf)
```

### FindBroadcastBufferByGM

```angelscript
uint FindBroadcastBufferByGM(int id, array<IBroadcastBuffer@>& buf)
```

### UpdateBroadcast

```angelscript
void UpdateBroadcast()
```

### IsLocked

```angelscript
bool IsLocked(uint location_pid)
```

### tclock

```angelscript
void tclock(Critter& player, int one, int two, int lock)
```

### Broadcast_Message

```angelscript
IBroadcastBuffer@ Broadcast_Message(string& message, int time, int filters, bool send)
```

### Broadcast_Message

```angelscript
IBroadcastBuffer@ Broadcast_Message(string& message, int time, int filters)
```

### Broadcast_Message

```angelscript
IBroadcastBuffer@ Broadcast_Message(string& message, int& time)
```

### Broadcast_Message

```angelscript
IBroadcastBuffer@ Broadcast_Message(string& message, bool send)
```

### Broadcast_Message

```angelscript
IBroadcastBuffer@ Broadcast_Message(string& message)
```

### GetTownControlBuffer

```angelscript
IBroadcastBuffer@ GetTownControlBuffer(int location)
```

### Broadcast_TownControl_Set

```angelscript
void Broadcast_TownControl_Set(string& message, int location, int time, int faction)
```

### Broadcast_TownControl_Set

```angelscript
void Broadcast_TownControl_Set(int location, int time, int faction)
```

### Broadcast_TownControl_Stop

```angelscript
void Broadcast_TownControl_Stop(int location)
```

### GetInfluenceBuffer

```angelscript
IBroadcastBuffer@ GetInfluenceBuffer(int location)
```

### Broadcast_Influence

```angelscript
IBroadcastBuffer@ Broadcast_Influence(int location, int time, string& message)
```

### Broadcast_RequestHelp

RequestHelp, returns id of a GM who received the broadcast 

```angelscript
uint Broadcast_RequestHelp(Critter@ player, string& message)
```

### Broadcast_CheckRequestHelpBuffer

```angelscript
void Broadcast_CheckRequestHelpBuffer(Critter@ gm)
```

### Broadcast_DumpRequestHelpBuffer

```angelscript
void Broadcast_DumpRequestHelpBuffer(Critter @gm)
```

### GetEventCountDownBuffer

```angelscript
IBroadcastBuffer@ GetEventCountDownBuffer(int location, int type)
```

### ServerEventCountDownStart

```angelscript
void ServerEventCountDownStart(string& message, int location, int time, int type)
```

### ServerEventCountDownStart

```angelscript
void ServerEventCountDownStart(int location, int time, int type)
```

### ServerEventCountDownStop

```angelscript
void ServerEventCountDownStop(int location, int type)
```

### wipe

```angelscript
void wipe(Critter& player, int, int, int)
```

### baseControl

```angelscript
void baseControl(string msg, int mapId, uint time)
```

### baseControlLocal

```angelscript
void baseControlLocal(string msg, int mapId, uint time)
```

### baseControlRadio

```angelscript
void baseControlRadio(string msg, uint time, int mapId, uint factionId)
```

### ServerEventMSG

```angelscript
void ServerEventMSG(uint time, string msg)
```

### ServerEventCNTSet

```angelscript
void ServerEventCNTSet(string message, uint location, uint type, uint time)
```

### ServerEventCNTSet

```angelscript
void ServerEventCNTSet(uint location, uint type, uint time)
```

### ServerEventCNTStop

```angelscript
void ServerEventCNTStop(uint location, uint type)
```

### V13test

```angelscript
void V13test(Critter& player, int time, int, int)
```

### V13teststart

```angelscript
void V13teststart(Critter& player, int location, int type, int seconds)
```

### V13teststarthuman

```angelscript
void V13teststarthuman(Critter& player, int location, int type, int seconds)
```

### V13teststop

```angelscript
void V13teststop(Critter& player, int location, int type, int)
```

### teststart

```angelscript
void teststart(Critter& player, int location, int type, int seconds)
```

### teststop

```angelscript
void teststop(Critter& player, int location, int type, int)
```


