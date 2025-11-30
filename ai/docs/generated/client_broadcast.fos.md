---
title: client_broadcast.fos
description: " FOnline: 2238 Rotators  client_broadcast.fos ..."
---

# client_broadcast.fos


FOnline: 2238
Rotators

client_broadcast.fos


## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| SKIP_PRAGMAS |  |  |

## Classes

### CBroadcast

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| type | `int` |  |  |
| time | `uint` |  |  |
| message | `string` |  |  |
| extra | `uint` |  |  |
| kind | `uint` |  |  |


## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| Broadcast | `array<[CBroadcast](client_broadcast.fos.md)>` |  |  |

## Functions

### TimeToSeconds

```angelscript
int TimeToSeconds(uint& time)
```

### FindTimerTC

```angelscript
int FindTimerTC(uint location)
```

### FindEventCT

```angelscript
int FindEventCT(uint location, uint kind)
```

### FindInfluence

```angelscript
int FindInfluence(uint location)
```

### BroadcastProcess

```angelscript
void BroadcastProcess()
```

### BroadcastDraw

```angelscript
void BroadcastDraw()
```

### _ReceiveDump

```angelscript
void _ReceiveDump(int type, int time, int setup, string@ message, array<int>@ data)
```

### FindBaseControl

```angelscript
int FindBaseControl(uint location)
```

### _Receive

```angelscript
void _Receive(int type, int time, int setup, string@ message, array<int>@ data)
```


