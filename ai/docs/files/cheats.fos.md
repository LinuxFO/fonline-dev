---
title: cheats.fos
---

# cheats.fos

## Includes

- `_animation.fos`
- `_ai.fos`
- `_basetypes.fos`
- `_macros.fos`
- `_scripts.fos`
- `_vals.fos`
- `broadcast_h.fos`
- `buffer_h.fos`
- `cheats_core_h.fos`
- `combat_h.fos`
- `combat_msg.fos`
- `config_file_h.fos`
- `critter_age_h.fos`
- `debug_h.fos`
- `economy_h.fos`
- `entire.fos`
- `follower_common_h.fos`
- `follower_h.fos`
- `factions_h.fos`
- `factions_bases_h.fos`
- `gm.fos`
- `lexems_h.fos`
- `mapdata_h.fos`
- `minigames_h.fos`
- `npc_ai.fos`
- `npc_common_h.fos`
- `npc_names_h.fos`
- `npc_planes_h.fos`
- `serializator.fos`
- `town_h.fos`
- `traps_h.fos`
- `triggers_h.fos`
- `utils_h.fos`
- `world_common_h.fos`
- `worldmap_h.fos`
- `_colors.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| GETACCESS_CFG | `"config/GetAccess.cfg"` |  |
| CHEATS_CFG | `"config/Cheats.cfg"` |  |
| CFG_TRACKING | `"Tracking"` |  |
| MODE_EXT_GOD | `(0x00020000)` |  |
| _SetSpawner | `\` |  |
| _SetSpawnerLegit | `\` |  |
| _GetSpawner | `# (__item) _AsLegit(__item.Val9)` |  |
| WT_NO_ITEMS | `(0x01)` |  |
| WT_DELETE_ITEMS | `(0x02)` |  |
| WT_NO_FOLLOWERS | `(0x04)` |  |
| BLOCKER_VIS | `(PID_PLAYERS_EAR)` |  |
| BLOCKER_INVIS | `(PID_UNVISIBLE_BLOCK)` |  |
| SCOLOR_ERROR | `"|0xCC0000 "` | SAY COLORS  |
| SCOLOR_ERRORB | `"|0xFF4400 "` |  |
| SCOLOR_HELP | `"|0xBBBBBB "` |  |
| SCOLOR_HELPH | `"|0xFFFFFF "` |  |
| SCOLOR_HELPB | `"|0x00FFFF "` |  |
| SCOLOR_HELPI | `"|0x00BBBB "` |  |
| _PrintPlayer | `# (array, idx)GetSafePlayerName(array[idx].Id) + " (" + array[idx].Id + ")" + "(" + array[idx].GetMapId() + ") - " + GetAuthString(array[idx])` |  |
| AURA_FLAG_VISIBLE | `(0x01)` |  |
| AURA_FLAG_NEED_CRITTERS | `(0x02)` |  |
| AURA_FLAG_KNOCKBACK | `(0x04)` |  |
| AURA_FLAG_KNOCKBACK_SIMPLE | `(0x08)` |  |
| AURA_FLAG_IGNORE_ADMINS | `(0x10)` |  |
| AURA_FLAG_GRAVITY_PULL | `(0x20)` |  |

## Classes

### CNPC

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| protoId | `uint` |  |  |
| dialogId | `uint` |  |  |
| names | `array<string>` |  |  |

**Methods**

#### IsImportant
```angelscript
bool IsImportant(Critter& cr)
```

#### Name
```angelscript
CNPC@ Name(string& name)
```

### FakeCombat

**Methods**

#### Clear
```angelscript
FakeCombat@ Clear()
```

#### Target
```angelscript
FakeCombat@ Target(Critter& cr)
```

#### Miss
```angelscript
FakeCombat@ Miss()
```

#### CritMiss
```angelscript
FakeCombat@ CritMiss(uint effects)
```

#### CritMissDamage
```angelscript
FakeCombat@ CritMissDamage(uint effects, uint damage)
```

#### Oops
```angelscript
FakeCombat@ Oops(uint who2)
```

#### Hit
```angelscript
FakeCombat@ Hit(uint damage)
```

#### HitRandomly
```angelscript
FakeCombat@ HitRandomly()
```

#### HitDead
```angelscript
FakeCombat@ HitDead(uint damage)
```

#### AimedHit
```angelscript
FakeCombat@ AimedHit(uint location, uint damage)
```

#### AimedHitDead
```angelscript
FakeCombat@ AimedHitDead(uint location, uint damage)
```

#### CritHit
```angelscript
FakeCombat@ CritHit(uint damage, uint effect, uint message)
```

#### CritHitDead
```angelscript
FakeCombat@ CritHitDead(uint damage, uint effect, uint message)
```

#### CritAimedHit
```angelscript
FakeCombat@ CritAimedHit(uint location, uint damage, uint effect, uint message)
```

#### CritAimedHitDead
```angelscript
FakeCombat@ CritAimedHitDead(uint location, uint damage, uint effect, uint message)
```

#### Send
```angelscript
bool Send()
```

