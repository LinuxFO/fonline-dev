---
title: cave_item_h.fos
description: " FOnline: 2238 Rotators  cave_item_h.fos ..."
---

# cave_item_h.fos


FOnline: 2238
Rotators

cave_item_h.fos


## Includes

- `_macros.fos`
- `cave_h.fos`
- `cave_items.fos`

## Included By

- [cave.fos](cave.fos.md)

## Classes

### CaveItem

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| pid | `uint` |  |  |
| chance | `uint` |  |  |
| luckrequirement | `uint` |  |  |
| group | `uint` |  |  |

**Methods**

#### PID
```angelscript
ICaveItem@ PID(uint pid)
```

#### Group
```angelscript
ICaveItem@ Group(uint group)
```

#### Chance
Chance from 0-100

```angelscript
ICaveItem@ Chance(uint chance)
```

#### LuckRequirement
Min luck required to find item

```angelscript
ICaveItem@ LuckRequirement(uint luckrequirement)
```

#### GetLuckRequirement
```angelscript
uint GetLuckRequirement() { return luckrequirement; }
```

#### GetChance
```angelscript
uint GetChance()          { return chance; }
```

#### GetPID
```angelscript
uint GetPID()             { return pid; }
```

#### GetGroup
```angelscript
uint GetGroup()           { return group; }
```

#### AddItemToMap
```angelscript
void AddItemToMap(Map@ map, uint x, uint y)
```


## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| cur_group | `uint` |  |  |

## Functions

### InitItems

```angelscript
void InitItems()
```

### AddCaveItem

```angelscript
void AddCaveItem(uint pid, uint chance, uint luckrequirement)
```

### SetGroup

```angelscript
void SetGroup(uint group)
```


