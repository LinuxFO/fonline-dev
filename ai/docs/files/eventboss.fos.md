---
title: eventboss.fos
description: " FOnline: 2238 Rotators  eventboss.fos ..."
---

# eventboss.fos


FOnline: 2238
Rotators

eventboss.fos


## Includes

- `_macros.fos`
- `_animation.fos`
- `combat_msg.fos`
- `eventboss_h.fos`
- `traps_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| HF_KNOCKOUT | `(0x00000001)` |  |

## Classes

### DynamiteThrow

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| boss | `[MelchiorBoss](eventboss.fos.md)@` |  |  |
| dynamites | `array<uint>` |  |  |
| dynamiteI | `uint` |  |  |
| timer | `uint` |  |  |

**Methods**

#### AttackPrepareStart
```angelscript
void AttackPrepareStart()
```

#### AttackCommence
```angelscript
void AttackCommence()
```

#### MakeDynamite
```angelscript
Item@ MakeDynamite(Critter@ cr, uint timer)
```

#### AttackRecuperationEnd
```angelscript
void AttackRecuperationEnd()
```

### ImbaPunch

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| boss | `[MelchiorBoss](eventboss.fos.md)@` |  |  |

**Methods**

#### AttackPrepareStart
```angelscript
void AttackPrepareStart()
```

#### AttackCommence
```angelscript
void AttackCommence()
```

#### AttackRecuperationEnd
```angelscript
void AttackRecuperationEnd()
```

### MelchiorBoss

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| targetType | `int` |  |  |

**Methods**

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

### SilentKill

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| boss | `[GhostBoss](eventboss.fos.md)@` |  |  |
| timer | `uint` |  |  |

**Methods**

#### AttackPrepareStart
```angelscript
void AttackPrepareStart()
```

#### AttackCommence
```angelscript
void AttackCommence()
```

#### AttackRecuperationEnd
```angelscript
void AttackRecuperationEnd()
```

### GhostBoss

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| wasHit | `bool` |  |  |
| targetType | `int` |  |  |
| victimId | `uint` |  |  |

**Methods**

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

### PatternBoss

**Methods**

#### aggressionStart
called after beggining of the fight

```angelscript
void aggressionStart()
```

#### bossSee
called when any of bosses critter sees new critter

```angelscript
void bossSee(Critter& cr, Critter& shownCr)
```

#### bossAttacked
called when bosses critter attacked

```angelscript
bool bossAttacked(Critter& cr, Critter& attacker)
```

#### bossHit
called after attack when damages have been done

```angelscript
void bossHit(Critter& cr, Critter@ attacker, int dmg)
```

#### bossKilled
called when any of bosses critters is killed

```angelscript
void bossKilled(Critter& cr, Critter@ attacker)
```

#### bossFinish
```angelscript
void bossFinish(Critter& cr, bool deleted)
```


## Functions

### isMod

```angelscript
bool isMod(Critter& crit)
```

### isSameTeam

```angelscript
bool isSameTeam(Critter& crit1, Critter& crit2)
```

### isMerc

```angelscript
bool isMerc(Critter& crit)
```

### spawnMelchior

```angelscript
void spawnMelchior(Critter& player, int x, int y, int p2)
```

### spawnGhost

```angelscript
void spawnGhost(Critter& player, int x, int y, int p2)
```

### AddBoss

```angelscript
void AddBoss(CBoss@ boss)
```

### GetBoss

```angelscript
CBoss@ GetBoss(uint id)
```

### _BossMelchiorInit

```angelscript
void _BossMelchiorInit(Critter& boss, bool firstTime)
```

### _BossGhostInit

```angelscript
void _BossGhostInit(Critter& boss, bool firstTime)
```


