---
title: mob_wave.fos
description: " FOnline: 2238 Rotators  mob_wave.fos ..."
---

# mob_wave.fos


FOnline: 2238
Rotators

mob_wave.fos


## Includes

- `MsgStr.h`
- `_ai.fos`
- `_macros.fos`
- `_npc_pids.fos`
- `_time.fos`
- `follower_common_h.fos`
- `mapdata_h.fos`
- `mob_wave_h.fos`
- `npc_planes_h.fos`
- `npc_roles_h.fos`
- `utils_h.fos`
- `mob_wave_data.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __MOB_WAVE__ |  |  |

## Functions

### TryStartEncounterMobWave

```angelscript
void TryStartEncounterMobWave(Map& map)
```

### StartMobWave

```angelscript
void StartMobWave(Location@ loc, uint type, uint level, uint timeScale)
```

### EraseMobWave

```angelscript
void EraseMobWave(Location@ loc)
```

### e_MobWave

```angelscript
uint e_MobWave(array<uint>@ data)
```

### SpawnMobWaveAtCritter

```angelscript
void SpawnMobWaveAtCritter(Critter@ cr, array<uint>@ data, array<Item@>@ spots)
```

### start

Start a mob wave in the location 

```angelscript
void start(Critter& cr, int type, int level, int timeScale)
```

### erase

Erase mob wave in the location 

```angelscript
void erase(Critter& cr, int, int, int)
```

### info

```angelscript
void info(Critter& cr, int, int, int)
```

### spots_show

```angelscript
void spots_show(Critter& cr, int, int, int)
```

### spots_hide

```angelscript
void spots_hide(Critter& cr, int, int, int)
```

### spots_add

```angelscript
void spots_add(Critter& cr, int, int, int)
```

### spots_delete

```angelscript
void spots_delete(Critter& cr, int, int, int)
```


