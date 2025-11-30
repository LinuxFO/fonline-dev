---
title: quest_caravan_box.fos
description: " FOnline: 2238 Rotators  quest_caravan_box.fos ..."
---

# quest_caravan_box.fos


FOnline: 2238
Rotators

quest_caravan_box.fos


## Includes

- `_macros.fos`
- `utils_h.fos`
- `_entires.fos`
- `npc_roles_h.fos`
- `entire.fos`
- `reputations_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| BOX_STATUS_NONE | `(0)` |  |
| BOX_STATUS_ONGOING | `(1)` |  |

## Functions

### GetCaravanOfficer

```angelscript
Critter@ GetCaravanOfficer(Map@ map)
```

### d_IsOngoing

```angelscript
bool d_IsOngoing(Critter& player, Critter@ npc)
```

### d_NotStarted

```angelscript
bool d_NotStarted(Critter& player, Critter@ npc)
```

### d_IsDone

```angelscript
bool d_IsDone(Critter& player, Critter@ npc)
```

### r_StartQuest

```angelscript
void r_StartQuest(Critter& player, Critter@ npc)
```

### r_CompleteQuest

```angelscript
void r_CompleteQuest(Critter& player, Critter@ npc)
```

### _OnDropBox

```angelscript
void _OnDropBox(Item& item, Critter& cr)
```

### _BoxInit

```angelscript
void _BoxInit(Item& box, bool firstTime)
```

### _OnUseCaravan

```angelscript
bool _OnUseCaravan(Critter& cr, Scenery& scen, int skill, Item@ item)
```


