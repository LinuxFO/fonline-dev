---
title: client_spawn_npc.fos
description: " FOnline: 2238 Rotators  client_spawn_npc.fos ..."
---

# client_spawn_npc.fos


FOnline: 2238
Rotators

client_spawn_npc.fos


## Includes

- `_macros.fos`
- `cfg_file.fos`
- `client_gui_ex.fos`

## Classes

### CSpawnNpcOKButton

 Spawns critter with given params 

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| pid | `uint` |  | critter params |
| hexX | `uint16` |  |  |
| hexY | `uint16` |  |  |
| dir | `uint8` |  |  |
| dialog | `uint` |  |  |
| script | `string` |  |  |
| ai | `uint` |  |  |
| bag | `uint` |  |  |
| team | `uint` |  |  |
| mob | `uint` |  |  |
| level | `uint` |  |  |
| window | `[CSpawnNpcWindow](client_spawn_npc.fos.md)@` |  |  |

**Methods**

#### SetParams
sets params for critter to be spawned

```angelscript
void SetParams(uint pid, uint16 hexX, uint16 hexY, uint8 dir, uint dialog, string script, uint ai, uint bag, uint team, uint mob, uint level)
```

#### Click
```angelscript
void Click()
```

### CSpawnNpcCancelButton

 Closes window 

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| window | `[CSpawnNpcWindow](client_spawn_npc.fos.md)@` |  |  |

**Methods**

#### Click
```angelscript
void Click() { window.HideWindow(); }
```

### CSpawnNpcList

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| window | `[CSpawnNpcWindow](client_spawn_npc.fos.md)@` |  |  |

**Methods**

#### Click
```angelscript
void Click()
```

### CSpawnNpcScrollDown

 List scrolling 

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| list | `[CListBox](mapper_gui.fos.md)@` |  |  |

**Methods**

#### Click
```angelscript
void Click() { list.Scroll(1); }
```

### CSpawnNpcScrollUp

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| list | `[CListBox](mapper_gui.fos.md)@` |  |  |

**Methods**

#### Click
```angelscript
void Click() { list.Scroll(-1); }
```

### CSpawnNpcWindow

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| crId | `uint` |  |  |
| crits | `[CConfig](cfg_file.fos.md)@` |  |  |
| pid | `uint` |  | spawn params |
| hexX | `uint16` |  |  |
| hexY | `uint16` |  |  |
| dir | `uint8` |  |  |
| dialog | `uint` |  |  |
| script | `uint` |  |  |
| ai | `uint` |  |  |
| team | `uint` |  |  |
| bag | `uint` |  |  |
| mob | `uint` |  |  |
| level | `uint` |  |  |
| crName | `string@` |  | name (for cfg file) of the critter that'll be spawned |
| ok | `[CSpawnNpcOKButton](client_spawn_npc.fos.md)@` |  |  |
| cancel | `[CSpawnNpcCancelButton](client_spawn_npc.fos.md)@` |  |  |
| list | `[CListBox](mapper_gui.fos.md)@` |  |  |
| desc | `[CLabel](mapper_gui.fos.md)@` |  |  |
| pidTxt | `[CTextBox](mapper_gui.fos.md)@` |  |  |
| dialogTxt | `[CTextBox](mapper_gui.fos.md)@` |  |  |
| scriptTxt | `[CTextBox](mapper_gui.fos.md)@` |  |  |
| aiTxt | `[CTextBox](mapper_gui.fos.md)@` |  |  |
| teamTxt | `[CTextBox](mapper_gui.fos.md)@` |  |  |
| bagTxt | `[CTextBox](mapper_gui.fos.md)@` |  |  |
| mobTxt | `[CTextBox](mapper_gui.fos.md)@` |  |  |
| levelTxt | `[CTextBox](mapper_gui.fos.md)@` |  |  |

**Methods**

#### Init
```angelscript
void Init()
```

#### SetHex
 Sets hex coords for spawn 

```angelscript
void SetHex(uint16 hexX, uint16 hexY)
```

#### SetCritter
 Sets config name of the critter that'll b spawned 

```angelscript
void SetCritter(string@ name)
```

#### UpdateParams
 Update parameters from textboxes 

```angelscript
void UpdateParams()
```

#### Show
```angelscript
void Show()
```


