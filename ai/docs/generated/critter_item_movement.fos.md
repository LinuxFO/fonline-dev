---
title: critter_item_movement.fos
description: " FOnline: 2238 Rotators  critter_item_movement.fos ..."
---

# critter_item_movement.fos


FOnline: 2238
Rotators

critter_item_movement.fos


## Includes

- `_defines.fos`
- `_basetypes.fos`
- `_macros.fos`

## Functions

### critter_check_move_item

///////////////////////////////////////////////////////////////////////////////////////////////// Call on something critter want move item from one slot to another. Return true to allow transaction, false to disallow. Function must exist on server and client side.

```angelscript
bool critter_check_move_item(Critter& cr, Item& item, uint8 toSlot, Item@ itemSwap)
```

### critter_move_item

///////////////////////////////////////////////////////////////////////////////////////////////// Call on critter change item in active slot - Hands or Armor. If Item::CritSlot == 0xFF than item dropped/erased

```angelscript
void critter_move_item(Critter& cr, Item& item, uint8 fromSlot)
```


