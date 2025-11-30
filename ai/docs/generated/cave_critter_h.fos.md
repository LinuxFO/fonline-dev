---
title: cave_critter_h.fos
description: " FOnline: 2238 Rotators  cave_critter_h.fos ..."
---

# cave_critter_h.fos


FOnline: 2238
Rotators

cave_critter_h.fos


## Includes

- `_macros.fos`
- `_scripts.fos`
- `cave_h.fos`
- `groups_h.fos`
- `utils_h.fos`
- `weap_anim_table_h.fos`
- `cave_critters.fos`
- `cave_groups.fos`

## Included By

- [cave.fos](cave.fos.md)

## Classes

### CaveGroup

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| critters | `array<uint>` |  |  |

**Methods**

#### AddCritters
```angelscript
ICaveGroup@ AddCritters(array<uint> critters)
```

#### GetCritters
```angelscript
array<uint> GetCritters()
```

### CaveCritter

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| bags | `array<int>` |  |  |
| bag | `int` |  |  |
| selectedbag | `int` |  |  |
| team | `int` |  |  |
| pid | `int` |  |  |
| id | `int` |  |  |
| aipack | `int` |  |  |
| script | `string` |  |  |
| level | `int` |  |  |
| difficulty | `int` |  |  |

**Methods**

#### Bag
```angelscript
ICaveCritter@ Bag(int bag)
```

#### Bag
```angelscript
ICaveCritter@ Bag(array<int> bags)
```

#### Team
```angelscript
ICaveCritter@ Team(int team)
```

#### Level
```angelscript
ICaveCritter@ Level(int level)
```

#### PID
```angelscript
ICaveCritter@ PID(int pid)
```

#### ID
```angelscript
ICaveCritter@ ID(int id)
```

#### AI
```angelscript
ICaveCritter@ AI(int aipack)
```

#### Difficulty
```angelscript
ICaveCritter@ Difficulty(int difficulty)
```

#### GetDifficulty
```angelscript
int GetDifficulty() { return difficulty; }
```

#### GetID
```angelscript
int GetID()         { return id; }
```

#### SelectBag
```angelscript
int SelectBag()
```

#### GetCost
```angelscript
uint GetCost()
```

#### Spawn
```angelscript
bool Spawn(Map@ map, uint x, uint y)
```


## Functions

### InitCritters

```angelscript
void InitCritters()
```

### InitGroups

```angelscript
void InitGroups()
```

### e_Deteriorate

```angelscript
uint e_Deteriorate(array<uint>@ values)
```

### GetCaveCritterByID

```angelscript
ICaveCritter@ GetCaveCritterByID(uint id)
```

### AddBagToBag

```angelscript
void AddBagToBag(array<int>& bag, array<int> toadd)
```

### AddCaveGroup

```angelscript
void AddCaveGroup(array<uint> critters)
```

### AddCaveCritter

```angelscript
void AddCaveCritter(uint id, uint pid, uint bag, uint aipack)
```

### AddCaveCritter

```angelscript
void AddCaveCritter(uint id, uint pid, array<int> bags, uint aipack)
```


