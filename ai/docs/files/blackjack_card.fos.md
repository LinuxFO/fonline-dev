---
title: blackjack_card.fos
description: "*< *  Card class for Blackjack. ..."
---

# blackjack_card.fos

*<
*  Card class for Blackjack.


## Included By

- [blackjack_deck.fos](blackjack_deck.fos.md)

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| CARD_SUIT_NONE | `(0)` |  |
| CARD_SUIT_SPADES | `(1)` |  |
| CARD_SUIT_HEARTS | `(2)` |  |
| CARD_SUIT_DIAMONDS | `(3)` |  |
| CARD_SUIT_CLUBS | `(4)` |  |
| CARD_TYPE_NONE | `(0)` |  |
| CARD_TYPE_ACE | `(1)` |  |
| CARD_TYPE_TWO | `(2)` |  |
| CARD_TYPE_THREE | `(3)` |  |
| CARD_TYPE_FOUR | `(4)` |  |
| CARD_TYPE_FIVE | `(5)` |  |
| CARD_TYPE_SIX | `(6)` |  |
| CARD_TYPE_SEVEN | `(7)` |  |
| CARD_TYPE_EIGHT | `(8)` |  |
| CARD_TYPE_NINE | `(9)` |  |
| CARD_TYPE_TEN | `(10)` |  |
| CARD_TYPE_JACK | `(11)` |  |
| CARD_TYPE_QUEEN | `(12)` |  |
| CARD_TYPE_KING | `(13)` |  |
| CARD_COLOR_NONE | `(0)` |  |
| CARD_COLOR_RED | `(1)` |  |
| CARD_COLOR_BLACK | `(2)` |  |

## Classes

### CCard

**Methods**

#### Type
```angelscript
uint8 Type()    {   return type;    }
```

#### Suit
```angelscript
uint8 Suit()    {   return suit;    }
```

#### Color
```angelscript
uint8 Color()
```

#### Value
```angelscript
uint8 Value()
```

#### GetCardNotation
```angelscript
string GetCardNotation()
```


