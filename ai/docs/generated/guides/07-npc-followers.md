# Tutorial 7: NPC Followers

Learn how to create companion NPCs that follow and assist the player, including loyalty systems, combat assistance, and follower commands.

## What You'll Learn

- Understanding the follower system
- Creating a basic companion NPC
- Master-follower relationship
- Follower modes (Follow, Guard)
- Loyalty and behavior
- Combat assistance

## Prerequisites

- Completed [Tutorial 2: Working with NPCs](npc-tutorial.md)
- Understanding of [NPC AI Planes](npc-ai-planes.md)
- Familiarity with `follower.fos` and `follower_common.fos`

## Overview

The follower system allows NPCs to:
*   **Follow the player** across maps
*   **Assist in combat** based on attack policy
*   **Guard locations** when commanded
*   **Track loyalty** that affects behavior
*   **Respawn** after death (for companions)

**Follower Types**:
*   `FOLLOWER_TYPE_COMPANION` - Permanent companions (respawn)
*   `FOLLOWER_TYPE_SLAVE` - Enslaved followers
*   `FOLLOWER_TYPE_BRAHMIN` - Pack animals
*   `FOLLOWER_TYPE_DOG` - Animal companions

## Step 1: Basic Follower Setup

Every follower needs the follower system initialized via `FollowerBaseInit`.

### Minimal Follower Example

```angelscript
#include "_macros.fos"
#include "follower_h.fos"
#include "follower_common_h.fos"
#include "npc_planes_h.fos"

void critter_init(Critter& follower, bool firstTime)
{
    // Initialize follower system
    FollowerBaseInit(follower, firstTime);
    
    if(firstTime)
    {
        // Set as companion type
        follower.FollowerVarBase[FV_TYPE] = FOLLOWER_TYPE_COMPANION;
        
        // Set initial loyalty (0-100)
        follower.FollowerVarBase[FV_LOYALITY] = 100;
        
        // Set dialog for commands
        follower.StatBase[ST_DIALOG_ID] = DIALOG_companion_generic;
    }
}
```

**What `FollowerBaseInit` does**:
*   Sets up all follower event handlers (`_Idle`, `_ShowCritter`, `_Attacked`, etc.)
*   Initializes follower variables (mode, distance, attack policy)
*   Configures follower flags (`MODE_EXT_FOLLOWER`, `MODE_GECK`)
*   Starts loyalty update timer

## Step 2: Master-Follower Relationship

The follower tracks their master via `FV_MASTER`.

### Assigning a Master

```angelscript
import void MakeFollower(Critter& npc, uint type, string@ script, uint dialog, Critter& master, bool firstTime) from "follower_common";

// In a dialog result script
void r_HireCompanion(Critter& player, Critter@ npc)
{
    if(!valid(npc))
        return;
    
    // Make this NPC follow the player
    MakeFollower(npc, FOLLOWER_TYPE_COMPANION, "companion_script", DIALOG_companion_generic, player, true);
    
    player.Say(SAY_NETMSG, npc.Name + " is now following you.");
}
```

### Checking the Master

```angelscript
import Critter@ GetMaster(Critter& follower) from "follower";

void _FollowerIdle(Critter& follower)
{
    Critter@ master = GetMaster(follower);
    if(!valid(master))
    {
        // Master is gone or offline
        return;
    }
    
    // Check distance to master
    if(GetCrittersDistantion(follower, master) > 10)
    {
        // Too far, move closer
        GoToMaster(master, follower);
    }
}
```

## Step 3: Follower Modes

Followers have different behavior modes:

| Mode | Constant | Behavior |
|:-----|:---------|:---------|
| Follow | `FOLLOWMODE_FOLLOW` | Stays near master |
| Guard | `FOLLOWMODE_GUARD` | Stays at current position |
| Mine | `FOLLOWMODE_MINE` | Mining behavior (special) |

### Setting Mode via Dialog

```angelscript
// Dialog result: Set to Guard mode
void r_FollowMode(Critter& player, Critter@ follower, int mode)
{
    if(!valid(follower))
        return;
    
    follower.FollowerVarBase[FV_MODE] = mode;
    
    if(mode == FOLLOWMODE_GUARD)
    {
        follower.SetHomePos(follower.HexX, follower.HexY, follower.Dir);
        player.Say(SAY_NETMSG, follower.Name + " will guard this position.");
    }
    else if(mode == FOLLOWMODE_FOLLOW)
    {
        player.Say(SAY_NETMSG, follower.Name + " is following you again.");
    }
}
```

