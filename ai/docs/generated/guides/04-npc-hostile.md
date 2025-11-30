# Tutorial 4: Hostile NPCs

Learn how to create a fully-equipped enemy NPC that attacks players, has proper stats and skills, uses weapons with unlimited ammo, and shouts battle cries.

## What You'll Learn

- Initializing NPC stats and skills
- Equipping NPCs with weapons and armor
- Setting unlimited ammo mode
- Creating hostile behavior
- Random battle shouts
- Complete enemy NPC example

## Prerequisites

- Completed [Tutorial 2: Working with NPCs](npc-tutorial.md)
- Understanding of basic event handlers
- Familiarity with `_macros.fos` and `_defines.fos`

## Overview

Creating a proper enemy NPC requires more than just making it attack players. You need to:
1. Set appropriate stats and skills for the NPC's level
2. Equip it with weapons and armor
3. Make weapons work with unlimited ammo
4. Add personality through battle cries
5. Implement proper combat behavior

## Step 1: Basic Hostile NPC Structure

Let's start with a basic raider NPC:

```angelscript
// hostile_raider.fos
// A hostile raider that attacks players on sight

#include "_macros.fos"
#include "npc_common_h.fos"
#include "npc_planes_h.fos"

// Import the level-setting function
import void NpcSetLevel(Critter& npc, int level) from "parameters";

void critter_init(Critter& raider, bool firstTime)
{
    // Set event handlers
    raider.SetEvent(CRITTER_EVENT_IDLE, "_RaiderIdle");
    raider.SetEvent(CRITTER_EVENT_SHOW_CRITTER, "_RaiderShowCritter");
    raider.SetEvent(CRITTER_EVENT_ATTACKED, "_RaiderAttacked");
    
    if(firstTime)
    {
    NpcSetLevel(raider, 15);
    
    // Optionally boost specific skills
    raider.SkillBase[SK_SMALL_GUNS] += 20;  // Better with guns
    raider.SkillBase[SK_UNARMED] += 15;     // Can fight unarmed
    raider.SkillBase[SK_OUTDOORSMAN] += 10; // Wasteland survivor
    
    // Adjust SPECIAL stats if needed
    raider.StatBase[ST_STRENGTH] += 1;      // Stronger
    raider.StatBase[ST_ENDURANCE] += 1;     // Tougher
    
    // Set home position
    raider.SetHomePos(raider.HexX, raider.HexY, raider.Dir);
    
    Log("Raider initialized at level " + raider.Stat[ST_LEVEL]);
    }
}
```

**What `NpcSetLevel` does:**
- Increases max HP based on level and endurance
- Boosts all skills by 5 points per level
- Automatically heals to full HP

## Step 3: Equipping Weapons and Armor

Add items to the NPC's inventory and equip them:

```angelscript
void InitializeRaider(Critter& raider)
{
    // Set level first
    NpcSetLevel(raider, 15);
    
    // === Add Weapon ===
    // Add a 10mm SMG
    Item@ weapon = raider.AddItem(PID_10MM_SMG, 1);
    if(valid(weapon))
    {
        // Move to hand slot
        raider.MoveItem(weapon.Id, 1, SLOT_HAND1);
        
        // Set as favorite weapon (will re-equip if dropped)
        raider.SetFavoriteItem(SLOT_HAND1, PID_10MM_SMG);
    }
    
    // === Add Armor ===
    Item@ armor = raider.AddItem(PID_LEATHER_ARMOR, 1);
    if(valid(armor))
    {
        // Equip armor
        raider.MoveItem(armor.Id, 1, SLOT_ARMOR);
    }
    
    // === Add Other Items ===
    raider.AddItem(PID_STIMPAK, Random(1, 3));      // Healing items
    raider.AddItem(PID_BOTTLE_CAPS, Random(10, 50)); // Loot
    raider.AddItem(PID_KNIFE, 1);                    // Backup weapon
    
    // === Set Unlimited Ammo ===
    raider.ModeBase[MODE_UNLIMITED_AMMO] = 1;
    
    Log("Raider equipped with " + weapon.GetProtoId());
}
```

**Important Notes:**
- `AddItem(PID, count)` - Adds item to inventory
- `MoveItem(itemId, count, slot)` - Moves item to specific slot
- `SLOT_HAND1` - Primary hand
- `SLOT_HAND2` - Secondary hand (for two-handed weapons or shields)
- `SLOT_ARMOR` - Armor slot
- `MODE_UNLIMITED_AMMO` - Never runs out of ammo

## Step 4: Hostile Behavior

Make the NPC attack players on sight:

