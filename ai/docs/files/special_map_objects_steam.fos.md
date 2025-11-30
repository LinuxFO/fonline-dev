---
title: special_map_objects_steam.fos
description: " FOnline: 2238 Rotators  special_map_objects_steam.fos ..."
---

# special_map_objects_steam.fos


FOnline: 2238
Rotators

special_map_objects_steam.fos


## Included By

- [special_map_objects.fos](special_map_objects.fos.md)

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| STEAM_ON | `(0x01)` |  |
| STEAM_SPAWNER_PID | `(10014)` |  |
| STEAM_PID | `(PID_TANKER_STEAM)` |  |

## Classes

### CSteamSearcher

**Methods**

#### FindTogglableSMOs
```angelscript
uint FindTogglableSMOs(array<ITogglableSMO@>& list, Map& map, int globalId)
```

#### FindSteamObjects
```angelscript
uint FindSteamObjects(array<MapSteamObject@>& list, Map& map, int id)
```

### MapSteamObject

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| spawner | `Item@` |  |  |
| map | `Map@` |  |  |
| steamPid | `uint` |  |  |
| steam | `Item@` |  |  |
| steamInitialized | `bool` |  |  |

**Methods**

#### LazyInitSteam
```angelscript
void LazyInitSteam()
```

#### Toggle
```angelscript
void Toggle()
```

#### IsOn
```angelscript
bool IsOn()
```

#### IsOff
```angelscript
bool IsOff()
```

#### ForceOn
```angelscript
void ForceOn()
```

#### TurnOn
```angelscript
void TurnOn()
```

#### TurnOff
```angelscript
void TurnOff()
```

#### SetMovementRadius
```angelscript
void SetMovementRadius(uint radius)
```

#### GetMovementRadius
```angelscript
uint GetMovementRadius()
```

#### SetMovementInterval
```angelscript
void SetMovementInterval(uint interval)
```

#### GetMovementInterval
```angelscript
uint GetMovementInterval()
```

#### MoveSteam
```angelscript
uint MoveSteam()
```


## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| SteamSearcher | `[CSteamSearcher](special_map_objects_steam.fos.md)@` | `CSteamSearcher()` |  |

## Functions

### _InitSteamSpawner

```angelscript
void _InitSteamSpawner(Item& spawner, bool firstTime)
```

### s_SteamValve

```angelscript
bool s_SteamValve(Critter& player, Scenery& terminal, int skill, Item@ item, int steamId)
```

### s_SteamValve

```angelscript
bool s_SteamValve(Critter& player, Scenery& terminal, int skill, Item@ item, int steamId, int mapPid)
```

### e_StartSteam

```angelscript
uint e_StartSteam(array<uint>@ values)
```

### e_SpawnSteamItem

```angelscript
uint e_SpawnSteamItem(array<uint>@ values)
```


