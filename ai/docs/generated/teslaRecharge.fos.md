---
title: teslaRecharge.fos
---

# teslaRecharge.fos

## Includes

- `_macros.fos`
- `MsgStr.h`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| MFC_RECHARGE_VAL | `5` |  |
| SEC_RECHARGE_VAL | `2` |  |

## Functions

### TryRechargeItem

```angelscript
bool TryRechargeItem(Critter& cr, Item& item)
```

### RechargeCallback

```angelscript
void RechargeCallback(Critter& cr, uint n, string& s)
```

### RechargeArmor

```angelscript
bool RechargeArmor(Item& item, Critter& cr, Item@ usedItem)
```


