---
title: _math.fos
description: " FOnline: 2238 Rotators  _math.fos ..."
---

# _math.fos


FOnline: 2238
Rotators

_math.fos


## Included By

- [_macros.fos](_macros.fos.md)
- [_mapper_macros.fos](_mapper_macros.fos.md)
- [blackjack.fos](blackjack.fos.md)
- [caravans_h.fos](caravans_h.fos.md)
- [economy.fos](economy.fos.md)
- [explode.fos](explode.fos.md)
- [globalmap_group.fos](globalmap_group.fos.md)
- [item_attributes.fos](item_attributes.fos.md)
- [rq_cave.fos](rq_cave.fos.md)
- [town.fos](town.fos.md)

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __MATH__ |  |  |
| PI | `(3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067982148086513282306647093844)` |  |
| DEG2RAD | `(0.01745329251994329576923690768488)` |  |
| POW2 | `# (a)                 ((a) * (a))` |  |
| POW3 | `# (a)                 ((a) * (a) * (a))` |  |
| POW | `\` |  |
| ABS | `# (val)                (((val) > 0) ? (val) : (-(val)))` |  |
| DISTANCE | `# (x1, y1, x2, y2)DIST(x1, y1, x2, y2)` |  |
| MAKEWORD | `# (a, b)(uint16((uint8(a)) | (uint16(uint8(b))) << 8))` |  |
| MAKELONG | `# (a, b)(int32((uint16(a)) | (uint32(uint16(b))) << 16))` |  |
| LOWORD | `# (l)               (uint16(l))` |  |
| HIWORD | `# (l)               (uint16((uint32(l) >> 16) & 0xFFFF))` |  |
| LOBYTE | `# (w)               (uint8(w))` |  |
| HIBYTE | `# (w)               (uint8((uint16(w) >> 8) & 0xFF))` |  |
| LBS_TO_GRAMM | `# (lbs)       ((lbs) * 453)` |  |
| GRAMM_TO_LBS | `# (grm)       ((grm) / 453)` |  |
| NUMERICAL_NUMBER | `# (num)   ((num) * ((num) + 1) / 2)` |  |
| DIST | `# (x1, y1, x2, y2)(sqrt(((x1) - (x2)) * ((x1) - (x2)) + ((y1) - (y2)) * ((y1) - (y2))))` |  |
| EVEN | `# (num)               ((num) % 2 == 0)` |  |
| ODD | `# (num)                (!EVEN(num))` |  |

