---
title: sprite.fos
description: " FOnline: 2238 Rotators  sprite.fos ..."
---

# sprite.fos


FOnline: 2238
Rotators

sprite.fos


## Included By

- [chosen_tabs.fos](chosen_tabs.fos.md)
- [client_container_addons.fos](client_container_addons.fos.md)
- [client_critter_onhead.fos](client_critter_onhead.fos.md)
- [client_cutscene.fos](client_cutscene.fos.md)
- [client_fef.fos](client_fef.fos.md)
- [client_gui.fos](client_gui.fos.md)
- [mapper_gui.fos](mapper_gui.fos.md)

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| _SPRITE_ |  |  |

## Classes

### Sprite

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| Id | `uint` |  |  |
| Width | `int` |  |  |
| Height | `int` |  |  |
| FrmCount | `uint` |  |  |
| Filename | `string` |  |  |

**Methods**

#### Load
```angelscript
bool Load(string& name, int path)
```

#### LoadHash
```angelscript
void LoadHash(uint nameHash, uint8 dir)
```

#### LoadByIni
```angelscript
void LoadByIni(string& iniKey, int path)
```

#### Draw
```angelscript
void Draw(int x, int y)
```


