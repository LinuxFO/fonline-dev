---
title: unsafe_client.fos
description: " FOnline: 2238 Rotators  unsafe_client.fos ..."
---

# unsafe_client.fos


FOnline: 2238
Rotators

unsafe_client.fos


## Includes

- `_basetypes.fos`
- `_colors.fos`
- `_macros.fos`
- `broadcast_h.fos`
- `config_file_h.fos`
- `factions_h.fos`
- `follower_common_h.fos`
- `groups_h.fos`
- `logging_h.fos`
- `mapdata_h.fos`
- `npc_common_h.fos`
- `utils_h.fos`
- `town_h.fos`
- `worldmap_h.fos`
- `map_tent_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| GETACCESS_FILE | `"config\\GetAccess.cfg"` |  |
| RADIUS | `7` |  |
| AP_COST | `5` |  |
| EFFECT_CHANCE | `7` |  |
| DMG_MIN | `60` |  |
| DMG_MAX | `120` |  |
| DISCHARGE_COST | `100` |  |
| RECHARGE_VALUE | `100` |  |

## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| accessfile_loaded | `bool` | `false` |  |

## Functions

### unsafe_GetTimer

```angelscript
void unsafe_GetTimer(Critter& player, int p0, int p1, int p2, string@ commandString, array<int>@ param4)
```

### unsafe_ExecCommandEntered

```angelscript
void unsafe_ExecCommandEntered(Critter& player, int p0, int p1, int p2, string@ commandString, array<int>@ param4)
```

### unsafe_Spectate

```angelscript
void unsafe_Spectate(Critter& player, int p0, int p1, int p2, string@ commandString, array<int>@ param4)
```

### unsafe_PingServer

Detect FOCD

```angelscript
void unsafe_PingServer(Critter& player, int globalEnable, int duallog, int p2, string@ commandString, array<int>@ param4)
```

### unsafe_ExecShowFactionInfluence

```angelscript
void unsafe_ExecShowFactionInfluence(Critter& player, int, int, int, string@, array<int>@)
```

### unsafe_ExecDisbandParty

```angelscript
void unsafe_ExecDisbandParty(Critter& player, int p0, int p1, int p2, string@ commandString, array<int>@ param4)
```

### unsafe_ExecACReport

```angelscript
void unsafe_ExecACReport(Critter& player, int p0, int p1, int p2, string@ commandString, array<int>@ param4)
```

### unsafe_ExecGMHelpCommand

```angelscript
void unsafe_ExecGMHelpCommand(Critter& player, int p0, int p1, int p2, string@ commandString, array<int>@ param4)
```

### unsafe_RadioDistressCall

* * Sends radio call. 

```angelscript
void unsafe_RadioDistressCall(Critter& player, int p0, int p1, int p2, string@ message, array<int>@ param4)
```

### unsafe_Suicide

* * Suicidal tendencies. 

```angelscript
void unsafe_Suicide(Critter& player, int, int, int, string@, array<int>@)
```

### unsafe_Suicide2

```angelscript
void unsafe_Suicide2(Critter& player, int, int, int, string@, array<int>@)
```

### unsafe_PartyPoints

```angelscript
void unsafe_PartyPoints(Critter& player, int, int, int, string@, array<int>@)
```

### unsafe_WeaponMode

```angelscript
void unsafe_WeaponMode(Critter& player, int mode, int, int, string@, array<int>@)
```

### unsafe_TakeAll

```angelscript
void unsafe_TakeAll(Critter& target, int contId, int bodyId, int useFilter, string@, array<int>@)
```

### unsafe_PutAll

```angelscript
void unsafe_PutAll(Critter& target, int contId, int bodyId, int useFilter, string@, array<int>@)
```

### unsafe_PickAll

```angelscript
void unsafe_PickAll(Critter& target, int, int, int, string@, array<int>@)
```

### unsafe_DropAll

```angelscript
void unsafe_DropAll(Critter& target, int, int, int, string@, array<int>@)
```

### unsafe_DropOne

```angelscript
void unsafe_DropOne(Critter& target, int id, int, int, string@, array<int>@)
```

### unsafe_MoveItemCrit2Cont

```angelscript
void unsafe_MoveItemCrit2Cont(Critter& target, int itemId, int contId, int, string@, array<int>@)
```

### unsafe_MoveItemCont2Crit

```angelscript
void unsafe_MoveItemCont2Crit(Critter& target, int itemId, int contId, int, string@, array<int>@)
```

### unsafe_MoveItemBody2Crit

```angelscript
void unsafe_MoveItemBody2Crit(Critter& target, int itemId, int bodyId, int, string@, array<int>@)
```

### unsafe_MoveItemCrit2Body

```angelscript
void unsafe_MoveItemCrit2Body(Critter& target, int itemId, int bodyId, int, string@, array<int>@)
```

### unsafe_play_rr

```angelscript
void unsafe_play_rr(Critter& player, int, int, int, string@, array<int>@)
```

### PushCritter

```angelscript
bool PushCritter(Map& map, Critter@ cr, uint8 leadDir, uint8 depth)
```

### unsafe_PushCritter

```angelscript
void unsafe_PushCritter(Critter& player, int p0, int p1, int p2, string@ message, array<int>@ param4)
```

### unsafe_OOC

```angelscript
void unsafe_OOC(Critter& player, int, int, int, string@ message, array<int>@)
```

### unsafe_gameinfo

```angelscript
void        unsafe_gameinfo(Critter& player, int, int, int, string@ message, array<int>@)
```

### AuthPasswordOwner

```angelscript
string@ AuthPasswordOwner(string& password)
```

### accessfile_load

```angelscript
void accessfile_load(string& filename)
```

### unsafe_getaccess

```angelscript
void unsafe_getaccess(Critter& player, int, int, int, string@ message, array<int>@)
```

### unsafe_disconnect

```angelscript
void unsafe_disconnect(Critter& player, int, int, int, string@ message, array<int>@)
```

### unsafe_GetFactionCount

```angelscript
void unsafe_GetFactionCount(Critter& player, int, int, int, string@, array<int>@)
```

### unsafe_FreeFactionNames

```angelscript
void        unsafe_FreeFactionNames(Critter& player, int, int, int, string@, array<int>@)
```

### unsafe_FactionNames

Used for acquiring a list of factions

```angelscript
void        unsafe_FactionNames(Critter& player, int, int, int, string@, array<int>@)
```

### unsafe_MyInfo

```angelscript
void unsafe_MyInfo(Critter& player, int, int, int, string@, array<int>@)
```

### unsafe_FactionInfo

```angelscript
void unsafe_FactionInfo(Critter& player, int, int, int, string@, array<int>@)
```

### unsafe_CombatMode

```angelscript
void unsafe_CombatMode(Critter& player, int mode, int, int, string@, array<int>@)
```

### unsafe_EndTurnBasedTurn

```angelscript
void unsafe_EndTurnBasedTurn(Critter& player, int, int, int, string@, int[]@)
```

### unsafe_EndTurnBasedCombat

```angelscript
void unsafe_EndTurnBasedCombat(Critter& player, int, int, int, string@, int[]@)
```

### unsafe_Discharge

```angelscript
void unsafe_Discharge(Critter& player, int, int, int, string@, int[]@)
```

### unsafe_ScienceAtHex

```angelscript
void unsafe_ScienceAtHex(Critter& player, int mode, int, int, string@, array<int>@)
```


