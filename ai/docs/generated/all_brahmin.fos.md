---
title: all_brahmin.fos
description: " FOnline: 2238 Rotators  all_brahmin.fos ..."
---

# all_brahmin.fos


FOnline: 2238
Rotators

all_brahmin.fos


## Includes

- `_animation.fos`
- `_macros.fos`
- `npc_common_h.fos`
- `npc_planes_h.fos`
- `utils_h.fos`

## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| Shitrate | `uint` | `333` |  |

## Functions

### critter_init

```angelscript
void critter_init(Critter& npc, bool firstTime)
```

### _Domesticated

```angelscript
void _Domesticated(Critter& npc, bool firstTime)
```

### _Wild

```angelscript
void _Wild(Critter& npc, bool firstTime)
```

### change_shitrate

```angelscript
void change_shitrate(Critter& cr, int p0, int p1, int p2)
```

### _Idle

```angelscript
void _Idle(Critter& npc)
```

### IsDung

 Checks if item is brahmin crap 

```angelscript
bool IsDung(Item@ item)
```

### Shit

```angelscript
void Shit(Critter& brahmin)
```

### plane_agitated

* * plane AI_PLANE_MISC * Domesticated brahmin gets agitated by someone and will try to ram into the target that pissed him/her off. 

```angelscript
void plane_agitated(Critter& brahmin)
```

### t_block

* *  Brahmin blocker trigger (causes brahmin to return to home hex) * 

```angelscript
void t_block(Critter& cr, Scenery& trigger, bool entered, uint8 dir)
```


