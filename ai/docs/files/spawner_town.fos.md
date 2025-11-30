---
title: spawner_town.fos
description: " --- SPAWNER FOR SAFE TOWNS ---..."
---

# spawner_town.fos


--- SPAWNER FOR SAFE TOWNS ---

## Includes

- `_macros.fos`
- `utils_h.fos`
- `lockers.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __SPAWNER_TOWN__ |  |  |
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

### MakeSpawnerTown

```angelscript
void MakeSpawnerTown(Item& item, bool firstTime)
```

### e_SpawnTown

```angelscript
uint e_SpawnTown(uint[] @ values)
```

### InitItemsList

```angelscript
void InitItemsList()
```


