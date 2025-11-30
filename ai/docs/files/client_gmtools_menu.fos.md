---
title: client_gmtools_menu.fos
description: " FOnline: 2238 Rotators  client_gmtools_menu.fos ..."
---

# client_gmtools_menu.fos


FOnline: 2238
Rotators

client_gmtools_menu.fos


## Includes

- `gmtools_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __CLIENT_GMTOOLS_MENU__ |  |  |
| __CLIENT |  |  |

## Classes

### CButtonEx

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| ID | `uint` |  |  |
| RawCommand | `string` |  |  |
| ContextFlags | `int` |  |  |
| ispid | `int` |  |  |
| critter | `uint` |  |  |
| item | `uint` |  |  |
| hexX | `uint` |  |  |
| hexY | `uint` |  |  |

**Methods**

#### SetCritterAsChosen
```angelscript
void SetCritterAsChosen()
```

#### SetCritter
```angelscript
void SetCritter(uint cr)
```

#### SetItem
```angelscript
void SetItem(uint it)
```

#### SetHex
```angelscript
void SetHex(uint hx, uint hy)
```

#### Click
```angelscript
void Click()
```

### CContextMenu

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| title | `[CButton](mapper_gui.fos.md)@` |  |  |
| arranged | `int` |  |  |

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
```angelscript
void OnShow()
```

#### AddButton
```angelscript
Window@ AddButton(string caption, int context_flags, int ispid, string command)
```


## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| GMTmenu | `[CContextMenu](mapper_autowall.fos.md)` |  |  |
| GMTmenu_file | `string` | `GMT_BUTTONS_FILE` |  |

## Functions

### GMToolsLoadMenu

```angelscript
bool GMToolsLoadMenu()
```

### GMToolsLoadMenu

```angelscript
bool GMToolsLoadMenu(string filename)
```


