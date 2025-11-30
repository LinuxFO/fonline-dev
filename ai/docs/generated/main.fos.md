---
title: main.fos
description: " FOnline: 2238 Rotators  main.fos ..."
---

# main.fos


FOnline: 2238
Rotators

main.fos


## Includes

- `_animation.fos`
- `_basetypes.fos`
- `_colors.fos`
- `_macros.fos`
- `_town.fos`
- `_vars.fos`
- `_npc_pids.fos`
- `_vals.fos`
- `broadcast_h.fos`
- `config_h.fos`
- `config_file_h.fos`
- `critter_age_h.fos`
- `critter_skin_h.fos`
- `debug_h.fos`
- `economy_h.fos`
- `factions_h.fos`
- `follower_capturing.fos`
- `follower_common_h.fos`
- `follower_h.fos`
- `groups_h.fos`
- `item_dogtags_h.fos`
- `item_perks_h.fos`
- `logging_h.fos`
- `lexems_h.fos`
- `map_tent_h.fos`
- `mapdata_h.fos`
- `messages_h.fos`
- `minigames_h.fos`
- `mob_wave_h.fos`
- `MsgStr.h`
- `npc_common_h.fos`
- `npc_planes_h.fos`
- `online_stats_h.fos`
- `pdata_h.fos`
- `recycler_h.fos`
- `reinforcements_h.fos`
- `reputations_h.fos`
- `town_h.fos`
- `utils_h.fos`
- `world_common_h.fos`
- `worldmap_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| _CanHelp | `# (npc, who)(_GroupMode(npc) == FACTION_MODE_NPC_ONLY ? _IsTrueNpc(who) : (_GroupMode(npc) == FACTION_MODE_PLAYER_ONLY ? !_IsTrueNpc(who) : true))` | ///////////////////////////////////////////////////////////////////////////////////////////////// Called when a critter is attacked by another. |
| _AnyGuard | `# (npc)         (_GroupMode(npc) != 0 && _GroupMode(npc) != 4)` |  |
| _GenGuardTryHelpCr | `\` | These macros are a nice example of code that can't be inlined function nor can be put in do{}while(false) (because of continue) :) |
| _GenGuardTryHelpAttacker | `\` |  |
| _TryHelpCr | `\` |  |
| _TryHelpAttacker | `\` |  |
| _AddTrophy | `\` |  |
| REPUTATION_DECAY | `(10.0f)` | ///////////////////////////////////////////////////////////////////////////////////////////////// Call every __CritterIdleTick time. |
| REPUTATION_DECAY_TIME | `(REAL_DAY(1) / REPUTATION_DECAY)` |  |

## Classes

### SequenceCritter

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| critter | `Critter@` |  |  |

**Methods**

#### opCmp
```angelscript
int opCmp(SequenceCritter& in other)
```


## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| ItemPids | `dictionary` |  |  |
| VarIds | `dictionary` |  |  |
| BaseTypes | `dictionary` |  |  |
| MapData | `dictionary` |  |  |
| NpcProtoNameDescription | `dictionary` |  |  |
| ItemNames | `array<string>` |  |  |
| VarNames | `array<string>` |  |  |
| Tents | `array<uint>` |  |  |
| lastsecond | `uint` | `0` | ///////////////////////////////////////////////////////////////////////////////////////////////// Call every returned value, in milliseconds. Return next call in milliseconds or zero to disable loop. |
| last_os_save | `uint` | `0` |  |
| last_os_mod | `uint` | `0` |  |
| SequenceCritterRandom | `int` | `0` | Sequence sorter for turn_based_sequence |

## Functions

### GetItemPid

/ Get the id of the item using identifiers stored in ITEMPID.H file

```angelscript
bool GetItemPid(const string& in identifier, int& out pid)
```

### GetVarId

```angelscript
bool GetVarId(const string& in identifier, int& out id)
```

### GetBaseType

void GetVarNames(const string& filter

```angelscript
bool GetBaseType(const string& in identifier, int& out id)
```

### GetBaseType

```angelscript
bool GetBaseType(const int& in id, string& out name)
```

### GetMapData

```angelscript
bool GetMapData(const string& in identifier, int& out id)
```

### GetNpcProtoName

```angelscript
bool GetNpcProtoName( uint16 protoId, string& name )
```

### GetNpcProtoName

```angelscript
string GetNpcProtoName( uint16 protoId )
```

### GetNpcProtoDescription

```angelscript
bool GetNpcProtoDescription( uint16 protoId, string& description )
```

### GetNpcProtoDescription

```angelscript
string GetNpcProtoDescription( uint16 protoId )
```

### init

///////////////////////////////////////////////////////////////////////////////////////////////// Called before world generation.

```angelscript
void init()
```

### start

///////////////////////////////////////////////////////////////////////////////////////////////// Call on start server.

```angelscript
bool start()
```

### GotoTent

```angelscript
void GotoTent(Critter& cr, int p0, int p1, int p2)
```

### get_start_time

///////////////////////////////////////////////////////////////////////////////////////////////// Call on world initialization. Parameter         Min    Max multiplier        1      99 year              1700   30000 month             1      12 day               1      31 hour              0      23 minute            0      59

```angelscript
void get_start_time(uint16& multiplier, uint16& year, uint16& month, uint16& day, uint16& hour, uint16& minute)
```

### finish

///////////////////////////////////////////////////////////////////////////////////////////////// Call on finish server.

```angelscript
void finish()
```

### loop

```angelscript
uint loop()
```

### critter_attack

///////////////////////////////////////////////////////////////////////////////////////////////// Call when critter attack another.

```angelscript
void critter_attack(Critter& cr, Critter& target, ProtoItem& weapon, uint8 weaponMode, ProtoItem@ ammo)
```

### critter_attacked

```angelscript
void critter_attacked(Critter& cr, Critter& attacker)
```

### PostDamage

///////////////////////////////////////////////////////////////////////////////////////////////// Called after the critter gets any damage.

```angelscript
void PostDamage(Critter& cr)
```

### critter_stealing

///////////////////////////////////////////////////////////////////////////////////////////////// Call when a critter steals from another.

```angelscript
bool critter_stealing(Critter& cr, Critter& thief, Item& item, uint count)
```

### critter_use_item

///////////////////////////////////////////////////////////////////////////////////////////////// Call on something critter use item.

```angelscript
bool critter_use_item(Critter& cr, Item& item, Critter@ targetCr, Item@ targetItem, Scenery@ targetScen, uint param)
```

### critter_use_skill

///////////////////////////////////////////////////////////////////////////////////////////////// 

```angelscript
bool critter_use_skill(Critter& cr, int skill, Critter@ targetCr, Item@ targetItem, Scenery@ targetScen)
```

### critter_reload_weapon

///////////////////////////////////////////////////////////////////////////////////////////////// Call on something critter reload weapon. If ammo is not valid than only unload.

```angelscript
void critter_reload_weapon(Critter& cr, Item& weapon, Item@ ammo)
```

### e_CritterInitRun

```angelscript
uint e_CritterInitRun(array<uint>@ values)
```

### e_CritterMove

```angelscript
uint e_CritterMove(array<uint>@ values)
```

### critter_init

```angelscript
void critter_init(Critter& cr, bool firstTime)
```

### e_CritterInit_Broadcast

```angelscript
uint e_CritterInit_Broadcast(array<int>@ data)
```

### e_CritterInit_OnlineStats

```angelscript
uint e_CritterInit_OnlineStats(array<int>@ data)
```

### critter_finish

```angelscript
void critter_finish(Critter& cr, bool toDelete)
```

### critter_idle

```angelscript
void critter_idle(Critter& cr)
```

### CritterTrophy

```angelscript
void CritterTrophy(Critter& critter, Critter& looter)
```

### TownCitizenKilled

```angelscript
void TownCitizenKilled(Critter& critter, Critter@ killer)
```

### death

///////////////////////////////////////////////////////////////////////////////////////////////// Call on something critter dies. Killer can be null.

```angelscript
void death(Critter& cr, int p0, int p1, int p2)
```

### critter_dead

```angelscript
void critter_dead(Critter& cr, Critter@ killer)
```

### e_DeathSpeech

```angelscript
uint e_DeathSpeech(array<uint>@ values)
```

### critter_respawn

///////////////////////////////////////////////////////////////////////////////////////////////// Call on something critter reswapned.

```angelscript
void critter_respawn(Critter& cr)
```

### map_critter_in

///////////////////////////////////////////////////////////////////////////////////////////////// Called when a critter enters a map.

```angelscript
void map_critter_in(Map& map, Critter& cr)
```

### map_critter_out

///////////////////////////////////////////////////////////////////////////////////////////////// Call on something critter out from map.

```angelscript
void map_critter_out(Map& map, Critter& cr)
```

### karma_voting

///////////////////////////////////////////////////////////////////////////////////////////////// Call on something player votes for another. Already checked valid positions and timeout.

```angelscript
void karma_voting(Critter& crFrom, Critter& crTo, bool valUp)
```

### item_cost

///////////////////////////////////////////////////////////////////////////////////////////////// Call to determine cost of single item. To allow function set __CustomItemCost to true. Don't forgot specify this function in client script.

```angelscript
uint item_cost(Item& item, Critter& cr, Critter& npc, bool buy)
```

### items_barter

///////////////////////////////////////////////////////////////////////////////////////////////// Call on barter transaction. Return false to cancel transaction.

```angelscript
bool items_barter(array<Item@>& saleItems, array<uint>& saleItemsCount, array<Item@>& buyItems, array<uint>& buyItemsCount, Critter& player, Critter& npc)
```

### items_crafted

Call on something player craft some items.

```angelscript
void items_crafted(array<Item@>& items, array<uint>& itemsCount, array<Item@>& resources, Critter& crafter)
```

### FovCheck

* * Checks if critter B is out of fov. (used in 'entering sneak mode' check) 

```angelscript
bool FovCheck(Critter& cr, Critter& opponent)
```

### player_levelup

///////////////////////////////////////////////////////////////////////////////////////////////// Levelup callback.

```angelscript
void player_levelup(Critter& player, uint skillIndex, uint skillUp, uint perkIndex)
```

### turn_based_begin

///////////////////////////////////////////////////////////////////////////////////////////////// Turn based callbacks. Called on every round begin, return false to disable turn-based

```angelscript
void turn_based_begin(Map& map)
```

### turn_based_end

Call on end turn-based battle

```angelscript
void turn_based_end(Map& map)
```

### SetWalkRunTimeForNpcs

```angelscript
void SetWalkRunTimeForNpcs(Map& map, uint time)
```

### turn_based_process

Call on every begin and end turn

```angelscript
void turn_based_process(Map& map, Critter& cr, bool beginTurn)
```

### turn_based_sequence

Call when need generate turns sequence

```angelscript
void turn_based_sequence(Map& map, array<Critter@>& critters, Critter@ firstTurnCrit)
```

### world_save

Call on world saving Range of currentIndex: 1..9999

```angelscript
void world_save(uint currentIndex, array<uint>& deleteIndexes)
```

### player_registration

Call on player try register Return true to allow, false to disallow

```angelscript
bool player_registration(uint ip, string& name, uint& textMsg, uint& strNum)
```

### player_login

Call on player try login Return true to allow, false to disallow

```angelscript
bool player_login(uint ip, string& name, uint id, uint& textMsg, uint& strNum)
```

### access_level

```angelscript
uint8 access_level(string& access)
```

### access_level

```angelscript
string access_level(uint8& access)
```

### player_getaccess

Call on player try change access Return true to allow, false to disallow

```angelscript
bool player_getaccess(Critter& player, int access, string& password)
```

### player_allowcommand

Call on player trying to use a command Return true to allow, false to disallow

```angelscript
bool player_allowcommand(Critter@ cr, string@ adminPanel, uint8 command)
```

### server_log

```angelscript
void server_log(string& message)
```

### CheckScripts

```angelscript
void CheckScripts(Critter& cr, int p0, int p1, int p2)
```

### CheckPids

```angelscript
void CheckPids(Critter& cr, int p0, int p1, int p2)
```

### CheckItems

```angelscript
void CheckItems(Critter& cr, int p0, int p1, int p2)
```

### reprohang

```angelscript
void reprohang(Critter& cr, int p0, int p1, int p2)
```

### spawnjunk

```angelscript
void spawnjunk(Critter& cr, int, int, int)
```


