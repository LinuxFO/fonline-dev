---
title: faction_data.fos
description: " FOnline: 2238 Rotators  faction_data.fos ..."
---

# faction_data.fos


FOnline: 2238
Rotators

faction_data.fos


## Includes

- `_macros.fos`
- `factions_h.fos`
- `factions_names.fos`
- `factions_news.fos`
- `groups_h.fos`
- `mapdata_h.fos`
- `serializator.fos`
- `utils_h.fos`
- `lexems_h.fos`
- `logging_h.fos`

## Included By

- [factions.fos](factions.fos.md)

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __FACTION_DATA__ |  |  |
| MAX_ARRAY_SIZE | `(16000)` | max size of the array working as "database" |

## Classes

### FactionData

* * @ingroup FOnline2238 * Wrapper class for holding data needed to create Faction database in the array of * uints. It saves all data needed for faction. 

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| factionName | `string` |  | * Name of the faction |
| _assignednames | `dictionary@` |  |  |
| serialiser | `[Serializator](serializator.fos.md)` |  | * Serialiser used to store data in AnyData array |
| players | `array<uint>` |  | * Identifiers of players whose info is stored in faction database |
| factions | `array<int>` |  | * Identifiers of factions whose info is stored in faction database |
| faction | `uint` |  | * 'Owner' faction of that database |
| stringId | `uint` |  | * Index to the array holding factions names |
| freq | `uint` |  | * Radio frequency |
| locationId | `uint` |  | * * id of the location if faction uses dynamically created location, otherwise 0  |
| locationPid | `uint` |  | * prototype id of location |
| leaderId | `uint` |  | * id of the leader |
| claimId | `uint` |  | * id of the member who claimed leadership, and wants to overthrown current leader |
| leaderTime | `uint` |  | * time that will allow claimee to claim leadership even without forcing current leader to resign/killing him this is time for leader to act |
| claimTime | `uint` |  | * time that will allow another player to claim leadership this is time for claimee to act |
| newsId | `uint` |  | * index to array with faction news |
| news | `[FactionNews](factions_news.fos.md)` |  | * News |
| score | `uint` |  | * score |
| locX | `uint` |  | * worldmap coord |
| locY | `uint` |  | * worldmap coord |
| playerDriven | `bool` |  | * Denotes whether it's player-driven gang or not. |
| lastUsed | `uint` |  | * Tracks the time when faction has been last accessed. |
| update_seq | `uint` |  | * Some features requires us to track the 'update' counter. This is the counter. |

**Methods**

#### initRecognition
* * Initializes radio text listener for quick info 

```angelscript
void initRecognition()
```

#### IsPlayerDriven
* * Gang or not. 

```angelscript
bool IsPlayerDriven()
```

#### SetRadioChannel
* * Sets new radio frequency 

```angelscript
void SetRadioChannel(uint16 newFreq)
```

#### SetLocation
* * Sets new location data for player-faction hq 

```angelscript
void SetLocation(uint locId, uint pid, uint x, uint y)
```

#### GetFactionLocation
* * Gets location data for player-faction hq 

```angelscript
bool GetFactionLocation(uint& out locId, uint& out pid, uint& out x, uint& out y)
```

#### SetLeaderId
* * Sets new leader id 

```angelscript
void SetLeaderId(uint id)
```

#### SetClaimId
* * Sets new claim id 

```angelscript
void SetClaimId(uint id)
```

#### SetLeaderTime
* * Sets time when claim will be able to confirm leadership without doing anything 

```angelscript
void SetLeaderTime(uint time)
```

#### SetClaimTime
* * Sets time when another claim will be allowed to be made (previous claimee will lose it) 

```angelscript
void SetClaimTime(uint time)
```

#### SetScore
* * Sets faction score 

```angelscript
void SetScore(uint score)
```

#### GetRecordsCount
* * Number of records with player's data 

```angelscript
uint GetRecordsCount()
```

