---
title: client_io.fos
description: " FOnline: 2238 Rotators  client_io.fos ..."
---

# client_io.fos


FOnline: 2238
Rotators

client_io.fos


## Includes

- `_client_defines.fos`
- `client_gui_h.fos`
- `client_interface_h.fos`
- `config_file_h.fos`
- `client_utils_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| SKIP_PRAGMAS |  |  |
| LeftCtrl | `GUI_IsKeyPressed(DIK_LCONTROL)` |  |
| RightCtrl | `GUI_IsKeyPressed(DIK_RCONTROL)` |  |
| AnyCtrl | `(LeftCtrl || RightCtrl)` |  |
| NoCtrl | `(!LeftCtrl && !RightCtrl)` |  |
| LeftAlt | `GUI_IsKeyPressed(DIK_LMENU)` |  |
| RightAlt | `GUI_IsKeyPressed(DIK_RMENU)` |  |
| AnyAlt | `(LeftAlt || RightAlt)` |  |
| NoAlt | `(!LeftAlt && !RightAlt)` |  |
| LeftShift | `GUI_IsKeyPressed(DIK_LSHIFT)` |  |
| RightShift | `GUI_IsKeyPressed(DIK_RSHIFT)` |  |
| AnyShift | `(LeftShift || RightShift)` |  |
| NoShift | `(!LeftShift && !RightShift)` |  |

## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| PrevMouseX | `int` | `__MouseX` |  |
| PrevMouseY | `int` | `__MouseY` |  |

## Functions

### input_lost

///////////////////////////////////////////////////////////////////////////////////////////////// Called on mouse/keyboard input lost (alt-tab, minimize, lost focus).

```angelscript
void input_lost()
```

### key_down

///////////////////////////////////////////////////////////////////////////////////////////////// Keyboard behaviours. Key codes look in _client_defines.fos DirectInput keyboard scan codes. Return true to disable engine events.

```angelscript
bool key_down(uint8 key,string& keyText)
```

### key_up

```angelscript
bool key_up(uint8 key,string& keyText)
```

### mouse_down

///////////////////////////////////////////////////////////////////////////////////////////////// Mouse behaviours. Click states look in _client_defines.fos, Mouse click states. Return true to disable engine events.

```angelscript
bool mouse_down(int click)
```

### mouse_up

```angelscript
bool mouse_up(int click)
```

### mouse_move

```angelscript
void mouse_move(int x, int y)
```

### filename_tokens

```angelscript
void filename_tokens(string& replacement)
```

### filename_logfile

```angelscript
void filename_logfile(string& filename)
```

### filename_screenshot

```angelscript
void filename_screenshot(string& filename)
```

### EndTurnBasedTurn

```angelscript
bool EndTurnBasedTurn()
```

### EndTurnBasedCombat

```angelscript
bool EndTurnBasedCombat()
```


