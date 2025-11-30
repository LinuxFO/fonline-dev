---
title: item_perks.fos
description: " FOnline: 2238 Rotators  item_perks.fos ..."
---

# item_perks.fos


FOnline: 2238
Rotators

item_perks.fos


## Includes

- `_defines.fos`
- `_macros.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __ITEM_PERKS__ |  |  |
| Item_Perk | `Armor_Perk` |  |

## Functions

### ItemPerkTypeParam

helper

```angelscript
uint ItemPerkTypeParam(uint8 type)
```

### DisableItemPerk

```angelscript
void DisableItemPerk(Critter& cr, uint8 type)
```

### DisableItemPerk

```angelscript
void DisableItemPerk(Critter& cr, Item& item, uint8 type)
```

### EnableItemPerk

```angelscript
void EnableItemPerk(Critter& cr, Item& item, uint8 type)
```

### ApplyItemPerk

```angelscript
void ApplyItemPerk(Critter& cr, uint8 type, uint perk, bool enable)
```


