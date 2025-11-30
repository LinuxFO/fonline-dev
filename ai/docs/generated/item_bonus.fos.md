---
title: item_bonus.fos
description: "Item bonuses ..."
---

# item_bonus.fos

Item bonuses


## Includes

- `_defines.fos`
- `_macros.fos`

## Functions

### BonusNumber

Returns the number of item bonuses

```angelscript
uint BonusNumber(Item@ it)
```

### CheckBonus

```angelscript
int CheckBonus( Item@ item, int bonusType )
```

### AddSpecialBonusRaidersFarm

used to add bonuses to gear used by raiders in farm locations

```angelscript
void AddSpecialBonusRaidersFarm(Item@ it)
```

### AddSpecialBonusEncounterBoss

used to add bonuses to gear used by boss in encounters

```angelscript
void AddSpecialBonusEncounterBoss(Item@ it)
```

### AddSpecialBonusLow

```angelscript
void AddSpecialBonusLow(Item@ it)
```

### AddSpecialBonus

```angelscript
void AddSpecialBonus(Item@ it)
```

### AddBonuses

```angelscript
void AddBonuses(Item@ it, string@ crafter)
```

### AddAnotherBonus

```angelscript
bool AddAnotherBonus(Item@ it)
```

### AddArmorBonus

```angelscript
void AddArmorBonus(Item@ it, int number)
```

### AddWeaponBonus

```angelscript
void AddWeaponBonus(Item@ it, int number, bool isCrafting = false)
```

### IsBonusExcluded

Checks if given bonus is allowed - used to exclude some bonuses from crafting

```angelscript
bool IsBonusExcluded(bool isCrafting, int bonusType)
```

### HasBonusAlready

Checks if there is no such bonus already on an item

```angelscript
bool HasBonusAlready(Item@ it, int bonusType)
```

### checkBonus

```angelscript
int checkBonus(Item@ it, int bonusType)
```


