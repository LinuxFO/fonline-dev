# Tutorial 3: NPC AI & Behavior

Learn the AI Planes system - the core mechanism that controls NPC behavior in FOnline. This tutorial covers task priorities, plane types, and advanced NPC coordination.

## What You'll Learn

- Understanding the AI Planes system
- Plane types and priorities
- Creating patrol routes
- NPC coordination and messaging
- Advanced event handlers
- Guard behavior patterns

## Prerequisites

- Completed [Tutorial 2: Working with NPCs](npc-tutorial.md)
- Understanding of basic NPC event handlers
- Familiarity with `npc_planes_h.fos`

## Overview

The **AI Planes system** is how NPCs decide what to do. Think of planes as "tasks" in a priority queue - NPCs always execute the highest priority task first. This system is used in **105+ scripts** across the codebase.

**Why it matters:**
- Guards patrol and attack enemies
- Quest mobs coordinate attacks
- NPCs can multitask (walk, then attack, then return)
```angelscript
// Priority constants (from highest to lowest)
AI_PLANE_ATTACK_PRIORITY  = 10    // Combat
AI_PLANE_WALK_PRIORITY    = 5     // Movement
AI_PLANE_MISC_PRIORITY    = 3     // Custom behavior
```

**Example**: If an NPC has a walk plane (priority 5) and gets attacked, adding an attack plane (priority 10) will interrupt the walk.

### Plane Types

| Function | Plane Type | Purpose |
|:---------|:-----------|:--------|
| `AddWalkPlane` | Walk | Move to location |
| `AddAttackPlane` | Attack | Combat target |
| `AddMiscPlane` | Misc | Custom behavior |
| `AddPickPlane` | Pick | Pickup items |
| `AddHealCritterPlane` | Heal | Heal target |

## Step 1: Basic Plane Usage

### Walking to a Specific Location

```angelscript
void _GuardIdle(Critter& guard)
{
    // Walk to hex 100, 100
    AddWalkPlane(guard, AI_PLANE_WALK_PRIORITY, 100, 100, 0xFF, false, 0);
    
    guard.Wait(10000);
}
```

**Parameters explained:**
- `guard` - The NPC
- `AI_PLANE_WALK_PRIORITY` - Priority (5)
- `100, 100` - Target hex coordinates
- `0xFF` - Direction (0xFF = any direction)
- `false` - Walk (not run)
- `0` - Cut parameter (0 = normal pathfinding)

### Attacking a Target

```angelscript
void _GuardShowCritter(Critter& guard, Critter& target)
{
    if(target.IsPlayer() && IsEnemy(guard, target))
    {
        // Attack the player
        AddAttackPlane(guard, AI_PLANE_ATTACK_PRIORITY, target);
    }
}
```

### Custom Behavior with Misc Plane

```angelscript
void critter_init(Critter& npc, bool firstTime)
{
    npc.SetEvent(CRITTER_EVENT_IDLE, "_Idle");
    
    // Schedule custom function after 10 seconds
    AddMiscPlane(npc, AI_PLANE_MISC_PRIORITY, 10, "plane_CustomBehavior");
}

void plane_CustomBehavior(Critter& npc)
{
    npc.Say(SAY_NORM_ON_HEAD, "Time for my special behavior!");
    
    // Do something special
    npc.StatBase[ST_CURRENT_HP] = npc.Stat[ST_MAX_LIFE]; // Heal
}
```

## Step 2: Creating a Patrol Route

Let's create a guard that patrols between waypoints.

```angelscript
// patrol_guard.fos
#include "_macros.fos"
#include "npc_common_h.fos"
#include "npc_planes_h.fos"

// Waypoints (store in global arrays)
uint16[] g_PatrolX = {100, 120, 140, 120};
uint16[] g_PatrolY = {100, 110, 100, 90};

void critter_init(Critter& guard, bool firstTime)
{
    guard.SetEvent(CRITTER_EVENT_IDLE, "_PatrolIdle");
    guard.SetEvent(CRITTER_EVENT_PLANE_END, "_PatrolPlaneEnd");
    
    if(firstTime)
    {
        // Start at waypoint 0
        guard.SetAsInt(0, 0);
    }
}

void _PatrolIdle(Critter& guard)
{
    // Get current waypoint
    int waypoint = guard.GetAsInt(0);
    
    // Walk to current waypoint
    AddWalkPlane(guard, AI_PLANE_WALK_PRIORITY, 
                 g_PatrolX[waypoint], 
                 g_PatrolY[waypoint], 
                 0xFF, false, 0);
    
    guard.Wait(1000);
}

void _PatrolPlaneEnd(Critter& guard, int planeType, int reason, Critter@ someCr, Item@ someItem)
{
    if(planeType == AI_PLANE_WALK)
    {
        // Reached waypoint, move to next
        int waypoint = (guard.GetAsInt(0) + 1) % 4; // Loop back to 0 after 3
        guard.SetAsInt(0, waypoint);
        
        // Wait at waypoint
        guard.Wait(Random(3000, 7000));
    }
}
```

