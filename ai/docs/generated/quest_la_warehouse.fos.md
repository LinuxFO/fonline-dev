---
title: quest_la_warehouse.fos
description: " FOnline: 2238 Rotators  quest_la_warehouse.fos ..."
---

# quest_la_warehouse.fos


FOnline: 2238
Rotators

quest_la_warehouse.fos


## Includes

- `_colors.fos`
- `_maps.fos`
- `_vars.fos`
- `_macros.fos`
- `mapdata_h.fos`
- `npc_planes_h.fos`
- `messages_h.fos`
- `guard_h.fos`
- `npc_common_h.fos`
- `utils_h.fos`
- `entire.fos`
- `_entires.fos`
- `logging_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| DIALOG_WAREHOUSE_MAIN | `(10272)` |  |
| RUN_AWAY | `(2)` |  |
| ALL_KILLED | `(3)` |  |

## Functions

### r_SpawnMap

```angelscript
void r_SpawnMap(Critter& player, Critter@ npc)
```

### r_DeleteMap

Should be called after var x in dialog is set and player leaves the map, so location gets deleted.

```angelscript
void r_DeleteMap(Critter& critter, Critter@ npc, bool firstTime)
```

### GetOwner

```angelscript
Critter@ GetOwner(Map& map)
```

### GetOwnerId

```angelscript
uint GetOwnerId(Map& map)
```

### r_RemovePunks

```angelscript
void r_RemovePunks(Critter& player, Critter@ tray)
```

### r_FlushScreen

```angelscript
void r_FlushScreen(Critter& player, Critter@ tray)
```

### r_RemoveWeapon

```angelscript
void r_RemoveWeapon(Critter& player, Critter@ tray)
```

### t_StartAmbush

```angelscript
void t_StartAmbush(Critter& cr, Scenery& trigger, bool entered, uint8 dir)
```

### t_PunkAttack

```angelscript
void t_PunkAttack(Critter& cr, Scenery& trigger, bool entered, uint8 dir)
```

### _Punk

```angelscript
void _Punk(Critter& cr, bool firstTime)
```

### _PunkDead

```angelscript
void _PunkDead(Critter& cr, Critter@ killer)
```

### _Attacked

```angelscript
bool _Attacked(Critter& cr, Critter& attacker)
```

### _OnMessage

```angelscript
void _OnMessage(Critter& cr, Critter& fromCr, int message, int value)
```

### SendPunksToSleep

```angelscript
void SendPunksToSleep(Map& map)
```

### GetPunks

```angelscript
uint GetPunks(Map& map, array<Critter@>@ critters)
```

### CheckOwner

```angelscript
void CheckOwner(Critter& cr, int p0, int p1, int p2)
```

### CheckPunks

```angelscript
void CheckPunks(Critter& cr, int p0, int p1, int p2)
```

### PointPunks

```angelscript
void PointPunks(Critter& cr, int p0, int p1, int p2)
```


