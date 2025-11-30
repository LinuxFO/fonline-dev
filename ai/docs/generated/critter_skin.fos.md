---
title: critter_skin.fos
description: " Wipe/Rotators  critter_skin.fos ..."
---

# critter_skin.fos


Wipe/Rotators

critter_skin.fos


## Includes

- `_defines.fos`
- `_macros.fos`
- `_basetypes.fos`
- `ITEMPID.H`
- `critter_skin_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __CRITTER_SKIN__ |  |  |
| _SkinErr |  | i'm THAT lazy |
| _SkinError |  |  |
| _SkinErrorR |  |  |
| _GETTER |  |  |
| _INFO |  |  |

## Classes

### SkinBase

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| heavyEW | `SkinInfo` |  |  |
| throwing | `SkinInfo` |  |  |
| running | `SkinInfo` |  |  |

**Methods**

#### get_opIndex
```angelscript
uint16 get_opIndex( uint16 crType )
```

#### set_opIndex
```angelscript
void set_opIndex( uint16 crType, uint16 value )
```

#### Set
```angelscript
SkinBase@ Set( uint16 crType, uint16 value )
```

#### Set
```angelscript
SkinBase@ Set( uint16 crType, uint16 female, uint16 male )
```

#### Set
```angelscript
SkinBase@ Set( array<uint16> list )
```

#### Set
```angelscript
SkinBase@ Set( uint16 crType, array<uint16> list )
```

#### Unset
```angelscript
SkinBase@ Unset( uint16 crType )
```

#### Lock
locked skins always return base crType

```angelscript
SkinBase@ Lock()
```

#### Fill
filling = setting redirects only if they haven't been set previously

```angelscript
SkinBase@ Fill()
```

#### Fill
```angelscript
SkinBase@ Fill( uint16 crType )
```

#### Fill
```angelscript
SkinBase@ Fill( array<uint16> list )
```

#### Fill
```angelscript
SkinBase@ Fill( uint16 crType, array<uint16> tmpl )
```

#### Humanize
fills missing redirects with defaults for npc_barber should be used for all non-locked human skins which have some animations missing

```angelscript
SkinBase@ Humanize()
```

#### LongHair
```angelscript
SkinBase@ LongHair()
```

#### Bald
```angelscript
SkinBase@ Bald()
```

#### LeatherJacket
```angelscript
SkinBase@ LeatherJacket()
```

#### LeatherJacket
```angelscript
SkinBase@ LeatherJacket( uint16 crType )
```

#### LeatherArmor
```angelscript
SkinBase@ LeatherArmor()
```

#### LeatherArmor
```angelscript
SkinBase@ LeatherArmor( uint16 crType )
```

#### Leather
```angelscript
SkinBase@ Leather()
```

#### Leather
```angelscript
SkinBase@ Leather( uint16 crType )
```

#### Robes
```angelscript
SkinBase@ Robes()
```

#### Robes
```angelscript
SkinBase@ Robes( uint16 crType )
```

#### MetalArmor
```angelscript
SkinBase@ MetalArmor()
```

#### MetalArmor
```angelscript
SkinBase@ MetalArmor( uint16 crType )
```

#### CombatArmor
```angelscript
SkinBase@ CombatArmor()
```

#### CombatArmor
```angelscript
SkinBase@ CombatArmor( uint16 crType )
```

#### PowerArmor
```angelscript
SkinBase@ PowerArmor( uint16 crType )
```

#### RefreshInfo
another npc_barber crap

```angelscript
void RefreshInfo()
```

#### Effect
```angelscript
void Effect( SkinEffect eff )
```


## Functions

### InitSkins

```angelscript
void InitSkins()
```

### ValidateSkins

```angelscript
bool ValidateSkins()
```

### AddSkin

 add 

```angelscript
SkinBase@ AddSkin( uint16 crType )
```

### AddSkinFemale

```angelscript
SkinBase@ AddSkinFemale( uint16 crType )
```

### AddSkinMale

```angelscript
SkinBase@ AddSkinMale( uint16 crType )
```

### AddSkin

```angelscript
SkinBase@ AddSkin( uint16 crType, uint8 gender )
```

### GetSkin

 get 

```angelscript
Skin@ GetSkin( Critter& cr )
```

### GetSkin

```angelscript
Skin@ GetSkin( uint16 base )
```

### CheckWeapon

 misc 

```angelscript
void CheckWeapon( SkinInfo& result, uint crType, uint weaponPid )
```

### SetSkinEffects

 effects 

```angelscript
void SetSkinEffects( Critter& cr, Skin& skin )
```

### UnsetSkinEffects

```angelscript
void UnsetSkinEffects( Critter& cr )
```

### changedParam_SkinHooks

```angelscript
void changedParam_SkinHooks( Critter& cr, uint param, int oldValue )
```


