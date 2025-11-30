---
title: gm.fos
description: " FOnline: 2238 Rotators  gm.fos ..."
---

# gm.fos


FOnline: 2238
Rotators

gm.fos


## Includes

- `_macros.fos`
- `utils_h.fos`

## Included By

- [cheats.fos](cheats.fos.md)

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| AUTH_LEVEL_GM | `(1)` |  |
| AUTH_LEVEL_ADMIN | `(2)` |  |

## Functions

### GM_IsGameMaster

 Checks if player is Game Master (if and ONLY if) 

```angelscript
bool GM_IsGameMaster(uint playerId)
```

### GM_GetCredit

 Checks the amount of credit points given player have. 

```angelscript
int GM_GetCredit(uint playerId)
```

### GM_GiveCredit

 Gives credit points to GM 

```angelscript
void GM_GiveCredit(uint playerId, uint amount)
```

### GM_DeduceCredit

 Substracts given amount of credits points 

```angelscript
void GM_DeduceCredit(uint playerId, uint amount)
```

### GM_BindNpc

 Binds npc to GM 

```angelscript
void GM_BindNpc(uint playerId, uint npcId)
```

### ExecGMCommand

 Makes GM out of casual player 

```angelscript
void ExecGMCommand(array<string@>@ command, Critter& player, Critter@ target)
```

### ExecModCharCommand

 Manipulates stats of the GM character  It's not GM command. It's command admin should issue on GMs (he can issue it on every critter though)

```angelscript
void ExecModCharCommand(array<string@>@ command, Critter& player, Critter@ target)
```

### ModifyArmor

 Modifies armor of the given critter (BASE armor, any other armor critter can wear applies its modificators too) 

```angelscript
void ModifyArmor(Critter& player, Critter@ target, const string& armor)
```

### ModifyStat

 Modifies given statistic, returns false in case of failure 

```angelscript
bool ModifyStat(Critter& player, Critter@ target, const string& stat, int val)
```


