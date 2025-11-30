---
title: item_bag_container.fos
description: " FOnline: 2238 Rotators  item_bag_container.fos ..."
---

# item_bag_container.fos


FOnline: 2238
Rotators

item_bag_container.fos


## Includes

- `_macros.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| ID | `# (item)      (item.Val4)` |  |

## Classes

### CItemBag

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| id | `uint` |  |  |
| ratemin | `uint` |  | spawn rate, ingame minutes |
| ratemax | `uint` |  |  |
| lockermin | `uint` |  |  |
| lockermax | `uint` |  |  |
| bags | `array<uint>` |  |  |
| chances | `array<uint>` |  |  |
| totalChance | `uint` |  |  |

**Methods**

#### RateMin
 Sets spawn rate, minimum time 

```angelscript
CItemBag@ RateMin(uint min)
```

#### RateMax
 Sets locker complexity, minimum value 

```angelscript
CItemBag@ RateMax(uint max)
```

#### LockerMin
```angelscript
CItemBag@ LockerMin(uint min)
```

#### LockerMax
 Sets locker complexity, maximum value 

```angelscript
CItemBag@ LockerMax(uint max)
```

#### AddBag
 Adds bag that will be spawned, with chance (cumulative) 

```angelscript
CItemBag@ AddBag(uint bagId, uint chance)
```

#### GetSpawnTime
 Time in which next spawn should occur 

```angelscript
uint GetSpawnTime()
```

#### Spawn
 Spawn items 

```angelscript
void Spawn(Item& cont)
```

#### SpawnItems
 Gets item from bag 

```angelscript
void SpawnItems(Item& cont, uint bagId)
```


## Functions

### AddItemBag

//////////////// This is where container bags properties are assigned ////////////////

```angelscript
CItemBag@ AddItemBag(uint id)
```

### item_init

```angelscript
void item_init(Item& item, bool firstTime)
```

### e_Spawn

```angelscript
uint e_Spawn(array<uint>@ values)
```

### GetItemBag

```angelscript
CItemBag@ GetItemBag(uint id)
```


