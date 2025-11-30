---
title: rq_fetcher.fos
description: " FOnline: 2238 Rotators  rq_fetcher.fos ..."
---

# rq_fetcher.fos


FOnline: 2238
Rotators

rq_fetcher.fos


## Includes

- `_macros.fos`
- `utils_h.fos`
- `reputations_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| FETCH_STATUS_NONE | `(0)` |  |
| FETCH_STATUS_BRIEFED | `(1)` |  |
| FETCH_STATUS_ONGOING | `(2)` |  |

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

### d_HasStuff

```angelscript
bool d_HasStuff(Critter& player, Critter@ npc)
```

### r_CompleteQuest

```angelscript
void r_CompleteQuest(Critter& player, Critter@ npc)
```

### r_AcceptQuest

```angelscript
void r_AcceptQuest(Critter& player, Critter@ npc)
```

### dlg_ShowNum

```angelscript
void dlg_ShowNum(Critter& player, Critter@ npc, string@ text)
```

### r_ShowQuest

```angelscript
uint r_ShowQuest(Critter& player, Critter@ npc)
```

### r_GenerateFetchQuest

Generate and show fetch quest

```angelscript
uint r_GenerateFetchQuest(Critter& player, Critter@ npc)
```


