---
title: multihex.fos
description: " FOnline: 2238 Rotators  multihex.fos ..."
---

# multihex.fos


FOnline: 2238
Rotators

multihex.fos


## Includes

- `_macros.fos`
- `multihex_h.fos`
- `multihex_data.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __MULTIHEX__ |  |  |

## Functions

### MultihexSpawned

Should be called when the multihex item is spawned. 

```angelscript
void MultihexSpawned(Item& item)
```

### MultihexDeleted

Should be called when the multihex item is removed from the game. 

```angelscript
void MultihexDeleted(Item& item)
```

### GetMHexes

Gets all mHexes (PID_MHEX items) attached to a multihex item. 

```angelscript
uint GetMHexes(Item@ item, array<Item@>@ mHexes)
```

### IsMultihex

Returns true if the item is a multihex item. 

```angelscript
bool IsMultihex(Item@ item)
```

### IsMultihexBlocked

Returns true if any of the non-blocking hexes of the multihex item (mHexes or the item hex) are blocked by something else. 

```angelscript
bool IsMultihexBlocked(Item@ item)
```

### MultihexClose

Switches multihex to state 1 (AKA closed/off/default). 

```angelscript
void MultihexClose(Item@ item)
```

### MultihexOpen

Switches multihexes to state 2 (AKA open/on/non-default). 

```angelscript
void MultihexOpen(Item@ item)
```

### e_AddMHexes

TimeEvent function to delay spawning mHexes a bit. 

```angelscript
uint e_AddMHexes(array<uint>@ values)
```

### AddMHexes

Spawns mHexes for the multihex item according to the mHexData. 

```angelscript
void AddMHexes(Item@ item, const array<uint>@ mHexData)
```

### DeleteMHexes

Deletes all mHexes connected to the multihex item. 

```angelscript
void DeleteMHexes(Item@ item)
```

### GetMHexPosition

Returns by reference position of an mHex. Used when placing mHexes according to MHexData. 

```angelscript
void GetMHexPosition(uint move, Map& map, uint16& x, uint16& y)
```

### _Init

```angelscript
void _Init(Item& item, bool firstTime)
```

### _Finish

```angelscript
void _Finish(Item& item, bool deleted)
```

### _Walk

Called by mHexes when a critter walks on them. 

```angelscript
void _Walk(Item& item, Critter& cr, bool entered, uint8 dir)
```

### GuardMultihexMove

Called by critter_move_item() to protect multihexes from abuse. 

```angelscript
void GuardMultihexMove(Item& item, uint8 fromSlot, uint8 toSlot)
```

### close

```angelscript
void close(Critter& cr, int i, int, int)
```

### open

```angelscript
void open(Critter& cr, int i, int, int)
```

### cleanup

```angelscript
void cleanup(Critter& cr, int i, int, int)
```

### show

```angelscript
void show(Critter& cr, int i, int, int)
```

### hide

```angelscript
void hide(Critter& cr, int i, int, int)
```


