---
title: itempid.fos
description: " FOnline: 2238 Rotators  itempid.fos ..."
---

# itempid.fos


FOnline: 2238
Rotators

itempid.fos


## Includes

- `itempid_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __ITEMPID__ |  |  |
| FUNCTION_IS | `# (isName, listName) bool PidIs ## isName(uint p) { array<uint> l; PidList_ ## listName(l); return (l.find(p) >= 0); }` |  |
| FUNCTIONS | `# (isName, listName, enumName) bool PidIs ## isName(uint p) { array<uint> l; PidList_ ## listName(l); return (l.find(p) >= 0); } uint PidList_ ## listName(array<uint>&v) { return (GroupNameToPids(enumName, v)); }` |  |

## Functions

### test

```angelscript
void test()
```

### check0

```angelscript
void check0(Critter& cr, int, int, int)
```

### PidToName

```angelscript
string PidToName(uint pid)
```

### PidToGroupName

```angelscript
string PidToGroupName(uint pid)
```

### NameToPid

```angelscript
uint NameToPid(string& name)
```

### GroupNameToPids

```angelscript
uint GroupNameToPids(string& groupName, array<uint>& pids)
```

### GroupNameToNames

```angelscript
uint GroupNameToNames(string& groupName, array<string>& pidNames)
```

### PidList_Helmets

```angelscript
uint PidList_Helmets(array<uint>& pids)
```

### PidList_Armors

```angelscript
uint PidList_Armors(array<uint>& pids)
```

### PidList_Weapons

```angelscript
uint PidList_Weapons(array<uint>& pids)
```

### PidList_SmallGuns

```angelscript
uint PidList_SmallGuns(array<uint>& pids)
```

### PidList_BigGuns

```angelscript
uint PidList_BigGuns(array<uint>& pids)
```

### PidList_EnergyWeapons

```angelscript
uint PidList_EnergyWeapons(array<uint>& pids)
```

### PidList_ThrowingWeapons

```angelscript
uint PidList_ThrowingWeapons(array<uint>& pids)
```

### PidList_Grenades

```angelscript
uint PidList_Grenades(array<uint>& pids)
```

### PidList_Flares

```angelscript
uint PidList_Flares(array<uint>& pids)
```

### PidList_MeleeWeapons

```angelscript
uint PidList_MeleeWeapons(array<uint>& pids)
```

### PidList_Ammunition

```angelscript
uint PidList_Ammunition(array<uint>& pids)
```

### PidList_Consumables

```angelscript
uint PidList_Consumables(array<uint>& pids)
```

### PidList_Containers

```angelscript
uint PidList_Containers(array<uint>& pids)
```


