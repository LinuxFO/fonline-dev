---
title: mapdata_h.fos
description: " FOnline: 2238 Rotators  mapdata_h.fos ..."
---

# mapdata_h.fos


FOnline: 2238
Rotators

mapdata_h.fos


## Included By

- [bank_vault.fos](bank_vault.fos.md)
- [billboards.fos](billboards.fos.md)
- [cave.fos](cave.fos.md)
- [cheats.fos](cheats.fos.md)
- [combat.fos](combat.fos.md)
- [dialog.fos](dialog.fos.md)
- [economy_banker.fos](economy_banker.fos.md)
- [explode.fos](explode.fos.md)
- [faction_data.fos](faction_data.fos.md)
- [factions_bases.fos](factions_bases.fos.md)
- [factions_player.fos](factions_player.fos.md)
- [factions_terminal.fos](factions_terminal.fos.md)
- [follower.fos](follower.fos.md)
- [generic_guard.fos](generic_guard.fos.md)
- [guard.fos](guard.fos.md)
- [main.fos](main.fos.md)
- [main_planes.fos](main_planes.fos.md)
- [map_bos_lh.fos](map_bos_lh.fos.md)
- [map_broken.fos](map_broken.fos.md)
- [map_denbus.fos](map_denbus.fos.md)
- [map_encounter.fos](map_encounter.fos.md)
- [map_gecko.fos](map_gecko.fos.md)
- [map_hub.fos](map_hub.fos.md)
- [map_klamath.fos](map_klamath.fos.md)
- [map_modoc.fos](map_modoc.fos.md)
- [map_ncr_downtown.fos](map_ncr_downtown.fos.md)
- [map_playerfaction_hq.fos](map_playerfaction_hq.fos.md)
- [map_random_cave.fos](map_random_cave.fos.md)
- [map_redding.fos](map_redding.fos.md)
- [map_redding_bank_vault.fos](map_redding_bank_vault.fos.md)
- [map_redding_lost.fos](map_redding_lost.fos.md)
- [map_tent.fos](map_tent.fos.md)
- [mine.fos](mine.fos.md)
- [mob_wave.fos](mob_wave.fos.md)
- [prod_scavenge.fos](prod_scavenge.fos.md)
- [prod_veins.fos](prod_veins.fos.md)
- [prospects.fos](prospects.fos.md)
- [quest_bos_initiate.fos](quest_bos_initiate.fos.md)
- [quest_caesar_train.fos](quest_caesar_train.fos.md)
- [quest_first_tent.fos](quest_first_tent.fos.md)
- [quest_hub_sad_farmer.fos](quest_hub_sad_farmer.fos.md)
- [quest_killmobs_h.fos](quest_killmobs_h.fos.md)
- [quest_la_gunr_caravan.fos](quest_la_gunr_caravan.fos.md)
- [quest_la_warehouse.fos](quest_la_warehouse.fos.md)
- [recycler.fos](recycler.fos.md)
- [reinforcements.fos](reinforcements.fos.md)
- [replication.fos](replication.fos.md)
- [rq_cave.fos](rq_cave.fos.md)
- [slaverun_h.fos](slaverun_h.fos.md)
- [town.fos](town.fos.md)
- [unsafe_client.fos](unsafe_client.fos.md)
- [utils.fos](utils.fos.md)
- [worldmap.fos](worldmap.fos.md)

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __MAPDATA_H__ |  |  |
| MAP_DATA_FACTION | `(0)` | globals |
| MAP_DATA_CREATED_ON | `(1)` |  |
| MAP_DATA_BANK | `(2)` |  |
| MAP_DATA_TOWN | `(3)` |  |
| MAP_DATA_OWNER | `(5)` |  |
| MAP_DATA_LAST_ENTERED | `(6)` |  |
| MAP_DATA_ALERT_INDEX | `(7)` |  |
| MAP_DATA_ACTIVE_COUNTDOWN | `(8)` |  |
| MAP_DATA_SPAWNER | `(9)` |  |
| MAP_DATA_MAP_MODES | `(10)` |  |
| MAP_DATA_LOCATION_WEALTH | `(11)` |  |
| MAP_DATA_MOB_WAVE | `(12)` |  |
| _MapHasMode | `# (map, mode)((map.GetData(MAP_DATA_MAP_MODES) & (mode)) != 0)` |  |
| _MapSetMode | `# (map, mode)map.SetData(MAP_DATA_MAP_MODES, map.GetData(MAP_DATA_MAP_MODES) | (mode))` |  |
| _MapUnsetMode | `# (map, mode)map.SetData(MAP_DATA_MAP_MODES, map.GetData(MAP_DATA_MAP_MODES) & (~(mode)))` |  |
| MAP_MODE_EVENT | `(0x00000001)` |  |
| MAP_MODE_SPECTATE_FREELY | `(0x00000002)` |  |
| MAP_MODE_SPECTATE_ENTER | `(0x00000004)` |  |
| MAP_MODE_REPLICATION | `(0x00000008)` |  |
| MAP_MODE_TBRT_ITEMS | `(0x00000010)` |  |
| MAP_MODE_NO_PVP | `(0x00000020)` |  |
| MAP_MODE_NO_DISMANTLING | `(0x00000040)` |  |
| MAP_MODE_NO_GRIDS | `(0x00000080)` |  |
| MAP_MODE_ACTIVE_TC | `(0x00000100)` |  |
| MAP_MODE_LOOT_DROP | `(0x00000200)` |  |
| MAP_DATA_TENT_OWNER | `(20)` | tent |
| MAP_DATA_CAVE_INIT | `(20)` | caves |
| MAP_DATA_CAVE_RQ_PID | `(21)` |  |
| MAP_DATA_CAVE_RQ_PLAYER | `(22)` |  |
| MAP_DATA_SLAVERUN_INIT | `(20)` | slaveruns |
| MAP_DATA_SLAVERUN_PLAYER | `(21)` |  |
| MAP_DATA_SLAVERUN_COMBAT | `(22)` |  |
| MAP_DATA_SKUMPITT | `(20)` | skum pitt state |
| MAP_DATA_LEADER | `(20)` | redding guttersnipes leader chosen |
| MAP_DATA_SITE_BASETYPE | `(20)` | base building site |
| MAP_DATA_DELETE_ENCOUNTER | `(20)` | encounters |
| MAP_DATA_WELL | `(20)` | ============================================== QUEST LOCATIONS ============================================== raiders farmhome quest |
| MAP_DATA_PEN | `(21)` |  |
| MAP_DATA_SHED | `(22)` |  |
| MAP_DATA_KILL | `(23)` |  |
| MAP_DATA_FREE | `(24)` |  |
| MAP_DATA_FOOD | `(25)` |  |
| MAP_DATA_GUY | `(26)` |  |
| MAP_DATA_GUYTALKED | `(27)` |  |
| MAP_DATA_RAILGANG_OWNER | `(20)` | railgang quest |
| MAP_DATA_RAILGANG_THUGS | `(21)` |  |
| MAP_DATA_RAILRAIDER_OWNER | `(20)` | rail raider encounter |
| MAP_DATA_RAILRAIDER_THUGS | `(21)` |  |
| MAP_DATA_WAREHOUSE_OWNER | `(20)` | la warehouse quest |
| MAP_DATA_WAREHOUSE_PUNKS | `(21)` |  |
| MAP_DATA_CATH_BASEMENT_OWNER | `(20)` | cathedral basement quest |
| MAP_DATA_CATH_BASEMENT_PLANTS | `(21)` |  |
| MAP_DATA_ANTLAIR_ANTS | `(21)` | ant lair quest #define MAP_DATA_ANTLAIR_OWNER		(20) |
| MAP_DATA_ANTLAIR_ALIVE | `(22)` |  |
| MAP_DATA_TRAIN_CAMP_OWNER | `(20)` | Caesars Legion train quest |
| MAP_DATA_VALVES | `(20)` | tanker quest |
| MAP_DATA_HANDYS | `(21)` |  |
| MAP_DATA_STRANDEDTANKER_OWNER | `(22)` |  |
| MAP_DATA_FORCEFIELD | `(20)` | bos bunker quest |
| MAP_DATA_ROPE | `(21)` |  |
| MAP_DATA_GUNRUNNER_CARAVAN_OWNER | `(20)` | Gun Runners Caravan quest |
| MAP_DATA_FRISCO_SUBWAY_OWNER | `(20)` | Frisco Replication map quest |
| MAP_DATA_FRISCO_SUBWAY_SCORPIONS | `(21)` |  |
| MAP_DATA_NCR_BRAHMIN_WILLOW_OWNER | `(20)` | NCR Westin Ranch Quest 1 |
| MAP_DATA_NCR_BRAHMIN_WILLOW_CHILDREN | `(21)` |  |
| MAP_DATA_JT_SNEAKEATER_OWNER | `(20)` | Junktown Scorpion Quest - Sneakeater Perk |
| MAP_DATA_Q_MB_OWNER | `(20)` | Ruined Military Base Quest |
| MAP_DATA_Q_MB_ENC_SPAWNED | `(21)` |  |
| MAP_DATA_SELLER | `(20)` | prospects - yes, I know they will probably never get in |
| MAP_DATA_OUTPOST_INDEX | `(20)` | domination, this is in 'local' category because outposts maps are unique |
| MAP_DATA_ELEVATOR_TIME | `(20)` | glow, time for elevator work |
| MAP_LAST_DOOR_GROUP | `(22)` | talchem |
| MAP_DATA_SHA_ENIN_OWNER | `(20)` | sha-enin encounter |
| MAP_DATA_SHA_ENIN_BANDITS_COUNT | `(21)` |  |