**Key Points:**
- `SetAsInt(0, value)` - Store data on the NPC (waypoint index)
- `CRITTER_EVENT_PLANE_END` - Triggered when a plane completes
- Modulo operator `%` - Loop waypoints (0, 1, 2, 3, 0, 1...)

## Step 3: Advanced Event Handlers

### CRITTER_EVENT_SHOW_CRITTER

Triggered when another critter enters view range.

```angelscript
void critter_init(Critter& guard, bool firstTime)
{
    guard.SetEvent(CRITTER_EVENT_SHOW_CRITTER, "_OnShowCritter");
    guard.ShowCritterDist1 = 10; // See critters up to 10 hexes away
}

void _OnShowCritter(Critter& guard, Critter& target)
{
    // Greet friendly players
    if(target.IsPlayer() && IsFriendly(guard, target))
    {
        guard.Say(SAY_NORM, "Hello, " + target.Name + "!");
    }
    // Attack enemies
    else if(IsEnemy(guard, target))
    {
        guard.Say(SAY_SHOUT, "Intruder detected!");
        AddAttackPlane(guard, AI_PLANE_ATTACK_PRIORITY, target);
    }
}
```

### CRITTER_EVENT_ATTACKED

Triggered when NPC is attacked.

```angelscript
void critter_init(Critter& npc, bool firstTime)
{
    npc.SetEvent(CRITTER_EVENT_ATTACKED, "_OnAttacked");
}

void _OnAttacked(Critter& npc, Critter& attacker)
{
    // Call for help
    npc.Say(SAY_SHOUT, "Help! I'm under attack!");
    
    // Alert nearby allies
    array<Critter@> allies;
    npc.GetCritters(false, FIND_LIFE_AND_KO | FIND_ONLY_NPC, allies);
    
    for(uint i = 0; i < allies.length(); i++)
    {
        if(GetCrittersDistantion(npc, allies[i]) < 15)
        {
            // Send message to ally
            allies[i].SendMessage(MSG_ATTACK, npc.Id, attacker.Id);
        }
    }
    
    // Fight back
    AddAttackPlane(npc, AI_PLANE_ATTACK_PRIORITY, attacker);
}
```

### CRITTER_EVENT_DEAD

Triggered when NPC dies.

```angelscript
void critter_init(Critter& npc, bool firstTime)
{
    npc.SetEvent(CRITTER_EVENT_DEAD, "_OnDead");
}

void _OnDead(Critter& npc, Critter@ killer)
{
    // Death speech
    if(valid(killer) && killer.IsPlayer())
    {
        npc.Say(SAY_NORM, "You... will... pay...");
    }
    
    // Drop special loot
    Map@ map = npc.GetMap();
    if(valid(map) && Random(0, 100) < 20) // 20% chance
    {
        map.AddItem(npc.HexX, npc.HexY, PID_BOTTLE_CAPS, Random(50, 100));
    }
    
    // Update quest counter
    if(valid(killer) && killer.IsPlayer())
    {
        killer.StatBase[ST_VAR0]++; // Increment kill counter
    }
}
```

## Step 4: NPC Communication

NPCs can send messages to each other for coordination.

### Message Types

```angelscript
// Common message types
#define MSG_ATTACK        1  // Under attack
#define MSG_ENEMY_SPOTTED 2  // Enemy seen
#define MSG_HELP_NEEDED   3  // Need assistance
#define MSG_RETREAT       4  // Fall back
```

### Sending Messages

