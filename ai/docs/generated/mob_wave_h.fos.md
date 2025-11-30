---
title: mob_wave_h.fos
description: " FOnline: 2238 Rotators  mob_wave_h.fos ..."
---

# mob_wave_h.fos


FOnline: 2238
Rotators

mob_wave_h.fos


## Included By

- [main.fos](main.fos.md)
- [mob_wave.fos](mob_wave.fos.md)

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __MOB_WAVE_H__ |  |  |
| MOB_WAVE_LOCATION | `# (data)       data[0]` |  |
| MOB_WAVE_TYPE | `# (data)           data[1]` |  |
| MOB_WAVE_LEVEL | `# (data)          data[2]` |  |
| MOB_WAVE_COUNT | `# (data)          data[3]` |  |
| MOB_WAVE_MOBS | `# (data)           data[4]` |  |
| MOB_WAVE_RESET | `# (data)          data[5]` |  |
| MOB_WAVE_TIME_SCALE | `# (data)     data[6]` |  |
| MOB_WAVE_TIME_SPAWNING_BASE | `(REAL_SECOND(15))` |  |
| MOB_WAVE_TIME_SPAWNING | `# (data)  ((MOB_WAVE_TIME_SPAWNING_BASE * MOB_WAVE_TIME_SCALE(data)) / 100)` |  |
| MOB_WAVE_TIME_WARNING | `# (data)   (((Random(REAL_SECOND(MobWaves[MOB_WAVE_TYPE(data)][MOB_WAVE_LEVEL(data)][0][0]), REAL_SECOND(MobWaves[MOB_WAVE_TYPE(data)][MOB_WAVE_LEVEL(data)][0][1])) - MOB_WAVE_TIME_SPAWNING_BASE) * MOB_WAVE_TIME_SCALE(data)) / 100)` |  |
| MOB_WAVE_MAX_MOBS | `(50)` |  |
| _LocationHasMobWave | `# (loc) (loc.GetMapByIndex(0).GetData(MAP_DATA_MOB_WAVE) > 0)` |  |

