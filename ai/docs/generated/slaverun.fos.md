---
title: slaverun.fos
description: " FOnline: 2238 Rotators  slaverun.fos ..."
---

# slaverun.fos


FOnline: 2238
Rotators

slaverun.fos


## Includes

- `_macros.fos`
- `_ai.fos`
- `entire.fos`
- `follower_common_h.fos`
- `slaverun_h.fos`
- `groups_h.fos`
- `_scripts.fos`
- `utils_h.fos`
- `logging_h.fos`
- `slaverun_init.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| HOSTILES | `(1)` |  |
| NORMALS | `(2)` |  |
| SLAVERS | `(5)` |  |
| TAKEENTIRES | `\` | now it's the time for the most ugly macro ever: |

## Classes

### SlaverunLoc

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| LocPid | `uint` |  |  |
| X1 | `uint` |  |  |
| Y1 | `uint` |  |  |
| X2 | `uint` |  |  |
| Y2 | `uint` |  |  |
| Hostiles | `array<uint>` |  |  |
| Normals | `array<uint>` |  |  |
| Hscript | `string` |  |  |
| Nscript | `string` |  |  |
| Hpack | `uint` |  |  |
| Npack | `uint` |  |  |
| Hdialog | `uint` |  |  |
| Ndialog | `uint` |  |  |
| Sdialog | `uint` |  |  |
| Hlevel | `uint` |  |  |
| Nlevel | `uint` |  |  |
| Slevel | `uint` |  |  |
| Reward | `uint` |  |  |
| NoItems | `bool` |  |  |
| Weaps | `array<uint>` |  |  |
| Items | `array<uint>` |  |  |
| ContItems | `array<uint>` |  |  |

**Methods**

#### SetLocPid
```angelscript
ISlaverunLoc@ SetLocPid(uint pid)
```

#### SetCoords
```angelscript
ISlaverunLoc@ SetCoords(uint x1, uint y1, uint x2, uint y2)
```

#### SetReward
```angelscript
ISlaverunLoc@ SetReward(uint reward)
```

#### SetLevels
```angelscript
ISlaverunLoc@ SetLevels(uint hlevel, uint nlevel, uint slevel)
```

#### SetNoItems
```angelscript
ISlaverunLoc@ SetNoItems()
```

#### GetLocPid
```angelscript
uint GetLocPid()
```

#### GetReward
```angelscript
uint GetReward()
```

#### AddHostile
```angelscript
ISlaverunLoc@ AddHostile(uint pid)
```

#### AddNormal
```angelscript
ISlaverunLoc@ AddNormal(uint pid)
```

#### Scripts
```angelscript
ISlaverunLoc@ Scripts(string& script1, string& script2)
```

#### AIPacks
```angelscript
ISlaverunLoc@ AIPacks(uint pack1, uint pack2)
```

#### Dialogs
```angelscript
ISlaverunLoc@ Dialogs(uint dialog1, uint dialog2, uint sdialog)
```

#### AddWeapon
```angelscript
ISlaverunLoc@ AddWeapon(uint pid, uint ammo, uint min, uint max)
```

#### AddItem
```angelscript
ISlaverunLoc@ AddItem(uint pid, uint chance, uint min, uint max)
```

#### AddContItem
```angelscript
ISlaverunLoc@ AddContItem(uint pid, uint chance, uint min, uint max)
```

#### SpawnHostile
```angelscript
bool SpawnHostile(Map@ map, uint16 hexX, uint16 hexY)
```

#### SpawnNormal
```angelscript
bool SpawnNormal(Map@ map, uint16 hexX, uint16 hexY)
```

#### FillContainer
```angelscript
void FillContainer(Map@ map, uint16 hexX, uint16 hexY)
```

#### SpawnSlaver
```angelscript
bool SpawnSlaver(Map@ map, uint16 hexX, uint16 hexY, uint teamId)
```

#### Create
```angelscript
uint Create(Critter@ player)
```


## Functions

### InitSlaveruns

```angelscript
void InitSlaveruns()
```

### FillMap

```angelscript
void FillMap(Map@ map, uint& hostiles, uint& normals, uint& slavers, uint teamId)
```


