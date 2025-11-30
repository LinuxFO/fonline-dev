---
title: factions.fos
description: " FOnline: 2238 Rotators  factions.fos ..."
---

# factions.fos


FOnline: 2238
Rotators

factions.fos


## Includes

- `_macros.fos`
- `factions_h.fos`
- `factions_bases_h.fos`
- `faction_data.fos`
- `logging_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __FACTIONS_MODULE__ |  |  |
| UPDATE_FACTIONS_INTERVAL | `(2000)` |  |

## Classes

### Faction

ok, basic Faction info is here

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| id | `int` |  |  |
| name | `string` |  |  |
| database | `string` |  |  |
| update_seq | `int` |  | number describing last change in database |
| data | `[FactionData](faction_data.fos.md)@` |  | underlying FactionData object - used till we scrap it in favor of external db |

**Methods**

#### get_Id
```angelscript
int    get_Id() const       { return this.id; }
```

#### get_Name
```angelscript
string get_Name() const     { return this.name; }
```

#### get_StringId
```angelscript
int    get_StringId() const { return this.data.stringId; }
```

#### get_Database
```angelscript
string get_Database() const { return this.database; }
```

#### get_UpdateSeq
int get_UpdateSeq() const { return this.update_seq; } void set_UpdateSeq(int val) { this.update_seq = val; }

```angelscript
int  get_UpdateSeq() const  { return this.data.update_seq; }
```

#### set_UpdateSeq
```angelscript
void set_UpdateSeq(int val) { this.data.update_seq = val; }
```

#### GetRank
```angelscript
int GetRank(int cr_id) const
```

#### SetRank
```angelscript
void SetRank(int cr_id, int rank)
```

#### GetStatus
```angelscript
int GetStatus(int cr_id) const
```

#### SetStatus
```angelscript
void SetStatus(int cr_id, int status)
```

#### GetMembers
```angelscript
int GetMembers(array<uint>& members) const
```

#### GetRecords
```angelscript
int GetRecords(array<uint>& records) const
```

#### AddKnownFaction
```angelscript
void AddKnownFaction(int faction_id)
```

#### GetKnownFactions
```angelscript
int GetKnownFactions(array<int>& factions) const
```

#### Remove
```angelscript
void Remove()
```


## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| NameIndices | `dictionary` |  | "faction name" -> idx string -> int |
| IdIndices | `dictionary` |  | faction id -> idx (in hoping lookup times would be optimal) |
| LastId | `int` |  | and this is the id number of last faction in that array |
| GettingFactions | `bool` | `false` | some switches helping us to orchestrate this async fest |

## Functions

### GetFaction

```angelscript
IFaction@ GetFaction(int id)
```

### GetFaction

```angelscript
IFaction@ GetFaction(const string& name)
```

### GetFactionByIdx

```angelscript
IFaction@ GetFactionByIdx(int idx)
```

### AddFaction

```angelscript
void AddFaction(IFaction& faction)
```

### RemoveFaction

* * Removes faction with given id. 

```angelscript
bool RemoveFaction(uint faction_id)
```

### GetFactionsCount

```angelscript
uint GetFactionsCount()
```

### InitFactions

Initializes last faction id, fetches factions from 'factions' view which has to contain 'id' field

```angelscript
void InitFactions()
```

### InitFactionData

* * Initialize FactionData objects 

```angelscript
void InitFactionData()
```

### UpdateFactionsInfo

checks every faction, and if some of them got updated after player was last time synchronized, we issue fetch for his document at that faction

```angelscript
void UpdateFactionsInfo(Critter& player)
```

### UpdateBasesVisibility

updates bases visibility info basing on players rank and status within a faction

```angelscript
void UpdateBasesVisibility(IFaction@ faction, Critter& player)
```

### UpdateOneBaseVisibility

```angelscript
void UpdateOneBaseVisibility(IFaction@ faction, Critter& player, IFactionBase@ base)
```

### UpdateGroupVars

* * Checks the integrity of faction and rank lvars with teamid. Updates if necessary. 

```angelscript
void UpdateGroupVars(Critter& player)
```

### GetFactionNameStr

* * Gets name of the faction presented as string 

```angelscript
bool GetFactionNameStr(uint faction_id, string& out name)
```


