---
title: map_ncr_downtown.fos
---

# map_ncr_downtown.fos

## Includes

- `_macros.fos`
- `economy_h.fos`
- `mapdata_h.fos`
- `reinforcements_h.fos`
- `_maps.fos`
- `_entires.fos`
- `polygon_h.fos`

## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| WestinRanchPolygon | `IPolygon@` | `null` |  |

## Functions

### map_init

```angelscript
void map_init(Map& map, bool firstTime)
```

### _CritterOut

```angelscript
void _CritterOut(Map& map, Critter& cr)
```

### s_Westin_WaterPump

```angelscript
bool s_Westin_WaterPump(Critter& player, Scenery& table, int skill, Item@ item)
```

### InitWestinRanch

```angelscript
void InitWestinRanch(Map& map)
```

### d_InsideWestinRanch

```angelscript
bool d_InsideWestinRanch(Critter& cr, Critter@ npc)
```