```angelscript
void _RaiderShowCritter(Critter& raider, Critter& target)
{
    // Only attack players
    if(!target.IsPlayer())
        return;
    
    // Shout battle cry
    string[] battleCries = {
        "Die, wastelander!",
        "Your caps are mine!",
        "Time to die!",
        "I'll wear your skin!",
        "Fresh meat!",
        "No mercy!",
        "You picked the wrong road!"
    };
    
    raider.Say(SAY_SHOUT, battleCries[Random(0, 6)]);
    
    // Attack!
    AddAttackPlane(raider, AI_PLANE_ATTACK_PRIORITY, target);
}

void _RaiderAttacked(Critter& raider, Critter& attacker)
{
    // Fight back aggressively
    raider.Say(SAY_SHOUT, "You'll regret that!");
    AddAttackPlane(raider, AI_PLANE_ATTACK_PRIORITY, attacker);
}

void _RaiderIdle(Critter& raider)
{
    // Patrol or wander
    if(Random(0, 100) < 30)
    {
        MoveRandom(raider, 10, 3, false);
    }
    
    // Occasionally taunt
    if(Random(0, 500) == 0)
    {
        string[] taunts = {
            "Come out, come out...",
            "I smell fresh blood...",
            "Where are you hiding?"
        };
        raider.Say(SAY_NORM_ON_HEAD, taunts[Random(0, 2)]);
    }
    
    raider.Wait(Random(3000, 7000));
}
```

## Complete Example: Hostile Raider

Here's a complete, working hostile NPC script:

