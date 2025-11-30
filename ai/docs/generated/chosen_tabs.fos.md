---
title: chosen_tabs.fos
description: " FOnline: 2238 Rotators  chosen_tabs.fos ..."
---

# chosen_tabs.fos


FOnline: 2238
Rotators

chosen_tabs.fos


## Includes

- `_macros.fos`
- `_client_defines.fos`
- `_colors.fos`
- `MsgStr.h`
- `sprite.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| RADIATION_DEATH | `(1800)` |  |

## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| TabPic | `[Sprite](sprite.fos.md)` |  |  |
| Position | `array<int>` |  |  |
| StepX | `int` |  |  |
| StepY | `int` |  |  |
| LevelUp | `bool` |  |  |
| CurTab | `int` |  |  |

## Functions

### InitChosenTabs

```angelscript
void InitChosenTabs()
```

### ChosenTabSprite

```angelscript
Sprite ChosenTabSprite()
```

### ChosenTabsDrawn

```angelscript
int ChosenTabsDrawn()
```

### SetChosenTabLevelUp

```angelscript
void SetChosenTabLevelUp(bool enable)
```

### PercentColor

```angelscript
uint PercentColor(uint percent, bool clamp = true)
```

### DrawChosenTabs

```angelscript
void DrawChosenTabs()
```

### DrawTab

```angelscript
void DrawTab(string@ text, uint color, string@ onText = null, uint onColor = 0)
```

### DrawTab

```angelscript
void DrawTab(string@ text, int value, uint color, string@ onText = null, uint onColor = 0)
```


