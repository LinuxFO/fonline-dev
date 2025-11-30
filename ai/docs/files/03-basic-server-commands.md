# Basic Server Commands

There is around 200 server commands and dozens of scripts in various modules. A complete description is outside of the scope of this tutorial. Below you will find the basic set of commands which should help you get started with administrative duties.

Note: The parts of commands written with cursive are variables (not actual text to type but rather what kind of data should be typed there). The parts in brackets are optional. Elements mutually exclusive are in parentheses and separated with |.

Before you start - some switches are used across many commands. The most common is `[-p player]` switch, which let's you choose target critter (player or NPC) - player can be either critter Id (it works for NPCs too) or player name. Usually when the switch is omitted and a command requires a target, the character using the command is the target. Similar switch `[-n npc]` let's you choose NPC by providing NPC Id (which is equal to critter Id - 5000000), which in many cases is easier to type.

## Getting Information

```text
`alts [-l locationId] [-o]
```

Display IPs and characters suspected to be multilogs (sharing the same IP). `-l` option allows to limit the search to a specific location. By default offline characters are ignored, you can turn this behavior off with `-o` option.

```text
`gameinfo infoType
```

Scripted equivalent of hardcoded `~gameinfo`. Only `infoType == 1` is implemented.

```text
`listauthenticated
Alias: `la
```

Displays all authenticated characters present in the game (except those with GodOfTheRealm mode).

## Moving Around

```text
`teleport map [entire] [(-p player | -n npc)] [-x hexX -y hexY]
Alias: `tp
```

Teleports a critter to a specific place. The map parameter is either map Id or map alias (for example "nr" for New Reno). Full list of map aliases can be found in `SetAliases` function in cheats.fos module.

```text
`teleportteam map [entire] [(-p player | -n npc)] [-x hexX -y hexY]
```

Works exactly like ``teleport`, except it teleports also players who tagged you and are near you.

```text
`goto [(-p player | -n npc)] [-s] [-f]
```

Teleports to a critter. Use `-s` switch to be teleported in a safe distance from the critter. Use `-f` switch to force teleportation if the critter is on global map (by default teleporting to critters on global map is disabled).

```text
`toglobal [(-p player | -n npc)]
```

Teleports a critter to global map.

```text
`summon (-p player | -n npc)
```

Summons a critter to you.

```text
`dismiss (-p player | -n npc)
```

Teleports the critter back where it was.

## Items

```text
`spawnitem pid count [-x hexX -y hexY] [-r radius] [-a amount] [-script module@function] [-legit]
```

Spawns item on ground. Amount is amount of items in a single stack, count is number of stacks. Use `-legit` flag (admin access only) to spawn item which can be used in normal (legit) locations. Check cheats.fos, there is more options.

```text
`give pid count [(-p player | -n npc)] [-script module@function] [-legit]
```

Gives a critter an item. Check ITEMPID.H for the list of pids. Use `-legit` flag to spawn legit item (requires admin access level). Non-legit items can be used only in non-legit locations (locations spawned with a command without `-legit` option).

```text
`pickitems
```

Picks all items from the hex.

```text
`dropitems
```

Drops all items in inventory slot.

```text
`clearinventory
```

Deletes all items inside inventory slot.

## Critters

```text
`addnpc protoId [-d dialogId] [-s module@script] [-l level] [-dir direction] [-b bagId]
```

Creates an NPC. The options should be quite self explanatory (there is a lot more, check cheats.fos). There are similar commands `addmob` and `addfollower`.

```text
`param 0 param [value]
```

A command allowing to view and set your character params. Full list of params can be checked in \_defines.fos.

```text
`disguise crType [(-p player | -n npc)]
```

Popular command to change "skin" (critter type) of a player or an NPC. Critter types are defined in CritterTypes.cfg file.

```text
`ces
```

Clears enemy stack of all critters on the map. If AI hits the fan, ``ces` might help.

```text
`kill (players | npcs | all | -p player | -n npc)
```

Kills every player / NPC / critter in your sight or just a critter of your choice.

```text
`reviveall
```

Something you want to type quickly after you missclick airstrike button.

```text
`resetreputations [(-p player | -n npc)]
```

Resets all reputations of a critter.

```text
`dropdrugs [(-p player | -n npc)]
```

Removes all addictions from a critter.

## Locations

```text
`createlocation pid [-legit]
```

Creates a location with given location pid at your global map coordinates. Use `-legit` flag to create a legit location (in legit locations non-legit items won't work for players).

```text
`deletelocation
```

Deletes location you are in.

````text
`disablepvp
`enablepvp
```text

Disables / enables PvP in a map.

```text
`disablegrids
`enablegrids
````

Disables / enables exit grids in a map.

## Fun

```text
`slap (-p player | -n npc) [-a actionPoints]
```

Slaps a player. Optionally you can decide how many action points you want to take - be careful, large values can keep player character on the ground for hours.

```text
`massslap [-a actionPoints] [-r radius]
```

What is better than slapping a player? Slapping everyone in a map! Additionaly you can define how far the critters will fly (in a random direction). Warning: with large radius values players and especially NPCs (because they won't complain about it) might end up stuck in some unreachable places.
