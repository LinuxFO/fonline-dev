---
title: FOClassic.fos
description: "//  FOClassic v7 Timestamp 06.03.2019  //  This file contains all exposed 'magic numbers' used in FOClassic. It should not be edited directly by game ..."
---

# FOClassic.fos

//

FOClassic v7
Timestamp 06.03.2019

//

This file contains all exposed 'magic numbers' used in FOClassic.
It should not be edited directly by game developers.

Used by engine, native extensions, and scripts.

//

FOCLASSIC_EXTENSION
Enables macros, C++ syntax; cannot be used with FOCLASSIC_SCRIPT.
Enables macros/values useful in C++ code only.

FOCLASSIC_SCRIPT
Enables macros, AngelScript syntax; cannot be used with FOCLASSIC_EXTENSION.
They're weirdly formatted currently; uncrustify cannot correctly handle "#" between "MACRO_NAME" and "()"

FOCLASSIC_BLEEDING_EDGE
All values which are planned for removal/renaming in future, or related to experimental features, won't be defined.

FOCLASSIC_SKIP_PARAM
Critter parameters indexes won't be defined.

FOCLASSIC_SKIP_PID
Items prototypes IDs won't be defined.

//

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __FOCLASSIC_FOS__ |  |  |
| SECTION_NONE | `""` |  |
| SECTION_CLIENT | `"Game Options"` |  |
| SECTION_MAPPER | `"Mapper"` |  |
| SECTION_SERVER | `"Server"` |  |
| SECTION_CLIENT_DX | `"ClientDX"` |  |
| SECTION_CLIENT_GL | `"ClientGL"` |  |
| SECTION_MAPPER_DX | `"MapperDX"` |  |
| SECTION_MAPPER_GL | `"MapperGL"` |  |
| SECTION_SERVER_DIALOGS | `"Dialogs"` |  |
| SECTION_SERVER_SCRIPTS | `"Scripts"` |  |
| SECTION_CLIENT_SCRIPTS_MODULES | `"Client scripts"` |  |
| SECTION_CLIENT_SCRIPTS_BINDS | `"Client binds"` |  |
| SECTION_MAPPER_SCRIPTS_MODULES | `"Mapper scripts"` |  |
| SECTION_MAPPER_SCRIPTS_BINDS | `"Mapper binds"` |  |
| SECTION_SERVER_SCRIPTS_MODULES | `"Server scripts"` |  |
| SECTION_SERVER_SCRIPTS_BINDS | `"Server binds"` |  |
| PI_FLOAT | `(3.14159265f)` |  |
| PI_VALUE | `(3.141592654f)` |  |
| PIBY2_FLOAT | `(1.5707963f)` |  |
| SQRT3T2_FLOAT | `(3.4641016151f)` |  |
| SQRT3_FLOAT | `(1.732050807568877f)` |  |
| BIAS_FLOAT | `(0.02f)` |  |
| RAD2DEG | `(57.29577951f)` |  |
| DIRS_COUNT | `(GAME_OPTION( MapHexagonal ) ? 6 : 8)` |  |
| LEXEMS_SIZE | `(128)` |  |
| MAX_UINT8 | `(0xFF)` |  |
| MAX_UINT16 | `(0xFFFF)` |  |
| MIN_INT | `(0x80000000)` |  |
| MAX_INT | `(0x7FFFFFFF)` |  |
| MAX_UINT | `(0xFFFFFFFF)` |  |
| MAX_FOPATH | `UTF8_BUF_SIZE( 1024 )` |  |
| MAX_FOTEXT | `UTF8_BUF_SIZE( 2048 )` |  |
| MAX_LOGTEXT | `UTF8_BUF_SIZE( 2048 )` |  |
| MIN_NAME | `(1)` | Used for name and password |
| MAX_NAME | `(30)` |  |
| MIN_AGE | `(14)` | Character registration |
| MAX_AGE | `(60)` |  |
| MAX_DETERIORATION | `(10000)` |  |
| MAX_HOLO_INFO | `(250)` |  |
| MAX_PROTO_CRITTERS | `(10000)` | Proto |
| MAX_PROTO_ITEMS | `(30000)` |  |
| MAX_PROTO_LOCATIONS | `(30000)` |  |
| MAX_PROTO_MAPS | `(30000)` |  |
| MAX_SCRIPT_NAME | `(64)` |  |
| MAX_STORED_LOCATIONS | `(1000)` |  |
| MIN_ZOOM | `(0.2f)` |  |
| MAX_ZOOM | `(10.0f)` |  |
| ACCESS_CLIENT | `(0)` | Access levels |
| ACCESS_TESTER | `(1)` |  |
| ACCESS_MODER | `(2)` |  |
| ACCESS_ADMIN | `(3)` |  |
| ACCESS_LAST | `(ACCESS_ADMIN)` |  |
| AI_PLANE_MISC | `(0)` | AI Planes |
| AI_PLANE_ATTACK | `(1)` |  |
| AI_PLANE_WALK | `(2)` |  |
| AI_PLANE_PICK | `(3)` |  |
| AI_PLANE_LAST | `(AI_PLANE_PICK)` |  |
| AI_PLANE_MISC_PRIORITY | `(10)` | AI Planes priorities |
| AI_PLANE_ATTACK_PRIORITY | `(50)` |  |
| AI_PLANE_WALK_PRIORITY | `(20)` |  |
| AI_PLANE_PICK_PRIORITY | `(35)` |  |
| ANIM_TYPE_FALLOUT | `(0)` | Animation |
| ANIM_TYPE_3D | `(1)` |  |
| ANIM_TYPE_LAST | `(ANIM_TYPE_3D)` |  |
| ANIM1_UNARMED | `(1)` | Anim1 |
| ANIM2_IDLE | `(1)` | Anim2 |
| ANIM2_WALK | `(3)` |  |
| ANIM2_LIMP | `(4)` |  |
| ANIM2_RUN | `(5)` |  |
| ANIM2_PANIC_RUN | `(6)` |  |
| ANIM2_SNEAK_WALK | `(7)` |  |
| ANIM2_SNEAK_RUN | `(8)` |  |
| ANIM2_IDLE_PRONE_FRONT | `(86)` |  |
| ANIM2_IDLE_PRONE_BACK | `(87)` |  |
| ANIM2_DEAD_FRONT | `(102)` |  |
| ANIM2_DEAD_BACK | `(103)` |  |
| ANGELSCRIPT_ALLOW_UNSAFE_REFERENCES | `(1)` | AngelScript properties |
| ANGELSCRIPT_OPTIMIZE_BYTECODE | `(2)` |  |
| ANGELSCRIPT_COPY_SCRIPT_SECTIONS | `(3)` |  |
| ANGELSCRIPT_MAX_STACK_SIZE | `(4)` |  |
| ANGELSCRIPT_USE_CHARACTER_LITERALS | `(5)` |  |
| ANGELSCRIPT_ALLOW_MULTILINE_STRINGS | `(6)` |  |
| ANGELSCRIPT_ALLOW_IMPLICIT_HANDLE_TYPES | `(7)` |  |
| ANGELSCRIPT_BUILD_WITHOUT_LINE_CUES | `(8)` |  |
| ANGELSCRIPT_INIT_GLOBAL_VARS_AFTER_BUILD | `(9)` |  |
| ANGELSCRIPT_REQUIRE_ENUM_SCOPE | `(10)` |  |
| ANGELSCRIPT_SCRIPT_SCANNER | `(11)` |  |
| ANGELSCRIPT_INCLUDE_JIT_INSTRUCTIONS | `(12)` |  |
| ANGELSCRIPT_STRING_ENCODING | `(13)` |  |
| ANGELSCRIPT_PROPERTY_ACCESSOR_MODE | `(14)` |  |
| ANGELSCRIPT_EXPAND_DEF_ARRAY_TO_TMPL | `(15)` |  |
| ANGELSCRIPT_AUTO_GARBAGE_COLLECT | `(16)` |  |
| ANGELSCRIPT_DISALLOW_GLOBAL_VARS | `(17)` |  |
| ANGELSCRIPT_ALWAYS_IMPL_DEFAULT_CONSTRUCT | `(18)` |  |
| ANGELSCRIPT_COMPILER_WARNINGS | `(19)` |  |
| ANGELSCRIPT_DISALLOW_VALUE_ASSIGN_FOR_REF_TYPE | `(20)` |  |
| BI_BROKEN | `(0x0F)` | Item deterioration info |
| BINARY_TYPE_CLIENTSAVE | `'C'` |  |
| BINARY_TYPE_MAPSAVE | `'M'` |  |
| BINARY_TYPE_PROFILERSAVE | `'P'` |  |
| BINARY_TYPE_SCRIPTSAVE | `'S'` |  |
| BINARY_TYPE_WORLDSAVE | `'W'` |  |
| BINARY_TYPE_CACHE | `'c'` |  |
| CHOSEN_NONE | `(0)` | Chosen actions |
| CHOSEN_MOVE | `(1)` |  |
| CHOSEN_MOVE_TO_CRITTER | `(2)` |  |
| CHOSEN_DIR | `(3)` |  |
| CHOSEN_SHOW_ITEM | `(4)` |  |
| CHOSEN_HIDE_ITEM | `(5)` |  |
| CHOSEN_USE_ITEM | `(6)` |  |
| CHOSEN_MOVE_ITEM | `(7)` |  |
| CHOSEN_MOVE_ITEM_CONTAINER | `(8)` |  |
| CHOSEN_TAKE_ALL | `(9)` |  |
| CHOSEN_USE_SKILL_ON_CRITTER | `(10)` |  |
| CHOSEN_USE_SKILL_ON_ITEM | `(11)` |  |
| CHOSEN_USE_SKILL_ON_SCENERY | `(12)` |  |
| CHOSEN_TALK_NPC | `(13)` |  |
| CHOSEN_PICK_ITEM | `(14)` |  |
| CHOSEN_PICK_CRITTER | `(15)` |  |
| CHOSEN_WRITE_HOLODISK | `(16)` |  |
| CLIENT_SCREEN_NONE | `(0)` | Hardcoded screens |
| CLIENT_MAIN_SCREEN_LOGIN | `(1)` | Hardcoded screens, primary |
| CLIENT_MAIN_SCREEN_REGISTRATION | `(2)` |  |
| CLIENT_MAIN_SCREEN_CREDITS | `(3)` |  |
| CLIENT_MAIN_SCREEN_OPTIONS | `(4)` |  |
| CLIENT_MAIN_SCREEN_GAME | `(5)` |  |
| CLIENT_MAIN_SCREEN_WORLDMAP | `(6)` |  |
| CLIENT_MAIN_SCREEN_WAIT | `(7)` |  |
| CLIENT_SCREEN_INVENTORY | `(10)` | Hardcoded screens, secondary |
| CLIENT_SCREEN_PICKUP | `(11)` |  |
| CLIENT_SCREEN_MINIMAP | `(12)` |  |
| CLIENT_SCREEN_CHARACTER | `(13)` |  |
| CLIENT_SCREEN_DIALOG | `(14)` |  |
| CLIENT_SCREEN_BARTER | `(15)` |  |
| CLIENT_SCREEN_PIPBOY | `(16)` |  |
| CLIENT_SCREEN_FIXBOY | `(17)` |  |
| CLIENT_SCREEN_MENU | `(18)` |  |
| CLIENT_SCREEN_AIM | `(19)` |  |
| CLIENT_SCREEN_SPLIT | `(20)` |  |
| CLIENT_SCREEN_TIMER | `(21)` |  |
| CLIENT_SCREEN_DIALOGBOX | `(22)` |  |
| CLIENT_SCREEN_ELEVATOR | `(23)` |  |
| CLIENT_SCREEN_SAY | `(24)` |  |
| CLIENT_SCREEN_CHAR_NAME | `(25)` |  |
| CLIENT_SCREEN_CHAR_AGE | `(26)` |  |
| CLIENT_SCREEN_CHAR_SEX | `(27)` |  |
| CLIENT_SCREEN_WM_TOWN | `(28)` |  |
| CLIENT_SCREEN_INPUTBOX | `(29)` |  |
| CLIENT_SCREEN_SKILLBOX | `(30)` |  |
| CLIENT_SCREEN_USE | `(31)` |  |
| CLIENT_SCREEN_PERK | `(32)` |  |
| CLIENT_SCREEN_WM_TOWNVIEW | `(33)` |  |
| CLIENT_SCREEN_LOADSAVE | `(34)` |  |
| CLIENT_SCREEN_LAST | `(CLIENT_SCREEN_LOADSAVE)` |  |
| COLOR_IFACE_FIX | `COLOR_XRGB( 103, 95, 86 )` |  |
| COLOR_CRITTER_NAME | `COLOR_XRGB( 0xAD, 0xAD, 0xB9 )` |  |
| COLOR_TEXT | `COLOR_XRGB( 60, 248, 0 )` |  |
| COLOR_TEXT_WHITE | `COLOR_XRGB( 0xFF, 0xFF, 0xFF )` |  |
| COLOR_TEXT_DWHITE | `COLOR_XRGB( 0xBF, 0xBF, 0xBF )` |  |
| COLOR_TEXT_RED | `COLOR_XRGB( 0xC8, 0, 0 )` |  |
| COLOR_TEXT_DRED | `COLOR_XRGB( 0xAA, 0, 0 )` |  |
| COLOR_TEXT_DDRED | `COLOR_XRGB( 0x66, 0, 0 )` |  |
| COLOR_TEXT_LRED | `COLOR_XRGB( 0xFF, 0, 0 )` |  |
| COLOR_TEXT_BLUE | `COLOR_XRGB( 0, 0, 0xC8 )` |  |
| COLOR_TEXT_DBLUE | `COLOR_XRGB( 0, 0, 0xAA )` |  |
| COLOR_TEXT_LBLUE | `COLOR_XRGB( 0, 0, 0xFF )` |  |
| COLOR_TEXT_GREEN | `COLOR_XRGB( 0, 0xC8, 0 )` |  |
| COLOR_TEXT_DGREEN | `COLOR_XRGB( 0, 0xAA, 0 )` |  |
| COLOR_TEXT_DDGREEN | `COLOR_XRGB( 0, 0x66, 0 )` |  |
| COLOR_TEXT_LGREEN | `COLOR_XRGB( 0, 0xFF, 0 )` |  |
| COLOR_TEXT_BLACK | `COLOR_XRGB( 0, 0, 0 )` |  |
| COLOR_TEXT_SBLACK | `COLOR_XRGB( 0x10, 0x10, 0x10 )` |  |
| COLOR_TEXT_DARK | `COLOR_XRGB( 0x30, 0x30, 0x30 )` |  |
| COLOR_TEXT_GREEN_RED | `COLOR_XRGB( 0, 0xC8, 0xC8 )` |  |
| COLOR_TEXT_SAND | `COLOR_XRGB( 0x8F, 0x6F, 0 )` |  |
| COMMAND_EXIT | `(1)` | Commands |
| COMMAND_CHANGE_PASSWORD | `(2)` |  |
| COMMAND_DELETE_ACCOUNT | `(3)` |  |
| COMMAND_MYINFO | `(4)` |  |
| COMMAND_GETACCESS | `(5)` |  |
| COMMAND_PARAM | `(6)` |  |
| COMMAND_GAMEINFO | `(7)` |  |
| COMMAND_DROP_UID | `(8)` |  |
| COMMAND_CRITID | `(9)` |  |
| COMMAND_MOVECRIT | `(10)` |  |
| COMMAND_KILLCRIT | `(11)` |  |
| COMMAND_DISCONCRIT | `(12)` |  |
| COMMAND_TOGLOBAL | `(13)` |  |
| COMMAND_RESPAWN | `(14)` |  |
| COMMAND_LOG | `(15)` |  |
| COMMAND_BAN | `(16)` |  |
| COMMAND_ADDITEM | `(17)` |  |
| COMMAND_ADDITEM_SELF | `(18)` |  |
| COMMAND_ADDNPC | `(19)` |  |
| COMMAND_ADDLOCATION | `(20)` |  |
| COMMAND_LOADSCRIPT | `(21)` |  |
| COMMAND_RELOADSCRIPTS | `(22)` |  |
| COMMAND_RELOAD_CLIENT_SCRIPTS | `(23)` |  |
| COMMAND_RUNSCRIPT | `(24)` |  |
| COMMAND_LOADLOCATION | `(25)` |  |
| COMMAND_RELOADLOCATIONS | `(26)` |  |
| COMMAND_LOADMAP | `(27)` |  |
| COMMAND_RELOADMAPS | `(28)` |  |
| COMMAND_REGENMAP | `(29)` |  |
| COMMAND_LOADDIALOG | `(30)` |  |
| COMMAND_RELOADDIALOGS | `(31)` |  |
| COMMAND_RELOADTEXTS | `(32)` |  |
| COMMAND_RELOADAI | `(33)` |  |
| COMMAND_CHECKVAR | `(34)` |  |
| COMMAND_SETVAR | `(35)` |  |
| COMMAND_SETTIME | `(36)` |  |
| COMBAT_MODE_ANY | `(0)` | Combat modes |
| COMBAT_MODE_REAL_TIME | `(1)` |  |
| COMBAT_MODE_TURN_BASED | `(2)` |  |
| CONSTANTS_PARAM | `(0)` | Constants collections |
| CONSTANTS_ITEM | `(1)` |  |
| CONSTANTS_DEFINE | `(2)` |  |
| CONSTANTS_PICTURE | `(3)` |  |
| CONSTANTS_HASH | `(4)` |  |
| CONTAINER_GET | `(1)` | Take flags |
| CONTAINER_PUT | `(2)` |  |
| CONTAINER_GETALL | `(3)` |  |
| CONTAINER_PUTALL | `(4)` |  |
| CONTOUR_RED | `(1)` | Contour types |
| CONTOUR_YELLOW | `(2)` |  |
| CONTOUR_CUSTOM | `(3)` |  |
| CORNER_NORTH_SOUTH | `(0)` | Corner type |
| CORNER_WEST | `(1)` |  |
| CORNER_EAST | `(2)` |  |
| CORNER_SOUTH | `(3)` |  |
| CORNER_NORTH | `(4)` |  |
| CORNER_EAST_WEST | `(5)` |  |
| CRITTER_ACTION_MOVE | `(0)` | Critter actions  investigate: CRITTER_ACTION_RUN, CRITTER_ACTION_DODGE, CRITTER_ACTION_DAMAGE, CRITTER_ACTION_DAMAGE  Flags for chosen: l - hardcoded local call s - hardcoded server call for all others critters actions call only server  |
| CRITTER_ACTION_RUN | `(1)` |  |
| CRITTER_ACTION_MOVE_ITEM | `(2)` |  |
| CRITTER_ACTION_MOVE_ITEM_SWAP | `(3)` |  |
| CRITTER_ACTION_USE_ITEM | `(4)` |  |
| CRITTER_ACTION_DROP_ITEM | `(5)` |  |
| CRITTER_ACTION_USE_WEAPON | `(6)` |  |
| CRITTER_ACTION_RELOAD_WEAPON | `(7)` |  |
| CRITTER_ACTION_USE_SKILL | `(8)` |  |
| CRITTER_ACTION_PICK_ITEM | `(9)` |  |
| CRITTER_ACTION_PICK_CRITTER | `(10)` |  |
| CRITTER_ACTION_OPERATE_CONTAINER | `(11)` |  |
| CRITTER_ACTION_BARTER | `(12)` |  |
| CRITTER_ACTION_DODGE | `(13)` |  |
| CRITTER_ACTION_DAMAGE | `(14)` |  |
| CRITTER_ACTION_DAMAGE_FORCE | `(15)` |  |
| CRITTER_ACTION_KNOCKOUT | `(16)` |  |
| CRITTER_ACTION_STANDUP | `(17)` |  |
| CRITTER_ACTION_FIDGET | `(18)` |  |
| CRITTER_ACTION_DEAD | `(19)` |  |
| CRITTER_ACTION_CONNECT | `(20)` |  |
| CRITTER_ACTION_DISCONNECT | `(21)` |  |
| CRITTER_ACTION_RESPAWN | `(22)` |  |
| CRITTER_ACTION_REFRESH | `(23)` |  |
| CRITTER_CONDITION_LIFE | `(1)` | Critter conditions |
| CRITTER_CONDITION_KNOCKOUT | `(2)` |  |
| CRITTER_CONDITION_DEAD | `(3)` |  |
| CRITTER_EVENT_IDLE | `(0)` | Critter events |
| CRITTER_EVENT_FINISH | `(1)` |  |
| CRITTER_EVENT_DEAD | `(2)` |  |
| CRITTER_EVENT_RESPAWN | `(3)` |  |
| CRITTER_EVENT_SHOW_CRITTER | `(4)` |  |
| CRITTER_EVENT_SHOW_CRITTER_1 | `(5)` |  |
| CRITTER_EVENT_SHOW_CRITTER_2 | `(6)` |  |
| CRITTER_EVENT_SHOW_CRITTER_3 | `(7)` |  |
| CRITTER_EVENT_HIDE_CRITTER | `(8)` |  |
| CRITTER_EVENT_HIDE_CRITTER_1 | `(9)` |  |
| CRITTER_EVENT_HIDE_CRITTER_2 | `(10)` |  |
| CRITTER_EVENT_HIDE_CRITTER_3 | `(11)` |  |
| CRITTER_EVENT_SHOW_ITEM_ON_MAP | `(12)` |  |
| CRITTER_EVENT_CHANGE_ITEM_ON_MAP | `(13)` |  |
| CRITTER_EVENT_HIDE_ITEM_ON_MAP | `(14)` |  |
| CRITTER_EVENT_ATTACK | `(15)` |  |
| CRITTER_EVENT_ATTACKED | `(16)` |  |
| CRITTER_EVENT_STEALING | `(17)` |  |
| CRITTER_EVENT_MESSAGE | `(18)` |  |
| CRITTER_EVENT_USE_ITEM | `(19)` |  |
| CRITTER_EVENT_USE_ITEM_ON_ME | `(20)` |  |
| CRITTER_EVENT_USE_SKILL | `(21)` |  |
| CRITTER_EVENT_USE_SKILL_ON_ME | `(22)` |  |
| CRITTER_EVENT_DROP_ITEM | `(23)` |  |
| CRITTER_EVENT_MOVE_ITEM | `(24)` |  |
| CRITTER_EVENT_KNOCKOUT | `(25)` |  |
| CRITTER_EVENT_SMTH_DEAD | `(26)` |  |
| CRITTER_EVENT_SMTH_STEALING | `(27)` |  |
| CRITTER_EVENT_SMTH_ATTACK | `(28)` |  |
| CRITTER_EVENT_SMTH_ATTACKED | `(29)` |  |
| CRITTER_EVENT_SMTH_USE_ITEM | `(30)` |  |
| CRITTER_EVENT_SMTH_USE_SKILL | `(31)` |  |
| CRITTER_EVENT_SMTH_DROP_ITEM | `(32)` |  |
| CRITTER_EVENT_SMTH_MOVE_ITEM | `(33)` |  |
| CRITTER_EVENT_SMTH_KNOCKOUT | `(34)` |  |
| CRITTER_EVENT_PLANE_BEGIN | `(35)` |  |
| CRITTER_EVENT_PLANE_END | `(36)` |  |
| CRITTER_EVENT_PLANE_RUN | `(37)` |  |
| CRITTER_EVENT_BARTER | `(38)` |  |
| CRITTER_EVENT_TALK | `(39)` |  |
| CRITTER_EVENT_GLOBAL_PROCESS | `(40)` |  |
| CRITTER_EVENT_GLOBAL_INVITE | `(41)` |  |
| CRITTER_EVENT_TURN_BASED_PROCESS | `(42)` |  |
| CRITTER_EVENT_SMTH_TURN_BASED_PROCESS | `(43)` |  |
| CRITTER_EVENT_MAX | `(44)` |  |
| CRITTER_FLAG_PLAYER | `(0x00010000)` | Critters flags |
| CRITTER_FLAG_NPC | `(0x00020000)` |  |
| CRITTER_FLAG_DISCONNECT | `(0x00080000)` |  |
| CRITTER_FLAG_CHOSEN | `(0x00100000)` |  |
| CRITTER_FLAG_RULEGROUP | `(0x00200000)` |  |
| CRITTER_ID_START_PLAYER | `(1)` | Critters ID |
| CRITTER_ID_START_NPC | `(5000001)` |  |
| CRITTER_LOOK_NAME | `(0)` | Critter description |
| CRITTER_LOOK_SHORT | `(1)` |  |
| CRITTER_LOOK_FULL | `(2)` |  |
| CURSOR_DEFAULT | `(0)` | Cur modes |
| CURSOR_MOVE | `(1)` |  |
| CURSOR_USE_ITEM | `(2)` |  |
| CURSOR_USE_WEAPON | `(3)` |  |
| CURSOR_USE_SKILL | `(4)` |  |
| CURSOR_WAIT | `(5)` |  |
| CURSOR_HAND | `(6)` |  |
| DAMAGE_TYPE_UNCALLED | `(0)` | Damage types |
| DAMAGE_TYPE_NORMAL | `(1)` |  |
| DAMAGE_TYPE_LASER | `(2)` |  |
| DAMAGE_TYPE_FIRE | `(3)` |  |
| DAMAGE_TYPE_PLASMA | `(4)` |  |
| DAMAGE_TYPE_ELECTR | `(5)` |  |
| DAMAGE_TYPE_EMP | `(6)` |  |
| DAMAGE_TYPE_EXPLODE | `(7)` |  |
| DESC_INVENTORY_MAIN | `(0)` | Inventory descriptions |
| DESC_INVENTORY_SPECIAL | `(1)` |  |
| DESC_INVENTORY_STATS | `(2)` |  |
| DESC_INVENTORY_RESIST | `(3)` |  |
| DRAW_PRIMITIVE_POINTLIST | `(1)` | Primitives |
| DRAW_PRIMITIVE_LINELIST | `(2)` |  |
| DRAW_PRIMITIVE_LINESTRIP | `(3)` |  |
| DRAW_PRIMITIVE_TRIANGLELIST | `(4)` |  |
| DRAW_PRIMITIVE_TRIANGLESTRIP | `(5)` |  |
| DRAW_PRIMITIVE_TRIANGLEFAN | `(6)` |  |
| ENTIRE_DEFAULT | `(0)` | Entires |
| ENTIRE_LOG_OUT | `(241)` |  |
| FIND_LIFE | `(0x01)` | Critter finding flags |
| FIND_KO | `(0x02)` |  |
| FIND_DEAD | `(0x04)` |  |
| FIND_ONLY_PLAYERS | `(0x10)` |  |
| FIND_ONLY_NPC | `(0x20)` |  |
| FIXBOY_LIST | `(0)` | FixBoy function call states |
| FIXBOY_BUTTON | `(1)` |  |
| FIXBOY_CRAFT | `(2)` |  |
| FIXBOY_ALLOW_CRAFT | `(0x0001)` | FixBoy craft results |
| FIXBOY_CHECK_TIMEOUT | `(0x0002)` |  |
| FIXBOY_SET_TIMEOUT | `(0x0004)` |  |
| FIXBOY_CHECK_PARAMS | `(0x0008)` |  |
| FIXBOY_CHECK_MATERIALS | `(0x0010)` |  |
| FIXBOY_CHECK_TOOLS | `(0x0020)` |  |
| FIXBOY_SUB_MATERIALS | `(0x0040)` |  |
| FIXBOY_ADD_CRAFT_ITEMS | `(0x0080)` |  |
| FIXBOY_ADD_EXPERIENCE | `(0x0100)` |  |
| FIXBOY_SEND_SUCC_MESSAGE | `(0x0200)` |  |
| FIXBOY_SEND_FAIL_MESSAGE | `(0x0400)` |  |
| FIXBOY_DEFAULT | `(0xFFFF)` |  |
| FONT_FLAG_NOBREAK | `(0x0001)` | Font flags |
| FONT_FLAG_NOBREAK_LINE | `(0x0002)` |  |
| FONT_FLAG_CENTERX | `(0x0004)` |  |
| FONT_FLAG_CENTERY | `(0x0008)` |  |
| FONT_FLAG_CENTERR | `(0x0010)` |  |
| FONT_FLAG_BOTTOM | `(0x0020)` |  |
| FONT_FLAG_UPPER | `(0x0040)` |  |
| FONT_FLAG_NO_COLORIZE | `(0x0080)` |  |
| FONT_FLAG_ALIGN | `(0x0100)` |  |
| FONT_FLAG_BORDERED | `(0x0200)` |  |
| FONT_TYPE_FO | `(0)` | Fonts |
| FONT_TYPE_NUM | `(1)` |  |
| FONT_TYPE_BIG_NUM | `(2)` |  |
| FONT_TYPE_SAND_NUM | `(3)` |  |
| FONT_TYPE_SPECIAL | `(4)` |  |
| FONT_TYPE_DEFAULT | `(5)` |  |
| FONT_TYPE_THIN | `(6)` |  |
| FONT_TYPE_FAT | `(7)` |  |
| FONT_TYPE_BIG | `(8)` |  |
| FONT_TYPE_DIALOG | `(9)` | Additional fonts |
| GENDER_MALE | `(0)` |  |
| GENDER_FEMALE | `(1)` |  |
| GRID_EXITGRID | `(1)` | Grid Types |
| GRID_STAIRS | `(2)` |  |
| GRID_LADDERBOT | `(3)` |  |
| GRID_LADDERTOP | `(4)` |  |
| GRID_ELEVATOR | `(5)` |  |
| HEX_FLAG_BLOCK | `BIN8( 00000001 )` | Hex flags |
| HEX_FLAG_NOTRAKE | `BIN8( 00000010 )` |  |
| HEX_FLAG_WALL | `BIN8( 00000100 )` |  |
| HEX_FLAG_SCEN | `BIN8( 00001000 )` |  |
| HEX_FLAG_SCEN_GRID | `BIN8( 00010000 )` |  |
| HEX_FLAG_TRIGGER | `BIN8( 00100000 )` |  |
| HEX_FLAG_CRITTER | `BIN8( 00000001 )` |  |
| HEX_FLAG_DEAD_CRITTER | `BIN8( 00000010 )` |  |
| HEX_FLAG_ITEM | `BIN8( 00000100 )` |  |
| HEX_FLAG_DOOR | `BIN8( 00001000 )` |  |
| HEX_FLAG_BLOCK_ITEM | `BIN8( 00010000 )` |  |
| HEX_FLAG_NRAKE_ITEM | `BIN8( 00100000 )` |  |
| HEX_FLAG_WALK_ITEM | `BIN8( 01000000 )` |  |
| HEX_FLAG_GAG_ITEM | `BIN8( 10000000 )` |  |
| HEX_FLAG_NOWAY | `BIN16( 00010001, 00000001 )` |  |
| HEX_FLAG_NOSHOOT | `BIN16( 00100000, 00000010 )` |  |
| HIT_LOCATION_NONE | `(0)` | Hit locations |
| HIT_LOCATION_HEAD | `(1)` |  |
| HIT_LOCATION_LEFT_ARM | `(2)` |  |
| HIT_LOCATION_RIGHT_ARM | `(3)` |  |
| HIT_LOCATION_TORSO | `(4)` |  |
| HIT_LOCATION_RIGHT_LEG | `(5)` |  |
| HIT_LOCATION_LEFT_LEG | `(6)` |  |
| HIT_LOCATION_EYES | `(7)` |  |
| HIT_LOCATION_GROIN | `(8)` |  |
| HIT_LOCATION_UNCALLED | `(9)` |  |
| HIT_LOCATION_MAX | `(HIT_LOCATION_UNCALLED)` |  |
| INDICATOR_LINES | `(0)` | IndicatorType |
| INDICATOR_NUMBERS | `(1)` |  |
| INDICATOR_BOTH | `(2)` |  |
| ITEM_ACCESSORY_NONE | `(0)` | Accessory |
| ITEM_ACCESSORY_CRITTER | `(1)` |  |
| ITEM_ACCESSORY_HEX | `(2)` |  |
| ITEM_ACCESSORY_CONTAINER | `(3)` |  |
| ITEM_COLLECTION_INVENTORY | `(0)` | Items collections |
| ITEM_COLLECTION_USE | `(1)` |  |
| ITEM_COLLECTION_BARTER | `(2)` |  |
| ITEM_COLLECTION_BARTER_OFFER | `(3)` |  |
| ITEM_COLLECTION_BARTER_OPPONENT | `(4)` |  |
| ITEM_COLLECTION_BARTER_OPPONENT_OFFER | `(5)` |  |
| ITEM_COLLECTION_PICKUP | `(6)` |  |
| ITEM_COLLECTION_PICKUP_FROM | `(7)` |  |
| ITEM_DATA_MASK_CHOSEN | `(0)` | Item data masks |
| ITEM_DATA_MASK_CRITTER | `(1)` |  |
| ITEM_DATA_MASK_CRITTER_EXT | `(2)` |  |
| ITEM_DATA_MASK_CONTAINER | `(3)` |  |
| ITEM_DATA_MASK_MAP | `(4)` |  |
| ITEM_DATA_MASK_MAX | `(ITEM_DATA_MASK_MAP + 1)` |  |
| ITEM_EVENT_FINISH | `(0)` | Item events |
| ITEM_EVENT_ATTACK | `(1)` |  |
| ITEM_EVENT_USE | `(2)` |  |
| ITEM_EVENT_USE_ON_ME | `(3)` |  |
| ITEM_EVENT_SKILL | `(4)` |  |
| ITEM_EVENT_DROP | `(5)` |  |
| ITEM_EVENT_MOVE | `(6)` |  |
| ITEM_EVENT_WALK | `(7)` |  |
| ITEM_EVENT_MAX | `(ITEM_EVENT_WALK + 1)` |  |
| ITEM_FLAG_HIDDEN | `(0x00000001)` | Item flags |
| ITEM_FLAG_FLAT | `(0x00000002)` |  |
| ITEM_FLAG_NO_BLOCK | `(0x00000004)` |  |
| ITEM_FLAG_SHOOT_THRU | `(0x00000008)` |  |
| ITEM_FLAG_LIGHT_THRU | `(0x00000010)` |  |
| ITEM_FLAG_MULTI_HEX | `(0x00000020)` |  |
| ITEM_FLAG_WALL_TRANS_END | `(0x00000040)` |  |
| ITEM_FLAG_TWO_HANDS | `(0x00000080)` |  |
| ITEM_FLAG_BIG_GUN | `(0x00000100)` |  |
| ITEM_FLAG_ALWAYS_VIEW | `(0x00000200)` |  |
| ITEM_FLAG_HAS_TIMER | `(0x00000400)` |  |
| ITEM_FLAG_BAD_ITEM | `(0x00000800)` |  |
| ITEM_FLAG_NO_HIGHLIGHT | `(0x00001000)` |  |
| ITEM_FLAG_SHOW_ANIM | `(0x00002000)` |  |
| ITEM_FLAG_SHOW_ANIM_EXT | `(0x00004000)` |  |
| ITEM_FLAG_LIGHT | `(0x00008000)` |  |
| ITEM_FLAG_GECK | `(0x00010000)` |  |
| ITEM_FLAG_TRAP | `(0x00020000)` |  |
| ITEM_FLAG_NO_LIGHT_INFLUENCE | `(0x00040000)` |  |
| ITEM_FLAG_NO_LOOT | `(0x00080000)` |  |
| ITEM_FLAG_NO_STEAL | `(0x00100000)` |  |
| ITEM_FLAG_GAG | `(0x00200000)` |  |
| ITEM_FLAG_COLORIZE | `(0x00400000)` |  |
| ITEM_FLAG_COLORIZE_INV | `(0x00800000)` |  |
| ITEM_FLAG_CAN_USE_ON_SMTH | `(0x01000000)` |  |
| ITEM_FLAG_CAN_LOOK | `(0x02000000)` |  |
| ITEM_FLAG_CAN_TALK | `(0x04000000)` |  |
| ITEM_FLAG_CAN_PICKUP | `(0x08000000)` |  |
| ITEM_FLAG_CAN_USE | `(0x10000000)` |  |
| ITEM_FLAG_HOLODISK | `(0x20000000)` |  |
| ITEM_FLAG_RADIO | `(0x40000000)` |  |
| ITEM_FLAG_CACHED | `(0x80000000)` |  |
| ITEM_LOOK_DEFAULT | `(0)` |  |
| ITEM_LOOK_ONLY_NAME | `(1)` |  |
| ITEM_LOOK_MAP | `(2)` |  |
| ITEM_LOOK_BARTER | `(3)` |  |
| ITEM_LOOK_INVENTORY | `(4)` |  |
| ITEM_LOOK_WM_CAR | `(5)` |  |
| ITEM_TYPE_OTHER | `(0)` | Types |
| ITEM_TYPE_ARMOR | `(1)` |  |
| ITEM_TYPE_DRUG | `(2)` |  |
| ITEM_TYPE_WEAPON | `(3)` |  |
| ITEM_TYPE_AMMO | `(4)` |  |
| ITEM_TYPE_MISC | `(5)` |  |
| ITEM_TYPE_KEY | `(7)` |  |
| ITEM_TYPE_CONTAINER | `(8)` |  |
| ITEM_TYPE_DOOR | `(9)` |  |
| ITEM_TYPE_GRID | `(10)` |  |
| ITEM_TYPE_GENERIC | `(11)` |  |
| ITEM_TYPE_WALL | `(12)` |  |
| ITEM_TYPE_CAR | `(13)` |  |
| ITEM_TYPE_LAST | `(ITEM_TYPE_CAR)` |  |
| ITEM_TYPE_MAX | `(ITEM_TYPE_LAST + 1)` |  |
| LOCATION_EVENT_FINISH | `(0)` | Script events |
| LOCATION_EVENT_ENTER | `(1)` |  |
| LOCATION_EVENT_MAX | `(LOCATION_EVENT_ENTER + 1)` |  |
| LOCKER_ISOPEN | `(0x01)` | Locker |
| LOCKER_NOOPEN | `(0x10)` |  |
| LOOK_CHECK_DIR | `(0x01)` | Look checks |
| LOOK_CHECK_SNEAK_DIR | `(0x02)` |  |
| LOOK_CHECK_SNEAK_WEIGHT | `(0x04)` |  |
| LOOK_CHECK_TRACE | `(0x08)` |  |
| LOOK_CHECK_SCRIPT | `(0x10)` |  |
| LOOK_CHECK_ITEM_SCRIPT | `(0x20)` |  |
| MAP_EVENT_FINISH | `(0)` | Script events |
| MAP_EVENT_LOOP_0 | `(1)` |  |
| MAP_EVENT_LOOP_1 | `(2)` |  |
| MAP_EVENT_LOOP_2 | `(3)` |  |
| MAP_EVENT_LOOP_3 | `(4)` |  |
| MAP_EVENT_LOOP_4 | `(5)` |  |
| MAP_EVENT_IN_CRITTER | `(6)` |  |
| MAP_EVENT_OUT_CRITTER | `(7)` |  |
| MAP_EVENT_CRITTER_DEAD | `(8)` |  |
| MAP_EVENT_TURN_BASED_BEGIN | `(9)` |  |
| MAP_EVENT_TURN_BASED_END | `(10)` |  |
| MAP_EVENT_TURN_BASED_PROCESS | `(11)` |  |
| MAP_EVENT_MAX | `(MAP_EVENT_TURN_BASED_PROCESS + 1)` |  |
| MAP_OBJECT_CRITTER | `(0)` | Map object types |
| MAP_OBJECT_ITEM | `(1)` |  |
| MAP_OBJECT_SCENERY | `(2)` |  |
| MOUSE_CLICK_LEFT | `(0)` | Mouse click state |
| MOUSE_CLICK_RIGHT | `(1)` |  |
| MOUSE_CLICK_MIDDLE | `(2)` |  |
| MOUSE_CLICK_WHEEL_UP | `(3)` |  |
| MOUSE_CLICK_WHEEL_DOWN | `(4)` |  |
| MOUSE_CLICK_EXT0 | `(5)` |  |
| MOUSE_CLICK_EXT1 | `(6)` |  |
| MOUSE_CLICK_EXT2 | `(7)` |  |
| MOUSE_CLICK_EXT3 | `(8)` |  |
| MOUSE_CLICK_EXT4 | `(9)` |  |
| MSGBOX_GAME | `(0)` | Message box |
| MSGBOX_TALK | `(1)` |  |
| MSGBOX_COMBAT_RESULT | `(2)` |  |
| MSGBOX_VIEW | `(3)` |  |
| PATH_ROOT | `(0)` | Client and mapper paths |
| PATH_DATA | `(1)` |  |
| PATH_ART | `(2)` |  |
| PATH_ART_CRITTERS | `(3)` |  |
| PATH_ART_INTRFACE | `(4)` |  |
| PATH_ART_INVEN | `(5)` |  |
| PATH_ART_ITEMS | `(6)` |  |
| PATH_ART_MISC | `(7)` |  |
| PATH_ART_SCENERY | `(8)` |  |
| PATH_ART_SKILLDEX | `(9)` |  |
| PATH_ART_SPLASH | `(10)` |  |
| PATH_ART_TILES | `(11)` |  |
| PATH_ART_WALLS | `(12)` |  |
| PATH_TEXTURES | `(13)` |  |
| PATH_EFFECTS | `(14)` |  |
| PATH_SND_MUSIC | `(16)` |  |
| PATH_SND_SFX | `(17)` |  |
| PATH_SCRIPTS | `(18)` |  |
| PATH_VIDEO | `(19)` |  |
| PATH_TEXTS | `(20)` |  |
| PATH_SAVE | `(21)` |  |
| PATH_FONTS | `(22)` |  |
| PATH_CACHE | `(23)` |  |
| PATH_SERVER_ROOT | `(30)` | Server paths |
| PATH_SERVER_DATA | `(31)` |  |
| PATH_SERVER_TEXTS | `(32)` |  |
| PATH_SERVER_DIALOGS | `(33)` |  |
| PATH_SERVER_MAPS | `(34)` |  |
| PATH_SERVER_PRO_ITEMS | `(35)` |  |
| PATH_SERVER_PRO_CRITTERS | `(36)` |  |
| PATH_SERVER_SCRIPTS | `(37)` |  |
| PATH_SERVER_SAVE | `(38)` |  |
| PATH_SERVER_CLIENTS | `(39)` |  |
| PATH_SERVER_BANS | `(40)` |  |
| PATH_SERVER_LOGS | `(41)` |  |
| PATH_SERVER_DUMPS | `(42)` |  |
| PATH_SERVER_PROFILER | `(43)` |  |
| PATH_MAPPER_ROOT | `(45)` | Mapper paths |
| PATH_MAPPER_DATA | `(46)` |  |
| RADIO_DISABLE_SEND | `(0x01)` | Radio flags - Item::RadioFlags, ItemCl::RadioFlags |
| RADIO_DISABLE_RECV | `(0x02)` |  |
| RADIO_BROADCAST_WORLD | `(0)` | Broadcast |
| RADIO_BROADCAST_MAP | `(20)` |  |
| RADIO_BROADCAST_LOCATION | `(40)` |  |
| RADIO_BROADCAST_FORCE_ALL | `(250)` |  |
| REASON_GO_HOME | `(10)` | AI Plane begin/end/run reasons Begin |
| REASON_FOUND_IN_ENEMY_STACK | `(11)` |  |
| REASON_FROM_DIALOG | `(12)` |  |
| REASON_FROM_SCRIPT | `(13)` |  |
| REASON_RUN_AWAY | `(14)` |  |
| REASON_SUCCESS | `(30)` | End |
| REASON_HEX_TOO_FAR | `(31)` |  |
| REASON_HEX_BUSY | `(32)` |  |
| REASON_HEX_BUSY_RING | `(33)` |  |
| REASON_DEADLOCK | `(34)` |  |
| REASON_TRACE_FAIL | `(35)` |  |
| REASON_POSITION_NOT_FOUND | `(36)` |  |
| REASON_FIND_PATH_ERROR | `(37)` |  |
| REASON_CANT_WALK | `(38)` |  |
| REASON_TARGET_DISAPPEARED | `(39)` |  |
| REASON_USE_ITEM_NOT_FOUND | `(40)` |  |
| REASON_GAG_CRITTER | `(41)` |  |
| REASON_GAG_ITEM | `(42)` |  |
| REASON_NO_UNARMED | `(43)` |  |
| REASON_ATTACK_TARGET | `(50)` | Run |
| REASON_ATTACK_WEAPON | `(51)` |  |
| REASON_ATTACK_DISTANTION | `(52)` |  |
| REASON_ATTACK_USE_AIM | `(53)` |  |
| SAY_NORM | `(1)` | Say types |
| SAY_NORM_ON_HEAD | `(2)` |  |
| SAY_SHOUT | `(3)` |  |
| SAY_SHOUT_ON_HEAD | `(4)` |  |
| SAY_EMOTE | `(5)` |  |
| SAY_EMOTE_ON_HEAD | `(6)` |  |
| SAY_WHISP | `(7)` |  |
| SAY_WHISP_ON_HEAD | `(8)` |  |
| SAY_SOCIAL | `(9)` |  |
| SAY_RADIO | `(10)` |  |
| SAY_NETMSG | `(11)` |  |
| SAY_DIALOG | `(12)` |  |
| SAY_APPEND | `(13)` |  |
| SAY_ENCOUNTER_ANY | `(14)` |  |
| SAY_ENCOUNTER_RT | `(15)` |  |
| SAY_ENCOUNTER_TB | `(16)` |  |
| SAY_FIX_RESULT | `(17)` |  |
| SAY_DIALOGBOX_TEXT | `(18)` |  |
| SAY_SAY_TITLE | `(39)` | 19..38 SAY_DIALOGBOX_BUTTON |
| SAY_SAY_TEXT | `(40)` |  |
| SAY_FLASH_WINDOW | `(41)` |  |
| SCORE_SPEAKER | `(3)` | Scores |
| SCORE_TRADER | `(4)` |  |
| SCORES_MAX | `(50)` |  |
| SCROLL_MESSBOX | `(0)` | Scroll elements |
| SCROLL_INVENTORY | `(1)` |  |
| SCROLL_INVENTORY_ITEM_INFO | `(2)` |  |
| SCROLL_PICKUP | `(3)` |  |
| SCROLL_PICKUP_FROM | `(4)` |  |
| SCROLL_USE | `(5)` |  |
| SCROLL_BARTER | `(6)` |  |
| SCROLL_BARTER_OFFER | `(7)` |  |
| SCROLL_BARTER_OPPONENT | `(8)` |  |
| SCROLL_BARTER_OPPONENT_OFFER | `(9)` |  |
| SCROLL_GLOBAL_MAP_CITIES_X | `(10)` |  |
| SCROLL_GLOBAL_MAP_CITIES_Y | `(11)` |  |
| SCROLL_SPLIT_VALUE | `(12)` |  |
| SCROLL_TIMER_VALUE | `(13)` |  |
| SCROLL_PERK | `(14)` |  |
| SCROLL_DIALOG_TEXT | `(15)` |  |
| SCROLL_MAP_ZOOM_VALUE | `(16)` |  |
| SCROLL_CHARACTER_PERKS | `(17)` |  |
| SCROLL_CHARACTER_KARMA | `(18)` |  |
| SCROLL_CHARACTER_KILLS | `(19)` |  |
| SCROLL_PIPBOY_STATUS | `(20)` |  |
| SCROLL_PIPBOY_STATUS_QUESTS | `(21)` |  |
| SCROLL_PIPBOY_STATUS_SCORES | `(22)` |  |
| SCROLL_PIPBOY_AUTOMAPS | `(23)` |  |
| SCROLL_PIPBOY_ARCHIVES | `(24)` |  |
| SCROLL_PIPBOY_ARCHIVES_INFO | `(25)` |  |
| SENDMESSAGE_TO_VISIBLE_ME | `(0)` | SendMessage() |
| SENDMESSAGE_TO_IAM_VISIBLE | `(1)` |  |
| SENDMESSAGE_TO_ALL_ON_MAP | `(2)` |  |
| SLOT_INV | `(0)` | Slots |
| SLOT_HAND1 | `(1)` |  |
| SLOT_HAND2 | `(2)` |  |
| SLOT_ARMOR | `(3)` |  |
| SLOT_GROUND | `(255)` |  |
| SLOT_LAST | `(SLOT_ARMOR)` |  |
| SHOW_SCREEN_CLOSE | `(0)` | Show screen modes Ouput: it is 'uint param' in Critter::ShowScreen. Input: I - integer value 'uint answerI', S - string value 'string& answerS' in 'answer_' function. |
| SHOW_SCREEN_TIMER | `(1)` |  |
| SHOW_SCREEN_DIALOGBOX | `(2)` |  |
| SHOW_SCREEN_SKILLBOX | `(3)` |  |
| SHOW_SCREEN_BAG | `(4)` |  |
| SHOW_SCREEN_SAY | `(5)` |  |
| SHOW_SCREEN_ELEVATOR | `(6)` |  |
| SHOW_SCREEN_INVENTORY | `(7)` |  |
| SHOW_SCREEN_CHARACTER | `(8)` |  |
| SHOW_SCREEN_FIXBOY | `(9)` |  |
| SHOW_SCREEN_PIPBOY | `(10)` |  |
| SHOW_SCREEN_MINIMAP | `(11)` |  |
| SKILL_PICK_ON_GROUND | `(-1)` | Special skill values |
| SKILL_PUT_CONT | `(-2)` |  |
| SKILL_TAKE_CONT | `(-3)` |  |
| SKILL_TAKE_ALL_CONT | `(-4)` |  |
| SKILL_LOOT_CRITTER | `(-5)` |  |
| SKILL_PUSH_CRITTER | `(-6)` |  |
| SKILL_TALK | `(-7)` |  |
| SOUND_BUTTON1_IN | `"BUTIN1"` | Sounds |
| SOUND_BUTTON2_IN | `"BUTIN2"` |  |
| SOUND_BUTTON3_IN | `"BUTIN3"` |  |
| SOUND_BUTTON4_IN | `"BUTIN4"` |  |
| SOUND_BUTTON1_OUT | `"BUTOUT1"` |  |
| SOUND_BUTTON2_OUT | `"BUTOUT2"` |  |
| SOUND_BUTTON3_OUT | `"BUTOUT3"` |  |
| SOUND_BUTTON4_OUT | `"BUTOUT4"` |  |
| SOUND_LMENU | `"IACCUXX1"` |  |
| SOUND_COMBAT_MODE_ON | `"ICIBOXX1"` |  |
| SOUND_COMBAT_MODE_OFF | `"ICIBCXX1"` |  |
| SPRITE_CUT_HORIZONTAL | `(1)` | Sprites cutting |
| SPRITE_CUT_VERTICAL | `(2)` |  |
| TARGET_SELF | `(0)` | Target types |
| TARGET_SELF_ITEM | `(1)` |  |
| TARGET_CRITTER | `(2)` |  |
| TARGET_ITEM | `(3)` |  |
| TARGET_SCENERY | `(4)` |  |
| TEXTMSG_TEXT | `(0)` |  |
| TEXTMSG_DLG | `(1)` |  |
| TEXTMSG_ITEM | `(2)` |  |
| TEXTMSG_GAME | `(3)` |  |
| TEXTMSG_GM | `(4)` |  |
| TEXTMSG_COMBAT | `(5)` |  |
| TEXTMSG_QUEST | `(6)` |  |
| TEXTMSG_HOLO | `(7)` |  |
| TEXTMSG_CRAFT | `(8)` |  |
| TEXTMSG_INTERNAL | `(9)` |  |
| TEXTMSG_MAX | `(TEXTMSG_INTERNAL + 1)` |  |
| TRANSFER_CLOSE | `(0)` | Transfer types |
| TRANSFER_HEX_CONT_UP | `(1)` |  |
| TRANSFER_HEX_CONT_DOWN | `(2)` |  |
| TRANSFER_SELF_CONT | `(3)` |  |
| TRANSFER_CRIT_LOOT | `(4)` |  |
| TRANSFER_CRIT_STEAL | `(5)` |  |
| TRANSFER_CRIT_BARTER | `(6)` |  |
| TRANSFER_FAR_CONT | `(7)` |  |
| TRANSFER_FAR_CRIT | `(8)` |  |
| USE_PRIMARY | `(0)` | Uses |
| USE_SECONDARY | `(1)` |  |
| USE_THIRD | `(2)` |  |
| USE_RELOAD | `(3)` |  |
| USE_USE | `(4)` |  |
| USE_NONE | `(15)` |  |
| USE_MAX | `(3)` |  |
| CRITTER_USER_DATA_SIZE | `(400)` | User data |
| PROTO_ITEM_USER_DATA_SIZE | `(500)` |  |
| VAR_TYPE_GLOBAL | `(0)` | Vars types |
| VAR_TYPE_LOCAL | `(1)` |  |
| VAR_TYPE_UNICUM | `(2)` |  |
| VAR_TYPE_LOCAL_LOCATION | `(3)` |  |
| VAR_TYPE_LOCAL_MAP | `(4)` |  |
| VAR_TYPE_LOCAL_ITEM | `(5)` |  |
| VAR_FLAG_QUEST | `(0x01)` | Var flags |
| VAR_FLAG_RANDOM | `(0x02)` |  |
| VAR_FLAG_NO_CHECK | `(0x04)` |  |
| WORLDMAP_FOG_FULL | `(0)` | Worldmap fog |
| WORLDMAP_FOG_HALF | `(1)` |  |
| WORLDMAP_FOG_HALF_EX | `(2)` |  |
| WORLDMAP_FOG_NONE | `(3)` |  |
| WORLDMAP_PROCESS_MOVE | `(0)` | Worldmap events |
| WORLDMAP_PROCESS_ENTER | `(1)` |  |
| WORLDMAP_PROCESS_START_FAST | `(2)` |  |
| WORLDMAP_PROCESS_START | `(3)` |  |
| WORLDMAP_PROCESS_SET_MOVE | `(4)` |  |
| WORLDMAP_PROCESS_STOPPED | `(5)` |  |
| WORLDMAP_PROCESS_NPC_IDLE | `(6)` |  |
| WORLDMAP_PROCESS_KICK | `(7)` |  |
| WORLDMAP_WALK_GROUND | `(0)` | Worldmap walk types |
| WORLDMAP_WALK_FLY | `(1)` |  |
| WORLDMAP_WALK_WATER | `(2)` |  |
| MAX_PARAMS | `(1000)` | Limits |
| MAX_PARAMETERS_ARRAYS | `(100)` |  |
| SKILL_BEGIN | `(GAME_OPTION( SkillBegin ) )` | Skill |
| SKILL_END | `(GAME_OPTION( SkillEnd ) )` |  |
| SKILL_COUNT | `(SKILL_END - SKILL_BEGIN + 1)` |  |
| MAX_SKILL_VAL | `(GAME_OPTION( SkillMaxValue ) )` |  |
| PERK_BEGIN | `(GAME_OPTION( PerkBegin ) )` | Perk |
| PERK_END | `(GAME_OPTION( PerkEnd ) )` |  |
| PERK_COUNT | `(PERK_END - PERK_BEGIN + 1)` |  |
| TIMEOUT_BEGIN | `(GAME_OPTION( TimeoutBegin ) )` | Timeout |
| TIMEOUT_END | `(GAME_OPTION( TimeoutEnd ) )` |  |
| TIMEOUT_COUNT | `(TIMEOUT_END - TIMEOUT_BEGIN + 1)` |  |
| TB_BATTLE_TIMEOUT | `(100000000)` |  |
| TB_BATTLE_TIMEOUT_CHECK |  |  |
| KILL_BEGIN | `(GAME_OPTION( KillBegin ) )` | Kill |
| KILL_END | `(GAME_OPTION( KillEnd ) )` |  |
| ADDICTION_BEGIN | `(GAME_OPTION( AddictionBegin ) )` | Addiction |
| ADDICTION_END | `(GAME_OPTION( AddictionEnd ) )` |  |
| KARMA_BEGIN | `(GAME_OPTION( KarmaBegin ) )` | Karma |
| KARMA_END | `(GAME_OPTION( KarmaEnd ) )` |  |
| DAMAGE_BEGIN | `(GAME_OPTION( DamageBegin ) )` | Damage |
| DAMAGE_END | `(GAME_OPTION( DamageEnd ) )` |  |
| TRAIT_BEGIN | `(GAME_OPTION( TraitBegin ) )` | Trait |
| TRAIT_END | `(GAME_OPTION( TraitEnd ) )` |  |
| TRAIT_COUNT | `(TRAIT_END - TRAIT_BEGIN + 1)` |  |
| REPUTATION_BEGIN | `(GAME_OPTION( ReputationBegin ) )` | Reputation |
| REPUTATION_END | `(GAME_OPTION( ReputationEnd ) )` |  |

