---
title: worldmap_players.fos
description: " FOnline: 2238 Rotators  worldmap_players.fos ..."
---

# worldmap_players.fos


FOnline: 2238
Rotators

worldmap_players.fos


## Includes

- `_macros.fos`
- `worldmap_h.fos`

## Classes

### CZone

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| players | `array<uint>` |  | array of players |

**Methods**

#### AddPlayer
* * Gets the array of players in that zone.  Critter@[]@ GetPlayers() { return players; } * * Adds player to the zone. 

```angelscript
void AddPlayer(Critter@ player)
```

#### RemovePlayer
* * Removes player from the zone. 

```angelscript
void RemovePlayer(Critter@ player)
```


## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| idx | `uint` | `zy * ZONE_COUNT_X + zx` |  |
| cr | `Critter@` | `GetCritter(Zones[idx].players[i])` |  |

## Functions

### WorldmapUpdatePlayer

todo: if player just idles on worldmap after restart, he won't be placed in zone

```angelscript
void WorldmapUpdatePlayer(Critter@ player)
```

### WorldmapRemovePlayer

* * Removes the player from previously occupied zone. Called by critter_finish in main. 

```angelscript
void WorldmapRemovePlayer(Critter@ player)
```

### WorldmapUpdateGroup

same as above, but loops for all players in group

```angelscript
void WorldmapUpdateGroup(array<Critter@>& group)
```

### WorldmapGetPlayers

* * Retrieves players from given zone, appends them to given array * @return Number of players added. 

```angelscript
uint WorldmapGetPlayers(uint zx, uint zy, array<Critter@>& players)
```

### WorldmapGetPlayerTime

* * Retrieves time, how long player spent on worldmap. * Negative value denotes how long ago player left worldmap. 

```angelscript
int WorldmapGetPlayerTime(Critter& player)
```

### check_time

```angelscript
void check_time(Critter& cr, int p0, int p1, int p2)
```

### check_integrity

* * Iterates through every zone and checks if the players that are there are REALLY there. 

```angelscript
void check_integrity(Critter& cr, int p0, int p1, int p2)
```


