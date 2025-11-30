# Tutorial 2: NPC Basics

Learn how to create and control Non-Player Characters (NPCs) in FOnline. This tutorial covers NPC initialization, movement, behavior, and common patterns used throughout the codebase.

## What You'll Learn

- Creating NPC scripts with event handlers
- Understanding the `Critter` object and its properties
- Making NPCs move and wander
- Using NPC stats and attributes
- Implementing idle behavior
- Common NPC functions and utilities

## Prerequisites

- Completed [Tutorial 1: Hello World](getting-started.md)
- Basic understanding of AngelScript syntax
- Familiarity with `_macros.fos` and `_defines.fos`

## Overview

NPCs are the heart of FOnline gameplay. From merchants to guards to wandering brahmin, every NPC is controlled by a script. In this tutorial, you'll learn the fundamental patterns used in **1,400+ NPC-related functions** across the codebase.

**Real-world uses:**
- Town guards that patrol and respond to threats
- Merchants with custom behavior
- Quest NPCs with specific routines
- Wandering creatures and animals

## Understanding the Critter Object

The `Critter` object represents any character in the game (players and NPCs). Here are the most important properties:

### Key Properties

```angelscript
// Basic info
cr.Id              // Unique ID
cr.Name            // Display name
cr.HexX, cr.HexY   // Current position

// Stats (use ST_* constants from _defines.fos)
cr.Stat[ST_LEVEL]           // Level
cr.Stat[ST_CURRENT_HP]      // Current HP
cr.Stat[ST_MAX_LIFE]        // Max HP
cr.Stat[ST_BODY_TYPE]       // Body type (human, ghoul, etc.)
cr.Stat[ST_TEAM_ID]         // Team/faction ID

// Skills
cr.Skill[SK_SMALL_GUNS]     // Small guns skill
cr.Skill[SK_SNEAK]          // Sneak skill

// Perks
cr.Perk[PE_BONUS_MOVE]      // Has bonus move perk?
```

### Key Methods

```angelscript
cr.Say(SAY_NORM, "Hello!")          // Make NPC speak
cr.GetMap()                          // Get current map
cr.GetItems(SLOT_INV, items)        // Get inventory items
cr.Wait(1000)                        // Wait 1 second
cr.SetEvent(EVENT_TYPE, "function") // Set event handler
```

## Step 1: Create a Simple NPC Script

Let's create a wandering merchant NPC that moves around randomly.

### Create the File

1. Create `wandering_merchant.fos` in `PReloaded/Server/scripts/`

2. Add the basic structure:

```angelscript
// wandering_merchant.fos
// A simple wandering merchant NPC

#include "_macros.fos"
#include "npc_common_h.fos"
#include "npc_planes_h.fos"

// This function is called when the NPC is created or loaded
void critter_init(Critter& npc, bool firstTime)
{
    // Set up event handlers
    npc.SetEvent(CRITTER_EVENT_IDLE, "_MerchantIdle");
    
    // Log for debugging
    Log("Wandering merchant initialized: " + npc.Name);
}
```

**Code Explanation:**
- `critter_init` - Called when NPC spawns or server starts
- `firstTime` - `true` if NPC just spawned, `false` if loading from save
- `SetEvent` - Registers a function to handle specific events
- `CRITTER_EVENT_IDLE` - Triggered periodically when NPC has nothing to do

## Step 2: Implement Idle Behavior

The idle event is where NPCs "think" and decide what to do next.

```angelscript
void _MerchantIdle(Critter& npc)
{
    // Say something occasionally
    if(Random(0, 100) == 0)
    {
        npc.Say(SAY_NORM_ON_HEAD, "Best prices in the wasteland!");
    }
    
    // Move randomly 30% of the time
    if(Random(0, 100) < 30)
    {
        MoveRandom(npc, 10, 3, false);
    }
    
    // Wait before next idle call (5-15 seconds)
    npc.Wait(Random(5000, 15000));
}
```

**Code Explanation:**
- `Random(0, 100)` - Random number from 0 to 100
- `SAY_NORM_ON_HEAD` - Speech appears above NPC's head
- `MoveRandom(npc, maxDist, stepDist, run)` - Move randomly
  - `maxDist`: Maximum distance from home (10 hexes)
  - `stepDist`: Distance of each step (3 hexes)
  - `run`: Walk or run (false = walk)
- `npc.Wait(ms)` - Wait before next idle call

## Step 3: Add More Realistic Behavior

Let's make the merchant more interesting with greetings and reactions.

