---
title: production.fos
description: " FOnline: 2238 Rotators  production.fos ..."
---

# production.fos


FOnline: 2238
Rotators

production.fos


## Includes

- `production_h.fos`
- `utils_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __PRODUCTION_MODULE__ |  |  |
| TIMEOUT_CUMULATIVE | `(int(REAL_MINUTE(20)))` | cumulative timeout |
| SET_TIMEOUT | `# (cr, to)     { cr.TimeoutBase[TO_GATHERING] = __FullSecond + cr.Timeout[TO_GATHERING] + REAL_SECOND(to); }` | gathering timeout |

## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| RegenCounters | `dictionary` |  | every resource that's subject to regeneration increases this global counter so that we can later determine weight when regenerating particular facility |
| counter | `uint` |  | and global counters |
| is_container | `bool` | `item.GetType() == ITEM_TYPE_CONTAINER` |  |

## Functions

### InitProduction

```angelscript
void InitProduction()
```

### GetRegenerationAmount

* * Retrieves the amount of resources that should be injected into given facility. 

```angelscript
uint GetRegenerationAmount(uint16 pid, int counter, uint pool, uint facility_count)
```

### Regenerate

```angelscript
void Regenerate(Item& item, uint16 pid, int capacity, uint pool, int total_count)
```

### ReduceCounter

```angelscript
void ReduceCounter(uint16 pid, int value)
```

### IsOverweighted

* * Checks if critter carries too much. 

```angelscript
bool IsOverweighted(Critter& cr)
```

### CheckPrimitiveTool

```angelscript
void CheckPrimitiveTool(Critter& crit, Item& item)
```

### get_RegenerationInterval

```angelscript
uint get_RegenerationInterval()
```

### e_Unhide

'respawns' item

```angelscript
uint e_Unhide(array<uint>@ values)
```

### SetAmountOfResources

```angelscript
void SetAmountOfResources(array<Item@>& spots, int total_value)
```

### GetFacilities

```angelscript
uint GetFacilities(const Map& map, string@ script_name, array<Item@>& spots)
```

### IsMineDepleted

* * Checks iron and minerals facilities and their amounts. 

```angelscript
bool IsMineDepleted(Map& map)
```


