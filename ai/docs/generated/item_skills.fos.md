---
title: item_skills.fos
description: " FOnline: 2238 Rotators  item_skills.fos ..."
---

# item_skills.fos


FOnline: 2238
Rotators

item_skills.fos


## Includes

- `_macros.fos`
- `utils_h.fos`

## Classes

### ItemSkillUse

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| skill | `uint` |  |  |
| cr | `Critter@` |  |  |
| onCritter | `Critter@` |  |  |
| onItem | `Item@` |  |  |
| onScenery | `Scenery@` |  |  |


## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| EventsFunc | `FuncBind` |  |  |

## Functions

### _Init

```angelscript
void _Init(Item& item, bool firstTime)
```

### _Use

```angelscript
bool _Use(Item& item, Critter& cr, Critter@ onCritter, Item@ onItem, Scenery@ onScenery)
```

### CallEvents

[critter] used [skill] on [target critter]: [critter]: i used [skill] on target object // CRITTER_EVENT_USE_SKILL [target critter]: [critter] used [skill] on me // CRITTER_EVENT_USE_SKILL_ON_ME global: [critter] used [skill] on target object 

```angelscript
int CallEvents(IObject@ obj)
```

### ApplyToolTimeout

```angelscript
void ApplyToolTimeout(Critter& cr, int skill)
```

### s_Test

```angelscript
bool s_Test(Critter&, Scenery&, int, Item@)
```


