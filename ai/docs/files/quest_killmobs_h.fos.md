---
title: quest_killmobs_h.fos
description: " FOnline: 2238 Rotators  quest_killmobs_h.fos ..."
---

# quest_killmobs_h.fos


FOnline: 2238
Rotators

quest_killmobs_h.fos


## Includes

- `_maps.fos`
- `_vars.fos`
- `_macros.fos`
- `mapdata_h.fos`
- `messages_h.fos`
- `npc_common_h.fos`
- `npc_planes_h.fos`
- `_basetypes.fos`
- `logging_h.fos`

## Included By

- [player_dungeon_toxic.fos](player_dungeon_toxic.fos.md)
- [player_dungeonla.fos](player_dungeonla.fos.md)
- [player_dungeonlacity.fos](player_dungeonlacity.fos.md)
- [quest_advent.fos](quest_advent.fos.md)
- [quest_advent2.fos](quest_advent2.fos.md)
- [quest_advent3.fos](quest_advent3.fos.md)
- [quest_advent4.fos](quest_advent4.fos.md)
- [quest_advent5.fos](quest_advent5.fos.md)
- [quest_advent6.fos](quest_advent6.fos.md)
- [quest_advent7.fos](quest_advent7.fos.md)
- [quest_boss1.fos](quest_boss1.fos.md)
- [quest_boss10.fos](quest_boss10.fos.md)
- [quest_boss11.fos](quest_boss11.fos.md)
- [quest_boss12.fos](quest_boss12.fos.md)
- [quest_boss13.fos](quest_boss13.fos.md)
- [quest_boss14.fos](quest_boss14.fos.md)
- [quest_boss1sim.fos](quest_boss1sim.fos.md)
- [quest_boss2.fos](quest_boss2.fos.md)
- [quest_boss3.fos](quest_boss3.fos.md)
- [quest_boss4.fos](quest_boss4.fos.md)
- [quest_boss5.fos](quest_boss5.fos.md)
- [quest_boss6.fos](quest_boss6.fos.md)
- [quest_boss7.fos](quest_boss7.fos.md)
- [quest_boss8.fos](quest_boss8.fos.md)
- [quest_boss9.fos](quest_boss9.fos.md)
- [quest_cop.fos](quest_cop.fos.md)
- [quest_copsim.fos](quest_copsim.fos.md)
- [quest_dailycopboss.fos](quest_dailycopboss.fos.md)
- [quest_dailyfarm1.fos](quest_dailyfarm1.fos.md)
- [quest_evil.fos](quest_evil.fos.md)
- [quest_floaters.fos](quest_floaters.fos.md)
- [quest_fota.fos](quest_fota.fos.md)
- [quest_hub_sad_farmer.fos](quest_hub_sad_farmer.fos.md)
- [quest_hubo.fos](quest_hubo.fos.md)
- [quest_inde1.fos](quest_inde1.fos.md)
- [quest_inde2.fos](quest_inde2.fos.md)
- [quest_inde3.fos](quest_inde3.fos.md)
- [quest_indea.fos](quest_indea.fos.md)
- [quest_indeb.fos](quest_indeb.fos.md)
- [quest_indec.fos](quest_indec.fos.md)
- [quest_la_dogs.fos](quest_la_dogs.fos.md)
- [quest_loan.fos](quest_loan.fos.md)
- [quest_loansim.fos](quest_loansim.fos.md)
- [quest_morm.fos](quest_morm.fos.md)
- [quest_mutar.fos](quest_mutar.fos.md)
- [quest_mutarsim.fos](quest_mutarsim.fos.md)
- [quest_noire1.fos](quest_noire1.fos.md)
- [quest_skyt.fos](quest_skyt.fos.md)
- [survival.fos](survival.fos.md)
- [survivalclowns.fos](survivalclowns.fos.md)
- [survivalfloat.fos](survivalfloat.fos.md)
- [survivalgeckos.fos](survivalgeckos.fos.md)
- [survivalrats.fos](survivalrats.fos.md)
- [survivalzombies.fos](survivalzombies.fos.md)

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| ALL_KILLED | `(2)` |  |
| IDLE_NORMAL | `(3000)` |  |

## Functions

### GetOwnerId

```angelscript
uint GetOwnerId(Map& map)
```

### SetOwnerId

```angelscript
void SetOwnerId(Map& map, uint playerId)
```

### MobIdle

```angelscript
void MobIdle(Critter& mob)
```

### MobShowCritter

```angelscript
void MobShowCritter(Critter& mob, Critter& showCrit)
```

### MobsDead

Checks if there are other mobs (with given pids) alive

```angelscript
bool MobsDead(Map& map, array<uint16>& pids)
```

### MobAttacked

```angelscript
bool MobAttacked(Critter& cr, Critter& attacker)
```

### MobOnMessage

```angelscript
void MobOnMessage(Critter& cr, Critter& fromCr, int message, int value)
```

### check_owner

```angelscript
void check_owner(Critter& cr, int, int, int)
```


