---
title: quest_caesar_train.fos
description: " FOnline: 2238 Rotators  quest_caesar_train.fos ..."
---

# quest_caesar_train.fos


FOnline: 2238
Rotators

quest_caesar_train.fos


## Includes

- `_colors.fos`
- `_maps.fos`
- `_vars.fos`
- `_macros.fos`
- `mapdata_h.fos`
- `messages_h.fos`
- `npc_roles_h.fos`
- `npc_common_h.fos`
- `utils_h.fos`
- `npc_planes_h.fos`
- `logging_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| FATHER_KILLED | `(4)` |  |
| FATHER_INFO | `(5)` |  |
| FATHER_KILLED_INFO | `(6)` |  |
| CHILD_ATTACK | `(8)` | #define ALL_FLEE			(7) // Father could flee |
| CHILD_KILLED | `(9)` |  |
| DIALOG_ID | `(10263)` |  |
| STR_ATTACK_TAUNT | `(1)` |  |
| SHOWCRITTER1_DIST | `(2)` |  |

## Functions

### r_SpawnCamp

```angelscript
void r_SpawnCamp(Critter& player, Critter@ npc)
```

### r_DeleteCamp

```angelscript
void r_DeleteCamp(Critter& player, Critter@ npc)
```

### GetOwner

```angelscript
Critter@ GetOwner(Map& map)
```

### _Father

The father, main person

```angelscript
void _Father(Critter& cr, bool firstTime)
```

### _FatherDead

```angelscript
void _FatherDead(Critter& cr, Critter@ killer)
```

### _Child

The child, second person

```angelscript
void _Child(Critter& cr, bool firstTime)
```

### _ChildDead

```angelscript
void _ChildDead(Critter& cr, Critter@ killer)
```

### _Ambusher

The gangers in the ambush location. The leader of the gangers (ROLE_AMBUSH_LEADER) should start a dialogue with the player on map load. This would be the best.

```angelscript
void _Ambusher(Critter& ganger, bool firstTime)
```

### t_Ambush

This is important stuff for the later part of the quest. Player tries to run away from ambush, has to cross the trigger. But obacht, trigger is deactivated, if "LVAR_q_la_train_caesar_ambush == 3"

```angelscript
void t_Ambush(Critter& critter, Scenery& trigger, bool entered, uint8 dir)
```

### _AmbusherOnMessage

```angelscript
void _AmbusherOnMessage(Critter& npc, Critter& player, int num, int val)
```

### _AmbusherAttacked

```angelscript
bool _AmbusherAttacked(Critter& cr, Critter& attacker)
```

### _AmbusherOnShowCritter1

```angelscript
void _AmbusherOnShowCritter1(Critter& cr, Critter& target)
```

### _AmbusherOnHideCritter1

```angelscript
void _AmbusherOnHideCritter1(Critter& cr, Critter& target)
```

### CheckOwner

```angelscript
void CheckOwner(Critter& cr, int p0, int p1, int p2)
```

### e_CheckDistance

```angelscript
uint e_CheckDistance(array<uint>@ values)
```


