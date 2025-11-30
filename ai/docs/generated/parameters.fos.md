---
title: parameters.fos
description: " FOnline: 2238 Rotators  parameters.fos ..."
---

# parameters.fos


FOnline: 2238
Rotators

parameters.fos


## Includes

- `_macros.fos`
- `MsgStr.h`
- `lexems_h.fos`

## Functions

### getParamDialog_Reputation

```angelscript
int getParamDialog_Reputation(Critter@ master, Critter@ slave, uint index)
```

### changedParam_Hp

```angelscript
void changedParam_Hp(Critter& cr, uint, int oldValue)
```

### changedParam_Experience

```angelscript
void changedParam_Experience(Critter& cr, uint, int oldValue)
```

### changedParam_Level

```angelscript
void changedParam_Level(Critter& cr, uint a, int oldLevel)
```

### changedParam_Perks

```angelscript
void changedParam_Perks(Critter& cr, uint perk, int oldValue)
```

### changedParam_Hide

```angelscript
void changedParam_Hide(Critter& cr, uint, int oldValue)
```

### changedParam_FastShot

```angelscript
void changedParam_FastShot(Critter& cr, uint, int oldValue)
```

### NextLevelNeedExp

```angelscript
int NextLevelNeedExp(Critter& cr)
```

### changedParam_Alpha

```angelscript
void changedParam_Alpha( CritterCl& cr, uint, int )
```

### changedParam_Level

```angelscript
void changedParam_Level(CritterCl& cr, uint, int oldValue)
```

### changedParam_Experience

```angelscript
void changedParam_Experience(CritterCl& cr, uint, int oldValue)
```

### changedParam_UnspentPerks

```angelscript
void changedParam_UnspentPerks(CritterCl& cr, uint, int oldValue)
```

### changedParam_UnspentTag

```angelscript
void changedParam_UnspentTag(CritterCl& cr, uint, int oldValue)
```

### changedParam_Hide

```angelscript
void changedParam_Hide(CritterCl& cr, uint, int oldValue)
```

### GetMaxLife

```angelscript
int GetMaxLife(Critter& cr)
```

### IsPassiveSkill

```angelscript
bool IsPassiveSkill( int skill )
```

### CritterGenerate

```angelscript
void CritterGenerate(Critter& cr)
```

### CritterGenerate

```angelscript
void CritterGenerate(array<int>& data)
```

### CritterGenerateCheck

Check valid of input data

```angelscript
bool CritterGenerateCheck(array<int>& data)
```

### NpcProcessLevel

```angelscript
void NpcProcessLevel(Critter& npc)
```

### NpcSetLevel

backward compatibility

```angelscript
void NpcSetLevel(Critter& npc, int level)
```

### CheckPlayerName

```angelscript
uint CheckPlayerName( const string& name )
```

### Critter_IsOverweight

```angelscript
bool Critter_IsOverweight(CritterMutual& cr)
```


