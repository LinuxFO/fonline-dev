---
title: client_dev_menu.fos
description: " FOnline: 2238 Rotators  client_dev_menu.fos ..."
---

# client_dev_menu.fos


FOnline: 2238
Rotators

client_dev_menu.fos


## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| SKIP_PRAGMAS |  |  |
| __CLIENT |  | developer's menu Compile with -client switch |

## Classes

### CKillerButton

 Kills/revives critter 

**Methods**

#### SetCritter
```angelscript
void SetCritter(CritterCl@ cr)
```

#### Click
 Performs action depending on attached critter/item 

```angelscript
void Click()
```

### CNeutralizeButton

 Knocks out critter 

**Methods**

#### SetCritter
```angelscript
void SetCritter(CritterCl@ cr)
```

#### Click
 Performs action depending on attached critter/item 

```angelscript
void Click()
```

### CCleanButton

 Removes critter/item 

**Methods**

#### SetCritter
```angelscript
void SetCritter(CritterCl@ cr)
```

#### SetItem
```angelscript
void SetItem(ItemCl@ item)
```

#### Click
 Performs removal depending on attached critter/item 

```angelscript
void Click()
```

### CPossessButton

**Methods**

#### Click
```angelscript
void Click()
```

### CPickButton

 Issue pick plan for possessed critter 

**Methods**

#### Click
```angelscript
void Click()
```

### CAttackButton

**Methods**

#### Click
```angelscript
void Click()
```

### CMoveToButton

 Issues walk plan 

**Methods**

#### Click
```angelscript
void Click()
```

### CStopButton

 Cancels all plans 

**Methods**

#### Click
```angelscript
void Click()
```

### CTradeButton

 Container/critter equipment browsing 

**Methods**

#### SetCritter
```angelscript
void SetCritter(CritterCl@ cr)
```

#### SetItem
```angelscript
void SetItem(ItemCl@ item)
```

#### Click
 Shows appropriate inv window depending on attached critter/item 

```angelscript
void Click()
```

### CTeleportButton

 Teleport to hex 

**Methods**

#### Click
```angelscript
void Click()
```

### CAirstrikeButton

 Drop airstrike on hex 

**Methods**

#### Click
```angelscript
void Click()
```

### CXpButton

 Xp reward button 

**Methods**

#### Click
```angelscript
void Click()
```

### CXpOKButton

 Xp reward window 

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| window | `[CXpWindow](client_dev_menu.fos.md)@` |  |  |

**Methods**

#### Click
```angelscript
void Click()
```

### CXpCancelButton

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| window | `[CXpWindow](client_dev_menu.fos.md)@` |  |  |

**Methods**

#### Click
```angelscript
void Click() { parent.HideWindow(); }
```

### CXpWindow

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| message | `[CTextBox](mapper_gui.fos.md)@` |  |  |
| amount | `[CTextBox](mapper_gui.fos.md)@` |  |  |
| ok | `[CXpOKButton](client_dev_menu.fos.md)@` |  |  |
| cancel | `[CXpCancelButton](client_dev_menu.fos.md)@` |  |  |
| crId | `uint` |  |  |

**Methods**

#### Init
```angelscript
void Init()
```

#### CrId
 Properties 

```angelscript
uint CrId() { return crId; }
```

#### Xp
```angelscript
uint Xp()
```

#### Message
```angelscript
string@ Message() { return message.Text(); }
```

#### SetCritter
```angelscript
void SetCritter(uint crId) { this.crId = crId; }
```

#### OnShow
```angelscript
void OnShow()
```

### CSpawnNpcButton

 Spawn npc button 

**Methods**

#### Click
```angelscript
void Click()
```

### CContextMenu

 Right-click context menu 

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| title | `[CButton](mapper_gui.fos.md)@` |  |  |
| killer | `[CKillerButton](client_dev_menu.fos.md)@` |  |  |
| possess | `[CPossessButton](client_dev_menu.fos.md)@` |  |  |
| clean | `[CCleanButton](client_dev_menu.fos.md)@` |  |  |
| trade | `[CTradeButton](client_dev_menu.fos.md)@` |  |  |
| teleport | `[CTeleportButton](client_dev_menu.fos.md)@` |  |  |
| airstrike | `[CAirstrikeButton](client_dev_menu.fos.md)@` |  |  |
| xp | `[CXpButton](client_dev_menu.fos.md)@` |  |  |
| spawnNpc | `[CSpawnNpcButton](client_dev_menu.fos.md)@` |  |  |
| pick | `[CPickButton](client_dev_menu.fos.md)@` |  | possess mode buttons |
| attack | `[CAttackButton](client_dev_menu.fos.md)@` |  |  |
| moveTo | `[CMoveToButton](client_dev_menu.fos.md)@` |  |  |
| stop | `[CStopButton](client_dev_menu.fos.md)@` |  |  |
| neutralize | `[CNeutralizeButton](client_dev_menu.fos.md)@` |  |  |

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
* * Sets controls visibility depending on the context. 

```angelscript
void OnShow()
```


## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| Authorized | `bool` | `false` | for devmenu (can be hacked, but it really doesn't change anything) |
| DevMenu | `[CContextMenu](mapper_autowall.fos.md)` |  | global window controls |
| XpWindow | `[CXpWindow](client_dev_menu.fos.md)` |  |  |
| SpawnWindow | `[CSpawnNpcWindow](client_spawn_npc.fos.md)` |  |  |
| PossessedCritterId | `uint` |  | GLOBAL id of 'possessed' critter |

## Functions

### IsAuthorized

```angelscript
bool IsAuthorized() { return Authorized; }
```

### Authorize

```angelscript
void Authorize(int p0, int p1, int p2, string@ + p3, array<int>@ + p4)
```

### InitDevMenu

```angelscript
void InitDevMenu()
```

### DevMenuProcessKey

```angelscript
bool DevMenuProcessKey(uint8 key)
```

### GetPossessedCritterId

```angelscript
uint GetPossessedCritterId() { return PossessedCritterId; }
```

### IsPossessMode

 global check if possessed mode is on 

```angelscript
bool IsPossessMode()
```

### Unpossess

 Disables possess mode 

```angelscript
void Unpossess()
```


