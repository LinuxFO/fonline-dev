---
title: economy_bank.fos
description: " FOnline: 2238 Rotators  economy_bank.fos ..."
---

# economy_bank.fos


FOnline: 2238
Rotators

economy_bank.fos


## Includes

- `_macros.fos`
- `economy_h.fos`
- `utils_h.fos`
- `serializator.fos`
- `economy_bankaccount.fos`

## Included By

- [economy.fos](economy.fos.md)

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| BANK_ACCOUNT_MAX | `(100000)` |  |

## Classes

### Bank

Class for handling a single bank

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| owner | `uint` |  |  |
| totalmoney | `uint` |  |  |
| numaccounts | `uint` |  |  |
| loaninterest | `uint` |  |  |
| savingsinterest | `float` |  |  |
| initialized | `bool` |  |  |
| name | `string` |  |  |
| bankaccounts | `array<[BankAccount](economy_bankaccount.fos.md)>` |  |  |
| serializer | `[Serializator](serializator.fos.md)` |  |  |

**Methods**

#### InitAccounts
```angelscript
bool InitAccounts()
```

#### LoadData
Load data from database and set the variables

```angelscript
bool LoadData()
```

#### SaveData
Save data to the database

```angelscript
bool SaveData()
```

#### Init
```angelscript
bool Init(string name)
```

#### AddMoney
Add a sum of money to the bank, this money is not stored in any account

```angelscript
bool AddMoney(int amount)
```

#### RemoveMoney
Remove money from the bank

```angelscript
bool RemoveMoney(int amount)
```

#### SetMoney
Set the sum of money in the bank

```angelscript
bool SetMoney(uint amount)
```

#### AccountRemoveMoney
Remove money from specified account

```angelscript
bool AccountRemoveMoney(uint accountid, int amount)
```

#### GetAccountID
Get accountid of specified player. If he doesn't have an account in this bank, the function returns -1

```angelscript
int GetAccountID(uint playerid)
```

#### GetAccountBalance
Get account balance of specified account

```angelscript
int GetAccountBalance(uint account)
```

#### GetOwner
Get owner of specified accounti

```angelscript
uint GetOwner(uint account)
```

#### AccountExists
Check if the with the specified id exists.

```angelscript
bool AccountExists(uint account)
```

#### GetLoanInterest
```angelscript
uint GetLoanInterest()
```

#### SetLoanInterest
```angelscript
uint SetLoanInterest(uint interest)
```

#### GetSaveInterest
```angelscript
float GetSaveInterest()
```

#### SetSaveInterest
```angelscript
uint SetSaveInterest(float interest)
```

#### CreateBankAccount
```angelscript
uint CreateBankAccount(int playerid)
```

#### DepositMoney
```angelscript
uint DepositMoney(int playerid, uint account, int amount)
```

#### WithdrawMoney
```angelscript
uint WithdrawMoney(int playerid, uint account, int amount)
```

#### TransferMoney
```angelscript
uint TransferMoney(uint accountfrom, uint accountto, uint amount)
```

#### TakeLoan
```angelscript
uint TakeLoan(uint account, uint amount)
```

#### GetNumberOfAccounts
```angelscript
uint GetNumberOfAccounts()
```

#### GetTotalMoney
```angelscript
uint GetTotalMoney()
```

#### GetTotalBalance
Get total balance of all accounts

```angelscript
uint GetTotalBalance()
```

#### GetReserveRatio
```angelscript
float GetReserveRatio()
```

#### SetCreditRating
```angelscript
uint SetCreditRating(uint accountid, uint rating)
```

#### GetCreditRating
```angelscript
uint GetCreditRating(uint accountid)
```

#### SetLoan
```angelscript
uint SetLoan(uint accountid, uint loan)
```

#### GetLoan
```angelscript
uint GetLoan(uint accountid)
```

#### GetAccountType
```angelscript
uint GetAccountType(uint accountid)
```

#### SetAccountType
```angelscript
uint SetAccountType(uint accountid, uint accounttype)
```

#### AddAccess
```angelscript
uint AddAccess(uint accountid, uint playerid)
```

#### RemoveAccess
```angelscript
uint RemoveAccess(uint accountid, uint playerid)
```

#### HasAccess
```angelscript
bool HasAccess(uint accountid, uint playerid)
```

#### GetAccessCount
```angelscript
uint GetAccessCount(uint accountid)
```

#### UpdateInterestAccounts
```angelscript
bool UpdateInterestAccounts(uint startIndex, uint amount)
```

#### UpdateInterest
```angelscript
void UpdateInterest()
```


