---
title: utils.fos
description: " FOnline: 2238 Rotators  utils.fos ..."
---

# utils.fos


FOnline: 2238
Rotators

utils.fos


## Includes

- `_basetypes.fos`
- `_colors.fos`
- `_defines.fos`
- `_scripts.fos`
- `buffer_h.fos`
- `debug_h.fos`
- `entire.fos`
- `lexems_h.fos`
- `logging_h.fos`
- `mapdata_h.fos`
- `npc_common_h.fos`
- `utils_for_array.fos`
- `utils_h.fos`

## Included By

- [spawner_pvp.fos](spawner_pvp.fos.md)

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __UTILS_MODULE__ |  |  |
| PUSHIFNZ | `# (_var, _param) if((_var) != 0) { params.insertLast(_param); params.insertLast(_var); }` |  |
| DRUG_FIX_VERSION | `(1)` |  |
| _HexPoint | `# (_x, _y) do { if(_x >= 0 && _y >= 0) { xList.insertLast(_x); yList.insertLast(_y); } } while(false)` | * * Simple geometric shapes returned as list of x, y coordinates  |

## Classes

### DateTime

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| year | `uint16` |  |  |
| month | `uint16` |  |  |
| dayOfWeek | `uint16` |  |  |
| day | `uint16` |  |  |
| hour | `uint16` |  |  |
| minute | `uint16` |  |  |
| second | `uint16` |  |  |
| milliseconds | `uint16` |  |  |

**Methods**

#### get_Year
```angelscript
uint16 get_Year()         { return year; }
```

#### get_Month
```angelscript
uint16 get_Month()        { return month; }
```

#### get_DayOfWeek
```angelscript
uint16 get_DayOfWeek()    { return dayOfWeek; }
```

#### get_Day
```angelscript
uint16 get_Day()          { return day; }
```

#### get_Hour
```angelscript
uint16 get_Hour()         { return hour; }
```

#### get_Minute
```angelscript
uint16 get_Minute()       { return minute; }
```

#### get_Second
```angelscript
uint16 get_Second()       { return second; }
```

#### get_Milliseconds
```angelscript
uint16 get_Milliseconds() { return milliseconds; }
```

#### ToString
```angelscript
string@ ToString()
```


## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| OnlinePlayers | `array<uint>` |  | These functions/variables will not appear in documentation because they aren't meant to be used from the outside. |

## Functions

### AddNpc

* * AddNpc that is backwards compatible with old AddNpc function. * * @param map Map handle where NPC should be spawned. * @param pid PID of NPC to spawn. * @param x X-position on map. * @param y Y-position on map. * @param dir direction of NPC, see direction defines in _defines.fos * @param dialogId dialog id, see dialogs.lst or _dialogs.fos * @param script script module and init function to use, for example: "guard@critter_init", means use the function critter_init in script guard.fos * @param aiPack AI pack to assign to NPC. See _ai.fos * @param bagId Bag to assign to NPC. See BAGS.txt * @param teamId Assign Faction/Team. * @param isMob Deprecated parameter, used only in some really old code. Set it to false. * @param level Level of spawned NPC. * @return Handle to the spawned NPC, if AddNpc failed, it's null. 

```angelscript
Critter@ AddNpc(Map@ map, uint16 pid, uint16 x, uint16 y, uint8 dir, uint dialogId, string& script, uint aiPack, uint bagId, uint teamId, bool isMob, uint level)
```

### AddNpc

* * AddNpc that is backwards compatible with old AddNpc function and provide additional faction info setting. * * @param map Map handle where NPC should be spawned. * @param pid PID of NPC to spawn. * @param x X-position on map. * @param y Y-position on map. * @param dir direction of NPC, see direction defines in _defines.fos * @param dialogId dialog id, see dialogs.lst or _dialogs.fos * @param script script module and init function to use, for example: "guard@critter_init", means use the function critter_init in script guard.fos * @param aiPack AI pack to assign to NPC. See _ai.fos * @param bagId Bag to assign to NPC. See BAGS.txt * @param teamId Assign Faction/Team. * @param factionRank Assign Faction/Team rank. * @param factionMode Assign Faction/Team mode. * @param isMob Deprecated parameter, used only in some really old code. Set it to false. * @param level Level of spawned NPC. * @return Handle to the spawned NPC, if AddNpc failed, it's null. 

