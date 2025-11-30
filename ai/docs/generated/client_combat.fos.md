---
title: client_combat.fos
description: " FOnline: 2238 Rotators  client_combat.fos ..."
---

# client_combat.fos


FOnline: 2238
Rotators

client_combat.fos


## Includes

- `_client_defines.fos`
- `_macros.fos`
- `combat_h.fos`
- `lexems_h.fos`
- `config_file_h.fos`
- `client_utils_h.fos`

## Classes

### CCombatLog

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| MsgAttNormColor | `string` |  |  |
| MsgAttCritColor | `string` |  |  |
| MsgAttKillColor | `string` |  |  |
| MsgDefNormColor | `string` |  |  |
| MsgDefCritColor | `string` |  |  |
| MsgDefKillColor | `string` |  |  |


## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| CombatLog | `[CCombatLog](client_combat.fos.md)` |  |  |

## Functions

### CombatLogConfig

```angelscript
void CombatLogConfig()
```

### checkBonus

```angelscript
int checkBonus(ItemCl@ it, int bonusType)
```

### to_hit

///////////////////////////////////////////////////////////////////////////////////////////////// To-hit chance.

```angelscript
int to_hit(CritterCl& chosen, CritterCl& target, ProtoItem& weapon, uint8 weaponMode)
```

### GetHitAim

```angelscript
uint GetHitAim(int hitLocation)
```

### hit_aim

///////////////////////////////////////////////////////////////////////////////////////////////// Override aim location set by player through targetting screen or simple click on target.

```angelscript
void hit_aim(uint8& aim)
```

### combat_result

///////////////////////////////////////////////////////////////////////////////////////////////// Combat results.

```angelscript
void combat_result(array<uint>& data)
```


