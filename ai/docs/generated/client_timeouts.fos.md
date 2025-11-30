---
title: client_timeouts.fos
description: " FOnline: 2238 Rotators  client_timeouts.fos ..."
---

# client_timeouts.fos


FOnline: 2238
Rotators

client_timeouts.fos


## Includes

- `_defines.fos`
- `_client_defines.fos`
- `_macros.fos`
- `_colors.fos`
- `config_file_h.fos`
- `client_utils_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __CLIENT_TIMEOUTS__ |  |  |
| __CLIENT |  |  |
| CUSTOM_TIMEOUTS |  |  |
| TO_SECTION | `"Timeouts"` |  |
| TO_GATHERING_OK | `(20 * 60)` | temp |
| TO_CRAFTING_OK | `(60 * 60)` |  |

## Classes

### CTimeout

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| Enabled | `bool` |  |  |
| Direction | `uint` |  |  |
| PositionX | `int` |  |  |
| PositionY | `int` |  |  |
| SpacingX | `uint` |  |  |
| SpacingY | `uint` |  |  |
| NameColor | `uint` |  |  |
| ValueColor | `uint` |  |  |
| Alpha | `uint` |  |  |
| Font | `uint` |  |  |
| FontFlags | `uint` |  |  |
| Worldmap | `bool` |  |  |
| WorldmapX | `int` |  |  |
| WorldmapY | `int` |  |  |
| TimeFormat | `uint` |  |  |
| Ini | `array<string>` |  |  |

### CTimeoutCustom

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| PositionX | `int` |  |  |
| PositionY | `int` |  |  |
| SpacingX | `uint` |  |  |
| NameColor | `uint` |  |  |
| ValueColor | `uint` |  |  |
| Alpha | `uint` |  |  |
| Font | `uint` |  |  |
| ShowLabel | `bool` |  |  |
| CustomMode | `int` |  |  |

**Methods**

#### SetValues
```angelscript
void SetValues(int x, int y, uint sx, uint8 nR, uint8 nG, uint8 nB, uint8 vR, uint8 vG, uint8 vB, uint8 f, bool sl)
```

#### SetValues
```angelscript
void SetValues(uint8 nR, uint8 nG, uint8 nB, uint8 vR, uint8 vG, uint8 vB)
```

### MyTimeout

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| name | `string` |  |  |
| value | `uint` |  |  |
| tick | `uint` |  |  |


## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| Timeouts | `[CTimeout](client_timeouts.fos.md)` |  |  |
| TimeoutsCustom | `array<[CTimeoutCustom](client_timeouts.fos.md)>` |  |  |
| MyTimeouts | `array<[MyTimeout](client_timeouts.fos.md)>` |  |  |

## Functions

### TimeoutsConfig

```angelscript
void TimeoutsConfig(string& customConfig)
```

### screen_timeouts_draw

 void screen_timeouts_save() { } 

```angelscript
int screen_timeouts_draw(CritterCl& critter, uint skill, string& skillname, int x, int y, uint z, uint userCustomMode)
```

### screen_timeouts_draw

```angelscript
int screen_timeouts_draw(CritterCl& critter, uint skill, string& skillname, int x, int y, bool custom, uint z, uint userCustomMode)
```

### TimeoutsDraw

```angelscript
void TimeoutsDraw()
```

### TimeoutsCommand

```angelscript
bool TimeoutsCommand(string& message)
```

### screen_timeouts_add

```angelscript
void screen_timeouts_add(string& name, int value)
```

### screen_timeouts_add

```angelscript
void screen_timeouts_add(string& name, int value, int tick)
```

### _add_unsafe

```angelscript
void _add_unsafe(int value, int, int, string@ name, array<int>@)
```

### _add_unsafe

avoid errors

```angelscript
void _add_unsafe(int value, int p1, int p2, string@ name, array<int>@ unused)
```


