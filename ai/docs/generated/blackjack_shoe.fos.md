---
title: blackjack_shoe.fos
description: "*< *  Shoe class for Blackjack. ..."
---

# blackjack_shoe.fos

*<
*  Shoe class for Blackjack.


## Includes

- `blackjack_h.fos`
- `blackjack_deck.fos`
- `_macros.fos`

## Included By

- [blackjack.fos](blackjack.fos.md)

## Classes

### CShoe

**Methods**

#### IsEmpty
```angelscript
bool IsEmpty()
```

#### GetCurrentCardIndex
```angelscript
uint GetCurrentCardIndex()
```

#### GetTotalCards
```angelscript
uint GetTotalCards()
```

#### GetNumberOfDecks
```angelscript
uint GetNumberOfDecks()
```

#### Init
```angelscript
void Init()
```

#### Shuffle
```angelscript
void Shuffle()
```

#### HinduShuffle
If you don't know how Hindu shuffle is done, check it on youtube.

```angelscript
void HinduShuffle()
```

#### SplitShuffle
Also known as Pharao shuffle, split in half, and mix them up.

```angelscript
void SplitShuffle()
```

#### Cut
If you don't know what a cut is, get off the Blackjack table.

```angelscript
void Cut()
```

#### List
Used for debugging only

```angelscript
void List()
```

#### TakeNextCard
Takes next card, returning it and incrementing the index.

```angelscript
CCard@ TakeNextCard()
```

#### InsertTestValuesForPlayerBlackjackAndDealerNotAce
Even money option shall not be offered.

```angelscript
void InsertTestValuesForPlayerBlackjackAndDealerNotAce()
```

#### InsertTestValuesForPlayerBlackjackAndDealerIs21
```angelscript
void InsertTestValuesForPlayerBlackjackAndDealerIs21()
```

#### InsertTestValuesForPlayerBlackjackAndDealerBlackjack
```angelscript
void InsertTestValuesForPlayerBlackjackAndDealerBlackjack()
```

#### InsertTestValuesForPlayerBlackjackAndDealerStandOn17
```angelscript
void InsertTestValuesForPlayerBlackjackAndDealerStandOn17()
```

#### InsertTestValuesForPlayerDoubleDown20AndDealerBlackjack
```angelscript
void InsertTestValuesForPlayerDoubleDown20AndDealerBlackjack()
```

#### InsertTestValuesForPlayerDoubleDown20AndDealer18
```angelscript
void InsertTestValuesForPlayerDoubleDown20AndDealer18()
```

#### InsertTestValuesForPlayerDoubleDown20AndDealer21
```angelscript
void InsertTestValuesForPlayerDoubleDown20AndDealer21()
```

#### InsertTestValuesForPlayerDoubleDownAfterThirdCard20AndDealer18
```angelscript
void InsertTestValuesForPlayerDoubleDownAfterThirdCard20AndDealer18()
```

#### InsertTestValuesForPlayerDoubleDownAndBustAndDealer18
```angelscript
void InsertTestValuesForPlayerDoubleDownAndBustAndDealer18()
```

#### InsertTestValuesForLuckyLadiesQohpAndDealerBlackjack
*< Test data for Lucky Ladies side bet.

```angelscript
void InsertTestValuesForLuckyLadiesQohpAndDealerBlackjack()
```

#### InsertTestValuesForLuckyLadiesQohpAndDealer20
```angelscript
void InsertTestValuesForLuckyLadiesQohpAndDealer20()
```

#### InsertTestValuesForLuckyLadiesMatch
```angelscript
void InsertTestValuesForLuckyLadiesMatch()
```

#### InsertTestValuesForLuckyLadiesSuited
```angelscript
void InsertTestValuesForLuckyLadiesSuited()
```

#### InsertTestValuesForLuckyLadiesUnSuited
```angelscript
void InsertTestValuesForLuckyLadiesUnSuited()
```

#### InsertTestValuesForPerfectPairPlayerPerfectPair
*< Test data for Perfect Pair side bet.

```angelscript
void InsertTestValuesForPerfectPairPlayerPerfectPair()
```

#### InsertTestValuesForPerfectPairPlayerColoredPair
```angelscript
void InsertTestValuesForPerfectPairPlayerColoredPair()
```

#### InsertTestValuesForPerfectPairPlayerMixedPair
```angelscript
void InsertTestValuesForPerfectPairPlayerMixedPair()
```

#### InsertTestValuesForRoyalMatchPlayerRoyalMatch
*< Test data for Royal Match side bet.

```angelscript
void InsertTestValuesForRoyalMatchPlayerRoyalMatch()
```

#### InsertTestValuesForRoyalMatchPlayerSuited
```angelscript
void InsertTestValuesForRoyalMatchPlayerSuited()
```


