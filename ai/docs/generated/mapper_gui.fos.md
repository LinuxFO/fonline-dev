---
title: mapper_gui.fos
description: " FOnline: 2238 Rotators  mapper_gui.fos ..."
---

# mapper_gui.fos


FOnline: 2238
Rotators

mapper_gui.fos


## Includes

- `_mapper_macros.fos`
- `_defines.fos`
- `MsgStr.h`
- `sprite.fos`

## Included By

- [mapper_autowall.fos](mapper_autowall.fos.md)
- [mapper_crtypes.fos](mapper_crtypes.fos.md)

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __MAPPER_GUI__ |  |  |

## Classes

### CGuiManager

**Methods**

#### RegisterControl
 Adds control to the list 

```angelscript
void RegisterControl(IControl@ control)
```

#### Draw
 Draws all visible windows 

```angelscript
void Draw()
```

#### Update
 Updates all active windows 

```angelscript
void Update()
```

#### MouseDown
```angelscript
bool MouseDown(int click)
```

#### MouseUp
```angelscript
bool MouseUp(int click)
```

#### MouseMove
```angelscript
void MouseMove(int x, int y)
```

#### KeyDown
```angelscript
bool KeyDown(uint8 key)
```

#### KeyUp
```angelscript
bool KeyUp(uint8 key)
```

#### AnyVisible
```angelscript
bool AnyVisible()
```

### Control

 Basic element of gui subsystem 

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| parent | `IControl@` |  | parent control |
| left | `int` |  | coordinates (relative to parent) |
| top | `int` |  |  |
| width | `int` |  |  |
| height | `int` |  |  |
| active | `bool` |  | whether control should be processed by manager |
| visible | `bool` |  | whether control should be drawn |
| focus | `bool` |  | control has a focus |
| mousePressed | `bool` |  | stored event info (captured when event occurs) |

**Methods**

#### IsVisible
```angelscript
bool IsVisible() {      return visible; }
```

#### IsActive
```angelscript
bool IsActive()  { return active; }
```

#### Left
 Absolute coords 

```angelscript
int Left()
```

#### Top
```angelscript
int Top()
```

#### Right
```angelscript
int Right()
```

#### Bottom
```angelscript
int Bottom()
```

#### Height
```angelscript
int Height()
```

#### Width
```angelscript
int Width()
```

#### IsInside
 Checks if given coordinates are within control's bounds 

```angelscript
bool IsInside(int x, int y)
```

#### SetParent
 Assings parent control 

```angelscript
void SetParent(IControl@ control)
```

#### Enable
 Activating/deactivating 

```angelscript
void Enable()  { active = true; }
```

#### Disable
```angelscript
void Disable() { active = false; }
```

#### Show
 Showing/hiding 

```angelscript
void Show()
```

#### Show
```angelscript
void Show(int dx, int dy)
```

#### Hide
```angelscript
void Hide()
```

#### SetFocus
 Focus 

```angelscript
void SetFocus(bool focused)
```

#### AddControl
  Adds child control 

```angelscript
void AddControl(IControl@ control)
```

#### MouseDown
```angelscript
bool MouseDown(int click)
```

#### MouseUp
```angelscript
bool MouseUp(int click)
```

#### MouseMove
```angelscript
void MouseMove(int x, int y)
```

#### KeyDown
```angelscript
bool KeyDown(uint8 key)
```

#### KeyUp
```angelscript
void KeyUp(uint8 key)
```

#### Draw
 Draws all visible subcontrols 

```angelscript
void Draw()
```

#### Update
 Updates all active child controls 

```angelscript
void Update()
```

#### Click
 Called on left click 

```angelscript
void Click()
```

#### GotFocus
 Called when clicked on control 

```angelscript
void GotFocus()
```

#### LostFocus
 Called when clicked outside control 

```angelscript
void LostFocus()
```

### CButton