```angelscript
void critter_init(Critter& npc, bool firstTime)
{
    npc.SetEvent(CRITTER_EVENT_IDLE, "_MerchantIdle");
    npc.SetEvent(CRITTER_EVENT_MESSAGE, "_MerchantMessage");
    
    if(firstTime)
    {
        // Set home position (where NPC returns to)
        npc.SetHomePos(npc.HexX, npc.HexY, npc.Dir);
        
        Log("Wandering merchant spawned at " + npc.HexX + "," + npc.HexY);
    }
}

void _MerchantIdle(Critter& npc)
{
    // Occasionally say something
    int action = Random(0, 100);
    
    if(action < 5)
    {
        // 5% chance to advertise
        string[] messages = {
            "Best prices in the wasteland!",
            "Come see my wares!",
            "Trading post open for business!",
            "Got caps? I got goods!"
        };
        npc.Say(SAY_NORM_ON_HEAD, messages[Random(0, 3)]);
    }
    else if(action < 35)
    {
        // 30% chance to move randomly
        MoveRandom(npc, 15, 4, false);
    }
    else if(action < 40)
    {
        // 5% chance to return home
        uint bMap;
        uint16 bX = 0, bY = 0;
        uint8 bDir = 0;
        npc.GetHomePos(bMap, bX, bY, bDir);
        AddWalkPlane(npc, 0, bX, bY, bDir, false, 0);
    }
    
    // Wait 3-10 seconds
    npc.Wait(Random(3000, 10000));
}

void _MerchantMessage(Critter& npc, Critter& fromCr, int message, int value)
{
    // React when players come near
    if(message == CRITTER_EVENT_SHOW_CRITTER)
    {
        if(!_IsTrueNpc(fromCr)) // Is it a player?
        {
            npc.Say(SAY_NORM, "Greetings, traveler!");
        }
    }
}
```

## Step 4: Using NPC Stats

NPCs can have different stats that affect their behavior.

```angelscript
void _MerchantIdle(Critter& npc)
{
    // Check NPC's health
    int currentHP = npc.Stat[ST_CURRENT_HP];
    int maxHP = npc.Stat[ST_MAX_LIFE];
    
    if(currentHP < maxHP / 2)
    {
        // Merchant is injured, flee!
        npc.Say(SAY_SHOUT, "I'm getting out of here!");
        Flee(npc, true); // Run to exit grid
        return;
    }
    
    // Check if NPC has high charisma
    if(npc.Stat[ST_CHARISMA] >= 7)
    {
        // More talkative
        if(Random(0, 50) == 0)
        {
            npc.Say(SAY_NORM_ON_HEAD, "Have I got a deal for you!");
        }
    }
    
    // Normal behavior...
    npc.Wait(Random(5000, 15000));
}
```

## Complete Example: Wandering Brahmin

Here's a complete, working example based on the actual `all_brahmin.fos` script:

```angelscript
// my_brahmin.fos
// A simple brahmin that wanders and says "Moo"

#include "_macros.fos"
#include "npc_common_h.fos"
#include "npc_planes_h.fos"

void critter_init(Critter& brahmin, bool firstTime)
{
    brahmin.SetEvent(CRITTER_EVENT_IDLE, "_BrahminIdle");
    
    if(firstTime)
    {
        // Set home position
        brahmin.SetHomePos(brahmin.HexX, brahmin.HexY, brahmin.Dir);
        Log("Brahmin spawned!");
    }
}

void _BrahminIdle(Critter& brahmin)
{
    // Moo animation occasionally
    if(Random(0, 199) == 0)
    {
        _CritAnimatePunch(brahmin);
    }
    
    // Walking behavior
    int walking = Random(0, 99);
    
    if(walking == 0)
    {
        // Return to home hex
        brahmin.DropPlanes();
        uint bMap;
        uint16 bX = 0, bY = 0;
        uint8 bDir = 0;
        brahmin.GetHomePos(bMap, bX, bY, bDir);
        AddWalkPlane(brahmin, AI_PLANE_WALK_PRIORITY, bX, bY, bDir, false, 0);
    }
    else if(walking < 33)
    {
        // Walk randomly in small steps
        MoveRandom(brahmin, 14, 3, false);
    }
    
    // Say "Moo" occasionally
    if(Random(0, 3000) == 0)
    {
        brahmin.Say(SAY_NORM_ON_HEAD, "Moo. Moo I say.");
    }
    
    // Wait before next idle
    brahmin.Wait(Random(500, 20000));
}
```

## Common NPC Functions

These utility functions from `npc_common.fos` are frequently used:

### Movement Functions

