---
title: item_dogtags.fos
description: " FOnline: 2238 Rotators  item_dogtags.fos ..."
---

# item_dogtags.fos


FOnline: 2238
Rotators

item_dogtags.fos


## Includes

- `_defines.fos`
- `_macros.fos`
- `_vars.fos`
- `lexems_h.fos`
- `factions_h.fos`
- `npc_names_h.fos`
- `item_dogtags_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __DOGTAGS__ |  |  |
| DT_OWNER_MILITARY | `"$SURNAME, $NAME"` |  |
| DT_OWNER_CUSTOM | `"$NAME $NICK_$SURNAME"` |  |
| DT_INFO_MILITARY | `"$ID/$MOB/$YOB/$BLOOD"` |  |
| DT_INFO_CUSTOM | `"$MOB/$YOB/$BLOOD"` |  |

## Functions

### DogTag

```angelscript
Item@ DogTag(Critter@ cr)
```

### DogTag

```angelscript
Item@ DogTag(Critter@ holder, Critter@ target)
```

### DogTagBlank

```angelscript
Item@ DogTagBlank(Critter@ holder)
```

### IsSoldier

```angelscript
bool IsSoldier(Critter@ cr)
```

### IsRanger

```angelscript
bool IsRanger(Critter@ cr)
```

### d_HasFactionDogtags

```angelscript
bool d_HasFactionDogtags(Critter& player, Critter@ npc, int faction, int count)
```

### r_RemoveFactionDogtags

```angelscript
void r_RemoveFactionDogtags(Critter& player, Critter@ npc, int faction, int count)
```

### spawn

```angelscript
void spawn(Critter& holder, int id, int, int)
```


