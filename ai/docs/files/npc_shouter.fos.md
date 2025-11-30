---
title: npc_shouter.fos
description: " FOnline: 2238 Rotators  npc_shouter.fos ..."
---

# npc_shouter.fos


FOnline: 2238
Rotators

npc_shouter.fos


## Includes

- `_macros.fos`
- `npc_roles_h.fos`
- `npc_planes_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| _TryShouter | `# (__role, __dialog, __start, __end, __minwait, __maxwait) if(npc.Stat[ST_NPC_ROLE] == __role) { npc.SayMsg(SAY_NORM_ON_HEAD, TEXTMSG_DLG, DLGSTR(__dialog, Random(__start, __end))); npc.Wait(Random(__minwait, __maxwait)); }` |  |

## Functions

### critter_init

```angelscript
void critter_init(Critter& npc, bool firstTime)
```

### _Idle

```angelscript
void _Idle(Critter& npc)
```


