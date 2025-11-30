---
title: factions_terminal.fos
description: " FOnline: 2238 Rotators  factions_terminal.fos ..."
---

# factions_terminal.fos


FOnline: 2238
Rotators

factions_terminal.fos


## Includes

- `_macros.fos`
- `factions_h.fos`
- `factions_bases_h.fos`
- `mapdata_h.fos`
- `utils_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| TERMINAL_DIALOG | `(9060)` |  |
| SEND_ERROR_RETURN | `# (cr, error)     { cr.SayMsg(SAY_DIALOG, TEXTMSG_TEXT, error); return; }` |  |
| IF_NOT_VALID_RETURN | `# (obj, name)  { if(not valid(obj)) { Log("Null value: " + name); return; } }` |  |
| STR_WRONG_FACTION_NAME | `(30)` | dlg strs |
| STR_STATUS | `(10)` |  |
| STR_RANK | `(20)` |  |
| STR_CHANNEL_CHANGED | `(31)` |  |
| STR_WRONG_CHANNEL | `(32)` |  |
| STR_PLAYER_HAS_CLAIMED_LEADERSHIP | `(40)` |  |
| STR_YOUVE_CLAIMED_LEADERSHIP | `(41)` |  |
| STR_CHOOSE_ACTION | `(42)` |  |
| FORCE_DIALOG_COMPLETED | `(15)` | dialog lines |
| FORCE_DIALOG_DB_UPDATED | `(22)` |  |
| FORCE_DIALOG_SHOW_RECORD | `(18)` |  |
| FORCE_DIALOG_ERROR | `(29)` |  |
| FORCE_DIALOG_CHOOSE_PLAYER | `(17)` |  |
| FORCE_DIALOG_READ_ONLY | `(30)` |  |
| FORCE_DIALOG_SHOW_BASE | `(200)` |  |
| FORCE_DIALOG_FACTION_ADDED | `(300)` |  |
| FORCE_DIALOG_MENU_MEMBERS | `(5)` |  |
| FORCE_DIALOG_MEMBEROP_FORBIDDEN | `(45)` | when you can't promote/demote/expell |
| FORCE_DIALOG_MEMBEROP_OK | `(43)` | for promote/demote/expel with player name |
| FORCE_DIALOG_JOINED | `(110)` | nodes for news types |
| FORCE_DIALOG_RESIGNED | `(111)` |  |
| FORCE_DIALOG_EXPELLED | `(112)` |  |
| FORCE_DIALOG_PROMOTED | `(113)` |  |
| FORCE_DIALOG_DEMOTED | `(114)` |  |
| FORCE_DIALOG_CLAIMED | `(115)` |  |
| FORCE_DIALOG_LEADER | `(116)` |  |
| FORCE_DIALOG_OVERTHROWN | `(117)` |  |
| FORCE_DIALOG_NO_NEWS | `(118)` |  |

## Functions

### GetTerminalFaction

 Gets the faction to whihc terminal belongs using map.GetData(MAP_DATA_FACTION) value  USE ONLY WITH TERMINAL!!!

```angelscript
uint GetTerminalFaction(Critter& player)
```

### IncreaseUpdateSeq

increases the update_seq for given faction database this value is later used for player's data synchronization

```angelscript
void IncreaseUpdateSeq(uint faction_id)
```

### s_Terminal

```angelscript
bool s_Terminal(Critter& player, Scenery& terminal, int skill, Item@ item)
```

### dlg_TerminalWelcome

 Adds the faction name to the lexem in the welcome screen of the terminal. 

```angelscript
void dlg_TerminalWelcome(Critter& player, Critter@ terminal, string@ text)
```

### dlg_FactionName

 Adds the faction name to be used with the lexem 'faction' 

```angelscript
void dlg_FactionName(Critter& player, Critter@ terminal, string@ text)
```

### dlg_ChoosePlayer

 Gets the id of the player with specified name, and store it in the local variable: LVAR_terminal_current, so that it can be later used in other value modifications functions  it is used by terminal

```angelscript
uint dlg_ChoosePlayer(Critter& player, Critter@ terminal, string@ playerName)
```

### dlg_ShowRecord

 Displays the previously selected player's data (in the terminal) 

```angelscript
void dlg_ShowRecord(Critter& player, Critter@ npc, string@ say)
```

### GenerateDescription

 Generates description for record with given data 

```angelscript
string@ GenerateDescription(uint id, uint faction_id, uint rank, uint status, int8 reputation)
```

### r_SelectMember

 Selects member record  value: -1: previous member 0: first member in db (this has to be called first) 1: next member 

```angelscript
uint r_SelectMember(Critter& player, Critter@ npc, int value)
```

### r_SelectRecord

 Selects record  value: -1: previous member 0: first member in db (this has to be called first) 1: next member 

