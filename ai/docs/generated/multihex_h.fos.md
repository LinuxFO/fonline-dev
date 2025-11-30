---
title: multihex_h.fos
description: " FOnline: 2238 Rotators  multihex_h.fos ..."
---

# multihex_h.fos


FOnline: 2238
Rotators

multihex_h.fos


## Included By

- [grave.fos](grave.fos.md)
- [lockers.fos](lockers.fos.md)
- [multihex.fos](multihex.fos.md)

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __MULTIHEX_H__ |  |  |
| MHEX_MOVE | `# (dir1, step1, dir2, step2)((((step2) & 0xFF) << 24) | (((dir2) & 0xFF) << 16) | (((step1) & 0xFF) << 8) | ((dir1) & 0xFF))` |  |
| MHEX_BLOCK_NOTHING | `(ITEM_FLAG_NO_BLOCK | ITEM_FLAG_SHOOT_THRU | ITEM_FLAG_LIGHT_THRU)` |  |
| MHEX_BLOCK_WALKING | `(ITEM_FLAG_SHOOT_THRU | ITEM_FLAG_LIGHT_THRU)` |  |
| MHEX_BLOCK_ALL | `(0)` |  |
| MHEX_PARENT | `# (mhex) (mhex.Val0)` |  |
| MHEX_NEXT | `# (mhex) (mhex.Val1)` |  |
| MHEX_STATE_1 | `# (mhex) (mhex.Val2)` |  |
| MHEX_STATE_2 | `# (mhex) (mhex.Val3)` |  |
| MHEX_SET_PARENT | `# (mhex, parent)(mhex.Val0 = parent.Id)` |  |
| MHEX_SET_NEXT | `# (mhex, next)(mhex.Val1 = next.Id)` |  |
| MHEX_SET_STATE_1 | `# (mhex, state)(mhex.Val2 = state)` |  |
| MHEX_SET_STATE_2 | `# (mhex, state)(mhex.Val3 = state)` |  |
| MHEX_ORPHANED | `# (mhex) (MHEX_PARENT(mhex) == 0)` |  |

