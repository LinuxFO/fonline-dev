---
title: hexThrow.fos
---

# hexThrow.fos

## Includes

- `_macros.fos`
- `MsgStr.h`
- `polygon_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| STR_THROWING_HIT | `(10400)` |  |
| STR_THROWING_MISS | `(10401)` |  |
| RANGE_BORDER | `(0x77FF7777)` |  |
| SPLASH_RADIUS_BORDER | `(0x77FF0000)` |  |

## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| Active | `bool` | `false` |  |
| LastCursor | `int` | `0` |  |
| itemPos | `int` | `0` |  |
| availableCnt | `uint` | `0` |  |
| lastH | `uint16` | `0, lastM = 0, lastS = 0, lastMS = 0` |  |

## Functions

### IsHexThrowingWeapon

```angelscript
bool IsHexThrowingWeapon(ItemMutual@ item)
```

### HexThrowGetMaxRange

```angelscript
uint HexThrowGetMaxRange(CritterMutual& cr, ItemMutual@ item)
```

### IsHexThrowable

```angelscript
bool IsHexThrowable(ProtoItem& weapon)
```

### HexThrowingToHit

```angelscript
int HexThrowingToHit(CritterMutual& cr, uint16 tx, uint16 ty, ProtoItem& weapon)
```

### HexThrowActionPointsCost

```angelscript
int HexThrowActionPointsCost(ItemMutual& item, CritterMutual& cr)
```

### IsHexThrowableThere

```angelscript
bool IsHexThrowableThere(CritterMutual& cr, ItemMutual@ item, uint16 tx, uint16 ty)
```

### IsGrenade

```angelscript
bool IsGrenade(ItemMutual& item)
```

### unsafe_HexThrow

```angelscript
void unsafe_HexThrow(Critter& player, int px, int py, int p2, string@ param3, array<int>@ param4)
```

### CommenceHexThrowing

```angelscript
void CommenceHexThrowing(Critter& cr, Map& map, Item& item, uint16 tx, uint16 ty)
```

### e_HexThrowExplode

```angelscript
uint e_HexThrowExplode(array<uint>@ values)
```

### _UpdateWeapons

```angelscript
void _UpdateWeapons(int param1, int param2, int param3, string@ param4, array<int>@ param5)
```

### FindAvailableWeapons

```angelscript
bool FindAvailableWeapons()
```

### HexThrowingMouseDown

```angelscript
bool HexThrowingMouseDown(int click)
```

### IsHexThrowingActive

```angelscript
bool IsHexThrowingActive()
```

### HexThrowingKeyDown

```angelscript
void HexThrowingKeyDown(uint8 key)
```

### HexThrowingKeyUp

```angelscript
void HexThrowingKeyUp(uint8 key)
```

### HexThrowingInputLost

```angelscript
void HexThrowingInputLost()
```

### SetHexThrowing

```angelscript
void SetHexThrowing(bool enabled)
```

### RenderHexThrowing

```angelscript
void RenderHexThrowing()
```

### TryHexThrow

```angelscript
void TryHexThrow()
```

### CheckTimeDiff

```angelscript
bool CheckTimeDiff(uint16 lh, uint16 lm, uint16 ls, uint16 lms)
```


