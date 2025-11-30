---
title: cavelog.fos
description: " FOnline: 2238 Rotators  cavelog.fos ..."
---

# cavelog.fos


FOnline: 2238
Rotators

cavelog.fos


## Includes

- `_macros.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| CAVE_TIME | `(REAL_HOUR(6))` | 6 hour cycle |

## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| CavesGenerated | `uint` | `0` | Script to datamine cave stuff. |
| CrittersGenerated | `uint` | `0` |  |
| CrittersKilled | `uint` | `0` |  |
| PlayerDeaths | `uint` | `0` |  |
| ItemsGenerated | `uint` | `0` |  |
| ItemsPicked | `uint` | `0` |  |

## Functions

### AddCaveGenerated

```angelscript
void AddCaveGenerated()     { CavesGenerated++; }
```

### AddCrittersGenerated

```angelscript
void AddCrittersGenerated() { CrittersGenerated++; }
```

### AddCrittersKilled

```angelscript
void AddCrittersKilled()    { CrittersKilled++; }
```

### AddPlayerDeaths

```angelscript
void AddPlayerDeaths()      { PlayerDeaths++; }
```

### AddItemsGenerated

```angelscript
void AddItemsGenerated()    { ItemsGenerated++; }
```

### AddItemsPicked

```angelscript
void AddItemsPicked()       { ItemsPicked++; }
```

### InitCaveLog

```angelscript
void InitCaveLog()
```

### CritterEnterCave

```angelscript
void CritterEnterCave(Critter& critter)
```

### ClearVariables

```angelscript
void ClearVariables()
```


