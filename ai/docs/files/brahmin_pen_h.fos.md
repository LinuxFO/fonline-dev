---
title: brahmin_pen_h.fos
description: " FOnline: 2238 Rotators  brahmin_pen_h.fos ..."
---

# brahmin_pen_h.fos


FOnline: 2238
Rotators

brahmin_pen_h.fos


## Includes

- `_macros.fos`
- `_scripts.fos`
- `utils_h.fos`
- `entire.fos`
- `debug_h.fos`
- `serializator.fos`
- `reputations_h.fos`

## Included By

- [brahmin_pen.fos](brahmin_pen.fos.md)
- [brahmin_pens.fos](brahmin_pens.fos.md)
- [brahmin_trader.fos](brahmin_trader.fos.md)

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __BRAHMIN_PEN_H__ |  |  |

## Classes

### CBrahminPen

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| map | `Map@` |  |  |
| serializer | `[Serializator](serializator.fos.md)` |  |  |
| entires | `array<[Entire](entire.fos.md)>` |  |  |
| id | `uint` |  |  |
| amount | `uint` |  |  |
| max | `uint` |  |  |
| teamid | `uint` |  |  |
| initialized | `bool` |  |  |
| name | `string` |  |  |
| owner | `Critter@` |  |  |

**Methods**

#### LoadData
```angelscript
bool LoadData()
```

#### SaveData
```angelscript
bool SaveData()
```

#### RemoveBrahmin
```angelscript
bool RemoveBrahmin()
```

#### AddBrahmin
```angelscript
bool AddBrahmin()
```


