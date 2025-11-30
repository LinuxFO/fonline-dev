---
title: economy.fos
description: " FOnline: 2238 Rotators  economy.fos ..."
---

# economy.fos


FOnline: 2238
Rotators

economy.fos


## Includes

- `_macros.fos`
- `_math.fos`
- `_vars.fos`
- `entire.fos`
- `serializator.fos`
- `utils_h.fos`
- `economy_h.fos`
- `economy_bank.fos`
- `prices_server_client.fos`

## Included By

- [guard.fos](guard.fos.md)

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __ECONOMY__ |  |  |
| PROCESS_AMOUNT | `(250)` |  |

## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| f | `file` |  |  |
| itempids | `array<int>` |  |  |
| banks | `array<[Bank](economy_bank.fos.md)>` |  |  |
| PIDs | `array<uint16>` |  | list of pids to log |

## Functions

### InitEconomy

* * Initialize the economy. The only call you'll really need to run, as it'll call other initializers. 

```angelscript
void InitEconomy()
```

### GetItemPrice

Only used when calculating buying (from trader POV) price.

```angelscript
uint GetItemPrice(uint pid)
```

### GetBaseModifier

```angelscript
int GetBaseModifier(Critter& player, Critter& trader, bool buy)
```

### GetItemSellModifier

Calculate modifier which modifies how much the trader will buy the item for

```angelscript
int GetItemSellModifier(Critter& player, Critter& trader)
```

### GetItemBuyModifier

Calculate modifier which modifies how much trader will sell the item for

```angelscript
int GetItemBuyModifier(Critter& player, Critter& trader)
```

### BanksAddMoney

* * Add money divided among all banks * * @param amount How much money to add to reserves, the money will be splittled evenly among the banks * 

```angelscript
void BanksAddMoney(uint amount)
```

### BanksRemoveMoney

* * Remove money divided among all banks * * @param amount How much money to remove from reserves, the money will be taken as evenly as possible among the banks * 

```angelscript
void BanksRemoveMoney(uint amount)
```

### BanksGetTotalMoney

* * Get total money stored in all banks combined. * * @return Total money stored in all banks combined. * 

```angelscript
uint BanksGetTotalMoney()
```

### BanksTransferToCritter

```angelscript
bool BanksTransferToCritter(Critter& critter, uint amount, uint type, bool virtual)
```

### GetTransferReason

```angelscript
string GetTransferReason(uint type)
```

### BanksTransferFromCritter

```angelscript
bool BanksTransferFromCritter(Critter& critter, uint amount, uint type, bool virtual)
```

### BankAddMoney

* @return    Returns operation status 

```angelscript
bool BankAddMoney(uint bankid, uint amount)
```

### BankRemoveMoney

* @return    Returns operation status 

```angelscript
bool BankRemoveMoney(uint bankid, uint amount)
```

### BankSetMoney

* @return    Returns operation status 

```angelscript
bool BankSetMoney(uint bankid, uint amount)
```

### BankTransferFromCritter

```angelscript
bool BankTransferFromCritter(uint bankId, Critter& critter, uint amount, uint type, bool virtual)
```

### BankAccountRemoveMoney

* @return    Returns operation status 

```angelscript
bool BankAccountRemoveMoney(uint bankid, uint account, uint amount)
```

### BankCreateAccount

* @return Bank error code FD_BANK_RESULT_* defined in _economy.fos 

```angelscript
uint BankCreateAccount(uint bankid, uint playerid)
```

### BankDepositMoney

* @return Bank error code FD_BANK_RESULT_* defined in _economy.fos 

```angelscript
uint BankDepositMoney(uint bankid, uint playerid, uint account, int amount)
```

### BankWithdrawMoney

* @return Bank error code FD_BANK_RESULT_* defined in _economy.fos 

```angelscript
uint BankWithdrawMoney(uint bankid, uint playerid, uint account, int amount)
```

### BankTransferMoney

* @return Bank error code FD_BANK_RESULT_* defined in _economy.fos 

```angelscript
uint BankTransferMoney(uint bankid, uint fromaccount, uint toaccount, uint amount)
```

### BankGetAccountOwner

* @return Returns critter.Id of the owner of the specified account 

```angelscript
uint BankGetAccountOwner(uint bankid, uint account)
```

### BankGetAccountBalance

* @return Returns account balance 

```angelscript
int BankGetAccountBalance(uint bankid, uint account)
```

### BankGetAccountID

* @return Returns Account ID if found, -1 if none is found 

```angelscript
int BankGetAccountID(uint bankid, uint playerid)
```

### BankAccountExists

* @return Returns true if the account exists 

```angelscript
bool BankAccountExists(uint bankid, uint account)
```

### BankHasAccess

* @return Returns true if the specified player has access to the account 

```angelscript
bool BankHasAccess(uint bankid, uint account, uint playerid)
```

### BankGetAccessCount

* @return Returns the amount of additional players that have access to the bank, can at minimum be 0 (only owner has access) 

