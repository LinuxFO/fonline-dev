---
title: questpool.fos
description: " FOnline: 2238 Rotators  questpool.fos ..."
---

# questpool.fos


FOnline: 2238
Rotators

questpool.fos


## Includes

- `_macros.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __QUESTPOOL__ |  |  |

## Classes

### Quest

  Info about quest 

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| lvar | `int` |  | id of the lvar connected with that quest. The most important value, it in fact identifies quest |
| dialog | `uint` |  | dialog node that is responsible for quest introduction |
| dumbDialog | `uint` |  | dialog node for 'dumb' characters |
| about | `uint` |  | 'about' node, when npc is asking you about progress |
| dumbAbout | `uint` |  | 'about' node for dumb characters |
| lvarInitial | `int` |  | initial value of lvar (to activate quest), quest is only avaialble if lvar value is equal to 0 |
| lvarFailed | `int` |  | 'failed' value of lvar (to discard/cancel quest) |
| lvarFinished | `int` |  | 'finished' value of lvar, when quest is succesfully finished |
| time | `uint` |  | time (in game minutes) in which the quest is going back to the pool (even if not solved) |
| timeAcquired | `uint` |  | time (in game-minutes) at which quest was acquired. If this value is greater than time, we clear it, so that quest can be available again |
| requiredSkills | `array<int>` |  | skills which we require for that quest to be given (see skill defines in _defines.fos) |
| requiredSkillsValues | `array<int>` |  | min skill levels which are required for quest |

**Methods**

#### Initial
```angelscript
Quest@ Initial(int lvarInitial)
```

#### Failed
```angelscript
Quest@ Failed(int lvarFailed)
```

#### Finished
```angelscript
Quest@ Finished(int lvarFinished)
```

#### Time
```angelscript
Quest@ Time(uint time)
```

#### RequiredSkill
```angelscript
Quest@ RequiredSkill(int skill, int value)
```

#### IsAvailable
 Checks whether quest is available 

```angelscript
bool IsAvailable(Critter@ player)
```

#### SetTimeAcquired
 Sets the time at which given quest was acquired 

```angelscript
void SetTimeAcquired(int time)
```

### QuestPool

 Array with quests that can be randomly given to player 

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| data | `array<uint>` |  | useful values stored for quests used when quest is added to the pool |
| npcId | `uint` |  | id of the critter to which questpool belongs |

**Methods**

#### AddQuest
 Add quest object to the array, and reads appropriate data if exists 

```angelscript
Quest@ AddQuest(Quest@ quest)
```

#### AddQuest
  Adds quest to the pool 

```angelscript
Quest@ AddQuest(uint lvar, uint dialog, uint dumbDialog, uint about, uint dumbAbout)
```

#### GetRandomQuest
 Gets the random quest from the list of available ones  Returns quest, or null if there is nothing available

```angelscript
Quest@ GetRandomQuest(Critter@ player)
```

#### GetQuest
 Get quest with given lvar id  Return Quest object, or null if not found

```angelscript
Quest@ GetQuest(int lvar)
```

#### GetDataIndex
 Gets the index to the data associated with quest that has given lvar id  Returns 0 if not found ( 0 can't be that index nonethless, cause data is stored using the lvar,data,lvar,data layout)

```angelscript
uint GetDataIndex(uint lvar)
```

#### IsAvailable
 Checks if the quest with specific lvar is still available 

```angelscript
bool IsAvailable(int lvar, Critter@ player)
```

#### Store
 Stores needed values in AnyData array  Returns true if success, false otherwise

```angelscript
bool Store()
```

### CQuestPoolCache

 Caches QuestPool so that there is no need to create new objects each time the script asks for it 

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| pools | `array<[QuestPool](questpool.fos.md)>` |  |  |
| indices | `array<uint>` |  | ids of the npcs to which pools are attached |

**Methods**

#### GetPool
 Gets pool cached at given id, or create new one 

```angelscript
QuestPool@ GetPool(uint npcId)
```


## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| QuestPoolCache | `[CQuestPoolCache](questpool.fos.md)` |  | global manager |

## Functions

### GetQuestPool

 Retrieves the QuestPool object associated with the given NPC  Returns null if the QuestPool don't exist for a given NPC

```angelscript
QuestPool@ GetQuestPool(Critter@ npc)
```

### r_ChooseQuest

 Chooses random quest for player, and stores its lvar id in the unique variable so that if player refuses and ask next time for a job, NPC will give the same again (if available) or choose another (if not) after succesfull choice, it jumps to proper dialog node

```angelscript
uint r_ChooseQuest(Critter& player, Critter@ npc, int val)
```

### r_AssignQuest

 Activates quest if player agrees to do it 

```angelscript
void r_AssignQuest(Critter& player, Critter@ npc, int val)
```

### r_AboutQuest

 Jumps to the node which is used for dialogs about quest in progress 

```angelscript
uint r_AboutQuest(Critter& player, Critter@ npc, int val)
```

### r_DiscardQuest

 Sets quest' lvar to 'failed' state, it means player don't want to do that quest 

```angelscript
void r_DiscardQuest(Critter& player, Critter@ npc, int val)
```

### r_CancelQuest

 Sets quest' lvar to 'failed' state, it means player don't want to do that quest 

```angelscript
void r_CancelQuest(Critter& player, Critter@ npc, int val)
```

### r_FinishQuest

 Clears the quest timeAcquired value, and clear assigned 'job' UVAR, so that quest now is finished (lvar should be changed independently) 

```angelscript
void r_FinishQuest(Critter& player, Critter@ npc, int val)
```

### d_QuestInProgress

 Checks if the quest currently chosen for player is in progress (active and not failed) 

```angelscript
bool d_QuestInProgress(Critter& player, Critter@ npc, int val)
```

### d_NoQuestActive

 Checks if player has got no quest assigned 

```angelscript
bool d_NoQuestActive(Critter& player, Critter@ npc, int val)
```