#### Send
```angelscript
bool Send(Critter& cr)
```

### CRiddle

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| id | `uint` |  |  |
| name | `string` |  |  |
| author | `string` |  |  |
| type | `int` |  |  |
| state | `int` |  |  |
| question | `array<string>` |  |  |
| answer | `array<string>` |  |  |
| reward | `array<uint>` |  |  |
| reward_flags | `int` |  |  |

**Methods**

#### Load
```angelscript
void Load(Serializator@ riddle)
```

#### Save
```angelscript
void Save(string prefix)
```


## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| CheatsInitialized | `bool` | `false` | globals |
| Maps | `dictionary` |  | list of maps identifiers |
| eventItems | `array<int>` |  | items and critters spawned during event |
| eventCritters | `array<int>` |  |  |
| authName | `array<string>` |  |  |
| authId | `array<uint>` |  |  |
| serializer | `[Serializator](serializator.fos.md)` |  |  |

## Functions

### SetMapId

```angelscript
void SetMapId(string location, uint mapprotoid)
```

### RefreshAliases

```angelscript
void RefreshAliases(Critter& player, int, int, int)
```

### SetAliases

```angelscript
void SetAliases()
```

### ImportantNpc

```angelscript
CNPC@ ImportantNpc(uint protoId, uint dialogId)
```

### SetImportantNpcs

```angelscript
void SetImportantNpcs()
```

### GuardNotLegit

Checks if item can be used by critter with optional deletion if not. Returns true if item is illegal (not-legit item in legit map or not-legit item in not-legit map, if the critter carries a stackable legit item with the same pid). Called on item transfers and picking up / skills. 

```angelscript
bool GuardNotLegit(Critter@ cr, Item@ item, bool deleteItem)
```

### RemoveNotLegit

Removes all not legit items from a critter. Called when a critter moves from a not-legit map to WM or to a legit map. 

```angelscript
void RemoveNotLegit(Critter@ cr)
```

### cheatGetOption

```angelscript
string cheatGetOption(array<string@>@ command, int& option, string optionSwitch)
```

### cheatGetOption

```angelscript
string cheatGetOption(array<string@>@ command, uint& option, string optionSwitch)
```

### cheatGetOption

```angelscript
string cheatGetOption(array<string@>@ command, int16& option, string optionSwitch)
```

### cheatGetOption

```angelscript
string cheatGetOption(array<string@>@ command, uint16& option, string optionSwitch)
```

### cheatGetOption

```angelscript
string cheatGetOption(array<string@>@ command, bool& option, string optionSwitch)
```

### InitCheats

```angelscript
void InitCheats(bool fromGame)
```

### SaveCheats

```angelscript
void SaveCheats()
```

### IsAllowed

 Checks if player's authorization allows for given command 

```angelscript
bool IsAllowed(uint playerId, const string& command)
```

### IsInArray

```angelscript
bool IsInArray(array<string>& arr, string& str)
```

### GodOfTheRealm

```angelscript
bool GodOfTheRealm(uint id)
```

### WrathOfTheGod

```angelscript
bool WrathOfTheGod(Critter& di)
```

### god

```angelscript
void god(Critter& cr, int, int, int)
```

### mortal

```angelscript
void mortal(Critter& cr, int, int, int)
```

### adminlook

```angelscript
void adminlook(Critter& cr, int p, int r, int)
```

### normallook

```angelscript
void normallook(Critter& cr, int p, int r, int)
```

### imsospeed

```angelscript
void imsospeed(Critter& cr, int p0, int p1, int p2)
```

### vals

```angelscript
void vals(Critter& cr, int, int, int id)
```

### Fly

```angelscript
void Fly(Critter& cr, int pid, int p1, int p2)
```

### grab

```angelscript
void grab(Critter& player, int, int, int id)
```

### checkparam2

```angelscript
void checkparam2(Critter& cr, int p, int r, int)
```

### mapdata

```angelscript
void mapdata(Critter& cr, int p, int, int)
```

### setmapdata

```angelscript
void setmapdata(Critter& cr, int p, int r, int)
```

### massteleport

```angelscript
void massteleport(Critter& cr, int p0, int p1, int p2)
```

### GetAuthed

```angelscript
string GetAuthed(uint id)
```

### AuthedInfo

```angelscript
string AuthedInfo(uint id)
```

### SetAuthed

```angelscript
void SetAuthed(uint id, string name)
```

### RemoveAuthed

```angelscript
void RemoveAuthed(uint id)
```

### GetRandomDeathAnimation

```angelscript
uint GetRandomDeathAnimation()
```

### GenderString

helper

```angelscript
string GenderString(Critter& player, string male, string female, string it)
```

### ExecGiveCommand

 Execute give command  give item_pid number_of_items 

```angelscript
void ExecGiveCommand(array<string@>@ command, Critter@ player, Critter@ target)
```

### ExecGiveKeyCommand

 GiveKey command  givekey keyid number 

```angelscript
void ExecGiveKeyCommand(array<string@>@ command, Critter@ player, Critter@ target)
```