```angelscript
uint BankGetAccessCount(uint bankid, uint account)
```

### BankGetAccountType

* @return Returns a value defined by the ACCOUNT_TYPE_* define in _economy.fos 

```angelscript
uint BankGetAccountType(uint bankid, uint account)
```

### BankSetAccountType

* @return Bank error code FD_BANK_RESULT_* defined in _economy.fos 

```angelscript
uint BankSetAccountType(uint bankid, uint account, uint accounttype)
```

### BankSetCreditRating

* @return Bank error code FD_BANK_RESULT_* defined in _economy.fos 

```angelscript
uint BankSetCreditRating(uint bankid, uint account, uint rating)
```

### BankGetCreditRating

* @return a value matching any of the CREDITVALUE_* defines in _economy.fos 

```angelscript
uint BankGetCreditRating(uint bankid, uint account)
```

### BankSetLoan

* @return Bank error code FD_BANK_RESULT_* defined in _economy.fos 

```angelscript
uint BankSetLoan(uint bankid, uint account, uint loan)
```

### BankGetLoan

* @return The amount of loaned money 

```angelscript
uint BankGetLoan(uint bankid, uint account)
```

### BankAddAccess

* @return Bank error code FD_BANK_RESULT_* defined in _economy.fos 

```angelscript
uint BankAddAccess(uint bankid, uint account, uint playerid)
```

### BankRemoveAccess

* @return Bank error code FD_BANK_RESULT_* defined in _economy.fos 

```angelscript
uint BankRemoveAccess(uint bankid, uint account, uint playerid)
```

### BankGetLoanInterest

* @return Loan interest in percent 

```angelscript
uint BankGetLoanInterest(uint bankid)
```

### BankSetLoanInterest

* @return Bank error code FD_BANK_RESULT_* defined in _economy.fos 

```angelscript
uint BankSetLoanInterest(uint bankid, uint interest)
```

### BankGetSaveInterest

* @return Save interest in percent 

```angelscript
float BankGetSaveInterest(uint bankid)
```

### BankSetSaveInterest

* @return Bank error code FD_BANK_RESULT_* defined in _economy.fos 

```angelscript
uint BankSetSaveInterest(uint bankid, float interest)
```

### BankGetTotalMoney

* * Get total amount of money in the bank * * @param     bankid     Bank ID, see _economy.fos * * @return Total amount of money in the bank 

```angelscript
uint BankGetTotalMoney(uint bankid)
```

### BankGetTotalBalance

* @return Returns accounts balance 

```angelscript
uint BankGetTotalBalance(uint bankid)
```

### BankGetReserveRatio

* @return Returns reserve ratio 

```angelscript
float BankGetReserveRatio(uint bankid)
```

### BankTakeLoan

* @return Bank error code FD_BANK_RESULT_* defined in _economy.fos 

```angelscript
uint BankTakeLoan(uint bankid, uint account, uint amount)
```

### BankGetNumberOfAccounts

* @return Total number of accounts in the bank 

```angelscript
uint BankGetNumberOfAccounts(uint bankid)
```

### InitBanks

* * Initialize Bank objects 

```angelscript
bool InitBanks()
```

### InitPrices

Set base prices, first time

```angelscript
void InitPrices()
```

### UpdatePrices

Only used when calculating buying (from trader POV) price. WIP, need to check crafted items per cycle instead of items available on traders.

```angelscript
void UpdatePrices()
```

### e_UpdateInterestAccounts

```angelscript
uint e_UpdateInterestAccounts(array<uint>@ values)
```

### e_UpdateInterest

* * Update interest see _economy.fos for the value of INTEREST_UPDATE_INTERVAL 

```angelscript
uint e_UpdateInterest(array<uint>@ values)
```

### e_UpdateEconomy

```angelscript
uint e_UpdateEconomy(array<uint>@ values)
```

### GetTraderLevel

```angelscript
uint GetTraderLevel(Critter@ npc, uint type)
```

### GetTraderLevels

```angelscript
array<int> GetTraderLevels(Critter@ npc)
```

### SetTraderLevel

```angelscript
void SetTraderLevel(Critter@ npc, uint type, uint level)
```

### SetTraderLevels

```angelscript
void SetTraderLevels(Critter@ npc, array<uint>& levels)
```

### GetTraderLevels

```angelscript
void GetTraderLevels(Critter@ npc, array<uint>& levels)
```

### TraderCapacity

```angelscript
uint TraderCapacity(Critter@ npc, uint type, uint itemlevel)
```

### TraderCapacity

```angelscript
uint TraderCapacity(Critter@ npc)
```

### TraderMoneyCapacity

```angelscript
uint TraderMoneyCapacity(Critter@ npc)
```

### SaveBankData

```angelscript
void SaveBankData()
```

### e_LogEconomy

* * Items/virtualmoney log. 

```angelscript
uint e_LogEconomy(array<uint>@ values)
```


