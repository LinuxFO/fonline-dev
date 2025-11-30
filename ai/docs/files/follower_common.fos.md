---
title: follower_common.fos
description: " FOnline: 2238 Rotators  follower_common.fos ..."
---

# follower_common.fos


FOnline: 2238
Rotators

follower_common.fos


## Includes

- `_basetypes.fos`
- `_macros.fos`
- `follower_h.fos`
- `groups_h.fos`
- `lexems_h.fos`
- `mercs_h.fos`
- `utils_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __FOLLOWER_COMMON__ |  |  |

## Functions

### IsMerc

```angelscript
bool IsMerc(Critter& follower)
```

### IsFollowing

* * Check if a follower is in follow mode (either automatic or manual). 

```angelscript
bool IsFollowing(Critter& critter)
```

### IsOwnersFollower

* * Check if a follower belongs to a specific owner. * @param owner The proposed owner. * @param critter The follower. * @remarks If critter is not a follower, false will be returned. 

```angelscript
bool IsOwnersFollower(Critter& owner, Critter& critter)
```

### GetPartyPoints

* * Checks how many partypoints a certain FollowerType consumes. * @param FollowerType FOLLOWER_TYPE_* define of the specific follower type to get. * @remarks If FollowerType is not found, a safeguard value is returned to prevent exploits. 

```angelscript
uint GetPartyPoints(uint FollowerType)
```

### GetNumberOfType

* * Checks how many followers a player has of a certain FollowerType. 

```angelscript
uint GetNumberOfType(Critter& player, uint FollowerType)
```

### GetNumberOfCompanions

* * Checks how many companions a player has in total. 

```angelscript
uint GetNumberOfCompanions(Critter& player)
```

### GetNumberOfMercs

* * Checks how many mercs a player has in total. 

```angelscript
uint GetNumberOfMercs(Critter& player)
```

### GetPartyPointsMax

* * Returns the amount of party points a player has. 

```angelscript
uint GetPartyPointsMax(Critter& player)
```

### GetPartyPointsUsed

* * Returns the amount of party points a player is currently using. 

```angelscript
uint GetPartyPointsUsed(Critter& player)
```

### CanHaveMoreFollowers

* * Check if a player can have any more followers in his global slots. * @param player Target player. * @param FollowerType Check if a follower with this type can join the party. * @remarks There's a maximum of 25 slots, in practice however, maximum is lower. 

```angelscript
bool CanHaveMoreFollowers(Critter& player, uint FollowerType)
```

### GetFollowersOwner

* * * @remarks If critter is not a follower, a null handle will be returned. 

```angelscript
Critter@ GetFollowersOwner(Critter& critter)
```

### RightDistance

* * Check if the follower is close enough to a specific owner. * @remarks Used in GetFollowerByBaseType to make sure follower is close enough. 

```angelscript
bool RightDistance(Critter& follower, Critter& owner)
```

### HasFollowerOfBaseType

* * Check if a player has a follower of the specified basetype. * @remarks Uses GetFollowerByBaseType, so RightDistance needs to return true. 

```angelscript
bool HasFollowerOfBaseType(Critter& owner, uint basetype)
```

### GetFollowerByBaseType

```angelscript
Critter@ GetFollowerByBaseType(Critter& owner, uint basetype)
```

### RemoveFollowerByBaseType

```angelscript
bool RemoveFollowerByBaseType(Critter& owner, uint basetype)
```

### GetNumberOfFollowingFollowersOfPlayer

* * Retrieve the number of followers that a player has in active following mode (automatic or manual) on the same map as him/her. 

```angelscript
int GetNumberOfFollowingFollowersOfPlayer(Critter& player)
```

### GetNumberOfFollowersOfPlayer

* * Returns how many followers of any type a player has. * This only includes how many the player has, regardless of where they are, as long as their corpses have not decayed. 

```angelscript
int GetNumberOfFollowersOfPlayer(Critter& player)
```

### GetSlaveTypes

```angelscript
uint GetSlaveTypes(Critter& player)
```

### ClearFollowersEnemy

```angelscript
void ClearFollowersEnemy(Critter& player, Critter& target)
```

### AddFollowersEnemy

```angelscript
void AddFollowersEnemy(Critter& player, Critter& target)
```

### NumberOfFollowersOnMap

* * Returns the number of followers, regardless of owner on the map 

```angelscript
uint NumberOfFollowersOnMap(Map@ map)
```

### GetFollowerType

```angelscript
uint GetFollowerType(Critter& critter)
```

### DisbandFollower

 * * Critter is no longer follower a follower. * Removes the follower from a follower slot and assigns a neutral dialog. * @return If successfully disbanded, true, otherwise false. 

```angelscript
bool DisbandFollower(Critter& player, Critter& cr, bool reset)
```

### AddToFollowerlist

* * Assign follower's id to the list of followers. 

```angelscript
bool AddToFollowerlist(Critter& master, Critter& follower)
```

### MakeFollower

* * Makes the critter a follower to the specified owner. 

```angelscript
bool MakeFollower(Critter& critter, uint type, string& script, uint dialogid, Critter& owner, bool FreeBarter)
```

### LocateFollowerByType

Locate critter based on IMerc handle and return critter handle

```angelscript
Critter@ LocateFollowerByType(IMerc@ merc, Critter& owner)
```

### LocateFollowerByID

* * Locate critter based on merc id and return critter handle 

```angelscript
Critter@ LocateFollowerByID(uint id, Critter& owner)
```

### GetFollowers

```angelscript
int GetFollowers(Critter& player, Map@ map, array<Critter@>& followers)
```

### GetFollowers

```angelscript
int GetFollowers(Critter& player, Map@ map, array<Critter@>& followers, bool OnlyIsSeen)
```

### GetFollowers

* * Retrieves followers belonging to player. * @param	all		    if true, then all followers are put in table, if false then only the active ones. * @param    followers   Array to hold the retrieved followers. * @return   Number of followers found. 

```angelscript
int GetFollowers(Critter& player, bool all, array<Critter@>& followers)
```

### CountFollowers

* * Counts the followers, either all or 'active' (following) ones. 

```angelscript
uint CountFollowers(Critter& player, bool all)
```

### CountFollowers

* * Counts the followers on a specific map. * * @return   Number of followers on the specific map belonging to player 

```angelscript
uint CountFollowers(Critter& player, Map@ map)
```


