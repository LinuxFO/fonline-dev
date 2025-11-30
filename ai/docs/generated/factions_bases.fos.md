---
title: factions_bases.fos
description: " FOnline: 2238 Rotators  factions_bases.fos ..."
---

# factions_bases.fos


FOnline: 2238
Rotators

factions_bases.fos


## Includes

- `_macros.fos`
- `factions_h.fos`
- `factions_bases_h.fos`
- `serializator.fos`
- `mapdata_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __FACTIONS_BASES_MODULE__ |  |  |
| KEY | `# (fid, fname)("" + fid + "_" + fname)` | key for indices dictionary |

## Classes

### FactionBase

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| factionId | `uint` |  |  |
| locationId | `uint` |  |  |
| name | `string` |  |  |

**Methods**

#### get_FactionId
```angelscript
uint          get_FactionId() const  { return this.factionId; }
```

#### get_LocationId
```angelscript
uint          get_LocationId() const { return this.locationId; }
```

#### get_Id
unique id

```angelscript
uint get_Id() const
```

#### Show
shows the base location to player

```angelscript
void Show(Critter& cr) const
```

#### Hide
hides the base location from player

```angelscript
void Hide(Critter& cr) const
```

#### IsRankAllowed
checks whether given rank (from owning faction) has access to the base

```angelscript
bool IsRankAllowed(int rank) const
```

#### AllowRank
sets whether given rank can access the base

```angelscript
void AllowRank(int rank, bool allow)
```

#### IsStatusAllowed
```angelscript
bool IsStatusAllowed(int status) const
```

#### AllowStatus
```angelscript
void AllowStatus(int status, bool allow)
```

#### Remove
```angelscript
void Remove()
```


## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| Indices | `dictionary` |  | various indices dictionaries |
| ByLocId | `dictionary` |  |  |
| ById | `dictionary` |  |  |
| ByFaction | `dictionary` |  |  |

## Functions

### GetFactionBase

* * Retrieves IFactionBase object for a named base belonging to given faction. 

```angelscript
IFactionBase@ GetFactionBase(uint faction_id, const string& name)
```

### GetFactionBase

* * Retrieves IFactionBase object for a base with given id. 

```angelscript
IFactionBase@ GetFactionBase(uint id)
```

### GetFactionBaseByLocId

* * Retrieves IFactionBase object for a base with location with given id. 

```angelscript
IFactionBase@ GetFactionBaseByLocId(uint id)
```

### GetFactionBases

* * Retrieves list of IFactionBase objects representing all bases belonging to given faction. * @return Number of bases retrieved. 

```angelscript
uint GetFactionBases(uint faction_id, array<IFactionBase@>@ bases)
```

### AddFactionBase

* * Adds IFactionBase object to the internal list of bases. 

```angelscript
bool AddFactionBase(IFactionBase& base)
```

### AddFactionBase

* * Adds IFactionBase object created basing on the id of the existing location. 

```angelscript
void AddFactionBase(uint location_id)
```

### CreateFactionBase

* * Creates new faction base object for existing location. * @return Interface to newly created object. 

```angelscript
IFactionBase@ CreateFactionBase(uint faction_id, const string& name, uint location_id)
```

### RemoveFactionBase

* * Removes IFactionBase object representing a faction base with given name. 

```angelscript
void RemoveFactionBase(uint faction_id, const string& name)
```

### RemoveFactionBase

```angelscript
void RemoveFactionBase(IFactionBase& base)
```

### createbase

```angelscript
void createbase(Critter& player, int s, int, int)
```

### listfactionbases

```angelscript
void listfactionbases(Critter& cr, int, int, int)
```

### list

```angelscript
void list(Critter& cr, int, int, int)
```

### test_bases

```angelscript
void test_bases()
```

### test_bases_visibility

```angelscript
void test_bases_visibility()
```


