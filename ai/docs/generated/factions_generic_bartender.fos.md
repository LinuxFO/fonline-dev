---
title: factions_generic_bartender.fos
description: " FOnline: 2238 Rotators  factions_generic_bartender.fos ..."
---

# factions_generic_bartender.fos


FOnline: 2238
Rotators

factions_generic_bartender.fos


## Includes

- `_macros.fos`
- `factions_h.fos`
- `factions_generic.fos`

## Classes

### CMessageHandler

implement IMessageHandler to act as a delegate

**Methods**

#### OnMessage
```angelscript
void OnMessage(Critter& critter, Critter& sender, int num, int val)
```


## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| MessageHandler | `[CMessageHandler](factions_generic_bartender.fos.md)` |  |  |

## Functions

### critter_init

```angelscript
void critter_init(Critter& bartender, bool firstTime)
```

### _Idle

```angelscript
void _Idle(Critter& npc)
```

### _OnMessage

```angelscript
void _OnMessage(Critter& bartender, Critter& sender, int num, int val)
```


