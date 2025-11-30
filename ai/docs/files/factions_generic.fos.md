---
title: factions_generic.fos
description: " FOnline: 2238 Rotators  factions_generic.fos ..."
---

# factions_generic.fos


FOnline: 2238
Rotators

factions_generic.fos


## Includes

- `_macros.fos`
- `factions_h.fos`

## Included By

- [factions_generic_bartender.fos](factions_generic_bartender.fos.md)

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| MSG_PLAYER_NEAR | `(1)` | player near npc |
| MSG_PLAYER_ENTERED | `(2)` |  |
| MSG_PLAYER_LEFT | `(3)` |  |
| MSG_PLAYER_NEAR_RANK3_AREA | `(4)` |  |
| MSG_PLAYER_ENTERED_RANK3_AREA | `(5)` |  |
| MSG_PLAYER_NEAR_RANK1_AREA | `(6)` |  |
| MSG_PLAYER_ENTERED_RANK1_AREA | `(7)` |  |
| MSG_SAY_HELLO | `(100)` | say messages |

## Functions

### IdleLookAround

 Watches for players around, sends appropriate messages via handler  Params npc - npc that will handle the message dist - dist to send MESSAGE_NEAR

```angelscript
void IdleLookAround(Critter& npc, uint dist, IMessageHandler@ handler)
```

### GreetMember

 Greet if the critter is member of the same faction 

```angelscript
void GreetMember(Critter& npc, Critter& critter, IMessageHandler@ handler)
```