## Step 4: Attack Policy

Followers can be configured to attack different targets:

| Policy | Constant | Behavior |
|:-------|:---------|:---------|
| No one | `ATTACKPOLICY_NOONE` | Never attacks |
| Enemies | `ATTACKPOLICY_ENEMIES` | Attacks faction enemies |
| All | `ATTACKPOLICY_ALL` | Attacks anyone hostile |

### Setting Attack Policy

```angelscript
// Dialog result: Set attack policy
void r_AttackPolicy(Critter& player, Critter@ follower, int policy)
{
    if(!valid(follower))
        return;
    
    follower.FollowerVarBase[FV_ATTACK_POLICY] = policy;
    follower.FollowerVarBase[FV_FACTION] = GetGroupIndex(player);
    
    // Apply policy to nearby critters immediately
    array<Critter@> crits;
    uint num = player.GetCritters(false, FIND_LIFE_AND_KO, crits);
    for(uint i = 0; i < num; i++)
        _ShowCritter(follower, crits[i]);
}
```

## Step 5: Loyalty System

Loyalty (0-100) affects follower behavior:
*   **100**: Completely loyal, fights to the death
*   **50-99**: Normal behavior
*   **0-49**: May flee in combat
*   **0**: Will rebel (for slaves)

### Modifying Loyalty

```angelscript
import void ModifyLoyality(Critter& follower, int value) from "follower";

// Reward loyalty for good treatment
void r_IncreaseLoyality(Critter& player, Critter@ follower, int min, int max)
{
    if(!valid(follower))
        return;
    
    ModifyLoyality(follower, Random(min, max));
    player.Say(SAY_NETMSG, follower.Name + " seems more loyal.");
}

// Penalty for bad treatment
void _MasterAttackedFollower(Critter& follower, Critter& attacker)
{
    Critter@ master = GetMaster(follower);
    if(valid(master) && attacker.Id == master.Id)
    {
        // Master attacked us!
        ModifyLoyality(follower, -20);
    }
}
```

### Loyalty Decay

Loyalty automatically decreases over time (handled by `cte_UpdateLoyality`):

```angelscript
// From follower.fos
void UpdateLoyality(Critter& follower)
{
    // Decay: -5 to -15 per interval
    ModifyLoyality(follower, Random(-5, -15));
}
```

**Prevent decay**: Give the follower the "Master Speaker" perk to halve decay rate.

## Step 6: Combat Assistance

Followers automatically assist in combat based on their attack policy.

### Example: Follower Joins Combat

```angelscript
// From follower.fos - automatically called
void _ShowCritter(Critter& follower, Critter& target)
{
    int attack = follower.FollowerVar[FV_ATTACK_POLICY];
    
    if(attack == ATTACKPOLICY_NOONE)
        return;  // Pacifist
    
    // Check if target is an enemy
    if(IsFriend(follower, target))
        return;  // Don't attack friends
    
    if(attack == ATTACKPOLICY_ENEMIES)
    {
        // Attack faction enemies
        if(GetGroupsStatus(follower, target) == FACTION_ENEMY)
        {
            AddAttackPlane(follower, AI_PLANE_ATTACK_PRIORITY, target);
        }
    }
}
```

### Fleeing Based on Loyalty

```angelscript
// From follower.fos
int _PlaneRun(Critter& follower, NpcPlane& plane, int reason, uint& result0, uint& result1, uint& result2)
{
    if(plane.Type == AI_PLANE_ATTACK && reason == REASON_ATTACK_WEAPON)
    {
        uint percentage = 100 - follower.FollowerVar[FV_LOYALITY];
        int thresholdHp = (follower.Stat[ST_MAX_LIFE] * percentage) / 100;
        
        if(follower.Stat[ST_CURRENT_HP] < thresholdHp)
        {
            // Low HP and low loyalty = flee
            if(!Flee(follower))
                return PLANE_RUN_GLOBAL;
            return PLANE_DISCARD;
        }
    }
    return PLANE_RUN_GLOBAL;
}
```

## Complete Example: Simple Companion

Here's a complete companion NPC with dialog commands:

