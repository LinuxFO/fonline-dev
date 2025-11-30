---
title: name_colorizing.fos
description: " FOnline: 2238 Rotators  name_colorizing.fos ..."
---

# name_colorizing.fos


FOnline: 2238
Rotators

name_colorizing.fos


## Includes

- `_colors.fos`
- `_macros.fos`
- `minigames_h.fos`
- `lexems_h.fos`

## Classes

### Record

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| NameStr | `string` |  |  |
| NameColor | `uint` |  |  |
| ContourColor | `uint` |  |  |


## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| Records | `array<[Record](name_colorizing.fos.md)>` |  |  |
| Colorized | `array<int>` |  |  |

## Functions

### InitNameColorizing

```angelscript
void InitNameColorizing()
```

### IsFollowerCl

```angelscript
bool IsFollowerCl(CritterCl& cr)
```

### GetColor

```angelscript
uint GetColor(dictionary& dict, string& colorName, uint defaultColor)
```

### CompareName

```angelscript
bool CompareName(string& crName, string& nameStr)
```

### ColorizeCritterPreview

Special colorization for preview screen because chosen is not valid there

```angelscript
void ColorizeCritterPreview(CritterCl& cr)
```

### ColorizeCritter

Colorize critter, called by client script from other module

```angelscript
void ColorizeCritter(CritterCl& cr)
```

### ColorizeCritter

Because colorization of critter may be enforced by server, we need to send ST_MINIGAME_DATA of the critters as separate arguments, because it might be not yet received by client if it changed by the server script.

```angelscript
void ColorizeCritter(CritterCl& chosen, CritterCl& cr, int chosenMgData, int crMgData)
```

### ColorizeMinigame

```angelscript
bool ColorizeMinigame(CritterCl& chosen, CritterCl& cr, int chosenMgData, int crMgData)
```

### ColorizeFromFile

```angelscript
bool ColorizeFromFile(CritterCl& chosen, CritterCl& cr)
```

### ColorizeGoodEvil

```angelscript
bool ColorizeGoodEvil(CritterCl& chosen, CritterCl& cr)
```

### _RefreshColorizing

```angelscript
void _RefreshColorizing(int, int, int, string@, array<int>@ data)
```

### RefreshColorizing

```angelscript
void RefreshColorizing(Critter@ chosen)
```

### RefreshColorizingMyself

Tells chosen to recolorize himself/herself

```angelscript
void RefreshColorizingMyself(Critter@ chosen)
```

### RefreshColorizingOthers

Tells chosen to recolorize other critters

```angelscript
void RefreshColorizingOthers(Critter@ chosen)
```

### RefreshColorizingMe

Tells other players to recolorize chosen

```angelscript
void RefreshColorizingMe(Critter@ chosen)
```


