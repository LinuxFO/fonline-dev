---
title: mapper_grid.fos
description: " FOnline: 2238 Rotators  mapper_grid.fos ..."
---

# mapper_grid.fos


FOnline: 2238
Rotators

mapper_grid.fos


## Includes

- `_mapper_macros.fos`
- `mapper_plugin_h.fos`
- `mapper_utils_h.fos`
- `strtoint_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __MAPPER_GRID__ |  |  |

## Classes

### CGrid

**Methods**

#### GetName
```angelscript
string GetName() { return "Grid"; }
```

#### Render
```angelscript
void Render(uint layer)
```

#### Message
```angelscript
bool Message(string& message)
```

#### RenderMap
```angelscript
void RenderMap()         {}
```

#### MouseDown
```angelscript
bool MouseDown(int)      { return false; }
```

#### MouseUp
```angelscript
bool MouseUp(int)        { return false; }
```

#### MouseMove
```angelscript
void MouseMove(int, int) {}
```

#### KeyDown
```angelscript
bool KeyDown(uint8 key,string& keyText)
```

#### KeyUp
```angelscript
bool KeyUp(uint8,string&) { return false; }
```

#### InputLost
```angelscript
void InputLost()          {}
```

#### Loop
```angelscript
void Loop()               {}
```


## Functions

### RegisterGrid

```angelscript
void RegisterGrid()
```