```angelscript
// companion_dog.fos
#include "_macros.fos"
#include "follower_h.fos"
#include "follower_common_h.fos"
#include "npc_common_h.fos"
#include "npc_planes_h.fos"

import void NpcSetLevel(Critter& npc, int level) from "parameters";

void critter_init(Critter& dog, bool firstTime)
{
    // Initialize follower system
    FollowerBaseInit(dog, firstTime);
    
    if(firstTime)
    {
        // Set type
        dog.FollowerVarBase[FV_TYPE] = FOLLOWER_TYPE_DOG;
        
        // Set stats
        NpcSetLevel(dog, 5);
        dog.StatBase[ST_BODY_TYPE] = BT_DOG;
        
        // Set loyalty
        dog.FollowerVarBase[FV_LOYALITY] = 100;
        
        // Set dialog
        dog.StatBase[ST_DIALOG_ID] = DIALOG_dog_companion;
        
        // Default behavior
        dog.FollowerVarBase[FV_MODE] = FOLLOWMODE_FOLLOW;
        dog.FollowerVarBase[FV_ATTACK_POLICY] = ATTACKPOLICY_ENEMIES;
        dog.FollowerVarBase[FV_DISTANCE] = DISTANCE_CLOSE;  // Stay close
        
        // Combat setup
        dog.SkillBase[SK_UNARMED] += 30;  // Good at biting
        dog.StatBase[ST_STRENGTH] += 1;
        dog.StatBase[ST_AGILITY] += 2;
    }
}
```

## Follower Commands via Dialog

Create a dialog with these common commands:

### Dialog Demands (d_ functions)

```angelscript
// Check if player is the owner
bool d_IsOwner(Critter& player, Critter@ follower, int val)
{
    return (player.Id == uint(follower.FollowerVar[FV_MASTER]));
}

// Check if following
bool d_IsFollowing(Critter& player, Critter@ follower, int val)
{
    return (follower.FollowerVar[FV_MODE] == FOLLOWMODE_FOLLOW);
}

// Check if guarding
bool d_IsGuarding(Critter& player, Critter@ follower, int val)
{
    return (follower.FollowerVar[FV_MODE] == FOLLOWMODE_GUARD);
}
```

### Dialog Results (r_ functions)

```angelscript
// Set to follow mode
void r_SetFollow(Critter& player, Critter@ follower)
{
    r_FollowMode(player, follower, FOLLOWMODE_FOLLOW);
}

// Set to guard mode
void r_SetGuard(Critter& player, Critter@ follower)
{
    r_FollowMode(player, follower, FOLLOWMODE_GUARD);
}

// Arm best weapon
void r_ArmBestWeapon(Critter& player, Critter@ follower)
{
    ArmBestWeapon(follower);
    player.Say(SAY_NETMSG, follower.Name + " equipped their best weapon.");
}

// Dismiss follower
void r_DismissFollower(Critter& player, Critter@ follower)
{
    DisbandFollower(player, follower, false);
    player.Say(SAY_NETMSG, follower.Name + " is no longer following you.");
}
```

## Common Issues

### 1. Follower doesn't follow
**Problem**: Follower stays in place.
**Solution**:
- Check `FV_MODE` is set to `FOLLOWMODE_FOLLOW`
- Ensure `FollowerBaseInit` was called
- Verify `MODE_GECK` is set (prevents map deletion)

### 2. Follower attacks allies
**Problem**: Follower attacks friendly NPCs.
**Solution**:
- Check `FV_ATTACK_POLICY` setting
- Ensure `FV_FACTION` matches master's faction
- Verify `IsFriend` logic in `_ShowCritter`

### 3. Follower disappears after death
**Problem**: Companion doesn't respawn.
**Solution**:
- Check `FV_TYPE` is `FOLLOWER_TYPE_COMPANION`
- Ensure `ST_REPLICATION_TIME` is set to `FOLLOWER_RESPAWN_TIME`
- Verify respawn location is configured

## Next Steps

- **[Tutorial 2F: Advanced Dialog Patterns](npc-dialog-advanced.md)** - Complex conversations
- **[Tutorial 3: Dialog Systems](dialog-systems.md)** - Create follower dialogs
- **[NPC AI Planes](npc-ai-planes.md)** - Advanced follower behavior

## Further Reading

- [follower.fos](../follower.fos.md) - Follower implementation
- [follower_common.fos](../follower_common.fos.md) - Follower utilities
- [follower_h.fos](../follower_h.fos.md) - Follower constants

---

[← Back: NPC Traders](npc-traders.md) | [Next: Advanced Dialogs →](npc-dialog-advanced.md)
