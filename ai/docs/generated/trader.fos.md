---
title: trader.fos
description: " FOnline: 2238 Rotators  trader.fos ..."
---

# trader.fos


FOnline: 2238
Rotators

trader.fos


## Includes

- `_macros.fos`
- `economy_h.fos`
- `trader_h.fos`
- `utils_h.fos`

## Functions

### _OnBarter

Send relevant prices to client

```angelscript
bool _OnBarter(Critter& cr, Critter& player, bool attach, uint barterCount)
```

### e_Update

* * Updates trader inventory. 

```angelscript
uint e_Update(array<uint>@ values)
```

### _DenFlick

```angelscript
void _DenFlick(Critter& npc, bool firstTime)
```


