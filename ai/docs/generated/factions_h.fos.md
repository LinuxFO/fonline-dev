---
title: factions_h.fos
description: " FOnline: 2238 Rotators  factions_h.fos ..."
---

# factions_h.fos


FOnline: 2238
Rotators

factions_h.fos


## Includes

- `_macros.fos`
- `groups_h.fos`
- `utils_h.fos`

## Included By

- [all_farmer.fos](all_farmer.fos.md)
- [cheats.fos](cheats.fos.md)
- [den_metzger_guard.fos](den_metzger_guard.fos.md)
- [dialog.fos](dialog.fos.md)
- [dialog_factions.fos](dialog_factions.fos.md)
- [faction_data.fos](faction_data.fos.md)
- [factions.fos](factions.fos.md)
- [factions_bases.fos](factions_bases.fos.md)
- [factions_bases_h.fos](factions_bases_h.fos.md)
- [factions_generic.fos](factions_generic.fos.md)
- [factions_generic_bartender.fos](factions_generic_bartender.fos.md)
- [factions_news.fos](factions_news.fos.md)
- [factions_player.fos](factions_player.fos.md)
- [factions_recognition.fos](factions_recognition.fos.md)
- [factions_terminal.fos](factions_terminal.fos.md)
- [follower.fos](follower.fos.md)
- [hub_guard.fos](hub_guard.fos.md)
- [item_dogtags.fos](item_dogtags.fos.md)
- [la_ady_guard.fos](la_ady_guard.fos.md)
- [main.fos](main.fos.md)
- [map_bos_lh.fos](map_bos_lh.fos.md)
- [map_hub.fos](map_hub.fos.md)
- [map_playerfaction_hq.fos](map_playerfaction_hq.fos.md)
- [map_redding_lost.fos](map_redding_lost.fos.md)
- [ncr_guard.fos](ncr_guard.fos.md)
- [noob_camp_guard.fos](noob_camp_guard.fos.md)
- [prospect_guard.fos](prospect_guard.fos.md)
- [reputations_modifiers.fos](reputations_modifiers.fos.md)
- [town.fos](town.fos.md)
- [town_militia.fos](town_militia.fos.md)
- [unsafe_client.fos](unsafe_client.fos.md)
- [workbench.fos](workbench.fos.md)

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __FACTIONS__ |  |  |
| FACTION_COUNT | `(4096)` | checks if number represents valid faction |
| FACTION_VALID | `# (f)    (f < (FACTION_COUNT))` |  |
| RANK_UNKNOWN | `(0)` |  |
| RANK_ROOKIE | `(1)` |  |
| RANK_ACCEPTED | `(2)` |  |
| RANK_TRUSTED | `(3)` |  |
| RANK_IMPORTANT | `(4)` |  |
| RANK_LEADER | `(5)` |  |
| FIRST_RANK | `# (f)             (1)` |  |
| RANK_VALID | `# (r)             (r <= 5)` |  |
| RANK_BOS_INITIATE | `(1)` | BOS |
| RANK_BOS_APPRENTICE | `(2)` |  |
| RANK_BOS_SENIOR | `(3)` |  |
| RANK_BOS_ELDER | `(4)` |  |
| RANK_ENCLAVE_BOOT | `(1)` | ENCLAVE |
| RANK_ENCLAVE_TROOPER | `(2)` |  |
| RANK_ENCLAVE_SERGEANT | `(3)` |  |
| RANK_ENCLAVE_OFFICER | `(4)` |  |
| RANK_UNITY_INITIATE | `(1)` | UNITY |
| RANK_UNITY_CHILD | `(2)` |  |
| RANK_UNITY_PRIEST | `(3)` |  |
| RANK_UNITY_ELDER | `(4)` |  |
| RANK_NCR_DEMOCRAT | `(1)` | NCR |
| RANK_NCR_CITIZEN | `(2)` |  |
| RANK_NCR_MAGISTRATE | `(3)` |  |
| RANK_NCR_MARSHAL | `(4)` |  |
| RANK_VC_ADMITTED | `(1)` | VAULTCITY |
| RANK_VC_CITIZEN | `(2)` |  |
| RANK_VC_REGULATOR | `(3)` |  |
| RANK_VC_PROCONSUL | `(4)` |  |
| STATUS_UNKNOWN | `(0)` | Status |
| STATUS_FRIEND | `(1)` |  |
| STATUS_NEUTRAL | `(2)` |  |
| STATUS_ENEMY | `(3)` |  |
| STATUS_INVITED | `(4)` |  |
| STATUS_VALID | `# (s)    (s <= 4)` | checks if number represents valid status |
| FIRST_FACTION | `(2)` | util defines, need to be updated after certain changes in previous defines |
| FACTION_PLAYER_START | `(200)` |  |
| REP_VALID | `# (r)             (-100 <= r && r <= 100)` |  |
| NEWS_JOINED | `(1)` | player x joined faction |
| NEWS_RESIGNED | `(2)` | player x resigned faction |
| NEWS_EXPELLED | `(3)` | player x was expelled by player y |
| NEWS_PROMOTED | `(4)` | player x was promoted/demoted by player y |
| NEWS_DEMOTED | `(7)` | #define NEWS_PROMOTED23             (5) #define NEWS_PROMOTED34             (6) |
| NEWS_CLAIMED | `(9)` | #define NEWS_DEMOTED43              (8) player x claimed leadership |
| NEWS_LEADER | `(10)` | player x became leader |
| NEWS_OVERTHROWN | `(11)` | player x cease to be leader |
| FD_RESULT_SUCCESS | `(0)` |  |
| FD_RESULT_ALREADY_EXISTS | `(1)` |  |
| FD_RESULT_NOT_FOUND | `(2)` |  |
| FD_RESULT_ANY_DATA_ERROR | `(3)` |  |
| FD_RESULT_INVALID_ARGUMENT | `(4)` |  |
| FD_RESULT_LVAR_ERROR | `(5)` |  |
| FD_RESULT_DB_NOT_FOUND | `(6)` |  |
| FD_RESULT_DB_FULL | `(7)` |  |
| FD_RESULT_DB_EMPTY | `(8)` |  |
| REGRESULT_SUCCESS | `(0)` | Register funcation errorcodes |
| REGRESULT_ALREADY_TAKEN | `(1)` | already registered |
| REGRESULT_WRONG_NAME | `(2)` | name not found |
| REGRESULT_MAXLIMIT | `(3)` | limit of number of factions reached |
| REGRESULT_EXCEPTION | `(4)` | lack of gvar, or anydata error |

