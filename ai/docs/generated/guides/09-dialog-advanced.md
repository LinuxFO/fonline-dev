# Tutorial 9: Advanced Dialogs

Learn advanced dialog techniques including multi-stage conversations, dynamic text generation, skill checks, and complex branching logic.

## What You'll Learn

- Multi-stage conversations with state tracking
- Dynamic text generation
- Skill checks and random outcomes
- Dialog-based services (healing, trading)
- Chaining dialogs
- Advanced dialog patterns

## Prerequisites

- Completed [Tutorial 3: Dialog Systems](dialog-systems.md)
- Understanding of basic `d_` and `r_` scripts
- Familiarity with `dialog.fos`

## Overview

Beyond basic dialogs, you can create:
*   **Stateful conversations** - Remember previous choices
*   **Dynamic content** - Generate text based on game state
*   **Skill-based outcomes** - Different results based on player skills
*   **Service dialogs** - Healing, repairs, information
*   **Quest integration** - Complex quest progression

## Pattern 1: Multi-Stage Conversations

Track conversation progress using variables.

### Example: Information Gathering Quest

```angelscript
// Quest: Player must ask 3 NPCs about a rumor

// Demand: Check if player has asked this NPC
bool d_HasAskedAboutRumor(Critter& player, Critter@ npc)
{
    // Use ST_VAR0 to track which NPCs have been asked
    // Bit flags: Bit 0 = NPC1, Bit 1 = NPC2, Bit 2 = NPC3
    int npcId = npc.Stat[ST_NPC_ROLE];  // Unique ID for this NPC
    int askedFlags = player.Stat[ST_VAR0];
    
    return FLAG(askedFlags, npcId);
}

// Result: Mark this NPC as asked
void r_MarkAskedAboutRumor(Critter& player, Critter@ npc)
{
    int npcId = npc.Stat[ST_NPC_ROLE];
    SETFLAG(player.StatBase[ST_VAR0], npcId);
    
    // Check if all 3 have been asked
    if(player.Stat[ST_VAR0] == 7)  // Binary: 111 (all 3 bits set)
    {
        player.Say(SAY_NETMSG, "You've gathered enough information!");
        player.StatBase[ST_VAR1] = 2;  // Quest stage 2
    }
}
```

## Pattern 2: Dynamic Text Generation

Use `dlg_` functions to insert dynamic content into dialog text.

### Example: Show Player Stats

```angelscript
// Dialog text: "Your current level is $level and you have $caps caps."

void dlg_ShowPlayerInfo(Critter& player, Critter@ npc, string@ text)
{
    if(!IS_DIALOG_GENERATED(text))
        return;
    
    // Replace $level with actual level
    text += "$level" + player.Stat[ST_LEVEL];
    
    // Replace $caps with cap count
    text += "$caps" + _CritCountItem(player, PID_BOTTLE_CAPS);
}
```

### Example: Show Quest Progress

```angelscript
void dlg_ShowQuestProgress(Critter& player, Critter@ npc, string@ text)
{
    if(!IS_DIALOG_GENERATED(text))
        return;
    
    int killed = player.Stat[ST_VAR0];
    int needed = 10;
    
    text += "$progress" + killed + "/" + needed + " rats killed";
}
```

## Pattern 3: Skill Checks

Implement skill-based dialog options with success/failure outcomes.

### Example: Speech Check

```angelscript
// Demand: Check if player has high speech
bool d_HighSpeech(Critter& player, Critter@ npc, int threshold)
{
    return player.Skill[SK_SPEECH] >= threshold;
}

// Result: Attempt to persuade (with chance of failure)
uint r_PersuadeCheck(Critter& player, Critter@ npc, int difficulty, int successNode, int failNode)
{
    int speech = player.Skill[SK_SPEECH];
    int chance = CLAMP((speech - difficulty) * 2, 10, 95);
    
    if(Random(1, 100) <= chance)
    {
        npc.Say(SAY_NORM, "Alright, you've convinced me.");
        return successNode;
    }
    else
    {
        npc.Say(SAY_NORM, "Nice try, but I'm not buying it.");
        return failNode;
    }
}
```

### Example: Intelligence Check

```angelscript
// Demand: Smart player option
bool d_IsSmart(Critter& player, Critter@ npc, int minInt)
{
    return player.Stat[ST_INTELLECT] >= minInt;
}

// Result: Smart solution
void r_SmartSolution(Critter& player, Critter@ npc)
{
    npc.Say(SAY_NORM, "Impressive! I didn't think you'd figure that out.");
    player.AddItem(PID_BOTTLE_CAPS, 500);  // Bonus reward
    AddReputation(player, npc.Stat[ST_TEAM_ID], 50);
}
```

