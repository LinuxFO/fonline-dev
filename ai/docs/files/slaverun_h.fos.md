---
title: slaverun_h.fos
description: " FOnline: 2238 Rotators  slaverun_h.fos ..."
---

# slaverun_h.fos


FOnline: 2238
Rotators

slaverun_h.fos


## Includes

- `mapdata_h.fos`
- `_entires.fos`

## Included By

- [map_slaverun.fos](map_slaverun.fos.md)
- [slaverun.fos](slaverun.fos.md)
- [slaverun_dialog.fos](slaverun_dialog.fos.md)
- [slaverun_slave_hostile.fos](slaverun_slave_hostile.fos.md)
- [slaverun_slave_normal.fos](slaverun_slave_normal.fos.md)
- [slaverun_slaver.fos](slaverun_slaver.fos.md)

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __SLAVERUN_H__ |  |  |
| UNITIALIZED | `(0)` | map states |
| INITIALIZED | `(1)` |  |
| SLAVERUN_UNKNOWN | `(0x0)` | current quest state, (*) - set only in location |
| SLAVERUN_KNOWN | `(0x1)` |  |
| SLAVERUN_ACTIVE | `(0x2)` |  |
| SLAVERUN_SLAVERS_KILLED | `(0x4)` |  |
| SLAVERUN_SLAVES_KILLED | `(0x8)` |  |
| SLAVERUN_BOTCHED | `(0x10)` |  |
| SLAVERUN_TOO_LATE | `(0x20)` |  |
| SLAVERUN_ATTEMPTED | `(0x40)` |  |
| SLAVERUN_COMPLETED | `(0x80)` |  |
| SLAVERUN_PID_SLAVER | `(217)` |  |
| RUN_TIME | `(GAME_MINUTE(2880))` |  |
| SLAVERUN_TIMEOUT | `(REAL_MINUTE(1))` |  |

