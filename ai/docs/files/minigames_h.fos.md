---
title: minigames_h.fos
description: " FOnline: 2238 Rotators  minigames_h.fos ..."
---

# minigames_h.fos


FOnline: 2238
Rotators

minigames_h.fos


## Included By

- [cheats.fos](cheats.fos.md)
- [main.fos](main.fos.md)
- [minigames.fos](minigames.fos.md)
- [name_colorizing.fos](name_colorizing.fos.md)
- [replication.fos](replication.fos.md)

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __MINIGAMES_H__ |  |  |
| _minigame | `# (cr)                 cr.ParamBase[ST_MINIGAME_DATA]` |  |
| _hasMinigame | `# (cr)              _minigame(cr) != 0` |  |
| _resetMinigame | `# (cr)            _minigame(cr) = 0` |  |
| _setMinigameTeam | `# (cr, team)_minigame(cr) = ((_minigame(cr) & 0xFFFFFFF0) | ((team) & 0xF))` | Mask 0x0000000F: MinigameTeam |
| _getMinigameTeam | `# (mgData)      ((mgData) & 0xF)` |  |
| _setMinigameId | `# (cr, id)cr.ParamBase[ST_MINIGAME_DATA] = ((cr.Param[ST_MINIGAME_DATA] & 0xFFFFFF0F) | (((id) & 0xF) << 4))` | Mask 0x000000F0: MinigameId |
| _getMinigameId | `# (mgData) (((mgData) >> 4) & 0xF)` |  |
| _getMinigameTeamAndId | `# (mgData) ((mgData) & 0xFF)` | Mask 0x000000FF: MinigameTeamAndId (MinigameTeam and MinigameId combined) |
| _setMinigameFlags | `# (cr, flags)cr.ParamBase[ST_MINIGAME_DATA] = ((cr.Param[ST_MINIGAME_DATA] & 0xFFFFF0FF) | (((flags) & 0xF) << 8))` | Mask 0x00000F00: MinigameFlags |
| _getMinigameFlags | `# (mgData) (((mgData) >> 8) & 0xF)` |  |
| MINIGAME_PERSISTENT | `(0x1)` |  |
| MINIGAME_FORCE_COLOR | `(0x2)` |  |
| _setMinigameData | `# (cr, data)cr.ParamBase[ST_MINIGAME_DATA] = ((cr.Param[ST_MINIGAME_DATA] & 0x00000FFF) | ((data & 0xFFFFF) << 12))` | Custom Data (remember not to overwrite first 12 bits) Mask 0xFFFFF000: Generic 20 bit unsigned number |
| _getMinigameData | `# (mgData) ((mgData) >> 12)` |  |
| _getPrevDSpawnId | `# (spawn, team)(ODD(team) ? spawn.Val3 : spawn.Val4)` |  |
| _getNextDSpawnId | `# (spawn, team)(ODD(team) ? spawn.Val4 : spawn.Val3)` |  |
| _getDSpawnTransportToMap | `# (spawn)   (spawn.Val5)` |  |
| DSPAWN_CAPTURE_TIME | `# (_dSpawn) (_dSpawn.Val1 >> 24)` |  |

