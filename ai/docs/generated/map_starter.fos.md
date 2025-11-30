---
title: map_starter.fos
---

# map_starter.fos

## Includes

- `_macros.fos`
- `logging_h.fos`

## Functions

### map_init

Map script for starter locations

```angelscript
void map_init(Map& map, bool firstTime)
```

### _OnLeaveMap

```angelscript
void _OnLeaveMap(Map& map, Critter& cr)
```

### s_Console

Vault Door Console

```angelscript
bool s_Console(Critter& player, Scenery& console, int skill, Item@ item)
```

### t_Tutorial

Trigger (Players chooses whether to play tutorial or not)

```angelscript
void t_Tutorial( Critter& player, Scenery& trigger, bool entered, uint8 dir)
```

### r_TutorialTeleport

Dialogue (on leaving Vault)

```angelscript
void r_TutorialTeleport(Critter& player, Critter@ npc)
```

### e_WelcomeMessage

Welcome message upon entering Tutorial map

```angelscript
uint e_WelcomeMessage(array<int>@ data)
```

### r_TutorialTeleportSF

Dialogue (on leaving Vault)

```angelscript
void r_TutorialTeleportSF(Critter& player, Critter@ npc)
```

### e_WelcomeMessageSF

Welcome message upon entering Tutorial map

```angelscript
uint e_WelcomeMessageSF(array<int>@ data)
```