### ExecAddNpcCommand

 ExecAddNpcCommand  Spawns NPC with default parameters AddNpc pid deltaX deltaY coords of NPC are calculated basing on players position and delta params  Switches used:

```angelscript
void ExecAddNpcCommand(array<string@>@ command, Critter@ player, Critter@ target, bool isMob, bool isFollower)
```

### ExecSpawnItemCommand

* * Spawns item on map. 

```angelscript
void ExecSpawnItemCommand(array<string@>@ command, Critter@ player, Critter@ target)
```

### ExecLockCommand

* * Locks doors/ container at given coords. 

```angelscript
void ExecLockCommand(array<string@>@ command, Critter@ player, Critter@ target)
```

### ExecCloneCommand

* * Clone another critter. Warning: there is no easy way to undo this operation (yet). 

```angelscript
void ExecCloneCommand(array<string@>@ command, Critter@ player, Critter@ target)
```

### e_ExecCloneItems

```angelscript
uint e_ExecCloneItems(array<uint>@ values)
```

### ExecSpawnCarCommand

* * Spawns car. 

```angelscript
void ExecSpawnCarCommand(array<string@>@ command, Critter@ player, Critter@ target)
```

### ExecCreateLocationCommand

 Calls CreateLocation function  createlocation pid /* x y */ x y are chosen randomly based on player's world coords

```angelscript
void ExecCreateLocationCommand(array<string@>@ command, Critter@ player)
```

### ExecDeleteLocationCommand

* * Deletes location player is in. 

```angelscript
void ExecDeleteLocationCommand(array<string@>@ command, Critter@ player)
```

### ExecChangeRankCommand

 Changing rank of the player in the faction db  

```angelscript
void ExecChangeRankCommand(array<string@>@ command, Critter@ player, Critter@ target)
```

### ExecChangeFactionCommand

 Changing faction player belongs  

```angelscript
void ExecChangeFactionCommand(array<string@>@ command, Critter@ player, Critter@ target)
```

### ExecShowVarsCommand

 Changing faction of the player in the faction db  

```angelscript
void ExecShowVarsCommand(array<string@>@ command, Critter@ player, Critter@ target)
```

### ExecRemoveFactionCommand

* * Removing faction. 

```angelscript
void ExecRemoveFactionCommand(array<string@>@ command, Critter@ player)
```

### ParseFactionBaseLocationId

```angelscript
bool ParseFactionBaseLocationId(const string& fparam, uint& out locId)
```

### ExecLocVisCommand

* * Changes the visilibity of given location. 

```angelscript
void ExecLocVisCommand(array<string@>@ command, Critter@ player, Critter@ target, bool show)
```

### ExecSetTimeoutCommand

 Sets the TRANSFER timeout for safe travels  

```angelscript
void ExecSetTimeoutCommand(array<string@>@ command, Critter@ player, Critter@ target)
```

### ExecGetVarCommand

 Shows the value of the local variable specified in the parameter 

```angelscript
void ExecGetVarCommand(array<string@>@ command, Critter@ player, uint targetId)
```

### ExecSetVarCommand

 Sets the value of the local variable specified in the parameter 

```angelscript
void ExecSetVarCommand(array<string@>@ command, Critter@ player, uint targetId)
```

### ExecGetUVarCommand

 Shows the value of the specified unique variable for the critters in sight default master-slave: critter-player with switch r, player become master, critter slave 

```angelscript
void ExecGetUVarCommand(array<string@>@ command, Critter@ player, Critter@ target)
```

### ExecSetUVarCommand

 Sets the value of the unique variable for the critter in front of player 

```angelscript
void ExecSetUVarCommand(array<string@>@ command, Critter@ player, Critter@ target)
```

### ExecKillCommand

 Kills the critter in front of player, without consequences or kills player with specified name

```angelscript
void ExecKillCommand(array<string@>@ command, Critter@ player, Critter@ target)
```

### ExecRegisterFactionCommand

 Register new faction with specified id and name 

```angelscript
void ExecRegisterFactionCommand(array<string@>@ command, Critter@ player)
```

### ExecTeleportCommand

 Teleports target to some location (or target and his team) 

```angelscript
void ExecTeleportCommand(array<string@>@ command, Critter@ player, Critter@ target, bool team)
```

### ExecTeleporterCommand

```angelscript
void ExecTeleporterCommand(array<string@>@ command, Critter@ player)
```

### ExecShiftCommand

 Shifts player (and his team) few hexes in the specific direction 

```angelscript
void ExecShiftCommand(array<string@>@ command, Critter@ player, Critter@ target, bool team, bool random)
```

### Teleport

 Summons target (and his team) near the player (summoner)  helper

```angelscript
bool Teleport(Critter@ player, Critter@ target, bool Safe)
```

### ExecSummonCommand

```angelscript
void ExecSummonCommand(array<string@>@ command, Critter@ player, Critter@ target, bool team)
```

### ExecDismissCommand

 returns target (and his team) to location from which they were summoned 

```angelscript
void ExecDismissCommand(array<string@>@ command, Critter@ player, Critter@ target, bool team)
```

