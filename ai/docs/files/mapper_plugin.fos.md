---
title: mapper_plugin.fos
description: " FOnline: 2238 Rotators  mapper_plugin.fos ..."
---

# mapper_plugin.fos


FOnline: 2238
Rotators

mapper_plugin.fos


## Includes

- `_macros.fos`
- `mapper_plugin_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __MAPPER_PLUGIN_MODULE__ |  |  |

## Functions

### Plugins_Register

```angelscript
bool Plugins_Register(IMapperPlugin@ plugin)
```

### Plugins_Render

```angelscript
void Plugins_Render(uint layer)
```

### Plugins_MouseDown

```angelscript
bool Plugins_MouseDown(int click)
```

### Plugins_MouseUp

```angelscript
bool Plugins_MouseUp(int click)
```

### Plugins_MouseMove

```angelscript
void Plugins_MouseMove(int x, int y)
```

### Plugins_KeyDown

```angelscript
bool Plugins_KeyDown(uint8 key,string& keyText)
```

### Plugins_KeyUp

```angelscript
bool Plugins_KeyUp(uint8 key,string& keyText)
```

### Plugins_InputLost

```angelscript
void Plugins_InputLost()
```

### Plugins_Loop

```angelscript
void Plugins_Loop()
```

### Plugins_Message

```angelscript
bool Plugins_Message(string& message)
```

### Plugins_RenderMap

```angelscript
void Plugins_RenderMap()
```


