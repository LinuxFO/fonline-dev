---
title: gmtools.fos
description: " FOnline: 2238 Rotators  gmtools.fos ..."
---

# gmtools.fos


FOnline: 2238
Rotators

gmtools.fos


## Includes

- `gmtools_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __GMTOOLS__ |  |  |

## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| null_data | `array<int>` |  |  |
| all | `uint` | `player.GetMap().GetCritters(0, FIND_ALL | FIND_ONLY_PLAYERS, critters)` |  |
| all | `uint` | `player.GetMap().GetCritters(0, FIND_ALL | FIND_ONLY_NPC, critters)` |  |
| all | `uint` | `player.GetMap().GetItems(param0, items)` |  |
| all | `uint` | `player.GetMap().GetSceneries(param0, scenery)` |  |
| victim | `Critter@` | `GetCritter(id)` |  |
| major | `uint` | `uint(GMTOOLS_VERSION / 1000)` |  |
| minor | `uint` | `uint((GMTOOLS_VERSION - (major * 1000)) / 100)` |  |
| fix | `uint` | `uint((GMTOOLS_VERSION - (major * 1000)) - (minor * 100))` |  |

## Functions

### ExplodeExEx

```angelscript
void ExplodeExEx(Map& map, uint16 hexX, uint16 hexY, uint16 effectPid, uint effectRadius, uint damage, uint damageType, uint damageRadius, uint ownerId, int quake, string& sound1, string sound2)
```

### AirstrikeEx

```angelscript
void AirstrikeEx(Critter& player, int hexX, int hexY, int unused, string@ sound, array<int>@ data)
```

### unsafe_question

```angelscript
void unsafe_question(Critter& player, int tick, int type, int flags, string@ question_text, array<int>@ data)
```

### GMTools_Chat

```angelscript
void GMTools_Chat(Critter& player, string& message)
```


