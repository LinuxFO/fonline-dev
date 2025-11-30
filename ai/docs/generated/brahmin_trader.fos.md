---
title: brahmin_trader.fos
description: " FOnline: 2238 Rotators  brahmin_trader.fos ..."
---

# brahmin_trader.fos


FOnline: 2238
Rotators

brahmin_trader.fos


## Includes

- `_basetypes.fos`
- `_macros.fos`
- `brahmin_pen_h.fos`
- `brahmin_trader_h.fos`
- `economy_h.fos`
- `follower_common_h.fos`
- `follower_h.fos`
- `utils_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| FORCE_DIALOG_SUCCESS_SOLD | `(16)` |  |
| FORCE_DIALOG_SUCCESS_BUY | `(16)` |  |
| FORCE_DIALOG_ERROR | `(6)` |  |
| FORCE_DIALOG_NOT_FOUND | `(7)` |  |
| FORCE_DIALOG_TOO_EXPENSIVE | `(8)` |  |
| FORCE_DIALOG_FULL_PARTY | `(40)` |  |
| FORCE_DIALOG_BUY | `(4)` |  |
| FORCE_DIALOG_SELL | `(11)` |  |
| FORCE_DIALOG_NO_BRAHMINS | `(20)` |  |
| FORCE_DIALOG_PEN_FULL | `(21)` |  |
| BRAHMIN_HUB | `(9)` |  |
| BRAHMIN_MODOC | `(10)` |  |
| BRAHMIN_NCR | `(11)` |  |
| BRAHMIN_BROKEN | `(12)` |  |
| BRAHMIN_KLAMATH | `(13)` |  |
| BRAHMIN_FRISCO | `(14)` |  |
| SELLPRICE | `(player.StatBase[ST_VAR0])` |  |
| BUYPRICE | `(player.StatBase[ST_VAR1])` |  |
| TRADER | `(player.StatBase[ST_VAR2])` |  |

## Functions

### GetPrice

```angelscript
uint GetPrice(uint traderid, bool buyprice)
```

### d_BrahminInPen

```angelscript
bool d_BrahminInPen(Critter& player, Critter@ npc, int val)
```

### d_BrahminPenNotFull

```angelscript
bool d_BrahminPenNotFull(Critter& player, Critter@ npc, int val)
```

### d_CanAfford

```angelscript
bool d_CanAfford(Critter& player, Critter@ npc, int val)
```

### d_PlayerHasBrahmin

```angelscript
bool d_PlayerHasBrahmin(Critter& player, Critter@ npc, int val)
```

### SellableBrahmin

```angelscript
bool SellableBrahmin(Critter& critter)
```

### RightBrahminDistance

The brahmin must be close enough to the NPC we are selling to

```angelscript
bool RightBrahminDistance(Critter& brahmin, Critter@ npc)
```

### GetPlayerBrahmin

```angelscript
Critter@ GetPlayerBrahmin(Critter& player, Critter@ npc)
```

### r_SetId

```angelscript
void r_SetId(Critter& player, Critter@ npc, int val)
```

### dlg_ShowBrahminSellPrice

```angelscript
void dlg_ShowBrahminSellPrice(Critter& player, Critter@ npc, string@ text)
```

### dlg_ShowBrahminBuyPrice

```angelscript
void dlg_ShowBrahminBuyPrice(Critter& player, Critter@ npc, string@ text)
```

### r_CheckBuy

```angelscript
uint r_CheckBuy(Critter& player, Critter@ npc, int val)
```

### r_CheckSell

```angelscript
uint r_CheckSell(Critter& player, Critter@ npc, int val)
```

### r_SellBrahmin

```angelscript
uint r_SellBrahmin(Critter& player, Critter@ npc, int val)
```

### r_SellBrahminFarm

```angelscript
uint r_SellBrahminFarm(Critter& player, Critter@ npc, int val)
```

### r_BuyBrahmin

```angelscript
uint r_BuyBrahmin(Critter& player, Critter@ npc, int val)
```

### r_CleaningPayment

 Pays money for cleaned dung val - cash per shit

```angelscript
void r_CleaningPayment(Critter& player, Critter@ npc, int val)
```

### d_CleanedSomeDung

 Checks if player cleaned some crap for trader 

```angelscript
bool d_CleanedSomeDung(Critter& player, Critter@ npc)
```


