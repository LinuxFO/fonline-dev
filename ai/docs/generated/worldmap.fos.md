---
title: worldmap.fos
description: " FOnline: Reloaded   worldmap.fos ..."
---

# worldmap.fos


FOnline: Reloaded


worldmap.fos


## Includes

- `_bags.fos`
- `_macros.fos`
- `groups_h.fos`
- `worldmap_h.fos`
- `logging_h.fos`
- `_colors.fos`
- `_macros.fos`
- `_maps.fos`
- `_scripts.fos`
- `groups_h.fos`
- `mapdata_h.fos`
- `npc_common_h.fos`
- `utils_h.fos`
- `world_common_h.fos`
- `worldmap_data.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __WORLDMAP_MODULE__ |  |  |
| STR_GROUP | `# (g)    (20000000 + g)` |  |
| _InjectLog | `# (text) file __f; __f.open("logs/injectvalue.log", "a"); __f.writeString(GetCurrentDateTimeString() + "> " + text + "\n"); __f.close();` | * * Injects value given by the amount to the zones chosen using world coordinate.  |
| FOUNDED_ENCOUNTER_LIVE_TIME | `(REAL_MINUTE(60))` |  |
| _CheckSpecialEncounter | `# (__loc, __condition, __result) if(__condition) { __result; return __loc; }` |  |
| GROUP_NPC_DATA_ITEM | `("0")` |  |
| GROUP_NPC_DATA_PERK | `("1")` |  |
| SAVE_INTERVAL | `(REAL_MINUTE(10))` |  |

## Classes

### CCheck

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| Type | `uint` |  |  |
| Index | `uint` |  |  |
| Operator | `uint8` |  |  |
| Value | `int` |  |  |

**Methods**

#### Set
```angelscript
void Set(uint type, uint index, uint8 operator, int value)
```

### CEncounterPerk

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| index | `uint` |  |  |
| level | `uint` |  |  |
| chance | `uint` |  |  |

### CEncounterObject

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| ObjectType | `uint` |  |  |
| Pid | `uint16` |  |  |
| Dialog | `uint` |  |  |
| Script | `string` |  |  |
| Distance | `uint` |  |  |
| Bag | `uint` |  |  |
| NpcRole | `uint` |  |  |
| TeamId | `uint` |  |  |
| Checks | `array<[CCheck](worldmap.fos.md)>` |  |  |
| Ratio | `uint` |  | Only for critter |
| Dead | `bool` |  |  |
| Armor | `int` |  |  |
| Helmet | `int` |  |  |
| OverrideCrtype | `int` |  |  |
| Minimum | `uint` |  | Only for item |
| Maximum | `uint` |  |  |
| Slot | `uint` |  |  |
| cost | `uint` |  | value required to generate object |
| Perks | `array<[CEncounterPerk](worldmap.fos.md)>` |  |  |
| BrokenMin | `uint` |  | for items: broken count |
| BrokenMax | `uint` |  |  |
| modes | `array<uint>` |  | modes to be set |

**Methods**

#### NewCheck
```angelscript
CEncounterObject@ NewCheck(uint type, uint index, uint8 operator, int value)
```

#### SetPid
```angelscript
CEncounterObject@ SetPid(uint16 pid)                            { Pid = pid; return this; }
```

#### SetDialog
```angelscript
CEncounterObject@ SetDialog(uint dialog)                        { Dialog = dialog; return this; }
```

#### SetScript
```angelscript
CEncounterObject@ SetScript(string& script)                     { Script = script; return this; }
```

#### SetBag
```angelscript
CEncounterObject@ SetBag(uint bag)                              { Bag = bag; return this; }
```

#### SetNpcRole
```angelscript
CEncounterObject@ SetNpcRole(uint role)                         { NpcRole = role; return this; }
```

#### SetTeamId
```angelscript
CEncounterObject@ SetTeamId(uint teamid)                        { TeamId = teamid; return this; }
```

#### SetTeamId
```angelscript
CEncounterObject@ SetTeamId(uint faction, uint rank, uint mode) { TeamId = _TeamIdPack(faction, rank, mode); return this; }
```

#### SetDistance
```angelscript
CEncounterObject@ SetDistance(uint distance)                       { Distance = distance; return this; }
```

#### CheckRandom
```angelscript
CEncounterObject@ CheckRandom(int value)                           { NewCheck(CHECK_RANDOM, 0, 0, value); return this; }
```