this one uses worldmap buttons graphics

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| caption | `string` |  |  |
| spriteUp | `[Sprite](sprite.fos.md)` |  |  |
| spriteDown | `[Sprite](sprite.fos.md)` |  |  |

**Methods**

#### SetCaption
 Caption 

```angelscript
void SetCaption(string@ caption) { this.caption = caption; }
```

#### Draw
```angelscript
void Draw()
```

### CDialogRedButton

this one uses dialog red button graphics when pressed

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| spriteDown | `[Sprite](sprite.fos.md)` |  |  |

**Methods**

#### Draw
 Draw only when pressed 

```angelscript
void Draw()
```

### CSmallButton

and that one uses smallbutton graphics when pressed

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| spriteDown | `[Sprite](sprite.fos.md)` |  |  |

**Methods**

#### Draw
 Draw only when pressed 

```angelscript
void Draw()
```

### CSmallArrowUp

small arrow up

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| spriteDown | `[Sprite](sprite.fos.md)` |  |  |

**Methods**

#### Draw
 Draw only when pressed 

```angelscript
void Draw()
```

### CSmallArrowDown

small arrow up

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| spriteDown | `[Sprite](sprite.fos.md)` |  |  |

**Methods**

#### Draw
 Draw only when pressed 

```angelscript
void Draw()
```

### CLabel

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| font | `int` |  |  |
| color | `int` |  |  |
| format | `int` |  |  |
| caption | `string@` |  |  |

**Methods**

#### SetCaption
```angelscript
void SetCaption(string@ caption)
```

#### SetColor
```angelscript
void SetColor(uint color)
```

#### SetFormat
```angelscript
void SetFormat(uint format)
```

#### Draw
```angelscript
void Draw()
```

### CTextBox

//////////////// TextBox ////////////////

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| text | `string` |  | textbox' text |
| drawnText | `string` |  | drawn text (with cursor) |
| cursorPos | `uint` |  |  |
| cursorTime | `uint` |  | cursor blink time, miliseconds |
| cursorChangedTime | `uint` |  | last changed |
| showCursor | `int` |  | (0 - invisible, 1/2 - visible (switching)) |
| cursor1 | `string` |  | cursor characters |
| cursor2 | `string` |  |  |
| color | `int` |  | text prop |
| format | `int` |  |  |
| font | `int` |  |  |

**Methods**

#### Text
 Returns textbox' text 

```angelscript
string@ Text()
```

#### GetCursor
 gets actually displayed cursor 

```angelscript
string@ GetCursor()
```

#### SetColor
```angelscript
void SetColor(uint color)
```

#### SetFormat
```angelscript
void SetFormat(uint format)
```

#### SetText
```angelscript
void SetText(string@ text)
```

#### ShowCursor
 Shows/hides cursor in drawnText (0 - invisible, 1/2 - visible (switching)) 

```angelscript
void ShowCursor(int show)
```

#### InsertChar
 Inserts character corresponding with pressed key 

```angelscript
void InsertChar(uint8 key)
```

#### Draw
```angelscript
void Draw()
```

#### KeyDown
```angelscript
bool KeyDown(uint8 key)
```

### CSprite

////////// Draws something //////////

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| sprite | `[Sprite](sprite.fos.md)` |  |  |

**Methods**

#### Draw
```angelscript
void Draw()
```

### CListBox

///////////// List Box /////////////

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| start | `uint` |  | first visible element |
| index | `uint` |  | selected element |
| textHeight | `uint` |  |  |

**Methods**

#### GetRowCount
 Gets number of visible elements 

```angelscript
uint GetRowCount()
```

#### GetIndex
 Gets index to selected item 

```angelscript
uint GetIndex()
```

#### AddElement
 Adds element to the list 

```angelscript
void AddElement(string@ elem)
```

#### Scroll
 Scrolls list by certain amount of elements 

```angelscript
void Scroll(int d)
```

#### Draw
 Draws all visible elements 

```angelscript
void Draw()
```

#### Click
 Selects element 

```angelscript
void Click()
```


