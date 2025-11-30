---
title: lockers.fos
description: " FOnline: 2238 Rotators  lockers.fos ..."
---

# lockers.fos


FOnline: 2238
Rotators

lockers.fos


## Includes

- `_macros.fos`
- `MsgStr.h`
- `multihex_h.fos`
- `utils_h.fos`

## Included By

- [spawner_nc.fos](spawner_nc.fos.md)
- [spawner_ntown.fos](spawner_ntown.fos.md)
- [spawner_town.fos](spawner_town.fos.md)

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| LOCKER_SOUND_RADIUS | `(15)` |  |

## Functions

### UseItemOnLocker

```angelscript
bool UseItemOnLocker(Critter& cr, Item& locker, Item& item)
```

### UseSkillOnLocker

```angelscript
bool UseSkillOnLocker(Critter& cr, Item& locker, int skill)
```

### HandleLocker

```angelscript
bool HandleLocker(Critter& cr, Map@ map, Item& locker, bool disregardKey)
```

### IsKeyAviable

```angelscript
bool IsKeyAviable(Critter& cr, uint lockerId)
```

### GetKeyId

```angelscript
uint GetKeyId(Critter& cr, uint lockerId)
```

### SwitchState

```angelscript
void SwitchState(Item& locker)
```

### IsAutoDoor

 Checks whether door with given pid should be closed automatically  TODO: fill this list with others

```angelscript
bool IsAutoDoor(Item& door)
```

### IsOpenableContainer

 Checks if item is container with doors 

```angelscript
bool IsOpenableContainer(uint pid)
```

### DoorIsBlocked

Returns true if the door is blocked by something (typically a critter) 

```angelscript
bool DoorIsBlocked(Item@ door)
```

### OnOpenAutoDoor

 Spawns event that will close door 

```angelscript
void OnOpenAutoDoor(Item@ targetItem, bool not_auto_door)
```

### OnOpenDoor

 Spawns event that will close normal door (long time) 

```angelscript
void OnOpenDoor(Item@ targetItem, bool not_auto_door)
```

### OnClose

 Removes event 

```angelscript
void OnClose(Item@ targetItem)
```

### OnOpenContainer

```angelscript
void OnOpenContainer(Item@ targetItem)
```

### e_CloseDoor

 Event handler that closes automatic doors 

```angelscript
uint e_CloseDoor(array<uint>@ values)
```

### LockerClose

```angelscript
bool LockerClose(Item& item)
```

### LockerOpen

```angelscript
bool LockerOpen(Item& item)
```

### LockerBudge

```angelscript
void LockerBudge(Item& item)
```


