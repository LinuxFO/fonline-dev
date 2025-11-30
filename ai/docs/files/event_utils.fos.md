---
title: event_utils.fos
description: " FOnline: 2238 Rotators  event_utils.fos ..."
---

# event_utils.fos


FOnline: 2238
Rotators

event_utils.fos


## Includes

- `_macros.fos`
- `follower_common_h.fos`
- `groups_h.fos`
- `lexems_h.fos`
- `pids_groups.fos`
- `utils_h.fos`
- `weap_anim_table_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| _AddItem | `# (group, max, chance) { if((value > 0) && Random(0, chance) == 0) { uint item = random_from_array(group); uint ival = Random(0, max); containers[j].AddItem(item, ival, 0); value -= BaseItemValue(item, true) * ival; DLog("deducting: " + (BaseItemValue(item, true) * ival) + " for " + item); } }` |  |
| WT_NO_ITEMS | `(0x01)` |  |
| WT_DELETE_ITEMS | `(0x02)` |  |
| WT_NO_FOLLOWERS | `(0x04)` |  |

## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| num | `uint` | `map.GetItems(x, y, items)` |  |

## Functions

### spawncontitems

```angelscript
void spawncontitems(Critter& cr, int techlvl, int startvalue, int p2)
```

### removeitems

```angelscript
void removeitems(Critter& cr, int p0, int p1, int p2)
```

### dlg_TeleportToVarMap

```angelscript
void dlg_TeleportToVarMap(Critter& player, Critter@ npc, string@ text)
```

### r_TeleportToVarMap

```angelscript
uint r_TeleportToVarMap(Critter& player, Critter@npc)
```

### r_TeleportToVarMapCoordinates

```angelscript
uint r_TeleportToVarMapCoordinates(Critter& player, Critter@npc)
```

### d_IsAuth

```angelscript
bool d_IsAuth(Critter& player, Critter@ npc)
```

### d_IsTester

```angelscript
bool d_IsTester(Critter& player, Critter@ npc)
```

### d_IsModer

```angelscript
bool d_IsModer(Critter& player, Critter@ npc)
```

### d_IsAdmin

```angelscript
bool d_IsAdmin(Critter& player, Critter@ npc)
```