```angelscript
Critter@ AddNpc(Map@ map, uint16 pid, uint16 x, uint16 y, uint8 dir, uint dialogId, string& script, uint aiPack, uint bagId, uint teamId, uint factionRank, uint factionMode, bool isMob, uint level)
```

### AddNpc

* * AddNpc that is backwards compatible with old AddNpc function and override default parameters. * * @param map Map handle where NPC should be spawned. * @param pid PID of NPC to spawn. * @param x X-position on map. * @param y Y-position on map. * @param dir direction of NPC, see direction defines in _defines.fos * @param params override for default parameters * @param dialogId dialog id, see dialogs.lst or _dialogs.fos * @param script script module and init function to use, for example: "guard@critter_init", means use the function critter_init in script guard.fos * @param aiPack AI pack to assign to NPC. See _ai.fos * @param bagId Bag to assign to NPC. See BAGS.txt * @param teamId Assign Faction/Team. * @param isMob Deprecated parameter, used only in some really old code. Set it to false. * @param level Level of spawned NPC. * @return Handle to the spawned NPC, if AddNpc failed, it's null. 

```angelscript
Critter@ AddNpc(Map@ map, uint16 pid, uint16 x, uint16 y, uint8 dir, array<int> params, uint dialogId, string& script, uint aiPack, uint bagId, uint teamId, bool isMob, uint level)
```

### AddNpc

* * AddNpc that is backwards compatible with old AddNpc function with additional faction data and override default parameters. * * @param map Map handle where NPC should be spawned. * @param pid PID of NPC to spawn. * @param x X-position on map. * @param y Y-position on map. * @param dir direction of NPC, see direction defines in _defines.fos * @param params override for default parameters * @param dialogId dialog id, see dialogs.lst or _dialogs.fos * @param script script module and init function to use, for example: "guard@critter_init", means use the function critter_init in script guard.fos * @param aiPack AI pack to assign to NPC. See _ai.fos * @param bagId Bag to assign to NPC. See BAGS.txt * @param teamId Assign Faction/Team. * @param isMob Deprecated parameter, used only in some really old code. Set it to false. * @param level Level of spawned NPC. * @return Handle to the spawned NPC, if AddNpc failed, it's null. 

```angelscript
Critter@ AddNpc(Map@ map, uint16 pid, uint16 x, uint16 y, uint8 dir, array<int> params, uint dialogId, string& script, uint aiPack, uint bagId, uint teamId, uint factionRank, uint factionMode, bool isMob, uint level)
```

### GetCritterInfo

* * Retrieve string with some critter information. Suitable for usage in logging. 

```angelscript
string GetCritterInfo(Critter& cr)
```

### AddScore

* * Add score to a critter * @param cr Critter handle. * @param score Score index. * @param points How many points to add. 

```angelscript
void AddScore(Critter@ cr, uint score, uint points)
```

### ReloadWeapon

```angelscript
bool ReloadWeapon(Critter& cr)
```

### GetRadio

* * Retrieve radio that critter wears in a slot. * @param cr Critter handle. * @return Item handle to found radio, or null if none is carried in slots. 

```angelscript
Item@ GetRadio(Critter& cr)
```

### GetRepairTool

* * Retrieve tool that critter wears in a slot. * @param cr Critter handle. * @return Item handle to found tool, or null if none is carried in slots. 

```angelscript
Item@ GetRepairTool(Critter& cr)
```

### GetEquippedItemByType

* * Retrieve an item of specified type (any weapon for example) that critter wears in a slot. * @param cr Critter handle. * @param ItemType Item type to search for. * @return Item handle to found item, or null if none is carried in slots. 

```angelscript
Item@ GetEquippedItemByType(Critter& cr, uint ItemType)
```

### GetEquippedItem

* * Retrieve a specific item that critter wears in a slot. * @param cr Critter handle. * @param Pid Item PID to search for. * @return Item handle to found item, or null if none is carried in slots. 

```angelscript
Item@ GetEquippedItem(Critter& cr, uint Pid)
```

### GetEquippedItem

* * Retrieve any item in list that critter wears in a slot. * @param cr Critter handle. * @param Pids List of item PIDs to search for. * @return Item handle to found item, or null if none is carried in slots. 

```angelscript
Item@ GetEquippedItem(Critter& cr, array<uint>& Pids)
```

### GetConditionOfCritter

