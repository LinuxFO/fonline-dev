---
title: minigames.fos
description: " FOnline: 2238 Rotators  minigames.fos ..."
---

# minigames.fos


FOnline: 2238
Rotators

minigames.fos


## Includes

- `_colors.fos`
- `_defines.fos`
- `_macros.fos`
- `minigames_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __MINIGAMES__ |  |  |

## Functions

### SetMinigame

Basic operations on ST_MINIGAME_DATA param...

```angelscript
void SetMinigame(Critter& cr, int team, int id, int flags, int data)
```

### UnsetMinigame

```angelscript
void UnsetMinigame(Critter& cr, bool refreshColors)
```

### UnsetMinigame

```angelscript
void UnsetMinigame(Critter& cr)
```

### ChangeMinigameTeam

```angelscript
void ChangeMinigameTeam(Critter& cr, int team)
```

### GetDSpawn

Find a random dynamic spawnpoint with specific minigameTeam amd minigameId Pick the last spawnpoint in the chain if the spawnpoint is linked with other 

```angelscript
Item@ GetDSpawn(Map@ map, int minigameData)
```

### GetNextDSpawn

Gets the last team spawnpoint in the chain 

```angelscript
Item@ GetNextDSpawn(Item@ dSpawn, int minigameTeamAndId, bool reverse)
```

### _DSpawn

DSpawn initialization & events 

```angelscript
void _DSpawn(Item& item, bool firstTime)
```

### _DSpawnWalk

```angelscript
void _DSpawnWalk(Item& item, Critter& crit, bool entered, uint8 dir)
```

### _DSpawnSkill

```angelscript
bool _DSpawnSkill(Item& item, Critter& crit, int skill)
```

### TryCaptureDSpawn

DSpawn Capturing 

```angelscript
bool TryCaptureDSpawn(Item@ dSpawn, Critter@ crit)
```

### CaptureDSpawn

```angelscript
void CaptureDSpawn(Item@ dSpawn, Critter@ crit, uint minigameTeamAndId)
```

### CaptureDSpawnTick

```angelscript
uint CaptureDSpawnTick(array<int>@ eventValues)
```

### GetMinigameTeamColor

I needed this, then I changed my mind. Still, it could be useful for something.

```angelscript
int GetMinigameTeamColor(int minigameTeam)
```

### r_SetMinigame

For dialogs

```angelscript
uint r_SetMinigame(Critter& player, Critter@ npc, int team, int id, int flags, int data, uint returnValue)
```

### r_SetMinigame

```angelscript
void r_SetMinigame(Critter& player, Critter@ npc, int team, int id, int flags, int data)
```

### refresh

Forces refreshing colorization, might be needed if you change param ST_MINIGAME_DATA manually.

```angelscript
void refresh(Critter& caller, int, int, int critterId)
```

### info

Basic info about data stored in ST_MINIGAME_DATA.

```angelscript
void info(Critter& caller, int, int, int critterId)
```

### team

Sets a minigame team for a critter.

```angelscript
void team(Critter& caller, int minigameTeam, int minigameId, int critterId)
```


