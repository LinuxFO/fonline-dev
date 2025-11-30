---
title: utils_for_array.fos
description: " FOnline: 2238 Rotators  utils_for_array.fos ..."
---

# utils_for_array.fos


FOnline: 2238
Rotators

utils_for_array.fos


## Included By

- [utils.fos](utils.fos.md)

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __UTILS_FOR_ARRAY__ |  |  |
| AddToArray | `# (A, V)ArrayPushBack(A, V)` |  |
| RemoveFromArray | `\` |  |
| RemoveFromArrayPtr | `\` |  |

## Functions

### FindInArray

```angelscript
int FindInArray(array<int>& arr, int value)
```

### FindInArray

```angelscript
bool FindInArray(array<int>& arr, int id, int& index)
```

### FindInArray

```angelscript
int FindInArray(array<uint>& arr, uint value)
```

### FindInArray

```angelscript
bool FindInArray(array<uint>& arr, uint id, int& index)
```

### FindInArray

```angelscript
int FindInArray(array<uint16>& arr, uint16 value)
```

### FindInArray

```angelscript
int FindInArray(array<uint8>& arr, uint8 value)
```

### FindInArray

```angelscript
bool FindInArray(array<uint8>& arr, uint8 id, int& index)
```

### FindInArray

```angelscript
int FindInArray(array<string>& arr, string& value)
```

### FindInArray

```angelscript
int FindInArray(array<string@>@ arr, string& value)
```

### Present

```angelscript
bool Present(int what, array<int>& where)
```

### Present

```angelscript
bool Present(uint what, array<uint>& where)
```

### Present

```angelscript
bool Present(uint16 what, array<uint16>& where)
```

### Present

```angelscript
bool Present(string& what, array<string>& where)
```

### Present

```angelscript
bool Present(string& what, array<string@>@ where)
```


