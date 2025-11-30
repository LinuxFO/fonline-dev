---
title: dialog.fos
---

# dialog.fos

## Includes

- `_macros.fos`
- `economy_h.fos`
- `factions_h.fos`
- `follower_common_h.fos`
- `lexems_h.fos`
- `mapdata_h.fos`
- `messages_h.fos`
- `npc_common_h.fos`
- `npc_roles_h.fos`
- `world_common_h.fos`
- `dialog_factions.fos`
- `dialog_reputations.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __DIALOG__ |  |  |
| HEALING_PRICE | `\` |  |
| _Tatoo_Corsican | `"Corsican Brothers"` |  |

## Functions

### d_IsLocationOwner

* * Check if the player is the owner of the currently occupied location 

```angelscript
bool d_IsLocationOwner(Critter& player, Critter@ npc)
```

### d_IsNotLocationOwner

* * Check if the player is not the owner of the currently occupied location 

```angelscript
bool d_IsNotLocationOwner(Critter& player, Critter@ npc)
```

### d_IsBusy

* * Check if a player is already talking to the NPC. 

```angelscript
bool d_IsBusy(Critter& player, Critter@ npc)
```

### r_AddExperience

* * Add some experience to the player. * This is the prefered method to add experience, instead of doing it manually in dialog editor. * @param val Amount of experience to add 

```angelscript
void r_AddExperience(Critter& player, Critter@ npc, int val)
```

### r_AddMoney

* * Add some caps to the player. * This is the prefered method to add caps, instead of doing it manually in dialog editor. * @param val Amount of money to add 

```angelscript
void r_AddMoney(Critter& player, Critter@ npc, int val)
```

### r_FlushScreen

* * Flush the screen black and back. 

```angelscript
void r_FlushScreen(Critter& cr, Critter@ tray)
```

### r_RemoveMoney

* * Remove some caps from the player. * This is the prefered method to remove caps, instead of doing it manually in dialog editor. * @param val Amount of money to subtract 

```angelscript
void r_RemoveMoney(Critter& player, Critter@ npc, int val)
```

### d_IsMoneyAvailable

* * Check if the amount of money is available in all banks combined. * @param val The given amount. 

```angelscript
bool d_IsMoneyAvailable(Critter& player, Critter@ npc, int val)
```

### d_IsWearingArmor

```angelscript
bool d_IsWearingArmor(Critter& player, Critter@ npc)
```

### d_IsWearingScaryHelmet

```angelscript
bool d_IsWearingScaryHelmet(Critter& player, Critter@ npc)
```

### r_RemoveWeapon

* * Remove the items the player has in Slot1 and 2. 1 drops to ground, 2 goes to inv. 

```angelscript
void r_RemoveWeapon(Critter& player, Critter@ tray)
```

### r_RemoveArmor

* * Drops armor to ground. 

```angelscript
void r_RemoveArmor(Critter& player, Critter@ tray)
```

### r_Alert

* * Send messages to everyone that sees the player, ordering them to attack. 

```angelscript
void r_Alert(Critter& player, Critter@npc)
```

### r_TeleportToMap

* * Teleport player to a map. * @param mappid PID of map to teleport to * @param entid Entire id on map, 0 is default entry point. 

```angelscript
void r_TeleportToMap(Critter& player, Critter@npc, int mappid, int entid)
```

### r_TeleportToMapFollowers

```angelscript
void r_TeleportToMapFollowers(Critter& player, Critter@npc, int mappid, int entid)
```

### r_ClearInventory

* * Delete all items in player's inventory 

```angelscript
void r_ClearInventory(Critter& player, Critter@npc)
```

### r_RunAway

```angelscript
void r_RunAway(Critter& player, Critter@ npc)
```

### r_RunAway

```angelscript
void r_RunAway(Critter& player, Critter@ npc, int distance)
```

### r_RunAway

```angelscript
void r_RunAway(Critter& player, Critter@ npc, int minDistance, int maxDistance)
```

### d_CheckNight

* * Check if it's night in the world. Night is defined as 22:00-06:59. 

```angelscript
bool d_CheckNight(Critter& player, Critter@ npc)
```

### d_CheckDay

* * Check if it's day in the world. Day is defined as 07:00-21:59. 

```angelscript
bool d_CheckDay(Critter& player, Critter@ npc)
```

### d_CheckMorning

* * Check if it's morning in the world. Morning is defined as 07:00-11:59. 

```angelscript
bool d_CheckMorning(Critter& player, Critter@ npc)
```

### d_CheckAfternoon

* * Check if it's afternoon in the world. Afternoon is defined as 12:00-17:59. 

```angelscript
bool d_CheckAfternoon(Critter& player, Critter@ npc)
```

### d_CheckEvening

* * Check if it's evening in the world. Evening is defined as 18:00-21:59. 

```angelscript
bool d_CheckEvening(Critter& player, Critter@ npc)
```

### d_IsLocationVisible

* * Check if a player can see a location. * @param locationId Unique id of the location. 

```angelscript
bool d_IsLocationVisible(Critter& player, Critter@ npc, int locationId)
```

### d_IsLocationNotVisible

* * Check if a player can not see a location. * @param locationId Unique id of the location. 

```angelscript
bool d_IsLocationNotVisible(Critter& player, Critter@ npc, int locationId)
```

### r_ShowLocation

* * Show location to the player. * @param locationId Unique id of the location. 

```angelscript
void r_ShowLocation(Critter& player, Critter@ npc, int locationId)
```

### r_RetireLocation

* * Mark the current location as autogarbage-ready. 

```angelscript
void r_RetireLocation(Critter& player, Critter@ npc)
```

### d_HpVeryLow

* * Check if player's current HP is under 25% of his maximum HP. 

```angelscript
bool d_HpVeryLow(Critter& player, Critter@ npc)
```

### d_HpLow

* * Check if player's current HP is under 50% of his maximum HP. 

```angelscript
bool d_HpLow(Critter& player, Critter@ npc)
```

### d_HpAverage

* * Check if player's current HP is under 75% of his maximum HP. 

```angelscript
bool d_HpAverage(Critter& player, Critter@ npc)
```

### d_HpHigh

* * Check if player's current HP is under 100% of his maximum HP. 

```angelscript
bool d_HpHigh(Critter& player, Critter@ npc)
```

### d_NPCHpVeryLow

* * Check if NPC's current HP is under 25% of his maximum HP. 

```angelscript
bool d_NPCHpVeryLow(Critter& player, Critter@ npc)
```

### d_NPCHpLow

* * Check if NPC's current HP is under 50% of his maximum HP. 

```angelscript
bool d_NPCHpLow(Critter& player, Critter@ npc)
```

### d_NPCHpAverage

* * Check if NPC's current HP is under 75% of his maximum HP. 

```angelscript
bool d_NPCHpAverage(Critter& player, Critter@ npc)
```

### d_NPCHpHigh

* * Check if NPC's current HP is under 100% of his maximum HP. 

```angelscript
bool d_NPCHpHigh(Critter& player, Critter@ npc)
```

### d_HealingMoney

* * Check if player has enough caps for healing. 

```angelscript
bool d_HealingMoney(Critter& player, Critter@ npc)
```

### d_IsToHeal

* * Check if player can be healed. 

```angelscript
bool d_IsToHeal(Critter& player, Critter@ npc)
```

### r_DocHeal

* * Removes poision, radiation, heals limbs and returns HP to max. 

```angelscript
void r_DocHeal(Critter& player, Critter@ npc)
```

### dlg_ShowHealingPrice

* * Show how much healing costs. @lex price@ is used. 

```angelscript
void dlg_ShowHealingPrice(Critter& player, Critter@ npc, string@ text)
```

### d_IsAddict

* * Check if a player is addicted to anything. * This includes: Nuka Cola, Buffout, Mentats, Psycho, Radaway, Jet or Tragic (the card game). 

```angelscript
bool d_IsAddict(Critter& player, Critter@ npc)
```

### d_IsNotAddict

* * Checks if player is not addicted to anything. * @see d_IsAddict 

```angelscript
bool d_IsNotAddict(Critter& player, Critter@ npc)
```

### d_WeaponInHand

* * Checks if player have any weapon in active slot 

```angelscript
bool d_WeaponInHand(Critter& player, Critter@ npc)
```

### d_NoWeaponInHand

* * Checks if player DOESNT have any weapon in active slot 

```angelscript
bool d_NoWeaponInHand(Critter& player, Critter@ npc)
```

### d_ItemInHand

* * Checks if player have specified item in active slot 

```angelscript
bool d_ItemInHand(Critter& player, Critter@ npc, int pid)
```

### r_ToHeal

* * Heal HP to players' maximum. 

```angelscript
void r_ToHeal(Critter& player, Critter@ npc)
```

### r_ToDead

* * Kill the player with a given animation * @param val Animation number 

```angelscript
void r_ToDead(Critter& player, Critter@ npc, int val)
```

### r_KillNpc

* * Kills the NPC, player is the killer. * @param val Death animation number 

```angelscript
void r_KillNpc(Critter& player, Critter@ npc, int val)
```

### r_NinjaKillNpc

* * Kills the NPC, no one is the killer. * @param val Death animation number 

```angelscript
void r_NinjaKillNpc(Critter& player, Critter@ npc, int val)
```

### d_NpcOnMap

* * Checks whether npc is on a map with given protoid 

```angelscript
bool d_NpcOnMap(Critter& player, Critter@ npc, int mappid)
```

### d_NpcInLocation

* * Checks whether npc is in location with given protoid. 

```angelscript
bool d_NpcInLocation(Critter& player, Critter@ npc, int locpid)
```

### r_Irradiate

////////// RADIATION ////////// * * Irradiate or de-radiate the player. * @param val Amount of radiation to receive (negative value will result in radiation decrease) 

```angelscript
void r_Irradiate(Critter& player, Critter@ npc, int val)
```

### r_JumpToRandomNode

* * Jump to a node between min and max nodes. * @param min Minimum node. * @param max Maximum node. * @param multiplier Multiplier. If multiplier is 10 and minimum node is 1 and maximum node is 5, then 10,20,30,40,50 are nodes that can be randomized 

```angelscript
uint r_JumpToRandomNode(Critter& player, Critter@ npc, int min, int max, int multiplier)
```

### r_JumpToRandomNode

* * Jump to a node between min and max nodes. * @param min Minimum node. * @param max Maximum node. 

```angelscript
uint r_JumpToRandomNode(Critter& player, Critter@ npc, int min, int max)
```

### r_NodeChancePercent

```angelscript
uint r_NodeChancePercent(Critter& player, Critter@ npc, int chance, int node)
```

### r_NodeChancePercent

```angelscript
uint r_NodeChancePercent(Critter& player, Critter@ npc, int chance, int nodeOK, int nodeFAIL)
```

### d_Random

* * Make a random dice roll which is true only if 1==n * @param n As in the function description. * n is the input value you provide * Some example of chances when providing different values: * 1 - Always true. * 2 - Will be true in 50% of cases * 5 - Will be true in 20% of cases. 

```angelscript
bool d_Random(Critter& player, Critter@ npc, int n)
```

### d_RandomPercent

* * Make a random roll which has a certain % chance of being true. * @param chance A number between 0 and 100. 

```angelscript
bool d_RandomPercent(Critter& player, Critter@ npc, int chance)
```

### r_Roll

```angelscript
uint r_Roll(Critter& player, Critter@ npc, int from, int to, int need, int jump)
```

### r_SkillRoll

* * Does a roll for skill, then redirects the dialog in case of success * @param     skill           Skill to be checked * @param     successnode     Node to redirect to in case of success 

```angelscript
uint r_SkillRoll(Critter& player, Critter@ npc, int skill, int successnode)
```

### r_SkillRoll

* * Does a roll for skill with specified skill bonus, then redirects the dialog in case of success * @param     skill           Skill to be checked * @param     skillbonus      Bonus to the checked skill * @param     successnode     Node to redirect to in case of success 

```angelscript
uint r_SkillRoll(Critter& player, Critter@ npc, int skill, int bonus, int successnode)
```

### r_StatRoll

* * Does a roll for stat, then redirects the dialog in case of success * @param     stat            Stat to be checked * @param     successnode     Node to redirect to in case of success 

```angelscript
uint r_StatRoll(Critter& player, Critter@ npc, int stat, int successnode)
```

### r_StatRoll

* * Does  aroll for stat with specified stat bonus, then redirects the dialog in case of success * @param     stat            Stat to be checked * @param     statbonus       Bonus to the checked stat * @param     successnode     Node to redirect to in case of success 

```angelscript
uint r_StatRoll(Critter& player, Critter@ npc, int stat, int bonus, int successnode)
```

### r_ReceiveDayPass

* * Add Vault City daypass to player. 

```angelscript
void r_ReceiveDayPass(Critter& player, Critter@ npc)
```

### d_HasValidDayPass

* * Check if player has a valid Vault City daypass. 

```angelscript
bool d_HasValidDayPass(Critter& player, Critter@ npc)
```

### d_LillyCheckQuest

JUNK

```angelscript
bool d_LillyCheckQuest(Critter& player, Critter@ npc, int val)
```

### d_VCCheckLK

```angelscript
bool d_VCCheckLK(Critter& player, Critter@ npc, int val)
```

### r_TransferItemsToContainer

```angelscript
void r_TransferItemsToContainer(Critter& player, Critter@npc, int mappid, int entid, int contpid, int itemtypes)
```

### r_TransferItemsFromContainer

```angelscript
void r_TransferItemsFromContainer(Critter& player, Critter@npc, int mappid, int entid, int contpid)
```

### r_PlaySound

////////////// SOUNDS    // //////////////

```angelscript
void r_PlaySound(Critter& player, Critter@ npc, int val)
```

### r_PlaySoundDice

```angelscript
void r_PlaySoundDice(Critter& player, Critter@ npc, int val)
```

### r_PlaySoundGun

```angelscript
void r_PlaySoundGun(Critter& player, Critter@ npc, int val)
```

### r_GunRunnerInsult

////////////// MISC     // //////////////

```angelscript
void r_GunRunnerInsult(Critter& player, Critter@ npc)
```

### r_DogsQuestReward

```angelscript
void r_DogsQuestReward(Critter& player, Critter@ npc)
```

### ProcessRewardTable

```angelscript
void ProcessRewardTable( Critter& player, const uint[][][]& table )
```

### r_BulkOrderRewardLow

```angelscript
void r_BulkOrderRewardLow(Critter& player, Critter@ npc)
```

### r_BulkOrderRewardHub

```angelscript
void r_BulkOrderRewardHub(Critter& player, Critter@ npc)
```

### r_BulkOrderRewardJunk

```angelscript
void r_BulkOrderRewardJunk(Critter& player, Critter@ npc)
```

### r_BulkOrderRewardFoundry

```angelscript
void r_BulkOrderRewardFoundry(Critter& player, Critter@ npc)
```

### r_BulkOrderRewardInde

```angelscript
void r_BulkOrderRewardInde(Critter& player, Critter@ npc)
```

### r_BulkOrderRewardGuns

```angelscript
void r_BulkOrderRewardGuns(Critter& player, Critter@ npc)
```

### r_BulkOrderRewardPrints

```angelscript
void r_BulkOrderRewardPrints(Critter& player, Critter@ npc)
```

### r_BulkOrderRewardPuppet

```angelscript
void r_BulkOrderRewardPuppet(Critter& player, Critter@ npc)
```

### r_BulkOrderRewardPuppetArmor

```angelscript
void r_BulkOrderRewardPuppetArmor(Critter& player, Critter@ npc)
```

### r_BulkOrderRewardPuppetGuns

```angelscript
void r_BulkOrderRewardPuppetGuns(Critter& player, Critter@ npc)
```

### r_SpawnInRandomContainer

* * Places item in random container on map with given pid. * @param	mapPid		PID of map to spawn the item in (MAPS.TXT) - Val1. * @param	itemPid		PID of item to be spawned - Val2. * @remarks	Since it uses GetMapByPid with skipCount 0, it takes first map with given pid. 

```angelscript
void r_SpawnInRandomContainer(Critter& player, Critter@ npc, int mapPid, int itemPid)
```

### test_SpawnInRandomContainer

```angelscript
void test_SpawnInRandomContainer(Critter& cr, int p0, int p1, int p2)
```

### d_QuestTimeoutReady

* * Checks timeout for given npc, in order to check if some repeatable quest can be given again. * It works per npc-player, so you can't make it for each quest. But it's simplier that way. * @return true - quest can be given, false - need to wait 

```angelscript
bool d_QuestTimeoutReady(Critter& player, Critter@ npc)
```

### d_QuestTimeoutNotReady

* * Checks timeout for given npc, in order to check if some repeatable quest can NOT be given again. * It works per npc-player, so you can't make it for each quest. But it's simplier that way. * @return true - quest cannot be given, false - quest is available 

```angelscript
bool d_QuestTimeoutNotReady(Critter& player, Critter@ npc)
```

### r_QuestTimeout

* * Assignes timeout for given npc so he will remember that player made some quest for him lately. * @param timeout       Quest timeout in ingame hours 

```angelscript
void r_QuestTimeout(Critter& player, Critter@ npc, int timeout)
```

### d_CommonTimeoutReady

* * Checks timeout for given npc, in order to check if some repeatable quest can be given again. * It works per npc, so you can't make it for each quest. But it's simplier that way. * @return true - quest can be given, false - need to wait 

```angelscript
bool d_CommonTimeoutReady(Critter& player, Critter@ npc)
```

### d_CommonTimeoutNotReady

* * Checks timeout for given npc, in order to check if some repeatable quest can NOT be given again. * It works per npc, so you can't make it for each quest. But it's simplier that way. * @return true - quest cannot be given, false - quest is available 

```angelscript
bool d_CommonTimeoutNotReady(Critter& player, Critter@ npc)
```

### r_CommonTimeout

* * Assignes timeout for given npc so he will remember that player made some quest for him lately. * @param timeout       Quest timeout in ingame hours 

```angelscript
void r_CommonTimeout(Critter& player, Critter@ npc, int timeout)
```

### d_HasHolodisk

* * Checks if the player has holodisk containing specific information. * @param val   Number of holodisk information 

```angelscript
bool d_HasHolodisk(Critter& player, Critter@ npc, int val)
```

### d_HasHoloInfo

* * Checks if the player has specific holodisk information stored in pipboy. * @param val   Number of holodisk information 

```angelscript
bool d_HasHoloInfo(Critter& player, Critter@ npc, int val)
```

### r_GiveHolodisk

* * Gives the player a holodisk containing specific information. * @param val   Number of holodisk information 

```angelscript
void r_GiveHolodisk(Critter& player, Critter@ npc, int val)
```

### d_CheckProfession

//////////////// Professions  // //////////////// Check if player has still some profession point that he can acquire profession for

```angelscript
bool d_CheckProfession(Critter& player, Critter@ npc, int val)
```

### CheckProfession

todo: move to perks

```angelscript
bool CheckProfession(Critter& player, int prof, int currentLevel)
```

### d_CheckArmorer0

check Armorer

```angelscript
bool d_CheckArmorer0(Critter& player, Critter@ npc, int val)
```

### d_CheckArmorer1

```angelscript
bool d_CheckArmorer1(Critter& player, Critter@ npc, int val)
```

### d_CheckArmorer2

```angelscript
bool d_CheckArmorer2(Critter& player, Critter@ npc, int val)
```

### d_CheckGunsmithS0

check Gunsmith Small Guns

```angelscript
bool d_CheckGunsmithS0(Critter& player, Critter@ npc, int val)
```

### d_CheckGunsmithS1

```angelscript
bool d_CheckGunsmithS1(Critter& player, Critter@ npc, int val)
```

### d_CheckGunsmithS2

```angelscript
bool d_CheckGunsmithS2(Critter& player, Critter@ npc, int val)
```

### d_CheckGunsmithB0

check Gunsmith Big Guns

```angelscript
bool d_CheckGunsmithB0(Critter& player, Critter@ npc, int val)
```

### d_CheckGunsmithB1

```angelscript
bool d_CheckGunsmithB1(Critter& player, Critter@ npc, int val)
```

### d_CheckGunsmithB2

```angelscript
bool d_CheckGunsmithB2(Critter& player, Critter@ npc, int val)
```

### d_CheckEnergyExpert0

check Energy Expert

```angelscript
bool d_CheckEnergyExpert0(Critter& player, Critter@ npc, int val)
```

### d_CheckEnergyExpert1

```angelscript
bool d_CheckEnergyExpert1(Critter& player, Critter@ npc, int val)
```

### d_CheckEnergyExpert2

```angelscript
bool d_CheckEnergyExpert2(Critter& player, Critter@ npc, int val)
```

### d_CheckDemolitionExpert0

check Demolition Expert

```angelscript
bool d_CheckDemolitionExpert0(Critter& player, Critter@ npc, int val)
```

### d_CheckDemolitionExpert1

```angelscript
bool d_CheckDemolitionExpert1(Critter& player, Critter@ npc, int val)
```

### d_CheckDoctor0

check Doctor

```angelscript
bool d_CheckDoctor0(Critter& player, Critter@ npc, int val)
```

### d_CheckDoctor1

```angelscript
bool d_CheckDoctor1(Critter& player, Critter@ npc, int val)
```

### d_CheckDoctor2

```angelscript
bool d_CheckDoctor2(Critter& player, Critter@ npc, int val)
```

### dlg_ShrenRumour

```angelscript
void dlg_ShrenRumour(Critter& player, Critter@ npc, string@ text)
```

### d_ExploredWasteland

* * Checks if PC can see all locations needed to take the Explorer perk. 

```angelscript
bool d_ExploredWasteland(Critter& player, Critter@ npc)
```

### d_IsTatoo

/////////// Tatoos  // ///////////

```angelscript
bool d_IsTatoo(Critter& player, Critter@ npc)
```

### d_NoTatoo

```angelscript
bool d_NoTatoo(Critter& player, Critter@ npc)
```

### d_HaveCorsicanBrothersTatoo

```angelscript
bool d_HaveCorsicanBrothersTatoo(Critter& player, Critter@ npc)
```

### r_SetCorsicanBrothersTatoo

```angelscript
void r_SetCorsicanBrothersTatoo(Critter& player, Critter@ npc)
```

### dlg_EnterTatoo

```angelscript
uint dlg_EnterTatoo(Critter& player, Critter@ npc, string@ say)
```

### d_SetDialogImage

```angelscript
bool d_SetDialogImage(Critter& player, Critter@ npc, int x, int y, int imageId)
```

### d_IsHighestParamInRange

Returns true if a param in specific param range has the highest value. It can be used for example to test if a skill is the best combat skill.

```angelscript
bool d_IsHighestParamInRange(Critter& player, Critter@ npc, int param, int paramFrom, int paramTo)
```

### r_Outfitter

```angelscript
void r_Outfitter(Critter& player, Critter@npc, int outfitId)
```

### d_IsAdmin

```angelscript
bool d_IsAdmin( Critter& player, Critter@ )
```

### d_IsModer

```angelscript
bool d_IsModer( Critter& player, Critter@ )
```

### d_IsTester

```angelscript
bool d_IsTester( Critter& player, Critter@ )
```

### dlg_SayBuyJet

```angelscript
uint dlg_SayBuyJet(Critter& player, Critter@ npc, string@ text)
```

### dlg_SayBuyNuka

```angelscript
uint dlg_SayBuyNuka(Critter& player, Critter@ npc, string@ text)
```

### dlg_SayBuyBeer

```angelscript
uint dlg_SayBuyBeer(Critter& player, Critter@ npc, string@ text)
```

### dlg_SayBuyBooze

```angelscript
uint dlg_SayBuyBooze(Critter& player, Critter@ npc, string@ text)
```

### dlg_SayBuyCigarettes

```angelscript
uint dlg_SayBuyCigarettes(Critter& player, Critter@ npc, string@ text)
```

### dlg_SayBuyLighter

```angelscript
uint dlg_SayBuyLighter(Critter& player, Critter@ npc, string@ text)
```

### dlg_SayBuyMedGel

```angelscript
uint dlg_SayBuyMedGel(Critter& player, Critter@ npc, string@ text)
```

### dlg_SayBuyNeedles

```angelscript
uint dlg_SayBuyNeedles(Critter& player, Critter@ npc, string@ text)
```

### dlg_SayBuyJetCan

```angelscript
uint dlg_SayBuyJetCan(Critter& player, Critter@ npc, string@ text)
```

### r_CrateSpawn3

For water merchant job

```angelscript
void r_CrateSpawn3(Critter& player, Critter@ npc)
```

### r_CrateSpawn

```angelscript
void r_CrateSpawn(Critter& player, Critter@ npc)
```

### r_RemoveCrate

```angelscript
void r_RemoveCrate(Critter& player, Critter@ npc)
```

### dlg_WarFC

for war public system between followers and cathedral

```angelscript
void dlg_WarFC(Critter& player, Critter@ npc, string@ text)
```

### dlg_Kid

for the dark priest

```angelscript
void dlg_Kid(Critter& player, Critter@ npc, string@ text)
```

### d_IsAreaScouted

```angelscript
bool d_IsAreaScouted(Critter& player, Critter@ npc, int zoneSX, int zoneSY, int zoneEX, int zoneEY)
```

### dlg_TryEnchantItem

```angelscript
void dlg_TryEnchantItem(Critter& player, Critter@ npc, string@ text)
```

### r_GiveDeterioratedItem

```angelscript
void r_GiveDeterioratedItem(Critter& player, Critter@ npc, int pid, int det)
```

### r_PuppetHeal

Puppet Healing

```angelscript
void r_PuppetHeal(Critter& player, Critter@ npc)
```

### r_AddLootSetLevel1

MagicItemSpawner - Tier 1 - Easy use this to spawn low statted random chance items, gives 1 gun, helmet, armor, and ammo set, potentially with stats

```angelscript
void r_AddLootSetLevel1 (Critter& player, Critter@ npc)
```

### r_AddLootSetLevel2

MagicItemSpawner - Tier 2 - Medium

```angelscript
void r_AddLootSetLevel2 (Critter& player, Critter@ npc)
```

### r_AddLootSetLevel3

MagicItemSpawner - Tier 3 - Hard

```angelscript
void r_AddLootSetLevel3 (Critter& player, Critter@ npc)
```


