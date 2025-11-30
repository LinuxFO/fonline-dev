---
title: map_playerfaction_hq.fos
description: " FOnline: 2238 Rotators  map_playerfaction_hq.fos ..."
---

# map_playerfaction_hq.fos


FOnline: 2238
Rotators

map_playerfaction_hq.fos


## Includes

- `_macros.fos`
- `factions_h.fos`
- `factions_bases_h.fos`
- `utils_h.fos`
- `mapdata_h.fos`

## Functions

### map_init

 Initialize map 

```angelscript
void map_init(Map& map, bool firstTime)
```

### _Finish

removes data associated with faction base if map is going to be deleted

```angelscript
void _Finish(Map& map, bool todelete)
```

### _OnInCritter

set this location as visible to player when he enters but only when he is friend of the faction

```angelscript
void _OnInCritter(Map& map, Critter& crit)
```

### _Dead

 If faction member killed leader on faction ground, and there is someone who claimed leadership the leader cease to be leader, so that claimee can claim leadership if claimee dies on the faction ground, he cease to be claimee too  If not member is killed by member or follower of member, he no longer can see the location If a faction friend/invited person kills a faction member inside faction base, he is removed from faction friends/invited

```angelscript
void _Dead(Map& map, Critter& player, Critter@ killer)
```


