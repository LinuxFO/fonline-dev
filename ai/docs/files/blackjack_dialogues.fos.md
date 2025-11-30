---
title: blackjack_dialogues.fos
description: "*< *  Dialogue calls for the Blackjack module. ..."
---

# blackjack_dialogues.fos

*<
*  Dialogue calls for the Blackjack module.


## Includes

- `blackjack_h.fos`
- `blackjack_manager.fos`

## Functions

### r_Init

```angelscript
void r_Init(Critter& player, Critter@ dealer)
```

### r_LeaveBlackjackTable

*< Leave Blackjack table

```angelscript
void r_LeaveBlackjackTable(Critter& player, Critter@ dealer)
```

### r_SetSidebetType

```angelscript
void r_SetSidebetType(Critter& player, Critter@ dealer, int sidebetType)
```

### r_SetSidebetValue

```angelscript
void r_SetSidebetValue(Critter& player, Critter@ dealer, int sidebetValue)
```

### d_IsSidebetAvailable

```angelscript
bool d_IsSidebetAvailable(Critter& player, Critter@ dealer)
```

### r_SetBetValue

```angelscript
void r_SetBetValue(Critter& player, Critter@ dealer, int value)
```

### d_IsHitAvailable

```angelscript
bool d_IsHitAvailable(Critter& player, Critter@ dealer)
```

### r_Hit

```angelscript
void r_Hit(Critter& player, Critter@ dealer)
```

### d_IsStandAvailable

```angelscript
bool d_IsStandAvailable(Critter& player, Critter@ dealer)
```

### r_Stand

```angelscript
void r_Stand(Critter& player, Critter@ dealer)
```

### d_IsPlayerBusted

```angelscript
bool d_IsPlayerBusted(Critter& player, Critter@ dealer)
```

### d_IsDoubleDownContinueAvailable

```angelscript
bool d_IsDoubleDownContinueAvailable(Critter& player, Critter@ dealer)
```

### d_IsDoubleDownAvailable

```angelscript
bool d_IsDoubleDownAvailable(Critter& player, Critter@ dealer)
```

### r_DoubleDown

```angelscript
void r_DoubleDown(Critter& player, Critter@ dealer)
```

### d_IsSplitPairsAvailable

```angelscript
bool d_IsSplitPairsAvailable(Critter& player, Critter@ dealer)
```

### d_IsInsuranceAvailable

```angelscript
bool d_IsInsuranceAvailable(Critter& player, Critter@ dealer)
```

### r_Insurance

```angelscript
void r_Insurance(Critter& player, Critter@ dealer)
```

### d_IsEvenMoneyAvailable

```angelscript
bool d_IsEvenMoneyAvailable(Critter& player, Critter@ dealer)
```

### d_IsSurrenderAvailable

```angelscript
bool d_IsSurrenderAvailable(Critter& player, Critter@ dealer)
```

### r_Surrender

```angelscript
void r_Surrender(Critter& player, Critter@ dealer)
```

### r_NewRound

```angelscript
void r_NewRound(Critter& player, Critter@ dealer)
```

### r_EvenMoney

```angelscript
void r_EvenMoney(Critter& player, Critter@ dealer)
```

### r_DealerTakesCard

```angelscript
void r_DealerTakesCard(Critter& player, Critter@ dealer)
```

### d_IsDealerDone

```angelscript
bool d_IsDealerDone(Critter& player, Critter@ dealer)
```

### d_IsDealerNotDone

```angelscript
bool d_IsDealerNotDone(Critter& player, Critter@ dealer)
```

### r_DealerFinishedTurn

```angelscript
void r_DealerFinishedTurn(Critter& player, Critter@ dealer)
```

### dlg_ShowInfo

```angelscript
void dlg_ShowInfo(Critter& player, Critter@ npc, string@ text)
```


