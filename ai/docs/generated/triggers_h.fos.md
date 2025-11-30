---
title: triggers_h.fos
description: " FOnline: 2238 Rotators  triggers_h.fos ..."
---

# triggers_h.fos


FOnline: 2238
Rotators

triggers_h.fos


## Included By

- [cheats.fos](cheats.fos.md)
- [triggers.fos](triggers.fos.md)

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __TRIGGERS_H__ |  |  |
| GetTriggerFunction | `# (tr) (tr.Val0)` |  |
| SetTriggerFunction | `# (tr, val)tr.Val0 = val` |  |
| GetTriggerSettings | `# (tr) (tr.Val1)` |  |
| SetTriggerSettings | `# (tr, val)tr.Val1 = val` |  |
| GetTriggerGroup | `# (tr) (GetTriggerSettings(tr) & 0xFF)` |  |
| SetTriggerGroup | `# (tr, val)SetTriggerSettings(tr, ((GetTriggerSettings(tr) & 0xFFFFFF00) | ((val) & 0xFF)))` |  |
| GetTriggerDelay | `# (tr) ((GetTriggerSettings(tr) >> 16) & 0xFF)` |  |
| SetTriggerDelay | `# (tr, val)SetTriggerSettings(tr, ((GetTriggerSettings(tr) & 0xFF00FFFF) | (((val) & 0xFF) << 16)))` |  |
| GetTriggerNextTick | `# (tr) ((GetTriggerSettings(tr) >> 24) & 0xFF)` |  |
| SetTriggerNextTick | `# (tr, val)SetTriggerSettings(tr, ((GetTriggerSettings(tr) & 0x00FFFFFF) | (((val) & 0xFF) << 24)))` |  |
| TRIGGER_STANDALONE | `(0x00000100)` |  |
| TRIGGER_IGNORE_PLAYERS | `(0x00000200)` |  |
| TRIGGER_IGNORE_FOLLOWERS | `(0x00000400)` |  |
| TRIGGER_IGNORE_TRUE_NPCS | `(0x00000800)` |  |
| TRIGGER_RUN_ONCE | `(0x00001000)` |  |
| TRIGGER_KEEP_TICKING | `(0x00002000)` |  |
| TRIGGER_CRITTERLESS | `(0x00004000)` |  |
| TRIGGER_RESERVED | `(0x00008000)` |  |
| VALUE_TRIGGER_ID | `(0)` |  |
| VALUE_CRITTER_ID | `(1)` |  |
| VALUE_DIR | `(2)` |  |
| VALUE_COUNT | `(3)` |  |
| TRIGGER_FUNC_DEFAULT | `(0)` |  |
| TRIGGER_FUNC_ANTIBLOCK | `(1)` |  |
| TRIGGER_FUNC_AGGRAVATE | `(2)` |  |
| TRIGGER_FUNC_TELEPORT | `(3)` |  |

