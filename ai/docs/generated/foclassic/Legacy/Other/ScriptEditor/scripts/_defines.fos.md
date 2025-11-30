---
title: _defines.fos
---

# _defines.fos

## Includes

- `.\scripts\ITEMPID.H`

## Included By

- [_colors.fos](../../../../../PReloaded/Server/scripts/_colors.fos.md)
- [_macros.fos](../../../../../PReloaded/Server/scripts/_macros.fos.md)
- [buffer_lazy.fos](../../../../../PReloaded/Server/scripts/buffer_lazy.fos.md)
- [buffer_lazy_h.fos](../../../../../PReloaded/Server/scripts/buffer_lazy_h.fos.md)
- [smart_cursor.fos](../../../../../PReloaded/Server/scripts/client/smart_cursor.fos.md)
- [client_access.fos](../../../../../PReloaded/Server/scripts/client_access.fos.md)
- [client_critter_onhead.fos](../../../../../PReloaded/Server/scripts/client_critter_onhead.fos.md)
- [client_fef.fos](../../../../../PReloaded/Server/scripts/client_fef.fos.md)
- [client_interface.fos](../../../../../PReloaded/Server/scripts/client_interface.fos.md)
- [client_mapper_animation.fos](../../../../../PReloaded/Server/scripts/client_mapper_animation.fos.md)
- [client_messages.fos](../../../../../PReloaded/Server/scripts/client_messages.fos.md)
- [client_screen_gameinfo_h.fos](../../../../../PReloaded/Server/scripts/client_screen_gameinfo_h.fos.md)
- [client_timeouts.fos](../../../../../PReloaded/Server/scripts/client_timeouts.fos.md)
- [config.fos](../../../../../PReloaded/Server/scripts/config.fos.md)
- [critter_description.fos](../../../../../PReloaded/Server/scripts/critter_description.fos.md)
- [critter_item_movement.fos](../../../../../PReloaded/Server/scripts/critter_item_movement.fos.md)
- [critter_skin.fos](../../../../../PReloaded/Server/scripts/critter_skin.fos.md)
- [devconnect.fos](../../../../../PReloaded/Server/scripts/devconnect.fos.md)
- [entire.fos](../../../../../PReloaded/Server/scripts/entire.fos.md)
- [gmtools_h.fos](../../../../../PReloaded/Server/scripts/gmtools_h.fos.md)
- [item_achievementbook.fos](../../../../../PReloaded/Server/scripts/item_achievementbook.fos.md)
- [item_attributes.fos](../../../../../PReloaded/Server/scripts/item_attributes.fos.md)
- [item_bonus.fos](../../../../../PReloaded/Server/scripts/item_bonus.fos.md)
- [item_dogtags.fos](../../../../../PReloaded/Server/scripts/item_dogtags.fos.md)
- [item_dynamic.fos](../../../../../PReloaded/Server/scripts/item_dynamic.fos.md)
- [item_mapdoor.fos](../../../../../PReloaded/Server/scripts/item_mapdoor.fos.md)
- [item_misc.fos](../../../../../PReloaded/Server/scripts/item_misc.fos.md)
- [item_perks.fos](../../../../../PReloaded/Server/scripts/item_perks.fos.md)
- [item_tent.fos](../../../../../PReloaded/Server/scripts/item_tent.fos.md)
- [linetracer.fos](../../../../../PReloaded/Server/scripts/linetracer.fos.md)
- [map_bos_lh.fos](../../../../../PReloaded/Server/scripts/map_bos_lh.fos.md)
- [map_hub.fos](../../../../../PReloaded/Server/scripts/map_hub.fos.md)
- [map_npcmap.fos](../../../../../PReloaded/Server/scripts/map_npcmap.fos.md)
- [map_tent.fos](../../../../../PReloaded/Server/scripts/map_tent.fos.md)
- [mapper_autowall.fos](../../../../../PReloaded/Server/scripts/mapper_autowall.fos.md)
- [mapper_generators.fos](../../../../../PReloaded/Server/scripts/mapper_generators.fos.md)
- [mapper_gui.fos](../../../../../PReloaded/Server/scripts/mapper_gui.fos.md)
- [minigames.fos](../../../../../PReloaded/Server/scripts/minigames.fos.md)
- [npc_ai.fos](../../../../../PReloaded/Server/scripts/npc_ai.fos.md)
- [npc_barber.fos](../../../../../PReloaded/Server/scripts/npc_barber.fos.md)
- [npc_planes_h.fos](../../../../../PReloaded/Server/scripts/npc_planes_h.fos.md)
- [pdata.fos](../../../../../PReloaded/Server/scripts/pdata.fos.md)
- [polygon.fos](../../../../../PReloaded/Server/scripts/polygon.fos.md)
- [prod_ingredients.fos](../../../../../PReloaded/Server/scripts/prod_ingredients.fos.md)
- [server_fixboy.fos](../../../../../PReloaded/Server/scripts/server_fixboy.fos.md)
- [utils.fos](../../../../../PReloaded/Server/scripts/utils.fos.md)
- [workbench.fos](../../../../../PReloaded/Server/scripts/workbench.fos.md)
- [zzz.fos](../../../../../PReloaded/Server/scripts/zzz.fos.md)
- [_all_defines.fos](_all_defines.fos.md)
- [den_barbekky_boy.fos](den_barbekky_boy.fos.md)
- [dialog.fos](dialog.fos.md)
- [trader.fos](trader.fos.md)

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __DEFINES__ |  |  |
| NULL | `(0)` |  |
| NONE | `(0)` |  |
| FALSE | `(0)` |  |
| TRUE | `(1)` |  |
| OK | `#(a)                   ((a)>=0)` |  |
| ERROR | `#(a)                ((a)<0)` |  |
| VALID | `#(ptr)              ((ptr)!=null)` |  |
| NOT_VALID | `#(ptr)          ((ptr)==null)` |  |
| MIN | `#(a,b)                (((a)<(b))?(a):(b))` |  |
| MAX | `#(a,b)                (((a)>(b))?(a):(b))` |  |
| POW2 | `#(a)                 ((a)*(a))` |  |
| POW3 | `#(a)                 ((a)*(a)*(a))` |  |
| BOOL | `int32` | Data types |
| DWORD | `uint32` |  |
| WORD | `uint16` |  |
| BYTE | `uint8` |  |
| long | `int32` |  |
| short | `int16` |  |
| char | `int8` |  |
| SAY_NORM | `(1)` | Say types |
| SAY_SHOUT | `(2)` |  |
| SAY_EMOTE | `(3)` |  |
| SAY_WHISP | `(4)` |  |
| SAY_SOCIAL | `(5)` |  |
| SAY_RADIO | `(6)` |  |
| ACT_NULL | `1` | Actions |
| ACT_SHOW_OBJ | `2` |  |
| ACT_HIDE_OBJ | `3` |  |
| ACT_ACTIVATE_OBJ | `4` |  |
| ACT_DACTIVATE_OBJ | `5` |  |
| ACT_USE_OBJ | `6` |  |
| ACT_CHANGE_ARM | `7` |  |
| ACT_DEFEAT | `8` |  |
| ACT_DEFEAT_MISS | `1` |  |
| ACT_DEFEAT_FRONT | `2` |  |
| ACT_DEFEAT_REAR | `3` |  |
| ACT_DEFEAT_KO_FRONT | `4` |  |
| ACT_DEFEAT_KO_REAR | `5` |  |
| ACT_REFRESH | `(9` |  |
| ACT_DEAD | `(10` |  |
| ACT_CR_DEAD | `(11` |  |
| ACT_DISCONNECT | `(12` |  |
| ACT_DROP_OBJ | `(13` |  |
| ACT_PICK_OBJ_UP | `(14` |  |
| ACT_PICK_OBJ_DOWN | `(15` |  |
| COND_LIFE | `(1)` | Critter conditions |
| COND_LIFE_NONE | `(1)` |  |
| COND_LIFE_ACTWEAP | `(2)` |  |
| COND_LIFE_USEOBJ | `(3)` |  |
| COND_LIFE_OFFLINE | `(4)` |  |
| COND_KNOCK_OUT | `(2)` |  |
| COND_KO_UP | `(1)` |  |
| COND_KO_DOWN | `(2)` |  |
| COND_DEAD | `(3)` |  |
| COND_DEAD_NORMAL_UP | `(1)` |  |
| COND_DEAD_NORMAL_DOWN | `(2)` |  |
| COND_DEAD_CR_NORMAL_UP | `(3)` |  |
| COND_DEAD_BRUST | `(4)` |  |
| COND_DEAD_CR_BRUST | `(5)` |  |
| COND_DEAD_LASER | `(6)` |  |
| COND_DEAD_FIRE | `(7)` |  |
| COND_DEAD_PLASMA | `(8)` |  |
| COND_DEAD_ELECTR | `(9)` |  |
| COND_DEAD_EMP | `(10)` |  |
| COND_DEAD_EXPLODE | `(11)` |  |
| COND_NOT_IN_GAME | `(4)` |  |
| GENDER_MALE | `(0)` | Gender |
| GENDER_FEMALE | `(1)` |  |
| OBJ_ARMOR | `(1)` | Objects types |
| OBJ_CONTAINER | `(2)` |  |
| OBJ_DRUG | `(3)` |  |
| OBJ_WEAPON | `(4)` |  |
| OBJ_AMMO | `(5)` |  |
| OBJ_MISC | `(6)` |  |
| OBJ_KEY | `(7)` |  |
| OBJ_DOOR | `(8)` |  |
| OBJ_CRAFTING | `(9)` |  |
| OBJ_GRID | `(10)` |  |
| ACCESSORY_CRIT | `(1)` | Accessory |
| ACCESSORY_HEX | `(2)` |  |
| ACCESSORY_CONT | `(3)` |  |
| DAMAGE_NORMAL | `(1)` | Damage types |
| DAMAGE_LASER | `(2)` |  |
| DAMAGE_FIRE | `(3)` |  |
| DAMAGE_PLASMA | `(4)` |  |
| DAMAGE_ELECTR | `(5)` |  |
| DAMAGE_EMP | `(6)` |  |
| DAMAGE_EXPLODE | `(7)` |  |
| MESSAGE_TO_VISIBLE_ME | `(0)` | In SendMessage |
| MESSAGE_TO_IAM_VISIBLE | `(1)` |  |
| MESSAGE_TO_ALL_ON_MAP | `(2)` |  |
| SLOT_INV | `(0)` | Slots |
| SLOT_HAND1 | `(1)` |  |
| SLOT_HAND2 | `(2)` |  |
| SLOT_ARMOR | `(3)` |  |
| ST_STRENGHT | `0` | Primary stats |
| ST_PERCEPTION | `1` |  |
| ST_ENDURANCE | `2` |  |
| ST_CHARISMA | `3` |  |
| ST_INTELLECT | `4` |  |
| ST_AGILITY | `5` |  |
| ST_LUCK | `6` |  |
| ST_MAX_LIFE | `7` | Secondary stats |
| ST_MAX_COND | `8` |  |
| ST_ARMOR_CLASS | `9` |  |
| ST_MELEE_DAMAGE | `10` |  |
| ST_WEAPON_DAMAGE | `11` |  |
| ST_CARRY_WEIGHT | `12` |  |
| ST_SEQUENCE | `13` |  |
| ST_HEALING_RATE | `14` |  |
| ST_CRITICAL_CHANCE | `15` |  |
| ST_MAX_CRITICAL | `16` |  |
| ST_INGURE_ABSORB | `17` |  |
| ST_LASER_ABSORB | `18` |  |
| ST_FIRE_ABSORB | `19` |  |
| ST_PLASMA_ABSORB | `20` |  |
| ST_ELECTRO_ABSORB | `21` |  |
| ST_EMP_ABSORB | `22` |  |
| ST_BLAST_ABSORB | `23` |  |
| ST_INGURE_RESIST | `24` |  |
| ST_LASER_RESIST | `25` |  |
| ST_FIRE_RESIST | `26` |  |
| ST_PLASMA_RESIST | `27` |  |
| ST_ELECTRO_RESIST | `28` |  |
| ST_EMP_RESIST | `29` |  |
| ST_BLAST_RESIST | `30` |  |
| ST_RADIATION_RESISTANCE | `31` |  |
| ST_POISON_RESISTANCE | `32` |  |
| ST_AGE | `33` |  |
| ST_GENDER | `34` |  |
| ST_CURRENT_HP | `35` |  |
| ST_POISONING_LEVEL | `36` |  |
| ST_RADIATION_LEVEL | `37` |  |
| ST_CURRENT_STANDART | `38` |  |
| ST_EXPERIENCE | `39` |  |
| ST_LEVEL | `40` |  |
| ST_UNSPENT_SKILL_POINTS | `41` |  |
| ST_UNSPENT_PERKS | `42` |  |
| ST_KARMA | `43` |  |
| SK_SMALL_GUNS | `0` | Skills |
| SK_BIG_GUNS | `1` |  |
| SK_ENERGY_WEAPONS | `2` |  |
| SK_UNARMED | `3` |  |
| SK_MELEE_WEAPONS | `4` |  |
| SK_THROWING | `5` |  |
| SK_FIRST_AID | `6` |  |
| SK_DOCTOR | `7` |  |
| SK_SNEAK | `8` |  |
| SK_LOCKPICK | `9` |  |
| SK_STEAL | `10` |  |
| SK_TRAPS | `11` |  |
| SK_SCIENCE | `12` |  |
| SK_REPAIR | `13` |  |
| SK_SPEECH | `14` |  |
| SK_BARTER | `15` |  |
| SK_GAMBLING | `16` |  |
| SK_OUTDOORSMAN | `17` |  |
| PE_FAST_METABOLISM | `0` | Traits |
| PE_BRUISER | `1` |  |
| PE_SMALL_FRAME | `2` |  |
| PE_ONE_HANDER | `3` |  |
| PE_FINESSE | `4` |  |
| PE_KAMIKAZE | `5` |  |
| PE_HEAVY_HANDED | `6` |  |
| PE_FAST_SHOT | `7` |  |
| PE_BLOODY_MESS | `8` |  |
| PE_JINXED | `9` |  |
| PE_GOOD_NATURED | `10` |  |
| PE_CHEM_RELIANT | `11` |  |
| PE_CHEM_RESISTANT | `12` |  |
| PE_NIGHT_PERSON | `13` |  |
| PE_SKILLED | `14` |  |
| PE_GIFTED | `15` |  |
| PE_AWARENESS | `16` | Perks |
| PE_A_MELEE_ATT | `17` |  |
| PE_A_MELEE_DAM | `18` |  |
| PE_A_MOVE | `19` |  |
| PE_A_DAM | `20` |  |
| PE_A_SPEED | `21` |  |
| PE_PASS_FRONT | `22` |  |
| PE_RAPID_HEAL | `23` |  |
| PE_MORE_CRIT_DAM | `24` |  |
| PE_NIGHT_SIGHT | `25` |  |
| PE_PRESENCE | `26` |  |
| PE_RES_NUKLEAR | `27` |  |
| PE_ENDURENCE | `28` |  |
| PE_STR_BACK | `29` |  |
| PE_MARKSMAN | `30` |  |
| PE_STEALHING | `31` |  |
| PE_LIFEFULL | `32` |  |
| PE_MERCHANT | `33` |  |
| PE_FORMED | `34` |  |
| PE_HEALER | `35` |  |
| PE_TR_DIGGER | `36` |  |
| PE_BEST_HITS | `37` |  |
| PE_COMPASION | `38` |  |
| PE_KILLER | `39` |  |
| PE_SNIPER | `40` |  |
| PE_SILENT_DEATH | `41` |  |
| PE_C_FIGHTER | `42` |  |
| PE_MIND_BLOCK | `43` |  |
| PE_PROLONGATION_LIFE | `44` |  |
| PE_RECOURCEFULNESS | `45` |  |
| PE_SNAKE_EATER | `46` |  |
| PE_REPEARER | `47` |  |
| PE_MEDIC | `48` |  |
| PE_SKILLED_THIEF | `49` |  |
| PE_SPEAKER | `50` |  |
| PE_GUTCHER | `51` |  |
| PE_FRIENDLY_FOE | `52` |  |
| PE_PICK_POCKER | `53` |  |
| PE_GHOST | `54` |  |
| PE_CHAR_CULT | `55` |  |
| PE_THIFER | `56` |  |
| PE_DISCOVER | `57` |  |
| PE_THE_PURETY | `58` |  |
| PE_OVERROAD | `59` |  |
| PE_ANIMAL_FRIENDSHIP | `60` |  |
| PE_SCOUT | `61` |  |
| PE_MIST_CHAR | `62` |  |
| PE_RANGER | `63` |  |
| PE_PICK_POCKET_2 | `64` |  |
| PE_INTERLOCUTER | `65` |  |
| PE_NOVICE | `66` |  |
| PE_PRIME_SKILL | `67` |  |
| PE_MUTATION | `68` |  |
| PE_NARC_NUKACOLA | `69` |  |
| PE_NARC_BUFFOUT | `70` |  |
| PE_NARC_MENTAT | `71` |  |
| PE_NARC_PSYHO | `72` |  |
| PE_NARC_RADAWAY | `73` |  |
| PE_DISTANT_WEAP | `74` |  |
| PE_ACCURARY_WEAP | `75` |  |
| PE_PENETRATION_WEAP | `76` |  |
| PE_KILLER_WEAP | `77` |  |
| PE_ENERGY_ARMOR | `78` |  |
| PE_BATTLE_ARMOR | `79` |  |
| PE_WEAP_RANGE | `80` |  |
| PE_RAPID_RELOAD | `81` |  |
| PE_NIGHT_SPYGLASS | `82` |  |
| PE_FLAMER | `83` |  |
| PE_APA_I | `84` |  |
| PE_APA_II | `85` |  |
| PE_FORCEAGE | `86` |  |
| PE_DEADLY_NARC | `87` |  |
| PE_CHARMOLEANCE | `88` |  |
| PE_GEKK_SKINER | `89` |  |
| PE_SKIN_ARMOR | `90` |  |
| PE_A_SKIN_ARMOR | `91` |  |
| PE_SUPER_ARMOR | `92` |  |
| PE_A_SUPER_ARMOR | `93` |  |
| PE_VAULT_INOCUL | `94` |  |
| PE_ADRENALIN_RUSH | `95` |  |
| PE_CAREFULL | `96` |  |
| PE_INTELEGENCE | `97` |  |
| PE_PYROKASY | `98` |  |
| PE_DUDE | `99` |  |
| PE_A_STR | `100` |  |
| PE_A_PER | `101` |  |
| PE_A_END | `102` |  |
| PE_A_CHA | `103` |  |
| PE_A_INT | `104` |  |
| PE_A_AGL | `105` |  |
| PE_A_LUC | `106` |  |
| PE_PURERER | `107` |  |
| PE_IMAG | `108` |  |
| PE_EVASION | `109` |  |
| PE_DROSHKADRAT | `110` |  |
| PE_KARMA_GLOW | `111` |  |
| PE_SILENT_STEPS | `112` |  |
| PE_ANATOMY | `113` |  |
| PE_CHAMER | `114` |  |
| PE_ORATOR | `115` |  |
| PE_PACKER | `116` |  |
| PE_EDD_GAYAN_MANIAC | `117` |  |
| PE_FAST_REGENERATION | `118` |  |
| PE_VENDOR | `119` |  |
| PE_STONE_WALL | `120` |  |
| PE_THIEF_AGAIN | `121` |  |
| PE_WEAPON_SKILL | `122` |  |
| PE_MAKE_VAULT | `123` |  |
| PE_ALC_BUFF_1 | `124` |  |
| PE_ALC_BUFF_2 | `125` |  |
| PE_ALC_RAIS_1 | `126` |  |
| PE_ALC_RAIS_2 | `127` |  |
| PE_AUTODOC_BUFF_1 | `128` |  |
| PE_AUTODOC_BUFF_2 | `129` |  |
| PE_AUTODOC_RAIS_1 | `130` |  |
| PE_AUTODOC_RAIS_2 | `131` |  |
| PE_EXCREMENT_EXPEDITOR | `132` |  |
| PE_WEAPON_ENHANCED | `133` |  |
| PE_UNLUCK | `134` |  |
| PE_BOOKWORM | `135` |  |
| PE_DAMAGE_POISONED | `200` | Critter damages |
| PE_DAMAGE_RADIATED | `201` |  |
| PE_DAMAGE_EYE | `202` |  |
| PE_DAMAGE_RIGHT_ARM | `203` |  |
| PE_DAMAGE_LEFT_ARM | `204` |  |
| PE_DAMAGE_RIGHT_LEG | `205` |  |
| PE_DAMAGE_LEFT_LEG | `206` |  |
| PE_DMGRESERVED1 | `207` |  |
| PE_DMGRESERVED2 | `208` |  |
| PE_DMGRESERVED3 | `209` |  |
| PE_TAG_SKILL1 | `210` | Tag skills |
| PE_TAG_SKILL2 | `211` |  |
| PE_TAG_SKILL3 | `212` |  |
| PE_HIDE_MODE | `215` | Modes |

