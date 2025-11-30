---
title: economy_banker.fos
description: " FOnline: 2238 Rotators  economy_banker.fos ..."
---

# economy_banker.fos


FOnline: 2238
Rotators

economy_banker.fos


## Includes

- `_macros.fos`
- `economy_h.fos`
- `mapdata_h.fos`
- `utils_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| FORCE_DIALOG_REGISTRATION_SUCCESS | `(6)` |  |
| FORCE_DIALOG_ALREADY_HAS_ACCOUNT | `(7)` |  |
| FORCE_DIALOG_VALID_ACCOUNT | `(9)` |  |
| FORCE_DIALOG_BUSY | `(8)` |  |
| FORCE_DIALOG_NO_ACCOUNT | `(10)` |  |
| FORCE_DIALOG_TOO_MANY_ACCOUNTS | `(15)` |  |
| FORCE_DIALOG_ERROR | `(16)` |  |
| FORCE_DIALOG_INVALID_ACCOUNT | `(17)` |  |
| FORCE_DIALOG_NOT_AUTHORIZED | `(18)` |  |
| FORCE_DIALOG_TRANSFER_SUM | `(21)` |  |
| FORCE_DIALOG_BANK_NOT_FOUND | `(23)` |  |
| FORCE_DIALOG_JOINT_ACCOUNT_NO_MONEY | `(26)` |  |
| FORCE_DIALOG_JOINT_ACCOUNT_ERROR | `(27)` |  |
| FORCE_DIALOG_JOINT_ACCOUNT_SUCCESS | `(25)` |  |
| FORCE_DIALOG_LOAN_ERROR | `(33)` |  |
| FORCE_DIALOG_LOAN_NO_MONEY | `(35)` |  |
| FORCE_DIALOG_LOAN_SUCCESS | `(36)` |  |
| SESSION_ACCOUNT | `(player.StatBase[ST_VAR0])` | "Session" variables that should last only while the dialog takes place, it is resetted when dialog is initialized. |
| SESSION_TRANSFER_ACCOUNT | `(player.StatBase[ST_VAR1])` |  |
| SESSION_BANK | `(player.StatBase[ST_VAR2])` |  |

## Functions

### GetStrCreditRating

```angelscript
string GetStrCreditRating(uint rating)
```

### GetStrAccountType

```angelscript
string GetStrAccountType(uint accounttype)
```

### JumpDialog

```angelscript
uint JumpDialog(uint result)
```

### r_CreateAccount

Dialog functions

```angelscript
uint r_CreateAccount(Critter& player, Critter@ npc, int value)
```

### r_IsFree

```angelscript
uint r_IsFree(Critter& player, Critter@ npc, int value)
```

### d_LoaningEnabled

Check if loaning is enabled in options

```angelscript
bool d_LoaningEnabled(Critter& player, Critter@ npc, int val)
```

### d_IsOwnerOfAccount

```angelscript
bool d_IsOwnerOfAccount(Critter& player, Critter@ npc, int val)
```

### d_HasAccount

```angelscript
bool d_HasAccount(Critter& player, Critter@ npc, int val)
```

### d_HasJointAccount

```angelscript
bool d_HasJointAccount(Critter& player, Critter@ npc, int val)
```

### d_HasNormalAccount

```angelscript
bool d_HasNormalAccount(Critter& player, Critter@ npc, int val)
```

### r_TakeLoan

```angelscript
uint r_TakeLoan(Critter& player, Critter@ npc, int val)
```

### dlg_ShowInterest

```angelscript
void dlg_ShowInterest(Critter& player, Critter@ npc, string@ text)
```

### dlg_ShowLoans

```angelscript
void dlg_ShowLoans(Critter& player, Critter@ npc, string@ text)
```

### dlg_ShowAccountStatus

```angelscript
void dlg_ShowAccountStatus(Critter& player, Critter@ npc, string@ text)
```

### dlg_WithdrawMoney

```angelscript
void dlg_WithdrawMoney(Critter& player, Critter@ npc, string@ say)
```

### dlg_DepositMoney

```angelscript
uint dlg_DepositMoney(Critter& player, Critter@ npc, string@ say)
```

### dlg_TransferMoney

```angelscript
void dlg_TransferMoney(Critter& player, Critter@ npc, string@ say)
```

### dlg_EnterTransferNumber

```angelscript
uint dlg_EnterTransferNumber(Critter& player, Critter@ npc, string@ say)
```

### dlg_GiveAccess

```angelscript
void dlg_GiveAccess(Critter& player, Critter@ npc, string@ say)
```

### dlg_RevokeAccess

```angelscript
void dlg_RevokeAccess(Critter& player, Critter@ npc, string@ say)
```

### dlg_EnterAccountNumber

```angelscript
uint dlg_EnterAccountNumber(Critter& player, Critter@ npc, string@ say)
```

### r_CreateJointAccount

```angelscript
uint r_CreateJointAccount(Critter& player, Critter@ npc, int value)
```

### r_FindPlayerAccount

```angelscript
uint r_FindPlayerAccount(Critter& player, Critter@ npc, int value)
```


