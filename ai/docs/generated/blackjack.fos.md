---
title: blackjack.fos
description: "*< *  Main logic for the Blackjack module. ..."
---

# blackjack.fos

*<
*  Main logic for the Blackjack module.


## Includes

- `blackjack_h.fos`
- `blackjack_shoe.fos`
- `ITEMPID.H`
- `_math.fos`

## Included By

- [blackjack_manager.fos](blackjack_manager.fos.md)

## Classes

### CBlackjack

**Methods**

#### GetPlayerId
*< Getters

```angelscript
uint GetPlayerId()
```

#### GetDealerId
```angelscript
uint GetDealerId()
```

#### GetLastAction
```angelscript
string GetLastAction()
```

#### GetPlayerHand
```angelscript
string GetPlayerHand()
```

#### GetDealerHand
```angelscript
string GetDealerHand()
```

#### GetResult
```angelscript
string GetResult()
```

#### Init
*< Initialize variables for a clean session, generate a new shoe and shuffle it.

```angelscript
void Init()
```

#### SetGamblingSkills
```angelscript
void SetGamblingSkills()
```

#### IsSeeShoeSize
```angelscript
bool IsSeeShoeSize()
```

#### ResetVariables
```angelscript
void ResetVariables()
```

#### IsSeeDealerCards
*< Gambling skill related stuff.

```angelscript
bool IsSeeDealerCards()
```

#### IsShuffleNeeded
```angelscript
bool IsShuffleNeeded()
```

#### IsSeeReshuffling
```angelscript
bool IsSeeReshuffling()
```

#### IsSidebetAvailable
*< *  Side bet related. 

```angelscript
bool IsSidebetAvailable()
```

#### SetSidebetType
```angelscript
void SetSidebetType(int type)
```

#### GetSidebetType
```angelscript
string GetSidebetType()
```

#### SetSidebetValue
```angelscript
void SetSidebetValue(int value)
```

#### ProgressToSidebetDone
```angelscript
void ProgressToSidebetDone()
```

#### GetSidebetResult
```angelscript
string GetSidebetResult()
```

#### SetBetValue
*< *  Bet related. 

```angelscript
void SetBetValue(int value)
```

#### IsHitAvailable
*< *  Hit related. 

```angelscript
bool IsHitAvailable()
```

#### Hit
```angelscript
void Hit()
```

#### IsStandAvailable
*< *  Stand related. 

```angelscript
bool IsStandAvailable()
```

#### Stand
```angelscript
void Stand()
```

#### IsEvenMoneyAvailable
```angelscript
bool IsEvenMoneyAvailable()
```

#### IsDealerFirstCardAce
```angelscript
bool IsDealerFirstCardAce()
```

#### EvenMoney
```angelscript
void EvenMoney()
```

#### IsDoubleDownAvailable
*< *  Double down related. *  Double down is available anytime as long as the player is not busted or does not have 21 already. *  The player will receive exactly one card after doubling the bet and finishes his turn. 

```angelscript
bool IsDoubleDownAvailable()
```

#### DoubleDown
```angelscript
void DoubleDown()
```

#### IsPlayerHaveMoney
```angelscript
bool IsPlayerHaveMoney(uint value)
```

#### IsSurrenderAvailable
*< Surrender related, available only at starting hand. (Early surrender, bc easier to implement and easier for player also.)

```angelscript
bool IsSurrenderAvailable()
```

#### Surrender
```angelscript
void Surrender()
```

#### IsInsuranceAvailable
*< Insurance related - Only available when Dealer has an Ace revealed and only wins if host has a Blackjack.

```angelscript
bool IsInsuranceAvailable()
```

#### Insurance
```angelscript
void Insurance()
```

#### dealFirst
*< *  Game mechanic 

```angelscript
void dealFirst()
```

#### giveCardToPlayer
```angelscript
void giveCardToPlayer()
```

#### showDealersHoleCard
```angelscript
void showDealersHoleCard()
```

#### GetDealersHoleCard
```angelscript
CCard@ GetDealersHoleCard()
```

#### GetHandSoftValue
```angelscript
int GetHandSoftValue(array<CCard@> hand)
```

#### GetDealerHandHardValue
*< Needed for the "Hit hard 17" rule, but only for the dealer.

```angelscript
int GetDealerHandHardValue()
```

#### IsPlayerBust
```angelscript
bool IsPlayerBust()
```

#### IsPlayerBlackjack
```angelscript
bool IsPlayerBlackjack()
```

#### DidPlayerReachBlackjackValue
```angelscript
bool DidPlayerReachBlackjackValue()
```

#### ProcessSidebet
*< Side bet result check

```angelscript
void ProcessSidebet()
```

#### ProcessSidebetLuckyLadies
```angelscript
void ProcessSidebetLuckyLadies()
```

#### ProcessSidebetPerfectPair
```angelscript
void ProcessSidebetPerfectPair()
```

#### ProcessSidebetRoyalMatch
```angelscript
void ProcessSidebetRoyalMatch()
```

#### ProcessSidebetNone
```angelscript
void ProcessSidebetNone()
```

#### IsPlayerHaveTwenty
```angelscript
bool IsPlayerHaveTwenty()
```

#### IsPlayerHaveQueenOfHearts
```angelscript
bool IsPlayerHaveQueenOfHearts()
```

#### IsPlayerHaveSuit
```angelscript
bool IsPlayerHaveSuit()
```

#### IsPlayerHavePair
```angelscript
bool IsPlayerHavePair()
```

#### IsPlayerHaveColor
```angelscript
bool IsPlayerHaveColor()
```

#### IsPlayerHaveRoyalPair
```angelscript
bool IsPlayerHaveRoyalPair()
```

#### ProgressToFirst
*< *  Progress calls - Most of these are in separate function for readability. 

```angelscript
void ProgressToFirst()
```

#### ProgressToPlayerBust
```angelscript
void ProgressToPlayerBust()
```

#### ProgressToResult
```angelscript
void ProgressToResult()
```

#### ProgressToPlayerBlackjack
```angelscript
void ProgressToPlayerBlackjack()
```

#### ProgressToRest
```angelscript
void ProgressToRest()
```

#### ProgressToDealersTurn
```angelscript
void ProgressToDealersTurn()
```

#### IsDealerDone
```angelscript
bool IsDealerDone()
```

#### canDealerStand
```angelscript
bool canDealerStand()
```

#### isDealerBust
```angelscript
bool isDealerBust()
```

#### IsDealerBlackjack
```angelscript
bool IsDealerBlackjack()
```

#### DealerTakesCard
```angelscript
void DealerTakesCard()
```

#### DealerFinishedTurn
```angelscript
void DealerFinishedTurn()
```

#### GivePlayerMoney
```angelscript
void GivePlayerMoney(int amount)
```

#### TakePlayerMoney
```angelscript
void TakePlayerMoney(int amount)
```

#### InsertTestCasesForPlayerBlackjack
*< *  Test cases - Function names speak for themselves, they should cover all possibilities, use the correct one for your tests. 

```angelscript
void InsertTestCasesForPlayerBlackjack()
```

#### InsertTestCasesForDoubleDown
```angelscript
void InsertTestCasesForDoubleDown()
```

#### InsertTestCasesForLuckyLadies
```angelscript
void InsertTestCasesForLuckyLadies()
```

#### InsertTestCasesForPerfectPair
```angelscript
void InsertTestCasesForPerfectPair()
```

#### InsertTestCasesForRoyalMatch
```angelscript
void InsertTestCasesForRoyalMatch()
```


