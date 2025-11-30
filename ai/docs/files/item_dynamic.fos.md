---
title: item_dynamic.fos
description: " FOnline: 2238 Rotators  item_dynamic.fos ..."
---

# item_dynamic.fos


FOnline: 2238
Rotators

item_dynamic.fos


## Includes

- `_defines.fos`
- `_macros.fos`
- `_vals.fos`
- `item_dynamic_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __ITEM_DYNAMIC__ |  |  |
| ITEM_DYNAMIC_REALPID | `# (_item)                    _item.Val5` |  |
| ITEM_DYNAMIC_REALPID_SET | `# (_item, _pid)ITEM_DYNAMIC_REALPID(_item) = _pid` |  |
| ITEM_DYNAMIC_REALPID_REMOVE | `# (_item)             ITEM_DYNAMIC_REALPID(_item) = _item.Proto.StartValue_5` |  |

## Functions

### item_init

```angelscript
void item_init(Item& item, bool firstTime)
```

### IsDynamicItem

```angelscript
bool IsDynamicItem(Item& item)
```

### IsDynamicItem

```angelscript
bool IsDynamicItem(Item& item, uint16 pid)
```

### ContainsDynamicItems

```angelscript
bool ContainsDynamicItems(Location& location, uint16 pid)
```

### ContainsDynamicItems

```angelscript
bool ContainsDynamicItems(Map& map, uint16 pid)
```

### ShowAllDynamicItems

```angelscript
void ShowAllDynamicItems(Location& location, uint16 pid)
```

### ShowAllDynamicItems

```angelscript
void ShowAllDynamicItems(Map& map, uint16 pid)
```

### ShowAllDynamicItems

```angelscript
void ShowAllDynamicItems(Location& location, uint16 pid, uint& found, uint& shown)
```

### ShowAllDynamicItems

```angelscript
void ShowAllDynamicItems(Map& map, uint16 pid, uint& found, uint& shown)
```

### ShowDynamicItem

```angelscript
bool ShowDynamicItem(Item& item)
```


