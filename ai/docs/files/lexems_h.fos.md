---
title: lexems_h.fos
description: " FOnline: 2238 Rotators  lexems_h.fos ..."
---

# lexems_h.fos


FOnline: 2238
Rotators

lexems_h.fos


## Included By

- [cheats.fos](cheats.fos.md)
- [client_combat.fos](client_combat.fos.md)
- [client_critter_onhead.fos](client_critter_onhead.fos.md)
- [client_fef.fos](client_fef.fos.md)
- [client_interface.fos](client_interface.fos.md)
- [client_messages.fos](client_messages.fos.md)
- [dialog.fos](dialog.fos.md)
- [event_utils.fos](event_utils.fos.md)
- [explode.fos](explode.fos.md)
- [faction_data.fos](faction_data.fos.md)
- [follower_common.fos](follower_common.fos.md)
- [item_dogtags.fos](item_dogtags.fos.md)
- [item_misc.fos](item_misc.fos.md)
- [lexems.fos](lexems.fos.md)
- [main.fos](main.fos.md)
- [map_tent.fos](map_tent.fos.md)
- [mercs_h.fos](mercs_h.fos.md)
- [name_colorizing.fos](name_colorizing.fos.md)
- [parameters.fos](parameters.fos.md)
- [utils.fos](utils.fos.md)

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __LEXEMS_H__ |  |  |
| LEXEM |  |  |
| LEXEM_CRITTER_DESCRIPTION | `LEXEM("~")` | overwrites player description overwrites npc description, "You see [name]. [+text if long description]" enforces using LEXEM_CRITTER_NAME or Critter::Name (in that order) for all look types |
| LEXEM_CRITTER_HEAD | `LEXEM("@")` | overwrites name over head, can be empty. player only |
| LEXEM_CRITTER_NAME | `LEXEM("N")` | overwrites name used in long/short description and combat messages |
| LEXEM_CRITTER_TATTOO | `LEXEM("T")` | tattoo text |
| LEXEM_CRITTER_FACTION | `LEXEM("F")` | faction name |
| LEXEM_ITEM_DESCRIPTION_OVERRIDE | `LEXEM("~")` | overwrites short description |
| LEXEM_ITEM_DESCRIPTION_ADD | `LEXEM("+")` | a |
| LEXEM_ITEM_DESCRIPTION_SHORT | `LEXEM("-")` |  |
| LEXEM_ITEM_CRAFTER | `LEXEM("c")` |  |
| LEXEM_KEY_DESCRIPTION | `LEXEM("k")` |  |
| LEXEM_DOGTAG_OWNER | `LEXEM("o")` | name of player/npc military   "[surname], [name]" custom player "[name]" npc    "[name] [nickWithSpace_or_nothing][surname]" |
| LEXEM_DOGTAG_INFO | `LEXEM("i")` | extra info military "[id]/[birth_month]/[birth_year]/[blood_type]" custom   "[birth_month]/[birth_year]/[blood_type]" |