### ExecGoToCommand

* * Teleports to given target critter. 

```angelscript
void ExecGoToCommand(array<string@>@ command, Critter@ player, Critter@ target, bool team)
```

### ExecDamageCommand

```angelscript
void ExecDamageCommand(array<string@>@ command, Critter@ player, Critter@ target)
```

### ExecSlapCommand

```angelscript
void ExecSlapCommand(array<string@>@ command, Critter@ player, Critter@ target)
```

### ExecMassSlapCommand

```angelscript
void ExecMassSlapCommand(array<string@>@ command, Critter@ player, Critter@ target)
```

### ExecSetHPCommand

```angelscript
void ExecSetHPCommand(array<string@>@ command, Critter@ player, Critter@ target)
```

### ExecExplodeCommand

```angelscript
void ExecExplodeCommand(array<string@>@ command, Critter@ player, Critter@ target)
```

### ExecAirstrikeCommand

```angelscript
void ExecAirstrikeCommand(array<string@>@ command, Critter@ player, Critter@ target)
```

### ExecAltsCommand

```angelscript
void ExecAltsCommand(array<string@>@ command, Critter@ player)
```

### ExecListPlayersCommand

```angelscript
void ExecListPlayersCommand(array<string@>@ command, Critter@ player)
```

### ExecCritterInfoCommand

```angelscript
void ExecCritterInfoCommand(array<string@>@ command, Critter@ player, Critter@ target)
```

### ExecZeroExtCommand

```angelscript
void ExecZeroExtCommand(array<string@>@ command, Critter@ player, Critter@ target)
```

### ExecGodCommand

  

```angelscript
void ExecGodCommand(array<string@>@ command, Critter@ player)
```

### ExecIDKFACommand

```angelscript
void ExecIDKFACommand(array<string@>@ command, Critter@ player, Critter@ target)
```

### ExecCleanupCommand

```angelscript
void ExecCleanupCommand(array<string@>@ command, Critter@ player)
```

### ControlNpc

 Controling npcs 

```angelscript
bool ControlNpc(Critter& npc, string& cmd, Critter& target, Critter& player, bool setHome)
```

### ExecControlNpcCommand

 Controling npc 

```angelscript
void ExecControlNpcCommand(array<string@>@ command, Critter@ player, Critter@ target)
```

### ExecControlMobsCommand

 Controling all npcs in sight 

```angelscript
void ExecControlMobsCommand(array<string@>@ command, Critter@ player, Critter@ target)
```

### ExecDeathmatchCommand

```angelscript
void ExecDeathmatchCommand(array<string@>@ command, Critter@ player)
```

### ExecInspectCommand

 Sends debug message to nearby npcs 

```angelscript
void ExecInspectCommand(array<string@>@ command, Critter@ player)
```

### ExecXpCommand

 Xp reward 

```angelscript
void ExecXpCommand(array<string@>@ command, Critter& player, Critter@ target, bool team)
```

### ExecKarmaCommand

 Karma modification 

```angelscript
void ExecKarmaCommand(array<string@>@ command, Critter& player, Critter@ target, bool team)
```

### ExecPlayerKarmaCommand

```angelscript
void ExecPlayerKarmaCommand(array<string@>@ command, Critter& player, Critter@ target, bool team)
```

### ExecIrradiateCommand

 Radiation 

```angelscript
void ExecIrradiateCommand(array<string@>@ command, Critter& player, Critter@ target)
```

### ExecPoisonCommand

 Poison 

```angelscript
void ExecPoisonCommand(array<string@>@ command, Critter& player, Critter@ target)
```

### ExecFactionInfoCommand

 list factions 

```angelscript
void ExecFactionInfoCommand(array<string@>@ command, Critter& player, Critter@ target, bool all)
```

### ExecFactionOnlineCommand

```angelscript
void ExecFactionOnlineCommand(array<string@>@ command, Critter& player)
```

### ExecFindItemsCommand

```angelscript
void ExecFindItemsCommand(array<string@>@ command, Critter& player)
```

### ExecSayCommand

 Forces target to say specific message 

```angelscript
void ExecSayCommand(array<string@>@ command, Critter& player, Critter@ target, int sayType)
```

### ExecSetAnimCommand

```angelscript
void ExecSetAnimCommand(array<string@>@ command, Critter& player, Critter@ target, bool mass)
```

### ExecDisguiseCommand

 Changes critter sprites 

```angelscript
void ExecDisguiseCommand(array<string@>@ command, Critter& player, Critter@ target)
```

### ExecDisguiseInfoCommand

```angelscript
void ExecDisguiseInfoCommand(array<string@>@ command, Critter& player)
```

### ExecConditionCommand

```angelscript
void ExecConditionCommand(array<string@>@ command, Critter& player, Critter@ target)
```

### ExecBroadcastCommand

```angelscript
void ExecBroadcastCommand(array<string@>@ command, Critter& player)
```

### ExecSetExpModCommand

```angelscript
void ExecSetExpModCommand(array<string@>@ command, Critter& player)
```

### ExecSetFactionCommand

