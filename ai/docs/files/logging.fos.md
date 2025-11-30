---
title: logging.fos
description: " FOnline: 2238 Rotators  logging.fos ..."
---

# logging.fos


FOnline: 2238
Rotators

logging.fos


## Includes

- `_macros.fos`
- `utils_h.fos`
- `logging_h.fos`
- `config_file_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __LOGGING__ |  |  |

## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| filenames | `array<string>` |  |  |
| ilogdir | `string` | `""` |  |

## Functions

### AddLog

```angelscript
uint AddLog(string& filename)
```

### AddLog

```angelscript
uint AddLog(string& filename, uint index)
```

### InitLogs

```angelscript
void InitLogs()
```

### GMLog

```angelscript
void GMLog(Critter& cr, string& text)
```

### FLog

```angelscript
void FLog(uint logindex, string& text)
```

### ILog

it's bad and ugly, should be replaced by DevConnect...

```angelscript
void ILog(string& section, string& text)
```

### GetLogHeader

```angelscript
string GetLogHeader()
```

### CloseLogs

```angelscript
void CloseLogs()
```

### DynamicLocationAddLog

```angelscript
void DynamicLocationAddLog(Critter& cr, Critter& npc, GameVar& var, string file)
```

### DynamicLocationDelLog

```angelscript
void DynamicLocationDelLog(Critter& cr, Critter& npc, GameVar& var, string file)
```


