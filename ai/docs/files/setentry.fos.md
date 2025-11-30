---
title: setentry.fos
description: " FOnline: 2238 Rotators  setentry.fos ..."
---

# setentry.fos


FOnline: 2238
Rotators

setentry.fos


## Included By

- [mapper_autowall.fos](mapper_autowall.fos.md)

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| ROLE_NONE | `(0)` | inlined |
| ROLE_WALL_NW | `(1)` |  |
| ROLE_WALL_SE | `(2)` |  |
| ROLE_WALL_NE | `(3)` |  |
| ROLE_WALL_SW | `(4)` |  |
| ROLE_CORNER_W | `(5)` |  |
| ROLE_CORNER_N | `(6)` |  |
| ROLE_CORNER_E | `(7)` |  |
| ROLE_CORNER_S | `(8)` |  |
| ROLE_JUNCTION_NW | `(9)` |  |
| ROLE_JUNCTION_NE | `(10)` |  |
| ROLE_JUNCTION_SW | `(11)` |  |
| ROLE_JUNCTION_SE | `(12)` |  |
| ROLE_CROSS | `(13)` |  |
| ROLE_TILE | `(14)` |  |
| ROLE_ROOF | `(15)` |  |

## Classes

### CSetEntry

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| isGroup | `bool` |  |  |
| role | `uint8` |  |  |
| ent1 | `uint` |  |  |
| ent2 | `uint` |  |  |
| entries | `array<uint>` |  |  |
| horizincident | `array<uint>` |  |  |
| vertincident | `array<uint>` |  |  |

**Methods**

#### AddIncident
```angelscript
void AddIncident(uint id, bool verti)
```

#### AddIncidents
```angelscript
void AddIncidents(array<uint>& ids, bool verti)
```

### CWallSet

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| id | `uint` |  |  |
| name | `string` |  |  |
| walls_nw | `array<uint>` |  |  |
| walls_se | `array<uint>` |  |  |
| walls_ne | `array<uint>` |  |  |
| walls_sw | `array<uint>` |  |  |
| wall_blank_nw | `array<uint>` |  |  |
| wall_blank_se | `array<uint>` |  |  |
| wall_blank_ne | `array<uint>` |  |  |
| wall_blank_sw | `array<uint>` |  |  |
| corners_n | `array<uint>` |  |  |
| corners_e | `array<uint>` |  |  |
| corners_w | `array<uint>` |  |  |
| corners_s | `array<uint>` |  |  |
| junctions_nw | `array<uint>` |  |  |
| junctions_ne | `array<uint>` |  |  |
| junctions_sw | `array<uint>` |  |  |
| junctions_se | `array<uint>` |  |  |
| crosses | `array<uint>` |  |  |
| tilegroups | `array<uint>` |  |  |
| roofgroups | `array<uint>` |  |  |


