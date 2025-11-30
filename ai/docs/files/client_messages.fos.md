---
title: client_messages.fos
description: " FOnline: 2238 Rotators  client_messages.fos ..."
---

# client_messages.fos


FOnline: 2238
Rotators

client_messages.fos


## Includes

- `_defines.fos`
- `_macros.fos`
- `_globalvars.fos`
- `_client_defines.fos`
- `_colors.fos`
- `buffer_h.fos`
- `config_file_h.fos`
- `client_utils_h.fos`
- `lexems_h.fos`

## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| isListen | `bool` | `false` |  |
| LogAutoSave | `bool` | `false` |  |
| oocflood | `array<string>` |  |  |

## Functions

### ForceSay

words to be replaced; first - original word, anything else - possible variations input word case is ignored if variaton picked is empty, word is removed const string[][] out_replace = { { "input",			"output", "output" }, { "a",				"" }, { "am",				"is" }, { "an",				"" }, { "are",			"harr" }, { "armor",			"armar" }, { "attack",			"hurt" }, { "bos",			"Shiny Shiny Tinmen" }, { "brotherhood",	"Tinmen" }, { "burst",			"dakdak" }, { "but",			"bat" }, { "caps",			"munneh", "maney", "monnies" }, { "could",			"cudd" }, { "dead",			"deaded" }, { "doc",			"dok" } { "don't",			"donn" }, { "dont",			"donn" }, { "enemy",			"enemi" }, { "enemies",		"baddies" }, { "encounter",		"fite" }, { "enclave",		"Anklaff", "Enlkav" }, { "fa",				"stich meh!" }, { "food",			"yummeyh" }, { "did",			"done" }, { "ghoul",			"stinker" }, { "ghouls",			"stinkers" }, { "grenade",		"boomer", "boom-boom" }, { "gun",			"boomstick", "gan" }, { "had",			"haved" }, { "has",			"got" }, { "have",			"gotted" }, { "hunt",			"killen" }, { "into",			"in" }, { "i",				"me" }, { "injured",		"hurted" }, { "join",			"go vith mee" }, { "kill",			"ded", "keel" }, { "knife",			"stabber" }, { "laser",			"red light" }, { "love",			"luv" }, { "mutant",			"ugly" }, { "mutants",		"ugly" }, { "nade",			"boomer", "boom-boom" }, { "no",				"nah" }, { "pa",				"Big Tin Zuit" }, { "pk",				"baddies" }, { "powerarmor",		"Big Tin Zuit" }, { "plasma",			"plazme" }, { "pretty",			"preety" }, { "raiders",		"baddies" }, { "rocket",			"rokkeet" }, { "so",				"den" }, { "tank",			"strongman" }, { "the",			"teh" }, { "thief",			"stealer" }, { "took",			"tack" }, { "want",			"wannuh { "weak",			"girly" }, { "weapon",			"hurter" }, { "what?",			"duhh" }, { "wtb",			"me buyyeh" }, { "wtb",			"me solding" }, { "why",			"wai", "y" }, { "will",			"gonnah" }, { "with",			"vith" }, { "you",			"yoo", "u" }, { "yell",			"yel" }, { "yes",			"yeh" } }; 

```angelscript
void ForceSay(uint8 sayType, uint critterId, string& message)
```

### ForceSay

```angelscript
void ForceSay(uint8 sayType, string& who, string& message)
```

### map_message

///////////////////////////////////////////////////////////////////////////////////////////////// Call on receive message on map. By default delay == [TextDelay + message length * 100] ms

```angelscript
bool map_message(string& message, uint16& hexX, uint16& hexY, uint& color, uint& delay)
```

### in_message

///////////////////////////////////////////////////////////////////////////////////////////////// Call on receive message. By default delay == [TextDelay + message length * 100] ms

```angelscript
bool in_message(string& message, int& sayType, uint& critterId, uint& delay)
```

### out_message

///////////////////////////////////////////////////////////////////////////////////////////////// Call on send message.

```angelscript
bool out_message(string& message, int& sayType)
```

### _Listen

```angelscript
void _Listen(int param1, int param2, int param3, string@ param4, array<int>@ param5)
```

### sayEx

```angelscript
void sayEx(int type, int crId, int, string@ text, array<int>@)
```

### map

```angelscript
void map(int type, int hx, int hy, string@ text, array<int>@ data)
```