```angelscript
void ExecSetFactionCommand(array<string@>@ command, Critter& player, Critter@ target)
```

### ExecSetLocVisibility

```angelscript
void ExecSetLocVisibility(array<string@>@ command, Critter& player)
```

### ExecSetRain

```angelscript
void ExecSetRain(array<string@>@ command, Critter& player)
```

### ExecSetMapDataCommand

```angelscript
void ExecSetMapDataCommand(array<string@>@ command, Critter& player)
```

### ExecSetTurnbasedCombat

```angelscript
void ExecSetTurnbasedCombat(Critter& player, bool enable)
```

### ExecMapDismantling

```angelscript
void ExecMapDismantling(Critter& player, bool enable)
```

### ExecMapPvp

```angelscript
void ExecMapPvp(Critter& player, bool enable)
```

### ExecMapGrids

```angelscript
void ExecMapGrids(Critter& player, bool enable)
```

### ExecMapLootDrop

```angelscript
void ExecMapLootDrop(Critter& player, string mode)
```

### ExecClearEnemyStackCommand

```angelscript
void ExecClearEnemyStackCommand(array<string@>@ command, Critter& player, Critter@ target, bool all)
```

### ExecCheckBankCommand

```angelscript
void ExecCheckBankCommand(array<string@>@ command, Critter& player)
```

### ExecCheckBanksCommand

```angelscript
void ExecCheckBanksCommand(array<string@>@ command, Critter& player)
```

### PrintAccountInfo

```angelscript
void PrintAccountInfo(Critter& player, uint bank, uint acc, uint filtersum, bool verbose)
```

### ExecCheckBankAccount

```angelscript
void ExecCheckBankAccount(array<string@>@ command, Critter& player, bool All)
```

### ExecBankMoney

```angelscript
void ExecBankMoney(array<string@>@ command, Critter& player, bool add)
```

### ExecCheckTownCommand

```angelscript
void ExecCheckTownCommand(array<string@>@ command, Critter& player)
```

### ExecGainTownControlCommand

```angelscript
void ExecGainTownControlCommand(array<string@>@ command, Critter& player)
```

### ExecResetTownCommand

```angelscript
void ExecResetTownCommand(array<string@>@ command, Critter& player, bool all)
```

### _Kill

 Event handler for deathincarnate command 

```angelscript
void _Kill(Critter& killer, Critter& victim)
```

### ExecSetPerkCommand

 Perk cheats 

```angelscript
void ExecSetPerkCommand(array<string@>@ command, Critter& player, Critter& target)
```

### ExecPerkAdjust

```angelscript
void ExecPerkAdjust(array<string@>@ command, Critter@ player, Critter@ target)
```

### ExecProfAdjust

```angelscript
void ExecProfAdjust(array<string@>@ command, Critter@ player, Critter@ target)
```

### ExecCriticalChance

```angelscript
void ExecCriticalChance(array<string@>@ command, Critter@ player, Critter@ target)
```

### ExecSetReputationCommand

```angelscript
void ExecSetReputationCommand(array<string@>@ command, Critter@ player, Critter@ target)
```

### ExecResetReputationsCommand

```angelscript
void ExecResetReputationsCommand(array<string@>@ command, Critter@ player, Critter@ target)
```

### ExecSafeRegenCommand

* * Regenerates location, keeps rentable domiciles containers 

```angelscript
void ExecSafeRegenCommand(array<string@>@ command, Critter@ player)
```

### ExecRemoveItemsCommand

* * Removes certain items from current map or globally. 

```angelscript
void ExecRemoveItemsCommand(array<string@>@ command, Critter@ player)
```

### ExecCountItemsCommand

* * Count items with given pid. 

```angelscript
void ExecCountItemsCommand(array<string@>@ command, Critter@ player)
```

### ExecVirtualMoneyCommand

* * Counts the item of value kept in banks/encounter store. 

```angelscript
void ExecVirtualMoneyCommand(array<string@>@ command, Critter@ player)
```

### ExecZoneCommand

* * Checking/modifying zones' values. 

```angelscript
void ExecZoneCommand(array<string@>@ command, Critter@ player)
```

### ExecSuicideCommand

```angelscript
void ExecSuicideCommand(array<string@>@ command, Critter@ player)
```

### ExecGetLeaderTimeCommand

```angelscript
void ExecGetLeaderTimeCommand(array<string@>@ command, Critter@ player)
```

### ExecGetClaimTimeCommand

```angelscript
void ExecGetClaimTimeCommand(array<string@>@ command, Critter@ player)
```

### ExecGetClaimCommand

```angelscript
void ExecGetClaimCommand(array<string@>@ command, Critter@ player)
```

### ExecMakeEncounterCommand

```angelscript
void ExecMakeEncounterCommand(array<string@>@ command, Critter@ player)
```

### ExecMapInfoCommand

```angelscript
void ExecMapInfoCommand(array<string@>@ command, Critter@ player)
```

### ExecGetLeaderCommand

```angelscript
void ExecGetLeaderCommand(array<string@>@ command, Critter@ player)
```

