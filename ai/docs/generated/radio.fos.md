---
title: radio.fos
description: " FOnline: 2238 Rotators  radio.fos ..."
---

# radio.fos


FOnline: 2238
Rotators

radio.fos


## Includes

- `_macros.fos`

## Classes

### ScreenMain

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| Channel | `[TextboxChannel](radio.fos.md)@` |  |  |
| Send | `[ButtonSendRecv](radio.fos.md)@` |  |  |
| Recv | `[ButtonSendRecv](radio.fos.md)@` |  |  |
| SendDial | `[DialButton](radio.fos.md)@` |  |  |
| RecvDial | `[DialButton](radio.fos.md)@` |  |  |
| BroadcastSendType | `int` |  |  |
| BroadcastRecvType | `int` |  |  |
| RadioId | `int` |  |  |
| RadioChannel | `uint16` |  |  |
| RadioBroadcastSend | `int` |  |  |
| RadioBroadcastRecv | `int` |  |  |
| RadioFlags | `int` |  |  |

**Methods**

#### OnShow
```angelscript
void OnShow(int radioId, int radioChannel, int radioData)
```

#### ChangeChannel
```angelscript
void ChangeChannel()
```

#### ChangeActivity
```angelscript
void ChangeActivity(bool isSend)
```

#### ChangeBroadcast
```angelscript
void ChangeBroadcast(bool isSend, int type)
```

### TextboxChannel

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| Instance | `[ScreenMain](radio.fos.md)@` |  |  |
| RadioChannel | `uint16` |  |  |

**Methods**

#### KeyDown
```angelscript
bool KeyDown(uint8 key,string& keyText)
```

#### SetChannel
```angelscript
void SetChannel(uint16 channel)
```

### ButtonRefresh

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| Instance | `[ScreenMain](radio.fos.md)@` |  |  |

**Methods**

#### Click
```angelscript
void Click()
```

### ButtonSendRecv

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| Instance | `[ScreenMain](radio.fos.md)@` |  |  |
| IsSend | `bool` |  |  |
| IsPressed | `bool` |  |  |

**Methods**

#### Click
```angelscript
void Click()
```

#### Draw
```angelscript
void Draw()
```

#### SetPressed
```angelscript
void SetPressed(bool pressed)
```

### DialButton

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| Instance | `[ScreenMain](radio.fos.md)@` |  |  |
| IsSend | `bool` |  |  |
| Type | `int` |  |  |
| Dir | `bool` |  |  |
| MaxType | `int` |  |  |
| Surface | `array<[Sprite](sprite.fos.md)>` |  |  |

**Methods**

#### Click
```angelscript
void Click()
```

#### SetType
```angelscript
void SetType(int type)
```

#### Draw
```angelscript
void Draw()
```


## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| Init | `bool` | `false` |  |

## Functions

### EditRadioSettings

```angelscript
void EditRadioSettings(Critter& player, Item& radio)
```

### unsafe_ChangeChannel

```angelscript
void unsafe_ChangeChannel(Critter& player, int radioId, int radioChannel, int, string@, array<int>@)
```

### unsafe_ChangeActivity

```angelscript
void unsafe_ChangeActivity(Critter& player, int radioId, int isSend, int, string@, array<int>@)
```

### unsafe_ChangeBroadcast

```angelscript
void unsafe_ChangeBroadcast(Critter& player, int radioId, int broadcastSend, int broadcastRecv, string@, array<int>@)
```

### SetInHand

```angelscript
void SetInHand(Critter& player, int flags, int broadcastSend, int broadcastRecv)
```

### UnsetInHand

```angelscript
void UnsetInHand(Critter& player, int, int, int)
```

### InitRadioScreen

```angelscript
void InitRadioScreen()
```

### ShowEditScreen

```angelscript
void ShowEditScreen(int itemId, int, int, string@, array<int>@)
```


