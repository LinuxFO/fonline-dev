---
title: merc_dialog.fos
description: " FOnline: 2238 Rotators  merc_dialog.fos ..."
---

# merc_dialog.fos


FOnline: 2238
Rotators

merc_dialog.fos


## Includes

- `_macros.fos`
- `mercs_h.fos`
- `utils_h.fos`
- `follower_h.fos`
- `economy_h.fos`
- `follower_common_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| FORCE_DIALOG_SUCCESS | `(5)` |  |
| FORCE_DIALOG_ERROR | `(6)` |  |
| FORCE_DIALOG_NOT_FOUND | `(7)` |  |
| FORCE_DIALOG_TOO_EXPENSIVE | `(8)` |  |
| FORCE_DIALOG_PARTY_FULL | `(9)` |  |
| FORCE_DIALOG_NO_FOLLOWER | `(9)` | Selling |
| FORCE_DIALOG_NO_SELL_PRICE | `(10)` |  |
| FORCE_DIALOG_SUCCESS_SOLD | `(11)` |  |
| CURRENT_MERC_ID | `(player.StatBase[ST_VAR1])` |  |
| SLAVES_PRESENT | `(player.StatBase[ST_VAR2])` |  |

## Functions

### d_HasFollowerOfType

Check if player has follower of specified basetype

```angelscript
bool d_HasFollowerOfType(Critter& player, Critter@ npc, int val)
```

### r_SellMerc

```angelscript
uint r_SellMerc(Critter& player, Critter@ npc, int val)
```

### r_SellCurrentMerc

```angelscript
uint r_SellCurrentMerc(Critter& player, Critter@ npc, int val)
```

### r_HireMerc

```angelscript
uint r_HireMerc(Critter& player, Critter@ npc, int MercId)
```

### r_SetMerc

```angelscript
void r_SetMerc(Critter& player, Critter@ npc, int val)
```

### r_GetSlaveTypes

```angelscript
void r_GetSlaveTypes(Critter& player, Critter@ npc, int val)
```

### d_IsSlavePresent

do NOT use this before using r_GetSlaveTypes(Critter& player, Critter@ npc, int val) first.

```angelscript
bool d_IsSlavePresent(Critter& player, Critter@ npc, int val)
```

### d_CanAffordMerc

```angelscript
bool d_CanAffordMerc(Critter& player, Critter@ npc, int val)
```

### dlg_ShowGhoulCost

```angelscript
void dlg_ShowGhoulCost(Critter& player, Critter@ npc, string@ text)
```

### dlg_ShowMutantCost

```angelscript
void dlg_ShowMutantCost(Critter& player, Critter@ npc, string@ text)
```

### dlg_ShowMeleeCost

```angelscript
void dlg_ShowMeleeCost(Critter& player, Critter@ npc, string@ text)
```

### dlg_ShowSmallGunsCost

```angelscript
void dlg_ShowSmallGunsCost(Critter& player, Critter@ npc, string@ text)
```

### dlg_ShowBigGunsCost

```angelscript
void dlg_ShowBigGunsCost(Critter& player, Critter@ npc, string@ text)
```

### dlg_ShowDogCost

```angelscript
void dlg_ShowDogCost(Critter& player, Critter@ npc, string@ text)
```

### dlg_ShowDog2Cost

```angelscript
void dlg_ShowDog2Cost(Critter& player, Critter@ npc, string@ text)
```

### dlg_ShowDog3Cost

```angelscript
void dlg_ShowDog3Cost(Critter& player, Critter@ npc, string@ text)
```

### dlg_ShowEnergyWeaponCost

```angelscript
void dlg_ShowEnergyWeaponCost(Critter& player, Critter@ npc, string@ text)
```

### dlg_ShowMoleratCost

```angelscript
void dlg_ShowMoleratCost(Critter& player, Critter@ npc, string@ text)
```

### dlg_ShowMercSellPrice

```angelscript
void dlg_ShowMercSellPrice(Critter& player, Critter@ npc, string@ text)
```

### dlg_ShowMercCost

```angelscript
void dlg_ShowMercCost(Critter& player, Critter@ npc, string@ text)
```

### dlg_ShowMaleSlavesPrices

```angelscript
void dlg_ShowMaleSlavesPrices(Critter& player, Critter@ npc, string@ text)
```

### dlg_ShowFemaleSlavesPrices

```angelscript
void dlg_ShowFemaleSlavesPrices(Critter& player, Critter@ npc, string@ text)
```


