---
title: _animation.fos
description: " FOnline: 2238 Rotators  _animation.fos ..."
---

# _animation.fos


FOnline: 2238
Rotators

_animation.fos


## Included By

- [_macros.fos](_macros.fos.md)
- [all_brahmin.fos](all_brahmin.fos.md)
- [cheats.fos](cheats.fos.md)
- [client_mapper_animation.fos](client_mapper_animation.fos.md)
- [config.fos](config.fos.md)
- [eventboss.fos](eventboss.fos.md)
- [item_attributes.fos](item_attributes.fos.md)
- [main.fos](main.fos.md)
- [map_npcmap.fos](map_npcmap.fos.md)
- [prospect_miner.fos](prospect_miner.fos.md)
- [replication_hell.fos](replication_hell.fos.md)
- [talchem.fos](talchem.fos.md)

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __ANIMATION__ |  |  |
| _CritAnimate | `# (cr, anim)cr.Animate(0, anim, null, true, true)` | Animation macro |
| _CritAnimateUse | `# (cr) cr.Animate(0, ANIM2_USE, null, true, true)` |  |
| _CritAnimatePickup | `# (cr) cr.Animate(0, ANIM2_PICKUP, null, true, true)` |  |
| _CritAnimatePunch | `# (cr) cr.Animate(0, ANIM2_PUNCH_RIGHT, null, true, true)` |  |
| _CritAnimateKick | `# (cr) cr.Animate(0, ANIM2_KICK_HI, null, true, true)` |  |
| _CritAnimateThrow | `# (cr) cr.Animate(0, ANIM2_THROW, null, true, true)` |  |
| _CritAnimateThrust | `# (cr) cr.Animate(0, ANIM2_THRUST_1H, null, true, true)` |  |
| _CritAnimateSwing | `# (cr) cr.Animate(0, ANIM2_SWING_1H, null, true, true)` |  |
| _CritAnimateThrowWeap | `# (cr) cr.Animate(0, ANIM2_THROW, null, true, true)` |  |
| _CritAnimateSingle | `# (cr) cr.Animate(0, ANIM2_SINGLE, null, true, true)` |  |
| _CritAnimateBurst | `# (cr) cr.Animate(0, ANIM2_BURST, null, true, true)` |  |
| _CritAnimateFidget | `# (cr) cr.Animate(0, ANIM2_FIDGET, null, true, true)` |  |
| ANIM_TYPE_TACTICS | `(ANIM_TYPE_LAST+1)` | Anim types |
| ANIM_TYPE_ARCANUM | `(ANIM_TYPE_LAST+2)` |  |
| ANIM_TYPE_EXPERIMENTS | `(ANIM_TYPE_LAST+3)` |  |
| ANIM_FLAG_FIRST_FRAME | `(0x01)` | Anim loading flags |
| ANIM_FLAG_LAST_FRAME | `(0x02)` |  |
| ANIM1_WEAPON_MASK | `(0x000000FF)` | Anim1 Weapon / Flags 0 1 2 3 4 5 6 7 |<  Weapon   >| Manage constants |
| ANIM1_FLAGS_MASK | `(0xFFFFFF00)` |  |
| ANIM1_FLAGS_BITS | `(8)` |  |
| ANIM1_CROUCH | `(0x0100)` | Flags Tactics specific 8        9       10 1 2 3 4 5 6 7 8 9 20  1 2  3 4 5 6  7 8 9 30  1 | Crouch | Prone                       | Skin  | | Hair | | Armor | |
| ANIM1_PRONE | `(0x0200)` |  |
| ANIM1_COLOR_SKIN | `# (index)   (((index) & 0xF) << 20)` |  |
| ANIM1_COLOR_HAIR | `# (index)   (((index) & 0xF) << 24)` |  |
| ANIM1_COLOR_ARMOR | `# (index)   (((index) & 0xF) << 28)` |  |
| ANIM1_SHIELD | `(0x1000)` | Arcanum specific 8 9 10 1 2        3 4 5 6     7     8 9 20 1 2 3 4 5 6 7 8 9 30 1 | Shield       |< Palette >| |
| ANIM1_PALETTE | `# (num)         (((num) & 3) << (ANIM1_FLAGS_BITS + 8))` |  |
| ANIM1_KNIFE | `(4)` | Weapons |
| ANIM1_CLUB | `(5)` |  |
| ANIM1_HAMMER | `(6)` |  |
| ANIM1_SPEAR | `(7)` |  |
| ANIM1_PISTOL | `(8)` |  |
| ANIM1_SMG | `(9)` |  |
| ANIM1_SHOOTGUN | `(10)` |  |
| ANIM1_HEAVY_RIFLE | `(11)` |  |
| ANIM1_MINIGUN | `(12)` |  |
| ANIM1_ROCKET_LAUNCHER | `(13)` |  |
| ANIM1_FLAMER | `(14)` |  |
| ANIM1_RIFLE | `(15)` |  |
| ANIM1_SWORD | `(16)` |  |
| ANIM1_LONG_SWORD | `(17)` |  |
| ANIM1_AXE | `(18)` |  |
| ANIM1_BOW | `(19)` |  |
| ANIM2_DEAD_BEGIN | `(100)` | Anim2 Actions Manage constants |
| ANIM2_DEAD_END | `(120)` |  |
| ANIM2_IDLE_STUNNED | `(2)` | Animations |
| ANIM2_STAND | `(10)` |  |
| ANIM2_CROUCH | `(11)` |  |
| ANIM2_PRONE | `(12)` |  |
| ANIM2_SHOW_WEAPON | `(20)` |  |
| ANIM2_HIDE_WEAPON | `(21)` |  |
| ANIM2_PREPARE_WEAPON | `(22)` |  |
| ANIM2_TURNOFF_WEAPON | `(23)` |  |
| ANIM2_FIDGET | `(24)` |  |
| ANIM2_CLIMBING | `(26)` |  |
| ANIM2_PICKUP | `(27)` |  |
| ANIM2_USE | `(28)` |  |
| ANIM2_SWITCH_ITEMS | `(29)` |  |
| ANIM2_RELOAD | `(30)` |  |
| ANIM2_REPAIR | `(31)` |  |
| ANIM2_LOOT | `(35)` |  |
| ANIM2_STEAL | `(36)` |  |
| ANIM2_PUSH | `(37)` |  |
| ANIM2_BEGIN_COMBAT | `(40)` |  |
| ANIM2_IDLE_COMBAT | `(41)` |  |
| ANIM2_END_COMBAT | `(42)` |  |
| ANIM2_PUNCH_RIGHT | `(43)` |  |
| ANIM2_PUNCH_LEFT | `(44)` |  |
| ANIM2_PUNCH_COMBO | `(45)` |  |
| ANIM2_KICK_HI | `(46)` |  |
| ANIM2_KICK_LO | `(47)` |  |
| ANIM2_KICK_COMBO | `(48)` |  |
| ANIM2_THRUST_1H | `(49)` |  |
| ANIM2_THRUST_2H | `(50)` |  |
| ANIM2_SWING_1H | `(51)` |  |
| ANIM2_SWING_2H | `(52)` |  |
| ANIM2_THROW | `(53)` |  |
| ANIM2_SINGLE | `(54)` |  |
| ANIM2_BURST | `(55)` |  |
| ANIM2_SWEEP | `(56)` |  |
| ANIM2_BUTT | `(57)` |  |
| ANIM2_FLAME | `(58)` |  |
| ANIM2_NO_RECOIL | `(59)` |  |
| ANIM2_DODGE_FRONT | `(70)` |  |
| ANIM2_DODGE_BACK | `(71)` |  |
| ANIM2_DAMAGE_FRONT | `(72)` |  |
| ANIM2_DAMAGE_BACK | `(73)` |  |
| ANIM2_DAMAGE_MUL_FRONT | `(74)` |  |
| ANIM2_DAMAGE_MUL_BACK | `(75)` |  |
| ANIM2_WALK_DAMAGE_FRONT | `(76)` |  |
| ANIM2_WALK_DAMAGE_BACK | `(77)` |  |
| ANIM2_LIMP_DAMAGE_FRONT | `(78)` |  |
| ANIM2_LIMP_DAMAGE_BACK | `(79)` |  |
| ANIM2_RUN_DAMAGE_FRONT | `(80)` |  |
| ANIM2_RUN_DAMAGE_BACK | `(81)` |  |
| ANIM2_KNOCK_FRONT | `(82)` |  |
| ANIM2_KNOCK_BACK | `(83)` |  |
| ANIM2_LAYDOWN_FRONT | `(84)` |  |
| ANIM2_LAYDOWN_BACK | `(85)` |  |
| ANIM2_STANDUP_FRONT | `(88)` |  |
| ANIM2_STANDUP_BACK | `(89)` |  |
| ANIM2_DAMAGE_PRONE_FRONT | `(90)` |  |
| ANIM2_DAMAGE_PRONE_BACK | `(91)` |  |
| ANIM2_DAMAGE_MUL_PRONE_FRONT | `(92)` |  |
| ANIM2_DAMAGE_MUL_PRONE_BACK | `(93)` |  |
| ANIM2_TWITCH_PRONE_FRONT | `(94)` |  |
| ANIM2_TWITCH_PRONE_BACK | `(95)` |  |
| ANIM2_DEAD_PRONE_FRONT | `(100)` |  |
| ANIM2_DEAD_PRONE_BACK | `(101)` |  |
| ANIM2_DEAD_BLOODY_SINGLE | `(110)` |  |
| ANIM2_DEAD_BLOODY_BURST | `(111)` |  |
| ANIM2_DEAD_BURST | `(112)` |  |
| ANIM2_DEAD_PULSE | `(113)` |  |
| ANIM2_DEAD_PULSE_DUST | `(114)` |  |
| ANIM2_DEAD_LASER | `(115)` |  |
| ANIM2_DEAD_FUSED | `(116)` |  |
| ANIM2_DEAD_EXPLODE | `(117)` |  |
| ANIM2_DEAD_BURN | `(118)` |  |
| ANIM2_DEAD_BURN_RUN | `(119)` |  |
| ANIM2_SMOKE | `(120)` |  |
| KNOCKOUT_ANIM2_DEFAULT | `# (f)  ((f) ? ANIM2_KNOCK_FRONT : ANIM2_KNOCK_BACK), ((f) ? ANIM2_IDLE_PRONE_FRONT : ANIM2_IDLE_PRONE_BACK), ((f) ? ANIM2_STANDUP_FRONT : ANIM2_STANDUP_BACK)` | Knockout animations, f - face up/down |
| KNOCKOUT_ANIM2_STUNNED | `# (f)  ((f) ? ANIM2_DAMAGE_FRONT : ANIM2_DAMAGE_BACK), ANIM2_IDLE_STUNNED, ANIM2_IDLE_STUNNED` |  |
| ANIM3D_LAYER_SKIN | `(0)` | 3d models layers, maximum 30 Used in CritterCl::Anim3dLayer |
| ANIM3D_LAYER_RHANDLE | `(1)` |  |
| ANIM3D_LAYER_LHANDLE | `(2)` |  |
| ANIM3D_LAYER_BODY | `(3)` |  |
| ANIM3D_LAYER_FEET | `(4)` |  |
| ANIM3D_LAYER_HANDS | `(5)` |  |
| ANIM3D_LAYER_HEAD | `(6)` |  |
| ANIM3D_LAYER_HAIR | `(7)` |  |
| ANIM3D_LAYER_EYE | `(8)` |  |
| ANIM3D_LAYER_MUSTACHE | `(9)` |  |
| ANIM3D_LAYER_PONYTAIL | `(10)` |  |
| ANIM3D_LAYER_BEARD | `(11)` |  |
| ANIM3D_LAYER_SHOULDER | `(12)` |  |
| ANIM3D_LAYER_ARMLET | `(13)` |  |
| ANIM3D_LAYER_BACK | `(14)` |  |
| ANIM3D_LAYER_BACKPACK | `(15)` |  |
| ANIM3D_LAYERS_COUNT | `(30)` |  |
| ATTRIBUTE_Skin_Human_White01 | `(0)` | 3d models attributes ANIM3D_LAYER_SKIN      (0)  Skin |
| ATTRIBUTE_Skin_Human_White02 | `(1)` |  |
| ATTRIBUTE_Skin_Human_White03 | `(2)` |  |
| ATTRIBUTE_Skin_Human_Black01 | `(3)` |  |
| ATTRIBUTE_Skin_Human_Black02 | `(4)` |  |
| ATTRIBUTE_Skin_Human_Black03 | `(5)` |  |
| ATTRIBUTE_Skin_Human_Brown01 | `(6)` |  |
| ATTRIBUTE_Skin_Human_Brown02 | `(7)` |  |
| ATTRIBUTE_Skin_Human_Brown03 | `(8)` |  |
| ATTRIBUTE_Skin_Human_Red01 | `(9)` |  |
| ATTRIBUTE_Skin_Human_Red02 | `(10)` |  |
| ATTRIBUTE_Skin_Human_Red03 | `(11)` |  |
| ATTRIBUTE_Skin_Human_Tan01 | `(12)` |  |
| ATTRIBUTE_Skin_Human_Tan02 | `(13)` |  |
| ATTRIBUTE_Skin_Human_Tan03 | `(14)` |  |
| ATTRIBUTE_Skin_Human_Yellow01 | `(15)` |  |
| ATTRIBUTE_Skin_Human_Yellow02 | `(16)` |  |
| ATTRIBUTE_Skin_Human_Yellow03 | `(17)` |  |
| ATTRIBUTE_Skin_Centipede_Brown | `(0)` |  |
| ATTRIBUTE_Skin_Centipede_Red | `(1)` |  |
| ATTRIBUTE_Skin_Centipede_Green | `(2)` |  |
| ATTRIBUTE_Skin_Centipede_Blue | `(3)` |  |
| ATTRIBUTE_Handle_Weapon_15mmArtemisRailGun | `(1)` | ANIM3D_LAYER_RHANDLE   (1)  Right Handle ANIM3D_LAYER_LHANDLE   (2)  Left Handle |
| ATTRIBUTE_Handle_Weapon_223Autoloader | `(2)` |  |
| ATTRIBUTE_Handle_Weapon_223Autoloader_GunSilencer | `(3)` |  |
| ATTRIBUTE_Handle_Weapon_223Minigun | `(4)` |  |
| ATTRIBUTE_Handle_Weapon_22Autoloader | `(5)` |  |
| ATTRIBUTE_Handle_Weapon_22Autoloader_GunSilencer | `(6)` |  |
| ATTRIBUTE_Handle_Weapon_2mmGaussPistol | `(7)` |  |
| ATTRIBUTE_Handle_Weapon_44Revolver | `(8)` |  |
| ATTRIBUTE_Handle_Weapon_45Autoloader | `(9)` |  |
| ATTRIBUTE_Handle_Weapon_45Autoloader_GunExtClip | `(10)` |  |
| ATTRIBUTE_Handle_Weapon_45Autoloader_GunExtClip_GunSilencer | `(11)` |  |
| ATTRIBUTE_Handle_Weapon_45Autoloader_GunSilencer | `(12)` |  |
| ATTRIBUTE_Handle_Weapon_45Revolver | `(13)` |  |
| ATTRIBUTE_Handle_Weapon_50Revolver | `(14)` |  |
| ATTRIBUTE_Handle_Weapon_9mmAutoloader | `(15)` |  |
| ATTRIBUTE_Handle_Weapon_9mmAutoloader_GunExtClip | `(16)` |  |
| ATTRIBUTE_Handle_Weapon_9mmAutoloader_GunExtClip_GunSilencer | `(17)` |  |
| ATTRIBUTE_Handle_Weapon_9mmAutoloader_GunSilencer | `(18)` |  |
| ATTRIBUTE_Handle_Weapon_9mmMachinePistol | `(19)` |  |
| ATTRIBUTE_Handle_Weapon_9mmMachinePistol_GunExtClip | `(20)` |  |
| ATTRIBUTE_Handle_Weapon_9mmMachinePistol_GunExtClip_GunSilencer | `(21)` |  |
| ATTRIBUTE_Handle_Weapon_9mmMachinePistol_GunExtClip_GunSuppressor | `(22)` |  |
| ATTRIBUTE_Handle_Weapon_9mmMachinePistol_GunSilencer | `(23)` |  |
| ATTRIBUTE_Handle_Weapon_9mmMachinePistol_GunSuppressor | `(24)` |  |
| ATTRIBUTE_Handle_Weapon_APOLLOLaserPistol | `(25)` |  |
| ATTRIBUTE_Handle_Weapon_ArcWelder | `(26)` |  |
| ATTRIBUTE_Handle_Weapon_Baseballbat | `(27)` |  |
| ATTRIBUTE_Handle_Weapon_CattleProd | `(28)` |  |
| ATTRIBUTE_Handle_Weapon_CombatKnife | `(29)` |  |
| ATTRIBUTE_Handle_Weapon_Crowbar | `(30)` |  |
| ATTRIBUTE_Handle_Weapon_Dynamite | `(31)` |  |
| ATTRIBUTE_Handle_Weapon_Flamethrower | `(32)` |  |
| ATTRIBUTE_Handle_Weapon_Flamethrower_FlamerExtTank | `(33)` |  |
| ATTRIBUTE_Handle_Weapon_Flare | `(34)` |  |
| ATTRIBUTE_Handle_Weapon_GrenadeBio | `(35)` |  |
| ATTRIBUTE_Handle_Weapon_GrenadeEMP | `(36)` |  |
| ATTRIBUTE_Handle_Weapon_GrenadeFrag | `(37)` |  |
| ATTRIBUTE_Handle_Weapon_GrenadePlasma | `(38)` |  |
| ATTRIBUTE_Handle_Weapon_HandFlamer | `(39)` |  |
| ATTRIBUTE_Handle_Weapon_Hatchet | `(40)` |  |
| ATTRIBUTE_Handle_Weapon_HeavyWrench | `(41)` |  |
| ATTRIBUTE_Handle_Weapon_KitchenKnife | `(42)` |  |
| ATTRIBUTE_Handle_Weapon_LaserArraygun | `(43)` |  |
| ATTRIBUTE_Handle_Weapon_LaserPistol | `(44)` |  |
| ATTRIBUTE_Handle_Weapon_LaserSaw | `(45)` |  |
| ATTRIBUTE_Handle_Weapon_LeadPipe | `(46)` |  |
| ATTRIBUTE_Handle_Weapon_Machete | `(47)` |  |
| ATTRIBUTE_Handle_Weapon_NightStick | `(48)` |  |
| ATTRIBUTE_Handle_Weapon_Rock | `(49)` |  |
| ATTRIBUTE_Handle_Weapon_SawedOffShotgun | `(50)` |  |
| ATTRIBUTE_Handle_Weapon_Shiv | `(51)` |  |
| ATTRIBUTE_Handle_Weapon_Switchblade | `(52)` |  |
| ATTRIBUTE_Handle_Weapon_TableLeg | `(53)` |  |
| ATTRIBUTE_Handle_Weapon_ThrowingKnife | `(54)` |  |
| ATTRIBUTE_Handle_Weapon_Spear | `(55)` |  |
| ATTRIBUTE_Handle_Weapon_Sledgehammer | `(56)` |  |
| ATTRIBUTE_Handle_Item_FirstAidKit | `(100)` |  |
| ATTRIBUTE_Handle_Item_SecurityKit | `(101)` |  |
| ATTRIBUTE_Handle_Item_Toolkit | `(102)` |  |
| ATTRIBUTE_Body_LeatherOutfit | `(1)` | ANIM3D_LAYER_BODY      (3)  Body |
| ATTRIBUTE_Body_PowerArmor | `(2)` |  |
| ATTRIBUTE_Body_PrisonSuit | `(3)` |  |
| ATTRIBUTE_Body_VaultSuit | `(4)` |  |
| ATTRIBUTE_Body_CombatArmor | `(5)` |  |
| ATTRIBUTE_Feet_LeatherOutfit | `(1)` | ANIM3D_LAYER_FEET      (4)  Feet |
| ATTRIBUTE_Feet_PowerArmor | `(2)` |  |
| ATTRIBUTE_Feet_PrisonSuit | `(3)` |  |
| ATTRIBUTE_Feet_VaultSuit | `(4)` |  |
| ATTRIBUTE_Feet_CombatArmor | `(5)` |  |
| ATTRIBUTE_Hands_LeatherOutfit | `(1)` | ANIM3D_LAYER_HANDS     (5)  Hands |
| ATTRIBUTE_Hands_PowerArmor | `(2)` |  |
| ATTRIBUTE_Hands_LeatherOutfitGauntlet | `(3)` |  |
| ATTRIBUTE_Hands_CombatArmor | `(5)` |  |
| ATTRIBUTE_Hands_PowerFist | `(10)` |  |
| ATTRIBUTE_Head_ArmingCap | `(1)` | ANIM3D_LAYER_HEAD      (6)  Head |
| ATTRIBUTE_Head_PowerArmor | `(2)` |  |
| ATTRIBUTE_Head_StrawHat | `(3)` |  |
| ATTRIBUTE_Head_CombatArmor | `(5)` |  |
| ATTRIBUTE_Head_Motorcycle_White | `(10)` |  |
| ATTRIBUTE_Head_Motorcycle_Black | `(11)` |  |
| ATTRIBUTE_Head_Motorcycle_Red | `(12)` |  |
| ATTRIBUTE_Head_Motorcycle_Green | `(13)` |  |
| ATTRIBUTE_Head_Motorcycle_Blue | `(14)` |  |
| ATTRIBUTE_Head_Motorcycle_Grey | `(15)` |  |
| ATTRIBUTE_Head_Motorcycle_Yellow | `(16)` |  |
| ATTRIBUTE_Head_Motorcycle_8Ball | `(17)` |  |
| ATTRIBUTE_Head_Motorcycle_EasyRider | `(18)` |  |
| ATTRIBUTE_Head_Motorcycle_EyeRed | `(19)` |  |
| ATTRIBUTE_Head_Motorcycle_Flames | `(20)` |  |
| ATTRIBUTE_Head_Motorcycle_Police | `(21)` |  |
| ATTRIBUTE_Head_Motorcycle_ShotSmiley | `(22)` |  |
| ATTRIBUTE_Head_Motorcycle_SkullFull | `(23)` |  |
| ATTRIBUTE_Head_Motorcycle_Skull | `(24)` |  |
| ATTRIBUTE_Hair_Male_Afro | `(10)` | ANIM3D_LAYER_HAIR      (7)  Hair |
| ATTRIBUTE_Hair_Male_Bald | `(20)` |  |
| ATTRIBUTE_Hair_Male_Bowl | `(30)` |  |
| ATTRIBUTE_Hair_Male_Crown | `(40)` |  |
| ATTRIBUTE_Hair_Male_Greaser | `(50)` |  |
| ATTRIBUTE_Hair_Male_Long | `(60)` |  |
| ATTRIBUTE_Hair_Male_Military | `(70)` |  |
| ATTRIBUTE_Hair_Male_Mohawk | `(80)` |  |
| ATTRIBUTE_Hair_Male_Ponytail | `(90)` |  |
| ATTRIBUTE_Hair_Male_Shaggy | `(100)` |  |
| ATTRIBUTE_Hair_Male_Short | `(110)` |  |
| ATTRIBUTE_Hair_Male_Shoulder | `(120)` |  |
| ATTRIBUTE_Hair_Female_Afro | `(210)` |  |
| ATTRIBUTE_Hair_Female_Bald | `(220)` |  |
| ATTRIBUTE_Hair_Female_Beehive | `(230)` |  |
| ATTRIBUTE_Hair_Female_BettyPage | `(240)` |  |
| ATTRIBUTE_Hair_Female_Bob | `(250)` |  |
| ATTRIBUTE_Hair_Female_Bun | `(260)` |  |
| ATTRIBUTE_Hair_Female_Chin | `(270)` |  |
| ATTRIBUTE_Hair_Female_Flip | `(280)` |  |
| ATTRIBUTE_Hair_Female_Frizzy | `(290)` |  |
| ATTRIBUTE_Hair_Female_Long | `(300)` |  |
| ATTRIBUTE_Hair_Female_Mohawk | `(310)` |  |
| ATTRIBUTE_Hair_Female_Ponytail | `(320)` |  |
| ATTRIBUTE_Hair_Female_Pulled | `(330)` |  |
| ATTRIBUTE_Hair_Female_Short | `(340)` |  |
| ATTRIBUTE_Eye_PatchLeft | `(1)` | ANIM3D_LAYER_EYE       (8)  Eye |
| ATTRIBUTE_Eye_PatchRight | `(2)` |  |
| ATTRIBUTE_Eye_Authorities | `(3)` |  |
| ATTRIBUTE_Eye_Spectacles | `(4)` |  |
| ATTRIBUTE_Mustache_Male_Full | `(10)` | ANIM3D_LAYER_MUSTACHE  (9)  Mustache |
| ATTRIBUTE_Mustache_Male_FuManchu | `(20)` |  |
| ATTRIBUTE_Mustache_Male_Goatee | `(30)` |  |
| ATTRIBUTE_Mustache_Male_Guvner | `(40)` |  |
| ATTRIBUTE_Mustache_Male_Handlebar | `(50)` |  |
| ATTRIBUTE_Mustache_Male_Hermit | `(60)` |  |
| ATTRIBUTE_Mustache_Male_MuttonChops | `(70)` |  |
| ATTRIBUTE_Mustache_Male_Small | `(80)` |  |
| ATTRIBUTE_Mustache_Male_Stubble | `(90)` |  |
| ATTRIBUTE_Mustache_MadMax | `(200)` |  |
| ATTRIBUTE_Ponytail_Ponytail1 | `(10)` | ANIM3D_LAYER_PONYTAIL  (10)  Ponytail |
| ATTRIBUTE_Ponytail_Ponytail2 | `(20)` |  |
| ATTRIBUTE_Beard_Male_Amish | `(10)` | ANIM3D_LAYER_BEARD     (11)  Beard |
| ATTRIBUTE_Beard_Male_Full | `(20)` |  |
| ATTRIBUTE_Beard_Male_FuManchu | `(30)` |  |
| ATTRIBUTE_Beard_Male_Goatee | `(40)` |  |
| ATTRIBUTE_Beard_Male_Guvner | `(50)` |  |
| ATTRIBUTE_Beard_Male_Hermit | `(60)` |  |
| ATTRIBUTE_Beard_Male_Stubble | `(70)` |  |
| ATTRIBUTE_Shoulderpieces_LeatherOutfit | `(1)` | ANIM3D_LAYER_SHOULDER  (12)  Shoulderpieces |
| ATTRIBUTE_Shoulderpieces_PowerArmor | `(2)` |  |
| ATTRIBUTE_Shoulderpieces_CombatArmor | `(5)` |  |
| ATTRIBUTE_Armlet_PipBoyClosed | `(1)` | ANIM3D_LAYER_ARMLET    (13)  Armlet |
| ATTRIBUTE_Armlet_PipBoyOpen | `(2)` |  |
| ATTRIBUTE_Back_LeatherOutfit_Skull | `(1)` | ANIM3D_LAYER_BACK      (14)  Back |
| ATTRIBUTE_Back_LeatherOutfit_Biohazard | `(2)` |  |
| ATTRIBUTE_Back_LeatherOutfit_Dragon | `(3)` |  |
| ATTRIBUTE_Back_LeatherOutfit_Eagle | `(4)` |  |
| ATTRIBUTE_Back_PrisonSuit | `(100)` |  |
| ATTRIBUTE_Back_VaultSuit | `(200)` |  |
| ATTRIBUTE_Backpack_PaLg01 | `(1)` | ANIM3D_LAYER_BACKPACK  (15)  Backpack |
| ATTRIBUTE_Backpack_PaSm01 | `(2)` |  |
| ATTRIBUTE_COLOR_Brown | `(0)` | Textures for Hair, Mustache, Ponytail, Beard |
| ATTRIBUTE_COLOR_BrownGrey | `(1)` |  |
| ATTRIBUTE_COLOR_Black | `(2)` |  |
| ATTRIBUTE_COLOR_BlackGrey | `(3)` |  |
| ATTRIBUTE_COLOR_White | `(4)` |  |
| ATTRIBUTE_COLOR_WhiteGrey | `(5)` |  |
| ATTRIBUTE_COLOR_Blonde | `(6)` |  |
| ATTRIBUTE_COLOR_BlondeGrey | `(7)` |  |
| ATTRIBUTE_COLOR_Red | `(8)` |  |
| ATTRIBUTE_COLOR_RedGrey | `(9)` |  |
| SUBSET_Human_Chest | `(0)` | Humans 3d models body subsets |
| SUBSET_Human_Feet | `(1)` |  |
| SUBSET_Human_ForeArms | `(2)` |  |
| SUBSET_Human_Hands | `(3)` |  |
| SUBSET_Human_Head | `(4)` |  |
| SUBSET_Human_Legs | `(5)` |  |
| SUBSET_Human_Shins | `(6)` |  |
| SUBSET_Human_UpperArms | `(7)` |  |
| SUBSET_Human_Waist | `(8)` |  |