### ExecClearTimeoutsCommand

```angelscript
void ExecClearTimeoutsCommand(array<string@>@ command, Critter@ player, Critter@ target)
```

### ExecClearAllTimeoutsCommand

```angelscript
void ExecClearAllTimeoutsCommand(array<string@>@ command, Critter@ player)
```

### ExecDeathIncarnateCommand

```angelscript
void ExecDeathIncarnateCommand(array<string@>@ command, Critter@ player, Critter@ target)
```

### ExecNormalDeadlyCommand

```angelscript
void ExecNormalDeadlyCommand(array<string@>@ command, Critter@ player, Critter@ target)
```

### ExecMoveCommand

```angelscript
void ExecMoveCommand(array<string@>@ command, Critter@ player, Critter@ target)
```

### ExecKillMobsCommand

```angelscript
void ExecKillMobsCommand(array<string@>@ command, Critter@ player)
```

### ExecRespawnCommand

```angelscript
void ExecRespawnCommand(array<string@>@ command, Critter@ player, Critter@ target)
```

### ExecRespawnAllCommand

```angelscript
void ExecRespawnAllCommand(array<string@>@ command, Critter@ player)
```

### ExecHealCommand

```angelscript
void ExecHealCommand(array<string@>@ command, Critter@ player, Critter@ target)
```

### ExecHealAllCommand

```angelscript
void ExecHealAllCommand(array<string@>@ command, Critter@ player)
```

### ExecRespawnAllPlayersCommand

```angelscript
void ExecRespawnAllPlayersCommand(array<string@>@ command, Critter@ player, Critter@ target)
```

### ExecDevEnableCommand

```angelscript
void ExecDevEnableCommand(array<string@>@ command, Critter@ player)
```

### ExecAntiblockCommand

```angelscript
void ExecAntiblockCommand(array<string@>@ command, Critter@ player)
```

### ExecSpawnPointCommand

* * Places dynamic spawnpoint. 

```angelscript
void ExecSpawnPointCommand(array<string@>@ command, Critter@ player)
```

### ExecKillerAdminCommand

```angelscript
void ExecKillerAdminCommand(array<string@>@ command, Critter@ player)
```

### ExecHideMapCommand

```angelscript
void ExecHideMapCommand(array<string@>@ command, Critter@ player)
```

### ExecClearAllIllegalFlagsCommand

```angelscript
void ExecClearAllIllegalFlagsCommand(array<string@>@ command, Critter@ player)
```

### ExecListAuthenticatedCommand

```angelscript
void ExecListAuthenticatedCommand(array<string@>@ command, Critter@ player)
```

### ExecResetAllDisguisesCommand

```angelscript
void ExecResetAllDisguisesCommand(array<string@>@ command, Critter@ player)
```

### ExecDropDrugsCommand

 TODO: abused, addictions should be kept or command disabled 

```angelscript
void ExecDropDrugsCommand(array<string@>@ command, Critter@ player, Critter@ target)
```

### ExecZonePlayersCommand

```angelscript
void ExecZonePlayersCommand(array<string@>@ command, Critter@ player)
```

### ExecListCommandsCommand

```angelscript
void ExecListCommandsCommand(array<string@>@ command, Critter@ player)
```

### GMTrack

```angelscript
uint GMTrack(uint targetId, string@ message)
```

### GetCritterArgument

```angelscript
Critter@ GetCritterArgument(array<string@>& command)
```

### ExecTrackPlayerCommand

```angelscript
void ExecTrackPlayerCommand(array<string@>@ command, Critter@ player, Critter@ target)
```

### ExecStopTrackPlayerCommand

```angelscript
void ExecStopTrackPlayerCommand(array<string@>@ command, Critter@ player, Critter@ target)
```

### ExecListTrackedPlayersCommand

```angelscript
void ExecListTrackedPlayersCommand(array<string@>@ command, Critter@ player)
```

### ExecRotateCommand

```angelscript
void ExecRotateCommand(array<string@>@ command, Critter@ player, Critter@ target)
```

### ExecStartEventCommand

```angelscript
void ExecStartEventCommand(array<string@>@ command, Critter@ player)
```

### ExecStopEventCommand

```angelscript
void ExecStopEventCommand(array<string@>@ command, Critter@ player)
```

### PrintTentList

```angelscript
void PrintTentList(Critter& player, Critter& target, bool short)
```

### ExecTentInfoCommand

```angelscript
void ExecTentInfoCommand(array<string@>@ command, Critter@ player, Critter@ target)
```

### ExecTentListCommand

```angelscript
void ExecTentListCommand(array<string@>@ command, Critter@ player)
```

### ExecListMapsCommand

```angelscript
void ExecListMapsCommand(array<string@>@ command, Critter@ player)
```

### ExecShowHandsCommand

```angelscript
void ExecShowHandsCommand(array<string@>@ command, Critter@ player, Critter@ target)
```

### ExecNameToIdCommand

```angelscript
void ExecNameToIdCommand(array<string@>@ command, Critter@ player, Critter@ target)
```

