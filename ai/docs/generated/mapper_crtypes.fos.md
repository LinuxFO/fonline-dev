---
title: mapper_crtypes.fos
description: " FOnline: 2238 Rotators  mapper_crtypes.fos ..."
---

# mapper_crtypes.fos


FOnline: 2238
Rotators

mapper_crtypes.fos


## Includes

- `_macros.fos`
- `mapper_gui.fos`
- `mapper_plugin_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| SPR_HEIGHT | `(100)` |  |
| SPR_WIDTH | `(50)` |  |

## Classes

### CCrButton

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| Crtype | `uint` |  |  |
| def | `bool` |  |  |
| index | `int` |  |  |
| menu | `[CCrtypeMenu](mapper_crtypes.fos.md)@` |  |  |

**Methods**

#### Draw
```angelscript
void Draw()
```

#### Click
```angelscript
void Click()
```

### CCrtypeMenu

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| critter | `MapperObject@` |  |  |

**Methods**

#### Fill
```angelscript
void Fill(MapperObject@ obj)
```

#### Selected
```angelscript
void Selected(uint crtype, bool def)
```

#### Show
```angelscript
void Show(int x, int y)
```

#### MouseDown
```angelscript
bool MouseDown(int click)
```

### CCrtypePlugin

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| Alt | `bool` |  |  |
| LastIndex | `int` |  |  |

**Methods**

#### KeyDown
```angelscript
bool KeyDown(uint8 key,string& keyText)
```

#### KeyUp
```angelscript
bool KeyUp(uint8 key,string& keyText)
```

#### InputLost
```angelscript
void InputLost() {}
```

#### Loop
```angelscript
void Loop()
```

#### Render
```angelscript
void Render(uint layer)
```

#### Message
```angelscript
bool Message(string&) { return false; }
```

#### RenderMap
```angelscript
void RenderMap()      {}
```


## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| UnarmoredTypesMale | `array<uint>` |  |  |
| UnarmoredTypesFemale | `array<uint>` |  |  |
| Menu | `[CCrtypeMenu](mapper_crtypes.fos.md)@` |  |  |
| Plugin | `[CCrtypePlugin](mapper_crtypes.fos.md)@` |  |  |

## Functions

### SetUnarmoredCrtypes

```angelscript
void SetUnarmoredCrtypes()
```

### AssertCrtypeReadiness

```angelscript
bool AssertCrtypeReadiness(MapperObject@ critter)
```

### GetValidCrtypes

```angelscript
array<uint>@ GetValidCrtypes(MapperObject@ critter, uint16 pid)
```

### GetArmorPid

```angelscript
uint16 GetArmorPid(MapperObject@ critter)
```

### ChangeCrtype

```angelscript
void ChangeCrtype(MapperObject@ critter, uint crtype)
```

### UpdateImplied

```angelscript
void UpdateImplied(MapperObject@ critter, uint16 pid, uint& implied)
```

### NormalizeCrtype

```angelscript
void NormalizeCrtype(MapperObject@ critter)
```

### RegisterCrtypes

```angelscript
void RegisterCrtypes()
```


