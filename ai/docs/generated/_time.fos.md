---
title: _time.fos
description: " FOnline: 2238 Rotators  _time.fos ..."
---

# _time.fos


FOnline: 2238
Rotators

_time.fos


## Included By

- [_macros.fos](_macros.fos.md)
- [broadcast.fos](broadcast.fos.md)
- [critter_age.fos](critter_age.fos.md)
- [mob_wave.fos](mob_wave.fos.md)
- [pdata.fos](pdata.fos.md)
- [recycler_h.fos](recycler_h.fos.md)

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __TIME__ |  |  |
| ELAPSED_TIME | `(__FullSecond)` | Time |
| REAL_MS | `# (x)              ((x) * __TimeMultiplier / 1000)` |  |
| REAL_SECOND | `# (x)          ((x) * __TimeMultiplier)` |  |
| REAL_MINUTE | `# (x)          ((x) * __TimeMultiplier * 60)` |  |
| REAL_HOUR | `# (x)            ((x) * __TimeMultiplier * 3600)` |  |
| REAL_DAY | `# (x)             ((x) * __TimeMultiplier * 86400)` |  |
| REAL_WEEK | `# (x)            ((x) * __TimeMultiplier * 604800)` |  |
| REAL_MONTH | `# (x)           ((x) * __TimeMultiplier * 2592000)` |  |
| REAL_YEAR | `# (x)            ((x) * __TimeMultiplier * 31536000)` |  |
| GAME_SECOND | `# (x)          ((x))` |  |
| GAME_MINUTE | `# (x)          ((x) * 60)` |  |
| GAME_HOUR | `# (x)            ((x) * 3600)` |  |
| GAME_DAY | `# (x)             ((x) * 86400)` |  |
| GAME_WEEK | `# (x)            ((x) * 604800)` |  |
| GAME_MONTH | `# (x)           ((x) * 2592000)` |  |
| GAME_YEAR | `# (x)            ((x) * 31536000)` |  |
| REPLICATION_SECOND | `# (x)          ((x))` |  |
| REPLICATION_MINUTE | `# (x)          ((x) * 60)` |  |
| REPLICATION_HOUR | `# (x)            ((x) * 3600)` |  |
| REPLICATION_DAY | `# (x)             ((x) * 86400)` |  |
| REPLICATION_WEEK | `# (x)            ((x) * 604800)` |  |
| REPLICATION_MONTH | `# (x)           ((x) * 2592000)` |  |
| REPLICATION_YEAR | `# (x)            ((x) * 31536000)` |  |
| AFTER | `# (x)                (ELAPSED_TIME + (x))` |  |

