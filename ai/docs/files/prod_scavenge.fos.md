---
title: prod_scavenge.fos
description: " !!! IMPORTANT !!! change PROD_REGEN_TIME value after tests ..."
---

# prod_scavenge.fos


!!! IMPORTANT !!!
change PROD_REGEN_TIME value after tests


## Includes

- `_macros.fos`
- `mapdata_h.fos`
- `utils_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| MSG_SCAVENGING_SUCCESS | `(3200)` |  |
| MSG_SCAVENGING_FAIL | `(3201)` |  |
| MSG_SCAVENGING_NOTHING | `(3202)` |  |
| MSG_SCAVENGING_TOOL | `(3203)` |  |
| MSG_SCAVENGING_USE | `(3204)` |  |
| PROD_REGEN_TIME | `(REAL_MINUTE(Random(1, 15)))` |  |
| SCAVENGING_CAP | `(100)` |  |
| PROD_REGEN_TIME_NC | `(REAL_MINUTE(Random(1, 3)))` |  |
| SCAVENGING_CAP_NC | `(20)` |  |
| OBJECT_USE_TIMES | `(2)` |  |
| _ChanceToScavenge | `# (skill, max) ( ((max/5)*2) + ( ((max/5)*3) * skill )/SCAVENGING_CAP )` | chance with max Scavenging skill = max, chance with 0 Scavenging skill = 2/5 max |

## Functions

### AddScavengedItem

```angelscript
void AddScavengedItem(Critter& player, uint pid, uint cnt)
```

### Scavenge

```angelscript
bool Scavenge(Critter@ scavenger, Item@ tool, Item@ junk, uint type)
```

### e_Regen

```angelscript
uint e_Regen(array<uint>@ values)
```

### _InitWoodenJunk

```angelscript
void _InitWoodenJunk(Item& item, bool firstTime)
```

### _InitMetalJunk

```angelscript
void _InitMetalJunk(Item& item, bool firstTime)
```

### _InitPaperMachine

```angelscript
void _InitPaperMachine(Item& item, bool firstTime)
```

### _InitJunkBarrel

```angelscript
void _InitJunkBarrel(Item& item, bool firstTime)
```

### _UseWoodenJunk

```angelscript
bool _UseWoodenJunk(Item& item, Critter& cr, Item@ usedItem)
```

### _UseMetalJunk

```angelscript
bool _UseMetalJunk(Item& item, Critter& cr, Item@ usedItem)
```

### _UsePaperMachine

```angelscript
bool _UsePaperMachine(Item& item, Critter& cr, Item@ usedItem)
```

### _UseJunkBarrel

```angelscript
bool _UseJunkBarrel(Item& item, Critter& cr, Item@ usedItem)
```

### _SkillWoodenJunk

```angelscript
bool _SkillWoodenJunk(Item& item, Critter& cr, int skill)
```

### _SkillMetalJunk

```angelscript
bool _SkillMetalJunk(Item& item, Critter& cr, int skill)
```

### _SkillPaperMachine

```angelscript
bool _SkillPaperMachine(Item& item, Critter& cr, int skill)
```

### _SkillJunkBarrel

```angelscript
bool _SkillJunkBarrel(Item& item, Critter& cr, int skill)
```


