---
title: follower.fos
description: " FOnline: 2238 Rotators  follower.fos ..."
---

# follower.fos


FOnline: 2238
Rotators

follower.fos


## Includes

- `_basetypes.fos`
- `_macros.fos`
- `_town.fos`
- `economy_h.fos`
- `entire.fos`
- `factions_bases_h.fos`
- `factions_h.fos`
- `follower_common_h.fos`
- `follower_h.fos`
- `map_tent_h.fos`
- `mapdata_h.fos`
- `messages_h.fos`
- `mercs_h.fos`
- `npc_common_h.fos`
- `npc_planes_h.fos`
- `town_h.fos`
- `utils_h.fos`
- `world_common_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __FOLLOWER__ |  |  |

## Functions

### IsCompanion

```angelscript
bool IsCompanion(Critter& follower)
```

### IsAnimal

```angelscript
bool IsAnimal(Critter& follower)
```

### cte_UpdateLoyality

```angelscript
uint cte_UpdateLoyality(Critter& follower, int identifier, uint& rate)
```

### HasMasterSpeakerPerk

```angelscript
bool HasMasterSpeakerPerk(Critter& follower) { return FLAG(follower.FollowerVar[FV_FLAGS], FV_FLAG_MASTER_SPEAKER); }
```

### UpdateLoyality

```angelscript
void UpdateLoyality(Critter& follower)
```

### r_FollowMode

```angelscript
void r_FollowMode(Critter& player, Critter@ follower, int value)
```

### r_AttackPolicy

Set attack policy and apply it to nearby critters immediately

```angelscript
void r_AttackPolicy(Critter& player, Critter@ follower, int value)
```

### r_ArmBestWeapon

```angelscript
void r_ArmBestWeapon(Critter& player, Critter@ follower)
```

### r_PutDownWeapon

```angelscript
void r_PutDownWeapon(Critter& player, Critter@ follower)
```

### r_DropAllItems

```angelscript
void r_DropAllItems(Critter& player, Critter@ follower)
```

### r_IncreaseLoyality

```angelscript
void r_IncreaseLoyality(Critter& player, Critter@ follower, int Min, int Max)
```

### r_Rotate

Rotate one dir

```angelscript
void r_Rotate(Critter& player, Critter@ follower, int value)
```

### r_Distance

Set follow distance

```angelscript
void r_Distance(Critter& player, Critter@ follower, int value)
```

### r_ClaimFollower

Takeover follower from another owner.

```angelscript
void r_ClaimFollower(Critter& player, Critter@ follower, int value)
```

### r_TellWeaponSkill

Check which weapon skill is the highest and jump to the specific node in dialog.

```angelscript
uint r_TellWeaponSkill(Critter& player, Critter@ follower)
```

### GetLoyality

```angelscript
uint GetLoyality(Critter& follower) { return follower.FollowerVar[FV_LOYALITY]; }
```

### ModifyLoyality

```angelscript
void ModifyLoyality(Critter& cr, int value)
```

### ModifyLoyality

```angelscript
void ModifyLoyality(Critter& cr, int IncMin, int IncMax)
```

### GetMercLoyalityText

TODO: Might be a good idea to move these to FOTEXT.

```angelscript
string GetMercLoyalityText(uint loyality)
```

### GetCompanionLoyalityText

```angelscript
string GetCompanionLoyalityText(uint loyality)
```

### GetSlaveLoyalityText

```angelscript
string GetSlaveLoyalityText(uint loyality)
```

### GetLoyalityText

```angelscript
string GetLoyalityText(Critter& npc)
```

### dlg_ShowMercPayCost

```angelscript
void dlg_ShowMercPayCost(Critter& player, Critter@ follower, string@ text)
```

### dlg_ShowLoyality

```angelscript
void dlg_ShowLoyality(Critter& player, Critter@ npc, string@ text)
```

### dlg_ShowStats

```angelscript
void dlg_ShowStats(Critter& player, Critter@ npc, string@ text)
```

### dlg_ChooseBase

```angelscript
uint dlg_ChooseBase(Critter& cr, Critter@ follower, string@ say)
```

### dlg_GiveFollower

```angelscript
uint dlg_GiveFollower(Critter& player, Critter@ npc, string@ say)
```

### d_IsLoyalityMax

```angelscript
bool d_IsLoyalityMax(Critter& player, Critter@ follower)
```

### d_IsNotLoyalityMax

```angelscript
bool d_IsNotLoyalityMax(Critter& player, Critter@ follower)
```

### d_IsOwner

```angelscript
bool d_IsOwner(Critter& player, Critter@ follower, int val)
```

### d_IsClaimable

```angelscript
bool d_IsClaimable(Critter& player, Critter@ follower, int val)
```

### d_IsGuarding

```angelscript
bool d_IsGuarding(Critter& player, Critter@ follower, int val)
```

### d_IsFollowing

```angelscript
bool d_IsFollowing(Critter& player, Critter@ follower, int val)
```

### d_SpawnMap

```angelscript
int d_SpawnMap(Critter& player, Critter@ follower, int val)
```

### d_IsNotMode

```angelscript
bool d_IsNotMode(Critter& player, Critter@ follower, int val)
```

### d_CanMine

```angelscript
bool d_CanMine(Critter& player, Critter@ follower)
```

### d_CanStay

```angelscript
bool d_CanStay(Critter& player, Critter@ follower)
```

### d_HasFollowerOfBaseType

```angelscript
bool d_HasFollowerOfBaseType(Critter& player, Critter@ npc, int val)
```

### r_RemoveFollowerOfBaseType

```angelscript
void r_RemoveFollowerOfBaseType(Critter& player, Critter@ npc, int val)
```

### d_HasBrahmin

```angelscript
bool d_HasBrahmin(Critter& player, Critter@ npc, int val)
```

### d_HasNoBrahmin

```angelscript
bool d_HasNoBrahmin(Critter& player, Critter@ npc, int val)
```

### d_CanLeadMoreFollowers

Followers that follow

```angelscript
bool d_CanLeadMoreFollowers(Critter& player, Critter@ npc)
```

### d_CanHaveMoreFollowers

All followers on map

```angelscript
bool d_CanHaveMoreFollowers(Critter& player, Critter@ npc, int FollowerType)
```

### r_RemoveBrahmin

```angelscript
void r_RemoveBrahmin(Critter& player, Critter@ npc, int val)
```

### r_RemoveFollower

```angelscript
void r_RemoveFollower(Critter& player, Critter@ npc, int mode)
```

### d_IsSpawnPlaceAvailable

```angelscript
bool d_IsSpawnPlaceAvailable(Critter& player, Critter@ npc, int place)
```

### r_RemoveArmor

```angelscript
void r_RemoveArmor(Critter& player, Critter@ follower)
```

### r_SetArmor

```angelscript
void r_SetArmor(Critter& player, Critter@ follower, int pid)
```

### r_RemoveHelmet

```angelscript
void r_RemoveHelmet(Critter& player, Critter@ follower)
```

### r_SetHelmet

```angelscript
void r_SetHelmet(Critter& player, Critter@ follower, int pid)
```

### r_SetSpawnPlace

```angelscript
void r_SetSpawnPlace(Critter& player, Critter@ follower, int place)
```

### r_SetFaction

```angelscript
void r_SetFaction(Critter& player, Critter@ follower)
```

### d_CanPayMerc

```angelscript
bool d_CanPayMerc(Critter& player, Critter@ follower)
```

### r_PayMerc

```angelscript
void r_PayMerc(Critter& player, Critter@ follower)
```

### GetMercLoyalityCost

Todo: Add d_CanPayMerc / r_PayMerc functions for slave/companion

```angelscript
uint GetMercLoyalityCost(uint basecost)
```

### SetMode

```angelscript
void SetMode(Critter& master, Critter& follower, uint mode)
```

### SetEvents

Events for NPC followers

```angelscript
void SetEvents(Critter& critter)
```

### FollowerBaseInit

```angelscript
void FollowerBaseInit(Critter& follower, bool firstTime)
```

### critter_init

```angelscript
void critter_init(Critter& follower, bool firstTime)
```

### _PlaneRun

```angelscript
int _PlaneRun(Critter& follower, NpcPlane& plane, int reason, uint& result0, uint& result1, uint& result2)
```

### _PlaneEnd

```angelscript
int _PlaneEnd(Critter& follower, NpcPlane& plane, int reason, Critter@ someCr, Item@ someItem)
```

### _Slave

```angelscript
void _Slave(Critter& cr, bool firstTime)
```

### _Dead

Remove GECK mode to enable deletion of map

```angelscript
void _Dead(Critter& cr, Critter@ killer)
```

### _ShowCritter

```angelscript
void _ShowCritter(Critter& follower, Critter& critter)
```

### GetMaster

```angelscript
Critter@ GetMaster(Critter& follower)
```

### IsAwayFromMaster

```angelscript
bool IsAwayFromMaster(Critter& master, Critter& follower)
```

### IsAwayFromMaster

```angelscript
bool IsAwayFromMaster(Critter& follower)
```

### GoToMaster

```angelscript
void GoToMaster(Critter& master, Critter& follower)
```

### _Idle

```angelscript
void _Idle(Critter& follower)
```

### _Attacked

```angelscript
bool _Attacked(Critter& follower, Critter& attacker)
```

### _Attack

```angelscript
bool _Attack(Critter& follower, Critter& target)
```

### _SomeoneAttacked

```angelscript
void _SomeoneAttacked(Critter& follower, Critter& fromCrit, Critter& target)
```

### GetDistance

Retrieve how many hexes away the follower should be from the master

```angelscript
uint GetDistance(Critter& follower)
```

### IsMaster

```angelscript
bool IsMaster(Critter& follower, Critter& critter)
```

### IsOnBufferMap

```angelscript
bool IsOnBufferMap(Critter& follower)
```

### IsOnSameMap

```angelscript
bool IsOnSameMap(Critter& critter1, Critter& critter2)
```

### IsOnWorldmap

```angelscript
bool IsOnWorldmap(Critter& critter)
```

### IsFriend

Checks if a critter is considered friendly

```angelscript
bool IsFriend(Critter& follower, Critter& critter)
```

### IsSquadMember

Checks if critter is in the same squad (it's owner or has the same owner)

```angelscript
bool IsSquadMember(Critter& follower, Critter& critter)
```

### IsNonAggressive

```angelscript
bool IsNonAggressive(Critter& follower)
```


