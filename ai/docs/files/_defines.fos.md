---
title: _defines.fos
description: "uncomment for verbose npc_schedule*.fos #define DEBUG_SCHEDULES..."
---

# _defines.fos

uncomment for verbose npc_schedule*.fos
#define DEBUG_SCHEDULES

## Included By

- [_colors.fos](_colors.fos.md)
- [_macros.fos](_macros.fos.md)
- [buffer_lazy.fos](buffer_lazy.fos.md)
- [buffer_lazy_h.fos](buffer_lazy_h.fos.md)
- [smart_cursor.fos](client/smart_cursor.fos.md)
- [client_access.fos](client_access.fos.md)
- [client_critter_onhead.fos](client_critter_onhead.fos.md)
- [client_fef.fos](client_fef.fos.md)
- [client_interface.fos](client_interface.fos.md)
- [client_mapper_animation.fos](client_mapper_animation.fos.md)
- [client_messages.fos](client_messages.fos.md)
- [client_screen_gameinfo_h.fos](client_screen_gameinfo_h.fos.md)
- [client_timeouts.fos](client_timeouts.fos.md)
- [config.fos](config.fos.md)
- [critter_description.fos](critter_description.fos.md)
- [critter_item_movement.fos](critter_item_movement.fos.md)
- [critter_skin.fos](critter_skin.fos.md)
- [devconnect.fos](devconnect.fos.md)
- [entire.fos](entire.fos.md)
- [gmtools_h.fos](gmtools_h.fos.md)
- [item_achievementbook.fos](item_achievementbook.fos.md)
- [item_attributes.fos](item_attributes.fos.md)
- [item_bonus.fos](item_bonus.fos.md)
- [item_dogtags.fos](item_dogtags.fos.md)
- [item_dynamic.fos](item_dynamic.fos.md)
- [item_mapdoor.fos](item_mapdoor.fos.md)
- [item_misc.fos](item_misc.fos.md)
- [item_perks.fos](item_perks.fos.md)
- [item_tent.fos](item_tent.fos.md)
- [linetracer.fos](linetracer.fos.md)
- [map_bos_lh.fos](map_bos_lh.fos.md)
- [map_hub.fos](map_hub.fos.md)
- [map_npcmap.fos](map_npcmap.fos.md)
- [map_tent.fos](map_tent.fos.md)
- [mapper_autowall.fos](mapper_autowall.fos.md)
- [mapper_generators.fos](mapper_generators.fos.md)
- [mapper_gui.fos](mapper_gui.fos.md)
- [minigames.fos](minigames.fos.md)
- [npc_ai.fos](npc_ai.fos.md)
- [npc_barber.fos](npc_barber.fos.md)
- [npc_planes_h.fos](npc_planes_h.fos.md)
- [pdata.fos](pdata.fos.md)
- [polygon.fos](polygon.fos.md)
- [prod_ingredients.fos](prod_ingredients.fos.md)
- [server_fixboy.fos](server_fixboy.fos.md)
- [utils.fos](utils.fos.md)
- [workbench.fos](workbench.fos.md)
- [zzz.fos](zzz.fos.md)

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __DEBUG_DISABLE_SQL__ |  |  |
| PLAYER_NO_DROP | `1` | NO DROP MODE FOR PLAYERS (ugly) |
| SAYEX_VERBOSE_ACTION | `(1)` | SayEx() type |
| SAYEX_MAX | `(2)` |  |
| FLOAT_ENFORCED | `(0)` | MapMessageEx() type |
| FLOAT_VERBOSE_ACTION | `(1)` |  |
| FLOAT_EXPERIENCE | `(2)` |  |
| FLOAT_MAX | `(3)` |  |
| FLOAT_MODE_SINGLE | `(1)` | MapMessageEx() mode |
| FLOAT_MODE_ALL | `(2)` |  |
| FLOAT_MODE_AROUND | `(3)` |  |
| FLOAT_MODE_MAX | `(4)` |  |
| DLGSTR | `# (dialogId, strNum)(1000000000 + (dialogId) * 100000 + (strNum))` | Msg nums |
| COND_LIFE | `(1)` | Critter conditions |
| COND_KNOCKOUT | `(2)` |  |
| COND_DEAD | `(3)` |  |
| CRITTER_CONDITION_NOT_IN_GAME | `(4)` |  |
| GENDER_IT | `(2)` | Gender |
| ACCESSORY_NONE | `(0)` | Items accessory |
| ACCESSORY_CRITTER | `(1)` |  |
| ACCESSORY_HEX | `(2)` |  |
| ACCESSORY_CONTAINER | `(3)` |  |
| ITEM_TYPE_SMO | `(14)` | hardcoded type values in proto files :/ :( :| User types |
| ITEM_TYPE_BLUEPRINT | `(20)` |  |
| ITEM_TYPE_SPOT | `(21)` |  |
| ITEM_TYPE_MAP_OBJECT | `(22)` |  |
| ITEM_TYPE_TRANSFER | `(23)` |  |
| ITEM_TYPE_TRIGGER | `(24)` | or walked over: exit edges, ladders etc. (WIP, don't use). |
| ITEM_HIDDEN | `(0x00000001)` | Item flags |
| ITEM_FLAT | `(0x00000002)` |  |
| ITEM_NO_BLOCK | `(0x00000004)` |  |
| ITEM_SHOOT_THRU | `(0x00000008)` |  |
| ITEM_LIGHT_THRU | `(0x00000010)` |  |
| ITEM_MULTI_HEX | `(0x00000020)` |  |
| ITEM_WALL_TRANS_END | `(0x00000040)` |  |
| ITEM_TWO_HANDS | `(0x00000080)` |  |
| ITEM_BIG_GUN | `(0x00000100)` |  |
| ITEM_ALWAYS_VIEW | `(0x00000200)` |  |
| ITEM_HAS_TIMER | `(0x00000400)` |  |
| ITEM_BAD_ITEM | `(0x00000800)` |  |
| ITEM_NO_HIGHLIGHT | `(0x00001000)` |  |
| ITEM_SHOW_ANIM | `(0x00002000)` |  |
| ITEM_SHOW_ANIM_EXT | `(0x00004000)` |  |
| ITEM_LIGHT | `(0x00008000)` |  |
| ITEM_GECK | `(0x00010000)` |  |
| ITEM_TRAP | `(0x00020000)` |  |
| ITEM_NO_LIGHT_INFLUENCE | `(0x00040000)` |  |
| ITEM_NO_LOOT | `(0x00080000)` |  |
| ITEM_NO_STEAL | `(0x00100000)` |  |
| ITEM_GAG | `(0x00200000)` |  |
| ITEM_COLORIZE | `(0x00400000)` |  |
| ITEM_COLORIZE_INV | `(0x00800000)` |  |
| ITEM_CAN_USE_ON_SMTH | `(0x01000000)` |  |
| ITEM_CAN_LOOK | `(0x02000000)` |  |
| ITEM_CAN_TALK | `(0x04000000)` |  |
| ITEM_CAN_PICKUP | `(0x08000000)` |  |
| ITEM_CAN_USE | `(0x10000000)` |  |
| ITEM_HOLODISK | `(0x20000000)` |  |
| ITEM_RADIO | `(0x40000000)` |  |
| ITEM_CACHED | `(0x80000000)` |  |
| BONUS_WEAPON_CRITICAL_ROLL | `(100)` | Possible weapon bonus |
| BONUS_WEAPON_CRITICAL_CHANCE | `(101)` |  |
| BONUS_WEAPON_MIN_DMG | `(102)` |  |
| BONUS_WEAPON_MAX_DMG | `(103)` |  |
| BONUS_WEAPON_ACCURACY | `(104)` |  |
| BONUS_WEAPON_MAX_AP | `(105)` |  |
| BONUS_WEAPON_MAX_RANGE | `(106)` |  |
| BONUS_ARMOR_CRIT_CHANCE | `(100)` | Possible armor bonus |
| BONUS_ARMOR_CRIT_POWER | `(101)` |  |
| BONUS_ARMOR_NORMAL_DT | `(102)` |  |
| BONUS_ARMOR_LASER_DT | `(103)` |  |
| BONUS_ARMOR_FIRE_DT | `(104)` |  |
| BONUS_ARMOR_PLASMA_DT | `(105)` |  |
| BONUS_ARMOR_NORMAL_DR | `(106)` |  |
| BONUS_ARMOR_LASER_DR | `(107)` |  |
| BONUS_ARMOR_FIRE_DR | `(108)` |  |
| BONUS_ARMOR_PLASMA_DR | `(109)` |  |
| BONUS_ARMOR_EXPLODE_DT | `(110)` |  |
| BONUS_ARMOR_EXPLODE_DR | `(111)` |  |
| BONUS_ARMOR_MAX_AP | `(112)` |  |
| BONUS_ARMOR_RAD_RES | `(113)` |  |
| BONUS_ARMOR_POISON_RES | `(114)` |  |
| BONUS_ARMOR_STRENGTH | `(115)` |  |
| BONUS_ARMOR_PERCEPTION | `(116)` |  |
| BONUS_ARMOR_ENDURANCE | `(117)` |  |
| BONUS_ARMOR_CHARISMA | `(118)` |  |
| BONUS_ARMOR_INTELLIGENCE | `(119)` |  |
| BONUS_ARMOR_AGILITY | `(120)` |  |
| BONUS_ARMOR_LUCK | `(121)` |  |
| BONUS_ARMOR_CARRY_WEIGHT | `(122)` |  |
| BONUS_ARMOR_HEALING_RATE | `(123)` |  |
| GRID_EXITGRID | `(1)` | Grid Types |
| GRID_STAIRS | `(2)` |  |
| GRID_LADDERBOT | `(3)` |  |
| GRID_LADDERTOP | `(4)` |  |
| GRID_ELEVATOR | `(5)` |  |
| CRIPPLED_EYE | `(0x00000001)` |  |
| CRIPPLED_RIGHT_ARM | `(0x00000002)` |  |
| CRIPPLED_LEFT_ARM | `(0x00000004)` |  |
| CRIPPLED_RIGHT_LEG | `(0x00000008)` |  |
| CRIPPLED_LEFT_LEG | `(0x00000010)` |  |
| DAMAGE_UNCALLED | `(0)` | Damage types |
| DAMAGE_NORMAL | `(1)` |  |
| DAMAGE_LASER | `(2)` |  |
| DAMAGE_FIRE | `(3)` |  |
| DAMAGE_PLASMA | `(4)` |  |
| DAMAGE_ELECTR | `(5)` |  |
| DAMAGE_EMP | `(6)` |  |
| DAMAGE_EXPLODE | `(7)` |  |
| CRITTER_EVENT_EXT_MAP_IN | `(0)` | 2238-specific |
| CRITTER_EVENT_EXT_MAP_OUT | `(1)` |  |
| CRITTER_EVENT_EXT_MAX | `(2)` |  |
| PLANE_RUN_GLOBAL | `(0)` | Return values for CRITTER_EVENT_PLANE_ BEGIN/END/RUN events |
| PLANE_KEEP | `(1)` |  |
| PLANE_DISCARD | `(2)` |  |
| ITEM_PERK_ARMOR | `(1)` | Item perks |
| ITEM_PERK_HELMET | `(2)` |  |
| WEAPON_PERK_LONG_RANGE | `(1)` |  |
| WEAPON_PERK_ACCURATE | `(2)` |  |
| WEAPON_PERK_PENETRATE | `(3)` |  |
| WEAPON_PERK_KNOCKBACK | `(4)` |  |
| WEAPON_PERK_SCOPE_RANGE | `(5)` |  |
| WEAPON_PERK_FAST_RELOAD | `(6)` |  |
| WEAPON_PERK_NIGHT_SIGHT | `(7)` |  |
| WEAPON_PERK_FLAMEBOY | `(8)` |  |
| WEAPON_PERK_ENHANCED_KNOCKOUT | `(9)` |  |
| ARMOR_PERK_POWERED | `(1)` |  |
| ARMOR_PERK_COMBAT | `(2)` |  |
| ARMOR_PERK_ADVANCED_I | `(3)` |  |
| ARMOR_PERK_ADVANCED_II | `(4)` |  |
| HELMET_PERK_CHARISMA | `(1)` |  |
| HELMET_PERK_PERCEPTION_GLASSES | `(2)` |  |
| HELMET_PERK_PROTECT_EYES | `(3)` |  |
| SLOT_PERK_COSMETIC_CASE | `(0x02)` |  |
| SLOT_PERK_MOTION_SENSOR | `(0x04)` |  |
| SLOT_PERK_STEALTH_BOY | `(0x08)` |  |
| MESSAGE_TO_VISIBLE_ME | `(0)` | In SendMessage |
| MESSAGE_TO_IAM_VISIBLE | `(1)` |  |
| MESSAGE_TO_ALL_ON_MAP | `(2)` |  |
| SENDMESSAGE_TO_WHO_SEES_ME | `(SENDMESSAGE_TO_VISIBLE_ME)` | more eng-friendly aliases |
| SENDMESSAGE_TO_I_SEE | `(SENDMESSAGE_TO_IAM_VISIBLE)` |  |
| SLOT_HEAD | `(SLOT_LAST+1)` | Slots |
| SLOT_TROPHY | `(SLOT_LAST+2)` |  |
| SLOT_GROUND | `(255)` |  |
| CTE_DELETE | `(-1)` | Critter timeevents identifiers |
| CTE_POISON | `(1)` |  |
| CTE_RADIATION | `(2)` |  |
| CTE_TRADER | `(3)` |  |
| CTE_OBSERVING | `(4)` |  |
| CTE_AUTOKILL | `(5)` |  |
| CTE_FOLLOWER_LOYALITY | `(6)` |  |
| CTE_FOLLOWER_JOIN | `(7)` |  |
| CTE_AGE | `(8)` |  |
| CTE_CUTSCENE | `(9)` |  |
| CTE_SCHEDULE | `(10)` |  |
| CTE_SCHEDULE_FIND_NEXT | `(11)` |  |
| CTE_CHEAT_AURA | `(1337)` | Drugs time events                40 (PID_STIMPAK) .. 1000 |
| STAT_BEGIN | `(0)` | Parameters Stats |
| STAT_END | `(199)` |  |
| STAT_COUNT | `(STAT_END - STAT_BEGIN + 1)` |  |
| STAT_EXT_BEGIN | `(32)` |  |
| STAT_EXT_END | `(63)` |  |
| ST_ENDURANCE | `(2)` | FOClassic.fos #define ST_STRENGTH                              (0) // Used in engine +++ FOClassic.fos #define ST_PERCEPTION                            (1) |
| ST_LUCK | `(6)` | FOClassic.fos #define ST_CHARISMA                              (3) FOClassic.fos #define ST_INTELLECT                             (4) FOClassic.fos #define ST_AGILITY                               (5) |
| ST_MAX_CRITICAL | `(15)` | FOClassic.fos #define ST_MAX_LIFE                              (7) FOClassic.fos #define ST_ACTION_POINTS                         (8) FOClassic.fos #define ST_ARMOR_CLASS                           (9) FOClassic.fos #define ST_MELEE_DAMAGE                          (10) FOClassic.fos #define ST_CARRY_WEIGHT                          (11) FOClassic.fos #define ST_SEQUENCE                              (12) FOClassic.fos #define ST_HEALING_RATE                          (13) FOClassic.fos #define ST_CRITICAL_CHANCE                       (14) |
| ST_NORMAL_ABSORB | `(16)` |  |
| ST_LASER_ABSORB | `(17)` |  |
| ST_FIRE_ABSORB | `(18)` |  |
| ST_PLASMA_ABSORB | `(19)` |  |
| ST_ELECTRO_ABSORB | `(20)` |  |
| ST_EMP_ABSORB | `(21)` |  |
| ST_EXPLODE_ABSORB | `(22)` |  |
| ST_LASER_RESIST | `(24)` | FOClassic.fos #define ST_NORMAL_RESIST                         (23) |
| ST_FIRE_RESIST | `(25)` |  |
| ST_PLASMA_RESIST | `(26)` |  |
| ST_ELECTRO_RESIST | `(27)` |  |
| ST_EMP_RESIST | `(28)` |  |
| ST_EXPLODE_RESIST | `(29)` |  |
| ST_STRENGTH_EXT | `(32)` | FOClassic.fos #define ST_RADIATION_RESISTANCE                  (30) FOClassic.fos #define ST_POISON_RESISTANCE                     (31) |
| ST_PERCEPTION_EXT | `(33)` |  |
| ST_ENDURANCE_EXT | `(34)` |  |
| ST_CHARISMA_EXT | `(35)` |  |
| ST_INTELLECT_EXT | `(36)` |  |
| ST_AGILITY_EXT | `(37)` |  |
| ST_LUCK_EXT | `(38)` |  |
| ST_MAX_LIFE_EXT | `(39)` |  |
| ST_ACTION_POINTS_EXT | `(40)` |  |
| ST_ARMOR_CLASS_EXT | `(41)` |  |
| ST_MELEE_DAMAGE_EXT | `(42)` |  |
| ST_CARRY_WEIGHT_EXT | `(43)` |  |
| ST_SEQUENCE_EXT | `(44)` |  |
| ST_HEALING_RATE_EXT | `(45)` |  |
| ST_CRITICAL_CHANCE_EXT | `(46)` |  |
| ST_MAX_CRITICAL_EXT | `(47)` |  |
| ST_NORMAL_ABSORB_EXT | `(48)` |  |
| ST_LASER_ABSORB_EXT | `(49)` |  |
| ST_FIRE_ABSORB_EXT | `(50)` |  |
| ST_PLASMA_ABSORB_EXT | `(51)` |  |
| ST_ELECTRO_ABSORB_EXT | `(52)` |  |
| ST_EMP_ABSORB_EXT | `(53)` |  |
| ST_EXPLODE_ABSORB_EXT | `(54)` |  |
| ST_NORMAL_RESIST_EXT | `(55)` |  |
| ST_LASER_RESIST_EXT | `(56)` |  |
| ST_FIRE_RESIST_EXT | `(57)` |  |
| ST_PLASMA_RESIST_EXT | `(58)` |  |
| ST_ELECTRO_RESIST_EXT | `(59)` |  |
| ST_EMP_RESIST_EXT | `(60)` |  |
| ST_EXPLODE_RESIST_EXT | `(61)` |  |
| ST_RADIATION_RESISTANCE_EXT | `(62)` |  |
| ST_POISON_RESISTANCE_EXT | `(63)` |  |
| ST_TOXIC | `(64)` |  |
| ST_RADIOACTIVE | `(65)` |  |
| ST_KILL_EXPERIENCE | `(66)` |  |
| ST_BODY_TYPE | `(67)` |  |
| ST_LOCOMOTION_TYPE | `(68)` |  |
| ST_DAMAGE_TYPE | `(69)` |  |
| ST_VAR0 | `(90)` | FOClassic.fos #define ST_AGE                                   (70) // Used in engine FOClassic.fos #define ST_GENDER                                (71) // Used in engine FOClassic.fos #define ST_CURRENT_HP                            (72) // Used in engine FOClassic.fos #define ST_POISONING_LEVEL                       (73) // Used in engine FOClassic.fos #define ST_RADIATION_LEVEL                       (74) // Used in engine FOClassic.fos #define ST_CURRENT_AP                            (75) // Used in engine FOClassic.fos #define ST_EXPERIENCE                            (76) // Used in engine FOClassic.fos #define ST_LEVEL                                 (77) // Used in engine FOClassic.fos #define ST_UNSPENT_SKILL_POINTS                  (78) // Used in engine FOClassic.fos #define ST_UNSPENT_PERKS                         (79) // Used in engine FOClassic.fos #define ST_KARMA                                 (80) // Used in engine FOClassic.fos #define ST_FOLLOW_CRIT                           (81) // Used in engine FOClassic.fos #define ST_REPLICATION_MONEY                     (82) // Used in engine FOClassic.fos #define ST_REPLICATION_COUNT                     (83) // Used in engine FOClassic.fos #define ST_REPLICATION_TIME                      (84) // Used in engine FOClassic.fos #define ST_REPLICATION_COST                      (85) // Used in engine FOClassic.fos #define ST_TURN_BASED_AC                         (86) // Used in engine FOClassic.fos #define ST_MAX_MOVE_AP                           (87) // Used in engine FOClassic.fos #define ST_MOVE_AP                               (88) // Used in engine FOClassic.fos #define ST_NPC_ROLE                              (89) // Used in engine |
| ST_VAR1 | `(91)` |  |
| ST_VAR2 | `(92)` |  |
| ST_VAR3 | `(93)` |  |
| ST_VAR4 | `(94)` |  |
| ST_VAR5 | `(95)` |  |
| ST_VAR6 | `(96)` |  |
| ST_VAR7 | `(97)` |  |
| ST_VAR8 | `(98)` |  |
| ST_VAR9 | `(99)` |  |
| ST_PLAYER_KARMA | `(100)` |  |
| ST_LAST_STEAL_CR_ID | `(108)` | FOClassic.fos #define ST_BONUS_LOOK                            (101) // Used in engine FOClassic.fos #define ST_HANDS_ITEM_AND_MODE                   (102) // Used in engine FOClassic.fos #define ST_FREE_BARTER_PLAYER                    (103) // Used in engine FOClassic.fos #define ST_DIALOG_ID                             (104) // Used in engine FOClassic.fos #define ST_AI_ID                                 (105) // Used in engine FOClassic.fos #define ST_TEAM_ID                               (106) // Used in engine FOClassic.fos #define ST_BAG_ID                                (107) // Used in engine |
| ST_STEAL_COUNT | `(109)` |  |
| ST_LAST_WEAPON_USE | `(111)` | FOClassic.fos #define ST_LAST_WEAPON_ID                        (110) // Used in engine |
| ST_DEAD_BLOCKER_ID | `(113)` | FOClassic.fos #define ST_BASE_CRTYPE                           (112) // Used in engine |
| ST_CURRENT_ARMOR_PERK | `(114)` |  |
| ST_FACTION_RANK | `(121)` | post-wipe todo: move those to 130+ to avoid conflicts with new hardcoded values |
| ST_FACTION_MODE | `(122)` |  |
| ST_REP_DECAY | `(130)` | 121..150 |
| ST_SCENARIO | `(131)` |  |
| ST_WEAPON_BLUEPRINTS | `(132)` |  |
| ST_ARMOR_BLUEPRINTS | `(133)` |  |
| ST_MISC_BLUEPRINTS | `(134)` |  |
| ST_EXT_SNEAK | `(135)` |  |
| ST_HEALTH_LEVEL | `(136)` |  |
| ST_SNEAK_FLAGS | `(137)` |  |
| ST_DESCRIPTION1 | `(138)` |  |
| ST_DESCRIPTION2 | `(139)` |  |
| ST_DEFAULT_ARMOR_PID | `(140)` |  |
| ST_DEFAULT_HELMET_PID | `(141)` |  |
| ST_OVERRIDE_CRTYPE | `(143)` |  |
| ST_TURN_BASED_HEX | `(144)` |  |
| ST_CURRENT_HELMET_PERK | `(145)` |  |
| ST_FACTION_UPDATE_SEQ | `(146)` |  |
| ST_MINIGAME_DATA | `(147)` |  |
| ST_UNSPENT_TAG | `(180)` |  |
| ST_FIXBOY_COUNTER | `(181)` |  |
| ST_FIXBOY_FILTER | `(182)` |  |
| ST_FIXBOY_FIXALL | `(183)` |  |
| ST_ALPHA | `(184)` |  |
| SK_SMALL_GUNS | `(200)` | Skills |
| SK_BIG_GUNS | `(201)` |  |
| SK_ENERGY_WEAPONS | `(202)` |  |
| SK_SCAVENGING | `(204)` | FOClassic.fos #define SK_UNARMED                               (203) // Used in engine |
| SK_THROWING | `(205)` |  |
| SK_GAMBLING | `(216)` | FOClassic.fos #define SK_FIRST_AID                             (206) // Used in engine FOClassic.fos #define SK_DOCTOR                                (207) // Used in engine FOClassic.fos #define SK_SNEAK                                 (208) // Used in engine FOClassic.fos #define SK_LOCKPICK                              (209) // Used in engine FOClassic.fos #define SK_STEAL                                 (210) // Used in engine FOClassic.fos #define SK_TRAPS                                 (211) // Used in engine FOClassic.fos #define SK_SCIENCE                               (212) // Used in engine FOClassic.fos #define SK_REPAIR                                (213) // Used in engine FOClassic.fos #define SK_SPEECH                                (214) // Used in engine FOClassic.fos #define SK_BARTER                                (215) // Used in engine |
| SK_OUTDOORSMAN | `(217)` |  |
| TAG_BEGIN | `(226)` | Tag skills |
| TAG_END | `(229)` |  |
| TO_SK_FIRST_AID | `(230)` | Timeouts |
| TO_SK_DOCTOR | `(231)` |  |
| TO_SK_LOCKPICK | `(234)` | FOClassic.fos #define TO_SK_REPAIR                             (232) // Used in engine FOClassic.fos #define TO_SK_SCIENCE                            (233) // Used in engine |
| TO_SK_STEAL | `(235)` |  |
| TO_WEAKENED | `(236)` |  |
| TO_FIXBOY | `(237)` |  |
| TO_REPLICATION | `(241)` | FOClassic.fos #define TO_BATTLE                                (238) // Used in engine FOClassic.fos #define TO_TRANSFER                              (239) // Used in engine FOClassic.fos #define TO_REMOVE_FROM_GAME                      (240) // Used in engine |
| TO_GATHERING | `(243)` | FOClassic.fos #define TO_KARMA_VOTING                          (242) // Used in engine |
| TO_SNEAK | `(244)` |  |
| TO_HEALING | `(245)` |  |
| TO_CIGARETTES | `(246)` |  |
| TO_NUKA_COLA | `(247)` |  |
| TO_BEER | `(248)` |  |
| TO_AGGRESSOR | `(249)` |  |
| TO_PSYCHO | `(250)` |  |
| TO_JET | `(251)` |  |
| TO_IMMUNITY_TIME | `(252)` |  |
| TO_MENTATS | `(253)` |  |
| TO_BUFFOUT | `(254)` |  |
| TO_RAD_X | `(255)` |  |
| KILL_COUNT | `(KILL_END - KILL_BEGIN + 1)` | Kills Reserved 260..299 (BT_MEN..BT_BIG_BAD_BOSS) |
| PE_BOOKWORM | `(300)` | Perks legend: implementation: [no comment] - implemented in scripts (can be referenced in dlls as well) Used in dll - implemented in a dll Used in engine - the perk is implemented in the engine Not implemented - completely unused and left for hypothetical reactivation status: [no comment] - active Disabled - the perk cannot be taken Nolevel - the perk is not available via levelling todo: perk editor? |
| PE_AWARENESS | `(301)` |  |
| PE_BONUS_HTH_ATTACKS | `(302)` |  |
| PE_CLOSE_COMBAT_MASTER | `(303)` |  |
| PE_BONUS_MOVE | `(304)` |  |
| PE_BONUS_RANGED_DAMAGE | `(305)` |  |
| PE_BONUS_RATE_OF_ATTACK | `(306)` |  |
| PE_EARLIER_SEQUENCE | `(307)` |  |
| PE_FASTER_HEALING | `(308)` |  |
| PE_MORE_CRITICALS | `(309)` |  |
| PE_NIGHT_VISION | `(310)` |  |
| PE_PRESENCE | `(311)` |  |
| PE_RAD_RESISTANCE | `(312)` |  |
| PE_TOUGHNESS | `(313)` |  |
| PE_STRONG_BACK | `(314)` |  |
| PE_SHARPSHOOTER | `(315)` |  |
| PE_SURVIVALIST | `(317)` | FOClassic.fos #define PE_SILENT_RUNNING                        (316) // Used in engine |
| PE_EDUCATED | `(319)` | FOClassic.fos #define PE_MASTER_TRADER                         (318) // Disabled, Used in engine |
| PE_FIELD_MEDIC | `(320)` |  |
| PE_FORTUNE_FINDER | `(321)` |  |
| PE_BETTER_CRITICALS | `(322)` |  |
| PE_EMPATHY | `(323)` |  |
| PE_SLAYER | `(324)` |  |
| PE_SNIPER | `(325)` |  |
| PE_SILENT_DEATH | `(326)` |  |
| PE_ACTION_BOY | `(327)` |  |
| PE_MENTAL_BLOCK | `(328)` |  |
| PE_LIFEGIVER | `(329)` |  |
| PE_DODGER | `(330)` |  |
| PE_SNAKEATER | `(331)` |  |
| PE_MR_FIXIT | `(332)` |  |
| PE_MEDIC | `(333)` |  |
| PE_MASTER_THIEF | `(334)` |  |
| PE_SPEAKER | `(335)` |  |
| PE_HEAVE_HO | `(336)` |  |
| PE_FRIENDLY_FOE | `(337)` |  |
| PE_PICKPOCKET | `(338)` |  |
| PE_GHOST | `(339)` |  |
| PE_CULT_OF_PERSONALITY | `(340)` |  |
| PE_SCROUNGER | `(341)` |  |
| PE_EXPLORER | `(342)` |  |
| PE_FLOWER_CHILD | `(343)` |  |
| PE_PATHFINDER | `(344)` |  |
| PE_ANIMAL_FRIEND | `(345)` |  |
| PE_SCOUT | `(346)` |  |
| PE_MYSTERIOUS_STRANGER | `(347)` |  |
| PE_RANGER | `(348)` |  |
| PE_SMOOTH_TALKER | `(350)` | FOClassic.fos #define PE_QUICK_POCKETS                         (349) // Used in engine |
| PE_SWIFT_LEARNER | `(351)` |  |
| PE_TAG | `(352)` |  |
| PE_MUTATE | `(353)` |  |
| PE_PROFESSION_BEGIN | `(354)` | Professions |
| PE_PROFESSION_ARMORER | `(354)` |  |
| PE_PROFESSION_GUNSMITH_S | `(355)` |  |
| PE_PROFESSION_GUNSMITH_B | `(356)` |  |
| PE_PROFESSION_ENERGY_EXPERT | `(357)` |  |
| PE_PROFESSION_DEMOLITION_EXPERT | `(358)` |  |
| PE_PROFESSION_DOCTOR | `(359)` |  |
| PE_PROFESSION_MORDINO_CHEMIST | `(360)` |  |
| PE_PROFESSION_THIEF | `(361)` |  |
| PE_PROFESSION_LIBRARIAN | `(362)` |  |
| PE_PROFESSION_SCOUT | `(363)` |  |
| PE_PROFESSION_END | `(364)` |  |
| PE_PROFESSION_COUNT | `(PE_PROFESSION_END - PE_PROFESSION_BEGIN + 1)` |  |
| PE_ADRENALINE_RUSH | `(380)` | 364...379 |
| PE_CAUTIOUS_NATURE | `(381)` |  |
| PE_COMPREHENSION | `(382)` |  |
| PE_DEMOLITION_EXPERT | `(383)` |  |
| PE_GAMBLER | `(384)` |  |
| PE_GAIN_STRENGTH | `(385)` |  |
| PE_GAIN_PERCEPTION | `(386)` |  |
| PE_GAIN_ENDURANCE | `(387)` |  |
| PE_GAIN_CHARISMA | `(388)` |  |
| PE_GAIN_INTELLIGENCE | `(389)` |  |
| PE_GAIN_AGILITY | `(390)` |  |
| PE_GAIN_LUCK | `(391)` |  |
| PE_HARMLESS | `(392)` |  |
| PE_HERE_AND_NOW | `(393)` |  |
| PE_HTH_EVADE | `(394)` |  |
| PE_KAMA_SUTRA_MASTER | `(395)` |  |
| PE_KARMA_BEACON | `(396)` |  |
| PE_LIGHT_STEP | `(397)` |  |
| PE_LIVING_ANATOMY | `(398)` |  |
| PE_MAGNETIC_PERSONALITY | `(399)` |  |
| PE_NEGOTIATOR | `(400)` |  |
| PE_PACK_RAT | `(401)` |  |
| PE_PYROMANIAC | `(402)` |  |
| PE_QUICK_RECOVERY | `(403)` |  |
| PE_SALESMAN | `(404)` |  |
| PE_STONEWALL | `(405)` |  |
| PE_THIEF | `(406)` |  |
| PE_WEAPON_HANDLING | `(407)` |  |
| PE_VAULT_CITY_TRAINING | `(408)` |  |
| PE_ALCOHOL_RAISED_HP | `(409)` |  |
| PE_ALCOHOL_RAISED_HP_II | `(410)` |  |
| PE_ALCOHOL_LOWERED_HP | `(411)` |  |
| PE_ALCOHOL_LOWERED_HP_II | `(412)` |  |
| PE_AUTODOC_RAISED_HP | `(413)` |  |
| PE_AUTODOC_RAISED_HP_II | `(414)` |  |
| PE_AUTODOC_LOWERED_HP | `(415)` |  |
| PE_AUTODOC_LOWERED_HP_II | `(416)` |  |
| PE_EXPERT_EXCREMENT | `(417)` |  |
| PE_WAY_OF_THE_FRUIT | `(418)` |  |
| PE_JINXED_II | `(419)` |  |
| PE_TERMINATOR | `(420)` |  |
| PE_TREE_TRUNK_THIGHS | `(421)` |  |
| PE_IRON_LIMBS | `(422)` |  |
| PE_MAN_OF_STEEL | `(423)` |  |
| PE_EVEN_MORE_CRITICALS | `(424)` |  |
| PE_RIGHT_BETWEEN_THE_EYES | `(425)` |  |
| PE_FAST_RELOAD | `(426)` |  |
| PE_SPRAY_AND_PRAY | `(427)` |  |
| PE_MORE_RANGED_DAMAGE | `(428)` |  |
| PE_LIVEWIRE | `(429)` |  |
| PE_GECKO_SKINNING | `(430)` |  |
| PE_VAULT_CITY_INOCULATIONS | `(431)` |  |
| PE_DERMAL_IMPACT | `(432)` |  |
| PE_DERMAL_IMPACT_ENH | `(433)` |  |
| PE_PHOENIX_IMPLANTS | `(434)` |  |
| PE_PHOENIX_IMPLANTS_ENH | `(435)` |  |
| PE_HTH_EVADE_II | `(436)` | 436..469 |
| PE_DODGER_II | `(437)` |  |
| PE_EVEN_TOUGHER | `(438)` |  |
| PE_HEALER_II | `(439)` |  |
| PE_BLESSED_ARE_THE_WEAK | `(440)` |  |
| PE_NIGHT_PERSON | `(441)` |  |
| PE_MELT_INTO_SHADOW | `(442)` |  |
| PE_BONUS_HTH_DAMAGE_II | `(443)` |  |
| PE_IN_YOUR_FACE | `(444)` |  |
| PE_HIT_THE_GAPS | `(445)` |  |
| PE_HTH_CRITICALS | `(446)` |  |
| PE_HEAVE_HO_II | `(447)` |  |
| PE_JUNK_MERCHANT | `(448)` |  |
| PE_BULK_TRADER | `(449)` |  |
| PE_SEX_APPEAL | `(450)` |  |
| PE_BORN_LEADER | `(451)` |  |
| PE_TRAPPER | `(452)` |  |
| PE_HAND_LOADER | `(453)` |  |
| PE_STEALTH_GIRL | `(454)` |  |
| PE_BEST_OF_A_BAD_LOT | `(455)` |  |
| PE_DISMANTLER | `(456)` |  |
| PE_VIGILANT_RECYCLER | `(457)` |  |
| PE_RETENTION | `(458)` |  |
| PE_TREASURE_HUNTER | `(459)` |  |
| PE_LOCKPICK_PERK_2 | `(460)` |  |
| PE_DEAD_MAN_WALKING | `(461)` |  |
| PE_NEMEAN_ARMOR | `(462)` |  |
| PE_IMP_STRENGTH | `(463)` |  |
| PE_IMP_PERCEPTION | `(464)` |  |
| PE_IMP_ENDURANCE | `(465)` |  |
| PE_IMP_CHARISMA | `(466)` |  |
| PE_IMP_INTELLIGENCE | `(467)` |  |
| PE_IMP_AGILITY | `(468)` |  |
| PE_IMP_LUCK | `(469)` |  |
| ADDICTION_COUNT | `(ADDICTION_END - ADDICTION_BEGIN + 1)` | Addictions |
| ADDICTION_NUKA_COLA | `(470)` |  |
| ADDICTION_BUFFOUT | `(471)` |  |
| ADDICTION_MENTATS | `(472)` |  |
| ADDICTION_PSYCHO | `(473)` |  |
| ADDICTION_RADAWAY | `(474)` |  |
| ADDICTION_JET | `(475)` |  |
| ADDICTION_TRAGIC | `(476)` |  |
| ADDICTION_CIGARETTES | `(477)` |  |
| ADDICTION_BEER | `(478)` |  |
| KARMA_COUNT | `(KARMA_END - KARMA_BEGIN + 1)` | Karma perks |
| KARMA_BERSERKER | `(480)` |  |
| KARMA_CHAMPION | `(481)` |  |
| KARMA_CHILDKILLER | `(482)` |  |
| KARMA_SEXPERT | `(483)` |  |
| KARMA_PRIZEFIGHTER | `(484)` |  |
| KARMA_GIGOLO | `(485)` |  |
| KARMA_GRAVE_DIGGER | `(486)` |  |
| KARMA_MARRIED | `(487)` |  |
| KARMA_PORN_STAR | `(488)` |  |
| KARMA_SLAVER | `(489)` |  |
| KARMA_VIRGIN_WASTES | `(490)` |  |
| KARMA_MAN_SALVATORE | `(491)` |  |
| KARMA_MAN_BISHOP | `(492)` |  |
| KARMA_MAN_MORDINO | `(493)` |  |
| KARMA_MAN_WRIGHT | `(494)` |  |
| KARMA_SEPARATED | `(495)` |  |
| KARMA_NCR_RANGER | `(496)` |  |
| DAMAGE_COUNT | `(DAMAGE_END - DAMAGE_BEGIN + 1)` | Damages |
| DAMAGE_EYE | `(502)` | FOClassic.fos #define DAMAGE_POISONED                          (500) // Used in engine FOClassic.fos #define DAMAGE_RADIATED                          (501) // Used in engine |
| MODE_BEGIN | `(510)` | Modes |
| MODE_END | `(549)` |  |
| MODE_COUNT | `(MODE_END - MODE_BEGIN + 1)` |  |
| MODE_NO_DROP | `(523)` | FOClassic.fos #define MODE_HIDE                                (510) // Состояние скрытности                                   Used in engine FOClassic.fos #define MODE_NO_STEAL                            (511) // Нельзя обворовать                                      Used in engine FOClassic.fos #define MODE_NO_BARTER                           (512) // Нельзя тоговать                                        Used in engine FOClassic.fos #define MODE_NO_ENEMY_STACK                      (513) // Нпц не запоминает врагов                               Used in engine FOClassic.fos #define MODE_NO_PVP                              (514) // Запрещает ПвП для игрока                               Used in engine FOClassic.fos #define MODE_END_COMBAT                          (515) // Согласен ли игрок закончить пошаговый бой              Used in engine FOClassic.fos #define MODE_DEFAULT_COMBAT                      (516) // Режим боя по-умолчанию                                 Used in engine FOClassic.fos #define MODE_NO_HOME                             (517) // Нпц не возвращается в домашнюю позицию автоматически   Used in engine FOClassic.fos #define MODE_GECK                                (518) // Локация не удаляется при наличии такого нпц            Used in engine FOClassic.fos #define MODE_NO_FAVORITE_ITEM                    (519) // Режим установки итемов по-умолчанию                    Used in engine FOClassic.fos #define MODE_NO_ITEM_GARBAGER                    (520) // Итемы не удаляются движком                             Used in engine FOClassic.fos #define MODE_DLG_SCRIPT_BARTER                   (521) // Возможно торговать при активном скрипте на диалоге     Used in engine FOClassic.fos #define MODE_UNLIMITED_AMMO                      (522) // Бесконечные патроны                                    Used in engine |
| MODE_NO_LOOSE_LIMBS | `(524)` |  |
| MODE_DEAD_AGES | `(525)` |  |
| MODE_NO_HEAL | `(526)` |  |
| MODE_SPECIAL_DEAD | `(529)` | FOClassic.fos #define MODE_INVULNERABLE                        (527) // Неуязвимый                                             Used in engine FOClassic.fos #define MODE_NO_FLATTEN                          (528) // Не помещать труп на задний план после смерти           Used in engine |
| MODE_NO_KNOCK | `(531)` | FOClassic.fos #define MODE_RANGE_HTH                           (530) // Возможна рукопашная атака на расстоянии                Used in engine |
| MODE_TRADER_ITEM_LEVELS | `(533)` | FOClassic.fos #define MODE_NO_LOOT                             (532) // Нельзя лутать                                          Used in engine |
| MODE_EXT | `(534)` |  |
| MODE_KILLER_ADMIN | `(535)` |  |
| MODE_NEGATE_CRIT_EFF | `(542)` | FOClassic.fos #define MODE_NO_PUSH                             (536) // Can't be pushed FOClassic.fos #define MODE_NO_UNARMED                          (537) FOClassic.fos #define MODE_NO_AIM                              (538) // Critter can't do aim attacks                           Hardcoded FOClassic.fos #define MODE_NO_WALK                             (539) // Critter can't walk                                     Hardcoded FOClassic.fos #define MODE_NO_RUN                              (540) // Critter can't run                                      Hardcoded FOClassic.fos #define MODE_NO_TALK                             (541) // Npc can't talk                                         Hardcoded |
| MODE_LAST_IP | `(543)` |  |
| MODE_LAST_WPN_MODE | `(544)` |  |
| MODE_EXT_NO_SLAVE | `(0x00000001)` | ext mode flags |
| MODE_EXT_NO_WALL_CHECK | `(0x00000002)` |  |
| MODE_EXT_MOB | `(0x00000004)` |  |
| MODE_EXT_GUARD | `(0x00000008)` |  |
| MODE_EXT_TRADER | `(0x00000010)` |  |
| MODE_EXT_FOLLOWER | `(0x00000020)` |  |
| MODE_EXT_PEN_BRAHMIN | `(0x00000040)` |  |
| MODE_EXT_SLAVE_HOSTILE | `(0x00000080)` |  |
| MODE_EXT_SLAVE_NORMAL | `(0x00000100)` |  |
| MODE_EXT_NO_DETERIORATION | `(0x00000200)` |  |
| MODE_EXT_EVENT | `(0x00000400)` |  |
| MODE_EXT_NO_ATTACK_AUTH | `(0x00000800)` |  |
| MODE_EXT_MILITIA | `(0x00001000)` |  |
| MODE_EXT_TC_LEADER | `(0x00002000)` |  |
| MODE_EXT_SLAVE | `(0x00004000)` |  |
| MODE_EXT_LOOK_ADMIN | `(0x00008000)` |  |
| MODE_EXT_LOOK_INVISIBLE | `(0x00010000)` |  |
| MODE_EXT_LOOK_ALWAYS_VISIBLE | `(0x00040000)` | don't use (0x00020000) |
| MODE_EXT_NO_HIT_ANIM | `(0x00080000)` |  |
| TRAIT_COUNT | `(TRAIT_END - TRAIT_BEGIN + 1)` | Traits |
| TRAIT_FAST_METABOLISM | `(550)` |  |
| TRAIT_BRUISER | `(551)` |  |
| TRAIT_ONE_HANDER | `(552)` |  |
| TRAIT_FINESSE | `(553)` |  |
| TRAIT_KAMIKAZE | `(554)` |  |
| TRAIT_HEAVY_HANDED | `(555)` |  |
| TRAIT_FAST_SHOT | `(556)` |  |
| TRAIT_BLOODY_MESS | `(557)` |  |
| TRAIT_JINXED | `(558)` |  |
| TRAIT_GOOD_NATURED | `(559)` |  |
| TRAIT_CHEM_RELIANT | `(560)` |  |
| TRAIT_BONEHEAD | `(561)` |  |
| TRAIT_SKILLED | `(562)` |  |
| TRAIT_LONER | `(563)` |  |
| ACHIEVEMENT_BEGIN | `(580)` |  |
| ACHIEVEMENT_END | `(587)` |  |
| REPUTATION_COUNT | `(REPUTATION_END - REPUTATION_BEGIN + 1)` | Reputation Used range in engine character screen __ReputationBegin..__ReputationEnd Remains with + as indexing from 0 is foreign dependency (team ids) |
| GOOD_EVIL_LIST_BEGIN | `(700)` | Good / Evil list |
| GOOD_EVIL_LIST_END | `(899)` |  |
| GOOD_EVIL_LIST_COUNT | `(GOOD_EVIL_LIST_END - GOOD_EVIL_LIST_BEGIN + 1)` |  |
| FOLLOWER_BEGIN | `(900)` |  |
| FOLLOWER_END | `(924)` |  |
| FV_BEGIN | `(925)` |  |
| FV_END | `(935)` |  |
| FV_MODE | `(925)` |  |
| FV_ATTACK_POLICY | `(926)` |  |
| FV_CLAIMABLE | `(927)` |  |
| FV_DISTANCE | `(928)` |  |
| FV_FACTION | `(929)` |  |
| FV_MERCID | `(930)` |  |
| FV_SPAWNMAP | `(931)` |  |
| FV_TYPE | `(932)` |  |
| FV_MASTER | `(933)` |  |
| FV_WM_IDLE | `(934)` |  |
| FV_WM_NEXT_TRY | `(935)` |  |
| FV_RESPAWN_PLACE | `(936)` |  |
| FV_LOYALITY | `(937)` |  |
| FV_LAST_DIALOG_ID | `(938)` |  |
| FV_DEFAULT_ARMOR | `(939)` |  |
| FV_WORN_ARMOR | `(940)` |  |
| FV_FLAGS | `(941)` |  |
| FV_RESPAWN_BASE_ID | `(942)` |  |
| FV_FLAG_MASTER_SPEAKER | `(0x1)` |  |
| FV_FLAG_FLED_BATTLE | `(0x2)` |  |
| ST_EX_IDX | `(999)` |  943..999  |
| PARAMS_COUNT | `(1000)` |  |
| AI_PLANE_PATROL | `(AI_PLANE_LAST+1)` | Planes types |
| AI_PLANE_COURIER | `(AI_PLANE_LAST+2)` |  |
| AI_PLANE_PATROL_PRIORITY | `(25)` | Planes default priority |
| AI_PLANE_COURIER_PRIORITY | `(30)` |  |
| PLANE_GOTO_EXIT | `(29)` | Plane identifiers |
| PLANE_LOOT | `(30)` |  |
| PLANE_LOOT_EX | `(31)` |  |
| PLANE_WANDER | `(32)` |  |
| PLANE_HEAL_CRITTER | `(33)` |  |
| PLANE_DOCTOR_CRITTER | `(34)` |  |
| PLANE_GOTO_TRANSFER | `(35)` |  |
| PLANE_PUSH_CRITTER | `(36)` |  |
| PLANE_FOLLOWER_GOTO_MASTER | `(37)` |  |
| PLANE_PICK_DROPPED_WPN | `(38)` |  |
| PLANE_FIRE_IN_THE_HOLE | `(39)` |  |
| PLANE_RETURN_WPN | `(40)` |  |
| PLANE_RAM_INTO_CRITTER | `(41)` |  |
| LOCKER_LOCKED | `(0x02)` | Locker #define LOCKER_ISOPEN                            (0x01) // Used in engine |
| LOCKER_JAMMED | `(0x04)` |  |
| LOCKER_BROKEN | `(0x08)` |  |
| LOCKER_ELECTRO | `(0x20)` | #define LOCKER_NOOPEN                            (0x10) // Hardcoded |
| TIMER_MIN_VALUE | `(1)` | Timer |
| TIMER_MAX_VALUE | `(599)` |  |
| FIRST_AID_TIMEOUT | `# (cr)     ( REAL_SECOND( (((cr.Skill[SK_FIRST_AID] > 50 ? cr.Skill[SK_FIRST_AID] : 50) * -6 / 10) + 210) / (cr.Perk[PE_MEDIC] > 0 ? 2 : 1)) )` | Timeouts in real seconds, generic values |
| DOCTOR_TIMEOUT | `# (cr)     ( REAL_SECOND( (((cr.Skill[SK_DOCTOR] > 50 ? cr.Skill[SK_DOCTOR] : 50) * -6 / 10) + 210) / (cr.Perk[PE_MEDIC] > 0 ? 2 : 1)) )` |  |
| REPAIR_TIMEOUT | `# (cr)        (REAL_MINUTE(1))` |  |
| SCIENCE_TIMEOUT | `# (cr)       (REAL_MINUTE(1))` |  |
| LOCKPICK_TIMEOUT | `# (cr)      (REAL_SECOND(15))` |  |
| STEAL_TIMEOUT | `# (cr)         (cr.Perk[PE_MASTER_THIEF] != 0 ? REAL_SECOND(15) : REAL_SECOND(30))` |  |
| TRANSFER_TIMEOUT | `# (cr)      (REAL_SECOND(30))` |  |
| WEAKENED_TIMEOUT | `# (cr)          (REAL_MINUTE((16 - Random(1, cr.Stat[ST_LUCK])) / 2))` |  |
| HEALING_TIMEOUT | `# (cr) (cr.Trait[TRAIT_FAST_METABOLISM] > 0 ? REAL_SECOND(30) : REAL_SECOND(60))` |  |
| IS_TURN_BASED_TIMEOUT | `# (cr) (cr.Timeout[TO_BATTLE] > 100000)` |  |
| MAXIMUM_TIMEOUT | `(10000000)` |  |
| SLEEPY_DEATH_IMMUNITY | `# (cr)     (REAL_SECOND(300))` |  |
| SLEEPY_BASE_IMMUNITY | `# (cr)      (REAL_SECOND(20))` |  |
| TOOL_TIMEOUT_DIV | `(2)` |  |
| SCORE_EVIL_OF_HOUR | `(0)` | Scores |
| SCORE_HERO_OF_HOUR | `(1)` |  |
| SCORE_KARMA_ON_HOUR | `(2)` |  |
| SCORE_ZOMBY | `(5)` | #define SCORE_SPEAKER                            (3) #define SCORE_TRADER                             (4) |
| SCORE_PATY | `(6)` |  |
| SCORE_MANIAC | `(7)` |  |
| SCORE_SCAUT | `(8)` |  |
| SCORE_DOCTOR | `(9)` |  |
| SCORE_SHOOTER | `(10)` |  |
| SCORE_MELEE | `(11)` |  |
| SCORE_UNARMED | `(12)` |  |
| SCORE_THIEF | `(13)` |  |
| SCORE_DRIVER | `(14)` |  |
| SCORE_KILLER | `(15)` |  |
| SCORE_SNIPER | `(16)` |  |
| SCORE_ADVENTURER | `(17)` |  |
| SCORE_CRACKER | `(18)` |  |
| SCORE_UNARMED_DAMAGE | `(19)` |  |
| SCORE_RITCH | `(20)` |  |
| SCORE_CHOSEN_ONE | `(21)` |  |
| SCORE_EXPERT_EXCREMENT | `(22)` |  |
| SCORE_ARMORER | `(23)` |  |
| SCORE_GUNSMITH | `(24)` |  |
| SCORE_TC_MODOC | `(30)` |  |
| SCORE_TC_KLAMATH | `(31)` |  |
| SCORE_TC_GECKO | `(32)` |  |
| SCORE_TC_BH | `(33)` |  |
| SCORE_TC_DEN | `(34)` |  |
| SCORE_TC_REDDING | `(35)` |  |
| SCORE_DOM_DAYGLOW | `(36)` |  |
| SCORE_BEST_MODOC | `(40)` |  |
| SCORE_BEST_KLAMATH | `(41)` |  |
| SCORE_BEST_GECKO | `(42)` |  |
| SCORE_BEST_BH | `(43)` |  |
| SCORE_BEST_DEN | `(44)` |  |
| SCORE_BEST_REDDING | `(45)` |  |
| SCORE_CATHEDRAL_CUR | `(46)` |  |
| SCORE_MARIPOSA_CUR | `(47)` |  |
| SCORE_SIERRA_CUR | `(48)` |  |
| SCORE_NCR_CUR | `(49)` |  |
| CAR_BIO_ENGINE | `(0x0001)` | Car flags |
| CAR_NO_LOCKPICK | `(0x0002)` |  |
| CAR_LOCKPICK_TIMEOUT | `(0x0004)` |  |
| BT_MEN | `(0)` | Body types |
| BT_WOMEN | `(1)` |  |
| BT_CHILDREN | `(2)` |  |
| BT_SUPER_MUTANT | `(3)` |  |
| BT_GHOUL | `(4)` |  |
| BT_BRAHMIN | `(5)` |  |
| BT_RADSCORPION | `(6)` |  |
| BT_RAT | `(7)` |  |
| BT_FLOATER | `(8)` |  |
| BT_CENTAUR | `(9)` |  |
| BT_ROBOT | `(10)` |  |
| BT_DOG | `(11)` |  |
| BT_MANTI | `(12)` |  |
| BT_DEADCLAW | `(13)` |  |
| BT_PLANT | `(14)` |  |
| BT_GECKO | `(15)` |  |
| BT_ALIEN | `(16)` |  |
| BT_GIANT_ANT | `(17)` |  |
| BT_BIG_BAD_BOSS | `(18)` |  |
| BT_DESERT_STALKER | `(19)` |  |
| BT_MAN_TRAP | `(20)` |  |
| BT_RAD_TOAD | `(21)` |  |
| BT_THORNSLINGER | `(22)` |  |
| BT_PASHTSHUUR | `(23)` |  |
| MAX_BODY_TYPES | `(24)` |  |
| LOCOMOTION_BIPED | `(0)` | Locomotion types |
| LOCOMOTION_QUADRUPED | `(1)` |  |
| LOCOMOTION_ROBOTIC | `(2)` |  |
| LOCOMOTION_FLY | `(3)` |  |
| FLUSH_SCREEN_DEFAULT | `(1000)` | Other |
| IS_DIALOG_END | `# (str)        (not valid(str))` | Dilalog functions |
| IS_DIALOG_GENERATED | `# (str)  (valid(str) && str.length() == 0)` |  |
| IS_DIALOG_SAY_MODE | `# (str)   (valid(str) && str.length() > 0)` |  |
| HOUR_MORNING | `(7)` | Time |
| HOUR_AFTERNOON | `(12)` |  |
| HOUR_EVENING | `(18)` |  |
| HOUR_NIGHT | `(22)` |  |
| IS_MORNING | `# (hour)	((hour) >= HOUR_MORNING && (hour) < HOUR_AFTERNOON)` |  |
| IS_AFTERNOON | `# (hour)	((hour) >= HOUR_AFTERNOON && (hour) < HOUR_EVENING)` |  |
| IS_EVENING | `# (hour)	((hour) >= HOUR_EVENING && (hour) < HOUR_NIGHT)` |  |
| IS_NIGHT | `# (hour)	((hour) >= HOUR_NIGHT || (hour) < HOUR_MORNING)` |  |
| MAX_BROKENS | `(100)` | Item deterioration info |
| BI_LOWBROKEN | `(0x01)` | Broken Information |
| BI_NORMBROKEN | `(0x02)` |  |
| BI_HIGHBROKEN | `(0x04)` |  |
| BI_NOTRESC | `(0x08)` |  |
| BI_SERVICE | `(0x10)` |  |
| BI_SERVICE_EXT | `(0x20)` |  |
| BI_ETERNAL | `(0x40)` |  |
| CRITTER_PLAYER | `(0x00010000)` | Critter extra flags, only for read |
| CRITTER_NPC | `(0x00020000)` |  |
| CRITTER_DISCONNECT | `(0x00080000)` |  |
| CRITTER_CHOSEN | `(0x00100000)` |  |
| CRITTER_RULEGROUP | `(0x00200000)` |  |
| SOUND_WEAPON | `'W'` | Sound types Generic <Type Subtype SoundId SoundIdExt X X X X> Weapon <Type Subtype SoundId SoundIdExt X X X [Random 1 or 2]> |
| SOUND_WEAPON_USE | `'A'` |  |
| SOUND_WEAPON_FLY | `'F'` |  |
| SOUND_WEAPON_MISS | `'H'` |  |
| SOUND_WEAPON_EMPTY | `'O'` |  |
| SOUND_WEAPON_RELOAD | `'R'` |  |
| SOUND_DOOR | `'S'` | Door <Type Subtype D O O R S SoundId> |
| SOUND_DOOR_OPEN | `'O'` |  |
| SOUND_DOOR_LOCK | `'L'` |  |
| SOUND_DOOR_CLOSE | `'C'` |  |
| SOUND_DOOR_NOT_OPEN | `'N'` |  |
| ELEVATOR_X | `# (elevator, current_level)((uint((current_level) & 0xFFFF) << 16) | (elevator) & 0xFFFF)` | Elevators |
| ELEVATOR_BOS_1234 | `# (current_level)         (ELEVATOR_X(0, current_level))` |  |
| ELEVATOR_BOS_01 | `# (current_level)           (ELEVATOR_X(1, current_level))` |  |
| ELEVATOR_MASTER_123 | `# (current_level)       (ELEVATOR_X(2, current_level))` |  |
| ELEVATOR_MASTER_34 | `# (current_level)        (ELEVATOR_X(3, current_level))` |  |
| ELEVATOR_MILITARY_123 | `# (current_level)     (ELEVATOR_X(4, current_level))` |  |
| ELEVATOR_MILITARY_34 | `# (current_level)      (ELEVATOR_X(5, current_level))` |  |
| ELEVATOR_MILITARY_346 | `# (current_level)     (ELEVATOR_X(6, current_level))` |  |
| ELEVATOR_MILITARY_456 | `# (current_level)     (ELEVATOR_X(7, current_level))` |  |
| ELEVATOR_VAULT_123 | `# (current_level)        (ELEVATOR_X(8, current_level))` |  |
| DIALOG_END | `uint(-1)` | Dialog links |
| DIALOG_BACK | `uint(-2)` |  |
| DIALOG_BARTER | `uint(-3)` |  |
| DIALOG_ATTACK | `uint(-4)` |  |
| REPLICATION_DELETE_FAST | `(-3)` |  |
| REPLICATION_DELETE | `(-2)` |  |
| REPLICATION_NEVER | `(-1)` |  |
| REPLICATION_DEFAULT | `(0)` |  |
| CRTYPE_MALE_DEFAULT | `(CRTYPE_MALE_VAULTSUIT)` | Critter base types |
| CRTYPE_FEMALE_DEFAULT | `(CRTYPE_FEMALE_JUMPSUIT)` |  |
| GLOBAL_PROCESS_MOVE | `(0)` | Global map events |
| GLOBAL_PROCESS_ENTER | `(1)` |  |
| GLOBAL_PROCESS_START_FAST | `(2)` |  |
| GLOBAL_PROCESS_START | `(3)` |  |
| GLOBAL_PROCESS_SET_MOVE | `(4)` |  |
| GLOBAL_PROCESS_STOPPED | `(5)` |  |
| GLOBAL_PROCESS_NPC_IDLE | `(6)` |  |
| GLOBAL_PROCESS_KICK | `(7)` |  |
| GLOBAL_MAP_BASE_SPEED | `(6.0f)` |  |
| AS_ALLOW_UNSAFE_REFERENCES | `(1)` | AngelScript properties |
| AS_OPTIMIZE_BYTECODE | `(2)` |  |
| AS_COPY_SCRIPT_SECTIONS | `(3)` |  |
| AS_MAX_STACK_SIZE | `(4)` |  |
| AS_USE_CHARACTER_LITERALS | `(5)` |  |
| AS_ALLOW_MULTILINE_STRINGS | `(6)` |  |
| AS_ALLOW_IMPLICIT_HANDLE_TYPES | `(7)` |  |
| AS_BUILD_WITHOUT_LINE_CUES | `(8)` |  |
| AS_INIT_GLOBAL_VARS_AFTER_BUILD | `(9)` |  |
| AS_REQUIRE_ENUM_SCOPE | `(10)` |  |
| AS_SCRIPT_SCANNER | `(11)` |  |
| AS_INCLUDE_JIT_INSTRUCTIONS | `(12)` |  |
| AS_STRING_ENCODING | `(13)` |  |
| LIGHT_DISABLE_DIR | `# (dir)       (1 << CLAMP(dir, 0, 5))` | Light flags |
| LIGHT_GLOBAL | `(0x40)` |  |
| LIGHT_INVERSE | `(0x80)` |  |
| RADIO_DISABLE_SHIFT_SEND | `(0x0100)` | Radio Flags, Item/ItemCl::RadioFlags |
| RADIO_DISABLE_SHIFT_RECV | `(0x0200)` |  |
| RADIO_DISABLE_SHIFT_BC_SEND | `(0x0400)` |  |
| RADIO_DISABLE_SHIFT_BC_RECV | `(0x0800)` |  |
| RADIO_DISABLE_SHIFT_CHANNEL | `(0x1000)` |  |
| CALIBER_NONE | `(0)` | Weapon calibers |
| CALIBER_ROCKET | `(1)` |  |
| CALIBER_FLAMETHROWER_FUEL | `(2)` |  |
| CALIBER_C_ENERGY_CELL | `(3)` |  |
| CALIBER_D_ENERGY_CELL | `(4)` |  |
| CALIBER_223 | `(5)` |  |
| CALIBER_5MM | `(6)` |  |
| CALIBER_40 | `(7)` |  |
| CALIBER_10MM | `(8)` |  |
| CALIBER_44 | `(9)` |  |
| CALIBER_14MM | `(10)` |  |
| CALIBER_12_GAUGE | `(11)` |  |
| CALIBER_9MM | `(12)` |  |
| CALIBER_BB | `(13)` |  |
| CALIBER_45 | `(14)` |  |
| CALIBER_2MM | `(15)` |  |
| CALIBER_4_7MM_CASELESS | `(16)` |  |
| CALIBER_HN_NEEDLER | `(17)` |  |
| CALIBER_7_62MM | `(18)` |  |
| CALIBER_22 | `(19)` |  |
| CALIBER_40MM_GRENADE | `(20)` |  |
| GEOMETRY_FALLOUT | `(0)` | Geometry |
| GEOMETRY_TACTICS | `(1)` |  |
| GEOMETRY_ARCANUM | `(2)` |  |
| IMAGE_RELIEF | `(0)` | Game images |
| ELEVATOR_BOS_1234 | `(0)` |  |
| ELEVATOR_BOS_01 | `(1)` |  |
| ELEVATOR_MASTER_123 | `(2)` |  |
| ELEVATOR_MASTER_34 | `(3)` |  |
| ELEVATOR_MILITARY_123 | `(4)` |  |
| ELEVATOR_MILITARY_34 | `(5)` |  |
| ELEVATOR_MILITARY_346 | `(6)` |  |
| ELEVATOR_MILITARY_456 | `(7)` |  |
| ELEVATOR_VAULT_123 | `(8)` |  |
| ELEVATOR_MILITARY_12 | `(9)` |  |
| MSG_DEBUG | `((2 ^ 32 - 1) / 2)` | debug message for npcs |
| ITEMTYPE_SMALL_GUNS | `(0)` | traders' item types |
| ITEMTYPE_BIG_GUNS | `(1)` |  |
| ITEMTYPE_ENERGY | `(2)` |  |
| ITEMTYPE_ARMOR | `(3)` |  |
| ITEMTYPE_DRUG | `(4)` |  |
| ITEMTYPE_MEDICINE | `(5)` |  |
| ITEMTYPE_MISC | `(6)` |  |
| ITEMTYPE_MAX | `(7)` |  |
| DIR_NE | `(0)` | Directions |
| DIR_E | `(1)` |  |
| DIR_SE | `(2)` |  |
| DIR_SW | `(3)` |  |
| DIR_W | `(4)` |  |
| DIR_NW | `(5)` |  |
| NPC_BASE_ID | `(5000000)` |  |
| MAX_ITEM_PROTOTYPES | `(30000)` |  |
| MAX_MAP_PROTOTYPES | `(30000)` |  |
| MAX_LOCATION_PROTOTYPES | `(30000)` |  |
| INJECTVALUE_CHEATS | `(0)` |  |
| INJECTVALUE_TRADER | `(1)` |  |
| INJECTVALUE_RECYCLING | `(2)` |  |
| INJECTVALUE_ROOMS | `(3)` |  |
| INJECTVALUE_REWARD | `(4)` |  |
| INJECTVALUE_LIMBO | `(5)` |  |
| PROFESSIONS_MAX | `(666)` |  |
| ITEMTRANSFER_ALL | `(0)` |  |
| ITEMTRANSFER_WEAPONS | `(1)` |  |
| FO2238 |  | for some shared scripts: |
| RELOADED |  |  |
| _TIMEBEGIN | `uint __nowZZZ = GetTick()` | ugly debug, deleteme! |
| _TIMEEND | `\` |  |
| WEEKDAY_SUNDAY | `(0)` |  |
| WEEKDAY_MONDAY | `(1)` |  |
| WEEKDAY_TUESDAY | `(2)` |  |
| WEEKDAY_WEDNESDAY | `(3)` |  |
| WEEKDAY_THURSTDAY | `(4)` |  |
| WEEKDAY_FRIDAY | `(5)` |  |
| WEEKDAY_SATURDAY | `(6)` |  |
| CRITTER_EVENT_EXT_INDEX_START | `(100)` | Extended methods |
| PLAYER_MAXIMUM_SIGHT | `(__LookNormal + 30 + 6)` | Maximum possible normal player's sight range |

## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| __endZZZ | `uint` | `GetTick()` |  |