* * Gives string of player condition. * @param cr Handle to critter. * @return If not valid critter or condition couldn't be converted, returns "", else it returns condition in string form. 

```angelscript
string GetConditionOfCritter(Critter@ cr)
```

### SkillRoll

* * Does a skill roll. * @param cr Handle to critter. * @param skill Skill number * @param bonus Skill bonus * @return True is passed, false otherwise 

```angelscript
bool SkillRoll(Critter@ cr, int skill, int bonus)
```

### SkillCheck

* * Useful wrapper for making checks if a proper skill or item was applied in a given context. * @param cr Critter reference. * @param skill Skill number to be checked * @param skillused Skill that is supposed to be used - if used item implied skill or used skill do not match, the function fails * @param item Item handle, might imply used skill, e.g. Lockpicks imply SK_LOCKPICK * @param bonus Skill bonus * @return SKILL_CHECK_DOES_NOTHING if the skill used and wanted/implied by item do not match. Otherwise, result of the skill roll, either SKILL_CHECK_FAILURE or SKILL_CHECK_SUCCESS 

```angelscript
int SkillCheck(Critter& cr, int skill, int skillused, Item@ item, int bonus)
```

### SkillName

```angelscript
string SkillName(uint8 skill)
```

### GetExtConditionOfCritter

* * Gives string of extended player condition (animation). * @param cr Handle to critter. * @return If not valid critter or condition couldn't be converted, returns "", else it returns condition in string form. * @remarks This will only work if condition of critter is either CRITTER_CONDITION_KNOCKOUT or CRITTER_CONDITION_DEAD as only those use ExtCondition. 

```angelscript
string GetExtConditionOfCritter(Critter@ cr)
```

### AddExpTeam

* * Function to add xp divided equally among all members of a "team". * @param critter Handle to one member of a team. * @param xp Amount of total XP points to add. * @remarks A team is currently defined as everyone that has arrowed the leader. If leader is invalid, all the xp will be added to the specified critter. * @return If leader is valid, true, otherwise false. 

```angelscript
bool AddExpTeam(Critter& critter, int xp)
```

### DropTimeouts

* * Drop all timeouts of target critter * @param cr Critter handle. 

```angelscript
void DropTimeouts(Critter& cr)
```

### ClearEvents

* * Clears all current critter events * @param cr Critter handle. 

```angelscript
void ClearEvents(Critter& cr)
```

### GiveBag

* * Create bag and add items to critter * @param cr Critter handle. * @param bag Bag Id to give. 

```angelscript
void GiveBag(uint bag, Critter@ cr)
```

### HasItem

```angelscript
bool HasItem(Critter@ cr, uint pid)
```

### HasSomeWeapon

* * Has a weapon in inventory or equipped. 

```angelscript
bool HasSomeWeapon(Critter@ cr)
```

### GetBestWeaponSkill

* * Gets the best weapon skill that a critter has. * @param cr Handle to critter. * @return The best weapon skill the critter has. See _defines.fos and the SK_* entries for relevant skills. 

```angelscript
uint GetBestWeaponSkill(Critter@ cr)
```

### AddOnlinePlayer

* * Add player to array of all online players. * @param cr Handle to critter. 

```angelscript
void AddOnlinePlayer(Critter& cr)
```

### RemoveOnlinePlayer

* * Remove player from array of all online players. * @param cr Handle to critter. 

```angelscript
void RemoveOnlinePlayer(Critter& cr)
```

### GetAllOnlinePlayers

* * Retrieve all players that are online. * @param players Array to store player handles in. * @return Number of players online. 

```angelscript
uint GetAllOnlinePlayers(array<Critter@>& out players)
```

### GetNumberOfPlayersOnline

* * Check how many players are online. * @return Number of players online. 

```angelscript
uint GetNumberOfPlayersOnline()
```

### GetAuthenticatedPlayers

```angelscript
uint GetAuthenticatedPlayers(array<Critter@>& out players)
```

### GetAuthenticatedPlayers

```angelscript
uint GetAuthenticatedPlayers(array<Critter@>& out players, bool ignorePriviledges)
```

### GetMostSkilled

* * Gets critter that is best at some skill in the group. * @param group A group of critters. * @param skill Which skill. See _defines.fos for a list of skills. (SK_*) * @return Handle to most skilled critter. 

```angelscript
Critter@ GetMostSkilled(array<Critter@>@ group, int skill)
```