#### CheckStat
```angelscript
CEncounterObject@ CheckStat(uint index, uint8 operator, int value) { NewCheck(CHECK_STAT, index, operator, value); return this; }
```

#### CheckPerk
```angelscript
CEncounterObject@ CheckPerk(uint index, uint8 operator, int value) { NewCheck(CHECK_PERK, index, operator, value); return this; }
```

#### CheckLVar
```angelscript
CEncounterObject@ CheckLVar(uint index, uint8 operator, int value) { NewCheck(CHECK_LVAR, index, operator, value); return this; }
```

#### CheckGVar
```angelscript
CEncounterObject@ CheckGVar(uint index, uint8 operator, int value) { NewCheck(CHECK_GVAR, index, operator, value); return this; }
```

#### CheckHour
```angelscript
CEncounterObject@ CheckHour(uint8 operator, int value)             { NewCheck(CHECK_HOUR, 0, operator, value); return this; }
```

#### SetRatio
```angelscript
CEncounterObject@ SetRatio(uint ratio)                             { Ratio = ratio; return this; }
```

#### SetDead
```angelscript
CEncounterObject@ SetDead(bool dead)                               { Dead = dead; return this; }
```

#### SetMinimum
```angelscript
CEncounterObject@ SetMinimum(uint minimum)                         { Minimum = minimum; return this; }
```

#### SetMaximum
```angelscript
CEncounterObject@ SetMaximum(uint maximum)                         { Maximum = maximum; return this; }
```

#### SetSlot
```angelscript
CEncounterObject@ SetSlot(uint slot)                               { Slot = slot; return this; }
```

#### Mode
```angelscript
CEncounterObject@ Mode(uint mode)
```

#### Mode
```angelscript
CEncounterObject@ Mode(uint mode, uint val)
```

#### AddPerk
```angelscript
CEncounterObject@ AddPerk(uint index, uint level, uint chance)
```

#### AddItem
```angelscript
CEncounterObject@ AddItem(uint16 pid, uint min, uint max, uint slot)
```

#### AddItem
```angelscript
CEncounterObject@ AddItem(uint16 pid, uint min, uint max, uint slot, uint brokenMin, uint brokenMax)
```

#### GetCost
* * Value required to generate given object, for the purpose of calculating the average priece only. 

```angelscript
uint GetCost() { return cost; }
```

#### SetModes
* * Set modes for given critter' instance. 

```angelscript
void SetModes(Critter& npc)
```

### CEncounterGroup

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| Index | `uint` |  |  |
| TeamNum | `uint` |  |  |
| Position | `uint` |  |  |
| Spacing | `uint` |  |  |
| DistMin | `uint` |  | distance from center of encounter |
| DistMax | `uint` |  |  |
| RatioMin | `uint` |  | denotes number of 'ratio' critters in group...some critters can be multiplied using those values using their Ratio(EncounterObject::Ratio) property. It's percentage. For example, radscorpion in Radscorpions group have ratio 100% so if RatioMin is equal to 1 and RatioMax is equal to 10 we will get Random(1,10) radscorpions |
| RatioMax | `uint` |  |  |
| Cost | `uint` |  |  |
| QuantityNight | `float` |  | quantity ratio modifiers |
| QuantityDay | `float` |  |  |
| Objects | `array<[CEncounterObject](worldmap.fos.md)>` |  |  |

**Methods**

#### GetModifiedQuantity
* * Gets the modified quantity for the group, basing on the value passed from zone. 

```angelscript
uint GetModifiedQuantity(uint quantity)
```

#### GetCost
* * Gets value needed to spawn group, knowing the ratio 

```angelscript
uint GetCost(int ratio)
```

#### SetAverageCost
* * Sets the average vaule of the group, derived from ratio and objects. It must be called every time the group is defined, see InitGroupsCost(). 

```angelscript
void SetAverageCost()
```

#### NewObject
```angelscript
CEncounterObject@ NewObject()
```

#### AddCritter
```angelscript
CEncounterObject@ AddCritter(uint16 pid)
```

#### AddItem
```angelscript
CEncounterObject@ AddItem(uint16 pid)
```

### CAction

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| Target | `int` |  |  |
| Action | `int` |  |  |

### CEncounter

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| Difficulty | `int` |  |  |
| LocationPid | `uint16` |  |  |
| Special | `bool` |  |  |
| Groups | `array<uint>` |  |  |
| Players | `array<uint>` |  |  |
| Checks | `array<[CCheck](worldmap.fos.md)>` |  | uint[] RatioMin; uint[] RatioMax; |
| Ratio | `uint` |  |  |

