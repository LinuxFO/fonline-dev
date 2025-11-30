---
title: elevators_h.fos
description: " FOnline: 2238 Rotators  elevators_h.fos ..."
---

# elevators_h.fos


FOnline: 2238
Rotators

elevators_h.fos


## Includes

- `_macros.fos`
- `entire.fos`
- `utils_h.fos`

## Included By

- [elevators.fos](elevators.fos.md)
- [map_bos_lh.fos](map_bos_lh.fos.md)
- [map_redding.fos](map_redding.fos.md)
- [map_redding_mine.fos](map_redding_mine.fos.md)

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __ELEVATOR__ |  |  |

## Classes

### CFloor

 Describes elevator entrance/floor 

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| MapId | `uint` |  |  |
| EntireNum | `uint8` |  |  |
| HexX | `uint16` |  |  |
| HexY | `uint16` |  |  |

### CElevator

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| floors | `array<[CFloor](elevators_h.fos.md)>` |  |  |
| players | `array<uint>` |  | players (their ids) that are inside the elevator usually one per floor |
| type | `uint` |  | type of the elevator (descriptor number) |
| onmove | `IElevatorOnMove@` |  |  |

**Methods**

#### get_Type
```angelscript
uint get_Type() { return type; }
```

#### GetDescriptor
 Creates elevator with first floor diff than 0  CElevator(uint id, uint base) { this.id = id; this.base = base; }  Creates elevator with custom floor numbers  CElevator(uint id, uint[]& levels) { this.id = id; this.base = 0; this.levels = levels; }  Gets descriptor used in elevator gui window 

```angelscript
uint GetDescriptor(Critter& cr)
```

#### Floors
 Number of floors 

```angelscript
uint Floors()
```

#### GetCurrentLevel
 Returns floor number with regard to base  uint GetLevel(uint level) { if(levels.length() == 0) return base + level; else return levels[level]; }  Gets current level for player 

```angelscript
uint GetCurrentLevel(Critter& player)
```

#### IsInside
 Checks if player is inside the elevator 

```angelscript
bool IsInside(Critter& player)
```

#### AddPlayer
 Put player inside the elevator 

```angelscript
void AddPlayer(Critter& player)
```

#### RemovePlayer
 Takes player out from elevator 

```angelscript
void RemovePlayer(Critter@ player)
```

#### Transit
 Transits player to the given floor 

```angelscript
void Transit(Critter& player, uint floor)
```

#### PlaySound
```angelscript
void PlaySound(Critter& player, int floornum)
```

#### AddFloor
 Adds floor entrance to elevator 

```angelscript
IElevator@ AddFloor(uint mapId, uint8 entireNum)
```

#### Debug
```angelscript
void Debug(Critter& player)
```

#### SetOnMove
Sets OnMove callback (returning false disallow moving, changing of target floor is possible) 

```angelscript
void SetOnMove(IElevatorOnMove@ callback)
```

### CPidElevator

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| floors | `array<[CPidFloor](elevators_h.fos.md)>` |  |  |
| players | `array<uint>` |  | players (their ids) that are inside the elevator usually one per floor |
| type | `uint` |  | type of the elevator (descriptor number) |
| onmove | `IElevatorOnMove@` |  |  |

**Methods**

#### get_Type
```angelscript
uint get_Type() { return type; }
```

#### GetDescriptor
 Gets descriptor used in elevator gui window 

```angelscript
uint GetDescriptor(Critter& cr)
```

#### Floors
 Number of floors 

```angelscript
uint Floors()
```

#### GetCurrentLevel
 Gets current level for player 

```angelscript
uint GetCurrentLevel(Critter& player)
```

#### IsInside
 Checks if player is inside the elevator 

```angelscript
bool IsInside(Critter& player)
```

#### AddPlayer
 Put player inside the elevator 

```angelscript
void AddPlayer(Critter& player)
```

#### RemovePlayer
 Takes player out from elevator 

```angelscript
void RemovePlayer(Critter@ player)
```

#### Transit
 Transits player to the given floor 

```angelscript
void Transit(Critter& player, uint floor)
```

#### PlaySound
```angelscript
void PlaySound(Critter& player, int floornum)
```

#### AddFloor
 Adds floor entrance to elevator 

```angelscript
IElevator@ AddFloor(uint mapId, uint8 entireNum)
```

#### Debug
```angelscript
void Debug(Critter& player)
```

#### SetOnMove
Sets OnMove callback (returning false disallow moving, changing of target floor is possible) 

```angelscript
void SetOnMove(IElevatorOnMove@ callback)
```

### CPidFloor

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| MapPid | `uint` |  |  |
| EntireNum | `uint8` |  |  |
| HexX | `uint16` |  |  |
| HexY | `uint16` |  |  |


