---
title: map_redding_lost.fos
description: " FOnline: 2238 Rotators  map_redding_lost.fos ..."
---

# map_redding_lost.fos


FOnline: 2238
Rotators

map_redding_lost.fos


## Includes

- `_macros.fos`
- `factions_h.fos`
- `mapdata_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| TERMINAL_DIALOG | `(9060)` |  |
| COMPUTER_DIALOG | `(1334)` |  |

## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| FACTION | `uint` | `FACTION_REDDING_GUTTERSNIPES` |  |

## Functions

### map_init

 Initialize map, and store The Redding Guttersnipes faction id to be read by their terminal 

```angelscript
void map_init(Map& map, bool firstTime)
```

### s_Computer

 Instead of calling factions_terminal, we will use that function to assign first player who will find this terminal to that faction 

```angelscript
bool s_Computer(Critter& player, Scenery& terminal, int skill, Item@ item)
```

### s_Desk

 Just some hint for the player where to click 

```angelscript
bool s_Desk(Critter& player, Scenery& terminal, int skill, Item@ item)
```

### r_Leader

 This (called by computer dialog) will make player a leader 

```angelscript
void r_Leader(Critter& player, Critter@ computer, int value)
```