### ExecIdToNameCommand

```angelscript
void ExecIdToNameCommand(array<string@>@ command, Critter@ player)
```

### ExecListFollowersCommand

```angelscript
void ExecListFollowersCommand(array<string@>@ command, Critter@ player, Critter@ target)
```

### BlockerSetProto

Sets / changes prototype of a blocker: visible oe invisible Called after a blocker is created or when visibility changes Returns false if can't change prototype 

```angelscript
bool BlockerSetProto(Item@ blocker, bool visible)
```

### BlockerCreate

Creates a single blocker This function should be used by all methods of creating blockers Returns false if fails to create a blocker. 

```angelscript
bool BlockerCreate(Critter@ creator, Map@ map, uint16 x, uint16 y, int group, bool safe, bool visible)
```

### BlockerDelete

Deletes a group of blockers or all blockers with specific pid 

```angelscript
void BlockerDelete(Critter@ deleter, uint16 pid, uint group, bool deleteAll)
```

### ExecBlockersCommand

Execute Blockers Command 

```angelscript
void ExecBlockersCommand(array<string@>@ command, Critter@ player, Critter@ target)
```

### ExecLogCommand

```angelscript
void ExecLogCommand(array<string@>@ command, Critter@ player)
```

### ExecClearInventoryCommand

```angelscript
void ExecClearInventoryCommand(array<string@>@ command, Critter@ player, Critter@ target)
```

### ExecDropItemsCommand

```angelscript
void ExecDropItemsCommand(array<string@>@ command, Critter@ player, Critter@ target)
```

### ExecPickItemsCommand

```angelscript
void ExecPickItemsCommand(array<string@>@ command, Critter@ player, Critter@ target)
```

### FindItem

helper order: player -> [if not on worldmap -> [current map -> current location]] -> world

```angelscript
Item@ FindItem(Critter@ player, uint itemId)
```

### GetParameterString

let it be here for now...

```angelscript
string GetParameterString(array<string@>@ search, array<string>& this)
```

### GetIndexOfString

...this...

```angelscript
int GetIndexOfString(array<string>& search, string& this)
```

### GetIndexOfString

...and this

```angelscript
int GetIndexOfString(array<string@>@ search, array<string>& this)
```

### ExecItemFlagsCommand

```angelscript
void ExecItemFlagsCommand(array<string@>@ command, Critter@ player)
```

### ExecItemProtoCommand

```angelscript
void ExecItemProtoCommand(array<string@>@ command, Critter@ player)
```

### ExecItemLightCommand

```angelscript
void ExecItemLightCommand(array<string@>@ command, Critter@ player)
```

### ExecSetLexemCommand

```angelscript
void ExecSetLexemCommand(array<string@>@ command, Critter@ player, Critter@ target)
```

### ExecLockCarCommand

```angelscript
void ExecLockCarCommand(array<string@>@ command, Critter@ player, bool lock)
```

### ExecGetItemsCommand

```angelscript
void ExecGetItemsCommand(array<string@>@ command, Critter@ player, Critter@ target)
```

### ExecCoreCheats

built-in client cheats

```angelscript
void ExecCoreCheats(array<string@>@ command, Critter@ player)
```

### ExecFindCharsCommand

```angelscript
void ExecFindCharsCommand(array<string@>@ command, Critter@ player)
```

### ExecFindNpcCommand

```angelscript
void ExecFindNpcCommand(array<string@>@ command, Critter@ player)
```

### ExecPlayMusicCommand

```angelscript
void ExecPlayMusicCommand(array<string@>@ command, Critter@ player)
```

### ExecPlaySoundCommand

```angelscript
void ExecPlaySoundCommand(array<string@>@ command, Critter@ player, bool speech)
```

### ExecGetRequestsCommand

```angelscript
void ExecGetRequestsCommand(array<string@>@ command, Critter@ player)
```

### ExecParamCommand

TODO: finish tester params table and move command to tester access

```angelscript
void ExecParamCommand(array<string@>@ command, Critter@ player, Critter@ target)
```

### ExecGetColorCommand

```angelscript
void ExecGetColorCommand(array<string@>@ command, Critter@ player)
```

### ExecLastSpawnedCommand

```angelscript
void ExecLastSpawnedCommand(array<string@>@ command, Critter@ player, Critter@ target)
```

### spaces

```angelscript
string@ spaces(int num)
```

### ExecGameInfoCommand

```angelscript
void ExecGameInfoCommand(array<string@>@ command, Critter@ player)
```

### ExecLastRegisteredCommand

```angelscript
void ExecLastRegisteredCommand(array<string@>@ command, Critter@ player)
```

### ExecAccessListCommand

```angelscript
void ExecAccessListCommand(array<string@>@ command, Critter@ player)
```

### ExecReservedNicknameCommand

```angelscript
void ExecReservedNicknameCommand(array<string@>@ command, Critter@ player)
```

### ExecToGlobal

```angelscript
void ExecToGlobal(Critter@ player, Critter@ target)
```

### ExecCCD

```angelscript
void ExecCCD(array<string@>@ command, Critter@ player)
```

