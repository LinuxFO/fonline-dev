---
title: reputations.fos
description: " FOnline: 2238 Rotators  reputations.fos ..."
---

# reputations.fos


FOnline: 2238
Rotators

reputations.fos


## Includes

- `reputations_h.fos`
- `utils_h.fos`

## Included By

- [town.fos](town.fos.md)

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __REPUTATIONS_MODULE__ |  |  |

## Functions

### AddReputation

* * Adds reputation points for the critter * @param     cr        Critter which reputation should increase * @param     index     Index of reputation group for which the change should occur * @param     val       Amount of points * 

```angelscript
void AddReputation(Critter@ cr, uint index, int val)
```

### SubReputation

* * Substracts reputation points for the critter * @param     cr        Critter which reputation should decrease * @param     index     Index of reputation group for which the change should occur * @param     val       Amount of points * 

```angelscript
void SubReputation(Critter@ cr, uint index, int val)
```

### AddReputation

capped versions * * Adds reputation points to the critter, but not above the specified cap * @param     cr        Critter which reputation should increase * @param     index     Index of reputation group for which the change should occur * @param     val       Amount of points * @param     cap       Maximum level beyond which the reputation won't be increased, and if it is already higher, change will not occur * 

```angelscript
void AddReputation(Critter@ cr, uint index, int val, int cap)
```

### SubReputation

* * Substracts reputation points for the critter * @param     cr        Critter which reputation should decrease * @param     index     Index of reputation group for which the change should occur * @param     val       Amount of points * @param     cap       Minimum level below which the reputation won't be increased, and if it is already lower, change will not occur * 

```angelscript
void SubReputation(Critter@ cr, uint index, int val, int cap)
```

### ReputationIndex

todo: change to use map data faction * * Checks the reputation index of the location owners * @param     locid     Location id * * @return    Reputation index 

```angelscript
uint ReputationIndex(uint locid)
```

### ProcessProfitReputation

```angelscript
void ProcessProfitReputation(Critter@ cr, uint index, int profit)
```


