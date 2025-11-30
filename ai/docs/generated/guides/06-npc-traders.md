# Tutorial 6: NPC Traders

Learn how to create trading NPCs integrated with the FOnline economy system, including inventory management, price modifiers, and custom barter logic.

## What You'll Learn

- Setting up a basic trader NPC
- Configuring trader inventory levels
- Understanding price modifiers (barter skill, reputation)
- Trader inventory refresh cycles
- Custom barter logic and restrictions
- Complete trader examples

## Prerequisites

- Completed [Tutorial 2: Working with NPCs](npc-tutorial.md)
- Understanding of [NPC Reputation](npc-reputation.md)
- Familiarity with `economy.fos` and `trader.fos`

## Overview

Traders are NPCs that buy and sell items to players. The FOnline economy system automatically handles:
*   **Price Calculation**: Based on barter skill and reputation
*   **Inventory Management**: Automatic refresh and capacity limits
*   **Item Levels**: Traders stock items appropriate to their "level"

## Step 1: Basic Trader Setup

Every trader needs three things:
1.  `MODE_EXT_TRADER` - Marks the NPC as a trader
2.  `CRITTER_EVENT_BARTER` - Handles barter interactions
3.  Trader levels configuration

### Minimal Trader Example

```angelscript
#include "_macros.fos"
#include "economy_h.fos"
#include "trader_h.fos"

import void SetTraderLevels(Critter@ npc, array<uint>& levels) from "economy";

void critter_init(Critter& trader, bool firstTime)
{
    // Set barter event
    trader.SetEvent(CRITTER_EVENT_BARTER, "_OnBarter");
    
    if(firstTime)
    {
        // Mark as trader
        _CritSetExtMode(trader, MODE_EXT_TRADER);
        _CritUnsetMode(trader, MODE_NO_BARTER);
        _CritSetMode(trader, MODE_NO_STEAL);
        
        // Set barter skill
        trader.SkillBase[SK_BARTER] = 75;
        
        // Configure inventory (explained below)
        uint[] levels = {1, 1, 0, 1, 0, 0, 1};
        SetTraderLevels(trader, levels);
        
        // Start inventory refresh cycle
        CreateTimeEvent(AFTER(TRADER_UPDATE_TIME), "e_Update", trader.Id, false);
    }
}

bool _OnBarter(Critter& trader, Critter& player, bool attach, uint barterCount)
{
    if(!attach)
        return false;
    
    // Send price modifiers to client
    player.RunClientScript("_BarterInit", 
                          GetItemBuyModifier(player, trader), 
                          GetItemSellModifier(player, trader), 
                          0, "", null);
    player.RunClientScript("_BarterTraderLevels", 
                          0, 0, 0, "", GetTraderLevels(trader));
    return true;
}
```

## Step 2: Trader Levels

Trader levels determine what items the trader stocks. There are **7 item categories**:

| Index | Category | Examples |
|:------|:---------|:---------|
| 0 | Small Guns | Pistols, SMGs, Rifles |
| 1 | Big Guns | Miniguns, Rocket Launchers |
| 2 | Energy Weapons | Laser/Plasma weapons |
| 3 | Armor | Leather, Metal, Combat Armor |
| 4 | Drugs | Stimpaks, Buffout |
| 5 | Medicine | Doctor's Bags, First Aid Kits |
| 6 | Misc | Tools, Ammo, General goods |

### Level Values

Each category can have a level from **0 to 3**:
*   **0** = Does not stock this category
*   **1** = Low-tier items (cheap, common)
*   **2** = Mid-tier items (moderate quality)
*   **3** = High-tier items (expensive, rare)

### Example Configurations

