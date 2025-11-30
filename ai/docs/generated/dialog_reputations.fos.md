---
title: dialog_reputations.fos
description: " FOnline: 2238 Rotators  dialog_reputations.fos ..."
---

# dialog_reputations.fos


FOnline: 2238
Rotators

dialog_reputations.fos


## Includes

- `reputations_h.fos`

## Included By

- [dialog.fos](dialog.fos.md)

## Functions

### r_AddReputation

* * Increase the reputation of the player up to the certain level. * @param index Index of the faction's reputation to change * @param val Number of reputation points * @param cap Maximum value to which the function can increase the reputation 

```angelscript
void r_AddReputation(Critter& player, Critter@ npc, int index, int val, int cap)
```

### r_SubReputation

* * Decrease the reputation of the player down to the certain level. * @param index Index of the faction's reputation to change * @param val Number of reputation points * @param cap Minimum value to which the function can decrease the reputation 

```angelscript
void r_SubReputation(Critter& player, Critter@ npc, int index, int val, int cap)
```

### r_AddReputationDogtags

```angelscript
void r_AddReputationDogtags(Critter& player, Critter@ npc, int index, int count)
```

### r_ApplyReputationModifiers

```angelscript
void r_ApplyReputationModifiers(Critter& player, Critter@ npc, int index, int num, int den)
```

### r_ApplyReputationModifiers

```angelscript
void r_ApplyReputationModifiers(Critter& player, Critter@ npc, int num, int den)
```

### r_AddReputation

* * Increase the reputation of the player in respect of npc's faction up to the certain level. * @param val Number of reputation points * @param cap Maximum value to which the function can increase the reputation 

```angelscript
void r_AddReputation(Critter& player, Critter@ npc, int val, int cap)
```

### r_SubReputation

* * Decrease the reputation of the player in respect of npc's faction down to the certain level. * @param val Number of reputation points * @param cap Minimum value to which the function can decrease the reputation 

```angelscript
void r_SubReputation(Critter& player, Critter@ npc, int val, int cap)
```

### r_AddReputation

* * Increase the reputation of the player in respect of npc's faction. * @param val Number of reputation points 

```angelscript
void r_AddReputation(Critter& player, Critter@ npc, int val)
```

### r_SubReputation

* * Decrease the reputation of the player in respect of npc's faction. * @param val Number of reputation points 

```angelscript
void r_SubReputation(Critter& player, Critter@ npc, int val)
```


