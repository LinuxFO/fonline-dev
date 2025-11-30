---
title: client_keybinds.fos
description: " FOnline: 2238 Rotators  client_keybinds.fos ..."
---

# client_keybinds.fos


FOnline: 2238
Rotators

client_keybinds.fos


## Includes

- `_client_defines.fos`
- `_macros.fos`
- `client_keybinds_h.fos`
- `config_file_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| SKIP_PRAGMAS |  |  |
| CLIENT_KEYBINDS |  |  |

## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| bindlists | `array<[BindList](client_keybinds_h.fos.md)>` |  |  |
| KeyMap | `dictionary` |  |  |
| KeyMapRaw | `dictionary` |  |  |
| CurrentAim | `uint8` | `HIT_LOCATION_UNCALLED` |  |

## Functions

### GetCurrentAim

```angelscript
uint8 GetCurrentAim()
```

### TryAddBind

read basic bind string ("Ctrl Alt Del 1")

```angelscript
bool TryAddBind(string@ s, BaseBind& bind)
```

### AddGMBind

Bind key -> cheat

```angelscript
void AddGMBind(int key, array<int>& modifiers, string command)
```

### AddAimBind

```angelscript
bool AddAimBind(string& cfgkey, uint8 num)
```

### ProcessBind

```angelscript
bool ProcessBind(uint8 key)
```

### InitBinds

```angelscript
bool InitBinds()
```

### InitGMBinds

```angelscript
bool InitGMBinds()
```

### InitUseBinds

```angelscript
bool InitUseBinds()
```

### InitStopCritterBind

```angelscript
bool InitStopCritterBind()
```

### InitReloadBind

```angelscript
bool InitReloadBind()
```

### InitPickupBind

```angelscript
bool InitPickupBind()
```

### InitDropallBind

```angelscript
bool InitDropallBind()
```

### InitFASelfBind

```angelscript
bool InitFASelfBind()
```

### InitDocSelfBind

```angelscript
bool InitDocSelfBind()
```

### InitSSOtherBind

```angelscript
bool InitSSOtherBind()
```

### InitFogBind

```angelscript
bool InitFogBind()
```

### InitRoofBind

```angelscript
bool InitRoofBind()
```

### InitWallBind

```angelscript
bool InitWallBind()
```

### InitMsFovBind

```angelscript
bool InitMsFovBind()
```

### InitDischargeBind

```angelscript
bool InitDischargeBind()
```

### InitScienceAtHexBind

```angelscript
bool InitScienceAtHexBind()
```

### InitCenterChosenBind

```angelscript
bool InitCenterChosenBind()
```

### InitTransparencyBind

```angelscript
bool InitTransparencyBind()
```

### InitAimBinds

```angelscript
bool InitAimBinds()
```

### InitKeyMap

```angelscript
void InitKeyMap()
```


