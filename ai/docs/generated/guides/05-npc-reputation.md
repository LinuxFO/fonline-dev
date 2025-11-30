# Tutorial 5: NPC Reputation & Factions

Learn how to use the FOnline reputation system to create complex faction relationships and dynamic NPC reactions.

## What You'll Learn

- Understanding the Faction & Reputation system
- Setting up NPC factions
- Modifying player reputation
- Creating faction-based reactions
- Using `reputations_h.fos` and `groups_h.fos`

## Prerequisites

- Completed [Tutorial 2A: NPC AI Planes](npc-ai-planes.md)
- Familiarity with `_groups.fos` (or `groups_h.fos`)

## Overview

The reputation system determines how NPCs react to players and other NPCs. It's built on two core concepts:
1.  **Factions (Teams)**: Every NPC belongs to a faction (Team ID).
2.  **Reputation**: A numerical value representing how much a faction likes or dislikes a player.

## Step 1: Assigning Factions

Every NPC has a `ST_TEAM_ID` stat that determines their faction.

### Common Factions
Defined in `groups_h.fos`:

```angelscript
#define FACTION_NONE                    (1)
#define FACTION_BOS                     (2)
#define FACTION_ENCLAVE                 (3)
#define FACTION_NCR                     (5)
#define FACTION_RAIDERS                 (7)
#define FACTION_VAULT_CITY              (6)
```

### Setting Faction in Script

```angelscript
void critter_init(Critter& npc, bool firstTime)
{
    if(firstTime)
    {
        // Set NPC as a member of the Brotherhood of Steel
        npc.StatBase[ST_TEAM_ID] = FACTION_BOS;
        
        // Optional: Set rank (1=Initiate, 4=Elder)
        npc.StatBase[ST_FACTION_RANK] = 2;
    }
}
```

## Step 2: Checking Reputation

You can check how a faction feels about a player using `GetGroupsStatus` or by checking the reputation value directly.

### Reputation Values
- **Ally**: > 1000
- **Neutral**: -1000 to 1000
- **Enemy**: < -1000

### Using GetGroupsStatus

```angelscript
#include "reputations_h.fos"

void _GuardShowCritter(Critter& guard, Critter& target)
{
    if(target.IsPlayer())
    {
        int status = GetGroupsStatus(guard, target);
        
        if(status == FACTION_ENEMY)
        {
            // Attack enemies
            guard.Say(SAY_SHOUT, "Enemy of the Brotherhood!");
            AddAttackPlane(guard, AI_PLANE_ATTACK_PRIORITY, target);
        }
        else if(status == FACTION_ALLY)
        {
            // Greet allies
            guard.Say(SAY_NORM, "Ad Victoriam, brother.");
        }
    }
}
```

### Checking Specific Reputation

You can check the raw reputation value for more granular reactions.

```angelscript
void _MerchantIdle(Critter& merchant)
{
    // Get nearby player
    Critter@ player = GetNearbyPlayer(merchant);
    if(!valid(player)) return;
    
    // Check reputation with Merchant's faction
    int rep = player.Reputation[merchant.Stat[ST_TEAM_ID]];
    
    if(rep > 500)
    {
        merchant.Say(SAY_NORM, "Good to see you again, friend!");
    }
    else if(rep < -500)
    {
        merchant.Say(SAY_NORM, "I've heard bad things about you...");
    player.Say(SAY_NETMSG, "You gained reputation with " + GetFactionName(questGiver.Stat[ST_TEAM_ID]));
}
```

### Removing Reputation

```angelscript
import void SubReputation(Critter@ cr, uint index, int val) from "reputations";

void _GuardAttacked(Critter& guard, Critter& attacker)
{
    if(attacker.IsPlayer())
    {
        // Major penalty for attacking a guard
        SubReputation(attacker, guard.Stat[ST_TEAM_ID], 500);
    }
}
```

## Step 4: Faction Relations

Factions can have relationships with each other (e.g., BOS hates Enclave). This is usually defined in `reputations_modifiers.fos` or similar configuration files, but you can check it in script.

```angelscript
void _OnShowCritter(Critter& npc, Critter& target)
{
    // Check if the target's faction is an enemy of my faction
    if(GetGroupsStatus(npc.Stat[ST_TEAM_ID], target.Stat[ST_TEAM_ID]) == FACTION_ENEMY)
    {
        AddAttackPlane(npc, AI_PLANE_ATTACK_PRIORITY, target);
    }
}
```

## Complete Example: Faction Recruiter

Here is an NPC that recruits players into a faction if their reputation is high enough.

```angelscript
// faction_recruiter.fos
#include "_macros.fos"
#include "reputations_h.fos"

#define MY_FACTION      FACTION_NCR
#define MIN_REP_JOIN    500

void critter_init(Critter& npc, bool firstTime)
{
    npc.StatBase[ST_TEAM_ID] = MY_FACTION;
    npc.SetEvent(CRITTER_EVENT_TALK, "_OnTalk");
}

bool _OnTalk(Critter& npc, Critter& player, bool attach, uint talkCount)
{
    int rep = player.Reputation[MY_FACTION];
    
    if(rep >= MIN_REP_JOIN)
    {
        npc.Say(SAY_NORM, "You've done good work for the NCR. Ready to join?");
        return true; // Open dialog
    }
    else if(rep < 0)
    {
        npc.Say(SAY_NORM, "Get lost, troublemaker.");
        return false; // Don't talk
    }
    else
    {
        npc.Say(SAY_NORM, "Prove yourself first, then we'll talk.");
        return false;
    }
}
```

## Common Issues

### 1. Reputation not updating
**Problem**: `AddReputation` doesn't seem to change the value.
**Solution**: Check if the reputation is capped. Some functions have a cap parameter.

### 2. NPC attacking allies
**Problem**: Guard attacks players with high reputation.
**Solution**: Check `GetGroupsStatus` logic. Ensure `ST_TEAM_ID` is set correctly on the NPC.

## Next Steps

- **[Tutorial 3: Dialog Systems](dialog-systems.md)** - Create complex dialog trees
- **[Tutorial 4: Quest Systems](quest-basics.md)** - Create quests that affect reputation

## Further Reading

- [reputations_h.fos](../reputations_h.fos.md)
- [groups_h.fos](../groups_h.fos.md)
