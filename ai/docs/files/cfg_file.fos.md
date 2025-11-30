---
title: cfg_file.fos
description: " FOnline: 2238 Rotators  cfg_file.fos ..."
---

# cfg_file.fos


FOnline: 2238
Rotators

cfg_file.fos


## Includes

- `_macros.fos`

## Included By

- [client_spawn_npc.fos](client_spawn_npc.fos.md)

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __CFG_FILE__ |  |  |

## Classes

### CSection

 Section of the config file 

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| indices | `dictionary` |  | all properties of a section (indices to values array) |
| name | `string` |  |  |

**Methods**

#### SetName
 Sets name of a section 

```angelscript
void SetName(string& name)
```

#### AddProperty
 Adds property to dictionary 

```angelscript
void AddProperty(string@ name, string@ value)
```

#### GetValue
 Gets value for a property 

```angelscript
string@ GetValue(string& property)
```

### CConfig

 Parsing file/creating data representaiton 

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| indices | `dictionary` |  | indices to sections |

**Methods**

#### GetValue
 Properties 

```angelscript
string@ GetValue(string& sectionName, string& property)
```

#### AddSection
 Adds section to the list and dicitonary 

```angelscript
void AddSection(CSection@ section)
```

#### Parse
 Parse content of the file 

```angelscript
void Parse(file& f)
```

#### ParseSection
 Parses properties for section 

```angelscript
CSection@ ParseSection(array<string@>@ lines, uint& i)
```


