---
title: mercs_h.fos
description: " FOnline: 2238 Rotators  mercs_h.fos ..."
---

# mercs_h.fos


FOnline: 2238
Rotators

mercs_h.fos


## Includes

- `_macros.fos`
- `lexems_h.fos`
- `utils_h.fos`
- `npc_common_h.fos`
- `npc_names_h.fos`
- `follower_h.fos`
- `serializator.fos`

## Included By

- [follower.fos](follower.fos.md)
- [follower_common.fos](follower_common.fos.md)
- [follower_common_h.fos](follower_common_h.fos.md)
- [merc_dialog.fos](merc_dialog.fos.md)
- [mercs.fos](mercs.fos.md)

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __MERCS_H__ |  |  |

## Classes

### CMerc

Base hireling

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| dynamicprice | `bool` |  |  |
| dir | `int` |  |  |
| dialogid | `int` |  |  |
| script | `string` |  |  |
| aipack | `int` |  |  |
| basetype | `int8` |  |  |
| bagid | `int` |  |  |
| teamid | `int` |  |  |
| level | `int` |  |  |
| respawnTime | `int` |  |  |
| npcpids | `array<int>` |  |  |
| npcpid | `int` |  |  |
| cost | `int` |  |  |
| bagvalue | `int` |  |  |
| startcost | `int` |  |  |
| type | `uint` |  |  |
| sellprice | `int` |  |  |
| id | `uint` |  |  |
| name | `string` |  |  |
| serializer | `[Serializator](serializator.fos.md)` |  |  |

**Methods**

#### Spawn
```angelscript
bool Spawn(Critter& master)
```

#### Dialog
```angelscript
IMerc@ Dialog(int dialogid)
```

#### Script
```angelscript
IMerc@ Script(string& script)
```

#### AI
```angelscript
IMerc@ AI(int aipack)
```

#### Bag
```angelscript
IMerc@ Bag(int bagid)
```

#### Team
```angelscript
IMerc@ Team(int teamid)
```

#### Level
```angelscript
IMerc@ Level(int level)
```

#### PID
```angelscript
IMerc@ PID(int npcpid)
```

#### PID
```angelscript
IMerc@ PID(array<int> npcpids)
```

#### Type
```angelscript
IMerc@ Type(int type)
```

#### ID
```angelscript
IMerc@ ID(int id)
```

#### DynamicPrice
```angelscript
IMerc@ DynamicPrice()
```

#### IsDynamicPrice
```angelscript
bool IsDynamicPrice()
```

#### StartCost
```angelscript
IMerc@ StartCost(int cost)
```

#### Cost
```angelscript
IMerc@ Cost(int cost)
```

#### SellPrice
```angelscript
IMerc@ SellPrice(int sellprice)
```

#### GetDialog
```angelscript
int        GetDialog()    { return dialogid; }
```

#### GetScript
```angelscript
string@    GetScript()    { return script; }
```

#### GetBaseType
```angelscript
int8       GetBaseType()  { return basetype; }
```

#### GetAIPack
```angelscript
int        GetAIPack()    { return aipack; }
```

#### GetBagID
```angelscript
int        GetBagID()     { return bagid; }
```

#### GetTeamID
```angelscript
int        GetTeamID()    { return teamid; }
```

#### GetLevel
```angelscript
int        GetLevel()     { return level; }
```

#### GetLastPID
```angelscript
int        GetLastPID()   { return npcpid; }
```

#### GetPIDs
```angelscript
array<int> GetPIDs()      { return npcpids; }
```

#### GetCost
```angelscript
int        GetCost()      { return cost; }
```

#### GetBagValue
```angelscript
int        GetBagValue()  { return bagvalue; }
```

#### GetSellPrice
```angelscript
int        GetSellPrice() { return sellprice; }
```

#### GetID
```angelscript
uint       GetID()        { return id; }
```

#### GetType
```angelscript
uint       GetType()      { return type; }
```

#### GetName
```angelscript
string@    GetName()      { return name; }
```


## Functions

### e_DisableBagRefresh

Deprecate this in the future, maybe now.

```angelscript
uint e_DisableBagRefresh(array<uint>@ values)
```

### NerfWeaponSkills

```angelscript
void NerfWeaponSkills(Critter& cr, uint primary, uint secondary)
```


