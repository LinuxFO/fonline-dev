---
title: debug.fos
description: " FOnline: 2238 Rotators  debug.fos ..."
---

# debug.fos


FOnline: 2238
Rotators

debug.fos


## Includes

- `_macros.fos`
- `debug_h.fos`
- `logging_h.fos`
- `utils_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __DEBUG_MODULE__ |  |  |
| SET_DEBUG_LEVEL | `# (name, level)Dict.set(name, level)` |  |

## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| Dict | `dictionary` |  |  |

## Functions

### InitDebug

Set minimum levels here

```angelscript
void InitDebug()
```

### WLog

```angelscript
void WLog(string& type, string& message, int level)
```

### WLog

Duplication: PrintCallstack requires it

```angelscript
void WLog(string& type, string& message)
```

### ToShow

```angelscript
bool ToShow(string& type, int level)
```

### ToShowCallstack

```angelscript
bool ToShowCallstack(int level)
```

### ToBroadcast

```angelscript
bool ToBroadcast(int level)
```

### LevelToString

```angelscript
string@ LevelToString(int level)
```


