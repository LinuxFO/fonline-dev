---
title: client_gui_ex.fos
description: " FOnline: 2238 Rotators  client_gui_ex.fos ..."
---

# client_gui_ex.fos


FOnline: 2238
Rotators

client_gui_ex.fos


## Included By

- [client_container_addons.fos](client_container_addons.fos.md)
- [client_fixboy.fos](client_fixboy.fos.md)
- [client_gui_h.fos](client_gui_h.fos.md)
- [client_online_stats.fos](client_online_stats.fos.md)
- [client_screens.fos](client_screens.fos.md)
- [client_spawn_npc.fos](client_spawn_npc.fos.md)

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __CLIENT |  | scriptable client-side gui extended-edition Compile with -client switch |

## Classes

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
| mouseX | `int` |  |  |
| mouseY | `int` |  |  |

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
int Right()  { return Left() + Width();  }
```

#### Bottom
```angelscript
int Bottom() { return Top() + Height(); }
```

#### Height
```angelscript
int Height() { return height; }
```

#### Width
```angelscript
int Width()  { return width; }
```

#### Position
```angelscript
IControl@ Position(int x, int y) { left = x; top = y; return this; }
```

#### Left
```angelscript
IControl@ Left(int x)            { left = x; return this; }
```

#### Top
```angelscript
IControl@ Top(int y)             { top = y; return this; }
```

#### Width
```angelscript
IControl@ Width(int w)           { width = w; return this; }
```

#### Height
```angelscript
IControl@ Height(int h)          { height = h; return this; }
```

#### Size
```angelscript
IControl@ Size(int w, int h)     { height = h; width = w; return this; }
```

#### Position
```angelscript
IControl@ Position(string& iniKey)
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
void Enable()
```

#### Disable
```angelscript
void Disable()
```

#### Show
 Showing/hiding 

```angelscript
void Show(bool showAll = false)
```

#### Show
```angelscript
void Show(int left, int top)
```

#### Hide
```angelscript
void Hide()
```

#### ShowWindow
```angelscript
void ShowWindow()
```

#### ShowWindow
```angelscript
void ShowWindow(int x, int y)
```

#### HideWindow
```angelscript
void HideWindow()
```

#### Center
* * Centers control in parent control. 

```angelscript
void Center()
```

#### Init
```angelscript
void Init()
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
bool MouseDown(int x, int y, int click)
```

#### MouseUp
```angelscript
bool MouseUp(int x, int y, int click)
```

#### MouseMove
```angelscript
void MouseMove(int fromX, int fromY, int toX, int toY)
```

#### KeyDown
```angelscript
bool KeyDown(uint8 key,string& keyText)
```

#### KeyUp
```angelscript
void KeyUp(uint8 key,string& keyText)
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

#### OnShow
 Called when control is shown 

```angelscript
void OnShow()
```

#### OnHide
 Called when control is being hidden. 

```angelscript
void OnHide()
```

#### OnEnabled
 Called when contorl is being enabled 

```angelscript
void OnEnabled()
```

#### OnDisabled
 Called when control is being disabled 

```angelscript
void OnDisabled()
```

### CButton

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| caption | `string` |  |  |
| spriteUp | `[Sprite](sprite.fos.md)` |  |  |
| spriteDown | `[Sprite](sprite.fos.md)` |  |  |
| textBorder | `int` |  |  |

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

#### set_Caption
```angelscript
void set_Caption(string@ caption)
```

#### get_Caption
```angelscript
string@ get_Caption()
```

#### SetColor
```angelscript
void SetColor(uint color)
```

#### set_Color
```angelscript
void set_Color(uint color)
```

#### SetFont
```angelscript
void SetFont(uint font)
```

#### set_Font
```angelscript
void set_Font(uint font)
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
| maxlength | `uint` |  |  |

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

#### SetMaxLength
```angelscript
void SetMaxLength(uint ml)
```

#### ShowCursor
 Shows/hides cursor in drawnText (0 - invisible, 1/2 - visible (switching)) 

```angelscript
void ShowCursor(int show)
```

#### RefreshDrawnText
 Refreshes the drawn text 

```angelscript
void RefreshDrawnText()
```

#### InsertChar
 Inserts character corresponding with pressed key 

```angelscript
void InsertChar(uint8 key, string& keyText)
```

#### Draw
```angelscript
void Draw()
```

#### KeyDown
```angelscript
bool KeyDown(uint8 key,string& keyText)
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

### CSpriteEx

////////// Draws something customizable //////////

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| index | `int` |  |  |
| scratch | `bool` |  |  |
| center | `bool` |  |  |
| color | `uint` |  |  |
| applyOffsets | `bool` |  |  |

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

### CContextButton

 Control connected to some critter/item/hex depending on context 

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| crId | `uint` |  |  |
| itemId | `uint` |  |  |
| hexX | `uint16` |  |  |
| hexY | `uint16` |  |  |

**Methods**

#### SetCritter
 Assigns critter 

```angelscript
void SetCritter(CritterCl@ cr)
```

#### SetItem
 Assigns item 

```angelscript
void SetItem(ItemCl@ item)
```

#### SetHex
 Assign hex 

```angelscript
void SetHex(uint16 x, uint16 y)
```

### Window

 Base class for new windows 

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| screen | `IGUIScreenOpt@` |  |  |
| autoMode | `bool` |  |  |

**Methods**

#### Left
```angelscript
int Left()   { return screen.GetPosX(); }
```

#### Top
```angelscript
int Top()    { return screen.GetPosY(); }
```

#### Width
```angelscript
int Width()  { return screen.GetWidth(); }
```

#### Height
```angelscript
int Height() { return screen.GetHeight(); }
```

#### Init
```angelscript
void Init()
```

#### Position
```angelscript
IControl@ Position(int x, int y)
```

#### Size
```angelscript
IControl@ Size(int w, int h)
```

#### Center
* * Centers window on screen. 

```angelscript
void Center()
```

#### OnShow
small compatilibity part with vanilla code...

```angelscript
void OnShow(int p0, int p1, int p2)
```

#### Show
```angelscript
void Show(int x, int y)
```

#### ShowWindow
for use when access to parent-screen is needed via control

```angelscript
void ShowWindow()
```

#### ShowWindow
```angelscript
void ShowWindow(int x, int y)
```

#### HideWindow
```angelscript
void HideWindow()
```

#### OnLostFocus
```angelscript
void OnLostFocus()
```

#### MouseDown
```angelscript
bool MouseDown(int x, int y, int click)
```

#### Auto
* * If in auto mode window uses previous values to spawn critter. 

```angelscript
void Auto(bool v) { autoMode = v; }
```

#### Auto
```angelscript
bool Auto()       { return autoMode; }
```


