---
title: reinforcements.fos
description: " FOnline: 2238 Rotators  reinforcements.fos ..."
---

# reinforcements.fos


FOnline: 2238
Rotators

reinforcements.fos


## Includes

- `_macros.fos`
- `_npc_pids.fos`
- `_dialogs.fos`
- `_bags.fos`
- `npc_planes_h.fos`
- `mapdata_h.fos`
- `reputations_h.fos`
- `utils_h.fos`
- `reinforcements_h.fos`
- `guard_h.fos`
- `entire.fos`
- `serializator.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __REINFORCEMENTS_MODULE__ |  |  |

## Classes

### CAlertSettings

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| AlertLevelNone | `uint` |  |  |
| AlertLevelLight | `uint` |  |  |
| AlertLevelHeavy | `uint` |  |  |
| AlertCountGuard | `uint` |  |  |
| AlertCountNpc | `uint` |  |  |
| AlertCountDrop | `uint` |  |  |
| AlertCountPDrop | `uint` |  |  |
| ReinforcementsDelayLow | `uint` |  |  |
| ReinforcementsDelayHigh | `uint` |  |  |
| ReinforcementsDelayRet | `uint` |  |  |
| ReinforcementsCountLow | `uint` |  |  |
| ReinforcementsCountHigh | `uint` |  |  |
| CycleLength | `uint` |  |  |

**Methods**

#### Init
```angelscript
void Init()
```

#### Load
```angelscript
void Load()
```

#### Save
```angelscript
void Save()
```

#### Update
```angelscript
void Update()
```

### CAlertMap

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| Index | `uint` |  |  |
| MapId | `uint` |  |  |
| AlertLevel | `uint` |  |  |
| NoReinforcements | `bool` |  |  |
| Dead | `bool` |  |  |
| Reinforcements | `array<uint>` |  |  |
| ReinforcementsMax | `array<uint>` |  |  |
| Calling | `array<bool>` |  |  |
| EventId | `array<uint>` |  |  |
| Attackers | `array<uint>` |  |  |

**Methods**

#### StartCalling
```angelscript
void StartCalling(uint type)
```

#### Spawn
```angelscript
void Spawn(uint type)
```

#### Cycle
```angelscript
void Cycle()
```

#### ProcessDeath
```angelscript
void ProcessDeath(Critter& cr, Critter@ killer)
```

#### ReinforcementReturn
```angelscript
void ReinforcementReturn(uint type)
```

#### IsDead
```angelscript
bool IsDead()
```

#### Validate
```angelscript
void Validate()
```


## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| Initialized | `bool` | `false` |  |
| settings | `[CAlertSettings](reinforcements.fos.md)` |  |  |
| obs | `uint` | `0` |  |

## Functions

### SaveAlertMaps

```angelscript
void SaveAlertMaps()
```

### SetAlertMap

```angelscript
void SetAlertMap(Map& map, array<uint>@ maxes)
```

### InitAlertMaps

```angelscript
bool InitAlertMaps()
```

### IsAlertMap

```angelscript
bool IsAlertMap(Map& map)
```

### GetAlertLevel

```angelscript
uint GetAlertLevel(Map& map)
```

### ProcessDeath

```angelscript
void ProcessDeath(Map& map, Critter& cr, Critter@ killer)
```

### ReinforcementReturn

```angelscript
void ReinforcementReturn(Critter& npc)
```

### e_ReinforcementReturn

```angelscript
uint e_ReinforcementReturn(array<uint>@ values)
```

### e_CallReinforcements

```angelscript
uint e_CallReinforcements(array<uint>@ values)
```

### e_AlertMapsCycle

```angelscript
uint e_AlertMapsCycle(array<uint>@ values)
```

### GetPid

* * Gets the PID number for the reinforcement guard appropriate for the location * @param     locpid     Location pid * @param     mappid     Map pid * @param     type       Reinforcements weight * * @return PID number 

```angelscript
uint GetPid(uint locpid, uint mappid, uint type)
```

### GetBag

* * Gets the bag number for the reinforcement guard appropriate for the location * @param     locpid     Location pid * @param     mappid     Map pid * @param     type       Reinforcements weight * * @return Bag number 

```angelscript
uint GetBag(uint locpid, uint mappid, uint type)
```

### GetLevel

* * Gets the level for the reinforcement guard appropriate for the location * @param     locpid     Location pid * @param     mappid     Map pid * @param     type       Reinforcements weight * * @return Level 

```angelscript
uint GetLevel(uint locpid, uint mappid, uint type)
```

### GetTeamId

* * Gets the team id for the reinforcement guard appropriate for the location * @param     locpid     Location pid * @param     mappid     Map pid * @param     type       Reinforcements weight * * @return Team id 

```angelscript
uint GetTeamId(uint locpid, uint mappid, uint type)
```

### GetDialog

* * Gets the dialog id for the reinforcement guard appropriate for the location * @param     locpid     Location pid * @param     mappid     Map pid * @param     type       Reinforcements weight * * @return DIalog id 

```angelscript
uint GetDialog(uint locpid, uint mappid, uint type)
```

### CallReinforcements

* * Summons the reinforcement guards * @param     enemy     Critter that will be attacked by the guard * @param     map       Map instance on which the guard will spawn * 

```angelscript
uint CallReinforcements(array<uint>@ enemies, CAlertMap& alert, uint amount, uint type)
```

### _ReinforcementInit

```angelscript
void _ReinforcementInit(Critter& npc, bool firstTime)
```

### _ReinforcementIdle

```angelscript
void _ReinforcementIdle(Critter& npc)
```

### _ReinforcementFinish

```angelscript
void _ReinforcementFinish(Critter& npc, bool deleted)
```

### _ReinforcementPlaneEnd

```angelscript
int _ReinforcementPlaneEnd(Critter& npc, NpcPlane& plane, int reason, Critter@ someCr, Item@ someItem)
```

### log

```angelscript
void log(Critter& cr, int, int, int)
```

### logthis

```angelscript
void logthis(Critter& cr, int, int, int)
```

### showsettings

```angelscript
void showsettings(Critter& cr, int, int, int)
```

### setsettings

```angelscript
void setsettings(Critter& cr, int n, int val, int)
```

### clear

```angelscript
void clear(Critter& cr, int, int, int)
```

### observer

```angelscript
void observer(Critter& cr, int, int, int)
```

### ExecObserve

```angelscript
void ExecObserve(uint n, string& str)
```


