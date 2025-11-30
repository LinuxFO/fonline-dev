---
title: combat.fos
description: " FOnline: 2238 Rotators  combat.fos ..."
---

# combat.fos


FOnline: 2238
Rotators

combat.fos


## Includes

- `_basetypes.fos`
- `_macros.fos`
- `combat_msg.fos`
- `critical_table.fos`
- `critical_failures.fos`
- `logging_h.fos`
- `npc_ai.fos`
- `utils_h.fos`
- `mapdata_h.fos`
- `MsgStr.h`
- `combat_h.fos`
- `_npc_pids.fos`

## Classes

### AttackStruct

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| Attacker | `Critter@` | `null` |  |
| RealWeapon | `Item@` | `null` |  |
| Hx | `uint16` | `0` |  |
| Hy | `uint16` | `0` |  |
| Aim | `uint8` | `HIT_LOCATION_UNCALLED` |  |
| AimHead | `bool` | `false` |  |
| IsBurst | `bool` | `false` |  |
| BloodyMess | `bool` | `false` |  |
| CombatMessage | `bool` | `false` |  |
| IsUnarmed | `bool` | `false` |  |
| WeaponPerk | `int` | `-1` |  |
| WeaponSubtype | `uint8` | `0` |  |
| DmgMin | `int` | `0` |  |
| DmgMax | `int` | `0` |  |
| DmgType | `int` | `0` |  |
| BonusDmg | `int` | `0` |  |
| DmgMul | `int` | `2` |  |
| DRMod | `int` | `0` |  |
| DMMod | `int` | `1` |  |
| DDMod | `int` | `1` |  |
| TargetId | `uint` | `0` |  |
| TargetHit | `bool` | `false` |  |
| ShowHitAnimForce | `bool` | `false` |  |
| Ammo | `ProtoItem@` | `null` |  |
| SilentDeathEffect | `bool` | `false` |  |
| ammoPid | `uint16` |  |  |
| weaponPid | `uint16` |  |  |
| weaponMode | `int8` |  |  |

**Methods**

#### set_Aim
```angelscript
void set_Aim(uint8 aim)
```

#### get_Aim
```angelscript
uint8 get_Aim()
```

#### SelectWeaponBonus
```angelscript
int SelectWeaponBonus(int Int_Val_WeaponBonus)
```


## Functions

### SelectArmorBonus

```angelscript
int SelectArmorBonus(Item@ armor, int Int_Val_ArmorBonus)
```

### CombatAttack

```angelscript
void CombatAttack(Critter& cr, Critter& target, ProtoItem& weapon, uint8 weaponMode, ProtoItem@ ammo)
```

### ApplyDamage

```angelscript
void ApplyDamage(AttackStruct& attack, Critter& target, uint rounds, bool isCritical, bool intentionally, array<CombatRes>& results, int CriticalChance)
```

### CommenceExplosion

```angelscript
void CommenceExplosion(AttackStruct& attack, Map@ map, uint16 tx, uint16 ty, Critter@ target, uint weapPid, bool isCritical, uint intentionallyId, bool isRocket, array<CombatRes>& results, bool isExplodeRocket)
```

### CommenceExplosionEx

```angelscript
void CommenceExplosionEx(Critter@ attacker, Map@ map, uint16 tx, uint16 ty, Critter@ target, uint weapPid, bool isCritical, uint intentionallyId, bool isRocket, bool isExplodeRocket)
```

### CommenceExplosionHexEx

```angelscript
void CommenceExplosionHexEx(Critter@ attacker, Map@ map, uint16 tx, uint16 ty, Critter@ target, uint weapPid, Item@ usedWeapon, uint ammoPid, bool isCritical, uint intentionallyId, bool isRocket, bool isExplodeRocket)
```

### CommenceDischargeEx

```angelscript
void CommenceDischargeEx(Critter@ attacker, Map@ map, uint16 tx, uint16 ty, uint dmgRad, uint dmgMin, uint dmgMax, int effChance, uint rechargeVal)
```

### CommenceFireHex

```angelscript
void CommenceFireHex(Critter@ attacker, Map@ map, uint16 tx, uint16 ty, uint8 radius)
```

### _FireInit

```angelscript
void _FireInit( Item& item, bool firstTime )
```

### _FireWalk

```angelscript
void _FireWalk(Item& fire, Critter& cr, bool entered, uint8 dir )
```

### e_ProcessFireHex

```angelscript
uint e_ProcessFireHex( uint[] @ values )
```

### CriticalFailure

```angelscript
void CriticalFailure(Critter& cr, ProtoItem& weapon, uint8 weaponUse, ProtoItem@ ammo, uint eff, array<CombatRes>& results)
```

### InjureCritter

```angelscript
void InjureCritter(Critter& cr, uint dmg, uint dmgType, uint8 dir, uint attackerId)
```

### FindCritterInArray

```angelscript
int FindCritterInArray(array<Critter@>& crits, Critter& cr)
```

### GetAimApCost

```angelscript
uint GetAimApCost(int hitLocation)
```

### GetHitAim

```angelscript
uint GetHitAim(int hitLocation)
```

### RawToHit

Used by AI

```angelscript
int RawToHit(Critter& cr, Critter& target, ProtoItem@ weapon, uint8 weaponUse, ProtoItem@ ammo)
```

### NotifyOops

```angelscript
void NotifyOops(Critter@ cr, Critter@ t1, Critter@ t2, array<CombatRes>& results)
```

### NotifyMiss

```angelscript
void NotifyMiss(Critter@ cr, array<CombatRes>& results)
```

### ChooseRandomTarget

```angelscript
Critter@ ChooseRandomTarget(Map& map, Critter& cr, Critter& target, uint wpnMaxDist)
```

### GetPartialBypassChance

```angelscript
int GetPartialBypassChance(Critter& target, bool aimHead)
```

### AddCritRollWeapon

```angelscript
int AddCritRollWeapon(Item@ realWeapon)
```