```angelscript
uint r_SelectRecord(Critter& player, Critter@ npc, int value)
```

### IsReadOnly

 Checks whenever current record belongs to a member, so other member cannot modify them 

```angelscript
bool IsReadOnly(uint faction, uint id)
```

### r_ModifyStatus

 Changes the status of the player stored in db Player id was previously chosen, and is stored in the local variable LVAR_terminal_current 

```angelscript
uint r_ModifyStatus(Critter& player, Critter@ npc, int value)
```

### r_ModifyReputation

 Changes the reputation of the actually selected player with regard to the player operating terminal Player id was previously chosen, and is stored in the local variable LVAR_terminal_current  

```angelscript
void r_ModifyReputation(Critter& player, Critter@ npc, int value)
```

### r_ModifyRank

 Changes the rank of the player stored in db Player id was previously chosen, and is stored in the local variable LVAR_terminal_current 

```angelscript
uint r_ModifyRank(Critter& player, Critter@ npc, int value)
```

### r_ModifyFaction

 Changes the faction of the player stored in db Player id was previously chosen, and is stored in the local variable LVAR_terminal_current 

```angelscript
uint r_ModifyFaction(Critter& player, Critter@ npc, int value)
```

### dlg_ModifyFactionByName

 Changes the faction of the player stored in db faction name has to be entered via Say mode Player id was previously chosen, and is stored in the local variable LVAR_terminal_current 

```angelscript
uint dlg_ModifyFactionByName(Critter& player, Critter@ npc, string@ say)
```

### dlg_Invite

 Invites player to be faction member  Params: player - player that operates the terminal npc - npc that is performing operation 

```angelscript
uint dlg_Invite(Critter& recruiter, Critter@ npc, string@ playerName)
```

### r_ConfirmInvitation

 Player confirms invitation, thus making himself a member 

```angelscript
void r_ConfirmInvitation(Critter& player, Critter@ npc, int value)
```

### dlg_PromoteMember

 Promote member of the faction  Params: player - player that performs operation 

```angelscript
uint dlg_PromoteMember(Critter& player, Critter@ npc, string@ playerName)
```

### r_PromoteMember

 Promotes actually selected member 

```angelscript
uint r_PromoteMember(Critter& player, Critter@ npc, int value)
```

### PromoteMember

 Helper func - promotes if it possible, returns false otherwise 

```angelscript
bool PromoteMember(uint promoterId, uint promoteeId)
```

### dlg_DemoteMember

 Demote member of the faction  Params: player - player that performs operation 

```angelscript
uint dlg_DemoteMember(Critter& player, Critter@ npc, string@ playerName)
```

### r_DemoteMember

 Demotes actually selected member 

```angelscript
uint r_DemoteMember(Critter& player, Critter@ npc, int value)
```

### DemoteMember

 Helper 

```angelscript
bool DemoteMember(uint demoterId, uint demoteeId)
```

### dlg_ExpelMember

 Expels member from the faction  Params: player - player that performs operation 

```angelscript
uint dlg_ExpelMember(Critter& player, Critter@ npc, string@ playerName)
```

### r_ExpelMember

 Expels actually selected member 

```angelscript
uint r_ExpelMember(Critter& player, Critter@ npc, int value)
```

### _ExpelMember

 Helper 

```angelscript
bool _ExpelMember(uint expellerId, uint exileId)
```

### r_Resign

 Resign from membership in the faction 

```angelscript
void r_Resign(Critter& player, Critter@ npc, int value)
```

### dlg_ChooseBase

///////////// BASES MGMT ////////////  Chooses base basing on its name and remembers it's 

```angelscript
uint dlg_ChooseBase(Critter& player, Critter@ terminal, string@ baseName)
```

### dlg_ShowBase

 Displays the previously selected base 

```angelscript
void dlg_ShowBase(Critter& player, Critter@ npc, string@ say)
```

### r_SelectBase

 Selects base  value: -1: previous base 0: initial 1: next base 

```angelscript
uint r_SelectBase(Critter& player, Critter@ npc, int value)
```

### d_BaseRankAllowed

checks if the rank is allowed/not allowed to access currently selected base

```angelscript
bool d_BaseRankAllowed(Critter& player, Critter@, int rank, int allowed)
```

### r_BaseRankAllow

changes the state of allowance of given rank for currently selected base

```angelscript
void r_BaseRankAllow(Critter& player, Critter@, int rank, int allowed)
```

### d_BaseStatusAllowed

checks if the status is allowed/not allowed to access currently selected base

```angelscript
bool d_BaseStatusAllowed(Critter& player, Critter@, int status, int allowed)
```

### r_BaseStatusAllow

allows/disallows given status to access currently selected base