### GetAuthString

* * Retrieve a string showing target players access level. * @param player Target player. * @return A string showing target players access level. * @remarks Possible results are: "Client", "Tester", "GM" and "Admin" 

```angelscript
string GetAuthString(Critter& player)
```

### GetAuthString

* * Retrieve a string showing target players access level. * @param accesslevel Access number. * @return A string showing target players access level. * @remarks Possible results are: "Client", "Tester", "GM" and "Admin" 

```angelscript
string GetAuthString(int accesslevel)
```

### CanRequestHelp

* * Check if target player can use +requesthelp * @param player Target player. 

```angelscript
bool CanRequestHelp(Critter& player)
```

### SetRequestedHelp

* * Disables the ability to use +requesthelp for some time. * @param player Target player. 

```angelscript
void SetRequestedHelp(Critter& player)
```

### SetRequestedHelp

```angelscript
void SetRequestedHelp(Critter& player, int minutes)
```

### GetOnlineGM

* * Retrieve a random GM. If none is found, any authenticated (Admin) is picked. * @return Handle of found GM/admin. Null if none is online. 

```angelscript
Critter@ GetOnlineGM()
```

### IsHumanoid

```angelscript
bool IsHumanoid(Critter@ cr)
```

### ClearEnemyStack

* * Clear EnemyStack of target NPC. * @param critter Target NPC. * @remarks The EnemyStack is an array/memory filled with ids of hostile critters. 

```angelscript
void ClearEnemyStack(Critter& critter)
```

### ClearEnemyStacksOnMap

* * Clear all EnemyStacks of all NPCs on specified map. * @param map Target Map. * @remarks The EnemyStack is an array/memory filled with ids of hostile critters. 

```angelscript
void ClearEnemyStacksOnMap(Map@ map)
```

### IsCurrentEnemy

* * Checks if a target with given id is the critter's enemy, based on the enemy stack and attack planes 

```angelscript
bool IsCurrentEnemy(Critter& cr, uint targetId)
```

### GetSafePlayerName

```angelscript
string@ GetSafePlayerName(uint id)
```

### GetSafePlayerName

```angelscript
string GetSafePlayerName(uint id, string& onSuccess, string& onError)
```

### GetGroupIndex

```angelscript
uint GetGroupIndex(Critter& cr)
```

### GetGroupIndex

```angelscript
uint GetGroupIndex(int st)
```

### SetGroupIndex

* * Modifies data responsible for holding faction/group index. 

```angelscript
void SetGroupIndex(Critter& cr, uint val)
```

### GetGroupRank

```angelscript
uint GetGroupRank(Critter& cr)
```

### SetGroupRank

```angelscript
void SetGroupRank(Critter& cr, uint val)
```

### GetGroupMode

```angelscript
uint GetGroupMode(Critter& cr)
```

### SetGroupMode

```angelscript
void SetGroupMode(Critter& cr, uint val)
```

### SetGroupInfo

```angelscript
void SetGroupInfo(Critter& cr, uint faction, uint rank, uint mode)
```

### SetGroupInfoPack

```angelscript
void SetGroupInfoPack(Critter& cr, uint packInfo)
```

### ReadPids

* * Reads ITEMPID.H into supplied array. * @param pids Array to store read pids in. * @param removeinvalid Remove PIDs not used in the game. * @return If file is found and parsed successfully, true, else false. 

```angelscript
bool ReadPids(array<int>& out pids, bool removeinvalid)
```

### ReadDefines

* * Read values defined in the given file. * @param fileName Name of the file to read defines from. Relative path from the server application can be used. * @param items A dictionary to which the defines will be read into, the key is in string format, while the dictionary value is the #define value. * @param defines A string array to which the defines will be read into. 

```angelscript
void ReadDefines(string@ fileName, dictionary& items, array<string>@ defines)
```

### ReadMsgStrings

```angelscript
void ReadMsgStrings(string& fileName, dictionary& output )
```

### ParseMsgStringRaw

```angelscript
bool ParseMsgStringRaw(const string& in line, int& out num, string& out msgStr)
```

### ParseDefine

* Gets info from line like this: * #define ITEM_PID	number * @param line A define line, example: "#define PID_ROCK (19)". * @param spid The parsed string will be stored in this variable. * @param id The parsed number will be stored in this variable. * @return True when succeeded, false otherwise 

