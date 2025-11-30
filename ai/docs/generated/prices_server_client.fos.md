---
title: prices_server_client.fos
description: " FOnline: 2238 Rotators  prices_server_client.fos ..."
---

# prices_server_client.fos


FOnline: 2238
Rotators

prices_server_client.fos


## Included By

- [client_main.fos](client_main.fos.md)
- [economy.fos](economy.fos.md)

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| _DefineThreshold | `# (_type, _level1, _level2)LevelThreshold1[(_type)] = GetProtoItem(_level1).Cost; LevelThreshold2[(_type)] = GetProtoItem(_level2).Cost` | everything strictly cheaper than _level1 value will be level one everything strictly cheaper than _level2 value and worth at least _level1 will be level two everything else will be level three |
| _NoThresholds | `# (_type) LevelThreshold1[(_type)] = 10000000` |  |

## Functions

### GetBasePrice

Fetches base price from item_prices_base array

```angelscript
uint GetBasePrice(uint pid)
```

### GetTraderMod

```angelscript
uint GetTraderMod(Critter& trader, Item& item)
```

### GetTraderMod

```angelscript
uint GetTraderMod(Critter& trader, uint16 pid)
```

### GetItemCost

```angelscript
uint GetItemCost(Item& item, Critter& cr, Critter& trader, bool sell)
```

### GetItemCostPlain

```angelscript
uint GetItemCostPlain(Item& item, Critter& cr, Critter& trader)
```

### SendLevelThresholds

```angelscript
void SendLevelThresholds(Critter& cr)
```

### TradingItemType

```angelscript
uint TradingItemType(Item& item)
```

### TradingItemType

```angelscript
uint TradingItemType(uint pid)
```

### InitItemsLevels

```angelscript
void InitItemsLevels()
```

### ItemLevel

```angelscript
uint ItemLevel(Item& item)
```

### ItemLevel

```angelscript
uint ItemLevel(uint pid)
```


