---
title: prod_veins.fos
description: " FOnline: 2238 Rotators  prod_veins.fos ..."
---

# prod_veins.fos


FOnline: 2238
Rotators

prod_veins.fos


## Includes

- `_macros.fos`
- `mine_h.fos`
- `mapdata_h.fos`
- `utils_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| VEIN_BATCH_IRON | `(2)` |  |
| VEIN_BATCH_IRON2 | `(1)` |  |
| VEIN_BATCH_MINERALS | `(2)` |  |
| VEIN_BATCH_MINERALS2 | `(1)` |  |
| VEIN_BATCH_URANIUM | `(1)` |  |
| VEIN_BATCH_GOLD | `(1)` |  |
| VEIN_CAPACITY_IRON | `(8)` |  |
| VEIN_CAPACITY_IRON2 | `(8)` |  |
| VEIN_CAPACITY_MINERALS | `(8)` |  |
| VEIN_CAPACITY_MINERALS2 | `(8)` |  |
| VEIN_CAPACITY_URANIUM | `(8)` |  |
| VEIN_CAPACITY_GOLD | `(4)` |  |
| VEIN_CAPACITY | `# (vein)                   vein.Val0` |  |

## Functions

### Dig

```angelscript
bool Dig(Critter@ miner, Item@ tool, Item@ vein, uint16 productPid, uint amount, uint msgIndex)
```

### _InitVeinIron

```angelscript
void _InitVeinIron(Item& item, bool firstTime)
```

### _InitVeinIron2

```angelscript
void _InitVeinIron2(Item& item, bool firstTime)
```

### _InitVeinMinerals

```angelscript
void _InitVeinMinerals(Item& item, bool firstTime)
```

### _InitVeinMinerals2

```angelscript
void _InitVeinMinerals2(Item& item, bool firstTime)
```

### _InitVeinUranium

```angelscript
void _InitVeinUranium(Item& item, bool firstTime)
```

### _InitVeinGold

```angelscript
void _InitVeinGold(Item& item, bool firstTime)
```

### _UseVeinIron

```angelscript
bool _UseVeinIron(Item& item, Critter& cr, Item@ usedItem)
```

### _UseVeinIron2

```angelscript
bool _UseVeinIron2(Item& item, Critter& cr, Item@ usedItem)
```

### _UseVeinMinerals

```angelscript
bool _UseVeinMinerals(Item& item, Critter& cr, Item@ usedItem)
```

### _UseVeinMinerals2

```angelscript
bool _UseVeinMinerals2(Item& item, Critter& cr, Item@ usedItem)
```

### _UseVeinUranium

```angelscript
bool _UseVeinUranium(Item& item, Critter& cr, Item@ usedItem)
```

### _UseVeinGold

```angelscript
bool _UseVeinGold(Item& item, Critter& cr, Item@ usedItem)
```

### _SkillVeinIron

```angelscript
bool _SkillVeinIron(Item& item, Critter& cr, int skill)
```

### _SkillVeinIron2

```angelscript
bool _SkillVeinIron2(Item& item, Critter& cr, int skill)
```

### _SkillVeinMinerals

```angelscript
bool _SkillVeinMinerals(Item& item, Critter& cr, int skill)
```

### _SkillVeinMinerals2

```angelscript
bool _SkillVeinMinerals2(Item& item, Critter& cr, int skill)
```

### _SkillVeinUranium

```angelscript
bool _SkillVeinUranium(Item& item, Critter& cr, int skill)
```

### _SkillVeinGold

```angelscript
bool _SkillVeinGold(Item& item, Critter& cr, int skill)
```