```angelscript
// General Store - Misc goods and basic weapons
uint[] generalStore = {
    1,  // Small Guns: Level 1 (10mm pistol, hunting rifle)
    0,  // Big Guns: None
    0,  // Energy: None
    1,  // Armor: Level 1 (leather jacket)
    1,  // Drugs: Level 1 (stimpaks)
    0,  // Medicine: None
    2   // Misc: Level 2 (lots of general goods)
};

// Weapon Specialist - High-end guns
uint[] weaponShop = {
    3,  // Small Guns: Level 3 (sniper rifle, assault rifle)
    2,  // Big Guns: Level 2 (minigun)
    0,  // Energy: None
    0,  // Armor: None
    0,  // Drugs: None
    0,  // Medicine: None
    0   // Misc: None
};

// Doctor - Medical supplies only
uint[] doctor = {
    0,  // Small Guns: None
    0,  // Big Guns: None
    0,  // Energy: None
    0,  // Armor: None
    2,  // Drugs: Level 2 (good stimpaks, drugs)
    2,  // Medicine: Level 2 (doctor's bags)
    0   // Misc: None
};
```

## Step 3: Price Modifiers

Prices are automatically adjusted based on two factors:

### 1. Barter Skill

The trader's barter skill vs. the player's barter skill affects prices.

```angelscript
// From economy.fos
int GetBaseModifier(Critter& player, Critter& trader, bool buy)
{
    int barter_factor = buy ? 
        ((trader.Skill[SK_BARTER] * 25) / player.Skill[SK_BARTER]) : 
        ((player.Skill[SK_BARTER] * 25) / trader.Skill[SK_BARTER]);
    barter_factor = CLAMP(barter_factor, 0, 25);
    
    // ... reputation factor ...
    
    if(buy)
        return 150 + barter_factor - rep_factor;  // Player buying
    else
        return 25 + barter_factor + rep_factor;   // Player selling
}
```

**Higher trader barter skill = Worse prices for player**

### 2. Reputation

Player reputation with the trader's faction affects prices (see [NPC Reputation](npc-reputation.md)).

*   **Good reputation** (-1000 to +1000): Better prices
*   **Bad reputation**: Worse prices

## Step 4: Inventory Refresh

Traders automatically refresh their inventory periodically. The refresh cycle is defined in `trader_h.fos`:

```angelscript
#define TRADER_UPDATE_TIME (REAL_MINUTE(Random(30, 90)))  // 30-90 real minutes
```

The `e_Update` event:
*   Removes old items (based on trader level and time)
*   Adds new items (based on trader capacity)
*   Logs changes to `logs/traders.log`

You don't need to implement this yourself - it's handled by the standard `e_Update` function in `trader.fos`.

## Step 5: Custom Barter Logic

You can add custom conditions to the barter event.

### Example: Refuse Trade Based on Reputation

```angelscript
bool _OnBarter(Critter& trader, Critter& player, bool attach, uint barterCount)
{
    if(!attach)
        return false;
    
    // Check reputation
    int rep = player.Reputation[trader.Stat[ST_TEAM_ID]];
    if(rep < -500)
    {
        trader.Say(SAY_NORM, "I don't trade with scum like you.");
        return false;  // Cancel barter
    }
    
    // Standard barter logic
    player.RunClientScript("_BarterInit", 
                          GetItemBuyModifier(player, trader), 
                          GetItemSellModifier(player, trader), 
                          0, "", null);
    player.RunClientScript("_BarterTraderLevels", 
                          0, 0, 0, "", GetTraderLevels(trader));
    return true;
}
```

### Example: Special Discount

```angelscript
bool _OnBarter(Critter& trader, Critter& player, bool attach, uint barterCount)
{
    if(!attach)
        return false;
    
    int buyMod = GetItemBuyModifier(player, trader);
    int sellMod = GetItemSellModifier(player, trader);
    
    // VIP discount
    if(player.Stat[ST_VAR0] == 1)  // VIP flag
    {
        buyMod = (buyMod * 90) / 100;  // 10% discount on buying
        sellMod = (sellMod * 110) / 100; // 10% bonus on selling
        trader.Say(SAY_NORM, "Ah, a VIP customer! Special prices for you.");
    }
    
    player.RunClientScript("_BarterInit", buyMod, sellMod, 0, "", null);
    player.RunClientScript("_BarterTraderLevels", 0, 0, 0, "", GetTraderLevels(trader));
    return true;
}
```

