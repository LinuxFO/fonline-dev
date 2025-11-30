---
title: shuffling_spawner.fos
description: " FOnline: 2238 Rotators  shuffling_spawner.fos ..."
---

# shuffling_spawner.fos


FOnline: 2238
Rotators

shuffling_spawner.fos


## Includes

- `_macros.fos`
- `debug_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| SPAWNDATA_NUMBER | `# (item)        (item.Val0)` |  |

## Classes

### SpawnData

**Methods**

#### Add
```angelscript
SpawnData@ Add(uint16 pid, uint chance)
```

#### SetDelay
```angelscript
SpawnData@ SetDelay(uint time)
```

#### TryRespawn
```angelscript
bool TryRespawn(Map& map, Item& marker, Item& item)
```

#### Respawn
```angelscript
bool Respawn(Map& map, Item& marker, Item@ item)
```


## Functions

### NewSpawnData

```angelscript
SpawnData@ NewSpawnData(uint index)
```

### GetSpawnData

```angelscript
SpawnData@ GetSpawnData(uint num)
```

### ShuffleItem

```angelscript
bool ShuffleItem(Item& item)
```

### e_Respawn

```angelscript
uint e_Respawn(array<uint>@ values)
```

### InitShufflingSpawns

```angelscript
void InitShufflingSpawns()
```

### _InitSpot

Default spawn data

```angelscript
void _InitSpot(Item& item, bool firstTime)
```

### e_InitSpot

```angelscript
uint e_InitSpot(array<uint>@ values)
```


