---
title: client_fixboy.fos
---

# client_fixboy.fos

## Includes

- `_colors.fos`
- `client_gui_h.fos`
- `client_gui_ex.fos`
- `client_utils_h.fos`
- `_client_defines.fos`
- `_macros.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __CLIENT_FIXBOY_ADDONS__ |  |  |

## Classes

### InjectCounterLabel

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| window | `IGUIScreenOpt@` |  |  |
| picControl | `[Control](mapper_gui.fos.md)@` |  |  |

**Methods**

#### TextPosition
```angelscript
void TextPosition(string& ini)
```

#### Left
```angelscript
int Left()
```

#### Top
```angelscript
int Top()
```

#### Draw
```angelscript
void Draw()
```

### InjectCounterButton

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| window | `IGUIScreenOpt@` |  |  |
| buttonDown | `[Sprite](sprite.fos.md)` |  |  |
| iniCord | `string` |  |  |
| change | `int` |  |  |

**Methods**

#### Init
```angelscript
void Init()
```

#### Click
```angelscript
void Click()
```

#### Left
```angelscript
int Left()
```

#### Top
```angelscript
int Top()
```

#### Draw
```angelscript
void Draw()
```

### InjectFixAllButton

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| window | `IGUIScreenOpt@` |  |  |
| isChecked | `bool` |  |  |
| buttonDown | `[Sprite](sprite.fos.md)` |  |  |

**Methods**

#### Init
```angelscript
void Init()
```

#### SetState
```angelscript
void SetState(bool st)
```

#### Click
```angelscript
void Click()
```

#### Left
```angelscript
int Left()
```

#### Top
```angelscript
int Top()
```

#### Draw
```angelscript
void Draw()
```

### InjectFilterButton

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| window | `IGUIScreenOpt@` |  |  |
| buttonDown | `[Sprite](sprite.fos.md)` |  |  |
| iniCord | `string` |  |  |
| filter | `uint8` |  |  |

**Methods**

#### Init
```angelscript
void Init()
```

#### Click
```angelscript
void Click()
```

#### Left
```angelscript
int Left()
```

#### Top
```angelscript
int Top()
```

#### Draw
```angelscript
void Draw()
```


## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| insectCntVal | `[InjectCounterLabel](client_fixboy.fos.md)@` |  |  |
| insectFixAll | `[InjectFixAllButton](client_fixboy.fos.md)@` |  |  |

## Functions

### InitFixboyAddons

```angelscript
void InitFixboyAddons()
```

### GetPlayerCounter

```angelscript
uint8 GetPlayerCounter()
```

### SetupFixboyAddons

```angelscript
void SetupFixboyAddons()
```

### ExecuteSetFixCounter

```angelscript
void ExecuteSetFixCounter(uint8 cnt)
```

### ExecuteSetFixAll

```angelscript
void ExecuteSetFixAll(uint8 cnt)
```

### ExecuteSetFixFilter

```angelscript
void ExecuteSetFixFilter(uint8 filter)
```

### FormatXX

```angelscript
string@ FormatXX( int value )
```


