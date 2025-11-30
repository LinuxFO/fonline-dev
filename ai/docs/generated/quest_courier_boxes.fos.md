---
title: quest_courier_boxes.fos
description: " FOnline: 2238 Rotators  quest_courier_boxes.fos ..."
---

# quest_courier_boxes.fos


FOnline: 2238
Rotators

quest_courier_boxes.fos


## Includes

- `_macros.fos`
- `reputations_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| BOX_QUEST_GUNRUNNERS_COURIER | `(0)` |  |
| BOX_QUEST_GUNRUNNERS_CARAVAN | `(1)` |  |
| _BoxReputation | `# (it)   (it.Val3)` |  |
| _BoxStatus | `# (it)   (it.Val4)` |  |
| _BoxCritterId | `# (it)   (it.Val5)` |  |
| BOX_STATUS_UNTOUCHED | `(0)` |  |
| BOX_STATUS_DISARMED | `(1)` |  |
| BOX_STATUS_OPENED | `(2)` |  |
| BOX_STATUS_JAMMED | `(3)` |  |

## Functions

### r_GiveGunRunnerCourierBox

```angelscript
void r_GiveGunRunnerCourierBox(Critter& cr, Critter@ npc)
```

### _GunRunnersBoxInit

```angelscript
void _GunRunnersBoxInit(Item& item, bool firstTime)
```

### _GunRunnersBoxUsed

```angelscript
bool _GunRunnersBoxUsed(Item& item, Critter& player, Critter@ onCritter, Item@ onItem, Scenery@ onScenery)
```

### ExplodeBomb

```angelscript
void ExplodeBomb(Critter& player, Item& item)
```

### DetonateBomb

```angelscript
bool DetonateBomb(Critter& player)
```

### _GunRunnersBoxUseSkill

```angelscript
bool _GunRunnersBoxUseSkill(Item& item, Critter& player, int skill)
```


