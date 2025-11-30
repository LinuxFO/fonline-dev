---
title: config_file.fos
description: " FOnline: 2238 Rotators  config_file.fos ..."
---

# config_file.fos


FOnline: 2238
Rotators

config_file.fos


## Includes

- `_macros.fos`
- `config_file_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __CONFIG_FILE__ |  |  |

## Classes

### CConfigVar

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| name | `string` |  |  |
| value | `string` |  |  |

**Methods**

#### GetName
```angelscript
string GetName()
```

#### GetValue
```angelscript
string GetValue()
```

#### GetValueAsArray
```angelscript
array<string> GetValueAsArray()
```

#### GetValueAsArray
```angelscript
array<string> GetValueAsArray(string& delimeter)
```

#### SetValue
```angelscript
void SetValue(int val)
```

#### SetValue
```angelscript
void SetValue(uint val)
```

#### SetValue
```angelscript
void SetValue(string& val)
```

#### SetValue
```angelscript
void SetValue(array<string>& val)
```

#### SetValue
```angelscript
void SetValue(array<string>& val, string& delimeter)
```

### CConfigSection

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| name | `string` |  |  |

**Methods**

#### GetName
```angelscript
string GetName()
```

#### AddVar
```angelscript
bool AddVar(string& varname, string& val)
```

#### DeleteVar
```angelscript
bool DeleteVar(string& varname)
```

#### DeleteVar
```angelscript
bool DeleteVar(string& varname, bool caseSensitive)
```

#### GetVar
```angelscript
IConfigVar@ GetVar(string& varname)
```

#### GetVar
```angelscript
IConfigVar@ GetVar(string& varname, bool caseSensitive)
```

#### GetVars
```angelscript
void GetVars(array<string>& list)
```

#### SetVar
```angelscript
bool SetVar(string& varname, string val)
```

#### VarExists
```angelscript
bool VarExists(string& varname)
```

#### VarExists
```angelscript
bool VarExists(string& varname, bool caseSensitive)
```

### CConfigFile

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| name | `string` |  |  |
| virtual | `bool` |  |  |

**Methods**

#### IsVirtual
```angelscript
bool IsVirtual()
```

#### GetName
```angelscript
string GetName()
```

#### AddSection
```angelscript
bool AddSection(string& sectioname)
```

#### GetSection
```angelscript
IConfigSection@ GetSection(string& sectioname)
```

#### GetSection
```angelscript
IConfigSection@ GetSection(string& sectioname, bool caseSensitive)
```

#### GetSections
```angelscript
void GetSections(array<string>& list)
```

#### SectionExists
```angelscript
bool SectionExists(string& sectioname)
```

#### SectionExists
```angelscript
bool SectionExists(string& sectioname, bool caseSensitive)
```


## Functions

### stringReplaceText

```angelscript
int stringReplaceText(string& s, string@ f, string@ t)
```

### NewConfig

```angelscript
IConfigFile@ NewConfig(string& filename)
```

### LoadConfig

```angelscript
bool LoadConfig(string& filename)
```

### SaveConfigFiles

```angelscript
void SaveConfigFiles()
```

### SaveConfig

```angelscript
bool SaveConfig(string& filename)
```

### UnloadConfig

```angelscript
bool UnloadConfig(string& filename)
```

### GetConfigFile

```angelscript
IConfigFile@ GetConfigFile(string& filename)
```

### GetConfigFile

```angelscript
IConfigFile@ GetConfigFile(string& filename, bool caseSensitive)
```

### GetConfigSection

```angelscript
IConfigSection@ GetConfigSection(string& filename, string& sectioname)
```

### GetConfigSection

```angelscript
IConfigSection@ GetConfigSection(string& filename, string& sectioname, bool caseSensitive)
```

### GetConfigVar

```angelscript
IConfigVar@ GetConfigVar(string& filename, string& sectioname, string@ varname)
```

### GetConfigVar

```angelscript
IConfigVar@ GetConfigVar(string& filename, string& sectioname, string@ varname, bool caseSensitive)
```

### GetConfigValue

```angelscript
string@ GetConfigValue(string& filename, string& sectioname, string@ varname)
```

### GetConfigValue

```angelscript
string@ GetConfigValue(string& filename, string& sectioname, string@ varname, bool caseSensitive)
```

### SetConfigValue

```angelscript
bool SetConfigValue(string& filename, string& sectioname, string@ varname, bool value)
```

### SetConfigValue

```angelscript
bool SetConfigValue(string& filename, string& sectioname, string@ varname, int value)
```

### SetConfigValue

```angelscript
bool SetConfigValue(string& filename, string& sectioname, string@ varname, uint value)
```

### SetConfigValue

```angelscript
bool SetConfigValue(string& filename, string& sectioname, string@ varname, string& value)
```

### version

```angelscript
void version(Critter& player, int, int, int)
```


