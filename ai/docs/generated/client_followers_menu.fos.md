---
title: client_followers_menu.fos
description: " FOnline: 2238 Rotators  client_followers_menu.fos ..."
---

# client_followers_menu.fos


FOnline: 2238
Rotators

client_followers_menu.fos


## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| SKIP_PRAGMAS |  |  |
| __CLIENT |  | Compile with -client switch |

## Classes

### CFollowersAttackButton

**Methods**

#### Click
 Performs action depending on attached critter/item 

```angelscript
void Click()
```

### CFollowersAttackHPButton

**Methods**

#### Click
 Performs action depending on attached critter/item 

```angelscript
void Click()
```

### CFollowersMoveToButton

**Methods**

#### Click
```angelscript
void Click()
```

### CFollowersMoveToHPButton

**Methods**

#### Click
```angelscript
void Click()
```

### CFollowersStopButton

**Methods**

#### Click
```angelscript
void Click()
```

### CFollowersFollowButton

**Methods**

#### Click
```angelscript
void Click()
```

### CFollowersRegroupButton

**Methods**

#### Click
```angelscript
void Click()
```

### CFollowersFleeButton

**Methods**

#### Click
```angelscript
void Click()
```

### CFollowersMoveManualButton

**Methods**

#### Click
```angelscript
void Click()
```

### CFollowersMoveAutoButton

**Methods**

#### Click
```angelscript
void Click()
```

### CFollowersPushButton

**Methods**

#### Click
 Performs action depending on attached critter/item 

```angelscript
void Click()
```

### CFollowersContextMenu

 Right-click context menu 

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| title | `[CButton](mapper_gui.fos.md)@` |  |  |
| attack | `[CFollowersAttackButton](client_followers_menu.fos.md)@` |  |  |
| attackHP | `[CFollowersAttackHPButton](client_followers_menu.fos.md)@` |  |  |
| moveTo | `[CFollowersMoveToButton](client_followers_menu.fos.md)@` |  |  |
| moveToHP | `[CFollowersMoveToHPButton](client_followers_menu.fos.md)@` |  |  |
| stop | `[CFollowersStopButton](client_followers_menu.fos.md)@` |  |  |
| regroup | `[CFollowersRegroupButton](client_followers_menu.fos.md)@` |  | CFollowersFollowButton@ follow; |
| flee | `[CFollowersFleeButton](client_followers_menu.fos.md)@` |  |  |
| moveManual | `[CFollowersMoveManualButton](client_followers_menu.fos.md)@` |  |  |
| moveAuto | `[CFollowersMoveAutoButton](client_followers_menu.fos.md)@` |  |  |
| pushcr | `[CFollowersPushButton](client_followers_menu.fos.md)@` |  |  |

**Methods**

#### Init
```angelscript
void Init()
```

#### Width
```angelscript
int Width() { return title.Width(); }
```

#### OnShow
 Shows drop down for given coords 

```angelscript
void OnShow()
```


## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| movemanual | `bool` |  |  |
| FollowersMenu | `[CFollowersContextMenu](client_followers_menu.fos.md)` |  |  |

## Functions

### InitFollowersMenu

```angelscript
void InitFollowersMenu()
```


