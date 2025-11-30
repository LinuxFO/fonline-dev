---
title: blackjack_manager.fos
description: "*< *  Manager class for Blackjack module. ..."
---

# blackjack_manager.fos

*<
*  Manager class for Blackjack module.


## Includes

- `blackjack.fos`

## Included By

- [blackjack_dialogues.fos](blackjack_dialogues.fos.md)

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __BLACKJACK_MANAGER__ |  |  |

## Classes

### CBlackjackManager

**Methods**

#### GetPlayerGame
```angelscript
CBlackjack@ GetPlayerGame(uint playerId)
```

#### CreateNewGame
```angelscript
CBlackjack@ CreateNewGame(uint playerId, uint dealerId, int numberOfDecksInShoe)
```

#### RemovePlayerGame
```angelscript
void RemovePlayerGame(uint playerId)
```

#### GetNumberOfGamesAvailable
```angelscript
int GetNumberOfGamesAvailable()
```


## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| blackjackManager | `[CBlackjackManager](blackjack_manager.fos.md)` | `CBlackjackManager()` | *< I moved this here, but need to find a place for it, where it will run only once. |

