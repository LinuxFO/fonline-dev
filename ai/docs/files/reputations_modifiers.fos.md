---
title: reputations_modifiers.fos
description: " FOnline: 2238 Rotators  reputations_modifiers.fos ..."
---

# reputations_modifiers.fos


FOnline: 2238
Rotators

reputations_modifiers.fos


## Includes

- `reputations_h.fos`
- `factions_h.fos`
- `utils_h.fos`
- `reputations_tables.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __REPUTATIONS_MODULE__ |  | do not include |
| FACTION_NPC_MAX | `(100)` |  |
| IDX | `# (_x, _y)(_x * FACTION_NPC_MAX + _y)` |  |

## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| FactionUniformsDictionary | `dictionary` |  |  |
| UniformHelmetsDictionary | `dictionary` |  |  |

## Functions

### InitGroups

```angelscript
void InitGroups()
```

### ApplyReputationModifiers

```angelscript
void ApplyReputationModifiers(Critter& cr, uint index)
```

### ApplyReputationModifiers

```angelscript
void ApplyReputationModifiers(Critter& cr, uint index, float fraction)
```

### ApplyReputationModifiers

```angelscript
void ApplyReputationModifiers(Critter& cr, uint index, int num, int den)
```

### GetReputationModifier

```angelscript
int GetReputationModifier(uint fac1, uint fac2)
```

### GetUniform

```angelscript
int GetUniform(Critter& cr, int& factionOut)
```

### HasFactionUniform

```angelscript
bool HasFactionUniform(Critter& cr, int factionIn, int minStatus)
```

### GetUniformFaction

```angelscript
int GetUniformFaction(Critter& cr)
```

### GetGroupsStatus

```angelscript
int GetGroupsStatus(uint fac1, uint fac2)
```

### GetGroupsStatus

```angelscript
int GetGroupsStatus(Critter& c2, Critter& c1)
```

### ReputationsInit

```angelscript
void ReputationsInit(Critter& cr)
```

### FeedReputations

* * When there is sub of reputation of given index, there is also * raise in their enemies. Should be small, and up to some cap. 

```angelscript
void FeedReputations(Critter@ cr, uint index, int cap)
```


