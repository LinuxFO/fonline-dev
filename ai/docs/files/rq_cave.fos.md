---
title: rq_cave.fos
description: " FOnline: 2238 Rotators  rq_cave.fos ..."
---

# rq_cave.fos


FOnline: 2238
Rotators

rq_cave.fos


## Includes

- `_macros.fos`
- `mapdata_h.fos`
- `utils_h.fos`
- `_math.fos`
- `reputations_h.fos`
- `logging_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| CAVE_STATUS_NONE | `(0)` |  |
| CAVE_STATUS_BRIEFED | `(1)` |  |
| CAVE_STATUS_ONGOING | `(2)` |  |
| CAVE_STATUS_COMPLETED | `(3)` |  |

## Functions

### d_None

```angelscript
bool d_None(Critter& player, Critter@ npc)
```

### d_CanAsk

```angelscript
bool d_CanAsk(Critter& player, Critter@ npc)
```

### d_Briefed

```angelscript
bool d_Briefed(Critter& player, Critter@ npc)
```

### d_OnGoing

```angelscript
bool d_OnGoing(Critter& player, Critter@ npc)
```

### d_Completed

```angelscript
bool d_Completed(Critter& player, Critter@ npc)
```

### d_NotCompleted

```angelscript
bool d_NotCompleted(Critter& player, Critter@ npc)
```

### d_HasStuff

```angelscript
bool d_HasStuff(Critter& player, Critter@ npc)
```

### r_ReceiveReward

```angelscript
void r_ReceiveReward(Critter& player, Critter@ npc)
```

### r_CompleteQuest

```angelscript
void r_CompleteQuest(Critter& player, Critter@ npc)
```

### r_AcceptQuest

```angelscript
void r_AcceptQuest(Critter& player, Critter@ npc)
```

### r_ShowQuest

```angelscript
uint r_ShowQuest(Critter& player, Critter@ npc)
```

### r_GenerateQuest

Generate and show quest

```angelscript
uint r_GenerateQuest(Critter& player, Critter@ npc)
```

### SpawnLoc

```angelscript
uint SpawnLoc(Critter@ player, Critter& npc)
```


