---
title: client_interface.fos
description: " FOnline: 2238 Rotators  client_interface.fos ..."
---

# client_interface.fos


FOnline: 2238
Rotators

client_interface.fos


## Includes

- `_client_defines.fos`
- `_client_maps.fos`
- `_defines.fos`
- `_macros.fos`
- `_colors.fos`
- `_basetypes.fos`
- `buffer_h.fos`
- `client_gui_h.fos`
- `groups_h.fos`
- `lexems_h.fos`
- `MsgStr.h`
- `polygon_h.fos`
- `polygon_towns.fos`
- `prod_ingredients_h.fos`
- `client_interface_h.fos`
- `combat_h.fos`
- `item_dogtags_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __CLIENT_INTERFACE__ |  |  |
| IsGM | `IsGMTEnabled() && GMToolsAccess` |  |
| AW_COLOR_ARMOR | `COLOR_DGREEN` |  |
| AW_COLOR_HEADGEAR | `COLOR_DGREEN` |  |
| AW_COLOR_WEAPON | `COLOR_LGREEN` |  |
| AW_COLOR_INJURIES | `COLOR_DRED` |  |
| AW_COLOR_NPC_NAME | `COLOR_DDGREEN` |  |
| AW_COLOR_FACTION_NAME | `COLOR_DGREEN` |  |
| AW_COLOR_FACTION_RANK | `COLOR_LGRAY` |  |
| BONUS_WEAPON_CRITICAL_ROLL | `(100)` |  |
| BONUS_WEAPON_CRITICAL_CHANCE | `(101)` |  |
| BONUS_WEAPON_MIN_DMG | `(102)` |  |
| BONUS_WEAPON_MAX_DMG | `(103)` |  |
| BONUS_WEAPON_ACCURACY | `(104)` |  |
| BONUS_WEAPON_MAX_AP | `(105)` |  |
| BONUS_WEAPON_MAX_RANGE | `(106)` |  |
| _DescHead | `((ELAPSED_TIME / REAL_SECOND(3)) % 2 == 1)` |  |
| COLOR_TOWN_AREA_BORDER | `(0x770000FF)` | client_town /// |
| COLOR_TOWN_AREA_INTERIOR | `(0x20000080)` |  |

## Classes

### CDialogImage

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| x | `int` |  |  |
| y | `int` |  |  |
| sprite | `int` |  |  |

**Methods**

#### Set
```angelscript
void Set(int x, int y, string& image)
```

#### Unset
```angelscript
void Unset()
```

#### Exists
```angelscript
bool Exists()
```

#### Draw
```angelscript
void Draw()
```

### CWorldmapElement

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| id | `int` |  |  |
| layer | `uint` |  |  |
| x | `uint` |  |  |
| y | `uint` |  |  |
| width | `uint` |  |  |
| height | `uint` |  |  |
| color | `uint` |  |  |
| sprite | `[Sprite](sprite.fos.md)` |  |  |
| scratch | `bool` |  |  |
| center | `bool` |  |  |
| applyOffset | `bool` |  |  |
| text | `string` |  |  |
| font | `int` |  |  |
| flags | `int` |  |  |

**Methods**

#### SetSprite
```angelscript
void SetSprite(Sprite& sprite, bool scratch, bool center, bool applyOffset)
```

#### SetText
```angelscript
void SetText(string& text, int font, int flags)
```

#### Draw
```angelscript
void Draw(uint layer)
```

### CTempWorldmapElement

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| expirationTime | `uint` |  |  |

**Methods**

#### IsExpired
```angelscript
bool IsExpired()
```

### BagCallbackHide

**Methods**

#### OnHide
```angelscript
void OnHide(int p0, int p1, int p2)
```

### Rect

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| X1 | `int` |  |  |
| Y1 | `int` |  |  |
| X2 | `int` |  |  |
| Y2 | `int` |  |  |

**Methods**

#### IsInside
```angelscript
bool IsInside(int x, int y)
```

#### H
```angelscript
int H() { return Y2 - Y1 + 1; }
```

#### W
```angelscript
int W() { return X2 - X1 + 1; }
```


## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| crFade | `array<uint>` |  |  |
| DialogImage | `[CDialogImage](client_interface.fos.md)` |  |  |
| pickupScreenScrollCritter | `uint` | `0` |  |
| pickupScreenScrollFrom | `uint` | `0` |  |
| disableItemMove | `bool` | `false` |  |
| recheckDialogImage | `bool` | `false` |  |
| MapZoom | `float` | `1` |  |
| BagHide | `[BagCallbackHide](client_interface.fos.md)` |  |  |
| ItemBar | `[Rect](utils_h.fos.md)@` |  |  |
| AmmoString | `string` |  |  |
| LastAmmoCount | `int` | `0` |  |
| IndicatorDraw | `bool` | `false` |  |
| CounterDraw | `bool` | `false` |  |
| InvItemClicked | `bool` | `false` |  |
| AmmoIndicatorPoints | `array<int>` |  |  |
| AmmoIndicatorTick | `uint` | `0` |  |
| AmmoIndicator | `[Rect](utils_h.fos.md)@` |  |  |
| AmmoCounter | `[Rect](utils_h.fos.md)@` |  |  |
| AmmoCounterClicked | `[Rect](utils_h.fos.md)@` |  |  |
| WearIndicatorPoints | `array<int>` |  |  |
| WearIndicatorTick | `uint` | `0` |  |
| WearIndicator | `[Rect](utils_h.fos.md)@` |  |  |
| WearCounter | `[Rect](utils_h.fos.md)@` |  |  |
| WearCounterClicked | `[Rect](utils_h.fos.md)@` |  |  |
| InterfaceShown | `bool` | `true` |  |
| WallRoofTransparency | `bool` | `false` |  |
| timers | `array<uint>` |  |  |
| factions | `array<string>` |  |  |
| townnames | `array<string>` |  |  |
| lastsecond | `uint` |  |  |
| lasthour | `uint` |  |  |
| modoc_area_t | `array<uint16>` |  |  |
| bh_area_t | `array<uint16>` |  |  |
| klamath_area_t | `array<uint16>` |  |  |
| den_area_t | `array<uint16>` |  |  |
| redding_area_t | `array<uint16>` |  |  |
| gecko_area_t | `array<uint16>` |  |  |
| modoc_area | `IPolygon@` |  |  |
| bh_area | `IPolygon@` |  |  |
| klamath_area | `IPolygon@` |  |  |
| den_area | `IPolygon@` |  |  |
| redding_area | `IPolygon@` |  |  |
| gecko_area | `IPolygon@` |  |  |
| Initialized | `bool` | `false` |  |

## Functions

### unsetall_location_combatzone

```angelscript
void unsetall_location_combatzone(int, int, int, string@, array<int>@)
```

### location_combatzone

```angelscript
void location_combatzone(int id, int layer, int expiration, string@, array<int>@ coords)
```

### worldmap_element

```angelscript
void worldmap_element(int id, int layer, int type, string@, array<int>@ data)
```

### get_active_screens

///////////////////////////////////////////////////////////////////////////////////////////////// Say to engine what screen is active.

```angelscript
void get_active_screens(array<int>& result)
```

### screen_change

///////////////////////////////////////////////////////////////////////////////////////////////// Show/hide screen behaviour.

```angelscript
void screen_change(bool show, int screen, int p0, int p1, int p2)
```

### render_iface

///////////////////////////////////////////////////////////////////////////////////////////////// Render interface function. You can use Draw* functions only there. Layer specification: 1 Game map 2 Console, Messbox 3 PopUp menu, Cursor 4  Extra layers: Global map 100 (over map), 101 (over all) 

```angelscript
void render_iface(uint layer)
```

### render_iface_screen

```angelscript
bool render_iface_screen(uint screen)
```

### generic_description

///////////////////////////////////////////////////////////////////////////////////////////////// Generic description. Descriptions type look in _client_defines.fos, Generic descriptions types. int& offsX, int& offsY - offsets of text, by default is zero.

```angelscript
string generic_description(int descType, int& offsX, int& offsY)
```

### item_description

///////////////////////////////////////////////////////////////////////////////////////////////// Item description. Look types look in _client_defines.fos, Item look types.

```angelscript
string item_description(ItemCl& item, int lookType)
```

### SelectWeaponBonus

```angelscript
int SelectWeaponBonus(ItemCl& it, int Int_Val_WeaponBonus)
```

### showItemBonus

```angelscript
string showItemBonus(ItemCl& it, int type, int value)
```

### showPrefix

```angelscript
string showPrefix(ItemCl@ it)
```

### critter_description

```angelscript
string critter_description(CritterCl& cr, int lookType)
```

### critter_in

///////////////////////////////////////////////////////////////////////////////////////////////// Called on something critter in/out game.

```angelscript
void critter_in(CritterCl& cr)
```

### critter_out

```angelscript
void critter_out(CritterCl& cr)
```

### _SetColor

* * Sets color basing on groups status and reputation. 

```angelscript
void _SetColor(int crId, int status, int reputation, string@ param3, array<int>@ param4)
```

### _EnableItemsMove

```angelscript
void _EnableItemsMove(int param1, int param2, int param3, string@ param4, array<int>@ param5)
```

### _SetScrolls

```angelscript
void _SetScrolls(int scrollCrit, int scrollCont, int param3, string@ param4, array<int>@ param5)
```

### _RepairSession

```angelscript
void _RepairSession(int param1, int param2, int param3, string@ param4, array<int>@ param5)
```

### _RechargeSession

```angelscript
void _RechargeSession(int param1, int param2, int param3, string@ param4, array<int>@ param5)
```

### _DialogImage

```angelscript
void _DialogImage(int x, int y, int imageId, string@, array<int>@)
```

### _DialogImageSkin

```angelscript
void _DialogImageSkin( int hash, int dir, int, string@, array<int>@ )
```

### _DialogImageUnset

```angelscript
void _DialogImageUnset( int, int, int, string@, array<int>@ )
```

### DialogImageKey

```angelscript
void DialogImageKey(uint8 key)
```

### InitBagCallbacks

```angelscript
void InitBagCallbacks()
```

### IndicatorMouse

```angelscript
void IndicatorMouse(bool down, int click)
```

### ReadIniInt

```angelscript
bool ReadIniInt(string& key, int& ret)
```

### InitIndicators

```angelscript
void InitIndicators()
```

### DrawIndicators

```angelscript
void DrawIndicators()
```

### IsInterfaceShown

```angelscript
bool IsInterfaceShown()
```

### ToggleInterfaceShown

```angelscript
void ToggleInterfaceShown()
```

### SetInterfaceShown

```angelscript
void SetInterfaceShown(bool setting)
```

### IsWallRoofTransparency

```angelscript
bool IsWallRoofTransparency()
```

### ToggleWallRoofTransparency

```angelscript
bool ToggleWallRoofTransparency()
```

### RestoreWallRoofTransparency

```angelscript
void RestoreWallRoofTransparency( bool force = false )
```

### DrawIndicator

yes, totally ripped from the engine

```angelscript
void DrawIndicator(Rect@ rect, array<int>& points, uint color, int procent, uint& tick, bool is_vertical, bool from_top_or_left, uint changeTick = 35)
```

### DrawCounter

```angelscript
void DrawCounter(Rect@ rect, string& text, uint color, int font)
```

### DrawArea

```angelscript
void DrawArea(uint mappid, uint8 mode)
```

### DrawInsideStatus

```angelscript
void DrawInsideStatus(bool inside)
```

### InitTownDisplay

```angelscript
void InitTownDisplay()
```

### InitAreas

```angelscript
void InitAreas()
```

### CountDownStop

```angelscript
void CountDownStop(int town)
```

### CountDownStart

```angelscript
void CountDownStart(int town, uint time, string@ faction)
```

### IsCounting

```angelscript
bool IsCounting(uint townid)
```

### GetTownName

```angelscript
string GetTownName(uint townid)
```

### GetFaction

```angelscript
string GetFaction(uint townid)
```

### GetSeconds

```angelscript
int GetSeconds(uint townid)
```

### render_map

///////////////////////////////////////////////////////////////////////////////////////////////// Render map function. You can use DrawMap* functions only there. This drawing before 1 iface layer.

```angelscript
void render_map()
```

### item_map_in

///////////////////////////////////////////////////////////////////////////////////////////////// Called on something item in/changed/out map.

```angelscript
void item_map_in(ItemCl& item)
```

### item_map_changed

```angelscript
void item_map_changed(ItemCl& itemNow, ItemCl& itemBefore)
```

### item_map_out

```angelscript
void item_map_out(ItemCl& item)
```

### item_inv_in

///////////////////////////////////////////////////////////////////////////////////////////////// Called on something critter in/out chosen inventory.

```angelscript
void item_inv_in(ItemCl& item)
```

### item_inv_out

```angelscript
void item_inv_out(ItemCl& item)
```

### item_drop

///////////////////////////////////////////////////////////////////////////////////////////////// Called on player drag&drop some item.

```angelscript
void item_drop(ItemCl& item)
```


