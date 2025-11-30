---
title: client_keybinds_h.fos
description: " FOnline: 2238 Rotators  client_keybinds_h.fos ..."
---

# client_keybinds_h.fos


FOnline: 2238
Rotators

client_keybinds_h.fos


## Included By

- [client_keybinds.fos](client_keybinds.fos.md)

## Classes

### BaseBind

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| ctrl | `bool` |  |  |
| alt | `bool` |  |  |
| shift | `bool` |  |  |

**Methods**

#### CtrlPressed
```angelscript
bool CtrlPressed()  { return GUI_IsKeyPressed(DIK_LCONTROL) || GUI_IsKeyPressed(DIK_RCONTROL); }
```

#### ShiftPressed
```angelscript
bool ShiftPressed() { return GUI_IsKeyPressed(DIK_LSHIFT) || GUI_IsKeyPressed(DIK_RSHIFT); }
```

#### AltPressed
```angelscript
bool AltPressed()   { return GUI_IsKeyPressed(DIK_LMENU) || GUI_IsKeyPressed(DIK_RMENU); }
```

#### Active
```angelscript
bool Active()
```

#### Exec
```angelscript
void Exec() {}
```

### BindList

**Methods**

#### TryRun
```angelscript
bool TryRun()
```

#### AddBind
```angelscript
void AddBind(IBind@ bind)
```

### Bind

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| modifiers | `array<int>` |  |  |

**Methods**

#### Active
```angelscript
bool Active()
```

#### Exec
```angelscript
void Exec() {}
```

### GMBind

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| commands | `array<string>` |  |  |

**Methods**

#### Exec
```angelscript
void Exec()
```

### UseBind

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| pids | `array<uint16>` |  |  |

**Methods**

#### Exec
```angelscript
void Exec()
```

### StopCritterBind

**Methods**

#### Exec
```angelscript
void Exec()
```

### ReloadBind

**Methods**

#### Exec
```angelscript
void Exec()
```

### PickupBind

**Methods**

#### Exec
```angelscript
void Exec()
```

### DropallBind

**Methods**

#### Exec
```angelscript
void Exec()
```

### AimBind

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| aim | `uint8` |  |  |

**Methods**

#### Exec
```angelscript
void Exec()
```

### ToggleFogBind

**Methods**

#### Exec
```angelscript
void Exec()
```

### ToggleRoofBind

**Methods**

#### Exec
```angelscript
void Exec()
```

### ToggleWallBind

**Methods**

#### Exec
```angelscript
void Exec()
```

### ToggleMsFovBind

**Methods**

#### Exec
```angelscript
void Exec()
```

### FASelfBind

**Methods**

#### Exec
```angelscript
void Exec()
```

### DocSelfBind

**Methods**

#### Exec
```angelscript
void Exec()
```

### SSOtherBind

**Methods**

#### Exec
```angelscript
void Exec()
```

### DischargeBind

**Methods**

#### Exec
```angelscript
void Exec()
```

### ScienceAtHexBind

**Methods**

#### Exec
```angelscript
void Exec()
```

### CenterChosenBind

**Methods**

#### Exec
```angelscript
void Exec()
```

### TransparencyBind

**Methods**

#### Exec
```angelscript
void Exec()
```