```angelscript
// Move randomly within maxDist from home
MoveRandom(npc, maxDist, stepDist, run);

// Flee to worldmap exit
Flee(npc, true);

// Move in a specific direction
MoveByDir(npc, direction, steps, run);

// Add a walk plane to specific hex
AddWalkPlane(npc, priority, hexX, hexY, dir, run, cut);
```

### Combat Functions

```angelscript
// Make NPC attack a target
AttackCritter(attacker, target);

// Arm best weapon from inventory
ArmBestWeapon(npc);

// Put away weapons
PutAwayItems(npc);
```

### Utility Functions

```angelscript
// Heal NPC completely
Heal(npc);

// Check if NPC is intelligent
HasIntelligentBrain(npc);

// Check if in specific location
IsInLocation(npc, locationPID);
```

## Common Event Handlers

NPCs can respond to various events:

```angelscript
void critter_init(Critter& npc, bool firstTime)
{
    // Called when NPC spawns or loads
}

void _Idle(Critter& npc)
{
    // Called periodically when NPC has nothing to do
}

void _Dead(Critter& npc, Critter@ killer)
{
    // Called when NPC dies
}

void _Message(Critter& npc, Critter& fromCr, int message, int value)
{
    // Called when NPC receives a message
    // (e.g., another critter comes into view)
}

void _Attacked(Critter& npc, Critter& attacker)
{
    // Called when NPC is attacked
}
```

## Common Issues & Solutions

### Issue 1: NPC doesn't move
**Problem**: `MoveRandom` doesn't work

**Solution**:
- Make sure `npc_common_h.fos` and `npc_planes_h.fos` are included
- Check that the NPC isn't in combat or busy
- Verify the NPC has a valid map: `if(valid(npc.GetMap()))`

### Issue 2: Idle function not called
**Problem**: `_Idle` never executes

**Solution**:
- Verify event is set: `npc.SetEvent(CRITTER_EVENT_IDLE, "_Idle");`
- Make sure function name matches exactly (case-sensitive)
- Check that `npc.Wait()` is called at the end of idle function

### Issue 3: NPC speaks but nothing appears
**Problem**: `npc.Say()` doesn't show text

**Solution**:
- Use correct say mode: `SAY_NORM_ON_HEAD` for overhead text
- Check that string isn't empty
- Verify NPC is on a valid map

## Exercises

### Exercise 1: Chatty Guard
Create a guard NPC that:
- Stands in one place
- Says "Halt!" when players approach
- Occasionally looks in different directions

<details>
<summary>Solution</summary>

```angelscript
void critter_init(Critter& guard, bool firstTime)
{
    guard.SetEvent(CRITTER_EVENT_IDLE, "_GuardIdle");
    guard.SetEvent(CRITTER_EVENT_MESSAGE, "_GuardMessage");
}

void _GuardIdle(Critter& guard)
{
    // Occasionally change direction
    if(Random(0, 100) < 10)
    {
        guard.SetDir(Random(0, 5));
    }
    
    guard.Wait(Random(5000, 10000));
}

void _GuardMessage(Critter& guard, Critter& fromCr, int message, int value)
{
    if(message == CRITTER_EVENT_SHOW_CRITTER && !_IsTrueNpc(fromCr))
    {
        guard.Say(SAY_NORM, "Halt! State your business.");
    }
}
```
</details>

### Exercise 2: Patrol Route
Create an NPC that walks between 3 specific hexes in a loop.

**Hint**: Use `AddWalkPlane` and track current waypoint with a local variable.

### Exercise 3: Coward NPC
Create an NPC that flees when its HP drops below 50%.

**Hint**: Check `npc.Stat[ST_CURRENT_HP]` in idle function and use `Flee(npc, true)`.

## Next Steps

Now that you understand basic NPCs, you're ready to learn:

- **[Tutorial 2A: NPC AI Planes & Advanced Behavior](npc-ai-planes.md)** - Master the AI Planes system, patrol routes, and NPC coordination
- **[Tutorial 3: Dialog Systems](dialog-systems.md)** - Make NPCs talk to players
- **[Tutorial 5: Quest System Basics](quest-basics.md)** - Create quest-giving NPCs
- **[Common Patterns Cookbook](../guides/patterns-cookbook.md)** - Quick NPC recipes

## Further Reading

- [npc_common.fos](../npc_common.fos.md) - NPC utility functions
- [npc_planes_h.fos](../npc_planes_h.fos.md) - AI plane system
- [main.fos](../main.fos.md) - Event handler examples
- [NPCs Category](../categories/npcs.md) - All NPC-related scripts

---

[← Back to Tutorials](../index.md#tutorials) | [Next: Dialog Systems →](dialog-systems.md)