```angelscript
bool ParseDefine(const string& in line, string& out spid, int& out id)
```

### SkipWhitespaces

* * skips all whitespaces in string starting at start position * @param str The string used. * @param start The position in the string to start at. * @return index of first non-whitespace character from start. 

```angelscript
int SkipWhitespaces(const string& in str, int start)
```

### SkipNonWhitespaces

* * skips all non-whitespaces in string starting at start position * @param str The string used. * @param start The position in the string to start at. * @return index of first whitespace character 

```angelscript
int SkipNonWhitespaces(const string& in str, int start)
```

### IsParameterTag

* * Checks if a string containers a parameter tag. Example: "-dir 0" * @param str The string used. * @return True if it contains any of the possible tags that can be used, false if not. * @remarks The following tags are valid:"-dir", "-full", "-dist" ,"-role" , "-min" ,"-max", "-v1" ,"-v2" ,"-v3" ,"-v4" ,"-v5", "-script" ,"-dmg" ,"-pid". Besides these, any character combined with - can be used, for example: "-b". 

```angelscript
bool IsParameterTag(string& str)
```

### GetParameterString

* Gets the string of a named parameter in an array of strings. * @param arr An array of strings (a sentance for example). * @param parameter The parameter tag to use. See IsParameterTag for more information. * @return A string with the parameter tag's information. Example: `whisper -p Lord Cektop -m Prepare to die! The parameter "-m" would in this case return "Prepare to die!" 

```angelscript
string GetParameterString(array<string@>@ arr, string& parameter)
```

### GetIndexOfString

* * Returns the index of a string in an array of strings. * @param arr The array of strings to search. * @param str The string to look for. * @return If not found, it returns -1, else it returns the index of the string in the array. 

```angelscript
int GetIndexOfString(array<string@>@ arr, string& str)
```

### GetConcatenatedString

* * Concatenates the specified indexes of an array of strings to a string and returns it * @param startindex Which index in the array to start at. * @param stopindex Which index in the array to stop at, if stopindex = -1 it means that it will run until the end of the array. * @return The concatenated string. 

```angelscript
string GetConcatenatedString(array<string@>@ arr, uint startindex, int stopindex)
```

### GetMsgStr

```angelscript
string GetMsgStr(int textMsg, uint strNum)
```

### SetTurnBasedAvailability

* * Sets turn based mode for all maps within the location * @param loc Location handle. 

```angelscript
void SetTurnBasedAvailability(Location@ loc)
```

### IsEncounterMap

* * Checks if map is an encounter map. * @param map Map handle. * @return True if map is an encounter map, otherwise false. 

```angelscript
bool IsEncounterMap(Map@ map)
```

### IsTown

* * Checks if map is a town map. * @param map Map handle. * @return True if map is a town map, otherwise false. 

```angelscript
bool IsTown(Map@ map)
```

### GetMapType

* * Gets the type of a map. * @param map Map handle. * @return Type of the map, see utils_h.fos for a list of different types. 

```angelscript
uint GetMapType(Map@ map)
```

### GetLocationOf

* * Retrieve current location of a critter * @param critter Critter handle. * @return Handle to the critter's location, null will be returned if the critter is on the worldmap or if there's some error. 

```angelscript
Location@ GetLocationOf(Critter& critter)
```

### GetLocationName

```angelscript
string GetLocationName(uint locId)
```

### GetLocationName

```angelscript
string GetLocationName(Location@ loc)
```

### SetQuestGarbager

* * Sets the time and event to garbage the location, setting a given variable to given value when the location was present on event execution * * @param time Time to garbage, in real minutes, if 0 then default is taken * @param playerid Id of the player, the location owner * @param locid Id of the location * @param var Variable number to be set * @param val Value for the variable * 

```angelscript
void SetQuestGarbager(uint time, uint playerid, uint locid, uint var, uint val)
```

### LockDoor

* * Lock a door. * @param x X-position on map. * @param y Y-position on map. * @param map Map handle. * @param complexity Lock complexity. * @param lockid Id of the lock to use. The Id corresponds to the key that is needed to open the door. 

```angelscript
void LockDoor(uint x, uint y, Map@ map, uint complexity, uint lockid)
```

### UnlockDoor

* * Unlock a door. * @param x X-position on map. * @param y Y-position on map. * @param map Map handle. 

```angelscript
void UnlockDoor(uint x, uint y, Map@ map)
```

