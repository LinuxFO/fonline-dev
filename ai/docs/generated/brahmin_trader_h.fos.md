---
title: brahmin_trader_h.fos
description: " FOnline: 2238 Rotators  brahmin_trader_h.fos ..."
---

# brahmin_trader_h.fos


FOnline: 2238
Rotators

brahmin_trader_h.fos


## Included By

- [brahmin_trader.fos](brahmin_trader.fos.md)
- [brahmin_traders.fos](brahmin_traders.fos.md)

## Classes

### CBrahminTrader

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| buyprice | `uint` |  | Base prices |
| sellprice | `uint` |  |  |
| modifier | `uint` |  | Price modifier dependant on number of brahmins |
| penid | `uint` |  |  |

**Methods**

#### GetSellPrice
```angelscript
uint GetSellPrice() { return sellprice; }
```

#### GetBuyPrice
```angelscript
uint GetBuyPrice()  { return buyprice; }
```

#### GetModifier
```angelscript
uint GetModifier()  { return modifier; }
```

#### GetPenID
```angelscript
uint GetPenID()     { return penid; }
```

#### BrahminPen
```angelscript
IBrahminTrader@ BrahminPen(uint penid)
```

#### SellPrice
```angelscript
IBrahminTrader@ SellPrice(uint price)
```

#### BuyPrice
```angelscript
IBrahminTrader@ BuyPrice(uint price)
```

#### Modifier
```angelscript
IBrahminTrader@ Modifier(uint price)
```


