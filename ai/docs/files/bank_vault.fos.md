---
title: bank_vault.fos
description: " FOnline: 2238 Rotators  bank_vault.fos ..."
---

# bank_vault.fos


FOnline: 2238
Rotators

bank_vault.fos


## Includes

- `_macros.fos`
- `economy_h.fos`
- `npc_common_h.fos`
- `messages_h.fos`
- `mapdata_h.fos`

## Included By

- [map_redding_bank_vault.fos](map_redding_bank_vault.fos.md)

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| MSG_SECURITY_HACKED | `(2)` |  |

## Functions

### OnInCritter

```angelscript
void OnInCritter(Map& map, Critter& player)
```

### t_Entered

```angelscript
void t_Entered(Critter& player, Scenery& trigger, bool entered, uint8 dir)
```

### s_SecurityTerminal

```angelscript
bool s_SecurityTerminal(Critter& player, Scenery& terminal, int skill, Item@ item)
```

### s_VaultTerminal

```angelscript
bool s_VaultTerminal(Critter& player, Scenery& terminal, int skill, Item@ item)
```

### t_Safe

```angelscript
void t_Safe(Critter& player, Scenery& trigger, bool entered, uint8 dir)
```