#### GetMembersCount
* * Number of members 

```angelscript
uint GetMembersCount()
```

#### GetMembers
* * Ids table with members. 

```angelscript
uint GetMembers(array<uint>& members)
```

#### GetRecords
* * Ids table with records. 

```angelscript
uint GetRecords(array<uint>& records)
```

#### GetFactions
* * Ids table with known factions. 

```angelscript
uint GetFactions(array<int>& factions)
```

#### GetLastUsed
* * Gets the time when faction was last used/accessed. 

```angelscript
uint GetLastUsed()
```

#### Exists
* * Checks if the key exists in the array 

```angelscript
bool Exists(uint key)
```

#### FactionExists
* * Checks if the faction with given id is in the known factions list 

```angelscript
bool FactionExists(int faction_id)
```

#### UpdateData
* * Updates any_data associated with the array 

```angelscript
int UpdateData()
```

#### RemoveData
* * Removes data associated with the faction 

```angelscript
int RemoveData()
```

#### UpdateNewsData
* * Updates any_data associated with the news array 

```angelscript
void UpdateNewsData()
```

#### UpdateLastUsed
* * Updates last used for actual time. 

```angelscript
void UpdateLastUsed()
```

#### LogData
* * Logs the content of data array 

```angelscript
uint LogData(bool fullLog, array<string>& strings)
```

#### ModifyRank
```angelscript
int ModifyRank(uint id, uint newRank)
```

#### ModifyStatus
```angelscript
int ModifyStatus(uint id, uint newStatus)
```

#### ModifyFaction
```angelscript
int ModifyFaction(uint id, uint newFaction)
```

#### AddPlayer
* * Adds player without knowing anything about him * * @return FD_RESULT_* value (see _factions.fos) 

```angelscript
int AddPlayer(uint id)
```

#### RemovePlayer
* * Clears the area occupied by a given player in the array * so that it won't be taken into consideration, and may be later be filled by new data * * @return FD_RESULT_* value (see _factions.fos) 

```angelscript
int RemovePlayer(uint id)
```

#### AddFaction
* * Adds faction to the list of known factions. 

```angelscript
int AddFaction(int faction_id)
```

#### RemoveFaction
```angelscript
int RemoveFaction(int id)
```


## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| data | `[FactionData](faction_data.fos.md)@` | `GetDatabase(faction)` |  |

## Functions

### RegisterFaction

* * Registers new faction, initializes database for it * * * @param id faction id, has to be proper id (within FACTION_COUNT range) *			and has to have name assigned in factions_names dictionary * @param name name of the faction (has to be equal to one of the names stored in fotext.msg) * @param playerDriven for player gangs * * @return error code defined by REGRESULT_* macros 

```angelscript
int RegisterFaction(uint id, const string@ name, bool playerDriven)
```

### RebuildList

```angelscript
bool RebuildList()
```

### RegisterFaction

* * Registers faction with given name, reads back the id for it * * @return error code defined by REGRESULT_* macros 

```angelscript
int RegisterFaction(const string@ name, bool playerDriven, uint& out id)
```

### GetDatabase

* * Gets data object for given faction * * @return null for wrong faction id 

```angelscript
FactionData@ GetDatabase(uint faction_id)
```

### AddPlayer

* * Adds player without knowing anything about him * I'm not sure whether it's useful actually * * @param faction faction whose database we will update * @param id id of the player we want to add * * @retrun FD_RESULT_* value (see _factions.fos) 

```angelscript
int AddPlayer(uint faction, uint id)
```

### AddPlayer

* * Adds player with specified faction * * @param faction faction whose database we will update * @param id id of the player we want to add * @param playerFaction faction to which given player belongs to * * @return FD_RESULT_* value (see _factions.fos) 

```angelscript
int AddPlayer(uint faction, uint id, uint playerFaction)
```

### AddPlayer

