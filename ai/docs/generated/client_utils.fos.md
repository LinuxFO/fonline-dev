---
title: client_utils.fos
description: " FOnline: 2238 Rotators  client_utils.fos ..."
---

# client_utils.fos


FOnline: 2238
Rotators

client_utils.fos


## Includes

- `_client_defines.fos`
- `_macros.fos`
- `_colors.fos`
- `strtoint_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __CLIENT_UTILS__ |  |  |

## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| newLine | `bool` | `true` |  |
| currentLine | `string` | `""` |  |
| currentWidth | `int` | `0, ignored = 0` |  |
| wordWidth | `int` | `0` |  |

## Functions

### COLOR_RGB_STRING

```angelscript
uint COLOR_RGB_STRING(string& r, string& g, string& b)
```

### COLOR_RGBA_STRING

```angelscript
uint COLOR_RGBA_STRING(string& r, string& g, string& b, string& a)
```

### COLOR_RGB_UNPACK

```angelscript
void COLOR_RGB_UNPACK(uint color, uint8& r, uint8& g, uint8& b)
```

### COLOR_RGB_UNPACK

```angelscript
void COLOR_RGB_UNPACK(uint color, uint8& r, uint8& g, uint8& b, uint8& a)
```

### string2bool

```angelscript
bool string2bool(string@ text)
```

### string2uint

```angelscript
uint string2uint(string@ text)
```

### string2int

```angelscript
int string2int(string& text)
```

### rgb_string2uint

```angelscript
uint rgb_string2uint(string& text)
```

### rgba_string2uint

```angelscript
uint rgba_string2uint(string& text)
```

### font_string2uint

```angelscript
uint font_string2uint(string& text)
```

### fontex_string2uint

```angelscript
uint fontex_string2uint(string& text)
```

### range_string2uint

returns: 0 - nothing was changed 1 - 'from' and 'to' set to same value : "5" -> 5, 5 2 - 'from' and 'to' set to different values : "5 10" -> 5, 10

```angelscript
uint range_string2uint(string& text, uint& from, uint& to)
```

### range_string2int

returns: 0 - nothing was changed 1 - 'from' and 'to' set to same value : "5" -> 5, 5 2 - 'from' and 'to' set to different values : "-5 10" -> -5, 10

```angelscript
uint range_string2int(string& text, int& from, int& to)
```

### vis_string2bool

```angelscript
void vis_string2bool(string& text, bool& head, bool& msgbox)
```

### RandomString

```angelscript
string RandomString(uint8 length)
```


