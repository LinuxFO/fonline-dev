---
title: encounter_guard.fos
description: " FOnline: 2238 Rotators  encounter_guard.fos ..."
---

# encounter_guard.fos


FOnline: 2238
Rotators

encounter_guard.fos


## Includes

- `_basetypes.fos`
- `_macros.fos`
- `groups_h.fos`
- `item_dogtags_h.fos`
- `npc_planes_h.fos`
- `utils_h.fos`
- `npc_common_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| SHOWCRITTER1_ENCGUARD | `(1)` |  |
| SHOWCRITTER1_VIGILANT | `(4)` |  |
| _CanHelp | `# (npc, who)(_GroupMode(npc) == FACTION_MODE_NPC_ONLY ? _IsTrueNpc(who) : (_GroupMode(npc) == FACTION_MODE_PLAYER_ONLY ? !_IsTrueNpc(who) : true))` |  |

## Functions

### critter_init

```angelscript
void critter_init(Critter& cr, bool firstTime)
```

### _Vigilant

```angelscript
void _Vigilant(Critter& cr, bool firstTime)
```

### _OnShowCritterEncounter

```angelscript
void _OnShowCritterEncounter(Critter& cr, Critter& target)
```

### _OnShowCritter1Encounter

```angelscript
void _OnShowCritter1Encounter(Critter& cr, Critter& target)
```

### _OnShowCritter2Encounter

```angelscript
void _OnShowCritter2Encounter(Critter& cr, Critter& target)
```

### e_PushAway

```angelscript
uint e_PushAway(array<uint>@ values)
```

### _OnHideCritter1Encounter

```angelscript
void _OnHideCritter1Encounter(Critter& cr, Critter& target)
```

### _OnIdleEncounter

```angelscript
void _OnIdleEncounter(Critter& cr)
```

### _OnSmthMoveItemEncounter

```angelscript
void _OnSmthMoveItemEncounter(Critter& crit, Critter& fromCrit, Item& item, uint8 fromSlot)
```

### _NpcSmthUseSkill

taken from encounter_npc

```angelscript
void _NpcSmthUseSkill(Critter& npc, Critter& fromCr, int skill, Critter@ onCritter, Item@ onItem, Scenery@ onScenery)
```

### _OnSmthDropItemEncounter

```angelscript
void _OnSmthDropItemEncounter(Critter& npc, Critter& fromCr, Item& item)
```

### _NpcPlaneStart

uint ida=0;

```angelscript
int _NpcPlaneStart(Critter& npc, NpcPlane& plane, int reason, Critter@ someCr, Item@ someItem)
```

### _NpcPlaneFinish

```angelscript
int _NpcPlaneFinish(Critter& npc, NpcPlane& plane, int reason, Critter@ someCr, Item@ someItem)
```

### _NpcMoveItem

```angelscript
void _NpcMoveItem(Critter& npc, Item& item, uint8 fromSlot)
```

### e_CheckDistance

///////// events

```angelscript
uint e_CheckDistance(array<uint>@ values)
```

### e_CheckDistance2

```angelscript
uint e_CheckDistance2(array<uint>@ values)
```

### e_CheckWeapon

```angelscript
uint e_CheckWeapon(array<uint>@ values)
```

### e_DelayedSayBehave

TODO: Warnings for non-humanoid critter like dogs

```angelscript
uint e_DelayedSayBehave(array<uint>@ values)
```

### e_DelayedAttackPlane

```angelscript
uint e_DelayedAttackPlane(array<uint>@ values)
```