* * Adds player with specified faction and rank * * @param faction faction whose database we will update * @param id id of the player we want to add * @param playerFaction faction to which given player belongs to * @param rank rank of the player * * @return FD_RESULT_* value (see _factions.fos) 

```angelscript
int AddPlayer(uint faction, uint id, uint playerFaction, uint rank)
```

### AddPlayer

* * Adds player with specified faction, rank and status * * @param faction faction whose database we will update * @param id id of the player we want to add * @param playerFaction faction to which given player belongs to * @param rank rank of the player * @param status status of the player * * @return FD_RESULT_* value (see _factions.fos) 

```angelscript
int AddPlayer(uint faction, uint id, uint playerFaction, uint rank, uint status)
```

### RemovePlayer

* * Removes player's info from faction's database * * @param faction faction whose database we will update * @param id id of the player the info about we want to remove * * @return FD_RESULT_* value (see _factions.fos) 

```angelscript
int RemovePlayer(uint faction, uint id)
```

### GetMembers

* * Fill the given array with member's ids * * @param faction id of the faction to take data from * @param ids array that will be filled with members identifiers * * @return length of created array, 0 if error occured 

```angelscript
uint GetMembers(uint faction, array<uint>& ids)
```

### GetRecordsCount

* * Gets the total number of records from the database 

```angelscript
uint GetRecordsCount(uint faction)
```

### GetMembersCount

* * Gets the total number of members 

```angelscript
uint GetMembersCount(uint faction)
```

### GetNextId

* * Gets id of the next record, with regard to record containing data for current Id * if members is set to true, seeks for next member record * * @return FD_RESULT_* value (see _factions.fos) 

```angelscript
int GetNextId(uint faction, uint currId, bool members, uint& out nextId)
```

### GetPrevId

* * Gets id of the previous record, with regard to record containing data for current Id * if members is set to true, seeks for prev member record * * @return FD_RESULT_* value (see _factions.fos) 

```angelscript
int GetPrevId(uint faction, uint currId, bool members, uint& out prevId)
```

### GetFirstId

* * Gets the id of the player stored at first record * if members is set to true seeks for first stored member * * @return FD_RESULT_* value (see _factions.fos) 

```angelscript
int GetFirstId(uint faction, bool members, uint& out id)
```

### GetFaction

* * Gets the faction of the given player, stores it in the faction argument. * * @param     faction        faction whose database we will check * @param     id             id of the player we want to check 

```angelscript
int GetFaction(uint faction, uint id)
```

### GetStatus

* * Gets the status of the given player, stores it in the appropriate argument. * * @param     faction    faction whose database we will check * @param     id         id of the player we want to check 

```angelscript
int GetStatus(uint faction, uint id)
```

### GetRank

* * Gets the rank of the given player, stores it in the appropriate argument. * * @param     faction    faction whose database we will check * @param     id         id of the player we want to check * @param     rank       player's rank will be stored there * 

```angelscript
int GetRank(uint faction, uint id)
```

### IsMember

* * Checks if the player with given id is the member of the faction * * @param     faction    faction whose database we will check * @param     cr         critter we want to check * * @return true if player belongs to the given faction, false when otherwise or when not found 

```angelscript
bool IsMember(uint faction, Critter& cr)
```

### IsMemberOffline

```angelscript
bool IsMemberOffline(uint faction, uint id)
```

### StoredInDB

* * Checks if the player with given id exists in the database * * @param     faction    faction whose database we will check * @param     id         id of the player we want to check * * @return true if player is in db, false otherwise 

```angelscript
bool StoredInDB(uint faction, uint id)
```

### GetLeaderId

* * Gets the id of the leader 

```angelscript
uint GetLeaderId(uint faction)
```

### SetLeaderId

* * Sets the id of the leader 

```angelscript
void SetLeaderId(uint faction, uint id)
```

### GetClaimId

* * Gets the id of the player who claimed leadership 

```angelscript
uint GetClaimId(uint faction)
```

### SetClaimId

* * Sets the id of the player who claimed leadership 