### gcd

```angelscript
int gcd(int a, int b)
```

### knapsack

```angelscript
array<int> knapsack(array<int> weights, int W)
```

### GetCurrentDateTime

```angelscript
IDateTime@ GetCurrentDateTime()
```

### GetCurrentDateTimeString

* * Gets a DateTime string which displays both date and time. * @param map Target Map. * @return Current DateTime string which displays both date and time.  Default, show both date/time

```angelscript
string GetCurrentDateTimeString()
```

### GetCurrentDateTimeString

* * Gets a DateTime string which displays date or/and time. * @param date Display date. * @param time Display time. * @return Current DateTime string with specified options. 

```angelscript
string GetCurrentDateTimeString(bool date, bool time)
```

### GetContainer

* * Retrieve container from a map, with Entire. * @param map Map handle. * @param contpid Itempid of the container to retrieve. * @param entire Which Entire to use for coordinates of the container (Entire has to be placed on the same hex as container in mapper) * @return Item handle of the found container. If map is invalid or container not found, null. 

```angelscript
Item@ GetContainer(Map@ map, uint contpid, uint entire)
```

### TeleportCar

* * Teleport a car to some other map. * @return False if no free spot for the vehicle is found 

```angelscript
bool TeleportCar(Item@ Car, uint MapId)
```

### TransferItemsToContOnMap

* * Transfer some items from target critter to a container on a specific map via Entire. * @param map Map handle. * @param cr Critter handle. * @param contpid Itempid of the container to transfer to. * @param entid Which Entire to use for coordinates of the container (Entire has to be placed on the same hex as container in mapper) * @param itemtypes Type of items to transfer from critter. ITEMTRANSFER_ALL or ITEMTRANSFER_WEAPONS is valid. 

```angelscript
void TransferItemsToContOnMap(Critter& cr, Map@ map, int entid, int contpid, int itemtypes)
```

### TransferItemsFromContOnMap

* * Transfer items from a container to a critter * @param map Map handle. * @param cr Critter handle. * @param contpid Itempid of the container to transfer from. * @param entid Which Entire to use for coordinates of the container (Entire has to be placed on the same hex as container in mapper) 

```angelscript
void TransferItemsFromContOnMap(Critter& cr, Map@ map, int entid, int contpid)
```

### ClearContainer

* * Deletes all items in specified container. * @param container Handle to target container. 

```angelscript
void ClearContainer(Item@ container)
```

### MoveItemsCritterToCont

* * Move all items from a critter to a subcontainer of a container. * @param crFrom The critter which items are moved from. * @param contTo Target container. * @param specid Special Id of subcontainer, if 0, critter's Id is used. 

```angelscript
void MoveItemsCritterToCont(Critter& crFrom, Item& contTo, uint specid)
```

### GetGvar

* * Wrapper function for retrieving the value of a GVAR (Global variable). * @param gvar Target GVAR. * @return Value of the specified GVAR. 

```angelscript
int GetGvar(uint gvar)
```

### SetGvar

* * Wrapper function for setting the value of a GVAR (Global variable). * @param gvar Target GVAR. * @param value Value to set. 

```angelscript
void SetGvar(uint gvar, uint value)
```

### GetLLvar

```angelscript
int GetLLvar(Location& location, uint llvar)
```

### GetLLvar

```angelscript
int GetLLvar(uint locationId, uint llvar)
```

### SetLLvar

```angelscript
void SetLLvar(Location& location, uint llvar, uint value)
```

### GetLMvar

```angelscript
int GetLMvar(Map& map, uint lmvar)
```

### GetLMvar

```angelscript
int GetLMvar(uint mapId, uint lmvar)
```

### SetLMvar

```angelscript
void SetLMvar(Map& map, uint lmvar, uint value)
```

### GetLIvar

```angelscript
int GetLIvar(Item& item, uint livar)
```

### GetLIvar

```angelscript
int GetLIvar(uint itemId, uint livar)
```

### SetLIvar

```angelscript
void SetLIvar(Item& item, uint livar, uint value)
```

### GetLvar

* * Wrapper function for retrieving the value of an LVAR (Local variable) from a critter. * @param critter Critter handle. * @param lvar LVAR to check. * @return Value of the specified LVAR. 

```angelscript
int GetLvar(Critter& critter, uint lvar)
```

### GetLvar