**Methods**

#### AddGroup
```angelscript
CEncounter@ AddGroup(uint group /*, uint ratioMin, uint ratioMax*/)
```

#### AddPlayer
```angelscript
CEncounter@ AddPlayer(Critter& player)
```

#### GetPlayer
```angelscript
Critter@ GetPlayer(uint i)
```

#### NewCheck
```angelscript
CEncounter@ NewCheck(uint type, uint index, uint8 operator, int value)
```

#### SetLocationPid
```angelscript
CEncounter@ SetLocationPid(uint16 locationPid)               { LocationPid = locationPid; return this; }
```

#### SetSpecial
```angelscript
CEncounter@ SetSpecial(bool special)                         { Special = special; return this; }
```

#### CheckRandom
```angelscript
CEncounter@ CheckRandom(int value)                           { NewCheck(CHECK_RANDOM, 0, 0, value); return this; }
```

#### CheckStat
```angelscript
CEncounter@ CheckStat(uint index, uint8 operator, int value) { NewCheck(CHECK_STAT, index, operator, value); return this; }
```

#### CheckPerk
```angelscript
CEncounter@ CheckPerk(uint index, uint8 operator, int value) { NewCheck(CHECK_PERK, index, operator, value); return this; }
```

#### CheckLVar
```angelscript
CEncounter@ CheckLVar(uint index, uint8 operator, int value) { NewCheck(CHECK_LVAR, index, operator, value); return this; }
```

#### CheckGVar
```angelscript
CEncounter@ CheckGVar(uint index, uint8 operator, int value) { NewCheck(CHECK_GVAR, index, operator, value); return this; }
```

#### CheckHour
```angelscript
CEncounter@ CheckHour(uint8 operator, int value)             { NewCheck(CHECK_HOUR, 0, operator, value); return this; }
```

#### GenerateEncounterString
```angelscript
int GenerateEncounterString(Critter& cr, string@ str, bool groupAdded, bool awareness)
```

#### getProbablyId
```angelscript
uint getProbablyId(uint i)
```

#### Ask
leader.SayMsg(SAY_ENCOUNTER_TB, TEXTMSG_GM, feAlready.OwnerGroup ? (10000026) : (10000025),  "$str1" + "|0xffff0000 " + "Encounter is in TURN-BASED mode." + "|0x0000FF00 " + "\n\n" + "$str2" + "Do you wish to encounter: " + "$player" + GetSafePlayerName(feAlready.OwnerId));

```angelscript
void Ask(int say, Critter@ leader, bool isTB)
```

#### Say
```angelscript
void Say(Critter@ leader, Critter@ player)
```

#### IsSingleGroup
```angelscript
bool IsSingleGroup() { return Groups.length() <= 2; }
```

#### GetCost
```angelscript
int GetCost()
```

### CZone

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| Groups | `array<uint>` |  |  |
| Quantities | `array<int>` |  |  |
| Flags | `array<uint>` |  |  |
| x | `uint` |  | world coords |
| y | `uint` |  |  |
| Difficulty | `int` |  |  |
| LocationPids | `array<uint16>` |  |  |
| Terrain | `uint` |  |  |
| Fill | `uint` |  |  |
| MorningChance | `uint` |  |  |
| AfternoonChance | `uint` |  |  |
| NightChance | `uint` |  |  |
| Factor | `uint8` |  | percentage factor that adjust a chance of finding prospects (and other special encounters in the future) initialized on every start, so that it gives some randomness to how players need to look for things |
| value | `int` |  | value that can be used to generate encounter objects |

**Methods**

#### GetX
```angelscript
uint GetX() { return x; }
```

#### GetY
```angelscript
uint GetY() { return y; }
```

#### GetLocationPids
```angelscript
uint GetLocationPids(array<uint16>& pids)
```

#### ContainsFlag
* * Checks if zone is flagged with given flag. 

```angelscript
bool ContainsFlag(uint flag)
```

#### GetQuantity
* * Retrieves quantity of the given group in zone, taking the day/night modifiers into account. 

```angelscript
uint GetQuantity(uint group)
```

#### GetBaseQuantity
* * Retrieves base quantity of the given group in zone (without their day/night mods). 

```angelscript
uint GetBaseQuantity(uint group)
```

#### SetQuantity
* * Sets the quantity for given group. 

```angelscript
void SetQuantity(uint group, uint quantity)
```

#### ChangeQuantity
* * Changes the quantity for given group. 

```angelscript
void ChangeQuantity(uint group, int mod)
```

