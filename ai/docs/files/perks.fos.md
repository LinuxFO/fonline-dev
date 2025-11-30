---
title: perks.fos
description: " FOnline: 2238 Rotators  perks.fos ..."
---

# perks.fos


FOnline: 2238
Rotators

perks.fos


## Includes

- `_macros.fos`
- `perks_data.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| SATISFIES | `# (__perk, __func, __p0, __p1, __p2)Perks[__perk].CustomSatisfies(__func, __p0, __p1, __p2)` | still some customizing, todo: make it generic |

## Classes

### Requirement

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| Param | `uint16` |  |  |
| Atleast | `bool` |  |  |
| Value | `int` |  |  |

**Methods**

#### Satisfies
```angelscript
bool Satisfies(Critter@ cr)
```

### Effect

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| Param | `uint16` |  |  |
| Increase | `bool` |  |  |
| Value | `int` |  |  |

**Methods**

#### Process
```angelscript
void Process(Critter@ cr)
```

### LevelData

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| Requirements | `array<[Requirement](perks.fos.md)>` |  |  |
| UpEffects | `array<[Effect](perks.fos.md)>` |  |  |
| DownEffects | `array<[Effect](perks.fos.md)>` |  |  |

**Methods**

#### Satisfies
```angelscript
bool Satisfies(Critter@ cr)
```

#### ProcessUp
```angelscript
void ProcessUp(Critter@ cr)
```

#### ProcessDown
```angelscript
void ProcessDown(Critter@ cr)
```

### PerkData

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| Id | `int` |  |  |
| Range | `int` |  |  |
| Type | `int` |  |  |
| SatisfiesF | `SatisfiesFunc@` |  |  |
| ProcessUpF | `ProcessFunc@` |  |  |
| ProcessDownF | `ProcessFunc@` |  |  |
| p0 | `int` |  |  |
| p1 | `int` |  |  |
| p2 | `int` |  |  |
| Levels | `array<[LevelData](perks.fos.md)>` |  |  |

**Methods**

#### Check
```angelscript
bool Check(Critter@ cr, int level)
```

#### ProcessUp
```angelscript
void ProcessUp(Critter@ cr, int fromlevel)
```

#### ProcessDown
```angelscript
void ProcessDown(Critter@ cr, int tolevel)
```

#### CustomSatisfies
```angelscript
void CustomSatisfies(SatisfiesFunc@ func, int _p0, int _p1, int _p2)
```


## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| Perks | `array<[PerkData](perks.fos.md)>` |  |  |

## Functions

### d_PerkCheck

```angelscript
bool d_PerkCheck(Critter& player, Critter@ npc, int perk)
```

### d_PerkCheckFalse

```angelscript
bool d_PerkCheckFalse(Critter& player, Critter@ npc, int perk)
```

### d_ProfessionPerkCheck

```angelscript
bool d_ProfessionPerkCheck(Critter& player, Critter@ npc, int perk, int level)
```

### d_ProfessionCheck

```angelscript
bool d_ProfessionCheck(Critter& player, Critter@ npc, int perk)
```

### InitPerks

```angelscript
void InitPerks()
```

### PerkCheck

```angelscript
bool PerkCheck(Critter& cr, uint perk, bool always)
```

### SupportPerkCheck

```angelscript
bool SupportPerkCheck(Critter& cr, uint perk)
```

### PerkUp

```angelscript
void PerkUp(Critter& cr, uint perk, int fromlevel)
```

### PerkDown

```angelscript
void PerkDown(Critter& cr, uint perk, int tolevel)
```

### _OrSkill

todo: make a generic condition in the editor

```angelscript
bool _OrSkill(Critter& cr, int perk, int level, int skill1, int skill2, int minskill)
```

### _OrCombatSkill

```angelscript
bool _OrCombatSkill(Critter& cr, int perk, int level, int, int, int minskill)
```

### _OrRangedSkill

```angelscript
bool _OrRangedSkill(Critter& cr, int perk, int level, int, int, int minskill)
```

### _OrRangedGunSkill

```angelscript
bool _OrRangedGunSkill(Critter& cr, int perk, int level, int, int, int minskill)
```

### _BRD

```angelscript
bool _BRD(Critter& cr, int perk, int level, int, int, int)
```

### _Awareness

```angelscript
bool _Awareness(Critter& cr, int perk, int level, int, int, int)
```

### _OneSkill

```angelscript
bool _OneSkill(Critter& cr, int perk, int level, int skill, int, int minskill)
```

### _ProfessionCheck

```angelscript
bool _ProfessionCheck(Critter& cr, int perk, int level, int skill, int level1, int level2)
```

### _SpeakerUp

```angelscript
void _SpeakerUp(Critter& cr, int perk, int level, int p0, int p1, int p2)
```

### _SpeakerDown

```angelscript
void _SpeakerDown(Critter& cr, int perk, int level, int p0, int p1, int p2)
```

### _ExplorerUp

```angelscript
void _ExplorerUp(Critter& cr, int perk, int level, int p0, int p1, int p2)
```

### AssertProfessions

```angelscript
bool AssertProfessions(Critter& player)
```


