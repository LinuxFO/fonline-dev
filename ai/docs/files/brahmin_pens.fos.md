---
title: brahmin_pens.fos
description: " FOnline: 2238 Rotators  brahmin_pens.fos ..."
---

# brahmin_pens.fos


FOnline: 2238
Rotators

brahmin_pens.fos


## Includes

- `_macros.fos`
- `_maps.fos`
- `_entires.fos`
- `groups_h.fos`
- `brahmin_pen_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __BRAHMIN_PENS__ |  |  |
| __BRAHMIN_PEN_MODULE__ |  |  |
| ADD_PEN | `# (name, map, entire, properties) CBrahminPen name(map, entire); name.properties; AddBrahminPen(name)` |  |

## Functions

### GetBrahminPen

```angelscript
IBrahminPen@ GetBrahminPen(uint id)
```

### AddBrahminPen

```angelscript
void AddBrahminPen(CBrahminPen& pen)
```

### SaveBrahminPenData

```angelscript
void SaveBrahminPenData()
```

### InitBrahminPens

```angelscript
void InitBrahminPens()
```