```angelscript
void _OnShowCritter(Critter& scout, Critter& enemy)
{
    if(enemy.IsPlayer())
    {
        // Alert all nearby allies
        array<Critter@> allies;
        scout.GetCritters(false, FIND_LIFE_AND_KO | FIND_ONLY_NPC, allies);
        
        for(uint i = 0; i < allies.length(); i++)
        {
            if(GetCrittersDistantion(scout, allies[i]) < 20)
            {
                allies[i].SendMessage(MSG_ENEMY_SPOTTED, scout.Id, enemy.Id);
            }
        }
    }
}
```

### Receiving Messages

```angelscript
void critter_init(Critter& guard, bool firstTime)
{
    guard.SetEvent(CRITTER_EVENT_MESSAGE, "_OnMessage");
}

void _OnMessage(Critter& guard, Critter& fromCr, int message, int value)
{
    if(message == MSG_ENEMY_SPOTTED)
    {
        Critter@ enemy = GetCritter(value);
        if(valid(enemy))
        {
            guard.Say(SAY_SHOUT, "On my way!");
            AddAttackPlane(guard, AI_PLANE_ATTACK_PRIORITY, enemy);
        }
    }
    else if(message == MSG_ATTACK)
    {
        Critter@ attacker = GetCritter(value);
        if(valid(attacker))
        {
            guard.Say(SAY_SHOUT, "Coming to help!");
            AddAttackPlane(guard, AI_PLANE_ATTACK_PRIORITY, attacker);
        }
    }
}
```

## Complete Example: Town Guard

Based on `generic_guard.fos` from the codebase:

```angelscript
// town_guard.fos
#include "_macros.fos"
#include "groups_h.fos"
#include "npc_common_h.fos"
#include "npc_planes_h.fos"
#include "reputations_h.fos"

void critter_init(Critter& guard, bool firstTime)
{
    guard.SetEvent(CRITTER_EVENT_IDLE, "_GuardIdle");
    guard.SetEvent(CRITTER_EVENT_SHOW_CRITTER, "_GuardShowCritter");
    guard.SetEvent(CRITTER_EVENT_ATTACKED, "_GuardAttacked");
    
    // Set view distance
    guard.ShowCritterDist1 = 5;
    
    // Mark as guard
    _CritSetExtMode(guard, MODE_EXT_GUARD);
    
    if(firstTime)
    {
        // Set level and equipment
        NpcSetLevel(guard, 15);
        ArmBestWeapon(guard);
    }
}

void _GuardShowCritter(Critter& guard, Critter& target)
{
    // Attack faction enemies
    if(GetGroupsStatus(target, guard) == FACTION_ENEMY)
    {
        guard.Say(SAY_SHOUT, "Enemy spotted!");
        AddAttackPlane(guard, AI_PLANE_ATTACK_PRIORITY, target);
        return;
    }
    
    // Check player reputation
    if(target.IsPlayer())
    {
        int reputation = target.Reputation[_GroupIndex(guard)];
        
        if(reputation < __ReputationHated)
        {
            // Hated - attack on sight
            if(Random(-2000, -1500) >= reputation)
            {
                guard.Say(SAY_SHOUT, "You're not welcome here!");
                AddAttackPlane(guard, AI_PLANE_ATTACK_PRIORITY, target);
            }
        }
        else if(reputation < -1000)
        {
            // Disliked - warn them
            if(Random(1, 25) == 1)
            {
                guard.Say(SAY_NORM_ON_HEAD, 
                         target.Name + ". We're watching you, scum.");
            }
        }
    }
}

void _GuardIdle(Critter& guard)
{
    // Check for armed criminals nearby
    array<Critter@> players;
    guard.GetCritters(false, FIND_LIFE | FIND_ONLY_PLAYERS, players);
    
    for(uint i = 0; i < players.length(); i++)
    {
        if(GetCrittersDistantion(guard, players[i]) > 5)
            continue;
        
        // Only check disliked players
        if(players[i].Reputation[_GroupIndex(guard)] > -1000)
            continue;
        
        // Check if armed
        Item@ weapon = _CritGetItemHand(players[i]);
        if(valid(weapon) && weapon.GetType() == ITEM_TYPE_WEAPON)
        {
            guard.Say(SAY_SHOUT_ON_HEAD, "Put down your weapon, NOW!");
            
            // Give them 5 seconds to comply
            int[] data = {players[i].Id, guard.Id};
            CreateTimeEvent(AFTER(REAL_SECOND(5)), "e_CheckWeapon", data, false);
        }
    }
    
    guard.Wait(Random(3000, 7000));
}

void _GuardAttacked(Critter& guard, Critter& attacker)
{
    // Call for backup
    guard.Say(SAY_SHOUT, "Guards! To me!");
    
    array<Critter@> guards;
    guard.GetCritters(false, FIND_LIFE_AND_KO | FIND_ONLY_NPC, guards);
    
    for(uint i = 0; i < guards.length(); i++)
    {
        if(_CritHasExtMode(guards[i], MODE_EXT_GUARD))
        {
            guards[i].SendMessage(MSG_ATTACK, guard.Id, attacker.Id);
        }
    }
    
    // Fight back
    AddAttackPlane(guard, AI_PLANE_ATTACK_PRIORITY, attacker);
}

uint e_CheckWeapon(array<uint>@ values)
{
    Critter@ player = GetCritter(values[0]);
    Critter@ guard = GetCritter(values[1]);
    
    if(!valid(player) || !valid(guard))
        return 0;
    
    Item@ weapon = _CritGetItemHand(player);
    if(valid(weapon) && weapon.GetType() == ITEM_TYPE_WEAPON)
    {
        // Still armed - attack!
        guard.Say(SAY_SHOUT, "You were warned!");
        AddAttackPlane(guard, AI_PLANE_ATTACK_PRIORITY, player);
    }
    
    return 0;
}
```