* * Wrapper function for retrieving the value of an LVAR (Local variable) from a critter. * @param id Critter Id. * @param lvar LVAR to check. * @return Value of the specified LVAR. 

```angelscript
int GetLvar(uint id, uint lvar)
```

### GetLvar

```angelscript
int GetLvar(uint id, uint lvar, string& typeShort)
```

### SetLvar

* * Wrapper function for setting the value of an LVAR (Local variable). * @param critter Critter handle. * @param lvar Target LVAR. * @param value Value to set. 

```angelscript
void SetLvar(Critter& critter, uint lvar, uint value)
```

### SetLvar

* * Wrapper function for setting the value of an LVAR (Local variable). * @param id Critter Id. * @param lvar Target LVAR. * @param value Value to set. 

```angelscript
void SetLvar(uint id, uint lvar, uint value)
```

### SetLvar

```angelscript
void SetLvar(uint id, uint lvar, uint value, string& typeShort, string& typeLong)
```

### GetUvar

* * Wrapper function for retrieving the value of an UVAR ("Unicum" variable). * @param uvar Target UVAR. * @param masterid MasterId corresponding to some critter. * @param slaveid SlaveId corresponding to another critter. * @return Value of the UVAR. 

```angelscript
int GetUvar(uint uvar, uint masterid, uint slaveid)
```

### SetUvar

* * Wrapper function for setting the value of an UVAR ("Unicum" variable). * @param uvar Target UVAR. * @param masterid MasterId corresponding to some critter. * @param slaveid SlaveId corresponding to another critter. * @param value Value of the UVAR to set. 

```angelscript
void SetUvar(uint uvar, uint masterid, uint slaveid, uint value)
```

### GetContainerValue

* * Uses BaseItemValue to deduce value of all items in a container * @param container Target container. * @return value Total value of all items in the container. 

```angelscript
uint GetContainerValue(Item@ container)
```

### BaseItemValue

* * base value of an spawned item with this pid (with 0% deterioration, unbroken) * @param pid Pid of an item. * @param ammo Is it ammo? * @return Base value of the item. 

```angelscript
uint BaseItemValue(uint pid, bool ammo)
```

### BaseItemValue

* * base value of an spawned item with this pid (with det% deterioration, broken times broken) * @param pid Pid of an item. * @param ammo Is it ammo? * @param broken How many times the item was broken. * @param det % deterioration. * @return Base value of the item. 

```angelscript
uint BaseItemValue(uint pid, uint broken, uint det, bool ammo)
```

### BaseItemValue

* * Full base value of an item, count included * @param item Item handle. * @return Base value of the item. 

```angelscript
uint BaseItemValue(Item@ item)
```

### BaseItemValue

* * proc% of base value of an item (ammo value is always 100%), count included * @param item Item handle. * @param proc Percentage of base value. * @return Calculated value. 

```angelscript
uint BaseItemValue(Item@ item, uint proc)
```

### BaseSingleItemValue

* * full base value of an item, count NOT included. * @param item Item handle. * @return Base value of item. 

```angelscript
uint BaseSingleItemValue(Item@ item)
```

### BaseSingleItemValue

* * proc% of base value of an item (ammo value is always 100%), count NOT included * @param item Item handle. * @param proc Percentage of value. * @return Calculated value of item. 

```angelscript
uint BaseSingleItemValue(Item@ item, uint proc)
```

### Pickable

```angelscript
bool Pickable(Item@ item)
```

### e_DeleteQuestLoc

```angelscript
uint e_DeleteQuestLoc(array<uint>@ values)
```

### e_UnsetRequestedHelp

Player can once again request gm help.

```angelscript
uint e_UnsetRequestedHelp(array<uint>@ values)
```

### Preprocess

:>

```angelscript
void Preprocess(Critter& player, string& commandString)
```

### LogCommandUsage

```angelscript
void LogCommandUsage(Critter& player, string& commandString)
```

### SetSpectator

```angelscript
void SetSpectator(Critter& cr, bool on)
```

### SetSpectator

```angelscript
void SetSpectator(Critter& cr, bool on, bool egg)
```

### SetBloodType

```angelscript
void SetBloodType(Critter@ cr)
```

### GetBloodType

```angelscript
string GetBloodType(Critter@ cr)
```

### GetBloodRandom

```angelscript
string GetBloodRandom()
```

### IpToString

