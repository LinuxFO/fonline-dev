---
title: npc_barber.fos
description: " FOnline: 2238 Rotators  npc_barber.fos ..."
---

# npc_barber.fos


FOnline: 2238
Rotators

npc_barber.fos


## Includes

- `_defines.fos`
- `_macros.fos`
- `_colors.fos`
- `_basetypes.fos`
- `_dialogs.fos`
- `ITEMPID.H`
- `critter_skin_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| NODE_SKINSELECT | `(10)` | dialog nodes redirections |
| NODE_NOCAPS | `(1000)` |  |
| SKIN_CRTYPE | `(0)` |  |
| SKIN_PRICE | `(1)` |  |
| SKIN_END | `(2)` |  |
| PRICE_DEFAULT | `(50)` |  |
| PRICE_HUMANOID | `(1000)` |  |
| PRICE_ANIMAL | `(500)` |  |
| PRICE_ROBOT | `(5000)` |  |
| PRICE_VIP | `(2500)` |  |
| FASTCOLOR |  |  |
| SAND_TEXT |  |  |
| RED_TEXT |  |  |

## Functions

### SkinDemand

```angelscript
bool SkinDemand( Critter& cr, uint crType, bool dBase, bool dPrice )
```

### d_SkinDemand

```angelscript
bool d_SkinDemand( Critter& player, Critter@ npc )
```

### d_SkinDemand

```angelscript
bool d_SkinDemand( Critter& player, Critter@ npc, int crType )
```

### d_SkinDemandNoCaps

```angelscript
bool d_SkinDemandNoCaps( Critter& player, Critter@ kitty, int crType )
```

### d_SkinDemandEx

```angelscript
bool d_SkinDemandEx( Critter& player, Critter@ kitty, int crType, int base, int price )
```

### FixDefaultCrType

```angelscript
void FixDefaultCrType( Critter& cr, int& crType )
```

### r_SkinShowPrepare

```angelscript
void r_SkinShowPrepare(Critter& player, Critter@ npc, int crType)
```

### CanUseWeapon

```angelscript
bool CanUseWeapon(uint crType, uint weaponPid )
```

### SkinInfoText

```angelscript
void SkinInfoText( array<string@>& list, SkinInfo info, string& text )
```

### dlg_SkinShow

```angelscript
void dlg_SkinShow(Critter& player,Critter@ npc,string@ lexems)
```

### r_SkinChange

```angelscript
uint r_SkinChange( Critter& player, Critter@ npc )
```

### r_SkinChange

```angelscript
uint r_SkinChange( Critter& player, Critter@ npc, int crType )
```

### d_NeedTestSet

```angelscript
bool d_NeedTestSet( Critter& player, Critter@, int idx )
```

### r_GiveTestSet

```angelscript
void r_GiveTestSet( Critter& player, Critter@, int idx )
```

### r_ChangeGender

```angelscript
void r_ChangeGender( Critter& player, Critter@ )
```

### r_Haircut

TODO: DEPRECATE THIS SHIT (cath_barber.fodlg)

```angelscript
void r_Haircut( Critter& player, Critter@ npc, int crType)
```

### d_IsCrType

```angelscript
bool d_IsCrType(Critter& player, Critter@ kitty, int crType)
```

### d_IsNotCrType

```angelscript
bool d_IsNotCrType(Critter& player, Critter@ kitty, int crType)
```


