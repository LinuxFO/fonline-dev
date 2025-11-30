---
title: blackjack_h.fos
description: "*< *  Blackjack - Card game for FOnline. *  What would be the most reasonable way that gambling skill would affect the course of the game? *  (It shal..."
---

# blackjack_h.fos

*<
*  Blackjack - Card game for FOnline.
*  What would be the most reasonable way that gambling skill would affect the course of the game?
*  (It shall be true to gambling in rl, shall be fun, and shall not be exploitable or afk farmed easily (or at all?).)
*
*  Specification:
*      1. Dialogue based with possibility to attach a new GUI for it.
*      2. The pile of cards shall be pre-generated at each shuffle and not randomized at each draw.
*      3. Gambling skill difference between host and player is checked, against a  roll, as usual.
*          3.1 The advantage of higher gambling skill:
*              3.1.1 Info over the the number of card packs used (which would be random 4 - 8 after each session).
*              3.1.2 Frequency of shuffling would be lower with better gambling + speech skill checks.
*              3.1.3 Card counting: available as long as gambling skill is higher than of host and the intellect of player is above X,
*                      as this is the easiest ways to get advantage over host.
*              3.1.4 Shuffle tracks: Occasionally on a critical or very hard roll on gambling + perception shuffling check,
*                      the player will be notified if there are way more high or low cards in the next X cards, if that is the case.
*          3.2 Disadvantage of lower gambling skill:
*              3.2.1 Basically missing out on the benefits, like: the character does not pay attention when the shuffling of cards happens,
*                      since he doesn't know that is important, so you miss that info.
*          3.3 Other possibilities:
*              3.3.1 Cheating 1: where the odds of high (7,8,9) or low cards (2,3,4) is reduced/raised, maybe the later could be added
*                      to some mini/repeatable quest or the host could be sweet talked /payed into changing the packs or whatever..
*                      (would only create the possibility for it, but not the quest itself) In this case the host would give a hint for the player,
*                      until the cards are replaced.
*              3.3.2 Cheating 2: where the player will be notified if the hole card is an Ace or 10.
*              3.3.3 Cheating 3: Casino could cheat as well, cutting down some cards for player session, this should be able to be find out
*                      via mini quest/tip drunk gambler/speech etc. or simply by gambling check rolls.
*          3.4. Different casinos could have different rules and special offers to promote themselves:
*              3.4.1 Rule changes:
*                  3.4.1.1 "Hit soft 17" - dealer has to draw a card if on soft 17.
*                  3.4.1.2 "Dealer wins ties" - dealer will win ties.
*                  3.4.1.3 "No Hole card" - dealer does not consult hole card until player finished his turns. (can't cheat to find out dealer's hole card)
*                  3.4.1.4 "No Black Jack after splitting Aces" - no bonus on Black Jack after splitting Aces.
*              3.4.2 Side bets:
*                  3.4.2.1 "Royal Match" - Pays for suit matches.
*                  3.4.2.2 "Perfect Pair" - is an extra bet option before drawing cards, the player can bet if he gets pairs (Perfect, Colored, Mixed, No pairs)
*                  3.4.2.3 "Lucky Ladies" - pays for initial cards value of 20. (Pair of Queen of Hearts, Suit Pair, etc)
*              3.4.3 Promotions:
*                  3.4.3.1 "Real" Black Jack pays higher than regular Black Jack. (11 to 2 instead of 3 to 2). (Real mean Ace of spades with a black Jack card.)
*
*  What to keep in sight:
*      1. It shall be configurable, so that mini quests or altering affects can differ from player to player and from session to session.
*      2. Shall be expandable later on to a graphical design.
*      3. Casino rules could be configurable, so that each session (or say,week) could be different, (or per player different odds) so that it can be tied to side quests to gather that info. (e.g.: Tip some wasted beggar or gambler to know the current situation / Or just the need to read the rules from dialogue so that botting is made harder.)
*
*  Author:     Slowhand
*  Reviewer:   N/A
*  Tester:     N/A


## Included By

- [blackjack.fos](blackjack.fos.md)
- [blackjack_dialogues.fos](blackjack_dialogues.fos.md)
- [blackjack_shoe.fos](blackjack_shoe.fos.md)

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __BLACKJACK_H__ |  |  |
| BLACKJACK_MIN_DECKS_IN_SHOE | `(2)` |  |
| BLACKJACK_MAX_DECKS_IN_SHOE | `(8)` |  |
| BLACKJACK_DEFAULT_DECKS_IN_SHOE | `(6)` |  |
| BLACKJACK_SIDE_NONE | `(0)` |  |
| BLACKJACK_SIDE_LUCKY_LADIES | `(1)` |  |
| BLACKJACK_SIDE_PERFECT_PAIR | `(2)` |  |
| BLAKCJACK_SIDE_ROYAL_MATCH | `(3)` |  |
| BLACKJACK_SHUFFLE_THRESHOLD_MIN | `(10)` |  |
| BLACKJACK_SHUFFLE_THRESHOLD_MAX | `(50)` |  |
| BLACKJACK_SHUFFLE_SKILL_THRESHOLD | `(50)` |  |
| BLACKJACK_SKILL_TO_SEE_SHOE_SIZE | `(40)` |  |
| BLACKJACK_SKILL_TO_SEE_SHUFFLING | `(60)` |  |
| BLACKJACK_SKILL_DIFF_TO_SEE_HOLE_CARD | `(10)` |  |
| BLACKJACK_SIDE_FACTOR_LL_QOHP_BJ | `(1000)` | Lucky Ladies side bet multiplication factors http://www.blackjack.com.au/side-bets/lucky-ladies/ |
| BLACKJACK_SIDE_FACTOR_LL_QOHP | `(125)` |  |
| BLACKJACK_SIDE_FACTOR_LL_MATCHED | `(19)` |  |
| BLACKJACK_SIDE_FACTOR_LL_SUITED | `(9)` |  |
| BLACKJACK_SIDE_FACTOR_LL_UNSUITED | `(4)` |  |
| BLACKJACK_SIDE_FACTOR_PP_PERFECTPAIR | `(25)` | Perfect Pair side bet multiplication factors http://www.blackjack.com.au/side-bets/perfect-pairs/ |
| BLACKJACK_SIDE_FACTOR_PP_COLOREDPAIR | `(12)` |  |
| BLACKJACK_SIDE_FACTOR_PP_MIXEDPAIR | `(6)` |  |
| BALCKJACK_SIDE_FACTOR_RM_ROYAL_MATCH | `(25)` | Royal Match side bet multiplication factors http://www.blackjack.com.au/side-bets/ |
| BLACKJACK_SIDE_FACTOR_RM_SUITED | `(2.5)` |  |

