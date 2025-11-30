---
title: slots.fos
description: "Slots by Kilgore..."
---

# slots.fos

Slots
by Kilgore

## Includes

- `_macros.fos`
- `entire.fos`
- `_msgstr.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| SLOTS_DIALOGUE | `(10001)` |  |
| SLOTS_MSG | `(13000)` |  |

## Functions

### item_init

```angelscript
void item_init(Item& item, bool firstTime)
```

### e_Ding

```angelscript
uint e_Ding(array<uint>@ values)
```

### _Play

```angelscript
bool _Play(Item& item, Critter& cr, int skill)
```

### dlg_Score

```angelscript
void dlg_Score(Critter& player, Critter@ npc, string@ text)
```

### HitMachine

```angelscript
uint HitMachine(Critter& player, Critter@ cr)
```


