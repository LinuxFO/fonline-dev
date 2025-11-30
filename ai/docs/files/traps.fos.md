---
title: traps.fos
description: " FOnline: 2238 Rotators  traps.fos ..."
---

# traps.fos


FOnline: 2238
Rotators

traps.fos


## Includes

- `_macros.fos`
- `utils_h.fos`
- `groups_h.fos`
- `entire.fos`
- `npc_common_h.fos`
- `traps_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __TRAPS_MODULE__ |  |  |

## Functions

### MakeSpearTrap

* * Sets the spear trap script for the item and assigns its parameters * @param     trap			The item to become a spear trap * @param     complexity       Complexity level for disarming the trap * @param     hideSkill		Value of traps skill used to hide the item, 0 to disable * @param     spearcount       Number of spear ammunition 

```angelscript
void MakeSpearTrap(Item& trap, uint complexity, uint hideSkill, uint spearcount)
```

### _SpearTrap

shoots spear if player walks on it. Val1 denotes number of shots it can do

```angelscript
void _SpearTrap(Item& item, bool firstTime)
```

### _SpearTrapWalk

```angelscript
void _SpearTrapWalk(Item& trap, Critter& cr, bool entered, uint8 dir)
```

### ShootSpear

```angelscript
void ShootSpear(Item& trap, Critter& cr)
```

### MakeGenericShotTrap

* * Sets the generic shot trap script for the item and assigns its parameters * @param     trap     The item to become a generic shot trap * @param     complexity       Complexity level for disarming the trap * @param     hideSkill     Value of traps skill used to hide the item, 0 to disable * @param     pid       Proto id for object to be shot * @param     dmgmin       Minimum amount of damage dealt * @param     dmgmax       Maximum amount of damage dealt 

```angelscript
void MakeGenericShotTrap(Item& trap, uint complexity, uint hideSkill, uint16 pid, uint dmgmin, uint dmgmax)
```

### _GenericShot

```angelscript
void _GenericShot(Item& item, bool firstTime)
```

### _GenericShotWalk

```angelscript
void _GenericShotWalk(Item& trap, Critter& cr, bool entered, uint8 dir)
```

### ShootGeneric

```angelscript
void ShootGeneric(Item& trap, Critter& cr)
```

### _TrapUse

```angelscript
bool _TrapUse(Item& trap, Critter& cr, int skill)
```

### MakeBearTrap

* * Sets the bear trap script for the item and assigns its parameters * @param     trap     The item to become a bear trap * @param     complexity       Complexity level for disarming the trap * @param     hideSkill     Value of traps skill used to hide the item, 0 to disable * @param     bonusDamage       Bonus damage dealt upon the trap activation 

```angelscript
void MakeBearTrap(Item& trap, uint complexity, uint hideSkill, uint bonusDamage)
```

### _BearTrapInit

```angelscript
void _BearTrapInit(Item& item, bool firstTime)
```

### _BearTrapWalk

```angelscript
void _BearTrapWalk(Item& item, Critter& cr, bool entered, uint8 dir)
```

### e_Clamp

```angelscript
uint e_Clamp(array<uint>@ values)
```

### MakeAlarmTrap

* * Sets the alarm (critter summoning) trap script for the item and assigns its parameters * @param     trap     The item to become an alarm trap * @param     complexity       Complexity level for disarming the trap * @param     hideSkill     Value of traps skill used to hide the item, 0 to disable * @param     pid       Proto id for critters spawned on trap activation * @param     min       Minimum number of critters to spawn * @param     max       Maximum number of critters to spawn * @param     bag       Bag used by the spawned critter * @param     level     Level of the spawned critters * @param     entire    Entire number around which the critters will be spawned 

```angelscript
void MakeAlarmTrap(Item& trap, uint complexity, uint hideSkill, uint16 pid, uint8 min, uint8 max, uint16 bag, uint8 level, uint8 entire)
```

### _AlarmTrapInit

```angelscript
void _AlarmTrapInit(Item& item, bool firstTime)
```

### _AlarmTrapWalk

```angelscript
void _AlarmTrapWalk(Item& item, Critter& cr, bool entered, uint8 dir)
```

### e_SummonEnemies

```angelscript
uint e_SummonEnemies(array<uint>@ values)
```

### ClearWalkTrap

* * Clears the script of walk-in type trap, such as mines or bear traps. * @param     item     The item to be cleared 

```angelscript
void ClearWalkTrap(Item& item)
```


