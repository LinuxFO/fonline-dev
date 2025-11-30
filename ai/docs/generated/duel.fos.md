---
title: duel.fos
description: " FOnline: 2238 Rotators  duel.fos ..."
---

# duel.fos


FOnline: 2238
Rotators

duel.fos


## Includes

- `_entires.fos`
- `_macros.fos`
- `entire.fos`
- `messages_h.fos`
- `utils_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| DUEL_IN_PROGRESS | `(npc.StatBase[ST_VAR1])` |  |
| DUEL_BET_AMOUNT | `(npc.StatBase[ST_VAR2])` |  |
| DUEL_PLAYER_1 | `(npc.StatBase[ST_VAR3])` |  |
| DUEL_PLAYER_2 | `(npc.StatBase[ST_VAR4])` |  |
| DUEL_COUNT_DOWN | `(npc.StatBase[ST_VAR5])` |  |
| DUEL_WINNER | `(npc.StatBase[ST_VAR6])` |  |
| DUEL_TYPE | `(npc.StatBase[ST_VAR7])` |  |
| DUEL_TIMEOUT_EID | `(npc.StatBase[ST_VAR8])` |  |
| DUEL_BET_MIN | `(0)` |  |
| DUEL_BET_MAX | `(10000)` |  |
| WIN_REASON_WALKOVER | `(1)` |  |
| WIN_REASON_ATTACK | `(2)` |  |
| WIN_REASON_NORMAL | `(3)` |  |
| DUEL_TYPE_UNARMED | `(1)` |  |
| DUEL_TYPE_FULL | `(2)` |  |
| DUEL_TYPE_BOXING | `(3)` |  |
| DUEL_BEGIN_TIMEOUT | `(REAL_SECOND(20))` |  |
| DUEL_END_TIMEOUT | `(REAL_SECOND(5))` |  |
| DUEL_TIME_TIMEOUT | `(REAL_MINUTE(3))` |  |

## Functions

### critter_init

```angelscript
void critter_init(Critter& npc, bool firstTime)
```

### _OnSomeoneAttacking

```angelscript
void _OnSomeoneAttacking(Critter& npc, Critter& fromCr, Critter& target)
```

### _OnMessage

```angelscript
void _OnMessage(Critter& npc, Critter& sender, int num, int val)
```

### e_Count

```angelscript
uint e_Count(array<uint>@ values)
```

### e_EndTimeout

```angelscript
uint e_EndTimeout(array<uint>@ values)
```

### e_BeginTimeout

```angelscript
uint e_BeginTimeout(array<uint>@ values)
```

### e_MatchTimeout

```angelscript
uint e_MatchTimeout(array<uint>@ values)
```

### r_SetMatchType

```angelscript
void r_SetMatchType(Critter& player, Critter@ npc, int val)
```

### d_ValidConditions

Check if storage container exists etc.

```angelscript
bool d_ValidConditions(Critter& player, Critter@ npc, int val)
```

### r_SignUp

```angelscript
void r_SignUp(Critter& player, Critter@ npc, int val)
```

### dlg_ShowBet

```angelscript
void dlg_ShowBet(Critter& player, Critter@ npc, string@ text)
```

### dlg_SetBet

```angelscript
void dlg_SetBet(Critter& player, Critter@ npc, string@ say)
```

### d_CanSignUp

```angelscript
bool d_CanSignUp(Critter& player, Critter@ npc, int val)
```

### r_ClearVars

```angelscript
void r_ClearVars(Critter& player, Critter@ npc, int val)
```

### d_CanClearVars

```angelscript
bool d_CanClearVars(Critter& player, Critter@ npc, int val)
```

### d_IsOpen

Only applies to junktown.

```angelscript
bool d_IsOpen(Critter& player, Critter@ npc, int val)
```

### d_IsNotOpen

Only applies to junktown.

```angelscript
bool d_IsNotOpen(Critter& player, Critter@ npc, int val)
```

### d_CanSetBet

```angelscript
bool d_CanSetBet(Critter& player, Critter@ npc, int val)
```

### d_CanAffordBet

```angelscript
bool d_CanAffordBet(Critter& player, Critter@ npc, int val)
```

### DeclareWinner

```angelscript
void DeclareWinner(Critter& winner, Critter& npc, uint reason)
```

### ResetVars

```angelscript
void ResetVars(Critter& npc)
```

### MatchStart

```angelscript
bool MatchStart(Critter& npc)
```

### TransferItemsToPlayer

```angelscript
bool TransferItemsToPlayer(Critter& cr)
```

### TransferItemsFromPlayer

```angelscript
bool TransferItemsFromPlayer(Critter& cr)
```

### GetItemContainer

```angelscript
Item@ GetItemContainer(Map@ map)
```

### TransferBack

```angelscript
void TransferBack(Critter& critter, uint entire)
```

### MatchOver

```angelscript
bool MatchOver(Critter& npc)
```


