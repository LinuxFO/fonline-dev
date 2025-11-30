---
title: quests.fos
description: " FOnline: 2238 Rotators  quests.fos ..."
---

# quests.fos


FOnline: 2238
Rotators

quests.fos


## Includes

- `_macros.fos`
- `serializator.fos`
- `changes_queue_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| GQ_LIFE_TIME | `(REAL_DAY(7))` |  |
| GQ_FAILED_STATE | `(100)` |  |
| GQ_ANYDATA_PREFIX | `("GroupQuest")` |  |

## Classes

### GroupQuest

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| Id | `uint` |  |  |
| LeaderId | `uint` |  |  |
| StringsLvar | `uint` |  |  |
| TimeStamp | `uint` |  |  |
| GroupIds | `array<uint>` |  |  |

**Methods**

#### Valid
```angelscript
bool Valid() { return Id != uint(-1); }
```

#### Alive
```angelscript
bool Alive() { return TimeStamp + GQ_LIFE_TIME > ELAPSED_TIME; }
```

#### GetId
```angelscript
uint GetId() { return Id; }
```

#### Save
```angelscript
void Save()
```

#### Delete
```angelscript
void Delete()
```

#### UpdateState
```angelscript
void UpdateState(uint state)
```

### GroupQuestManager

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| NextId | `uint` |  |  |
| CurrentIds | `array<uint>` |  |  |

**Methods**

#### Init
```angelscript
void Init()
```

#### Save
```angelscript
void Save()
```

#### NewQuest
```angelscript
GroupQuest@ NewQuest(uint strings_var, uint leader_id, array<uint>@ group_ids)
```

#### EndQuest
```angelscript
bool EndQuest(uint id)
```


## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| GroupQuestMngr | `[GroupQuestManager](quests.fos.md)@` |  |  |

## Functions

### GroupQuestInit

```angelscript
void GroupQuestInit()
```

### StartGroupQuest

```angelscript
bool StartGroupQuest(uint control_lvar, uint strings_lvar, Critter& leader, array<Critter@>@ group, uint start_state)
```

### StartGroupQuest

```angelscript
bool StartGroupQuest(uint control_lvar, uint strings_lvar, Critter& leader, array<Critter@>@ group, uint start_state, bool safe)
```

### EndGroupQuest

```angelscript
bool EndGroupQuest(uint control_lvar, Critter& cr, int end_state)
```

### ResetGroupQuest

```angelscript
bool ResetGroupQuest(uint control_lvar, Critter& cr)
```

### ChangeGroupQuestParam

```angelscript
bool ChangeGroupQuestParam(uint control_lvar, Critter& cr, int param, int value)
```

### UpdateGroupQuestState

```angelscript
bool UpdateGroupQuestState(uint control_lvar, Critter& cr, uint state)
```

### d_IsGroupQuestLeader

```angelscript
bool d_IsGroupQuestLeader(Critter& player, Critter@ npc, int control_lvar)
```

### r_ChangeGroupQuestParam

```angelscript
void r_ChangeGroupQuestParam(Critter& player, Critter@ npc, int control_lvar, int param, int value)
```

### r_UpdateGroupQuestState

```angelscript
void r_UpdateGroupQuestState(Critter& player, Critter@ npc, int control_lvar, int state)
```

### r_EndGroupQuest

```angelscript
void r_EndGroupQuest(Critter& player, Critter@ npc, int control_lvar, int end_state)
```

### r_ResetGroupQuest

```angelscript
void r_ResetGroupQuest(Critter& player, Critter@ npc, int control_lvar)
```


