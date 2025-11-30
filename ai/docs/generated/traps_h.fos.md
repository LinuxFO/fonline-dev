---
title: traps_h.fos
description: " FOnline: 2238 Rotators  traps_h.fos ..."
---

# traps_h.fos


FOnline: 2238
Rotators

traps_h.fos


## Included By

- [cheats.fos](cheats.fos.md)
- [encounter_containers.fos](encounter_containers.fos.md)
- [eventboss.fos](eventboss.fos.md)
- [explode.fos](explode.fos.md)
- [main_planes.fos](main_planes.fos.md)
- [special_map_objects.fos](special_map_objects.fos.md)
- [traps.fos](traps.fos.md)

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __TRAPS_H__ |  |  |
| TRAPS_HIDE | `# (traps)          ((traps) / 5 + 10)` |  |
| TRAP_CLEAR_EXPERIENCE | `# (_it)            (50 + _Complexity(_it) / 6)` |  |
| _Complexity | `# (it)       (it.Val3)` | shared |
| _BonusDamage | `# (it)      (it.Val4)` |  |
| _ExplodeSetNumEvent | `# (explode, eventNum)explode.Val1 = int(eventNum)` | all explosives (explode.fos only) |
| _ExplodeGetNumEvent | `# (explode) uint(explode.Val1)` |  |
| _ExplodeSetSwitch | `# (explode, explSwitch)explSwitch.Val1 = int(explode.Id)` |  |
| _ExplodeGetExplode | `# (explSwitch) GetItem(uint(explSwitch.Val1))` |  |
| _ExplodeSetOwner | `# (explode, ownerId)explode.Val2 = int(ownerId)` |  |
| _ExplodeGetOwner | `# (explode) uint(explode.Val2)` |  |
| _ExplodeSetBonusDamage | `# (explode, value)explode.Val4 = (value)` |  |
| _ExplodeGetBonusDamage | `# (explode) (explode.Val4)` |  |
| _ExplodeSetBonusRadius | `# (explode, value)explode.Val5 = (value)` |  |
| _ExplodeGetBonusRadius | `# (explode) (explode.Val5)` |  |
| _SpearCount | `# (it)       (it.Val1)` | spear traps only |
| _Pid | `# (it)              (it.Val1)` | generic shot trap only |
| _DmgMin | `# (it)   (it.Val2)` |  |
| _DmgMax | `# (it)   (it.Val4)` |  |
| _SetPidNum | `# (_it, _pid, _min, _max) do { _it.Val1 = ((_pid) << 16) | ((_min) << 8) | (_max); } while(false)` | alert trap only |
| _SetData | `# (_it, _bag, _level, _entire) do { _it.Val4 = ((_bag) << 16) | ((_level) << 8) | (_entire); } while(false)` |  |
| _GetPid | `# (_it) ((_it.Val1 & 0xFFFF0000) >> 16)` |  |
| _GetMin | `# (_it) ((_it.Val1 & 0xFF00) >> 8)` |  |
| _GetMax | `# (_it) (_it.Val1 & 0xFF)` |  |
| _GetBag | `# (_it) ((_it.Val4 & 0xFFFF0000) >> 16)` |  |
| _GetLevel | `# (_it) ((_it.Val4 & 0xFF00) >> 8)` |  |
| _GetEntire | `# (_it) ((_it.Val4 & 0xFF))` |  |