```angelscript
// hostile_raider.fos
// A fully-equipped hostile raider

#include "_macros.fos"
#include "npc_common_h.fos"
#include "npc_planes_h.fos"

import void NpcSetLevel(Critter& npc, int level) from "parameters";

// Battle cries (global arrays)
string[] g_BattleCries = {
    "Die, wastelander!",
    "Your caps are mine!",
    "Time to die!",
    "I'll wear your skin!",
    "Fresh meat!",
    "No mercy!",
    "You picked the wrong road!",
    "Say your prayers!",
    "This is raider territory!",
    "You're dead meat!"
};

string[] g_TauntMessages = {
    "Come out, come out...",
    "I smell fresh blood...",
    "Where are you hiding?",
    "Show yourself, coward!",
    "I'm gonna enjoy this..."
};

string[] g_DeathMessages = {
    "I'll... be... back...",
    "You got... lucky...",
    "Tell... my gang...",
    "Curse... you...",
    "Not... like this..."
};

void critter_init(Critter& raider, bool firstTime)
{
    // Set event handlers
    raider.SetEvent(CRITTER_EVENT_IDLE, "_RaiderIdle");
    raider.SetEvent(CRITTER_EVENT_SHOW_CRITTER, "_RaiderShowCritter");
    raider.SetEvent(CRITTER_EVENT_ATTACKED, "_RaiderAttacked");
    raider.SetEvent(CRITTER_EVENT_DEAD, "_RaiderDead");
    
    // Set view distance
    raider.ShowCritterDist1 = 15; // Can see 15 hexes away
    
    if(firstTime)
    {
        InitializeRaider(raider);
    }
}

void InitializeRaider(Critter& raider)
{
    // === Set Level and Skills ===
    NpcSetLevel(raider, Random(12, 18)); // Level 12-18
    
    // Boost combat skills
    raider.SkillBase[SK_SMALL_GUNS] += Random(15, 25);
    raider.SkillBase[SK_UNARMED] += Random(10, 20);
    raider.SkillBase[SK_MELEE_WEAPONS] += Random(10, 15);
    
    // Wasteland survival skills
    raider.SkillBase[SK_OUTDOORSMAN] += 10;
    raider.SkillBase[SK_FIRST_AID] += 5;
    
    // Adjust SPECIAL
    raider.StatBase[ST_STRENGTH] += Random(0, 2);
    raider.StatBase[ST_ENDURANCE] += Random(0, 2);
    raider.StatBase[ST_AGILITY] += Random(0, 1);
    
    // === Equipment ===
    // Choose random weapon
    uint[] weapons = {
        PID_10MM_SMG,
        PID_HUNTING_RIFLE,
        PID_SAWED_OFF_SHOTGUN,
        PID_DESERT_EAGLE,
        PID_14MM_PISTOL
    };
    uint weaponPid = weapons[Random(0, 4)];
    
    Item@ weapon = raider.AddItem(weaponPid, 1);
    if(valid(weapon))
    {
        raider.MoveItem(weapon.Id, 1, SLOT_HAND1);
        raider.SetFavoriteItem(SLOT_HAND1, weaponPid);
    }
    
    // Armor (random)
    uint[] armors = {
        PID_LEATHER_ARMOR,
        PID_LEATHER_JACKET,
        PID_METAL_ARMOR
    };
    uint armorPid = armors[Random(0, 2)];
    
    Item@ armor = raider.AddItem(armorPid, 1);
    if(valid(armor))
    {
        raider.MoveItem(armor.Id, 1, SLOT_ARMOR);
    }
    
    // Backup weapon
    raider.AddItem(PID_KNIFE, 1);
    
    // Consumables
    raider.AddItem(PID_STIMPAK, Random(1, 3));
    raider.AddItem(PID_BOTTLE_CAPS, Random(20, 100));
    
    // Random loot
    if(Random(0, 100) < 30) // 30% chance
    {
        raider.AddItem(PID_BEER, Random(1, 2));
    }
    
    // === Set Modes ===
    raider.ModeBase[MODE_UNLIMITED_AMMO] = 1; // Never runs out of ammo
    
    // Set home position
    raider.SetHomePos(raider.HexX, raider.HexY, raider.Dir);
    
    Log("Raider initialized: Level " + raider.Stat[ST_LEVEL] + 
        ", Weapon: " + weaponPid + ", Armor: " + armorPid);
}

void _RaiderShowCritter(Critter& raider, Critter& target)
{
    // Only attack players
    if(!target.IsPlayer())
        return;
    
    // Check if already attacking this target
    NpcPlane@ plane = raider.GetCurPlane();
    if(valid(plane) && plane.Type == AI_PLANE_ATTACK)
        return; // Already in combat
    
    // Shout battle cry
    raider.Say(SAY_SHOUT, g_BattleCries[Random(0, g_BattleCries.length() - 1)]);
    
    // Attack!
    AddAttackPlane(raider, AI_PLANE_ATTACK_PRIORITY, target);
}

void _RaiderAttacked(Critter& raider, Critter& attacker)
{
    // Aggressive response
    string[] responses = {
        "You'll regret that!",
        "Big mistake!",
        "You're dead!",
        "That's it, you're finished!"
    };
    
    raider.Say(SAY_SHOUT, responses[Random(0, 3)]);
    
    // Fight back
    AddAttackPlane(raider, AI_PLANE_ATTACK_PRIORITY, attacker);
}

void _RaiderIdle(Critter& raider)
{
    // Check health - flee if low
    int hp = raider.Stat[ST_CURRENT_HP];
    int maxHp = raider.Stat[ST_MAX_LIFE];
    
    if(hp < maxHp / 4) // Less than 25% HP
    {
        raider.Say(SAY_SHOUT, "Retreat! Retreat!");
        Flee(raider, true);
        return;
    }
    
    // Patrol behavior
    int action = Random(0, 100);
    
    if(action < 30)
    {
        // Wander around
        MoveRandom(raider, 15, 4, false);
    }
    else if(action < 35)
    {
        // Return to home
        uint bMap;
        uint16 bX = 0, bY = 0;
        uint8 bDir = 0;
        raider.GetHomePos(bMap, bX, bY, bDir);
        AddWalkPlane(raider, AI_PLANE_WALK_PRIORITY, bX, bY, bDir, false, 0);
    }
    
    // Occasional taunts
    if(Random(0, 500) == 0)
    {
        raider.Say(SAY_NORM_ON_HEAD, g_TauntMessages[Random(0, g_TauntMessages.length() - 1)]);
    }
    
    // Wait before next idle
    raider.Wait(Random(3000, 7000));
}

void _RaiderDead(Critter& raider, Critter@ killer)
{
    // Death speech
    raider.Say(SAY_NORM, g_DeathMessages[Random(0, g_DeathMessages.length() - 1)]);
    
    // Optional: Drop extra loot on death
    Map@ map = raider.GetMap();
    if(valid(map) && Random(0, 100) < 20) // 20% chance
    {
        // Drop bonus caps
        map.AddItem(raider.HexX, raider.HexY, PID_BOTTLE_CAPS, Random(50, 150));
    }
}
```

## Advanced: Different Enemy Types

### Melee Raider

```angelscript
void InitializeMeleeRaider(Critter& raider)
{
    NpcSetLevel(raider, 15);
    
    // Melee-focused skills
    raider.SkillBase[SK_MELEE_WEAPONS] += 30;
    raider.SkillBase[SK_UNARMED] += 25;
    
    // High strength and endurance
    raider.StatBase[ST_STRENGTH] += 2;
    raider.StatBase[ST_ENDURANCE] += 2;
    
    // Melee weapons
    Item@ weapon = raider.AddItem(PID_SLEDGEHAMMER, 1);
    if(valid(weapon))
    {
        raider.MoveItem(weapon.Id, 1, SLOT_HAND1);
        raider.SetFavoriteItem(SLOT_HAND1, PID_SLEDGEHAMMER);
    }
    
    // Heavy armor
    Item@ armor = raider.AddItem(PID_METAL_ARMOR, 1);
    if(valid(armor))
    {
        raider.MoveItem(armor.Id, 1, SLOT_ARMOR);
    }
}
```

