---
title: spawner_ntown.fos
description: " --- SPAWNER FOR UNSAFE TOWNS ---..."
---

# spawner_ntown.fos


--- SPAWNER FOR UNSAFE TOWNS ---

## Includes

- `_macros.fos`
- `utils_h.fos`
- `lockers.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __SPAWNER_NTOWN__ |  |  |
| SPAWN_TIME | `(REAL_MINUTE(Random(5, 60)))` |  |

## Classes

### SpawnItem

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| pid | `uint` |  |  |
| minCount | `uint` |  |  |
| maxCount | `uint` |  |  |


## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| Init | `bool` | `false` |  |

## Functions

### MakeSpawnerNTown

```angelscript
void MakeSpawnerNTown(Item& item, bool firstTime)
```

### e_SpawnNTown

```angelscript
uint e_SpawnNTown(uint[] @ values)
```

### InitItemsList

```angelscript
void InitItemsList()
```


