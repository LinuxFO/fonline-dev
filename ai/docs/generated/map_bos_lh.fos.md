---
title: map_bos_lh.fos
description: " FOnline: 2238 Rotators  map_bos_lh.fos ..."
---

# map_bos_lh.fos


FOnline: 2238
Rotators

map_bos_lh.fos


## Includes

- `_defines.fos`
- `_macros.fos`
- `_maps.fos`
- `elevators_h.fos`
- `factions_h.fos`
- `groups_h.fos`
- `mapdata_h.fos`
- `messages_h.fos`
- `MSGSTR.h`
- `npc_common_h.fos`
- `npc_roles_h.fos`

## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| ElevatorsAdded | `bool` | `false` |  |

## Functions

### map_init

```angelscript
void map_init(Map& map, bool firstTime)
```

### Debug

```angelscript
void Debug(Critter& player, int p0, int p1, int p2)
```

### t_Elevator

 Elevator triggers 

```angelscript
void t_Elevator(Critter& critter, Scenery& trigger, bool entered, uint8 dir)
```

### t_ElevatorOutside

```angelscript
void t_ElevatorOutside(Critter& critter, Scenery& trigger, bool entered, uint8 dir)
```

### t_NearHq

near hq building entrance

```angelscript
void t_NearHq(Critter& critter, Scenery& trigger, bool entered, uint8 dir)
```

### t_LastWarning

near hq building entrance

```angelscript
void t_LastWarning(Critter& critter, Scenery& trigger, bool entered, uint8 dir)
```

### t_EnterHq

at hq building entrance

```angelscript
void t_EnterHq(Critter& critter, Scenery& trigger, bool entered, uint8 dir)
```

### t_NearStorage

```angelscript
void t_NearStorage(Critter& critter, Scenery& trigger, bool entered, uint8 dir)
```

### t_StorageEnter

```angelscript
void t_StorageEnter(Critter& critter, Scenery& trigger, bool entered, uint8 dir)
```

### t_NearComputer

```angelscript
void t_NearComputer(Critter& critter, Scenery& trigger, bool entered, uint8 dir)
```

### t_EnterComputer

```angelscript
void t_EnterComputer(Critter& critter, Scenery& trigger, bool entered, uint8 dir)
```

### _OutpostDoor

```angelscript
void _OutpostDoor(Item& item, bool firstTime)
```

### OutpostIssueWarning

```angelscript
void OutpostIssueWarning(Item& item)
```

### OutpostAttack

```angelscript
void OutpostAttack(Item& item, Critter& crit)
```

### _OutpostDoorUseOnMe

```angelscript
bool _OutpostDoorUseOnMe(Item& item, Critter& crit, Item@ usedItem)
```

### _OutpostDoorSkill

```angelscript
bool _OutpostDoorSkill(Item& item, Critter& cr, int skill)
```