### ExecFactionNews

```angelscript
void ExecFactionNews(array<string@>@ command, Critter@ player)
```

### ExecRunDialog

```angelscript
void ExecRunDialog(array<string@>@ command, Critter@ player, Critter@ target)
```

### ExecTeamCommand

```angelscript
void ExecTeamCommand(array<string@>@ command, Critter@ player, Critter@ target)
```

### ExecAuraCommand

```angelscript
void ExecAuraCommand(array<string@>@ command, Critter@ player)
```

### cte_Aura

```angelscript
uint cte_Aura(Critter& cr, int identifier, uint& value)
```

### ExecAuraCleanupCommand

```angelscript
void ExecAuraCleanupCommand(array<string@>@ command, Critter@ player)
```

### IsAdmin

admin access

```angelscript
bool IsAdmin(Critter& player)
```

### IsGM

```angelscript
bool IsGM(Critter& player)
```

### AllowParameterIfAccess

```angelscript
int AllowParameterIfAccess(uint8 access, uint parameter, Critter& fromCr, Critter& toCr)
```

### AllowParameterIfTester

```angelscript
int AllowParameterIfTester(uint parameter, Critter& fromCr, Critter& toCr)
```

### AllowParameterIfModer

```angelscript
int AllowParameterIfModer(uint parameter, Critter& fromCr, Critter& toCr)
```

### AllowParameterIfAdmin

```angelscript
int AllowParameterIfAdmin(uint parameter, Critter& fromCr, Critter& toCr)
```

### AllowParameterIfGod

```angelscript
int AllowParameterIfGod(uint parameter, Critter& fromCr, Critter& toCr)
```

### unsafe_ExecCommand

 Executes command 

```angelscript
void unsafe_ExecCommand(Critter& player, int p0, int p1, int p2, string@ commandString, array<int>@ data)
```

### ExecCommand

```angelscript
void ExecCommand(Critter& player, int p0, int p1, int p2, string@ commandString, array<int>@ data)
```

### ExecCommand

bool, for broken macros

```angelscript
bool ExecCommand(Critter& player, string@ commandString)
```

### LoadEventSpawns

```angelscript
void LoadEventSpawns()
```

### SaveEventSpawns

```angelscript
void SaveEventSpawns()
```

### answer_Test

```angelscript
void answer_Test(Critter& player, uint answerI, string& answerS)
```

### _UseSkill

```angelscript
bool _UseSkill(Item& item, Critter& crit, int skill)
```

### checkbot

```angelscript
void checkbot(Critter& cr, int playerId, int, int)
```

### ip

```angelscript
void ip(Critter& cr, int, int, int)
```

### ItemEvent

```angelscript
void ItemEvent(Item& item, int event, string& function)
```

### ItemTypeEvent

```angelscript
void ItemTypeEvent(Item& item, int type, int event, string& function)
```

### weapon_disconnect

weapons

```angelscript
void weapon_disconnect(Item& item, bool firstTime)
```

### weapon_freeze

```angelscript
void weapon_freeze(Item& item, bool firstTime)
```

### weapon_explode

```angelscript
void weapon_explode(Item& item, bool firstTime)
```

### weapon_kill

```angelscript
void weapon_kill(Item& item, bool firstTime)
```

### weapon_heal

```angelscript
void weapon_heal(Item& item, bool firstTime)
```

### weapon_disguise

```angelscript
void weapon_disguise(Item& item, bool firstTime)
```

### weapon_function_disconnect

```angelscript
bool weapon_function_disconnect(Item& item, Critter& sadist, Critter& victim)
```

### weapon_function_freeze

```angelscript
bool weapon_function_freeze(Item& item, Critter& sadist, Critter& victim)
```

### weapon_function_explode

```angelscript
bool weapon_function_explode(Item& item, Critter& sadist, Critter& victim)
```

### weapon_function_kill

```angelscript
bool weapon_function_kill(Item& item, Critter& sadist, Critter& victim)
```

### weapon_function_heal

```angelscript
bool weapon_function_heal(Item& item, Critter& sadist, Critter& victim)
```

### weapon_function_disguise

```angelscript
bool weapon_function_disguise(Item& item, Critter& sadist, Critter& victim)
```

### _ForceEncounter

```angelscript
void _ForceEncounter(Map& map)
```

### SetTimeoutForAll

```angelscript
void SetTimeoutForAll(Map& map, int timeout, int time)
```

### _LockMap

```angelscript
void _LockMap(Map& map)
```

### _DoNothing

```angelscript
void _DoNothing(Map& map)
```

### unsafe_deflect

```angelscript
void unsafe_deflect(Critter& cr, int target, int, int, string@ func, array<int32>@ data)
```

### LoadRiddles

```angelscript
void LoadRiddles()
```

### SaveRiddles

```angelscript
void SaveRiddles()
```

### riddleInfo

```angelscript
string riddleInfo(uint idx, bool shortInfo)
```

### ExecRiddleCommand

```angelscript
void ExecRiddleCommand(array<string@>@ command, Critter@ player)
```


