---
title: main_planes.fos
description: " FOnline: 2238 Rotators  main_planes.fos ..."
---

# main_planes.fos


FOnline: 2238
Rotators

main_planes.fos


## Includes

- `_macros.fos`
- `_npc_pids.fos`
- `_vals.fos`
- `groups_h.fos`
- `linetracer_h.fos`
- `npc_ai.fos`
- `npc_common_h.fos`
- `npc_planes_h.fos`
- `utils_h.fos`
- `traps_h.fos`
- `mapdata_h.fos`

## Classes

### CTraceFirstCritter

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| Cr | `Critter@` |  |  |
| Mindist | `uint` |  |  |
| Gx | `uint16` |  |  |
| Gy | `uint16` |  |  |

**Methods**

#### Exec
```angelscript
bool Exec(Map& map, uint16 hx, uint16 hy)
```


## Functions

### plane2str

```angelscript
string plane2str(uint plane)
```

### reason2str

```angelscript
string reason2str(uint reason)
```

### npc_plane_begin

///////////////////////////////////////////////////////////////////////////////////////////////// Called on some plane added. Return true to allow plane, false to disallow. REASON_GO_HOME REASON_FOUND_IN_ENEMY_STACK   someCr as Enemy REASON_FROM_DIALOG            someCr as Player REASON_FROM_SCRIPT REASON_RUN_AWAY

```angelscript
bool npc_plane_begin(Critter& npc, NpcPlane& plane, int reason, Critter@ someCr, Item@ someItem)
```

### UseSkillOn

```angelscript
bool UseSkillOn(Critter& npc, uint crId, NpcPlane& plane)
```

### RamIntoCritter

* * Critter tries to forcefuly ram into another critter if it's standing next to it. * It can cause KD and damage but doesn't trigger combat. * The outcome depends on statistics of both critters and a bit of luck. 

```angelscript
void RamIntoCritter(Critter& npc, uint targetId, bool returnHome)
```

### FireInTheHole

* * Sends alert about an armed explosive. * All NPCs near the explosive will try to run to a safe distance and wait there until the bomb explodes. * * @param caller        The critter who warned others about the explosive. * @param armedBomb     The item which is about to explode. * @param dangerDist    Distance from the bomb which is considered dangerous by NPCs. 

```angelscript
void FireInTheHole(Critter& caller, Item& armedBomb, uint16 dangerDist)
```

### LootCritter

```angelscript
bool LootCritter(Critter& npc, uint crId, bool lootEx, uint16 hexX, uint16 hexY)
```

### PlaneEndSuccess

```angelscript
bool PlaneEndSuccess(Critter& npc, NpcPlane& plane)
```

### PlaneEndPositionIssue

```angelscript
bool PlaneEndPositionIssue(Critter& npc, NpcPlane& plane)
```

### PlaneEndGagCritter

```angelscript
bool PlaneEndGagCritter(Critter& npc, Critter@ someCr, NpcPlane& plane)
```

### PlaneEndGagItem

```angelscript
bool PlaneEndGagItem(Critter& npc, Item@ someItem, NpcPlane& plane)
```

### PlaneEndRunAway

```angelscript
bool PlaneEndRunAway(Critter& npc, NpcPlane& plane)
```

### PlaneEndNoArmed

```angelscript
bool PlaneEndNoArmed(Critter& npc, NpcPlane& plane)
```

### npc_plane_end

///////////////////////////////////////////////////////////////////////////////////////////////// Called on some plane added. Return true to erase plane, false to wait (set this plane to next priority of planes sequence). REASON_SUCCESS REASON_HEX_TOO_FAR REASON_HEX_BUSY REASON_HEX_BUSY_RING REASON_DEADLOCK REASON_TRACE_FAIL REASON_POSITION_NOT_FOUND REASON_FIND_PATH_ERROR REASON_CANT_WALK REASON_TARGET_DISAPPEARED     someCr as Enemy REASON_USE_ITEM_NOT_FOUND REASON_GAG_CRITTER            someCr as Enemy REASON_GAG_ITEM               someItem as Item REASON_NO_UNARMED

```angelscript
bool npc_plane_end(Critter& npc, NpcPlane& plane, int reason, Critter@ someCr, Item@ someItem)
```

### npc_plane_run

```angelscript
bool npc_plane_run(Critter& npc, NpcPlane& plane, int reason, uint& r0, uint& r1, uint& r2)
```

### CogitateFiring

TODO more general version, this will cover all our weapons though

```angelscript
bool CogitateFiring(Critter& cr, uint& mode, uint& aim)
```

### ChooseAim

```angelscript
int ChooseAim(Critter& cr, Critter& target, ProtoItem@ weapon, uint8 mode, ProtoItem@ ammo)
```

### TraceFirstCritter

```angelscript
Critter@ TraceFirstCritter(uint16 hx, uint16 hy, uint16 tx, uint16 ty, Map& map, int dist, uint16 gx, uint16 gy, uint mindist)
```

### ValidateBurst

```angelscript
bool ValidateBurst(Critter& cr, Critter& target, ProtoItem@ weapon, uint mode)
```

### SkillsSort

```angelscript
void SkillsSort(Critter& npc, array<int>& skills, uint first, uint count)
```

### SkillToBegin

```angelscript
void SkillToBegin(array<int>& skills, int skill)
```

### CheckBattleWeapon

```angelscript
bool CheckBattleWeapon(Critter& npc, Item& weapon)
```

### IsAmmoForWeapon

```angelscript
bool IsAmmoForWeapon(Critter& npc, Item& weapon)
```

### WillFight

```angelscript
bool WillFight(Critter@ cr)
```


