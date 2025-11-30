---
title: npc_common.fos
description: " FOnline: 2238 Rotators  npc_common.fos ..."
---

# npc_common.fos


FOnline: 2238
Rotators

npc_common.fos


## Includes

- `_colors.fos`
- `_macros.fos`
- `weap_anim_table_h.fos`
- `npc_common_h.fos`
- `npc_names_h.fos`
- `groups_h.fos`
- `messages_h.fos`
- `utils_h.fos`
- `npc_planes_h.fos`
- `reputations_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __NPC_COMMON__ |  |  |
| _FreeHex | `(map.IsHexPassed(hx, hy) && @ (map.GetCritter(hx, hy)) == null)` |  |
| _AddHex | `\` |  |
| _OldHex | `(hx == px && hy == py)` |  |
| _ReturnHex | `outX = hx; outY = hy; return true` |  |

## Functions

### AttackCritter

```angelscript
bool AttackCritter(Critter& attacker, Critter& target, uint minhp)
```

### AttackCritter

```angelscript
bool AttackCritter(Critter& attacker, Critter& target)
```

### HasIntelligentBrain

```angelscript
bool HasIntelligentBrain(Critter& cr)
```

### UnsetCritterIllegalFlag

```angelscript
void UnsetCritterIllegalFlag(Critter& critter)
```

### UnsetCritterIllegalFlag

```angelscript
void UnsetCritterIllegalFlag(Critter& critter, int location)
```

### UnsetCritterIllegalFlag

```angelscript
void UnsetCritterIllegalFlag(uint id, int location)
```

### SetCritterIllegalFlag

```angelscript
void SetCritterIllegalFlag(Critter& critter, int reason)
```

### SetCritterIllegalFlag

```angelscript
void SetCritterIllegalFlag(Critter& critter, int location, int reason)
```

### PutAwayItems

```angelscript
void PutAwayItems(Critter& critter)
```

### DropAllItems

```angelscript
void DropAllItems(Critter& critter)
```

### GetCritterIllegalFlag

* * Get illegal flag status of critter in a specific location. 

```angelscript
int GetCritterIllegalFlag(Critter& critter, int location)
```

### GetCritterIllegalFlag

* * Clear illegal flags in critter's current location. 

```angelscript
int GetCritterIllegalFlag(Critter& critter)
```

### ClearIllegalFlags

* * Clear illegal flags in all towns 

```angelscript
void ClearIllegalFlags(Critter& critter)
```

### IsFlaggedAsIllegal

```angelscript
bool IsFlaggedAsIllegal(Critter& critter)
```

### IsFlaggedAsIllegal

```angelscript
bool IsFlaggedAsIllegal(Critter& critter, int location)
```

### Heal

* * Heal a critter. * @param cr Critter handle. * @remarks This function will remove poison, radiation, heal limbs and give the critter full HP. 

```angelscript
void Heal(Critter& cr)
```

### HasSameScript

* * Check if two critters has the same script assigned. 

```angelscript
bool HasSameScript(Critter& critter1, Critter& critter2)
```

### IsInLocation

* * Check if a critter is in a specific location. 

```angelscript
bool IsInLocation(Critter& critter, int locationPID)
```

### MoveByDir

```angelscript
bool MoveByDir(Critter& critter, uint8 dir, uint steps, bool run)
```

### GetNearGuards

* * Gets all general purpose guards in a radius around given hex. 

```angelscript
uint GetNearGuards(Map@ map, uint16 hexX, uint16 hexY, uint radius, array<Critter@>@ crits)
```

### GetNearFactionGuards

* * Gets all faction guards in a radius around given hex. 

```angelscript
uint GetNearFactionGuards(Map@ map, uint16 hexX, uint16 hexY, uint radius, uint faction, array<Critter@>@ crits)
```

### ArmBestWeapon

* * Arm the best weapon available to the NPC. * @remarks Firstly, weapons of the best skill of the NPC is tried, then in the following order: SK_BIG_GUNS, SK_ENERGY_WEAPONS, SK_SMALL_GUNS, SK_THROWING, SK_UNARMED 

```angelscript
Item@ ArmBestWeapon(Critter& critter)
```

### ArmFavoriteWeapon

* * Tries to arm NPC with its favorite weapon. 

```angelscript
Item@ ArmFavoriteWeapon(Critter& critter)
```

### FindFreeHexes

```angelscript
void FindFreeHexes(Map@ map, uint16 hexX, uint16 hexY, int& num, array<uint16>& coordsX, array<uint16>& coordsY)
```

### FindNearestFreeHex

search near area for free hex

```angelscript
bool FindNearestFreeHex(Map@ map, uint16 hexX, uint16 hexY, uint16& outX, uint16& outY)
```

### Flee

```angelscript
bool Flee(Critter& cr)
```

### Flee

* * Flee to worldmap via closest exitgrid 

```angelscript
bool Flee(Critter& cr, bool Run)
```

### MoveRandom

* * Issue random walk for a critter to a hex in stepDist distance, as long as the actual distance * to home pos is less than maxDist. In this case, it issues walkplane closely to homepos. * * @param maxDist Max distance in hexes. * @param stepDist Step distance, the actual distance of single move 

```angelscript
void MoveRandom(Critter& npc, uint maxDist)
```

### MoveRandom

```angelscript
void MoveRandom(Critter& npc, uint maxDist, bool Run)
```

### MoveRandom

```angelscript
void MoveRandom(Critter& npc, uint maxDist, uint stepDist, bool Run)
```

### CanUseWeapon

* * Checks if a critter can use a weapon (has an animation for it). * @param critter Critter handle. * @param proto Proto Id of the weapon to check. 

```angelscript
bool CanUseWeapon(Critter& critter, uint proto)
```

### CanUseWeapon

* * Checks if a critter can use a weapon (has an animation for it). * @param critter Critter handle. * @param weapon Weapon to check. 

```angelscript
bool CanUseWeapon(Critter& critter, Item@ weapon)
```

### HasUnusableWeapon

* * Checks if a critter can't use a weapon from a specific bag. * @param critter Critter handle. * @param bag BagId to check. * @return If no weapons are found at all, or if all weapons are usable, true. Otherwise, false. * @remarks Usable here refers to them having the animations needed to use the weapon. 

```angelscript
bool HasUnusableWeapon(Critter& critter, uint bag)
```

### HasUnusableWeapon

* * Checks if a critter can't use a weapon in his inventory. * @param critter Critter handle. * @return If no weapons are found at all, or if all weapons are usable, true. Otherwise, false. * @remarks Usable here refers to them having the animations needed to use the weapon. 

```angelscript
bool HasUnusableWeapon(Critter& critter)
```

### HasUnusableWeapon

* * Checks if a critter PID can't use a weapon from a specific bag. * @param crpid Critter PID. * @param bag BagId to check. * @return If no weapons are found at all, or if all weapons are usable, true. Otherwise, false. * @remarks Usable here refers to them having the animations needed to use the weapon. 

```angelscript
bool HasUnusableWeapon(uint crpid, uint bag)
```

### AddWaitPlan

* * The critter will wait for the specified time without getting busy (it can speak to players). * @param critter Critter handle. * @param waittime Time in ms. 

```angelscript
void AddWaitPlan(Critter& critter, uint waittime)
```

### TryReportOffense

report attack/death in encounter etc.

```angelscript
void TryReportOffense(Critter@ cr, Critter@ offender, int reputationdrop)
```

### GetStoredFirstName

```angelscript
string GetStoredFirstName(Critter& critter)
```

### GetStoredName

Get name stored in lvars

```angelscript
string GetStoredName(Critter& critter)
```

### GenerateNewName

Generate a new name and save it

```angelscript
string GenerateNewName(Critter& critter)
```

### GetCrittersWithScript

* * Gather all critters from a map that share the given script, and comply to the search parameters. * @param map Map to take the critters from. * @param pid Critters pid, 0 to take all. * @param findType Critters type and state, same as for generic find functions. * @param scriptName Name of the script, if module is not given then current is used. * @param funcDeclaration Declaration of the function in format retval %s(args). * @param critters Array of critters to be filled with critters, or a null handle. * @return Number of critters found. 

```angelscript
uint GetCrittersWithScript(Map& map, uint16 pid, uint findType, string& scriptName, string& funcDeclaration, array<Critter@>@ critters)
```

### GetCrittersLoc

```angelscript
uint GetCrittersLoc(Location& loc, uint16 pid, uint findType, array<Critter@>@ critters)
```

### SetDeleteEvent

```angelscript
void SetDeleteEvent(Critter& cr, uint time)
```

### DropDeleteEvent

```angelscript
void DropDeleteEvent(Critter& cr)
```

### cte_Delete

```angelscript
uint cte_Delete(Critter& cr, int identifier, uint& rate)
```

### r_MoveRandom

```angelscript
void r_MoveRandom(Critter& player, Critter@npc, int val)
```

### d_HasNumPlayersInParty

* * Checks if a party has specified numbers of members. * @param num The amount of players to check for. * @remarks A player is considered to be in the party if he has tagged the leader and is within 8 hexes of the leader. 

```angelscript
bool d_HasNumPlayersInParty(Critter& leader, Critter@npc, int num)
```

### d_HasNotNumPlayersInParty

* * Checks if a party has NOT specified numbers of members. * @param num The amount of players to check for. * @remarks A player is considered to be in the party if he has tagged the leader and is within 8 hexes of the leader. 

```angelscript
bool d_HasNotNumPlayersInParty(Critter& leader, Critter@npc, int val)
```

### TransferToNPCMap

```angelscript
void TransferToNPCMap(Critter& critter)
```

### e_UnsetIllegalFlag

Event that removes flag from certain location after some time, instead of removing on death

```angelscript
uint e_UnsetIllegalFlag(array<uint>@ values)
```


