---
title: factions_recognition.fos
description: " FOnline: 2238 Rotators  factions_recognition.fos ..."
---

# factions_recognition.fos


FOnline: 2238
Rotators

factions_recognition.fos


## Includes

- `_macros.fos`
- `factions_h.fos`

## Functions

### listen_Recognition

 Gets the player name from the message, looks up for his id then looks in the database of the faction the player who called it belongs 

```angelscript
void listen_Recognition(Critter& player, string& message)
```

### e_Reply

 Event that sends the info about desired player through the radio 

```angelscript
uint e_Reply(array<uint>@ values)
```

### SendPlayerDesc

 Creates appropriate string description for player 

```angelscript
void SendPlayerDesc(uint checkingFaction, uint playerId, uint16 channel)
```


