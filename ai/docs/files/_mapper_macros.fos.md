---
title: _mapper_macros.fos
description: " FOnline: 2238 Rotators  _mapper_macros.fos ..."
---

# _mapper_macros.fos


FOnline: 2238
Rotators

_mapper_macros.fos


## Includes

- `_mapper_defines.fos`
- `_math.fos`
- `_colors.fos`

## Included By

- [mapper_autowall.fos](mapper_autowall.fos.md)
- [mapper_generators.fos](mapper_generators.fos.md)
- [mapper_grid.fos](mapper_grid.fos.md)
- [mapper_gui.fos](mapper_gui.fos.md)
- [mapper_utils.fos](mapper_utils.fos.md)

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __MAPPER_MACROS__ |  |  |
| valid | `# (__ptr)  (@__ptr != null)` |  |
| append_array | `# (a1, a2) do { uint a1len = a1.length(); uint a2len = a2len = a2.length(); a1.resize(a1len + a2len); for(uint iter = 0; iter < a2len; iter++) { a1[a1len + iter] = a2[iter]; } } while(false);` | appending an array |
| _TurnRight | `# (dir, times)(((dir) + (times)) % 6)` | Changing directions |
| _TurnLeft | `# (dir, times)(((dir) - (times)) % 6)` |  |
| _TurnAround | `# (dir) (_TurnRight((dir), 3))` |  |

