---
title: slaverun_dialog.fos
description: " FOnline: 2238 Rotators  slaverun_dialog.fos ..."
---

# slaverun_dialog.fos


FOnline: 2238
Rotators

slaverun_dialog.fos


## Includes

- `_macros.fos`
- `_vars.fos`
- `slaverun_h.fos`
- `utils_h.fos`
- `groups_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| NODE_FIRSTTIME | `(52)` | metzger's lines: |
| NODE_INTRODUCTION | `(56)` |  |
| NODE_TIMEOUT | `(58)` |  |
| NODE_BULLSHIT | `(62)` |  |
| NODE_SLAVER_SUCKED | `(63)` |  |
| NODE_BOLD_STUPID | `(65)` |  |
| NODE_COMPLETED | `(60)` |  |
| NODE_TOO_LATE | `(59)` |  |
| NODE_SLAVERS_KILLED | `(61)` |  |
| NODE_SLAVES_KILLED | `(64)` |  |
| NODE_BOTCHED | `(66)` |  |
| NODE_ERROR | `(6)` |  |
| NODE_TOO_LOW_REP | `(20)` |  |
| REWARD | `player.StatBase[ST_VAR1]` |  |

## Functions

### d_Var1isSet

```angelscript
bool d_Var1isSet(Critter& player, Critter@ npc, int val)
```

### d_NotStatusFlag

```angelscript
bool d_NotStatusFlag(Critter& player, Critter@ npc, int val)
```

### d_SlaverunAttempted

```angelscript
bool d_SlaverunAttempted(Critter& player, Critter@ npc, int val)
```

### r_SelectRewardNode

```angelscript
uint r_SelectRewardNode(Critter& player, Critter@ npc, int val)
```

### r_SelectNode

```angelscript
uint r_SelectNode(Critter& player, Critter@ npc, int val)
```

### r_ActivateQuest

```angelscript
uint r_ActivateQuest(Critter& player, Critter@ npc, int val)
```

### r_StartSlaverunCombat

```angelscript
void r_StartSlaverunCombat(Critter& player, Critter@ npc, int val)
```

### r_SpeechSlaver

```angelscript
uint r_SpeechSlaver(Critter& player, Critter@ npc, int val)
```

### r_SpeechBoldStupid

```angelscript
uint r_SpeechBoldStupid(Critter& player, Critter@ npc, int val)
```

### r_Var1Set

```angelscript
void r_Var1Set(Critter& player, Critter@ npc, int val)
```

### r_SlaverepModify

args: increase, cap (none if =0)

```angelscript
void r_SlaverepModify(Critter& player, Critter@ npc, int val1, int val2)
```

### dlg_ShowReward

```angelscript
void dlg_ShowReward(Critter& player, Critter@ npc, string@ text)
```

### SlaverepModify

```angelscript
void SlaverepModify(Critter& player, int val1, int val2)
```


