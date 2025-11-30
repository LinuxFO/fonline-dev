---
title: hexShot.fos
---

# hexShot.fos

## Includes

- `_macros.fos`
- `MsgStr.h`
- `polygon_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| RADIUS_BORDER | `(0x77FF0000)` |  |

## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| Active | `bool` | `false` |  |
| LastCursor | `int` | `0` |  |
| lastH | `uint16` | `0, lastM = 0, lastS = 0, lastMS = 0` |  |

## Functions

### SelectWeaponBonus

```angelscript
int SelectWeaponBonus(ItemMutual@ RealWeapon, int Int_Val_WeaponBonus)
```

### IsHexShotWeapon

```angelscript
bool IsHexShotWeapon(ItemMutual@ item)
```

### HexShotGetMaxRange

```angelscript
uint HexShotGetMaxRange(CritterMutual& cr, ItemMutual@ item)
```

### IsHexShotable

```angelscript
bool IsHexShotable(ProtoItem& weapon)
```

### HexShotingToHit

```angelscript
int HexShotingToHit(CritterMutual& cr, uint16 tx, uint16 ty, ProtoItem& weapon, ItemMutual& realWeapon)
```

### HexShotActionPointsCost

```angelscript
int HexShotActionPointsCost(ItemMutual& item, CritterMutual& cr)
```

### IsHexShotableThere

```angelscript
bool IsHexShotableThere(CritterMutual& cr, ItemMutual@ item, uint16 tx, uint16 ty)
```

### unsafe_HexShot

```angelscript
void unsafe_HexShot(Critter& player, int px, int py, int p2, string@ param3, array<int>@ param4)
```

### CommenceHexShoting

```angelscript
void CommenceHexShoting(Critter& cr, Map& map, Item& item, uint16 tx, uint16 ty)
```

### e_HexShotExplode

```angelscript
uint e_HexShotExplode(array<uint>@ values)
```

### HexShotingMouseDown

```angelscript
bool HexShotingMouseDown(int click)
```

### IsHexShotingActive

```angelscript
bool IsHexShotingActive()
```

### HexShotingKeyDown

```angelscript
void HexShotingKeyDown(uint8 key)
```

### HexShotingKeyUp

```angelscript
void HexShotingKeyUp(uint8 key)
```

### HexShotingInputLost

```angelscript
void HexShotingInputLost()
```

### SetHexShoting

```angelscript
void SetHexShoting(bool enabled)
```

### RenderHexShoting

```angelscript
void RenderHexShoting()
```

### TryHexShot

```angelscript
void TryHexShot()
```

### CheckTimeDiff

```angelscript
bool CheckTimeDiff(uint16 lh, uint16 lm, uint16 ls, uint16 lms)
```


