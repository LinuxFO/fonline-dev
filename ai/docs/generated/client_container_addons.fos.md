---
title: client_container_addons.fos
description: " FOnline: 2238 Rotators  client_container_volume.fos ..."
---

# client_container_addons.fos


FOnline: 2238
Rotators

client_container_volume.fos


## Includes

- `_client_defines.fos`
- `_macros.fos`
- `client_gui_h.fos`
- `client_gui_ex.fos`
- `sprite.fos`

## Classes

### InjectLabel

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| window | `IGUIScreenOpt@` |  |  |
| backgroundPic | `[Sprite](sprite.fos.md)` |  | bool infected; |
| picControl | `[Control](mapper_gui.fos.md)@` |  |  |

**Methods**

#### PicPosition
```angelscript
void PicPosition(string& ini)
```

#### TextPosition
```angelscript
void TextPosition(string& ini)
```

#### Left
```angelscript
int Left()
```

#### PicLeft
```angelscript
int PicLeft()
```

#### Top
```angelscript
int Top()
```

#### PicTop
```angelscript
int PicTop()
```

#### Draw
```angelscript
void Draw()
```

### InjectPutAllButton

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| window | `IGUIScreenOpt@` |  |  |
| buttonDown | `[Sprite](sprite.fos.md)` |  |  |

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

### InjectTakeAllButton

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| window | `IGUIScreenOpt@` |  |  |
| buttonDown | `[Sprite](sprite.fos.md)` |  |  |

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

### ButtonGroupPickup

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

### PickupFilterButton

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| group | `[ButtonGroupPickup](client_container_addons.fos.md)@` |  |  |
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

### PickupShow

**Methods**

#### OnShow
```angelscript
void OnShow(int p0, int p1, int p2)
```


## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| insect | `[InjectLabel](client_container_addons.fos.md)@` |  |  |
| itemsVolume | `int` | `0` |  |
| containerVolume | `int` | `0` |  |
| indicatorLabel | `string` |  |  |
| containerId | `uint` |  |  |
| bodyId | `uint` |  |  |
| pickupShow | `[PickupShow](client_container_addons.fos.md)@` |  |  |
| pickupGroupOwn | `[ButtonGroupPickup](client_container_addons.fos.md)@` |  |  |
| pickupGroupOpp | `[ButtonGroupPickup](client_container_addons.fos.md)@` |  |  |
| pickupFilterOwn | `int` | `-1` |  |
| pickupFilterOpp | `int` | `-1` |  |
| disableItemMove | `bool` | `false` |  |

## Functions

### GetPickupFilterOwn

```angelscript
int GetPickupFilterOwn()
```

### GetPickupFilterOpp

```angelscript
int GetPickupFilterOpp()
```

### GetContainerId

```angelscript
uint GetContainerId()
```

### GetBodyId

```angelscript
uint GetBodyId()
```

### SetContainerBodyId

```angelscript
void SetContainerBodyId(uint cId, uint bId)
```

### UpdateCaption

```angelscript
void UpdateCaption()
```

### HideVolumeIndicator

```angelscript
void HideVolumeIndicator()
```

### ZeroVolumeFillIndicator

```angelscript
void ZeroVolumeFillIndicator()
```

### SetVolumeFillIndicator

```angelscript
void SetVolumeFillIndicator(array<ItemCl@> items)
```

### SetVolumeIndicator

```angelscript
void SetVolumeIndicator(uint pid)
```

### InitContainerAddons

```angelscript
void InitContainerAddons()
```

### _EnableItemsMove

```angelscript
void _EnableItemsMove(int param1, int param2, int param3, string@ param4, array<int>@ param5)
```

### ExecutePutAll

```angelscript
void ExecutePutAll()
```

### ExecuteTakeAll

```angelscript
void ExecuteTakeAll()
```

### ParseFourInts

```angelscript
void ParseFourInts(string& str, int& v0, int& v1, int& v2, int& v3)
```


