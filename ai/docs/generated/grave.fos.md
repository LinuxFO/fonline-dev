---
title: grave.fos
description: " FOnline: 2238 Rotators  grave.fos ..."
---

# grave.fos


FOnline: 2238
Rotators

grave.fos


## Includes

- `_ai.fos`
- `_macros.fos`
- `multihex_h.fos`
- `npc_planes_h.fos`
- `recycler_h.fos`
- `reputations_h.fos`
- `utils_h.fos`
- `world_common_h.fos`

## Functions

### GraveRandomPic

```angelscript
void GraveRandomPic(Item@ grave)
```

### GraveOpen

Digging up a grave 

```angelscript
void GraveOpen(Item@ grave, Critter@ cr, Item@ shovel)
```

### GraveClose

Covering a grave 

```angelscript
void GraveClose(Item@ grave, Critter@ cr, Item@ shovel)
```

### _Init

```angelscript
void _Init(Item& grave, bool firstTime)
```

### _Finish

```angelscript
void _Finish(Item& item, bool deleted)
```

### e_Init

```angelscript
uint e_Init(array<uint>@ values)
```

### _UseSkill

Accesssing the grave 

```angelscript
bool _UseSkill(Item& grave, Critter& cr, int skill)
```

### _UseItem

Using shovel on the grave 

```angelscript
bool _UseItem(Item& grave, Critter& cr, Item@ usedItem)
```


