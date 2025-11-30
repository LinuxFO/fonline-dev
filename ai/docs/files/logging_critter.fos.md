---
title: logging_critter.fos
description: " FOnline: 2238 Rotators  logging_critter.fos ..."
---

# logging_critter.fos


FOnline: 2238
Rotators

logging_critter.fos


## Includes

- `_macros.fos`
- `logging_h.fos`
- `utils_h.fos`

## Functions

### LogAction

```angelscript
void LogAction(Critter& cr, string& s)
```

### _ShowCritter

```angelscript
void _ShowCritter(Critter& cr, Critter& showCrit)
```

### _HideCritter

```angelscript
void _HideCritter(Critter& cr, Critter& hideCrit)
```

### _Attacked

```angelscript
bool _Attacked(Critter& cr, Critter& attacker)
```

### _Attack

```angelscript
bool _Attack(Critter& cr, Critter& target)
```

### _SomeoneStealing

```angelscript
void _SomeoneStealing(Critter& cr, Critter& fromCr, Critter& thief, bool success, Item& item, uint count)
```

### _SomeoneDied

```angelscript
void _SomeoneDied(Critter& cr, Critter& killed, Critter@ killer)
```

### _SomeoneAttack

```angelscript
void _SomeoneAttack(Critter& cr, Critter& fromCr, Critter& target)
```

### GetOnText

```angelscript
string GetOnText(Critter@ onCritter, Item@ onItem, Scenery@ onScenery)
```

### SayHow

```angelscript
string SayHow(int sayType, int possessedId)
```

### unsafe_Say

```angelscript
void unsafe_Say(Critter& cr, int sayType, int possessedId, int p2, string@ sayString, array<int>@ param4)
```

### unsafe_SayMsgLog

```angelscript
void unsafe_SayMsgLog(Critter& cr, int sayType, int possessedId, int p2, string@ sayString, array<int>@ param4)
```

### unsafe_Ping

```angelscript
void unsafe_Ping(Critter& cr, int sayType, int possessedId, int p2, string@ sayString, array<int>@ param4)
```

### _SomeoneUseSkill

```angelscript
void _SomeoneUseSkill(Critter& cr, Critter& fromCr, int skill, Critter@ onCritter, Item@ onItem, Scenery@ onScenery)
```

### _DropItem

```angelscript
void _DropItem(Critter& cr, Item& item)
```

### SetCritterEvents

```angelscript
void SetCritterEvents(Critter& cr)
```


