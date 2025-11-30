---
title: mercs.fos
description: " FOnline: 2238 Rotators  mercs.fos ..."
---

# mercs.fos


FOnline: 2238
Rotators

mercs.fos


## Includes

- `_macros.fos`
- `_bags.fos`
- `mercs_h.fos`
- `_ai.fos`
- `follower_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| ADD_MERC | `# (name, properties) CMerc name(); name.properties; AddMerc(name)` |  |
| MERC_UPDATE_INTERVAL | `(REAL_DAY(9999))` |  |
| MERC_MIN_COST | `(50)` |  |

## Functions

### GetMerc

```angelscript
IMerc@ GetMerc(uint id)
```

### GetMercId

```angelscript
int GetMercId(int pid, uint type)
```

### AddMerc

```angelscript
void AddMerc(CMerc& merc)
```

### e_UpdateMercPrices

```angelscript
uint e_UpdateMercPrices(array<uint>@ values)
```

### InitMercs

Here we add our mercs, increment each new prototype's id with 1 (.ID(<previous merc's id+1>))

```angelscript
void InitMercs()
```


