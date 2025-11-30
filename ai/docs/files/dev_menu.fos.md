---
title: dev_menu.fos
description: " FOnline: 2238 Rotators  dev_menu.fos ..."
---

# dev_menu.fos


FOnline: 2238
Rotators

dev_menu.fos


## Includes

- `_macros.fos`
- `npc_common_h.fos`
- `npc_planes_h.fos`
- `utils_h.fos`

## Functions

### GetDevCritter

 helper - gets critter from given id, sends appropriate error messages to player 

```angelscript
Critter@ GetDevCritter(Critter& player, int crId)
```

### GetDevItem

 helper - gets item from given id, sends appropriate error message to player when item not found 

```angelscript
Item@ GetDevItem(Critter& player, int itemId)
```

### SendLVars

```angelscript
void SendLVars(Critter& player, int p0, int p1, int p2, string@ param3, array<int>@ param4)
```

### unsafe_Possess

 Posses given critter 

```angelscript
void unsafe_Possess(Critter& player, int crId, int p1, int p2, string@ param3, array<int>@ param4)
```

### unsafe_KillCritter

 Kills/revive critter 

```angelscript
void unsafe_KillCritter(Critter& player, int p0, int p1, int p2, string@ param3, array<int>@ param4)
```

### unsafe_NeutralizeCritter

 Knock outs/wakes up critter 

```angelscript
void unsafe_NeutralizeCritter(Critter& player, int crId, int p1, int p2, string@ param3, array<int>@ param4)
```

### unsafe_RemoveCritter

 Removes critter 

```angelscript
void unsafe_RemoveCritter(Critter& player, int crId, int p1, int p2, string@ param3, array<int>@ param4)
```

### unsafe_RemoveItem

 Removes item 

```angelscript
void unsafe_RemoveItem(Critter& player, int itemId, int p1, int p2, string@ param3, array<int>@ param4)
```

### unsafe_Say

 Forces critter to say something 

```angelscript
void unsafe_Say(Critter& player, int crId, int sayType, int p2, string@ message, array<int>@ param4)
```

### unsafe_MoveTo

 Issues move plan for an npc 

```angelscript
void unsafe_MoveTo(Critter& player, int crId, int x, int y, string@ param3, array<int>@ param4)
```

### unsafe_PickItem

 Issues pick plan for critter 

```angelscript
void unsafe_PickItem(Critter& player, int crId, int itemId, int p2, string@ param3, array<int>@ param4)
```

### unsafe_Attack

 Issues attack plan for critter 

```angelscript
void unsafe_Attack(Critter& player, int crId, int targetId, int p2, string@ param3, array<int>@ param4)
```

### unsafe_Stop

 Clears all plans 

```angelscript
void unsafe_Stop(Critter& player, int crId, int p1, int p2, string@ param3, array<int>@ param4)
```

### unsafe_Trade

 Shows item browsing window for critter or container 

```angelscript
void unsafe_Trade(Critter& player, int crId, int itemId, int p2, string@ param3, array<int>@ param4)
```

### unsafe_Teleport

 Teleports critter (crId) or player to hex 

```angelscript
void unsafe_Teleport(Critter& player, int crId, int x, int y, string@ param3, array<int>@ param4)
```

### unsafe_Rotate

 Guess what 

```angelscript
void unsafe_Rotate(Critter& player, int crId, int dir, int y, string@ param3, array<int>@ param4)
```

### GiveXp

 Xp reward 

```angelscript
void GiveXp(Critter& player, int crId, int amount, int p2, string@ message, array<int>@ param4)
```

### Airstrike

```angelscript
void Airstrike(Critter& player, int crId, int x, int y, string@ param3, array<int>@ param4)
```

### unsafe_SpawnCritter

 Spawn critters  param4: { pid, x, y, dir, dialog, /*script*/, ai, bag, team, mob, level }

```angelscript
void unsafe_SpawnCritter(Critter& player, int p0, int p1, int p2, string@ script, array<int>@ param4)
```

### answer_Generic

```angelscript
void answer_Generic(Critter& player, uint answerI, string& answerS)
```

### dlgbox

```angelscript
void dlgbox(Critter& cr, int p0, int p1, int p2)
```

### skillbox

```angelscript
void skillbox(Critter& cr, int p0, int p1, int p2)
```

### say

```angelscript
void say(Critter& cr, int p0, int p1, int p2)
```

### timer

```angelscript
void timer(Critter& cr, int p0, int p1, int p2)
```

### bag

```angelscript
void bag(Critter& cr, int p0, int p1, int p2)
```

### inventory

```angelscript
void inventory(Critter& cr, int p0, int p1, int p2)
```

### cha

```angelscript
void cha(Critter& cr, int p0, int p1, int p2)
```

### fixboy

```angelscript
void fixboy(Critter& cr, int p0, int p1, int p2)
```

### pipboy

```angelscript
void pipboy(Critter& cr, int p0, int p1, int p2)
```

### minimap

```angelscript
void minimap(Critter& cr, int p0, int p1, int p2)
```

### close

```angelscript
void close(Critter& cr, int p0, int p1, int p2)
```


