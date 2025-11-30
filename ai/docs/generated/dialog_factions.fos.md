---
title: dialog_factions.fos
description: " FOnline: 2238 Rotators  dialog_factions.fos ..."
---

# dialog_factions.fos


FOnline: 2238
Rotators

dialog_factions.fos


## Includes

- `_macros.fos`
- `factions_h.fos`
- `factions_bases_h.fos`
- `utils_h.fos`

## Included By

- [dialog.fos](dialog.fos.md)

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __DIALOG_FACTIONS__ |  |  |

## Functions

### d_IsLowerRankThan

* * Checks if player's rank in his/her faction is lower than value that is passed from dialog 

```angelscript
bool d_IsLowerRankThan(Critter& player, Critter@ npc, int rank)
```

### d_IsHigherRankThan

* * Checks if players' rank in his/her faction is higher than given value 

```angelscript
bool d_IsHigherRankThan(Critter& player, Critter@, int rank)
```

### d_HasFactionBase

```angelscript
bool d_HasFactionBase(Critter& player, Critter@ npc)
```

### d_IsLeader

* * Checks if the player is a leader of some faction. 

```angelscript
bool d_IsLeader(Critter& player, Critter@ npc)
```

### d_IsMember

* * Checks if the player is member of the same faction as npc. 

```angelscript
bool d_IsMember(Critter& player, Critter@ npc)
```

### d_IsNotMember

* * Checks if player is not member of the npc's faction. 

```angelscript
bool d_IsNotMember(Critter& player, Critter@ npc)
```

### d_IsMemberOf

* * Checks if the player is member of faction given by the parameter. * @param group The faction's id 

```angelscript
bool d_IsMemberOf(Critter& player, Critter@ npc, int group)
```

### d_IsNotMemberOf

* * Checks if player is not a member of faction given by the parameter. * @param group The faction's id 

```angelscript
bool d_IsNotMemberOf(Critter& player, Critter@ npc, int group)
```

### d_IsMemberOfSomeFaction

* * Checks if the player is member of some faction. 

```angelscript
bool d_IsMemberOfSomeFaction(Critter& player, Critter@ npc)
```

### d_NotMemberOfAnyFaction

* * Checks if player isn't member of any faction. 

```angelscript
bool d_NotMemberOfAnyFaction(Critter& player, Critter@ npc)
```

### d_IsGangMember

* * Checks if player is member of gang (playerdriven faction). 

```angelscript
bool d_IsGangMember(Critter& player, Critter@ npc)
```

### d_BigFactionMember

* * Checks whether given player is the member of one of the "big" (NPC) factions. 

```angelscript
bool d_BigFactionMember(Critter& player, Critter@ npc)
```

### r_AddMember

* * Adds the critter (player I assume) as a faction member. This bypass normal invitation procedure. * @remarks It uses recruiter faction LVAR to determine on which faction/DB to operate 

```angelscript
void r_AddMember(Critter& initiate, Critter@ recruiter)
```

### r_JoinFaction

* * Works very much like r_AddMember, the main difference is that faction that the critter should join is specified in the val parameter instead of being taking from NPC faction. 

```angelscript
void r_JoinFaction(Critter& player, Critter@ npc, int val)
```

### r_AddLeader

* * Adds the player as a faction member and leader * @remarks it uses recruiter faction LVAR to determine on which faction/DB to operate 

```angelscript
void r_AddLeader(Critter& initiate, Critter@ recruiter)
```

### r_AddFactionPoints

* * Adds a number to the player's faction points. Can be used to subtract the points by passing a negative value to add. * @param faction Number of the faction, must be one of the supported npc factions. * @param val Value to add. 

```angelscript
void r_AddFactionPoints(Critter& player, Critter@ npc, int faction, int val)
```

### dlg_ShowFaction

* * Shows the faction the player is member of. 

```angelscript
void dlg_ShowFaction(Critter& player, Critter@ npc, string@ text)
```

### dlg_DisplayFactionPoints

* * Shows the player's faction points. 

```angelscript
void dlg_DisplayFactionPoints(Critter& player, Critter@ npc, string@ text)
```

### d_IsDisguised

* * Checks if the player is disguised as member of the same faction as npc. 

```angelscript
bool d_IsDisguised(Critter& player, Critter@ npc)
```

### d_IsNotDisguised

* * Checks if the player is not disguised as member of the same faction as npc. 

```angelscript
bool d_IsNotDisguised(Critter& player, Critter@ npc)
```


