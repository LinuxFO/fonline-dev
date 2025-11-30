---
title: cheats_help.fos
description: " FOnline: 2238 Rotators  cheats_help.fos ..."
---

# cheats_help.fos


FOnline: 2238
Rotators

cheats_help.fos


## Includes

- `_macros.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __CHEATS_HELP__ |  |  |
| HLP_UNKNOWN | `(-1)` |  |
| HLP_NORMAL | `(0)` |  |
| HLP_CLIENT | `(1)` |  |
| HLP_LINK | `(2)` |  |
| HLP_WIKI | `"commands.txt"` |  |
| LongCommand | `# (name, text)cmd = AddCommand(name, text)` |  |
| LongLink | `# (sh, lo)cmd = AddLink(sh, lo)` |  |
| LastCommand | `# (text)                 CheatHelp[cmd].Description(text)` |  |
| LastLink | `# (text)                        CheatHelp[cmd].SeeAlso(text)` |  |
| LastType | `# (t)                           CheatHelp[cmd].type = t` |  |

## Classes

### CCheatHelp

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| command | `string` |  |  |
| type | `uint` |  |  |
| scripted | `bool` |  |  |
| disabled | `bool` |  |  |
| description | `array<string>` |  |  |
| see_also | `array<string>` |  |  |

**Methods**

#### Description
```angelscript
void Description(string line)
```

#### SeeAlso
```angelscript
void SeeAlso(string line)
```


## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| CheatHelp | `array<[CCheatHelp](cheats_help.fos.md)>` |  |  |
| CheatHelpInitialized | `bool` | `false` |  |

## Functions

### IsCorrectCommand

```angelscript
bool IsCorrectCommand(string& command)
```

### IsHelp

```angelscript
bool IsHelp(string& command)
```

### GetCommandType

```angelscript
int GetCommandType(string& command)
```

### AddCommand

```angelscript
int AddCommand(string& command, uint type)
```

### AddCommand

```angelscript
int AddCommand(string& command, string& description)
```

### AddLink

```angelscript
int AddLink(string& command_short, string& command_long)
```

### InitHelp

```angelscript
void InitHelp()
```

### CheatHelpShow

```angelscript
void CheatHelpShow(Critter& player, string& command)
```

### ExecHelpCommand

```angelscript
void ExecHelpCommand(array<string@>@ command, Critter@ player)
```

### GMWikiCommands

```angelscript
void GMWikiCommands()
```

### gmwiki

```angelscript
void gmwiki(Critter&, int, int, int)
```


