---
title: guard.fos
description: " FOnline: 2238 Rotators  guard.fos ..."
---

# guard.fos


FOnline: 2238
Rotators

guard.fos


## Includes

- `_colors.fos`
- `_macros.fos`
- `_maps.fos`
- `_vars.fos`
- `economy.fos`
- `follower_common_h.fos`
- `groups_h.fos`
- `mapdata_h.fos`
- `messages_h.fos`
- `MsgStr.h`
- `npc_common_h.fos`
- `world_common_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __NPC_GUARDS__ |  |  |

## Functions

### InNoStealZone

several In...Zone functions are still location-specific

```angelscript
bool InNoStealZone(Critter@ cr)
```

### InNoAttackZone

```angelscript
bool InNoAttackZone(Critter@ cr)
```

### InNoBombZone

```angelscript
bool InNoBombZone(Critter@ cr)
```

### InWeaponAllowedZone

Is it allowed to carry weapon openly

```angelscript
bool InWeaponAllowedZone(Critter@ cr)
```

### InDrugsAllowedZone

```angelscript
bool InDrugsAllowedZone(Critter@ cr)
```

### IsWeapon

```angelscript
bool IsWeapon(Item@ item)
```

### IsDrug

```angelscript
bool IsDrug(Item@ item)
```

### e_CheckWeapon

Check if player has put down weapon, else open fire.

```angelscript
uint e_CheckWeapon(array<uint>@ values)
```

### e_CheckDrug

```angelscript
uint e_CheckDrug(array<uint>@ values)
```

### CreateWeaponCheckEvent

```angelscript
uint CreateWeaponCheckEvent(Critter& guard, Critter& player)
```

### CreateDrugCheckEvent

```angelscript
uint CreateDrugCheckEvent(Critter& guard, Critter& player)
```

### CheckForDrugs

```angelscript
void CheckForDrugs(Critter& guard, Critter& crit)
```

### CheckForWeapons

```angelscript
void CheckForWeapons(Critter& guard, Critter& crit)
```

### CheckHealing

```angelscript
void CheckHealing(Critter& cr)
```

### CheckInventory

```angelscript
void CheckInventory(Critter& guard)
```

### GuardInit

```angelscript
void GuardInit(Critter& guard)
```

### GuardPerks

```angelscript
void GuardPerks(Critter& cr)
```

### GuardOnIdle

```angelscript
void GuardOnIdle(Critter& guard)
```

### DetectStealing

```angelscript
bool DetectStealing(Critter& cr, Critter& target, Critter& thief)
```

### GuardOnSomeoneSteal

```angelscript
void GuardOnSomeoneSteal(Critter& guard, Critter& target, Critter& thief, bool success, Item& item, uint count)
```

### WillCallForHelp

```angelscript
bool WillCallForHelp(uint locid)
```

### GuardOnShowCritter

```angelscript
void GuardOnShowCritter(Critter& cr, Critter& target)
```

### GuardOnMessage

```angelscript
void GuardOnMessage(Critter& guard, Critter& sender, int num, int val)
```


