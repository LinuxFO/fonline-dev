---
title: throwing.fos
description: " FOnline: 2238 Rotators  throwing.fos ..."
---

# throwing.fos


FOnline: 2238
Rotators

throwing.fos


## Includes

- `_macros.fos`
- `MsgStr.h`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| STR_THROWING_HIT | `(10400)` |  |
| STR_THROWING_MISS | `(10401)` |  |

## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| Active | `bool` | `false` |  |
| LastCursor | `int` | `0` |  |

## Functions

### IsThrowingWeapon

```angelscript
bool IsThrowingWeapon(ItemMutual@ item)
```

### GetMaxRange

```angelscript
uint GetMaxRange(CritterMutual& cr, ItemMutual@ item)
```

### IsThrowable

```angelscript
bool IsThrowable(ProtoItem& weapon)
```

### ThrowingToHit

```angelscript
int ThrowingToHit(CritterMutual& cr, uint16 tx, uint16 ty, ProtoItem& weapon)
```

### ActionPointsCost

```angelscript
int ActionPointsCost(ItemMutual& item, uint8 brofBonus)
```

### IsThrowableThere

```angelscript
bool IsThrowableThere(CritterMutual& cr, ItemMutual@ item, uint16 tx, uint16 ty)
```

### unsafe_Throw

```angelscript
void unsafe_Throw(Critter& player, int px, int py, int p2, string@ param3, array<int>@ param4)
```

### IsGrenade

```angelscript
bool IsGrenade(Item& item)
```

### CommenceThrowing

```angelscript
void CommenceThrowing(Critter& cr, Map& map, Item& item, uint16 tx, uint16 ty)
```

### e_Explode

```angelscript
uint e_Explode(array<uint>@ values)
```

### ThrowingMouseDown

```angelscript
bool ThrowingMouseDown(int click)
```

### IsThrowingActive

```angelscript
bool IsThrowingActive()
```

### ThrowingKeyDown

```angelscript
void ThrowingKeyDown(uint8 key)
```

### ThrowingKeyUp

```angelscript
void ThrowingKeyUp(uint8 key)
```

### ThrowingInputLost

```angelscript
void ThrowingInputLost()
```

### SetThrowing

```angelscript
void SetThrowing(bool enabled)
```

### RenderThrowing

```angelscript
void RenderThrowing()
```

### TryThrow

```angelscript
void TryThrow()
```


