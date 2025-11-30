---
title: workbench.fos
description: " FOnline: 2238 Rotators  workbench.fos ..."
---

# workbench.fos


FOnline: 2238
Rotators

workbench.fos


## Includes

- `_defines.fos`
- `_macros.fos`
- `_scripts.fos`
- `_vars.fos`
- `factions_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| TERMINAL_DIALOG | `(1200)` |  |
| TERMINAL_SAD_DIALOG | `(800)` |  |
| MSG_SAD_POWER_NOT_REPAIRED | `(0)` |  |
| MSG_SAD_POWER_REPAIRED | `(1)` |  |
| MSG_SAD_POWER_OK | `(2)` |  |
| MSG_SAD_POWER_NOT_OK | `(3)` |  |

## Functions

### item_init

```angelscript
void item_init(Item& item, bool firstTime)
```

### _Campfire

```angelscript
void _Campfire(Item& item, bool firstTime)
```

### _Primitive

```angelscript
void _Primitive(Item& item, bool firstTime)
```

### _Advanced

```angelscript
void _Advanced(Item& item, bool firstTime)
```

### _Tobacco

```angelscript
void _Tobacco(Item& item, bool firstTime)
```

### _Raiders

```angelscript
void _Raiders(Item& item, bool firstTime)
```

### _SierraAmmo

```angelscript
void _SierraAmmo(Item& item, bool firstTime)
```

### _SierraMed

```angelscript
void _SierraMed(Item& item, bool firstTime)
```

### _VCMed

```angelscript
void _VCMed(Item& item, bool firstTime)
```

### _Drop

removes item if dropped

```angelscript
void _Drop(Item& item, Critter& cr)
```

### _Move

```angelscript
void _Move(Item& item, Critter& cr, uint8 fromSlot)
```

### _UseSkillPrimitive

```angelscript
bool _UseSkillPrimitive(Item& item, Critter& player, int skill)
```

### _UseSkillSierraAmmo

Using Ammo Facility in Sierra Army Depot

```angelscript
bool _UseSkillSierraAmmo(Item& item, Critter& player, int skill)
```

### _UseSkillSierraMed

Using Med Facility in Sierra Army Depot

```angelscript
bool _UseSkillSierraMed(Item& item, Critter& player, int skill)
```

### _UseSkillVCMed

Using Med Facility in Vault City

```angelscript
bool _UseSkillVCMed(Item& item, Critter& player, int skill)
```

### _UseSkill

Using workbench

```angelscript
bool _UseSkill(Item& item, Critter& player, int skill)
```

### _UseSkillAdvanced

Using advanced bench

```angelscript
bool _UseSkillAdvanced(Item& item, Critter& player, int skill)
```

### _UseSkillTobacco

Using tobacco bench

```angelscript
bool _UseSkillTobacco(Item& item, Critter& player, int skill)
```

### _UseSkillRaiders

Using Raiders Workbench

```angelscript
bool _UseSkillRaiders(Item& item, Critter& player, int skill)
```

### GiveWorkbench

gives invisible workbench to players inv, so that it serves as 'tool'

```angelscript
void GiveWorkbench(Critter& player, uint pid)
```

### RemoveWorkbench

removes workbench from player inventory

```angelscript
void RemoveWorkbench(Critter& player, uint pid)
```

### RemoveWorkbenches

remove all workbenches from inventory

```angelscript
void RemoveWorkbenches(Critter& player)
```

### RemoveWorkbenches

remove all workbenches on map

```angelscript
void RemoveWorkbenches(Map& map)
```

### RemoveWorkbenches

remove all workbenches in location

```angelscript
void RemoveWorkbenches(Location& loc)
```

### t_Workbench

```angelscript
void t_Workbench(Critter& player, Scenery& trigger, bool entered, uint8 dir)
```

### t_WorkbenchRaiders

```angelscript
void t_WorkbenchRaiders(Critter& player, Scenery& trigger, bool entered, uint8 dir)
```

### s_Terminal

Mariposa Terminal

```angelscript
bool s_Terminal(Critter& player, Scenery& terminal, int skill, Item@ item)
```

### s_Terminal_SAD

Sierra Terminal/Mainframe

```angelscript
bool s_Terminal_SAD(Critter& player, Scenery& terminal, int skill, Item@ item)
```

### s_Mfc_Machine

Mariposa Machine for Micro Fusion Cells production

```angelscript
bool s_Mfc_Machine(Critter& player, Scenery& terminal, int skill, Item@ item)
```

### s_Power_SAD

Sierra Backup Power Supply

```angelscript
bool s_Power_SAD(Critter& player, Scenery& terminal, int skill, Item@ item)
```

### place_campfire

```angelscript
void place_campfire(Critter& cr, int, int, int)
```


