---
title: factions_player.fos
description: " FOnline: 2238 Rotators  factions_player.fos ..."
---

# factions_player.fos


FOnline: 2238
Rotators

factions_player.fos


## Includes

- `_macros.fos`
- `_maps.fos`
- `economy_h.fos`
- `factions_h.fos`
- `factions_player_h.fos`
- `mapdata_h.fos`
- `factions_bases_h.fos`
- `follower_h.fos`
- `follower_common_h.fos`
- `debug_h.fos`
- `_colors.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __FACTIONS_PLAYER__ |  |  |
| LOCATION_PID | `# (cr)              (cr.StatBase[ST_VAR1])` |  |
| COST | `# (cr)                                              (cr.StatBase[ST_VAR2])` |  |
| FORCE_DIALOG_BASE | `(4)` |  |
| FORCE_DIALOG_INVALID_NAME | `(5)` |  |
| FORCE_DIALOG_DONE | `(8)` |  |
| FORCE_DIALOG_ALREADY_EXISTS | `(9)` |  |
| FORCE_DIALOG_MAXLIMIT | `(10)` |  |
| FORCE_DIALOG_EXCEPTION | `(11)` |  |
| FORCE_DIALOG_NOMONEY | `(12)` |  |
| FORCE_DIALOG_WRONG_MAP | `(8)` |  |
| FORCE_DIALOG_BUILDER_EXCEPTION | `(7)` |  |

## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| EnteredNames | `dictionary` |  | buffer to keep the names given player chosen, entry erased when faction is created just before first-base creation |

## Functions

### ChooseLocation

```angelscript
uint ChooseLocation(Critter& player, Critter@ npc, int value)
```

### r_ChooseCave

```angelscript
uint r_ChooseCave(Critter& player, Critter@ npc)
```

### r_ChooseCave2

```angelscript
uint r_ChooseCave2(Critter& player, Critter@ npc)
```

### r_ChooseCamp

```angelscript
uint r_ChooseCamp(Critter& player, Critter@ npc)
```

### r_ChooseTents

```angelscript
uint r_ChooseTents(Critter& player, Critter@ npc)
```

### r_ChooseDepot

```angelscript
uint r_ChooseDepot(Critter& player, Critter@ npc)
```

### r_ChooseScrapheap

```angelscript
uint r_ChooseScrapheap(Critter& player, Critter@ npc)
```

### r_ChooseGasStation

```angelscript
uint r_ChooseGasStation(Critter& player, Critter@ npc)
```

### r_ChooseBunker

```angelscript
uint r_ChooseBunker(Critter& player, Critter@ npc)
```

### d_HasMoneyForCave

```angelscript
bool d_HasMoneyForCave(Critter& player, Critter@)
```

### d_HasMoneyForCave2

```angelscript
bool d_HasMoneyForCave2(Critter& player, Critter@)
```

### d_HasMoneyForTents

```angelscript
bool d_HasMoneyForTents(Critter& player, Critter@)
```

### d_HasMoneyForCamp

```angelscript
bool d_HasMoneyForCamp(Critter& player, Critter@)
```

### d_HasMoneyForDepot

```angelscript
bool d_HasMoneyForDepot(Critter& player, Critter@)
```

### d_HasMoneyForGasStation

```angelscript
bool d_HasMoneyForGasStation(Critter& player, Critter@)
```

### d_HasMoneyForScrapheap

```angelscript
bool d_HasMoneyForScrapheap(Critter& player, Critter@)
```

### d_HasMoneyForBunker

```angelscript
bool d_HasMoneyForBunker(Critter& player, Critter@)
```

### r_Blades

```angelscript
uint r_Blades(Critter& player, Critter@ npc, int value)
```

### RemoveMoneyForBase

```angelscript
void RemoveMoneyForBase(Critter& player)
```

### addmember

```angelscript
void addmember(Critter& cr, int id, int, int)
```

### registerfaction

```angelscript
void registerfaction(Critter& cr, int num, int, int)
```

### _Talk

* * We need to cleanup entered names when player ends talking with baseseller * and have not finished faction creation process 

```angelscript
bool _Talk(Critter& cr, Critter& talkCr, bool attach, uint talkCount)
```

### _BaseSeller

```angelscript
void _BaseSeller(Critter& cr, bool)
```

### dlg_EnterNameOfFaction

```angelscript
uint dlg_EnterNameOfFaction(Critter& player, Critter@ npc, string@ say)
```

### CreateFaction

```angelscript
uint CreateFaction(Critter& player)
```

### dlg_CreateFactionBase

```angelscript
uint dlg_CreateFactionBase(Critter& player, Critter@ npc, string@ say)
```

### d_HasRequiredFollowers

```angelscript
bool d_HasRequiredFollowers(Critter& player, Critter@ npc, int num)
```

### d_HasNotRequiredFollowers

```angelscript
bool d_HasNotRequiredFollowers(Critter& player, Critter@ npc, int num)
```

### FindBaseEncounter

 Checks if player is in faction base area, and produces encounter when requirements are met 

```angelscript
bool FindBaseEncounter(array<Critter@>& group, Item@ car, uint x, uint y, uint& encounterDescriptor, bool& waitForAnswer)
```

### s_ProgressInfo

* * Shows the info with amounts of resources that are gathered on the map * and the required amounts 

```angelscript
bool s_ProgressInfo(Critter& player, Scenery&, int skill, Item@)
```

### CalcRequirements

```angelscript
bool CalcRequirements(Map& map, array<int>& info)
```

### CreateBuilder

```angelscript
void CreateBuilder(Critter& player, int base)
```

### r_SiteDepot

```angelscript
uint r_SiteDepot(Critter& player, Critter@, int cost)
```

### r_SiteScrapheap

```angelscript
uint r_SiteScrapheap(Critter& player, Critter@, int cost)
```

### r_SiteCamp

```angelscript
uint r_SiteCamp(Critter& player, Critter@, int cost)
```

### r_SiteOutpost

```angelscript
uint r_SiteOutpost(Critter& player, Critter@, int cost)
```

### r_SiteTraderMansion

```angelscript
uint r_SiteTraderMansion(Critter& player, Critter@, int cost)
```

### r_CreateSite

```angelscript
uint r_CreateSite(Critter& player, Critter@ builder)
```

### d_OnSite

```angelscript
bool d_OnSite(Critter& player, Critter@)
```

### d_CanTalkWithBuilder

```angelscript
bool d_CanTalkWithBuilder(Critter& player, Critter@)
```

### d_ConstructionReady

```angelscript
bool d_ConstructionReady(Critter& player, Critter@)
```

### dlg_FinishConstruction

```angelscript
uint dlg_FinishConstruction(Critter& player, Critter@ builder, string@ say)
```

### foreworker_dialog

```angelscript
void foreworker_dialog(Critter& player, int, int, int)
```


