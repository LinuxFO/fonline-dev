---
title: triggers_funcs.fos
description: " FOnline: 2238 Rotators  triggers_funcs.fos ..."
---

# triggers_funcs.fos


FOnline: 2238
Rotators

triggers_funcs.fos


## Includes

- `messages_h.fos`
- `npc_common_h.fos`
- `npc_planes_h.fos`

## Included By

- [triggers.fos](triggers.fos.md)

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __TRIGGERS_FUNCS__ |  |  |

## Functions

### Default

```angelscript
bool Default(Item& tr, Critter@ cr, uint dir, uint count, array<uint>@ values)
```

### _AntiBlock

```angelscript
void _AntiBlock(Item& tr, bool firstTime)
```

### AntiBlock

```angelscript
bool AntiBlock(Item& tr, Critter@ cr, uint dir, uint count, array<uint>@ values)
```

### _Aggravate

****************************************************************************** * 2: Aggravate ****************************************************************************** Makes critters attack player, useful to wake up mobs in quest maps Val2: ST_TEAM_ID of NPCs to aggravate

```angelscript
void _Aggravate(Item& tr, bool firstTime)
```

### Aggravate

```angelscript
bool Aggravate(Item& tr, Critter@ cr, uint dir, uint count, array<uint>@ values)
```

### _Teleport

****************************************************************************** * 3: Teleports critter to another hex ****************************************************************************** Makes critters attack player, useful to wake up mobs in quest maps Val2: HexX, Val3: HexY, Val4: Dir

```angelscript
void _Teleport(Item& tr, bool firstTime)
```

### Teleport

```angelscript
bool Teleport(Item& tr, Critter@ cr, uint dir, uint count, array<uint>@ values)
```

### teleport

```angelscript
void teleport(Critter& cr, int x, int y, int dir)
```


