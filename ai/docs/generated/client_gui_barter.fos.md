---
title: client_gui_barter.fos
description: " FOnline: 2238 Rotators  client_gui_barter.fos ..."
---

# client_gui_barter.fos


FOnline: 2238
Rotators

client_gui_barter.fos


## Included By

- [client_main.fos](client_main.fos.md)

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __CLIENT |  |  |

## Classes

### ButtonGroup

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| window | `IGUIScreenOpt@` |  | only a container child controls should implement "unclick me" on Update() by index comparison and call this.set_Selected() with own index on Click() |
| selected | `int` |  |  |

**Methods**

#### Top
```angelscript
int Top()
```

#### Left
```angelscript
int Left()
```

### FilterButton

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| group | `[ButtonGroup](client_gui_barter.fos.md)@` |  |  |
| index | `int` |  |  |
| collection | `int` |  |  |
| selected | `bool` |  |  |
| own | `bool` |  |  |
| spriteUp | `[Sprite](sprite.fos.md)` |  |  |
| spriteDown | `[Sprite](sprite.fos.md)` |  |  |

**Methods**

#### Click
```angelscript
void Click()
```

#### Update
```angelscript
void Update()
```

#### Draw
```angelscript
void Draw()
```

### BarterShow

**Methods**

#### OnShow
```angelscript
void OnShow(int p0, int p1, int p2)
```


## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| FiltersettingOwn | `int` | `-1` | used in main body |
| FiltersettingOpp | `int` | `-1` |  |
| bartershow | `[BarterShow](client_gui_barter.fos.md)@` |  |  |
| groupown | `[ButtonGroup](client_gui_barter.fos.md)@` |  |  |
| groupopp | `[ButtonGroup](client_gui_barter.fos.md)@` |  |  |

## Functions

### ParseFourInts

```angelscript
void ParseFourInts(string& str, int& v0, int& v1, int& v2, int& v3)
```

### InitBarterFilters

```angelscript
void InitBarterFilters()
```