## Managing Planes

### Dropping All Planes

```angelscript
// Cancel all current tasks
npc.DropPlanes();
```

### Erasing Specific Planes

```angelscript
// Stop attacking a specific target
EraseAttackPlane(npc, AI_PLANE_ATTACK_PRIORITY, target);
```

### Checking Current Plane

```angelscript
NpcPlane@ plane = npc.GetCurPlane();
if(valid(plane))
{
    // NPC is busy with a task
    int planeType = plane.Type;
    int priority = plane.Priority;
}
```

## Common Patterns

### Pattern 1: Interrupt and Resume

```angelscript
void _OnAttacked(Critter& npc, Critter& attacker)
{
    // Save current activity
    NpcPlane@ currentPlane = npc.GetCurPlane();
    
    // Fight
    AddAttackPlane(npc, AI_PLANE_ATTACK_PRIORITY, attacker);
    
    // After combat, resume previous activity
    // (handled automatically by priority system)
}
```

### Pattern 2: Conditional Behavior

```angelscript
void _Idle(Critter& npc)
{
    int hp = npc.Stat[ST_CURRENT_HP];
    int maxHp = npc.Stat[ST_MAX_LIFE];
    
    if(hp < maxHp / 3)
    {
        // Low health - flee
        Flee(npc, true);
    }
    else if(hp < maxHp / 2)
    {
        // Medium health - defensive
        PutAwayItems(npc);
        MoveRandom(npc, 5, 2, false);
    }
    else
    {
        // Full health - aggressive patrol
        MoveRandom(npc, 15, 5, false);
    }
    
    npc.Wait(Random(3000, 7000));
}
```

## Exercises

### Exercise 1: Chase Behavior
Create an NPC that chases players who get too close, but gives up after 20 hexes.

**Hint**: Use `AddWalkPlane` with player's position, check distance in idle.

### Exercise 2: Pack Coordination
Create 3 NPCs that coordinate attacks - when one is attacked, all attack the attacker.

**Hint**: Use `SendMessage` and `CRITTER_EVENT_MESSAGE`.

### Exercise 3: Smart Patrol
Create a guard that patrols, but interrupts patrol to investigate players, then resumes.

**Hint**: Use `CRITTER_EVENT_PLANE_END` and store patrol state.

## Next Steps

- **[Tutorial 2B: Creating Hostile NPCs](npc-hostile.md)** - Create enemies and guards
- **[Tutorial 2C: NPC Reputation & Factions](npc-reputation.md)** - Faction-based behavior
- **[Tutorial 3: Dialog Systems](dialog-systems.md)** - Make NPCs talk
- **[Common Patterns Cookbook](patterns-cookbook.md)** - Quick recipes

## Further Reading

- [npc_planes_h.fos](../npc_planes_h.fos.md) - AI plane functions
- [generic_guard.fos](../generic_guard.fos.md) - Guard implementation
- [NPCs Category](../categories/npcs.md) - All NPC scripts

---

[← Back: Basic NPCs](npc-tutorial.md) | [Next: Hostile NPCs →](npc-hostile.md)
