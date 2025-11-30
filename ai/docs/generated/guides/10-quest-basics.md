# Tutorial 10: Quest Basics

Learn how to create and script quests in FOnline, from simple fetch tasks to complex storylines.

## What You'll Learn

- Understanding Quest Variables
- Designing Quest States
- Writing Demand (`d_`) and Result (`r_`) scripts for quests
- Updating the Quest Log
- Best practices for quest writing

## Prerequisites

- Completed [Tutorial 3: Dialog Systems](dialog-systems.md)
- Understanding of `_vars.fos`

## Overview

In FOnline, a "Quest" is essentially a tracking variable (GameVar) that changes value as the player progresses.

**Common Quest States:**
- `0`: None (Not started)
- `1`: Active (Started)
- `2`: Completed
- `3+`: Failed or alternative endings

## Step 1: Define the Quest Variable

All quest variables are defined in `_vars.fos`. You need to add a unique ID for your quest.

1. Open `PReloaded/Server/scripts/_vars.fos`
2. Add a new constant in the `Quest variables` section:

```angelscript
// _vars.fos

// ... existing vars ...
#define Q_MY_FIRST_QUEST        ( 4000 ) // Unique ID
```

> [!NOTE]
> Make sure the ID (4000) is not used by another variable.

## Step 2: Create the Quest Logic

You can put quest logic in a dedicated file (e.g., `quest_myquest.fos`) or use `quests.fos`. For this tutorial, we'll create a simple "Kill Rats" quest.

### The Scenario
1.  **Start**: NPC asks player to kill 5 rats.
2.  **Progress**: Player kills rats, counter increases.
3.  **Finish**: Player returns to NPC, gets reward.

### Scripting the Dialog Logic

Create a file `quest_rats.fos`:

```angelscript
// quest_rats.fos
#include "_macros.fos"

// Define the quest variable ID (if not in _vars.fos yet)
#define Q_RATS_PROBLEM      ( 4001 )

// Track number of rats killed
#define V_RATS_KILLED       ( 4002 ) 

// Demand: Check if quest is not started
bool d_NotStarted(Critter& player, Critter@ npc)
{
    return GameVar(Q_RATS_PROBLEM, player.Id).GetValue() == 0;
}

// Demand: Check if quest is active
bool d_IsActive(Critter& player, Critter@ npc)
{
    return GameVar(Q_RATS_PROBLEM, player.Id).GetValue() == 1;
}

// Demand: Check if player killed enough rats
bool d_RatsKilled(Critter& player, Critter@ npc)
{
    return GameVar(V_RATS_KILLED, player.Id).GetValue() >= 5;
}

// Result: Start the quest
void r_StartQuest(Critter& player, Critter@ npc)
{
    GameVar(Q_RATS_PROBLEM, player.Id) = 1;
    GameVar(V_RATS_KILLED, player.Id) = 0; // Reset counter
    
    // Add to quest log (requires msg string in FOGAME.MSG)
    // player.AddQuest(Q_RATS_PROBLEM); 
}

// Result: Finish the quest
void r_FinishQuest(Critter& player, Critter@ npc)
{
    GameVar(Q_RATS_PROBLEM, player.Id) = 2;
    
    // Give Reward
    player.AddItem(PID_BOTTLE_CAPS, 100);
    player.StatBase[ST_EXPERIENCE] += 500;
    
    // Remove from active quest log
    // player.RemoveQuest(Q_RATS_PROBLEM);
}
```

## Step 3: Handling Kills

To track rat kills, we need to hook into the `critter_dead` event or assign a script to the rats.

### Option A: Map Script (Recommended for specific locations)
If the rats are in a specific basement, use a map script.

```angelscript
// map_rat_basement.fos

void map_init(Map& map, bool firstTime)
{
    map.SetEvent(MAP_EVENT_CRITTER_DEAD, "_RatDead");
}

void _RatDead(Map& map, Critter& rat, Critter@ killer)
{
    // Check if it was a rat and killed by a player
    if(rat.Stat[ST_BODY_TYPE] == BT_RAT && valid(killer) && killer.IsPlayer())
    {
        // Check if player has the quest active
        GameVar qVar = GameVar(Q_RATS_PROBLEM, killer.Id);
        if(qVar.GetValue() == 1)
        {
            // Increment kill counter
            GameVar kVar = GameVar(V_RATS_KILLED, killer.Id);
            if(kVar.GetValue() < 5)
            {
                kVar += 1;
                killer.Say(SAY_NETMSG, "Rats killed: " + kVar.GetValue() + "/5");
            }
            
            if(kVar.GetValue() == 5)
            {
                killer.Say(SAY_NETMSG, "I should return to the quest giver.");
            }
        }
    }
}
```

## Step 4: Dialog Editor Setup

Now you link these scripts in the Dialog Editor:

1.  **Node 1 (Greeting)**:
    *   Answer: "I need work." -> **Demand**: `quest_rats@d_NotStarted` -> **GoTo**: Node 2
    *   Answer: "About those rats..." -> **Demand**: `quest_rats@d_IsActive` -> **GoTo**: Node 3

2.  **Node 2 (Proposal)**:
    *   Text: "Can you kill 5 rats in the basement?"
    *   Answer: "Sure." -> **Result**: `quest_rats@r_StartQuest` -> **GoTo**: Exit

3.  **Node 3 (Check Progress)**:
    *   Answer: "I killed them all." -> **Demand**: `quest_rats@d_RatsKilled` -> **Result**: `quest_rats@r_FinishQuest` -> **GoTo**: Node 4 (Thanks)
    *   Answer: "Still working on it." -> **GoTo**: Exit

## Advanced: Quest Log

To make the quest appear in the PipBoy:

1.  Define quest in `_vars.fos` with a number corresponding to `FOGAME.MSG`.
2.  Edit `text/engl/FOGAME.MSG`:
    ```
    {4001001}{}{Rat Problem}
    {4001002}{}{Kill 5 rats in the basement.}
    ```
3.  Use `player.AddQuest(Q_RATS_PROBLEM)` in your result script.

## Common Issues

### Quest variable resets?
*   Ensure you are using `GameVar` correctly.
*   Check if `_vars.fos` ID conflicts with another quest.

### Kill counter not updating?
*   Verify the map script is assigned to the map in Mapper.
*   Check if `_RatDead` signature matches `MAP_EVENT_CRITTER_DEAD`.

## Next Steps

*   **[Tutorial 5: Items & Crafting](items-crafting.md)** - Create custom rewards
*   **[Tutorial 6: Map Scripting](map-scripting.md)** - Create the rat basement
