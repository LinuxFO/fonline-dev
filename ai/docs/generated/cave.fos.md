---
title: cave.fos
description: " FOnline: 2238 Rotators  cave.fos ..."
---

# cave.fos


FOnline: 2238
Rotators

cave.fos


## Includes

- `_macros.fos`
- `cave_critter_h.fos`
- `cave_h.fos`
- `cave_item_h.fos`
- `entire.fos`
- `groups_h.fos`
- `mapdata_h.fos`
- `npc_common_h.fos`
- `utils_h.fos`
- `worldmap_h.fos`

## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| corpse_bags | `array<uint>` |  |  |

## Functions

### GetCaveItem

```angelscript
ICaveItem@ GetCaveItem(Critter& player)
```

### GetCaveCritter

```angelscript
ICaveCritter@ GetCaveCritter(ICaveGroup@ group)
```

### FillItems

```angelscript
bool FillItems(Map@ map, Critter& player)
```

### FillCritters

```angelscript
bool FillCritters(Map@ map, Critter& player)
```

### SelectCorpseBag

```angelscript
int SelectCorpseBag(uint crpid)
```

### AddCorpse

```angelscript
void AddCorpse(Map@ map, Critter& player, Entire@ entire)
```

### FillMap

```angelscript
bool FillMap(Map@ map, Critter& player)
```

### InitCaveRandomization

```angelscript
void InitCaveRandomization()
```