```angelscript
string IpToString(uint ip)
```

### GetCritterName

```angelscript
string GetCritterName(Critter& cr)
```

### SayEx

```angelscript
void SayEx(uint8 type, Critter& target, string& text)
```

### MapMessageEx

```angelscript
void MapMessageEx(uint8 type, uint8 mode, Critter& target, string& text, uint16 hexX, uint16 hexY, uint8 delay = 150, uint color = 0, bool fade = true, int8 fromX = 0, int8 toX = 0, int8 fromY = 0, int8 toY = 0)
```

### VerboseAction

```angelscript
void VerboseAction(Critter& cr, string& text)
```

### VerboseAction

```angelscript
void VerboseAction(Critter& cr, Critter& target, string& text)
```

### VerboseExperience

```angelscript
void VerboseExperience(Critter& cr, int xpDiff, int levelDiff)
```

### CreateLocationForGroup

* * Creates new location for the given player, his player and non-player followers. 

```angelscript
uint CreateLocationForGroup(Critter& player, uint16 pid, uint16 worldX, uint16 worldY, array<Critter@>& group)
```

### ChangeCrTypeSafe

```angelscript
void ChangeCrTypeSafe(Critter& cr, uint16 crType)
```

### SetChosenActions

```angelscript
void SetChosenActions(Critter& cr, array<int>& actions)
```

### PrintCallstack

```angelscript
void PrintCallstack()
```

### PrintCallstack

```angelscript
void PrintCallstack(int level)
```

### FixDrugs

```angelscript
void FixDrugs(Critter& cr)
```

### FindFirstFreeHex

* * Finds the first free hex in a given dir, starting from x, y. * @return True if a free hex was found, false otherwise. Hex coordinates are returned by reference. 

```angelscript
bool FindFirstFreeHex(Map@ map, uint16& x, uint16& y, uint8 dir, uint16 maxSteps)
```

### FindNearestFreeHex

* * Finds the nearest free hex within given radius. * @return True if a free hex was found, false otherwise. Hex coordinates are returned by reference. 

```angelscript
bool FindNearestFreeHex(Map& map, uint16& x, uint16& y, uint radius)
```

### GetItemCoordinates

* * Gets true coordinates of the item via reference * Returns false if unable to get the coordinates (for whatever reason). 

```angelscript
bool GetItemCoordinates(Item& item, uint& mapID, uint16& x, uint16& y)
```

### ItemOnHex

* * Returns true if there is an item with specific prototypeId on the hex. 

```angelscript
bool ItemOnHex(uint16 pid, Map@ map, uint16 x, uint16 y)
```

### HexLine

```angelscript
void HexLine(uint16 x0, uint16 y0, uint16 x1, uint16 y1, array<uint16>@ xList, array<uint16>@ yList)
```

### HexCircle

```angelscript
void HexCircle(uint16 x0, uint16 y0, uint16 radius, array<uint16>@ xList, array<uint16>@ yList)
```

### FindPreferredGridApprox

```angelscript
bool FindPreferredGridApprox(Map& map, uint16& hx, uint16& hy)
```

### LocationHasCritters

Returns true if there is at least one Critter of given type inside Location. 

```angelscript
bool LocationHasCritters(Location& loc, uint findType)
```

### LocationGetCritters

Gets all Critters of given type inside Location. 

```angelscript
uint LocationGetCritters(Location& loc, uint findType, array<Critter@>@ critters)
```

### LocationHasItems

Returns true if there is at least one Item with given protoId inside Location. 

```angelscript
bool LocationHasItems(Location& loc, uint16 protoId)
```

### LocationGetItems

Gets all items with given protoId inside Location. 

```angelscript
uint LocationGetItems(Location& loc, uint16 protoId, array<Item@>@ items)
```

### LocationDeleteItems

Deletes all items with given protoId inside Location. 

```angelscript
void LocationDeleteItems(Location& loc, uint16 protoId)
```

### IsDisposableEncounter

Returns true if location is an encounter, has no geck items and no players. 

```angelscript
bool IsDisposableEncounter(Location@ loc)
```

### IntToIp

```angelscript
string IntToIp(int d)
```

### SetLLvar

```angelscript
void SetLLvar(uint locationId, uint llvar, uint value)
```

### MapRefreshVisible

```angelscript
void MapRefreshVisible(Map@ map, uint hexX, uint hexY, uint radius)
```


