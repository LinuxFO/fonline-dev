---
title: reinforcements_h.fos
description: " FOnline: 2238 Rotators  reinforcements_h.fos ..."
---

# reinforcements_h.fos


FOnline: 2238
Rotators

reinforcements_h.fos


## Included By

- [main.fos](main.fos.md)
- [map_boneyard.fos](map_boneyard.fos.md)
- [map_hub.fos](map_hub.fos.md)
- [map_ncr_downtown.fos](map_ncr_downtown.fos.md)
- [reinforcements.fos](reinforcements.fos.md)

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __REINFORCEMENTS_H__ |  |  |
| ALERT_LEVEL_NONE | `(0)` | thresholds for reinforcement calling if current alert level >= threshold, start calling respective reinforcement type, and every lower type |
| ALERT_LEVEL_REGISTER | `(8)` |  |
| ALERT_LEVEL_LIGHT | `(24)` |  |
| ALERT_LEVEL_HEAVY | `(60)` |  |
| ALERT_LEVEL_REACT | `(50)` | threshold for making all guards reacting to an offense |
| ALERT_COUNT_GUARD | `(2)` | points of alert level increase per death of guard or allied npc |
| ALERT_COUNT_NPC | `(1)` |  |
| ALERT_CYCLE | `(GAME_MINUTE(30))` | main cycle length |
| ALERT_COUNT_DROP | `(4)` | minimum points of alert level dropped every cycle |
| ALERT_COUNT_P_DROP | `(20)` | minimum % of alert level points dropped every cycle |
| REINFORCEMENTS_COUNT_LOW | `(4)` | number of npcs in onr reinforcement batch (lower and upper bound) |
| REINFORCEMENTS_COUNT_HIGH | `(8)` |  |
| REINFORCEMENT_COUNT | `(2)` |  |

