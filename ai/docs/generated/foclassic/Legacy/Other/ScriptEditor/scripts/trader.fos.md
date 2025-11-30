---
title: trader.fos
---

# trader.fos

## Includes

- `.\scripts\_defines.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| EVENT_UPDATE_ITEMS | `0` | Time Events names |

## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| res | `int` | `npc.CreateTimeEvent(EVENT_UPDATE_ITEMS,-1,-1,8,0,0,"trader","UpdateInv")` |  |

## Functions

### init

```angelscript
void init(Critter& npc, BOOL first_time)
```

### UpdateInv

```angelscript
void UpdateInv(Critter& npc)
```


