---
title: map_tent.fos
description: " FOnline: 2238 Rotators  map_tent.fos ..."
---

# map_tent.fos


FOnline: 2238
Rotators

map_tent.fos


## Includes

- `_defines.fos`
- `_macros.fos`
- `_vars.fos`
- `MsgStr.h`
- `_colors.fos`
- `buffer_h.fos`
- `debug_h.fos`
- `follower_common_h.fos`
- `item_dynamic_h.fos`
- `item_misc_h.fos`
- `lexems_h.fos`
- `logging_h.fos`
- `mapdata_h.fos`
- `pdata_h.fos`
- `prod_ingredients_h.fos`
- `recycler_h.fos`
- `utils_h.fos`
- `map_tent_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __MAP_TENT__ |  |  |
| GARBAGE_TIMEOUT | `(REAL_DAY(7))` |  |
| CAMPFIRE_LIGHT_UPDATED | `# (_item)  _item.Val5` |  |
| TENT_VERSION | `(1)` |  |
| TENT_OWNER | `"tents:owner"` | avoid typos in pdata names |
| DYNAMIC_ITEMS | `"dynamicItems"` |  |
| _WLog |  |  |
| MSG_CAMPFIRE_MORE_WOOD | `(3065)` |  |
| MSG_CAMPFIRE_READY | `(3066)` |  |

## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| allTents | `array<uint>` |  | filled on init |
| allShelters | `array<uint>` |  |  |
| allHouses | `array<uint>` |  |  |

## Functions

### InitTents

```angelscript
void InitTents()
```

### GetTentLocationPid

```angelscript
uint GetTentLocationPid(uint mapType, bool house)
```

### map_init

```angelscript
void map_init(Map& map, bool firstTime)
```

### _TentEnviroment

```angelscript
void _TentEnviroment(Map& map)
```

### GetAllTents

```angelscript
uint GetAllTents(array<Location@>& locations)
```

### GetAllShelters

```angelscript
uint GetAllShelters(array<Location@>& locations)
```

### GetAllHouses

```angelscript
uint GetAllHouses(array<Location@>& locations)
```

### GetTentLocations

```angelscript
uint GetTentLocations(Critter& owner, array<Location@>& locations)
```

### GetTentLocations

```angelscript
uint GetTentLocations(uint ownerId, array<Location@>& locations)
```

### GetNearestTentLocation

```angelscript
Location@ GetNearestTentLocation(Critter& owner, uint16 wx, uint16 wy)
```

### GetNearestTentLocation

```angelscript
Location@ GetNearestTentLocation(uint ownerId, uint16 wx, uint16 wy)
```

### CreateTent

```angelscript
bool CreateTent(Critter& leader, uint& out id, uint locationpid, bool easterEgg)
```

### TryCreateTent

```angelscript
void TryCreateTent(Critter& cr)
```

### CanCreateTent

```angelscript
bool CanCreateTent(Map& map)
```

### RemoveTent

```angelscript
bool RemoveTent(Critter& cr, uint locId, bool recycle)
```

### RemoveAllTents

```angelscript
void RemoveAllTents(Critter& cr, bool recycle)
```

### removeall

```angelscript
void removeall(Critter& cr, int, int, int recycle)
```

### GetTentVersion

```angelscript
uint GetTentVersion(Location& tent)
```

### GetTentVersion

```angelscript
uint GetTentVersion(Map& tent)
```

### IsTentOwner

```angelscript
bool IsTentOwner(Location& tent, Critter& cr)
```

### IsTentOwner

```angelscript
bool IsTentOwner(Location& tent, uint crId)
```

### IsTentOwner

```angelscript
bool IsTentOwner(Map& tent, Critter& cr)
```

### _RegenItem

```angelscript
void _RegenItem(Item& item, bool firstTime)
```

### _RegenItemSkill

```angelscript
bool _RegenItemSkill(Item& item, Critter& player, int skill)
```

### SetCampfireLight

```angelscript
void SetCampfireLight(Item& campfire, uint8 value)
```

### MakeCampfireUsuable

```angelscript
void MakeCampfireUsuable(Item& campfire)
```

### MakeCampfireUnusuable

```angelscript
void MakeCampfireUnusuable(Item& campfire)
```

### _Campfire

```angelscript
void _Campfire(Item& item, bool firstTime)
```

### _UseItemCampfire

```angelscript
bool _UseItemCampfire(Item& item, Critter& cr, Item@ usedItem)
```

### _UseSkillCampfire

Using campfire

```angelscript
bool _UseSkillCampfire(Item& item, Critter& player, int skill)
```

### _Drop

```angelscript
void _Drop(Item& item, Critter& cr)
```

### GetCampfire

```angelscript
Item@ GetCampfire(Critter& player)
```

### d_IsNotTentOwner

```angelscript
bool d_IsNotTentOwner(Critter& player, Critter@)
```

### d_IsKnownLocation

```angelscript
bool d_IsKnownLocation(Critter& player, Critter@)
```

### r_ForgetLocation

```angelscript
void r_ForgetLocation(Critter& player, Critter@)
```

### r_ThrowSomething

```angelscript
uint r_ThrowSomething(Critter& player, Critter@)
```

### ExplosivePreProcess

```angelscript
bool ExplosivePreProcess( uint16& pid )
```

### answer_ThrowSomething

```angelscript
void answer_ThrowSomething(Critter& cr, uint itemId, string&)
```

### e_ThrowingExplode

```angelscript
uint e_ThrowingExplode(array<uint>@ values)
```

### d_IsTentOwner

```angelscript
bool d_IsTentOwner(Critter& player, Critter@)
```

### r_TentName

```angelscript
uint r_TentName(Critter& player, Critter@)
```

### answer_TentName

```angelscript
void answer_TentName(Critter& player, uint, string& name)
```

### r_CreateMap

```angelscript
uint r_CreateMap(Critter& player, Critter@)
```

### r_CreateMapFarm

```angelscript
uint r_CreateMapFarm(Critter& player, Critter@)
```

### d_IsUpgradeAvailable

```angelscript
bool d_IsUpgradeAvailable(Critter& player, Critter@, int pid)
```

### r_InstallUpgrade

```angelscript
void r_InstallUpgrade(Critter& player, Critter@, int pid)
```

### r_AbandonTent

```angelscript
uint r_AbandonTent(Critter& player, Critter@)
```

### answer_AbandonTent

```angelscript
void answer_AbandonTent(Critter& player, uint, string&)
```

### myinfo_tent

```angelscript
void myinfo_tent(Critter& player)
```


