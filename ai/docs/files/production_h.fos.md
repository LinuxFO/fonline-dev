---
title: production_h.fos
description: " FOnline: 2238 Rotators  production_h.fos ..."
---

# production_h.fos


FOnline: 2238
Rotators

production_h.fos


## Includes

- `_macros.fos`
- `MsgStr.h`

## Included By

- [item_brahmin_dung.fos](item_brahmin_dung.fos.md)
- [mine.fos](mine.fos.md)
- [prod_barrel_junk.fos](prod_barrel_junk.fos.md)
- [prod_broc_flower.fos](prod_broc_flower.fos.md)
- [prod_chemicals.fos](prod_chemicals.fos.md)
- [prod_computer.fos](prod_computer.fos.md)
- [prod_flint.fos](prod_flint.fos.md)
- [prod_generic.fos](prod_generic.fos.md)
- [prod_machine.fos](prod_machine.fos.md)
- [prod_mine_h.fos](prod_mine_h.fos.md)
- [prod_nukacola.fos](prod_nukacola.fos.md)
- [prod_plant_barley.fos](prod_plant_barley.fos.md)
- [prod_plant_fiber.fos](prod_plant_fiber.fos.md)
- [prod_plant_fruit.fos](prod_plant_fruit.fos.md)
- [prod_plant_h.fos](prod_plant_h.fos.md)
- [prod_plant_tobacco.fos](prod_plant_tobacco.fos.md)
- [prod_rocks_minerals.fos](prod_rocks_minerals.fos.md)
- [prod_rocks_ore.fos](prod_rocks_ore.fos.md)
- [prod_rocks_uranium.fos](prod_rocks_uranium.fos.md)
- [prod_still_rotgut.fos](prod_still_rotgut.fos.md)
- [prod_table_brahmin.fos](prod_table_brahmin.fos.md)
- [prod_tree_firewood.fos](prod_tree_firewood.fos.md)
- [prod_xander_root.fos](prod_xander_root.fos.md)
- [production.fos](production.fos.md)
- [prospect_miner.fos](prospect_miner.fos.md)
- [prospect_owner.fos](prospect_owner.fos.md)

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __PRODUCTION_H__ |  |  |
| AMOUNT | `# (item) (item.Val1)` | the amount of resource left |
| COUNTER | `# (item) (item.Val2)` | number of times facility has been used/resource fetched (that's to be decided, or scrapped;) ) |
| TIMEOUT_CUMULATIVE | `(int(REAL_MINUTE(20)))` | cumulative timeout |
| SET_TIMEOUT | `# (cr, to)     { cr.TimeoutBase[TO_GATHERING] = __FullSecond + cr.Timeout[TO_GATHERING] + REAL_SECOND(to); }` | gathering timeout |
| SAY_TIMEOUT | `# (crit) { crit.SayMsg(SAY_NETMSG, TEXTMSG_TEXT, 3000); }` | useful defines |
| SAY_LACKING_SKILLS | `# (crit) { crit.SayMsg(SAY_NETMSG, TEXTMSG_TEXT, 3001); }` |  |
| SAY_TIMEOUT_SELF | `# (cr)   { cr.SayMsg(SAY_NETMSG, TEXTMSG_GAME, STR_SKILL_WEARINESS); }` |  |
| TOOL_IS_KNIFE | `# (pid)  (pid == PID_SWITCHBLADE || pid == PID_KNIFE || pid == PID_THROWING_KNIFE || pid == PID_COMBAT_KNIFE || pid == PID_LIL_JESUS_WEAPON || pid == PID_WAKIZASHI_BLADE)` | tools types; should be in synch with smart_cursor lists |

## Classes

### PicHashes

helper for altering facility-item images

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| hashes | `array<uint>` |  |  |

**Methods**

#### GetRandom
```angelscript
uint GetRandom() const
```


## Functions

### StartRegeneration

* * Spawns regeneration event, if needed. * Because of the fact function is included in every module, * it will use whatever e_ function there is. 

```angelscript
void StartRegeneration(Item& item, string& func_name)
```


