---
title: town.fos
description: " FOnline: 2238 Rotators  town.fos ..."
---

# town.fos


FOnline: 2238
Rotators

town.fos


## Includes

- `_maps.fos`
- `_colors.fos`
- `_entires.fos`
- `_macros.fos`
- `_math.fos`
- `_town.fos`
- `broadcast_h.fos`
- `economy_h.fos`
- `entire.fos`
- `factions_h.fos`
- `follower_common_h.fos`
- `mapdata_h.fos`
- `npc_common_h.fos`
- `npc_roles_h.fos`
- `polygon_h.fos`
- `reputations.fos`
- `town_h.fos`
- `_vars.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __TOWN__ |  |  |
| FORCE_DIALOG_TOO_FEW_PRESENT | `(301)` |  |
| FORCE_DIALOG_TOO_FEW_MEMBERS | `(302)` |  |
| FORCE_DIALOG_SUCCESS | `(310)` |  |
| FORCE_DIALOG_SPEECH_SUCCESS | `(320)` |  |
| FORCE_DIALOG_MILITIA_ATTACK | `(330)` |  |
| FORCE_DIALOG_SPEECH_FAILURE | `(130)` |  |
| FORCE_DIALOG_RECRUIT_SUCCESS | `(410)` |  |
| FORCE_DIALOG_RECRUIT_TOO_MANY | `(420)` |  |
| FORCE_DIALOG_RECRUIT_CANT_AFFORD | `(430)` |  |
| FORCE_DIALOG_RECRUIT_ERROR | `(440)` |  |
| FORCE_DIALOG_RECRUIT_COMBAT | `(450)` |  |
| _AddContItem | `\` |  |
| _AddContItem | `\` |  |
| _AddBetterContItem | `\` |  |

## Classes

### CTown

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| tcVersion | `uint` |  |  |
| factionInfluence | `array<float>` |  |  |
| militiaEnabled | `bool` |  |  |
| militiamax | `uint` |  |  |
| status | `uint` |  |  |
| faction | `uint` |  |  |
| previousfaction | `uint` |  |  |
| memberControlReq | `uint` |  |  |
| memberNearbyReq | `uint` |  |  |
| memberInfluenceReq | `uint` |  |  |
| memberTotalReq | `uint` |  |  |
| npcDeaths | `uint` |  |  |
| controlCycles | `uint` |  |  |
| rewardCapsStart | `uint` |  |  |
| rewardCaps | `uint` |  |  |
| mapid | `uint` |  |  |
| lastHour | `uint` |  |  |
| lastMinute | `uint` |  |  |
| lastSecond | `uint` |  |  |
| townLeaderId | `uint` |  |  |
| id | `uint` |  |  |
| hour | `uint` |  |  |
| countdown | `uint` |  |  |
| ch | `int` |  |  |
| speech | `int` |  |  |
| baseValue | `int` |  |  |
| speechModifier | `int` |  |  |
| friendsList | `array<uint>` |  |  |
| location | `Location@` |  |  |
| lawIllegalWeapons | `bool` |  |  |
| lawPunishThieves | `bool` |  |  |
| lawKillAggressor | `bool` |  |  |
| outsideAreaCount | `uint` |  |  |
| name | `string` |  |  |
| LimboContainer | `Item@` |  |  |
| RewardContainer | `Item@` |  |  |
| serializer | `[Serializator](serializator.fos.md)` |  |  |
| Money | `int` |  |  |

**Methods**

#### SetLaw
```angelscript
void SetLaw(uint law, bool enabled)
```

#### IsLaw
```angelscript
bool IsLaw(uint law)
```

#### GetMilitias
```angelscript
uint GetMilitias(Map& map, array<Critter@>@ militia)
```

#### InitTownMilitia
```angelscript
void InitTownMilitia(Map& map, Critter& leader)
```

#### RemoveTownMilitia
```angelscript
void RemoveTownMilitia(Map& map)
```

#### InitTownLeader
```angelscript
void InitTownLeader(Critter& leader)
```

#### LoadData
```angelscript
bool LoadData()
```

#### SaveData
```angelscript
bool SaveData()
```

#### GetControllingInfluence
```angelscript
float GetControllingInfluence()
```

#### GetLargestInfluence
* * Retrieves the faction with highest influence in town * @param faction Variable where found faction is saved, if 0 then none found. * @return Influence in float. * @remarks Used in TC version 3 

```angelscript
float GetLargestInfluence(uint& factionid)
```

#### SortInfluence
```angelscript
void SortInfluence()
```

#### GetTopInfluence
* * Retrieves factions with highest influence in town. * @param factions Array where found factions while be storedin faction_id,value,faction_id,value format. Array is not cleared. * @param num How many of the top x to retrieve. 3 will retrieve only the three most influential factions. * @return Number of factions found. * @remarks Used in TC version 3 

```angelscript
uint GetTopInfluence(array<uint>& factions, uint num)
```

#### GetInfluence
```angelscript
float GetInfluence(uint factionId)
```

#### SetInfluence
```angelscript
void SetInfluence(uint factionId, float value)
```

#### ModifyInfluence
```angelscript
void ModifyInfluence(uint factionId, float value)
```

#### GetFriendlyFactions
```angelscript
array<uint> GetFriendlyFactions()
```

#### IsMilitiaEnabled
```angelscript
bool IsMilitiaEnabled()
```

#### IsFriendlyFaction
```angelscript
bool IsFriendlyFaction(uint factionid)
```

#### IsWithinCaptureArea
```angelscript
bool IsWithinCaptureArea(Critter& cr)
```

#### IsFriend
```angelscript
bool IsFriend(Critter& cr)
```

#### GetCaptorInfluence
maximum 0,00408 per person, per tick (every 10 seconds now) 1,4688 / hour 35 / day

```angelscript
float GetCaptorInfluence(Critter& cr)
```

#### IsValidCaptor
```angelscript
bool IsValidCaptor(Critter& cr)
```

#### AddFriendlyFaction
```angelscript
bool AddFriendlyFaction(uint factionid)
```

#### GetAreaCount
```angelscript
uint GetAreaCount()
```

#### RemoveFriendlyFaction
```angelscript
bool RemoveFriendlyFaction(uint factionid)
```

#### GetStatus
Town can only be taken during a one hour period each day or during countdown Not used

```angelscript
uint GetStatus()
```

#### SetStatus
```angelscript
void SetStatus(uint status)
```

#### SetPreviousFaction
```angelscript
void SetPreviousFaction(uint previous)
```

#### RevertControl
```angelscript
void RevertControl()
```

#### SetScore
```angelscript
void SetScore()
```

#### AssignMilitiaTeam
```angelscript
void AssignMilitiaTeam(Critter@ cr)
```

#### NumberOfValidFactionMembersPresent
```angelscript
uint NumberOfValidFactionMembersPresent(Map& map, uint someFaction)
```

#### TownCheck
version 2 All broadcast messages are unique in this function, if duplicate broadcast are sent, only one line should be shown.

```angelscript
void TownCheck()
```

#### AreaCheck
version 0 and 1

```angelscript
void AreaCheck()
```

#### ControlCheck
version 3

```angelscript
void ControlCheck()
```

#### Update
Hourly update

```angelscript
void Update(uint hour, uint minute)
```

#### AddReward
```angelscript
void AddReward(uint itemPid, int count)
```

#### GiveControlReward
```angelscript
void GiveControlReward()
```

#### GiveReward
```angelscript
void GiveReward(uint militiaCount)
```

#### UpdateTick
```angelscript
void UpdateTick()
```

#### UpdateCountdown
```angelscript
void UpdateCountdown()
```

#### IncreaseNPCDeath
```angelscript
void IncreaseNPCDeath(uint num)
```

#### IncreasecontrolCycles
```angelscript
void IncreasecontrolCycles(uint num)
```

#### GetlastSecond
```angelscript
uint GetlastSecond()
```

#### SetlastSecond
```angelscript
void SetlastSecond(uint sec)
```

#### GetCountdown
```angelscript
uint GetCountdown()
```

#### GetVersion
```angelscript
uint GetVersion() { return tcVersion; }
```

#### GetControlCycles
```angelscript
uint GetControlCycles()
```

#### GetNumberOfKilledNPCs
```angelscript
uint GetNumberOfKilledNPCs()
```

#### GetControllingFaction
```angelscript
uint GetControllingFaction()
```

#### GetMemberNearbyRequirement
```angelscript
uint GetMemberNearbyRequirement()
```

#### GetMemberTotalRequirement
```angelscript
uint GetMemberTotalRequirement()
```

#### GetMemberControlRequirement
```angelscript
uint GetMemberControlRequirement()
```

#### GetSpeechModifier
```angelscript
int GetSpeechModifier()
```

#### GetMilitiaMax
```angelscript
uint GetMilitiaMax()
```

#### GetLimboContainer
```angelscript
Item@ GetLimboContainer()
```

#### GetRewardContainer
```angelscript
Item@ GetRewardContainer()
```

#### GetMapID
```angelscript
uint GetMapID()
```

#### SendCountdownTime
```angelscript
void SendCountdownTime(Critter& player)
```

#### SetControl
```angelscript
bool SetControl(uint newFaction)
```

#### GainControl
Trying to gain control

```angelscript
bool GainControl(Critter& player)
```

#### SetCountdownStatus
```angelscript
void SetCountdownStatus(bool enabled)
```

#### GetCountdownStatus
```angelscript
bool GetCountdownStatus()
```

#### ResetControl
```angelscript
void ResetControl()
```

#### ResetStats
```angelscript
void ResetStats()
```

#### ClearRewardContainer
```angelscript
void ClearRewardContainer()
```

#### ClearLimboContainer
```angelscript
void ClearLimboContainer()
```

#### ClearContainers
```angelscript
void ClearContainers()
```

#### GetTownID
```angelscript
uint GetTownID()
```

#### GetTownName
```angelscript
string GetTownName()
```

#### GetTownLeaderId
```angelscript
uint GetTownLeaderId()
```

#### SetRewardStartCaps
```angelscript
ITown@ SetRewardStartCaps(uint caps)
```

#### SetMilitiaEnabled
```angelscript
ITown@ SetMilitiaEnabled()
```

#### SetCaptureArea
```angelscript
ITown@ SetCaptureArea(IPolygon@ capturearea)
```

#### SetHour
```angelscript
ITown@ SetHour(uint hour)
```

#### SetTownID
```angelscript
ITown@ SetTownID(uint id)
```

#### SetMapID
```angelscript
ITown@ SetMapID(uint id)
```

#### SetTownLeader
Not used

```angelscript
ITown@ SetTownLeader(Critter@ leader)
```

#### SetVersion
```angelscript
ITown@ SetVersion(uint version)
```

#### SetTownLeader
Not used

```angelscript
ITown@ SetTownLeader(uint id)
```

#### SetBaseRewardValue
```angelscript
ITown@ SetBaseRewardValue(uint baseValue)
```

#### SetSpeechModifier
```angelscript
ITown@ SetSpeechModifier(int modifier)
```

#### SetLimboContainer
```angelscript
ITown@ SetLimboContainer(Item@ container)
```

#### SetRewardContainer
```angelscript
ITown@ SetRewardContainer(Item@ container)
```

#### SetInfluenceMemberRequirement
```angelscript
ITown@ SetInfluenceMemberRequirement(uint number)
```

#### SetTotalMemberRequirement
```angelscript
ITown@ SetTotalMemberRequirement(uint number)
```

#### SetNearbyMemberRequirement
```angelscript
ITown@ SetNearbyMemberRequirement(uint number)
```

#### SetControlMemberRequirement
```angelscript
ITown@ SetControlMemberRequirement(uint number)
```

#### AddMoney
```angelscript
void AddMoney(int money)
```

#### GetMoney
```angelscript
int GetMoney()
```

#### GetLocation
```angelscript
Location@ GetLocation()
```


## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| bags | `array<uint>` |  |  |
| mil_modoc_pids | `array<uint>` |  |  |
| mil_klamath_pids | `array<uint>` |  |  |
| mil_bh_pids | `array<uint>` |  |  |
| mil_den_pids | `array<uint>` |  |  |
| mil_redding_pids | `array<uint>` |  |  |
| mil_gecko_pids | `array<uint>` |  |  |

## Functions

### InitMilitia

```angelscript
void InitMilitia()
```

### item_init

```angelscript
void item_init(Item& item, bool firstTime)
```

### _UseRewardContainer

Executed when opening reward chest

```angelscript
bool _UseRewardContainer(Item& item, Critter& crit, int skill)
```

### IsTCTown

```angelscript
bool IsTCTown(Map@ map)
```

### RetrieveTownId

```angelscript
uint RetrieveTownId(Map@ map)
```

### RetrieveTownId

```angelscript
uint RetrieveTownId(Critter& critter)
```

### RetrieveTown

```angelscript
ITown@ RetrieveTown(Map& map)
```

### RetrieveTown

```angelscript
ITown@ RetrieveTown(Critter& critter)
```

### ValidTown

```angelscript
bool ValidTown(ITown@ town)
```

### GainControl

```angelscript
void GainControl(Critter& player)
```

### GetNearMembers

```angelscript
uint GetNearMembers(Critter& player)
```

### GetMembersInZone

```angelscript
uint GetMembersInZone(Critter& player, uint factionId)
```

### IsPolicy

```angelscript
bool IsPolicy(Critter& player, uint policy)
```

### IsControllingTown

```angelscript
bool IsControllingTown(Critter& player)
```

### d_IsNotControllingTown

```angelscript
bool d_IsNotControllingTown(Critter& player, Critter@ npc, int val)
```

### d_IsControllingTown

```angelscript
bool d_IsControllingTown(Critter& player, Critter@ npc, int val)
```

### d_CanRecruitMilitia

```angelscript
bool d_CanRecruitMilitia(Critter& player, Critter@ npc)
```

### d_CanChangeLaws

```angelscript
bool d_CanChangeLaws(Critter& player, Critter@ npc)
```

### d_CanTakeOver

General check, here any conditions be added, it's possible to disable TC feature here.

```angelscript
bool d_CanTakeOver(Critter& player, Critter@ npc)
```

### d_IsBigEnoughFaction

```angelscript
bool d_IsBigEnoughFaction(Critter& player, Critter@ npc, int val)
```

### d_IsEnoughMembersPresent

```angelscript
bool d_IsEnoughMembersPresent(Critter& player, Critter@ npc, int val)
```

### d_CanBecomeMilitia

```angelscript
bool d_CanBecomeMilitia(Critter& player, Critter@ npc)
```

### d_IsMilitiaNotFull

```angelscript
bool d_IsMilitiaNotFull(Critter& player, Critter@ npc)
```

### r_FriendlyFactionsBrowse

```angelscript
void r_FriendlyFactionsBrowse(Critter& player, Critter@ npc, int val)
```

### r_SetFriendlyFactionsMode

```angelscript
void r_SetFriendlyFactionsMode(Critter& player, Critter@ npc, int val)
```

### dlg_ShowMilitiaCost

```angelscript
void dlg_ShowMilitiaCost(Critter& player, Critter@ npc, string@ text)
```

### dlg_ManipulateFriendlyFactions

```angelscript
void dlg_ManipulateFriendlyFactions(Critter& player, Critter@ npc, string@ say)
```

### dlg_ShowFriendlyFactions

```angelscript
void dlg_ShowFriendlyFactions(Critter& player, Critter@ npc, string@ text)
```

### AlertMilitia

```angelscript
bool AlertMilitia(Critter& cr)
```

### r_ClaimControl

```angelscript
uint r_ClaimControl(Critter& player, Critter@ npc, int val)
```

### SpawnInitMilitia

```angelscript
void SpawnInitMilitia(Map@ map)
```

### SelectBag

Take some bag militia can use

```angelscript
int SelectBag(uint crpid)
```

### dlg_ShowFactionName

```angelscript
void dlg_ShowFactionName(Critter& player, Critter@ npc, string@ text)
```

### CountMilitia

```angelscript
int CountMilitia(Map@ map)
```

### GetMilitiaPid

```angelscript
int GetMilitiaPid(uint MapProtoId)
```

### r_ModifyInfluenceBuffer

```angelscript
void r_ModifyInfluenceBuffer(Critter& cr, Critter@ npc, int value)
```

### ModifyInfluenceBuffer

influence buffer filled by shovelling crap mining ore quest crafting (not implemented)

```angelscript
void ModifyInfluenceBuffer(Critter& cr, int value)
```

### ClearInfluenceBuffer

```angelscript
void ClearInfluenceBuffer(Critter& cr)
```

### FlushInfluenceBuffer

```angelscript
void FlushInfluenceBuffer(Critter& cr, ITown@ town)
```

### AddMilitia

```angelscript
bool AddMilitia(Map@ map)
```

### r_RecruitMilitia

```angelscript
uint r_RecruitMilitia(Critter& player, Critter@ npc)
```

### r_GainControl

```angelscript
void r_GainControl(Critter& player, Critter@ npc, int val)
```

### r_SetPolicy

```angelscript
void r_SetPolicy(Critter& player, Critter@ npc, int policy, int value)
```

### d_IsPolicy

```angelscript
bool d_IsPolicy(Critter& player, Critter@ npc, int policy)
```

### d_IsNotPolicy

```angelscript
bool d_IsNotPolicy(Critter& player, Critter@ npc, int policy)
```

### dlg_ShowPolicies

```angelscript
void dlg_ShowPolicies(Critter& player, Critter@ npc, string@ text)
```

### dlg_ShowTownName

```angelscript
void dlg_ShowTownName(Critter& player, Critter@ npc, string@ text)
```

### d_InfluenceAtLeast

```angelscript
bool d_InfluenceAtLeast(Critter& player, Critter@ npc, int influence)
```

### d_IsVersion

```angelscript
bool d_IsVersion(Critter& player, Critter@ npc, int version)
```

### d_GainControl

When we need to set the control at the beginning of the dialog

```angelscript
bool d_GainControl(Critter& player, Critter@ npc, int val)
```

### d_PresentAlmost

True if one more present faction member implies that the conditions are met

```angelscript
bool d_PresentAlmost(Critter& player, Critter@ npc, int val)
```

### d_MembersAlmost

True if one more faction member implies that the conditions are met

```angelscript
bool d_MembersAlmost(Critter& player, Critter@ npc, int val)
```

### r_TakeoverCheck

```angelscript
uint r_TakeoverCheck(Critter& player, Critter@ npc, int val)
```

### _LeaderAttacked

```angelscript
bool _LeaderAttacked(Critter& cr, Critter& attacker)
```

### _LeaderDead

```angelscript
void _LeaderDead(Critter& cr, Critter@ killer)
```

### setinfluence

```angelscript
void setinfluence(Critter& cr, int factionId, int value, int)
```

### TC_QuestExpReward

```angelscript
void TC_QuestExpReward(Critter& player, int val)
```

### TC_QuestCapsReward

```angelscript
void TC_QuestCapsReward(Critter& player, int caps)
```

### TC_CraftExpReward

```angelscript
void TC_CraftExpReward(Critter& player, int exp)
```

### TC_CraftCapsReward

```angelscript
void TC_CraftCapsReward(Critter& player, int caps)
```

### TC_BarterReward

```angelscript
void TC_BarterReward(Critter& player, int caps)
```

### TC_ScavengeReward

```angelscript
void TC_ScavengeReward(Critter& player, uint pid, uint cnt)
```

### TC_DialogTradeReward

```angelscript
void TC_DialogTradeReward(Critter& player, int caps)
```

### CreateTown

```angelscript
ITown@ CreateTown(string Name)
```


