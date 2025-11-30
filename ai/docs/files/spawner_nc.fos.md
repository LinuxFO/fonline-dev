---
title: spawner_nc.fos
description: " --- SPAWNER FOR NOOB CAMP ---..."
---

# spawner_nc.fos


--- SPAWNER FOR NOOB CAMP ---

## Includes

- `_macros.fos`
- `utils_h.fos`
- `lockers.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __SPAWNER_NC__ |  |  |
| SPAWN_TIME | `(REAL_MINUTE(Random(1, 10)))` |  |

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

### MakeSpawnerNC

```angelscript
void MakeSpawnerNC(Item& item, bool firstTime)
```

### e_SpawnNC

```angelscript
uint e_SpawnNC(uint[] @ values)
```

### InitItemsList

```angelscript
void InitItemsList()
```