## Complete Example: Weapon Merchant

Here's a complete weapon merchant with high barter skill and mid-tier inventory:

```angelscript
// weapon_merchant.fos
#include "_macros.fos"
#include "economy_h.fos"
#include "trader_h.fos"
#include "reputations_h.fos"

import void SetTraderLevels(Critter@ npc, array<uint>& levels) from "economy";

void critter_init(Critter& merchant, bool firstTime)
{
    merchant.SetEvent(CRITTER_EVENT_BARTER, "_OnBarter");
    
    if(firstTime)
    {
        // Trader setup
        _CritSetExtMode(merchant, MODE_EXT_TRADER);
        _CritUnsetMode(merchant, MODE_NO_BARTER);
        _CritSetMode(merchant, MODE_NO_STEAL);
        _CritSetMode(merchant, MODE_DLG_SCRIPT_BARTER);
        
        // High barter skill (tough negotiator)
        merchant.SkillBase[SK_BARTER] = 120;
        
        // Set faction (for reputation)
        merchant.StatBase[ST_TEAM_ID] = FACTION_NCR;
        
        // Configure inventory
        // Small Guns: 2, Big Guns: 1, Energy: 0, Armor: 0, Drugs: 0, Medicine: 0, Misc: 1
        uint[] levels = {2, 1, 0, 0, 0, 0, 1};
        SetTraderLevels(merchant, levels);
        
        // Start refresh cycle
        CreateTimeEvent(AFTER(TRADER_UPDATE_TIME), "e_Update", merchant.Id, false);
    }
}

bool _OnBarter(Critter& merchant, Critter& player, bool attach, uint barterCount)
{
    if(!attach)
        return false;
    
    // Check reputation with NCR
    int rep = player.Reputation[FACTION_NCR];
    
    if(rep < -1000)
    {
        merchant.Say(SAY_NORM, "NCR doesn't trade with enemies.");
        return false;
    }
    
    // Friendly greeting for allies
    if(rep > 500)
    {
        merchant.Say(SAY_NORM, "Good to see you, friend. Take a look at my stock.");
    }
    
    // Send price modifiers
    player.RunClientScript("_BarterInit", 
                          GetItemBuyModifier(player, merchant), 
                          GetItemSellModifier(player, merchant), 
                          0, "", null);
    player.RunClientScript("_BarterTraderLevels", 
                          0, 0, 0, "", GetTraderLevels(merchant));
    return true;
}
```

## Common Issues

### 1. Trader has no items
**Problem**: Trader inventory is empty.
**Solution**:
- Check that `SetTraderLevels` is called
- Ensure at least one level is > 0
- Verify `e_Update` event is created

### 2. Prices don't change with reputation
**Problem**: Reputation doesn't affect prices.
**Solution**:
- Ensure `ST_TEAM_ID` is set on the trader
- Check that the faction index is valid
- Verify player has reputation with that faction

### 3. Barter window won't open
**Problem**: Clicking "Barter" does nothing.
**Solution**:
- Check `MODE_EXT_TRADER` is set
- Ensure `MODE_NO_BARTER` is unset
- Verify `CRITTER_EVENT_BARTER` is registered

## Next Steps

- **[Tutorial 2E: NPC Followers](npc-followers.md)** - Companion system
- **[Tutorial 3: Dialog Systems](dialog-systems.md)** - Create trader dialogs
- **[Quest Basics](quest-basics.md)** - Quest rewards with traders

## Further Reading

- [trader.fos](../trader.fos.md) - Trader implementation
- [economy.fos](../economy.fos.md) - Price calculation
- [economy_h.fos](../economy_h.fos.md) - Economy functions

---

[← Back: NPC Reputation](npc-reputation.md) | [Next: NPC Followers →](npc-followers.md)
