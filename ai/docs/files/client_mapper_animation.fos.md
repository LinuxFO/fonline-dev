---
title: client_mapper_animation.fos
description: " FOnline: 2238 Rotators  client_mapper_animation.fos ..."
---

# client_mapper_animation.fos


FOnline: 2238
Rotators

client_mapper_animation.fos


## Includes

- `_defines.fos`
- `_animation.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| ANIM1_FALLOUT_UNARMED | `(1)` | Fallout animations |
| ANIM1_FALLOUT_DEAD | `(2)` |  |
| ANIM1_FALLOUT_KNOCKOUT | `(3)` |  |
| ANIM1_FALLOUT_KNIFE | `(4)` |  |
| ANIM1_FALLOUT_CLUB | `(5)` |  |
| ANIM1_FALLOUT_HAMMER | `(6)` |  |
| ANIM1_FALLOUT_SPEAR | `(7)` |  |
| ANIM1_FALLOUT_PISTOL | `(8)` |  |
| ANIM1_FALLOUT_UZI | `(9)` |  |
| ANIM1_FALLOUT_SHOOTGUN | `(10)` |  |
| ANIM1_FALLOUT_RIFLE | `(11)` |  |
| ANIM1_FALLOUT_MINIGUN | `(12)` |  |
| ANIM1_FALLOUT_ROCKET_LAUNCHER | `(13)` |  |
| ANIM1_FALLOUT_AIM | `(14)` |  |
| ANIM2_FALLOUT_STAY | `(1)` |  |
| ANIM2_FALLOUT_WALK | `(2)` |  |
| ANIM2_FALLOUT_SHOW | `(3)` |  |
| ANIM2_FALLOUT_HIDE | `(4)` |  |
| ANIM2_FALLOUT_DODGE_WEAPON | `(5)` |  |
| ANIM2_FALLOUT_THRUST | `(6)` |  |
| ANIM2_FALLOUT_SWING | `(7)` |  |
| ANIM2_FALLOUT_PREPARE_WEAPON | `(8)` |  |
| ANIM2_FALLOUT_TURNOFF_WEAPON | `(9)` |  |
| ANIM2_FALLOUT_SHOOT | `(10)` |  |
| ANIM2_FALLOUT_BURST | `(11)` |  |
| ANIM2_FALLOUT_FLAME | `(12)` |  |
| ANIM2_FALLOUT_THROW_WEAPON | `(13)` |  |
| ANIM2_FALLOUT_DAMAGE_FRONT | `(15)` |  |
| ANIM2_FALLOUT_DAMAGE_BACK | `(16)` |  |
| ANIM2_FALLOUT_KNOCK_FRONT | `(1)` |  |
| ANIM2_FALLOUT_KNOCK_BACK | `(2)` |  |
| ANIM2_FALLOUT_STANDUP_BACK | `(8)` |  |
| ANIM2_FALLOUT_STANDUP_FRONT | `(10)` |  |
| ANIM2_FALLOUT_PICKUP | `(11)` |  |
| ANIM2_FALLOUT_USE | `(12)` |  |
| ANIM2_FALLOUT_DODGE_EMPTY | `(14)` |  |
| ANIM2_FALLOUT_PUNCH | `(17)` |  |
| ANIM2_FALLOUT_KICK | `(18)` |  |
| ANIM2_FALLOUT_THROW_EMPTY | `(19)` |  |
| ANIM2_FALLOUT_RUN | `(20)` |  |
| ANIM2_FALLOUT_SMOKE | `(21)` |  |
| ANIM2_FALLOUT_DEAD_FRONT | `(1)` |  |
| ANIM2_FALLOUT_DEAD_BACK | `(2)` |  |
| ANIM2_FALLOUT_DEAD_BLOODY_SINGLE | `(4)` |  |
| ANIM2_FALLOUT_DEAD_BURN | `(5)` |  |
| ANIM2_FALLOUT_DEAD_BLOODY_BURST | `(6)` |  |
| ANIM2_FALLOUT_DEAD_BURST | `(7)` |  |
| ANIM2_FALLOUT_DEAD_PULSE | `(8)` |  |
| ANIM2_FALLOUT_DEAD_LASER | `(9)` |  |
| ANIM2_FALLOUT_DEAD_BURN2 | `(10)` |  |
| ANIM2_FALLOUT_DEAD_PULSE_DUST | `(11)` |  |
| ANIM2_FALLOUT_DEAD_EXPLODE | `(12)` |  |
| ANIM2_FALLOUT_DEAD_FUSED | `(13)` |  |
| ANIM2_FALLOUT_DEAD_BURN_RUN | `(14)` |  |
| ANIM2_FALLOUT_DEAD_FRONT2 | `(15)` |  |
| ANIM2_FALLOUT_DEAD_BACK2 | `(16)` |  |

## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| lastMode | `uint8` | `0` |  |
| _disguise999 | `string@` | `null` |  |

## Functions

### SetLastMode

```angelscript
void SetLastMode(uint8 mode)
```

### critter_action

///////////////////////////////////////////////////////////////////////////////////////////////// Call on some critter action.

```angelscript
void critter_action(bool localCall, CritterCl& cr, int action, int actionExt, ItemCl@ item)
```

### animation2d_process

///////////////////////////////////////////////////////////////////////////////////////////////// Call before 2d animation playing.

```angelscript
void animation2d_process(bool animateStay, CritterCl& cr, uint anim1, uint anim2, ItemCl@ item)
```

### animation3d_process

///////////////////////////////////////////////////////////////////////////////////////////////// Call before 3d animation playing.

```angelscript
void animation3d_process(bool animateStay, CritterCl& cr, uint anim1, uint anim2, ItemCl@ item)
```

### critter_animation

```angelscript
string@ critter_animation(int animType, uint crType, uint anim1, uint anim2, uint& pass, uint& flags, int& ox, int& oy)
```

### disguise999

```angelscript
void disguise999(int, int, int, string@ str, array<int>@)
```

### critter_animation_substitute

```angelscript
bool critter_animation_substitute(int animType, uint crTypeBase, uint anim1Base, uint anim2Base, uint& crType, uint& anim1, uint& anim2)
```

### critter_animation_fallout

///////////////////////////////////////////////////////////////////////////////////////////////// Convert from common to fallout specific

```angelscript
bool critter_animation_fallout(uint crType, uint& anim1, uint& anim2, uint& anim1ex, uint& anim2ex, uint& flags)
```

### PlayAnimSound

```angelscript
void PlayAnimSound(uint crType, int gender, uint anim1, uint anim2)
```


