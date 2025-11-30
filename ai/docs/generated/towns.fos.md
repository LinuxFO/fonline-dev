---
title: towns.fos
description: " FOnline: 2238 Rotators  towns.fos ..."
---

# towns.fos


FOnline: 2238
Rotators

towns.fos


## Includes

- `_entires.fos`
- `_macros.fos`
- `_maps.fos`
- `entire.fos`
- `town_h.fos`
- `polygon_towns.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __TOWNS__ |  |  |
| GET_CONT_POSITIONS | `# (__map) { GetNearEntire(__map, ENTIRE_TC_CONT_REWARD, rx, ry); GetNearEntire(__map, ENTIRE_TC_CONT_LIMBO, lx, ly); }` |  |
| ADD_TOWN | `# (__name, __db, __properties) ITown@ __name = CreateTown(__db); __name.__properties; AddTown(__name)` |  |

## Functions

### GetTownByIndex

```angelscript
ITown@ GetTownByIndex(uint index)
```

### GetTown

```angelscript
ITown@ GetTown(uint id)
```

### GetTownCount

```angelscript
uint GetTownCount()
```

### AddTown

```angelscript
void AddTown(ITown& town)
```

### GetTowns

```angelscript
uint GetTowns(array<ITown@>@ towns)
```

### VerifyMaps

```angelscript
bool VerifyMaps(array<Map@>& maps)
```

### InitTowns

```angelscript
void InitTowns()
```


