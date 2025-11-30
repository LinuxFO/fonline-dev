---
title: eventboss_h.fos
description: " FOnline: 2238 Rotators  eventboss_h.fos ..."
---

# eventboss_h.fos


FOnline: 2238
Rotators

eventboss_h.fos


## Included By

- [eventboss.fos](eventboss.fos.md)

## Classes

### CBoss

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| id | `uint` |  |  |
| timeEvent | `uint` |  |  |
| critterList | `array<uint>` |  |  |
| attackChances | `array<int>` |  |  |
| totalChance | `int` |  |  |
| currentAttack | `uint` |  |  |
| attackPrepareTimes | `array<int>` |  |  |
| attackRecuperations | `array<int>` |  |  |
| patern | `bool` |  |  |

**Methods**

#### SetId
```angelscript
void SetId(uint id)
```

#### AddAttack
```angelscript
void AddAttack(IAttack@ attack, int chance, int timeBeforeAttack, int timeAfterAttack)
```

#### AddCritter
```angelscript
void AddCritter(Critter& crit)
```

#### MakeAgressive
```angelscript
void MakeAgressive()
```

#### startAttack
```angelscript
void startAttack()
```

#### commenceAttack
```angelscript
void commenceAttack()
```

#### finishAttack
```angelscript
void finishAttack()
```

#### aggressionStart
```angelscript
void aggressionStart()
```

#### bossSee
```angelscript
void bossSee(Critter& cr, Critter& shownCr)
```

#### bossAttacked
```angelscript
bool bossAttacked(Critter& cr, Critter& attacker)
```

#### bossHit
```angelscript
void bossHit(Critter& cr, Critter@ attacker, int dmg)
```

#### bossKilled
```angelscript
void bossKilled(Critter& cr, Critter@ attacker)
```

#### bossFinish
```angelscript
void bossFinish(Critter& cr, bool deleted)
```


## Functions

### e_CommenceAttack

```angelscript
uint e_CommenceAttack(array<int>@ vals)
```

### e_FinishAttack

```angelscript
uint e_FinishAttack(array<int>@ vals)
```

### _BossShowCritter

```angelscript
void _BossShowCritter(Critter& cr, Critter& shownCr)
```

### _BossAttacked

```angelscript
bool _BossAttacked(Critter& cr, Critter& attacker)
```

### _BossHit

```angelscript
uint _BossHit(array<uint>@ values)
```

### _BossDead

```angelscript
void _BossDead(Critter& cr, Critter@ killer)
```

### _BossFinish

```angelscript
void _BossFinish(Critter& cr, bool deleted)
```


