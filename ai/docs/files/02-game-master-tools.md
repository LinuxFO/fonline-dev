# Game Master Tools

Game Master Tools (GMT) is a set of scripted tools available for Game Masters, which allow to do various tasks in more efficient manner. To enable GMT add following lines to FOnline2238.cfg:

```init
[GMT]
Enabled=1
```

...and (re)start client. After changing access level to Tester or higher, on-screen display (OSD) should appear in top left corner of the screen minimal set of informations. After enabling all possible mini-features, OSD shows detailed information about current location, map and items/critters when you hover mouse cursor over them.

```ini
[GMT]
Enabled=1
Menu=1
Possess=1
OSDInfo=Location,Map,Critter,Item,Mouse,Hex
OSDInfoLocation=Maps,Position,Type,Extra
OSDInfoMap=Size,Faction,Owner,Size,Hex,Extra
OSDInfoCritter=Picture,Extra
OSDInfoItem=Extra
Draw=1
ItemInfo=Extra
CritterInfo=Extra
```

Next thing which may be interesting, is customizable menu allowing to execute server commands. It is fully configurable at client side, allowing your Game Masters to change it to their needs.
Traditional menu config, used in previous system, with famous Teleport next to Airstrike:

```text
;;`
;;Standard devmenu
;;

ONPLAYER,ONNPC;Possess;internal possess
ONPLAYER,ONNPC;Trade;runscript_unsafe dev_menu@unsafe_Trade $[Critter.Id] 0 0
ONITEM,ISCONTAINER;Browse items;runscript_unsafe dev_menu@unsafe_Trade 0 $[Item.Id] 0
ONPLAYER,ONNPC,ISALIVE;Kill;runscript_unsafe dev_menu@unsafe_KillCritter $[Critter.Id] 0 0
ONPLAYER,ONNPC,ISKNOCK;Kill;runscript_unsafe dev_menu@unsafe_KillCritter $[Critter.Id] 0 0
ONCHOSEN,ONPLAYER,ONNPC,ISDEAD;Revive;runscript_unsafe dev_menu@unsafe_KillCritter $[Critter.Id] 0 0
ONNPC;Remove critter;runscript_unsafe dev_menu@unsafe_RemoveCritter $[Critter.Id] 0 0
ONITEM;Remove item;runscript_unsafe dev_menu@unsafe_RemoveItem $[Item.Id] 0 0
ONITEM,ONGROUND;Teleport;runscript_unsafe dev_menu@unsafe_Teleport 0 $[HexX] $[HexY]
ONGROUND,NOHIDE;Airstrike;runscript dev_menu@Airstrike 0 $[HexX] $[HexY]
ONITEM,ISPOSSESS;Pick item;runscript_unsafe dev_menu@unsafe_PickItem $[Possessed.Id] $[Item.Id] 0
ONPLAYER,ONNPC,ISPOSSESS;Attack;runscript_unsafe dev_menu@unsafe_Attack $[Possessed.Id] $[Critter.Id] 0
ONGROUND,ISPOSSESS;Move to;runscript_unsafe dev_menu@unsafe_MoveTo $[Possessed.Id] $[HexX] $[HexY]
ISPOSSESS;Stop;runscript_unsafe dev_menu@unsafe_Stop $[Possessed.Id] 0 0
ONCHOSEN,ONPLAYER,ONNPC,ISKNOCK;Wake;runscript_unsafe dev_menu@unsafe_NeutralizeCritter $[Critter.Id] 0 0
ONCHOSEN,ONPLAYER,ONNPC,ISNTKNOCK;Neutralize;runscript_unsafe dev_menu@unsafe_NeutralizeCritter $[Critter.Id] 0 0
```

Made of three sections, each separated with ";" character, where first is set of flags defining when given button should show up, second is name, and third is command to execute. As it was revealed some time ago, it's possible to add submenu to specific buttons. To do so, replace command part with "internal menu". All next lines with single SUBMENU flag will be part of button submenu, anything else will become new top-level button.

```text
ONPLAYER;Be Friendly;internal menu
SUBMENU;Hug;command slap -p $[Player.Id]
SUBMENU;Gift;command airstrike -p $[Player.Id]
```

As single menu may be not enough, it's possible to switch between them, for example you during the events/bugs-hunting/etc. Default menu, which is loaded after GMT initialization, need to be stored in file named GMTbuttons.txt. Also be noted, that all menu buttons relay on macro system (they are in fact one-line macros).

To display GMT menu, use CTRL+Click.
To switch between menus, use `~gmtools` menu load FILENAME.
To reload currently used menu (after file edit), use `~gmtools` menu reload.

See `client_gmtools_menu.fos->CContextMenu::OnShow()` for details about menu flags
See `client_gmtools_macro.fos->GetVars()` for details about menu `$[variables]`. Note that `$[LastSpawned]` group is parsed at server side (`gmtools.fos->unsafe_question`).

As communication between Game Masters online is important thing, and it may be hard to enforce one specific way of communication using external tools, GMT provides simple chat system to be used ingame. It's not meant to replace IRC/voice communication, but should be enough for some situation (like during events, or when you want to talk ingame with/as GodOfTheRealm); to use it, put "@" characted before message.
GMTchat is single feature which works for all authenticated characters, even without GMT enabled.

```text
client_gmtools.fos
client_gmtools_menu.fos
client_gmtools_macro.fos
client_gmtools_chat.fos
gmtools_h.fos
gmtools.fos
gmtools_csc.fos
```

How exactly does one run the god function? What would the command be in-game?

However, it would open some of features to every character - unlike regular cheats, GodOfTheRealm may have some things enabled without need to be authenticated. For example, once you enabled this mode, your character will always stay invisible, until you disable it (note that invisibility includes list of players online provided by `~gameinfo 1`).

If that's for local server, then you're ready to go; if not, I'd uncomment original part of the function and use own name(s) there. Unless you remove/modify how it works in scripts and extensions, ofc.

```text
Enable:
~run cheats god 0 0 0
Disable:
~run cheats mortal 0 0 0
```
