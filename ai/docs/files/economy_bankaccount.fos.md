---
title: economy_bankaccount.fos
description: " FOnline: 2238 Rotators  economy_bankaccount.fos ..."
---

# economy_bankaccount.fos


FOnline: 2238
Rotators

economy_bankaccount.fos


## Includes

- `_macros.fos`
- `economy_h.fos`
- `serializator.fos`
- `utils_h.fos`

## Included By

- [economy_bank.fos](economy_bank.fos.md)

## Classes

### BankAccount

Class for handling personal bank data (money deposited, credit rating, debt etc)

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| ownerId | `uint` |  |  |
| balance | `int` |  |  |
| loan | `uint` |  |  |
| type | `uint` |  |  |
| rating | `uint` |  |  |
| name | `string` |  |  |
| accesslist | `array<uint>` |  |  |
| accesscount | `uint` |  |  |
| serializer | `[Serializator](serializator.fos.md)` |  |  |

**Methods**

#### LoadData
```angelscript
bool LoadData()
```

#### SaveData
```angelscript
bool SaveData()
```

#### Init
```angelscript
bool Init(string name)
```

#### AddLoan
```angelscript
bool AddLoan(uint amount)
```

#### AddMoney
```angelscript
bool AddMoney(uint amount)
```

#### RemoveMoney
```angelscript
bool RemoveMoney(uint amount)
```

#### SetOwner
```angelscript
bool SetOwner(uint ownerId)
```

#### AddAccess
```angelscript
uint AddAccess(uint playerid)
```

#### RemoveAccess
```angelscript
uint RemoveAccess(uint playerid)
```

#### HasAccess
```angelscript
bool HasAccess(uint playerid)
```

#### GetAccessCount
How many people that have access to the account

```angelscript
uint GetAccessCount()
```

#### GetOwner
```angelscript
uint GetOwner()
```

#### GetBalance
```angelscript
int GetBalance()
```

#### SetCreditRating
```angelscript
uint SetCreditRating(uint rating)
```

#### GetCreditRating
```angelscript
uint GetCreditRating()
```

#### SetLoan
```angelscript
uint SetLoan(uint loan)
```

#### GetLoan
```angelscript
uint GetLoan()
```

#### GetAccountType
```angelscript
uint GetAccountType()
```

#### SetAccountType
```angelscript
uint SetAccountType(uint type)
```

#### WithdrawMoney
```angelscript
uint WithdrawMoney(int amount, uint playerid)
```

#### DepositMoney
```angelscript
uint DepositMoney(int amount, uint playerid)
```