## Pattern 4: Dialog-Based Services

Implement services like healing or repairs through dialogs.

### Example: Doctor Service

```angelscript
// Demand: Check if player needs healing
bool d_NeedsHealing(Critter& player, Critter@ npc)
{
    return player.Stat[ST_CURRENT_HP] < player.Stat[ST_MAX_LIFE];
}

// Demand: Check if player can afford healing
bool d_CanAffordHealing(Critter& player, Critter@ npc, int cost)
{
    return _CritCountItem(player, PID_BOTTLE_CAPS) >= cost;
}

// Result: Heal player
void r_HealPlayer(Critter& player, Critter@ npc, int cost)
{
    // Take payment
    _CritDeleteItem(player, PID_BOTTLE_CAPS, cost);
    
    // Heal to full
    player.StatBase[ST_CURRENT_HP] = player.Stat[ST_MAX_LIFE];
    
    // Remove injuries (if any)
    player.StatBase[ST_DAMAGE_EYE] = 0;
    player.StatBase[ST_DAMAGE_RIGHT_ARM] = 0;
    player.StatBase[ST_DAMAGE_LEFT_ARM] = 0;
    
    npc.Say(SAY_NORM, "There you go, good as new!");
    player.Say(SAY_NETMSG, "You've been healed.");
}
```

### Example: Repair Service

```angelscript
// Result: Repair all items
void r_RepairItems(Critter& player, Critter@ npc, int cost)
{
    _CritDeleteItem(player, PID_BOTTLE_CAPS, cost);
    
    array<Item@> items;
    uint count = player.GetItems(-1, items);
    
    for(uint i = 0; i < count; i++)
    {
        // Repair deterioration
        if(items[i].IsDeteriorable())
        {
            items[i].Deterioration = 0;
        }
    }
    
    npc.Say(SAY_NORM, "All fixed up!");
    player.Say(SAY_NETMSG, "Your items have been repaired.");
}
```

## Pattern 5: Conditional Dialog Branches

Create complex branching based on multiple conditions.

### Example: Faction-Based Responses

```angelscript
// Different responses based on player's faction
uint r_FactionResponse(Critter& player, Critter@ npc)
{
    int playerFaction = GetGroupIndex(player);
    int npcFaction = npc.Stat[ST_TEAM_ID];
    
    if(playerFaction == npcFaction)
    {
        // Same faction - friendly
        return 10;  // Node 10: Friendly greeting
    }
    else if(GetGroupsStatus(playerFaction, npcFaction) == FACTION_ENEMY)
    {
        // Enemy faction - hostile
        return 20;  // Node 20: Hostile response
    }
    else
    {
        // Neutral - cautious
        return 30;  // Node 30: Neutral response
    }
}
```

### Example: Quest Stage Branching

```angelscript
uint r_QuestBranch(Critter& player, Critter@ npc)
{
    int questStage = player.Stat[ST_VAR0];
    
    switch(questStage)
    {
        case 0:  return 100;  // Not started
        case 1:  return 110;  // In progress
        case 2:  return 120;  // Completed
        case 3:  return 130;  // Failed
        default: return 0;
    }
}
```

## Pattern 6: Random Outcomes

Add variety with random dialog responses.

### Example: Random Greeting

```angelscript
void dlg_RandomGreeting(Critter& player, Critter@ npc, string@ text)
{
    if(!IS_DIALOG_GENERATED(text))
        return;
    
    string[] greetings = {
        "Well, hello there!",
        "What brings you here?",
        "Ah, a visitor!",
        "Good to see you.",
        "What can I do for you?"
    };
    
    text += "$greeting" + greetings[Random(0, 4)];
}
```

### Example: Random Reward

```angelscript
void r_RandomReward(Critter& player, Critter@ npc)
{
    int roll = Random(1, 100);
    
    if(roll <= 10)
    {
        // 10% - Rare item
        player.AddItem(PID_STIMPAK, 5);
        npc.Say(SAY_NORM, "Here, take these stimpaks!");
    }
    else if(roll <= 50)
    {
        // 40% - Caps
        player.AddItem(PID_BOTTLE_CAPS, Random(100, 300));
        npc.Say(SAY_NORM, "Here's some caps for your trouble.");
    }
    else
    {
        // 50% - Nothing special
        player.AddItem(PID_BOTTLE_CAPS, 50);
        npc.Say(SAY_NORM, "Thanks for your help.");
    }
}
```

