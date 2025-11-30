---
title: mapper_generators.fos
description: " FOnline: 2238 Rotators  mapper_generators.fos ..."
---

# mapper_generators.fos


FOnline: 2238
Rotators

mapper_generators.fos


## Includes

- `_mapper_macros.fos`
- `_defines.fos`
- `ITEMPID.H`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| SX | `(267)` | mapper only |
| SY | `(262)` |  |
| PID_SHOOTABLE | `PID_BLOCK_BARREL1` |  |
| PID_WALL | `PID_BLOCK_BARREL2` |  |
| TILE_WALL | `(0x00010000)` |  |
| TILE_UNINIT | `(-1)` |  |
| TILE_DELETED | `(-1)` |  |
| TILE_SHOOTABLE | `(0x00010002)` |  |
| EDGE_EXISTS | `(0)` |  |
| EDGE_WALK | `(1)` |  |
| EDGE_SHOOT | `(2)` |  |
| B_LEFT | `(0x1)` |  |
| B_TOP | `(0x2)` |  |
| B_BOTTOM | `(0x4)` |  |
| B_FLAG_SMALL | `(0xF0)` |  |
| WALL_V | `(B_TOP | B_BOTTOM)` |  |
| WALL_H | `(B_LEFT | B_TOP)` |  |
| WALL_CORNER1 | `(B_LEFT | B_TOP | B_BOTTOM)` |  |
| WALL_CORNER2 | `(B_LEFT | B_TOP)` |  |
| WALL_CORNER3 | `(B_TOP)` |  |
| WALL_CORNER4 | `(B_BOTTOM)` |  |
| WALL_T1 | `(B_LEFT | B_TOP)` |  |
| WALL_T2 | `(B_TOP | B_BOTTOM)` |  |
| WALL_T3 | `(B_LEFT | B_TOP | B_BOTTOM)` |  |
| WALL_T4 | `(B_LEFT | B_TOP | B_BOTTOM)` |  |
| WALL_CROSS | `(B_LEFT | B_TOP | B_BOTTOM)` |  |
| TAB1 | `# (_x, _y)tab1[(_y) * MaxX + (_x)]` |  |
| TAB2 | `# (_x, _y)tab2[(_y) * MaxX + (_x)]` |  |

## Classes

### Node

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| next | `[Node](mapper_generators.fos.md)@` |  |  |
| x | `uint` |  |  |
| y | `uint` |  |  |

### Queue

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| head | `[Node](mapper_generators.fos.md)@` |  |  |
| tail | `[Node](mapper_generators.fos.md)@` |  |  |

**Methods**

#### Push
```angelscript
void Push(uint x, uint y)
```

#### Empty
```angelscript
bool Empty()
```

#### Top
```angelscript
void Top(uint& x, uint& y)
```

#### Pop
```angelscript
void Pop(uint& x, uint& y)
```

#### Pop
```angelscript
void Pop()
```

### Room

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| X1 | `uint` |  |  |
| Y1 | `uint` |  |  |
| X2 | `uint` |  |  |
| Y2 | `uint` |  |  |
| Num | `uint` |  |  |
| Neighbours | `array<uint>` |  |  |

**Methods**

#### RX
```angelscript
uint RX() { return (X1 + X2) / 2; }
```

#### RY
```angelscript
uint RY() { return (Y1 + Y2) / 2; }
```

### Edge

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| Type | `uint` |  |  |
| From | `uint` |  |  |
| To | `uint` |  |  |
| Xs | `array<uint>` |  |  |
| Ys | `array<uint>` |  |  |

### GeneratorContext

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| MaxX | `uint` |  |  |
| MaxY | `uint` |  |  |
| RoomsCount | `uint` |  |  |

**Methods**

#### LineH
```angelscript
void LineH(uint x, uint y, uint len)
```

#### LineV
```angelscript
void LineV(uint x, uint y, uint len)
```

#### SubDivide
```angelscript
void SubDivide(uint x1, uint y1, uint x2, uint y2)
```

#### MakeRoom
```angelscript
void MakeRoom(uint x1, uint y1, uint x2, uint y2)
```

#### FindEdges
```angelscript
void FindEdges()
```

#### BuildTree
```angelscript
void BuildTree()
```

#### MakeShootableEdges
```angelscript
void MakeShootableEdges()
```

#### rollNoShootEdge
```angelscript
bool rollNoShootEdge()
```

#### ProcessWalls
```angelscript
void ProcessWalls()
```

#### Generate
```angelscript
void Generate()
```

#### Cleanup
```angelscript
void Cleanup()
```

#### Recognize
```angelscript
void Recognize()
```

#### Spawn
```angelscript
void Spawn(MapperMap@ map, uint16 hx, uint16 hy)
```

#### Render
```angelscript
void Render()
```


## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| ctx | `[GeneratorContext](mapper_generators.fos.md)@` | `null` |  |

## Functions

### test_generators

```angelscript
void test_generators()
```

### RenderGen

```angelscript
void RenderGen()
```


