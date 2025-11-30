---
title: combat_h.fos
description: " FOnline: 2238 Rotators  combat_h.fos ..."
---

# combat_h.fos


FOnline: 2238
Rotators

combat_h.fos


## Included By

- [cheats.fos](cheats.fos.md)
- [client_combat.fos](client_combat.fos.md)
- [client_interface.fos](client_interface.fos.md)
- [combat.fos](combat.fos.md)

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| _COMBAT_H_ |  |  |
| HF_KNOCKOUT | `(0x00000001)` | Critical hit/miss flags |
| HF_KNOCKDOWN | `(0x00000002)` |  |
| HF_CRIPPLED_LEFT_LEG | `(0x00000004)` |  |
| HF_CRIPPLED_RIGHT_LEG | `(0x00000008)` |  |
| HF_CRIPPLED_LEFT_ARM | `(0x00000010)` |  |
| HF_CRIPPLED_RIGHT_ARM | `(0x00000020)` |  |
| HF_BLINDED | `(0x00000040)` |  |
| HF_DEATH | `(0x00000080)` |  |
| HF_ON_FIRE | `(0x00000400)` |  |
| HF_BYPASS_ARMOR | `(0x00000800)` |  |
| HF_DROPPED_WEAPON | `(0x00004000)` |  |
| HF_LOST_NEXT_TURN | `(0x00008000)` |  |
| HF_RANDOM | `(0x00200000)` |  |
| MF_KNOCKED_DOWN | `(0x00000002)` |  |
| MF_ON_FIRE | `(0x00000400)` |  |
| MF_WEAPON_EXPLODED | `(0x00001000)` |  |
| MF_WEAPON_DESTROYED | `(0x00002000)` |  |
| MF_WEAPON_DROPPED | `(0x00004000)` |  |
| MF_LOST_NEXT_TURN | `(0x00008000)` |  |
| MF_HIT_SELF | `(0x00010000)` |  |
| MF_LOST_REST_OF_AMMO | `(0x00020000)` |  |
| MF_FIRED_DUD_SHOT | `(0x00040000)` |  |
| MF_HURT_SELF | `(0x00080000)` |  |
| MF_HIT_RANDOMLY | `(0x00100000)` |  |
| MF_CRIPPLED_RANDOM_LIMB | `(0x00200000)` |  |
| MF_WAS_KILLED | `(0x10000000)` |  |
| WS_UNARMED | `(1)` | for WeaponSubtype |
| WS_MELEE | `(2)` |  |
| WS_THROWING | `(3)` |  |
| WS_GUN | `(4)` |  |
| _GetCritterArmor | `# (cr_, head_)(cr_.GetItem(0, (head_) ? SLOT_HEAD : SLOT_ARMOR))` |  |
| COMBAT_AMMO_AP | `# (ammo_) (valid(ammo_) ? (ammo_.Ammo_DTDiv > 0) : false)` |  |
| COMBAT_WEAPON_ALLOWS_SD | `# (__weapon)     (__weapon.Proto.ProtoId == PID_14MM_PISTOL || __weapon.Proto.ProtoId == PID_223_PISTOL)` | todo: move to proto |
| MODE_PRIMARY_ATTACK | `(0)` | melee weapon attack mode by Cubik & John (from 2155) |
| MODE_SECONDARY_ATTACK | `(1)` |  |