### Sniper Raider

```angelscript
void InitializeSniperRaider(Critter& raider)
{
    NpcSetLevel(raider, 18);
    
    // Sniper skills
    raider.SkillBase[SK_SMALL_GUNS] += 40;
    raider.SkillBase[SK_PERCEPTION] += 2;
    
    // Sniper rifle
    Item@ weapon = raider.AddItem(PID_SNIPER_RIFLE, 1);
    if(valid(weapon))
    {
        raider.MoveItem(weapon.Id, 1, SLOT_HAND1);
        raider.SetFavoriteItem(SLOT_HAND1, PID_SNIPER_RIFLE);
    }
    
    // Light armor for mobility
    Item@ armor = raider.AddItem(PID_LEATHER_ARMOR, 1);
    if(valid(armor))
    {
        raider.MoveItem(armor.Id, 1, SLOT_ARMOR);
    }
    
    // Longer view distance
    raider.ShowCritterDist1 = 20;
}
```

## Common Weapon PIDs

```angelscript
// Pistols
PID_10MM_PISTOL
PID_DESERT_EAGLE
PID_14MM_PISTOL
PID_44_MAGNUM_REVOLVER

// SMGs
PID_10MM_SMG
PID_TOMMY_GUN
PID_GREASE_GUN

// Rifles
PID_HUNTING_RIFLE
PID_SNIPER_RIFLE
PID_ASSAULT_RIFLE
PID_FN_FAL

// Shotguns
PID_SAWED_OFF_SHOTGUN
PID_COMBAT_SHOTGUN

// Big Guns
PID_MINIGUN
PID_ROCKET_LAUNCHER
PID_FLAMER

// Melee
PID_KNIFE
PID_SPEAR
PID_SLEDGEHAMMER
PID_SUPER_SLEDGE

// Energy Weapons
PID_LASER_PISTOL
PID_PLASMA_PISTOL
PID_LASER_RIFLE
```

## Common Armor PIDs

```angelscript
PID_LEATHER_JACKET      // Light
PID_LEATHER_ARMOR       // Medium
PID_METAL_ARMOR         // Heavy
PID_COMBAT_ARMOR        // Very Heavy
PID_POWER_ARMOR         // Elite
```

## Tips and Best Practices

### 1. Balance Level and Equipment
- Level 10-15: Basic weapons (10mm pistol, hunting rifle)
- Level 15-20: Advanced weapons (assault rifle, combat shotgun)
- Level 20+: High-end weapons (sniper rifle, minigun)

### 2. Unlimited Ammo
Always set `MODE_UNLIMITED_AMMO` for NPCs, otherwise they'll run out quickly:
```angelscript
npc.ModeBase[MODE_UNLIMITED_AMMO] = 1;
```

### 3. Favorite Weapons
Set favorite weapons so NPCs re-equip them:
```angelscript
npc.SetFavoriteItem(SLOT_HAND1, PID_10MM_SMG);
```

### 4. Randomization
Add variety with random stats, equipment, and messages:
```angelscript
NpcSetLevel(npc, Random(12, 18));
uint weapon = weapons[Random(0, weapons.length() - 1)];
```

### 5. View Distance
Adjust how far NPCs can see:
```angelscript
npc.ShowCritterDist1 = 15; // Default is lower
```

## Exercises

### Exercise 1: Gang Leader
Create a tough gang leader with:
- Level 20
- Combat armor
- Assault rifle
- Extra HP (+50)
- Calls for backup when attacked

### Exercise 2: Ambush Group
Create 3 raiders that coordinate:
- When one spots a player, all attack
- Use SendMessage to alert each other
- Different weapon types (melee, ranged, sniper)

### Exercise 3: Boss Enemy
Create a boss enemy with:
- Level 25
- Power armor
- Minigun
- Double HP
- Special loot on death
- Unique battle cries

## Next Steps

- **[Tutorial 2C: NPC Reputation & Factions](npc-reputation.md)** - Faction-based behavior
- **[Tutorial 3: Dialog Systems](dialog-systems.md)** - Make NPCs talk
- **[Combat System Guide](combat-guide.md)** - Deep dive into combat mechanics

## Further Reading

- [parameters.fos](../parameters.fos.md) - NpcSetLevel implementation
- [guard.fos](../guard.fos.md) - Guard NPC examples
- [raiders_attack.fos](../raiders_attack.fos.md) - Raider implementation
- [Combat Category](../categories/combat.md) - Combat-related scripts

---

[← Back: Basic NPCs](npc-tutorial.md) | [Next: NPC Reputation →](npc-reputation.md)
