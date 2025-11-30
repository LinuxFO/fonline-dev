---
title: replication.fos
---

# replication.fos

## Includes

- `_macros.fos`
- `_basetypes.fos`
- `follower_h.fos`
- `factions_bases_h.fos`
- `npc_common_h.fos`
- `follower_common_h.fos`
- `world_common_h.fos`
- `entire.fos`
- `logging_h.fos`
- `map_tent_h.fos`
- `minigames_h.fos`
- `npc_roles_h.fos`
- `utils_h.fos`
- `MsgStr.h`
- `mapdata_h.fos`

## Functions

### GetNearestReplicatorMap

```angelscript
Map@ GetNearestReplicatorMap(Critter& player)
```

### GetRandomReplicatorMap

```angelscript
Map@ GetRandomReplicatorMap(Critter& player)
```

### GetStartingMap

```angelscript
Map@ GetStartingMap(Critter& player)
```

### SetStartLocation

```angelscript
void SetStartLocation(Critter& cr)
```

### SetReplicationTime

```angelscript
void SetReplicationTime(Critter& cr)
```

### DropItems

```angelscript
void DropItems(Critter& cr)
```

### TryFindCompanionRespawn

```angelscript
Map@ TryFindCompanionRespawn(Critter& cr, uint16& hx, uint16& hy, bool TryAny)
```

### ReplicateCritter

```angelscript
void ReplicateCritter(Critter& cr)
```


