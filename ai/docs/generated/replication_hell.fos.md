---
title: replication_hell.fos
---

# replication_hell.fos

## Includes

- `_macros.fos`
- `_vars.fos`
- `_animation.fos`
- `itempid.h`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| TIME_TO_DEATH | `( REAL_MINUTE( Random(110, 130 ) ) )` |  |

## Functions

### _TurretInit

```angelscript
void _TurretInit( Critter& turret, bool firstTime )
```

### cte_KillTurret

```angelscript
uint cte_KillTurret( Critter& cr, int identifier, uint& rate )
```

### t_Electro

```angelscript
void t_Electro( Critter& cr, Scenery& trigger, bool entered, uint8 dir )
```

### _TurretSmthUseSkill

```angelscript
void _TurretSmthUseSkill( Critter& turret, Critter& hacker, int skill, Critter@ onCritter, Item@ onItem, Scenery@ onScenery )
```

### _TurretSmthAttack

```angelscript
void _TurretSmthAttack( Critter& turret, Critter& attacker, Critter& target )
```


