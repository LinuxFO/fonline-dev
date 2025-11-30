---
title: antiblock.fos
description: " FOnline: 2238 Rotators  antiblock.fos ..."
---

# antiblock.fos


FOnline: 2238
Rotators

antiblock.fos


## Includes

- `_basetypes.fos`
- `_macros.fos`
- `follower_common_h.fos`
- `messages_h.fos`
- `npc_common_h.fos`
- `npc_planes_h.fos`
- `world_common_h.fos`

## Functions

### item_init

 Item 

```angelscript
void item_init(Item& item, bool firstTime)
```

### _Walk

```angelscript
void _Walk(Item& item, Critter& crit, bool entered, uint8 dir)
```

### t_Enter

 Trigger 

```angelscript
void t_Enter(Critter& crit, Scenery& trigger, bool entered, uint8 dir)
```

### StartDetection

 Logic behind it 

```angelscript
void StartDetection(Critter& cr)
```

### e_Check

```angelscript
uint e_Check(array<uint>@ values)
```


