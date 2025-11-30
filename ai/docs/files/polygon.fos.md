---
title: polygon.fos
description: " FOnline: 2238 Rotators  polygon.fos ..."
---

# polygon.fos


FOnline: 2238
Rotators

polygon.fos


## Includes

- `_defines.fos`
- `_macros.fos`
- `polygon_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __POLYGON_MODULE__ |  |  |

## Classes

### CTriPoly

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| count | `uint` |  |  |
| head | `[CVertex](polygon.fos.md)@` |  |  |
| tail | `[CVertex](polygon.fos.md)@` |  |  |

**Methods**

#### AddVertex
```angelscript
CTriPoly@ AddVertex(float x, float y)
```

### CVertex

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| x | `float` |  |  |
| y | `float` |  |  |
| num | `uint` |  |  |
| next | `[CVertex](polygon.fos.md)@` |  |  |
| prev | `[CVertex](polygon.fos.md)@` |  |  |

### CPolygon

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| xs | `array<float>` |  |  |
| ys | `array<float>` |  |  |
| hxs | `array<uint16>` |  |  |
| hys | `array<uint16>` |  |  |

**Methods**

#### AddVertex
```angelscript
IPolygon@ AddVertex(uint16 x, uint16 y)
```

#### AddVertices
```angelscript
IPolygon@ AddVertices(array<uint16>& hexes)
```

#### GetTriangulation
```angelscript
void GetTriangulation(array<uint16>& triangles)
```

#### Intersects
```angelscript
bool Intersects(float x, float y, float x1, float y1, float x2, float y2)
```

#### IsWithin
```angelscript
bool IsWithin(uint16 x, uint16 y)
```

#### IsWithin
```angelscript
bool IsWithin(Critter& cr)
```

#### IsWithin
```angelscript
bool IsWithin(Item& item)
```


## Functions

### ClipEar

```angelscript
void ClipEar(CTriPoly& poly, array<uint>& vertlist)
```

### FindEar

```angelscript
CVertex@ FindEar(CVertex@ vertex, bool& zero)
```

### DetNonnegative

```angelscript
bool DetNonnegative(float x1, float y1, float x2, float y2)
```

### Determinant

```angelscript
float Determinant(float x1, float y1, float x2, float y2)
```

### GetDrawHexAreaData

```angelscript
void GetDrawHexAreaData(array<uint16>& area, bool triangles, int color, array<int>& data)
```

### DrawHexArea

```angelscript
void DrawHexArea(array<uint16>& area, bool triangles, int color)
```

### NewPolygon

```angelscript
IPolygon@ NewPolygon()
```

### LoadShapeFromEntires

```angelscript
IPolygon@ LoadShapeFromEntires(Map& map, uint first, uint last)
```


