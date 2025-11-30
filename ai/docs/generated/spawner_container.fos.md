---
title: spawner_container.fos
description: " FOnline: 2238 Rotators  spawner_container.fos ..."
---

# spawner_container.fos


FOnline: 2238
Rotators

spawner_container.fos


## Includes

- `_macros.fos`
- `ITEMPID.H`
- `spawner_container_h.fos`
- `debug_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __SPAWNER_CONTAINER_MODULE__ |  |  |
| SPAWN_INTERVAL | `# (_time)  REAL_MINUTE(_time)` |  |
| ADD_ITEMSPAWNER | `# (_name, _prop) ItemSpawner@ _name = @ItemSpawner(); _name._prop; spawners.insertLast(_name)` |  |

## Classes

### ItemInstance

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| Pid | `uint` |  |  |
| Chance | `uint` |  |  |
| Min | `uint` |  |  |
| Max | `uint` |  |  |

### ItemSpawner

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| SumChance | `uint` |  |  |
| SpawnTimeMin | `uint` |  |  |
| SpawnTimeMax | `uint` |  |  |
| LockerMin | `uint16` |  |  |
| LockerMax | `uint16` |  |  |
| Separate | `bool` |  |  |
| Bonus | `bool` |  |  |
| BonusLow | `bool` |  |  |
| ClearAtSpawn | `bool` |  |  |

**Methods**

#### GetSpawnTime
```angelscript
uint GetSpawnTime()
```

#### GetLock
```angelscript
uint GetLock()
```

#### Lock
```angelscript
IItemSpawner@ Lock(uint16 min, uint16 max)
```

#### SpawnTime
```angelscript
IItemSpawner@ SpawnTime(uint min, uint max)
```

#### AddItem
```angelscript
IItemSpawner@ AddItem(uint16 pid, uint chance, uint min, uint max)
```

#### AddItem
```angelscript
IItemSpawner@ AddItem(uint16 pid, uint chance)
```

#### SetSeparate
```angelscript
IItemSpawner@ SetSeparate(bool separate)
```

#### SetBonus
```angelscript
IItemSpawner@ SetBonus(bool bonus)
```

#### SetBonusLow
```angelscript
IItemSpawner@ SetBonusLow(bool bonusLow)
```

#### SetClearAtSpawn
```angelscript
IItemSpawner@ SetClearAtSpawn(bool clearSpawn)
```

#### Clear
```angelscript
IItemSpawner@ Clear()
```

#### Spawn
```angelscript
uint Spawn(Item& item)
```

#### GetValue
```angelscript
uint GetValue()
```

#### LogValue
```angelscript
void LogValue(string& st)
```


## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| Init | `bool` | `false` |  |

## Functions

### ItemSpawnInit

```angelscript
void ItemSpawnInit()
```


