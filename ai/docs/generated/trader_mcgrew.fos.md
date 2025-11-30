---
title: trader_mcgrew.fos
description: " FOnline: 2238 Rotators  trader_mcgrew.fos ..."
---

# trader_mcgrew.fos


FOnline: 2238
Rotators

trader_mcgrew.fos


## Includes

- `_macros.fos`
- `trader_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| DETONATOR_STOCK | `(npc.StatBase[ST_VAR1])` |  |

## Functions

### critter_init

```angelscript
void critter_init(Critter& npc, bool firstTime)
```

### r_ReduceStock

```angelscript
void r_ReduceStock(Critter& player, Critter@ npc)
```

### d_HasStock

```angelscript
bool d_HasStock(Critter& player, Critter@ npc)
```

### d_HasNotStock

```angelscript
bool d_HasNotStock(Critter& player, Critter@ npc)
```

### e_Restock

```angelscript
uint e_Restock(array<uint>@ values)
```


