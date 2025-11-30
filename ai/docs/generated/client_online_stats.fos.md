---
title: client_online_stats.fos
description: " FOnline: 2238 Rotators  client_online_stats.fos ..."
---

# client_online_stats.fos


FOnline: 2238
Rotators

client_online_stats.fos


## Includes

- `_colors.fos`
- `client_gui_h.fos`
- `client_gui_ex.fos`
- `client_utils_h.fos`
- `online_stats_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __CLIENT_ONLINE_STATS__ |  |  |
| __ONLINE_STATS_MODULE__ |  |  |
| OSM_NONE | `(0)` |  |
| OSM_VTDB | `(1)` |  |
| OS_MSG_NONE | `("Nothing will be available to view by other players.")` |  |
| OS_MSG_DEFAULT | `(" ")` |  |
| OS_MSG_OK | `("Click to send current settings.")` | ("Current settings:\n\nLocal: "+OnlineStatsBuffer+"\nServer:"+OnlineStats) |
| OS_MSG_CANCEL | `("Click to abandon all changes.")` |  |
| OS_MSG_LINK | `("Click to visit this page:\n\n" + this.msg)` |  |
| OS_MSG_URL | `("http:` |  |
| OS_MSG_URL_ID | `("%ID%")` |  |
| OS_MSG_URL_CHAR | `("char.php?" + OS_MSG_URL_ID)` |  |
| OS_MSG_VTDB_ALL | `("All informations will be available to view.\n\nRemember that this flag will be used for things added in future.")` |  |
| OS_MSG_VTDB_SPECIAL | `("Display character SPECIAL points")` |  |
| OS_MSG_VTDB_XP | `("Display character level, current experience, and points needed for next level")` |  |
| OS_MSG_VTDB_LIFE | `("Display hit points and body status")` |  |
| OS_MSG_VTDB_STATS | `("Display character statistics")` |  |
| OS_MSG_VTDB_SKILLS | `("Display character skills")` |  |
| OS_MSG_VTDB_TRAITS | `("Display character traits")` |  |
| OS_MSG_VTDB_PERKS | `("Display character perks")` |  |
| OS_MSG_VTDB_PROFESSIONS | `("Display character professions")` |  |
| OS_MSG_VTDB_KARMA | `("Display character karma")` |  |
| OS_MSG_VTDB_ADDICTIONS | `("Display character addictions")` |  |
| OS_MSG_VTDB_REPUTATION | `("Display character reputation")` |  |
| OS_MSG_VTDB_KILLS | `("Display how many creatures meet its creator, thanks to You")` |  |
| OS_MSG_VTDB_POSITION | `("OS_POSITION - should !be visible")` |  |
| OS_MSG_BOK | `("OK")` |  |
| OS_MSG_BCANCEL | `("Cancel")` |  |
| OS_MSG_BCHARPAGE | `("Character page")` |  |
| OS_MSG_BHOMEPAGE | `("VTDB Homepage")` |  |
| OS_MSG_INSECT | `("Online")` |  |
| OS_INIPREFIX | `("OnlineStats")` |  |
| OS_INI | `# (key)           (OS_INIPREFIX + key)` |  |
| OS_INISTR | `# (key)        (GetIfaceIniStr(OS_INI(key)))` |  |
| OSB_NORMAL | `(0)` | buttons types |
| OSB_TOGGLE | `(1)` |  |
| OSB_ARROW | `(2)` |  |
| OSB_LINK | `(3)` |  |
| OSB_LINK_NORMAL | `(0)` | link flag |
| OSB_LINK_CHAR | `(1)` |  |
| OSB_LINK_CHAROK | `(2)` |  |
| _draw | `\` |  |

## Classes

### COSButton

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| mod | `int` |  | universal |
| ID | `int` |  |  |
| type | `int` |  |  |
| sType | `string` |  |  |
| name | `string` |  |  |
| spriteUp | `[Sprite](sprite.fos.md)` |  |  |
| spriteDown | `[Sprite](sprite.fos.md)` |  |  |
| label | `[CLabel](mapper_gui.fos.md)@` |  |  |
| callback | `CALLBACK@` |  |  |
| page | `int` |  |  |
| flag | `int` |  |  |
| msg | `string` |  |  |
| state | `bool` |  | OSB_TOGGLE |
| color_on | `uint` |  | OSB_NORMAL / OSB_TOGGLE / OSB_LINK |
| color_off | `uint` |  |  |

**Methods**

#### Init
```angelscript
void Init()
```

#### OnShow
```angelscript
void OnShow()
```

#### OnHide
```angelscript
void OnHide()
```

#### OnEnabled
```angelscript
void OnEnabled()
```

#### OnDisabled
```angelscript
void OnDisabled()
```

#### SetClick
```angelscript
void SetClick(CALLBACK@ callback)
```

#### Click
```angelscript
void Click()
```

#### MouseMove
```angelscript
void MouseMove(int fromX, int fromY, int toX, int toY)
```

#### SetCaption
```angelscript
void SetCaption(string caption)
```

#### SetColor
```angelscript
void SetColor(uint color)
```

#### SetFormat
```angelscript
void SetFormat(uint format)
```

#### Draw
```angelscript
void Draw()
```

### COnlineStatsWindow

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| title | `[CLabel](mapper_gui.fos.md)@` |  |  |
| infobox | `[CLabel](mapper_gui.fos.md)@` |  |  |
| infoboxUpdate | `uint` |  |  |
| infoboxID | `int` |  |  |
| pageInfo | `[CLabel](mapper_gui.fos.md)@` |  |  |
| page | `int` |  |  |
| pages | `int` |  |  |
| Author | `[CLabel](mapper_gui.fos.md)@` |  |  |
| mouseMove | `bool` |  |  |

**Methods**

#### Init
```angelscript
void Init()
```

#### OnShow
```angelscript
void OnShow()
```

#### OnHide
```angelscript
void OnHide(int, int, int)
```

#### MouseMove
```angelscript
void MouseMove(int fromX, int fromY, int toX, int toY)
```

### InjectButton

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| window | `IGUIScreenOpt@` |  |  |
| infected | `bool` |  |  |
| buttonDown | `[Sprite](sprite.fos.md)` |  |  |
| pos | `array<int>` |  |  |

**Methods**

#### Init
```angelscript
void Init()
```

#### Click
```angelscript
void Click()
```

#### Left
```angelscript
int Left()
```

#### Top
```angelscript
int Top()
```

#### Draw
```angelscript
void Draw()
```


## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| OnlineStats | `int` | `0` |  |
| OnlineStatsBuffer | `int` | `0` |  |
| OS_GUI | `bool` | `true` |  |
| OnlineStatsWindow | `[COnlineStatsWindow](client_online_stats.fos.md)` |  |  |
| initialized | `bool` | `false` |  |

## Functions

### cb_mouseMove

```angelscript
void cb_mouseMove(COSButton@ button)
```

### cb_nop

```angelscript
void cb_nop(COSButton@ button)
```

### cb_ok

```angelscript
void cb_ok(COSButton@ button)
```

### cb_cancel

```angelscript
void cb_cancel(COSButton@ button)
```

### cb_toggleButton

```angelscript
void cb_toggleButton(COSButton@ button)
```

### cb_arrow

```angelscript
void cb_arrow(COSButton@ button)
```

### cb_url

```angelscript
void cb_url(COSButton@ button)
```

### InitOnlineStats

```angelscript
void InitOnlineStats()
```

### OnlineStatsCommand

```angelscript
int OnlineStatsCommand(string& message)
```

### OnlineStatsGetSetup

```angelscript
void OnlineStatsGetSetup()
```

### SendSetup

```angelscript
void SendSetup(int setup)
```

### _Setup

* * 

```angelscript
void _Setup(int setup, int display, int, string@, array<int>@)
```