```angelscript
void SetClaimId(uint faction, uint id)
```

### GetLeaderTime

* * Gets the time when claimee will be able to confirm leadership without doing anything 

```angelscript
uint GetLeaderTime(uint faction)
```

### SetLeaderTime

* * Sets the time when claimee will be able to confirm leadership without doing anything * This is time for leader to act 

```angelscript
void SetLeaderTime(uint faction, uint time)
```

### GetClaimTime

* * Gets the time when next claim will be allowed (current claimee will loose his claim) 

```angelscript
uint GetClaimTime(uint faction)
```

### SetClaimTime

* * Sets the time when next claim will be allowed (current claimee will loose his claim) * This is time for claimee to act 

```angelscript
void SetClaimTime(uint faction, uint time)
```

### GetFactionRadioChannel

 ** Retrieves the radio frequency of given faction 

```angelscript
uint16 GetFactionRadioChannel(uint faction)
```

### SetFactionRadioChannel

* * Sets the radio channel for given faction 

```angelscript
void SetFactionRadioChannel(uint faction, uint16 channel)
```

### GetFactionLocationId

* * Retrieves location id for the faction * if the returned value is 0 it means faction doesn't use * dynamically created location, or there was some error * that should have been handled earlier (like not checking * returned value of CreateLocation) 

```angelscript
uint GetFactionLocationId(uint faction)
```

### SetFactionLocation

* * Sets new location data for faction hq 

```angelscript
void SetFactionLocation(uint faction, uint locId, uint pid, uint x, uint y)
```

### GetFactionLocation

* * Gets location data for player-faction hq 

```angelscript
bool GetFactionLocation(uint faction, uint& out locId, uint& out pid, uint& out x, uint& out y)
```

### GetFactionLocationCoords

* * Gets location coords 

```angelscript
void GetFactionLocationCoords(uint faction, uint& out x, uint& out y)
```

### GetFactionScore

* * Gets faction score - some global value used to abstract how succesfull faction is in some of their endeavours 

```angelscript
uint GetFactionScore(uint faction)
```

### ModifyFactionScore

* * Modifies faction score by given amount 

```angelscript
void ModifyFactionScore(uint faction, int amount)
```

### ModifyStatus

* * Modfy the player's status stored in db * * @param     faction    faction whose database we will modify * @param     id         player, the info about we want to modify * @param     newStatus  new value for player's status * * @return FD_RESULT_* value (see _factions.fos) 

```angelscript
int ModifyStatus(uint faction, uint id, uint newStatus)
```

### ModifyRank

* * Modfy the player's rank stored in db * * @param     faction    faction whose database we will modify * @param     id         player, the info about we want to modify * @param     newRank    new value for player's rank * * @return FD_RESULT_* value (see _factions.fos) 

```angelscript
int ModifyRank(uint faction, uint id, uint newRank)
```

### ModifyFaction

* * Modfy the player's faction stored in db * * @param     faction    faction whose database we will modify * @param     id         player, the info about we want to modify * @param     newFaction new value for player's faction * * @return FD_RESULT_* value (see _factions.fos) 

```angelscript
int ModifyFaction(uint faction, uint id, uint newFaction)
```

### InvitePlayer

* * Invites player to be a member of the faction * * @param     faction    faction whose database we will update * @param     playerId   id of the player we want to add * * @return FD_RESULT_* value (see _factions.fos) 

```angelscript
int InvitePlayer(uint faction, uint playerId)
```

### ConfirmInvitation

* * Adds member, who has been previously invited, to the given faction * * @param     faction    faction whose database we will update * @param     playerId   id of the player we want to add * * @remarks This method also updates local variables: *      * LVAR_factions_player_faction *      * LVAR_factions_player_rank * * @return FD_RESULT_* value (see _factions.fos) 

```angelscript
int ConfirmInvitation(uint faction, uint playerId)
```

### AddMember