## Pattern 7: Input Dialogs

Get text input from the player.

### Example: Name Input

```angelscript
uint dlg_GetPlayerName(Critter& player, Critter@ npc, string@ say)
{
    if(!IS_DIALOG_SAY_MODE(say))
        return 0;
    
    // 'say' contains the player's input
    if(say.length() < 3 || say.length() > 20)
    {
        player.Say(SAY_DIALOG, "Name must be 3-20 characters.");
        return 0;  // Stay on same node
    }
    
    // Store the name
    SetLexem(player, LEXEM_CUSTOM_NAME, say);
    
    npc.Say(SAY_NORM, "Nice to meet you, " + say + "!");
    return 100;  // Continue to next node
}
```

## Complete Example: Quest NPC with Multiple Stages

```angelscript
// quest_npc_advanced.fos
#include "_macros.fos"
#include "reputations_h.fos"

// Quest stages (ST_VAR0)
#define QUEST_NOT_STARTED  0
#define QUEST_ACTIVE       1
#define QUEST_COMPLETED    2

// === Demands ===

bool d_QuestNotStarted(Critter& player, Critter@ npc)
{
    return player.Stat[ST_VAR0] == QUEST_NOT_STARTED;
}

bool d_QuestActive(Critter& player, Critter@ npc)
{
    return player.Stat[ST_VAR0] == QUEST_ACTIVE;
}

bool d_QuestCompleted(Critter& player, Critter@ npc)
{
    return player.Stat[ST_VAR0] == QUEST_COMPLETED;
}

bool d_HasKilledEnough(Critter& player, Critter@ npc, int needed)
{
    return player.Stat[ST_VAR1] >= needed;
}

// === Results ===

void r_StartQuest(Critter& player, Critter@ npc)
{
    player.StatBase[ST_VAR0] = QUEST_ACTIVE;
    player.StatBase[ST_VAR1] = 0;  // Kill counter
    npc.Say(SAY_NORM, "Good luck out there!");
    player.Say(SAY_NETMSG, "Quest started: Clear the rats!");
}

void r_CompleteQuest(Critter& player, Critter@ npc)
{
    player.StatBase[ST_VAR0] = QUEST_COMPLETED;
    
    // Rewards
    player.AddItem(PID_BOTTLE_CAPS, 500);
    player.StatBase[ST_EXPERIENCE] += 1000;
    AddReputation(player, npc.Stat[ST_TEAM_ID], 100);
    
    npc.Say(SAY_NORM, "Excellent work! Here's your reward.");
    player.Say(SAY_NETMSG, "Quest completed!");
}

// === Dynamic Text ===

void dlg_ShowProgress(Critter& player, Critter@ npc, string@ text)
{
    if(!IS_DIALOG_GENERATED(text))
        return;
    
    int killed = player.Stat[ST_VAR1];
    text += "$progress" + killed + "/10 rats killed";
}
```

## Tips and Best Practices

### 1. Keep Dialog State Clean
Use specific variables for each quest/dialog to avoid conflicts:
```angelscript
// Good: Specific variables
#define QUEST_RATS_STAGE    ST_VAR0
#define QUEST_RATS_KILLS    ST_VAR1

// Bad: Reusing same variable
// ST_VAR0 for everything
```

### 2. Validate Player Input
Always check input in `dlg_` functions:
```angelscript
if(say.length() == 0 || say.length() > 50)
{
    player.Say(SAY_DIALOG, "Invalid input.");
    return 0;
}
```

### 3. Provide Feedback
Always inform the player of outcomes:
```angelscript
player.Say(SAY_NETMSG, "Quest updated!");
npc.Say(SAY_NORM, "Thanks for your help!");
```

## Next Steps

- **[Quest Basics](quest-basics.md)** - Integrate dialogs with quests
- **[NPC Reputation](npc-reputation.md)** - Faction-based dialogs
- **[NPC Traders](npc-traders.md)** - Trading dialogs

## Further Reading

- [dialog.fos](../dialog.fos.md) - Standard dialog functions
- [_dialogs.fos](../_dialogs.fos.md) - Dialog ID definitions

---

[← Back: NPC Followers](npc-followers.md) | [Next: Quest Basics →](quest-basics.md)
