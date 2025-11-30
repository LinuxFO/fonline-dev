---
title: special_map_objects.fos
description: " FOnline: 2238 Rotators  special_map_objects.fos ..."
---

# special_map_objects.fos


FOnline: 2238
Rotators

special_map_objects.fos


## Includes

- `_macros.fos`
- `MsgStr.h`
- `utils_h.fos`
- `traps_h.fos`
- `special_map_objects_forcefield.fos`
- `special_map_objects_steam.fos`
- `special_map_objects_floor.fos`

## Functions

### InitializeSMOs

```angelscript
void InitializeSMOs()
```

### AddCallback

```angelscript
void AddCallback(ISearchingCallback@ newCallback)
```

### FindSMOs

```angelscript
uint FindSMOs(array<ITogglableSMO@>& smos, Map& map, int globalId)
```

### r_SMOToggle

```angelscript
void r_SMOToggle(Critter& player, Critter@ npc, int globalId)
```

### r_SMOToggle

```angelscript
void r_SMOToggle(Critter& player, Critter@ npc, int globalId, int mapPid)
```

### r_SMOOn

```angelscript
void r_SMOOn(Critter& player, Critter@ npc, int globalId)
```

### r_SMOOn

```angelscript
void r_SMOOn(Critter& player, Critter@ npc, int globalId, int mapPid)
```

### r_SMOOff

```angelscript
void r_SMOOff(Critter& player, Critter@ npc, int globalId)
```

### r_SMOOff

```angelscript
void r_SMOOff(Critter& player, Critter@ npc, int globalId, int mapPid)
```

### ToggleSMO

```angelscript
void ToggleSMO(Map@ map, int globalId)
```

### SetSMOOn

```angelscript
void SetSMOOn(Map@ map, int globalId)
```

### SetSMOOff

```angelscript
void SetSMOOff(Map@ map, int globalId)
```