```angelscript
void r_BaseStatusAllow(Critter& player, Critter@, int status, int allowed)
```

### r_SelectFaction

* * Selects faction * * @param value: *   -1: previous *    0: initial *    1: next 

```angelscript
uint r_SelectFaction(Critter& player, Critter@ npc, int value)
```

### dlg_ShowKnownFaction

* * Fills the data for dialog node displaying known faction info 

```angelscript
void dlg_ShowKnownFaction(Critter& player, Critter@, string@ say)
```

### r_ChangeFactionStatus

* * Change status for ALL members of the currently selected faction 

```angelscript
void r_ChangeFactionStatus(Critter& player, Critter@, int status)
```

### dlg_AddKnownFaction

* * Adds faction with given name to the list of known factions 

```angelscript
uint dlg_AddKnownFaction(Critter& player, Critter@, string@ say)
```

### dlg_ShowInfo

 Shows useful info in the miscellaneous section (currently only about leadership) 

```angelscript
void dlg_ShowInfo(Critter& player, Critter@ npc, string@ text)
```

### d_CanClaimLeadership

 Checks if the player can claim leadership (he has to have highest reputation in the faction to do that), and no one else (including him, did that) and there should be leader existing 

```angelscript
bool d_CanClaimLeadership(Critter& player, Critter@ npc, int value)
```

### r_ClaimLeadership

 Sets player status as the one who claimed leadership 

```angelscript
void r_ClaimLeadership(Critter& player, Critter@ npc, int value)
```

### d_ClaimedLeadership

 Check if player is the one that claimed leadership 

```angelscript
bool d_ClaimedLeadership(Critter& player, Critter@ npc, int value)
```

### r_CancelClaim

 Cancels leadership claim 

```angelscript
void r_CancelClaim(Critter& player, Critter@ npc, int value)
```

### d_CanConfirmLeadership

 Checks if the player can confirm leadership (he has to be the one who claimed leadership and there should be no leader in faction) 

```angelscript
bool d_CanConfirmLeadership(Critter& player, Critter@ npc, int value)
```

### r_ConfirmLeadership

 Player becomes a leader after succesfull claim 

```angelscript
void r_ConfirmLeadership(Critter& player, Critter@ npc, int value)
```

### dlg_AddPlayer

 Adds player's records to database  Params: Critter@ player - player that is operating terminal 

```angelscript
uint dlg_AddPlayer(Critter& player, Critter@ terminal, string@ playerName)
```

### dlg_RemovePlayer

 Removes player from db  Params: playerName - name of the player to 

```angelscript
void dlg_RemovePlayer(Critter& player, Critter@ terminal, string@ playerName)
```

### dlg_RadioChannel

 Displays current faction' radio channel allows to modify it (if hi rank) 

```angelscript
void dlg_RadioChannel(Critter& player, Critter@ terminal, string@ say)
```

### d_Terminal_IsMember

 Checks whether player is member of the faction to which terminal belongs It is similar to d_IsMember, but this checks faction using map.GetData(MAP_DATA_FACTION) cause we can't get that data from terminal (Scenery object) 

```angelscript
bool d_Terminal_IsMember(Critter& player, Critter@ terminal, int val)
```

### d_Terminal_NotMember

```angelscript
bool d_Terminal_NotMember(Critter& player, Critter@ terminal, int val)
```

### d_IsInvited

 Checks whether player status in faction db is INVITED 

```angelscript
bool d_IsInvited(Critter& player, Critter@ terminal, int val)
```

### d_InvitationsAllowed

 If terminal belongs to (big) NPC faction, invitations aren't allowed 

```angelscript
bool d_InvitationsAllowed(Critter& player, Critter@ terminal, int val)
```

### dlg_ShowNews

 Display news info currently viewed news index is stored in player.Stat[ST_VAR0] (0 means last news) 

```angelscript
void dlg_ShowNews(Critter& player, Critter@ npc, string@ text)
```

### r_NextNews

 Jumps to the next news, and to the proper node to display it previously viewed news is stored in Var0 

```angelscript
uint r_NextNews(Critter& player, Critter@ npc, int val)
```

### r_PreviousNews

 Jumps to the previous news, and to the proper node to display it previously viewed news is stored in Var0 

```angelscript
uint r_PreviousNews(Critter& player, Critter@ npc, int val)
```

### r_GoToNews

 Initializes news index (player.Stat[ST_VAR0]) and go to the latest news (if any) 

```angelscript
uint r_GoToNews(Critter& player, Critter@ npc, int val)
```

### GoToNewsNode

```angelscript
uint GoToNewsNode(uint faction, uint index)
```

### r_UpdateLastUsed

* * Updates faction database to mark it as used now, to delay garbaging. 

```angelscript
void r_UpdateLastUsed(Critter& player, Critter@ npc)
```