* * Adds member to the given faction * * @param     faction    faction whose database we will update * @param     playerId   id of the player we want to add * @param     applyModifiers whether to apply reputation mods or not * * @return FD_RESULT_* value (see _factions.fos) 

```angelscript
int AddMember(uint faction, uint playerId, bool applyModifiers)
```

### AddMember

with default param

```angelscript
int AddMember(uint faction, uint playerId)
```

### ChangeRank

* * Change the players rank * * That means: * * degradation/promotion * * @param    faction     faction whose database we will modify * @param     playerId   id of the player, whose info about we want to modify * @param     newRank    new value for the player's rank * * @return FD_RESULT_* value (see _factions.fos) 

```angelscript
int ChangeRank(uint faction, uint playerId, uint newRank)
```

### ExpelMember

* * Expel member * * @param     faction    faction whose database we will modify * @param     playerId   id of the player, whose info about we want to modify * @param	 applyModifiers	whether to apply reputation modifiers on leaving or not * @remarks *      When player's faction is the same as the database owning faction, *      we also modify appropriate local variable: LVAR_factions_player_faction * * @return FD_RESULT_* value (see _factions.fos) 

```angelscript
int ExpelMember(uint faction, uint playerId, bool applyModifiers)
```

### ExpelMember

with default param

```angelscript
int ExpelMember(uint faction, uint playerId)
```

### AddFactionNews

* * Adds news * * @param     master id of the player performing operation of given type * @param     slave  id of the player on which operation is performed * @param     type   type of the opeartion * @param     time   time at which operation happened (__FullSecond/ELAPSED_TIME) 

```angelscript
void AddFactionNews(uint faction, uint master, uint slave, uint type)
```

### GetFactionNewsCount

* * Retrieves number of news stored for a given faction 

```angelscript
uint GetFactionNewsCount(uint faction)
```

### GetPlayerFaction

* * Helper method to determine faction player belongs too * described in appropriate local variable 

```angelscript
uint GetPlayerFaction(uint playerId)
```

### GetPlayerRank

* * Helper method to determine rank of the player * which is stored in appropriate local variable 

```angelscript
uint GetPlayerRank(uint playerId)
```

### GetFactionNameMsg

* * Retrieves number of the msg string representing faction name 

```angelscript
int GetFactionNameMsg(uint faction)
```

### GetFactionAliasNameMsg

* * Retrieves number of the msg string representing faction variation name(aliases) 

```angelscript
int GetFactionAliasNameMsg(uint faction)
```

### CheckFactionBaseCoords

* * Checks whether given coords are within base area of one of the playerfactions * returns faction id in case of success, 0 otherwise 

```angelscript
uint CheckFactionBaseCoords(uint x, uint y)
```

### IsGang

* * Checks if faction is playerdriven gang 

```angelscript
bool IsGang(uint faction)
```

### IsBigFaction

 Helper to determine whether it is big(npc) faction or playerdriven faction 

```angelscript
bool IsBigFaction(uint faction)
```

### IsTheSameFaction

 Helper 

```angelscript
bool IsTheSameFaction(uint player1Id, uint player2Id)
```

### _Resign

 Helper 

```angelscript
void _Resign(uint playerId)
```

### UpdateLastUsed

* * Updates 'last used' variable, that tracks time when faction was last time accessed. * It sets the time for current full minute. 

```angelscript
void UpdateLastUsed(uint faction)
```

### GetFactionLog

* * creates array of strings representing log of the faction data * if faction is 0 then all are displayed * returns number of strings 

```angelscript
uint GetFactionLog(uint faction, bool fullLog, array<string>& strings, uint begin, uint end)
```

### SaveFactionData

```angelscript
bool SaveFactionData(uint faction)
```

### FactionExists

```angelscript
bool FactionExists(uint faction)
```

### test

```angelscript
void test(Critter& cr, int p0, int p1, int p2)
```

### fix

careful!

```angelscript
void fix(Critter& cr, int p0, int p1, int p2)
```


