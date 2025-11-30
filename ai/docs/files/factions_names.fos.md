---
title: factions_names.fos
description: " FOnline: 2238 Rotators  factions_names.fos ..."
---

# factions_names.fos


FOnline: 2238
Rotators

factions_names.fos


## Includes

- `_macros.fos`
- `debug_h.fos`

## Included By

- [faction_data.fos](faction_data.fos.md)

## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| NameAliases | `dictionary` |  | list of factions names aliases with the string num assigned |
| FactionNames | `array<string>` |  | list of factions names('official' not aliases) accessed through string id |
| AssignedNames | `dictionary@` |  |  Global dictionary holding names that are assigned to specific faction id  |
| UnassignedNames | `array<int>` |  | free faction names (stringid) |

## Functions

### GetFactionNameStringId

 Gets the string number for the given faction name  Params: name - faction name id - resulting id will be stored here Returns true if found, false otherwise.

```angelscript
bool GetFactionNameStringId(const string@ name, uint& out id)
```

### GetFactionName

 Retrieves faction name (as a string) fro a given stringId 

```angelscript
bool GetFactionName(uint stringId, string& out name)
```

### GetFactionId

 Retrieves the id of faction with given name Faction has to be registered first  Returns true if found, false otherwise

```angelscript
bool GetFactionId(const string@ name, uint& out id)
```

### AssignFactionName

 Assign given name with specific faction id  Params: - name: desired faction name - faction: desired faction id - stringId: id to the FactionNames array  Returns REGRESULT_* errorcode

```angelscript
int AssignFactionName(const string@ name, uint faction, uint& out stringId)
```

### UnassignFactionName

```angelscript
void UnassignFactionName(int stringId, const string& name)
```

### AssignFactionNameByStringId

 Assigns given faction name number to the given faction 

```angelscript
void AssignFactionNameByStringId(uint faction, uint stringId)
```

### GetUnassignedFactionNames

* * Retrieves the list of string id numbers for all faction names * that are not taken. 

```angelscript
uint GetUnassignedFactionNames(array<int>& res)
```

### IsFactionNameFree

* * Checks if given name(alias) is free 

```angelscript
bool IsFactionNameFree(const string& name)
```

### IsFactionNameValid

* * Checks if given faction name(alias) is valid 

```angelscript
bool IsFactionNameValid(const string& name)
```

### InitFactionsNames

 Initialize global dictionary with lookup for factions id 

```angelscript
void InitFactionsNames()
```

### ReadMsgStrings

 Read msg strings from the specified file to the output array of string objects.  Parameters: fileName - path to the msg file min, max - range of numbers of the strings we need to read strings - array which will be filled with strings

```angelscript
void ReadMsgStrings(string@ fileName, int min, int max)
```

### ParseMsgString

 Retrieves string from the line with following format: {number}{}{string} only if the number is within a min, max range. 

```angelscript
bool ParseMsgString(const string& in line, int min, int max, int& out num, string& out msgStr)
```