#### GetChance
* * Chance (to be tested as percentage) of the encounter in given zone, depending on the groups and their quantities, and the current time. 

```angelscript
uint GetChance()
```

#### GetValue
* * Retrieves the value for that zone. 

```angelscript
int GetValue()
```

#### SetValue
```angelscript
void SetValue(int val)
```

#### AddValue
```angelscript
void AddValue(int val)
```

#### SubValue
* * Decreases value for given zone. 

```angelscript
void SubValue(uint val)
```

#### GetTerrain
* * Retrieves the type of terrain for given world-coordinates. 

```angelscript
uint GetTerrain()
```

#### GetFactor
* * Gets the random factor that decides about special discoveries. 

```angelscript
uint8 GetFactor()
```

#### SetFactor
* * Sets the random factor that decides about special discoveries. 

```angelscript
void SetFactor(uint8 factor)
```

#### AddLocationPid
```angelscript
void AddLocationPid(uint16 locationPid)
```

#### ChooseGroups
* * Chooses groups for an encounter. 

```angelscript
void ChooseGroups(Critter& leader, CEncounter& enc)
```

#### ChooseGroups2
* 06-02-2014 Cubik: nowa funckja ChooseGroups2 uwzgledniajaca czy to jest karawana, liczbe graczy i level gracza * Chooses groups for an encounter. 

```angelscript
void ChooseGroups2(Critter& leader, CEncounter& enc, int max_level_gracza, bool isCaravan, uint players_count, int min_level_gracza, bool isPlayerCaravan)
```

### CFoundedEncounter

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| Index | `uint` |  |  |
| Encounter | `[CEncounter](worldmap.fos.md)@` |  |  |
| Zone | `[CZone](worldmap_players.fos.md)@` |  |  |
| IsGenerated | `bool` |  |  |
| FullSecond | `uint` |  |  |
| PositionX | `uint` |  |  |
| PositionY | `uint` |  |  |
| OwnerId | `uint` |  |  |
| OwnerGroup | `bool` |  |  |
| TurnBased | `bool` |  |  |
| LocationId | `uint` |  |  |
| StartHexX | `uint16` |  |  |
| StartHexY | `uint16` |  |  |
| DirBusy | `array<bool>` |  |  |
| FirstDirIdx | `uint8` |  |  |
| AskChance | `uint` |  |  |
| Actions | `array<uint>` |  |  |

**Methods**

#### DetermineAction
* * Determines action between 2 groups. 

```angelscript
int DetermineAction(int gr1, int gr2)
```

#### PrepareActions
* * Prepares actions for groups. 

```angelscript
void PrepareActions()
```


## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| FoundedEncountersLastIndex | `uint` | `0` |  |
| enc | `[CEncounter](worldmap.fos.md)@` | `CEncounter()` |  |
| len | `uint` | `0` | count number of players/mercs within group |
| followers | `int` | `0` |  |
| players_count | `uint` | `0` | 05-02-2014 Cubik: obliczenie liczby graczy w grupie enco |
| max_level_gracza | `int` | `0` |  |
| min_level_gracza | `int` | `9999` |  |
| fe | `[CFoundedEncounter](worldmap.fos.md)@` | `CreateFoundedEncounter(x, y, @enc, zone, leader.Id, group.length() > 1)` |  |
| outdoorsman | `int` | `guide.Skill[SK_OUTDOORSMAN] - zone.Difficulty` |  |
| fe | `[CFoundedEncounter](worldmap.fos.md)@` | `CreateFoundedEncounter(x, y, null, zone, leader.Id, group.length() > 1)` |  |
| t | `uint` | `GetTick() - start` |  |

## Functions

### GetZone

* * Retrieves zone for given world-coords. 

```angelscript
IZone@ GetZone(uint x, uint y)
```

### ZoneContainsFlag

```angelscript
bool ZoneContainsFlag(CZone@ zone, uint flag)
```

### GetZonesWithFlag

* * Fetches the zones that are marked with given flag. 

```angelscript
uint GetZonesWithFlag(uint flag, array<IZone@>@ zones)
```

### InjectValue

```angelscript
void InjectValue(uint x, uint y, uint amount, uint from)
```

### WorldmapGetTotalValue

* * Total value of encounter store. 

```angelscript
int WorldmapGetTotalValue()
```

### SetZone

table is obsolete

```angelscript
CZone@ SetZone(uint zx, uint zy, uint table, int difficulty, uint terrain, uint fill, uint morningChance, uint afternoonChance, uint nightChance)
```

