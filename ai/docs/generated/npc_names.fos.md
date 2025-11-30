---
title: npc_names.fos
description: " FOnline: 2238 Rotators  npc_names.fos ..."
---

# npc_names.fos


FOnline: 2238
Rotators

npc_names.fos


## Includes

- `_macros.fos`
- `npc_names_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __NPC_NAMES__ |  |  |

## Functions

### GetFirstName

```angelscript
string GetFirstName(uint gender, uint index)
```

### GetRandomFirstName

```angelscript
string GetRandomFirstName(uint gender, int& index)
```

### GetRandomFirstName

```angelscript
string GetRandomFirstName(uint gender)
```

### GetNick

```angelscript
string GetNick(uint gender, uint index, bool genderNick)
```

### BaseGetRandomNick

```angelscript
string BaseGetRandomNick(uint gender, bool genderNick, int& index)
```

### GetRandomNick

```angelscript
string GetRandomNick(uint gender, bool& genderNick, int& index)
```

### GetRandomNick

```angelscript
string GetRandomNick(uint gender)
```

### GetSurname

```angelscript
string GetSurname(uint index)
```

### GetRandomSurname

```angelscript
string GetRandomSurname(int& index)
```

### GetRandomSurname

```angelscript
string GetRandomSurname()
```

### GetRandomFullName

```angelscript
string GetRandomFullName(uint gender, int& firstName, bool& genderNick, int& nick, int& surname)
```

### GetRandomFullName

```angelscript
string GetRandomFullName(uint gender)
```

### LogNames

```angelscript
void LogNames(bool printNames)
```

### lognames

```angelscript
void lognames(Critter&, int printNames, int, int)
```


