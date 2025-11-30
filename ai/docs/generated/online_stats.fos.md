---
title: online_stats.fos
description: " FOnline: 2238 Rotators  online_stats.fos ..."
---

# online_stats.fos


FOnline: 2238
Rotators

online_stats.fos


## Includes

- `_macros.fos`
- `MsgStr.h`
- `config_file_h.fos`
- `online_stats_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __ONLINE_STATS__ |  |  |
| __ONLINE_STATS_MODULE__ |  |  |
| OS_CONFIG | `"config\\OnlineStats.cfg"` |  |
| OS_SCRIPT | `"client_online_stats@_Setup"` |  |
| _checkflag | `# (c, f, r) if(FLAG(c, f)) { SETFLAG(r, f); }` |  |

## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| OS_Disabled | `bool` | `false` |  |
| OS_Initialized | `bool` | `false` |  |
| OS_Directory | `string` | `""` |  |

## Functions

### OnlineStats_Init

```angelscript
void OnlineStats_Init()
```

### OnlineStats_TrySave

```angelscript
void OnlineStats_TrySave(Critter& target)
```

### OnlineStats_SendSetup

* * Send LVAR copy to client * @sa: unsafe_setup 

```angelscript
void OnlineStats_SendSetup(Critter& target)
```

### unsafe_setup

* * Send/get LVAR to/from client, strip unknown flags. 

```angelscript
void unsafe_setup(Critter& target, int flags, int mode, int, string@, array<int>@)
```

### charsave

just some verbose around *TrySave

```angelscript
void charsave(Critter& player, int param0, int param1, int param2)
```

### get

```angelscript
void get(Critter& player, int, int, int)
```

### v_showflags

```angelscript
void v_showflags(Critter& player)
```

### showflags

```angelscript
void showflags(Critter& player, int param0, int param1, int param2)
```

### getflags

```angelscript
void getflags(Critter& player, int param0, int param1, int param2)
```

### setflag

```angelscript
void setflag(Critter& player, int param0, int param1, int param2)
```

### setflags

```angelscript
void setflags(Critter& player, int param0, int param1, int param2)
```


