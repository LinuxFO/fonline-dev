---
title: prospects.fos
description: " FOnline: 2238 Rotators  prospects.fos ..."
---

# prospects.fos


FOnline: 2238
Rotators

prospects.fos


## Includes

- `_macros.fos`
- `_maps.fos`
- `worldmap_h.fos`
- `MsgStr.h`
- `_scripts.fos`
- `mapdata_h.fos`
- `utils_h.fos`
- `groups_h.fos`
- `entire.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| PROSPECT_WOODS | `(1)` | prospects types |
| PROSPECT_ROCKS | `(2)` |  |
| PROSPECT_ORE | `(3)` |  |
| SCIENCE_TIMEOUT | `(REAL_MINUTE(5))` | timeout when looking for prospects |
| REQ_SKILL | `(80)` |  |

## Functions

### IsProspectLocation

* * Checks if map lies in prospect location 

```angelscript
bool IsProspectLocation(Map@ map)
```

### IsProspectLocation

* * Checks if given location is prospect location. 

```angelscript
bool IsProspectLocation(Location@ location)
```

### IsProspectMap

helper

```angelscript
bool IsProspectMap(Item@ map)
```

### r_GiveEmptyMap

 Give empty map to player 

```angelscript
void r_GiveEmptyMap(Critter& player, Critter@ npc, int val)
```

### d_HaveProspectMap

 Checks if player has prospect map with location marked in his hands 

```angelscript
bool d_HaveProspectMap(Critter& player, Critter@ npc, int val)
```

### r_SellProspect

 Sells prospect marked with a map that player have in hand 

```angelscript
void r_SellProspect(Critter& player, Critter@ npc, int val)
```

### Invade

* * Sends npcs expedition to prospect location. 

```angelscript
void Invade(uint locId, uint seller)
```

### invade

```angelscript
void invade(Critter& cr, int p0, int p1, int p2)
```

### UseProspectMap

* * Discovers prospect or prepares map to it for an npc. 

```angelscript
bool UseProspectMap(Critter& cr, Item& map)
```

### CreateProspectMap

* * Creats map that can be used to sell the prospect 

```angelscript
bool CreateProspectMap(Critter& player, Item& item)
```

### FindProspect

* * Discovers a prospect (or not). 

```angelscript
bool FindProspect(Critter& cr, Item& map)
```

### CheckTerrain

* * Checks if any prospect can be found on given type of terrain. 

```angelscript
bool CheckTerrain(uint terrain)
```

### CreateProspect

* * Creates prospect location for given type of terrain. 

```angelscript
void CreateProspect(Critter& cr, uint terrain)
```

### spawn_miner

```angelscript
void spawn_miner(Critter& cr, int p0, int p1, int p2)
```

### SetOwner

* * Assigns owner for prospect location. It's stored in 1st map data[0]. 

```angelscript
void SetOwner(uint locId, uint ownerId, uint sellerId)
```

### GetOwner

* * Retrieves the owner of the prospect 

```angelscript
uint GetOwner(uint locId)
```

### IsSeller

* * Checks if player has signed contract with the new owner, so that he can take his share. 

```angelscript
bool IsSeller(Critter& cr)
```

### GetContainer

* * Gets 'share' container for the map critter is actually in. 

```angelscript
Item@ GetContainer(Critter& cr)
```

### s_Container

* * Shows the container where share is stored. 

```angelscript
bool s_Container(Critter& crit, Scenery& scen, int skill, Item@ item)
```


