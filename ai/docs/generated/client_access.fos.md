---
title: client_access.fos
description: "Author: JohnPL Client access control..."
---

# client_access.fos

Author: JohnPL
Client access control

## Includes

- `_defines.fos`
- `client_access_h.fos`

## Classes

### ClientAccessLevel

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| accessLevel | `int` |  |  |
| gender | `int` |  |  |

**Methods**

#### setAccessLevel
```angelscript
void setAccessLevel(int level)
```

#### setPlayerGender
```angelscript
void setPlayerGender(int g)
```

#### getAccessLevel
```angelscript
int getAccessLevel()
```

#### getPlayerGender
```angelscript
int getPlayerGender()
```


## Functions

### InitAccessControl

Inicialization function

```angelscript
IClientAccessLevelOpt@ InitAccessControl()
```

### SetAccessLevel

Server call back function

```angelscript
void SetAccessLevel(int param0, int param1, int param2, string@ param3, int[]@ param4)
```

### SetGender

```angelscript
void SetGender(int param0, int param1, int param2, string@ param3, int[]@ param4)
```


