---
title: combat_msg.fos
description: " FOnline: 2238 Rotators  combat_msg.fos ..."
---

# combat_msg.fos


FOnline: 2238
Rotators

combat_msg.fos


## Included By

- [cheats.fos](cheats.fos.md)
- [combat.fos](combat.fos.md)
- [eventboss.fos](eventboss.fos.md)

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| PTR_NULL | `(-1)` |  |
| CMSG_MISS | `(1)` | message specs note: CMSG_AIMED_HIT must be CMSG_HIT+1, CMSG_CRIT_AIMED_HIT must be CMSG_CRIT_HIT+1 |
| CMSG_CRIT_MISS | `(2)` |  |
| CMSG_CRIT_MISS_DAMAGE | `(3)` |  |
| CMSG_HIT | `(4)` |  |
| CMSG_AIMED_HIT | `(5)` |  |
| CMSG_CRIT_HIT | `(6)` |  |
| CMSG_CRIT_AIMED_HIT | `(7)` |  |
| CMSG_HIT_DEAD | `(8)` |  |
| CMSG_AIMED_HIT_DEAD | `(9)` |  |
| CMSG_CRIT_HIT_DEAD | `(10)` |  |
| CMSG_CRIT_AIMED_HIT_DEAD | `(11)` |  |
| CMSG_OOPS | `(12)` |  |
| CMSG_HIT_RANDOMLY | `(13)` |  |
| FlushResults | `# (tree)  runTree(tree, 0)` |  |

## Classes

### CombatRes

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| Res | `array<uint>` |  |  |
| Crit | `Critter@` |  |  |
| Left | `int` |  |  |
| Right | `int` |  |  |


## Functions

### AddEff

```angelscript
void AddEff(Critter@ crit, array<uint>& eff, array<CombatRes>& combatResults)
```

### runTree

```angelscript
void runTree(array<CombatRes>& combatResults, int ptr)
```


