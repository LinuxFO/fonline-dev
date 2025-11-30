---
title: client_main.fos
description: " FOnline: 2238 Rotators  client_main.fos ..."
---

# client_main.fos


FOnline: 2238
Rotators

client_main.fos


## Includes

- `_client_defines.fos`
- `_macros.fos`
- `_colors.fos`
- `cheats_core_h.fos`
- `client_gui_barter.fos`
- `client_gui_elevator.fos`
- `config_file_h.fos`
- `prices_server_client.fos`
- `config_h.fos`
- `client_utils_h.fos`
- `client_access_h.fos`

## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| trader_levels | `array<int>` |  |  |
| item_prices_buy_modifier | `int` |  | int[] item_prices_base; // Cached item prices from server |
| item_prices_sell_modifier | `int` |  |  |
| isGMT | `bool` | `false` |  |
| accessControll | `IClientAccessLevelOpt@` |  |  |
| RepairPid | `uint16` | `0` |  |
| RepairItem | `uint` | `0` |  |

## Functions

### getParam_BonusLook

TODO: delete me!

```angelscript
int getParam_BonusLook(CritterCl& player, uint index)
```

### init

```angelscript
void init(int p0, int p1, int p2, string@ + p3, array<int>@ + p4)
```

### start

///////////////////////////////////////////////////////////////////////////////////////////////// Call on client loaded or new client_main.fos script received.

```angelscript
bool start()
```

### finish

```angelscript
void finish()
```

### loop

///////////////////////////////////////////////////////////////////////////////////////////////// Main loop function. Returned time of next call in milliseconds.

```angelscript
uint loop()
```

### get_elevator

```angelscript
bool get_elevator(uint type, array<uint>& data)
```

### _PingServer

```angelscript
void _PingServer(int a, int b, int c, string@ m, array<int>@ k)
```

### _PlaySound

```angelscript
void _PlaySound(int, int, int, string@ soundName, array<int>@)
```

### _PlayMusic

```angelscript
void _PlayMusic(int pos, int repeat, int, string@ musicName, array<int>@)
```

### _PlayVideo

```angelscript
void _PlayVideo(int canStop, int, int, string@ videoName, array<int>@)
```

### _FlushScreen

Effects, see effects.fos

```angelscript
void _FlushScreen(int fromColor, int toColor, int timeMs, string@, array<int>@)
```

### _QuakeScreen

```angelscript
void _QuakeScreen(int noise, int timeMs, int, string@, array<int>@)
```

### item_cost

///////////////////////////////////////////////////////////////////////////////////////////////// Call to determine cost of single item. To allow function set __CustomItemCost to true. Don't forgot specify this function in client script.

```angelscript
uint item_cost(ItemCl& item, CritterCl& chosen, CritterCl& npc, bool sell)
```

### check_perk

///////////////////////////////////////////////////////////////////////////////////////////////// Call to determine perk aviability.

```angelscript
bool check_perk(CritterCl& cr, uint perk)
```

### _ActionStealing

```angelscript
void _ActionStealing(int id, int, int, string@, array<int>@)
```

### _DisbandDone

```angelscript
void _DisbandDone(int num, int param2, int param3, string@ param4, array<int>@ param5)
```

### _ResetTimer

```angelscript
void _ResetTimer(int param1, int param2, int param3, string@ param4, array<int>@ param5)
```

### _BarterTraderLevels

Receive trader levels for barter

```angelscript
void _BarterTraderLevels(int param1, int param2, int param3, string@ param4, array<int>@ data)
```

### _BarterInit

Receive price + modifiers for barter

```angelscript
void _BarterInit(int buymodifier, int sellmodifier, int param2, string@ param3, array<int>@ data)
```

### _FreeFactionNames

```angelscript
void _FreeFactionNames(int, int, int, string@, array<int>@ list)
```

### _ShowBaseConstructionProgress

the info array contains: resource pid, count, required amount

```angelscript
void _ShowBaseConstructionProgress(int, int, int, string@, array<int>@ info)
```

### player_data_generate

///////////////////////////////////////////////////////////////////////////////////////////////// Call to calculate registration data. Input: 7 special, 3 tag skills, 2 traits, age, gender

```angelscript
void player_data_generate(array<int>& data)
```

### player_data_check

```angelscript
bool player_data_check(string& name, array<int>& data)
```

### SetRepairPid

```angelscript
void SetRepairPid(uint16 pid)
```

### SetRepairItem

```angelscript
void SetRepairItem(uint id)
```

### items_collection

///////////////////////////////////////////////////////////////////////////////////////////////// Called on some items collection generating. To force function call use RefreshItemsCollection(int collection) Collection constants see in Items collections _client_defines.fos If you want disable showing than just null pointer in collection

```angelscript
void items_collection(int collection, array<ItemCl@>& items)
```

### InitConfig

```angelscript
void InitConfig()
```

### _CC

```angelscript
void _CC(int c, int, int, string@, array<int>@)
```

### _SetChosenActions

```angelscript
void _SetChosenActions(int, int, int, string@, array<int>@ data)
```

### IsGMTEnabled

```angelscript
bool IsGMTEnabled()
```

### _OpenURL

```angelscript
void _OpenURL(int, int, int, string@ url, array<int>@)
```