### SetZone

```angelscript
CZone@ SetZone(uint zx, uint zy, uint table, int difficulty, uint terrain, uint fill, uint chance)
```

### CheckCompare

```angelscript
bool CheckCompare(int val1, uint8 operator, int val2)
```

### CheckChecks

```angelscript
bool CheckChecks(array<CCheck>@ checks, array<Critter@>@ critters)
```

### CreateFoundedEncounter

```angelscript
CFoundedEncounter@ CreateFoundedEncounter(uint x, uint y, CEncounter@ encounter, CZone@ zone, uint ownerId, bool ownerGroup)
```

### GetFoundedEncounter

```angelscript
CFoundedEncounter@ GetFoundedEncounter(uint index)
```

### GetNearFoundedEncounter

```angelscript
CFoundedEncounter@ GetNearFoundedEncounter(array<Critter@>@ group, uint x, uint y, uint radius)
```

### GetFreeDir

```angelscript
uint GetFreeDir(array<bool>& dirBusy, uint8& inout firstDirIdx)
```

### RotatePosition

```angelscript
void RotatePosition(uint toDir, array<uint>& positionsDirs)
```

### MovePositionPoint

```angelscript
void MovePositionPoint(Map& map, uint16& pointX, uint16& pointY, array<uint>& positionDirs, uint pathIndex, uint count, uint spacing)
```

### ParseEncounterObject

```angelscript
void ParseEncounterObject(CEncounterObject@ obj, Map@ map, uint16 posX, uint16 posY, uint8 reversDir, array<Critter@>& crittersGrouop, uint teamId, uint level)
```

### ActionFighting

 

```angelscript
void ActionFighting(array<Critter@>& npcL, array<Critter@>& npcR)
```

### GenerateEncounter

 

```angelscript
Map@ GenerateEncounter(CFoundedEncounter@ fe, array<Critter@>@ critters)
```

### GuideReward

```angelscript
void GuideReward(Critter@ leader, Critter@ guide, int amount)
```

### OnSpecialEncounterCreated

```angelscript
void OnSpecialEncounterCreated(Location@ loc, array<Critter@>& group, Item@ car, uint encounterDescriptor)
```

### CheckSpecialEncounter

```angelscript
int CheckSpecialEncounter(Critter@ leader, CZone@ zone)
```

### InviteToEncounter

```angelscript
void InviteToEncounter(array<Critter@>& group, Item@ car, uint encounterDescriptor, int combatMode, uint& mapId, uint16& hexX, uint16& hexY, uint8& dir)
```

### e_UnlockEncounterCaravan

```angelscript
uint e_UnlockEncounterCaravan(array<uint>@ values)
```

### OnPlayerCaravanEnterLocation

```angelscript
void OnPlayerCaravanEnterLocation(array<Critter@>& group, Item& car, uint locId, bool special)
```

### OnCarGroupEnterLocation

```angelscript
void OnCarGroupEnterLocation(array<Critter@>& group, Item& car, uint locId)
```

### dumpencountergroups

```angelscript
void dumpencountergroups(Critter&, int, int, int)
```

### DumpEncounterGroups

```angelscript
void DumpEncounterGroups()
```

### LoadWorldmapGroups

```angelscript
void LoadWorldmapGroups(string@ fileName)
```

### WorldmapInit

```angelscript
void WorldmapInit()
```

### GetGlobalMapRelief

```angelscript
uint GetGlobalMapRelief(uint x, uint y)
```

### InitGroupsCost

```angelscript
void InitGroupsCost()
```

### SaveGroupsQuantities

* * Saves the groups/quantities from the worldmap zones. * Format: number of groups, [group index, quantity], [,]... 

```angelscript
void SaveGroupsQuantities()
```

### LoadGroupsQuantities

* * Loads the groups/quantities into the worldmap zones. 

```angelscript
void LoadGroupsQuantities()
```

### e_WorldmapUpdate

```angelscript
uint e_WorldmapUpdate(array<uint>@ values)
```

### setquantity

```angelscript
void setquantity(Critter& cr, int group, int mod, int direct)
```

### listgroups

```angelscript
void listgroups(Critter& cr, int, int, int)
```

### savezones

```angelscript
void savezones(Critter& cr, int, int, int)
```

### loadzones

```angelscript
void loadzones(Critter& cr, int, int, int)
```

### MakeEncounterBoss

```angelscript
void MakeEncounterBoss(uint npcId, uint groupNum)
```


