---
title: _math.fos
description: "�������������� �����������..."
---

# _math.fos

�������������� �����������

## Included By

- [_macros.fos](../../../../../PReloaded/Server/scripts/_macros.fos.md)
- [_mapper_macros.fos](../../../../../PReloaded/Server/scripts/_mapper_macros.fos.md)
- [blackjack.fos](../../../../../PReloaded/Server/scripts/blackjack.fos.md)
- [caravans_h.fos](../../../../../PReloaded/Server/scripts/caravans_h.fos.md)
- [economy.fos](../../../../../PReloaded/Server/scripts/economy.fos.md)
- [explode.fos](../../../../../PReloaded/Server/scripts/explode.fos.md)
- [globalmap_group.fos](../../../../../PReloaded/Server/scripts/globalmap_group.fos.md)
- [item_attributes.fos](../../../../../PReloaded/Server/scripts/item_attributes.fos.md)
- [rq_cave.fos](../../../../../PReloaded/Server/scripts/rq_cave.fos.md)
- [town.fos](../../../../../PReloaded/Server/scripts/town.fos.md)
- [_all_defines.fos](_all_defines.fos.md)

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __MATH__ |  |  |
| MIN | `#(a,b) (((a)<(b))?(a):(b))` |  |
| MAX | `#(a,b) (((a)>(b))?(a):(b))` |  |
| POW2 | `#(a) ((a)*(a))` | #define SQRT #(a) mySQRT((a)); |
| POW3 | `#(a) ((a)*(a)*(a))` |  |
| MAKEWORD | `#(a, b)      ((a) | ((b) << 8))` | #define MAKEWORD #(a, b)      ((uint16)(((uint8)(a)) | ((uint16)((uint8)(b))) << 8)) #define MAKELONG #(a, b)      ((int32)(((uint16)(a)) | ((uint32)((uint16)(b))) << 16)) #define LOWORD #(l)           ((uint16)(l)) #define HIWORD #(l)           ((uint16)(((uint32)(l) >> 16) & 0xFFFF)) #define LOBYTE #(w)           ((uint8)(w)) #define HIBYTE #(w)           ((uint8)(((uint16)(w) >> 8) & 0xFF)) |
| MAKELONG | `#(a, b)      ((a) | ((b) << 16))` |  |
| LOWORD | `#(l)           ((l) & 0xFFFF)` |  |
| HIWORD | `#(l)           ((((l) >> 16) & 0xFFFF))` |  |
| LOBYTE | `#(w)           ((w) & 0xFF)` |  |
| HIBYTE | `#(w)           (((w) >> 8) & 0xFF)` |  |

