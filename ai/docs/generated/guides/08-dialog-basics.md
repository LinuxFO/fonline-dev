# Tutorial 8: Dialog Basics

Learn how to create interactive dialogs for NPCs, including branching conversations, skill checks, and rewards.

## What You'll Learn

- Understanding the Dialog structure
- Assigning dialogs to NPCs
- Using Demand and Result scripts
- Common dialog functions (`d_` and `r_` functions)
- Creating dynamic conversations

## Prerequisites

- Completed [Tutorial 2: Working with NPCs](npc-tutorial.md)
- Basic understanding of `dialog.fos` functions

## Overview

Dialogs in FOnline are not just text; they are powerful scripting tools. A dialog consists of:
1.  **Dialog ID**: A unique number identifying the dialog.
2.  **Nodes**: Individual screens of text and options.
3.  **Links**: Connections between nodes (answers).
4.  **Demands (`d_`)**: Conditions that must be met to see an option.
5.  **Results (`r_`)**: Actions taken when an option is chosen.

## Step 1: Assigning Dialog to NPC

Every NPC can have a dialog assigned via the `ST_DIALOG_ID` stat.

### In Script

```angelscript
#include "_dialogs.fos"

void critter_init(Critter& npc, bool firstTime)
{
    if(firstTime)
    {
        // Assign the "Hub Sheriff" dialog
        npc.StatBase[ST_DIALOG_ID] = DIALOG_hub_sheriff;
    }
}
```

### In Dialog Editor
Usually, dialogs are created in a visual Dialog Editor tool, which generates the underlying data. However, understanding the script side is crucial for advanced logic.

## Step 2: Demand Scripts (`d_`)

Demand scripts check conditions. They must return `bool`. If true, the option is shown; if false, it's hidden.

### Naming Convention
Function names must start with `d_`.

### Common Demands (from `dialog.fos`)

```angelscript
// Check if player has a specific item
bool d_HasItem(Critter& player, Critter@ npc, int pid, int count)

// Check if player has enough caps
bool d_HasMoney(Critter& player, Critter@ npc, int amount)

// Check if player has high intelligence
bool d_IsSmart(Critter& player, Critter@ npc)
{
    return player.Stat[ST_INTELLECT] >= 7;
}

// Check global variable (Quest state)
bool d_QuestActive(Critter& player, Critter@ npc, int varId)
{
    return GetRootMapData(player.GetMap(), varId) == 1;
}
```

### Example Usage
In the dialog editor, you would attach `d_IsSmart` to a "smart" answer option.

## Step 3: Result Scripts (`r_`)

Result scripts execute actions. They return `void` (usually) or `uint` (for node switching).

### Naming Convention
Function names must start with `r_`.

### Common Results (from `dialog.fos`)

```angelscript
// Give item to player
void r_AddItem(Critter& player, Critter@ npc, int pid, int count)

// Heal player
void r_DocHeal(Critter& player, Critter@ npc)

// Attack player
void r_Attack(Critter& player, Critter@ npc)
{
    AddAttackPlane(npc, AI_PLANE_ATTACK_PRIORITY, player);
}

// Teleport player
void r_TeleportToMap(Critter& player, Critter@ npc, int mapPid, int entry)
```

## Step 4: Creating Custom Dialog Scripts

You can create your own dialog scripts in any module, but `dialog.fos` is the standard place for general ones.

### Example: Quest Giver Logic

```angelscript
// my_quest_dialog.fos

// Demand: Check if player killed 10 rats
bool d_RatsKilled(Critter& player, Critter@ npc)
{
    return player.Stat[ST_VAR0] >= 10;
}

// Result: Give reward and reset counter
void r_GiveReward(Critter& player, Critter@ npc)
{
    player.AddItem(PID_BOTTLE_CAPS, 500);
    player.StatBase[ST_VAR0] = 0; // Reset
    player.Say(SAY_NETMSG, "You received 500 caps.");
}
```

## Step 5: Advanced Dialog Features

### Skill Rolls
You can perform skill checks directly in dialogs.

```angelscript
// Result: Roll Speech skill
// If success, go to node 5. If fail, go to node 6.
uint r_SkillRoll(Critter& player, Critter@ npc, int skill, int successNode)
```

### Random Branching
Make NPCs unpredictable.

```angelscript
// Demand: 50% chance to show this option
bool d_Random(Critter& player, Critter@ npc, int chance)
{
    return Random(0, 100) < chance;
}
```

## Common Issues

### 1. Dialog not appearing
**Problem**: NPC says nothing or "Error".
**Solution**:
- Check if `ST_DIALOG_ID` is set correctly.
- Ensure the dialog exists in the server files.
- Check if the root node has valid text.

### 2. Script not found
**Problem**: Server log says "Script 'd_MyFunc' not found".
**Solution**:
- Ensure the function is global (not inside a class).
- Check spelling strictly.
- If in a different module, use `module@function` syntax in the editor.

## Next Steps

- **[Tutorial 4: Quest System Basics](quest-basics.md)** - Link dialogs to quests
- **[Tutorial 5: Scripting Quests](quest-scripting.md)** - Advanced quest logic

## Further Reading

- [dialog.fos](../dialog.fos.md) - Standard dialog functions
- [_dialogs.fos](../_dialogs.fos.md) - Dialog ID definitions
