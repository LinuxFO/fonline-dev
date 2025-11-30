---
title: gmtools_h.fos
description: " FOnline: 2238 Rotators  gmtools_h.fos ..."
---

# gmtools_h.fos


FOnline: 2238
Rotators

gmtools_h.fos


## Includes

- `_defines.fos`
- `_colors.fos`

## Included By

- [broadcast.fos](broadcast.fos.md)
- [client_gmtools.fos](client_gmtools.fos.md)
- [client_gmtools_menu.fos](client_gmtools_menu.fos.md)
- [gmtools.fos](gmtools.fos.md)

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __GMTOOLS_H__ |  |  |
| GMTServerFunc | `\` | open ~runscript functions to macros |
| GMTOOLS_CONFIG_ENABLED |  |  |
| GMTOOLS_CONFIG_AUTHTIMER | `(1)` |  |
| GMTOOLS_VERSION | `3107` |  |
| GMT_ACCESS_ANY | `(ACCESS_TESTER)` | access levels |
| GMT_ACCESS_POSSESS | `(ACCESS_TESTER)` |  |
| GMT_ACCESS_COMMAND | `(ACCESS_MODER)` |  |
| GMT_ACCESS_RUNSCRIPT | `(ACCESS_ADMIN)` |  |
| GMT_ACCESS_RUNSCRIPT_UNSAFE | `(ACCESS_TESTER)` |  |
| GMT_ACCESS_CRITTER | `(ACCESS_MODER)` |  |
| GMT_ACCESS_ITEM | `(ACCESS_TESTER)` |  |
| GMT_ACCESS_MAP | `(ACCESS_TESTER)` |  |
| GMT_ACCESS_LOCATION | `(GMT_ACCESS_MAP)` |  |
| GMT_ACCESS_CHAT | `(ACCESS_TESTER)` |  |
| GMT_NOACCESS | `(0x42)` |  |
| GMT_COLOR_DEFAULT | `(COLOR_LGREEN)` | colors |
| GMT_COLOR_SERVER | `(COLOR_GREEN_RED)` |  |
| GMT_COLOR_NPC | `(COLOR_GREEN)` |  |
| GMT_COLOR_PLAYER | `(COLOR_LGREEN)` |  |
| GMT_COLOR_DEBUG | `(COLOR_RED)` |  |
| GMT_COLOR_CHAT | `(COLOR_CHANGE_ALPHA(GMT_COLOR_CHATFRAME, 150))` |  |
| GMT_COLOR_CHATFRAME | `(COLOR_RGB(0, 0, 0))` |  |
| GMT_COLOR_CHATTESTER | `(COLOR_RGB(0xFF, 0xFF, 0))` |  |
| GMT_COLOR_CHATMODER | `(COLOR_RGB(0, 0x6A, 0xD5))` |  |
| GMT_COLOR_CHATADMIN | `(COLOR_RGB(0xFF, 0, 0))` |  |
| GMT_COLOR_CHATDEV | `(COLOR_RGB(0xFF, 0xFF, 0xFF))` |  |
| GMT_OSD_X | `(10)` | OnScreen Display settings |
| GMT_OSD_Y | `(10)` |  |
| GMT_OSD_Y_TAB | `(30)` |  |
| GMT_OSD_WM_X | `(8)` |  |
| GMT_OSD_WM_Y | `(90)` |  |
| GMT_OSD_INFO | `(0x01)` | flags |
| GMT_OSD_INFOEX | `(0x02)` |  |
| GMT_OSD_CRITTER | `(0x04)` |  |
| GMT_BUTTONS_FILE | `"GMTbuttons.txt"` |  |
| GMT_BUTTON_ONCHOSEN | `(0x0000001)` | button flags primary |
| GMT_BUTTON_ONPLAYER | `(0x0000002)` |  |
| GMT_BUTTON_ONNPC | `(0x0000004)` |  |
| GMT_BUTTON_ONITEM | `(0x0000008)` |  |
| GMT_BUTTON_ONGROUND | `(0x0000010)` |  |
| GMT_BUTTON_ISPID | `(0x0000020)` | secondary - shared |
| GMT_BUTTON_ISALIVE | `(0x0000040)` | secondary - critter |
| GMT_BUTTON_ISKNOCK | `(0x0000080)` |  |
| GMT_BUTTON_ISNTKNOCK | `(0x0000100)` |  |
| GMT_BUTTON_ISDEAD | `(0x0000200)` |  |
| GMT_BUTTON_ISPOSSESS | `(0x0000400)` |  |
| GMT_BUTTON_ISCONTAINER | `(0x0000800)` | secondary - item |
| GMT_BUTTON_SUBMENU | `(0x0001000)` | button |
| GMT_BUTTON_NOHIDE | `(0x0002000)` |  |
| GMT_BUTTON_DISABLED | `(0x0004000)` |  |
| GMT_GETACCESS | `(0)` | question type |
| GMT_QUESTION_COMMAND | `(2)` | #define GMT_QUESTION_PING			(1) |
| GMT_QUESTION_GAMEVARS | `(3)` |  |
| GMT_QUESTION_CRITTER | `(4)` |  |
| GMT_QUESTION_ITEM | `(5)` |  |
| GMT_QUESTION_MAP | `(6)` |  |
| GMT_QUESTION_LOCATION | `(7)` |  |
| GMT_QUESTION_CHAT | `(8)` |  |
| GMT_QUESTION_BROADCAST | `(9)` |  |
| GMT_STATUS_SEND | `(0)` | answer status |
| GMT_STATUS_BAD | `(GMT_STATUS_SEND - 1)` | <0 |
| GMT_STATUS_DENIED | `(GMT_STATUS_BAD - 1)` |  |
| GMT_STATUS_UNKNOWN | `(GMT_STATUS_DENIED - 1)` |  |
| GMT_STATUS_OK | `(GMT_STATUS_SEND + 1)` | >0 |
| GMT_STATUS_FORCE | `(GMT_STATUS_OK + 1)` |  |
| GMT_STATUS_OLD | `(GMT_STATUS_FORCE + 1)` |  |
| GMT_DATAFLAG_CRITTER_EX | `(0x01)` | answer data - one character, case sensitive critter |
| GMT_DATAFLAG_CRITTER_SPECIAL | `(0x02)` |  |
| GMT_DATAFLAG_CRITTER_SKILLS | `(0x04)` |  |
| GMT_DATA_CRITTER_ST | `"S"` |  |
| GMT_DATA_CRITTER_PE | `"P"` |  |
| GMT_DATA_CRITTER_EN | `"E"` |  |
| GMT_DATA_CRITTER_CH | `"C"` |  |
| GMT_DATA_CRITTER_IN | `"I"` |  |
| GMT_DATA_CRITTER_AG | `"A"` |  |
| GMT_DATA_CRITTER_LK | `"L"` |  |
| GMT_DATA_CRITTER_SMALLGUNS | `"0"` |  |
| GMT_DATA_CRITTER_BIGGUNS | `"1"` |  |
| GMT_DATA_CRITTER_ENERGYWEAPONS | `"2"` |  |
| GMT_DATA_CRITTER_ENERGYWEAPONS | `"2"` |  |
| GMT_DATA_CRITTER_UNARMED | `"3"` |  |
| GMT_DATA_CRITTER_MELEE | `"4"` |  |
| GMT_DATA_CRITTER_MELEE | `"5"` |  |
| GMT_DATA_CRITTER_MELEE | `"6"` |  |
| GMT_DATA_CRITTER_MELEE | `"7"` |  |
| GMT_DATA_CRITTER_MELEE | `"8"` |  |
| GMT_DATA_CRITTER_MELEE | `"9"` |  |
| GMT_DATA_CRITTER_MELEE | `"0"` |  |
| GMT_DATA_CRITTER_MELEE | `"a"` |  |
| GMT_DATA_CRITTER_MELEE | `"b"` |  |
| GMT_DATA_CRITTER_MELEE | `"c"` |  |
| GMT_DATA_CRITTER_MELEE | `"d"` |  |
| GMT_DATA_CRITTER_MELEE | `"e"` |  |
| GMT_DATA_CRITTER_MELEE | `"f"` |  |
| GMT_DATA_CRITTER_MELEE | `"g"` |  |
| GMT_DATAFLAG_ITEM_EX | `(0x01)` | item |
| GMT_DATAFLAG_MAP_EX | `(0x01)` | map |
| GMT_DATAFLAG_MAP_SIZE | `(0x02)` |  |
| GMT_DATAFLAG_MAP_FACTION | `(0x04)` |  |
| GMT_DATA_MAP_CREATED | `"c"` |  |
| GMT_DATA_MAP_FACTION | `"f"` |  |
| GMT_DATA_MAP_FACTIONAME | `"F"` |  |
| GMT_DATA_MAP_FACTIONMEMBERS | `"M"` |  |
| GMT_DATA_MAP_HEIGHT | `"h"` |  |
| GMT_DATA_MAP_ID | `"i"` |  |
| GMT_DATA_MAP_LOCATIONID | `"I"` |  |
| GMT_DATA_MAP_LASTENTER | `"e"` |  |
| GMT_DATA_MAP_OWNER | `"o"` |  |
| GMT_DATA_MAP_WIDTH | `"w"` |  |
| GMT_DATAFLAG_LOCATION_EX | `(0x01)` | location |
| GMT_DATAFLAG_LOCATION_POSITION | `(0x02)` |  |
| GMT_DATAFLAG_LOCATION_TYPE | `(0x04)` |  |
| GMT_DATA_LOCATION_BASE | `"b"` |  |
| GMT_DATA_LOCATION_CAVE | `"c"` |  |
| GMT_DATA_LOCATION_CITYENCOUNTER | `"E"` |  |
| GMT_DATA_LOCATION_ENCOUNTER | `"e"` |  |
| GMT_DATA_LOCATION_ID | `"i"` |  |
| GMT_DATA_LOCATION_INSTANCEDQUEST | `"q"` |  |
| GMT_DATA_LOCATION_MAPCOUNT | `"?"` |  |
| GMT_DATA_LOCATION_MINE | `"m"` |  |
| GMT_DATA_LOCATION_PID | `"I"` |  |
| GMT_DATA_LOCATION_REPLICATION | `"r"` |  |
| GMT_DATA_LOCATION_TCTOWN | `"*"` |  |
| GMT_DATA_LOCATION_TENT | `"t"` |  |
| GMT_DATA_LOCATION_TOWN | `"T"` |  |
| GMT_DATA_LOCATION_VISIBLE | `"v"` |  |
| GMT_DATA_LOCATION_WORLDX | `"x"` |  |
| GMT_DATA_LOCATION_WORLDY | `"y"` |  |
| GMT_CHECKACCESS | `((GMTOOLS_CONFIG_AUTHTIMER * 60) * 1000)` |  |

## Functions

### name

```angelscript
void name(Critter & pX, int p0, int p1, int p2, string@ p3, array<int>@ p4) \
```

### name

```angelscript
void name(Critter & pX, int p0, int p1, int p2)
```


