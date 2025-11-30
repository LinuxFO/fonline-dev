---
title: explode.fos
description: " FOnline: 2238 Rotators  explode.fos ..."
---

# explode.fos


FOnline: 2238
Rotators

explode.fos


## Includes

- `MsgStr.h`
- `_macros.fos`
- `groups_h.fos`
- `lexems_h.fos`
- `logging_h.fos`
- `mapdata_h.fos`
- `npc_common_h.fos`
- `npc_planes_h.fos`
- `reputations_h.fos`
- `utils_h.fos`
- `world_common_h.fos`
- `traps_h.fos`
- `_math.fos`
- `_colors.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __TRAPS_MODULE__ |  |  |
| EXPLODE_CLEARANCE_EXPERIENCE | `(150)` |  |
| DOOR_RESPAWN_TIME | `(REAL_MINUTE(30))` |  |

## Functions

### ExpLog

```angelscript
void ExpLog(string& s)
```

### OnUseExplode

Global on use, export

```angelscript
bool OnUseExplode(Critter& cr, Item& explode, Critter@ targetCr, Item@ targetItem, Scenery@ targetScen, uint timer)
```

### _ExplodeInit

Explosions initialisation

```angelscript
void _ExplodeInit(Item& item, bool firstTime)
```

### _MineWalk

Item walk event

```angelscript
void _MineWalk(Item& mine, Critter& cr, bool entered, uint8 dir)
```

### e_Explode

Time event

```angelscript
uint e_Explode(array<uint>@ values)
```

### MakeMine

* * Sets the spear trap script for the item and assigns its parameters. NOTE: import this function from explode module. * @param     mine			The item to become a spear trap * @param     explodeOwner	Id of the critter responsible for setting the trap up * @param     complexity     Trap complexity * @param     hideSkill      The value of traps skill used to hide the item, 0 to disable * @param     bonusDamage       Bonus radius of the explosion * @param     bonusDamage       Bonus damage dealt upon the trap activation 

```angelscript
void MakeMine(Item& mine, uint explodeOwner, uint complexity, uint hideSkill, uint bonusDamage, uint bonusRadius)
```

### RemoveActiveExplosives

```angelscript
void RemoveActiveExplosives(Map@ map, uint16 hexX, uint16 hexY, uint radius)
```

### Explode

```angelscript
void Explode(Map@ map, uint16 hexX, uint16 hexY, Critter@ cr, uint16 explodePid, uint ownerId, int bonusDamage, int bonusRadius)
```

### ExplodeEx

```angelscript
void ExplodeEx(Map& map, uint16 hexX, uint16 hexY, uint16 effectPid, uint effectRadius, uint damage, uint damageType, uint damageRadius, uint ownerId, uint16 explodePid)
```

### ExplodeDoor

```angelscript
void ExplodeDoor(Item& door, int damage, Critter& attacker, uint16 explodePid)
```

### e_RespawnDoor

```angelscript
uint e_RespawnDoor(array<uint>@ values)
```

### _OnExplDrop

```angelscript
void _OnExplDrop(Item& item, Critter& crit)
```


