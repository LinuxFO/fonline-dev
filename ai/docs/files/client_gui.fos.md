---
title: client_gui.fos
description: " FOnline: 2238 Rotators  client_gui.fos ..."
---

# client_gui.fos


FOnline: 2238
Rotators

client_gui.fos


## Includes

- `client_gui_h.fos`
- `_client_defines.fos`
- `sprite.fos`
- `_colors.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| CLIENT_GUI |  |  |
| REMOVE_FROM_ARRAY | `\` |  |
| IS_COLLISION | `# (x1, y1, x2, y2, w, h)((x1) >= (x2) && (x1) <= (x2) + (w) && (y1) >= (y2) && (y1) <= (y2) + (h))` |  |

## Classes

### GUIScreen

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| Index | `int` |  | Data |
| PosX | `int` |  |  |
| PosY | `int` |  |  |
| width | `int` |  |  |
| height | `int` |  |  |
| Surface | `[Sprite](sprite.fos.md)` |  | int LastX; int LastY; |
| IsCanMove | `bool` |  |  |
| IsModal | `bool` |  |  |
| IsMultiinstance | `bool` |  |  |
| IsIgnoreBorders | `bool` |  |  |
| IsCloseOnMiss | `bool` |  |  |
| IsAutoCursor | `bool` |  |  |
| IsHardcoded | `bool` |  |  |
| IsLMouseDown | `bool` |  |  |
| AutoCursorType | `int` |  |  |
| AutoCursorPrev | `int` |  |  |
| CallbackShow | `IGUIScreenCallbackShow@` |  |  |
| CallbackHide | `IGUIScreenCallbackHide@` |  |  |
| CallbackMove | `IGUIScreenCallbackMove@` |  |  |
| CallbackFocus | `IGUIScreenCallbackFocus@` |  |  |
| CallbackMouseDown | `IGUIScreenCallbackMouseDown@` |  |  |
| CallbackKeyPress | `IGUIScreenCallbackKeyPress@` |  |  |
| screenControl | `IControl@` |  | main control container for all screen child-controls |

**Methods**

#### Draw
```angelscript
void Draw()
```

#### Update
```angelscript
void Update(uint dt)
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
bool KeyDown(uint8 key, string& keyText)
```

#### InputLost
```angelscript
void InputLost()
```

#### Control
```angelscript
IControl@ Control()
```

#### Control
```angelscript
void Control(IControl@ control)
```

#### SetCallbackShow
Options

```angelscript
void SetCallbackShow(IGUIScreenCallbackShow@ callback)   { @CallbackShow = callback;  }
```

#### SetCallbackHide
```angelscript
void SetCallbackHide(IGUIScreenCallbackHide@ callback)   { @CallbackHide = callback;  }
```

#### SetCallbackMove
```angelscript
void SetCallbackMove(IGUIScreenCallbackMove@ callback)   { @CallbackMove = callback;  }
```

#### SetCallbackFocus
```angelscript
void SetCallbackFocus(IGUIScreenCallbackFocus@ callback) { @CallbackFocus = callback;  }
```

#### SetCallbackMouseDown
```angelscript
void SetCallbackMouseDown(IGUIScreenCallbackMouseDown@ callback){@CallbackMouseDown=callback; }
```

#### SetCallbackKeyPress
```angelscript
void SetCallbackKeyPress(IGUIScreenCallbackKeyPress@ callback){@CallbackKeyPress=callback; }
```

#### Position
```angelscript
void Position(int x, int y)                   { PosX = x; PosY = y;  }
```

#### Size
```angelscript
void Size(int w, int h)                       { width = w; height = h;  }
```

#### CanMove
```angelscript
void CanMove(bool enabled)                    { IsCanMove = enabled;  }
```

#### Modal
```angelscript
void Modal(bool enabled)                      { IsModal = enabled;  }
```

#### Multiinstance
```angelscript
void Multiinstance(bool enabled)              { IsMultiinstance = enabled;  }
```

#### IgnoreBorders
```angelscript
void IgnoreBorders(bool enabled)              { IsIgnoreBorders = enabled;  }
```

#### CloseOnMiss
```angelscript
void CloseOnMiss(bool enabled)                { IsCloseOnMiss = enabled;  }
```

#### AutoCursor
```angelscript
void AutoCursor(bool enabled, int cursorType) { IsAutoCursor = enabled; AutoCursorType = cursorType;  }
```

#### Hardcoded
```angelscript
void Hardcoded(bool enabled)                  { IsHardcoded = enabled;  }
```

#### GetPosX
Info

```angelscript
int GetPosX()   { return PosX; }
```

#### GetPosY
```angelscript
int GetPosY()   { return PosY; }
```

#### GetWidth
```angelscript
int GetWidth()  { return width != 0 ? width : Surface.Width; }
```

#### GetHeight
```angelscript
int GetHeight() { return height != 0 ? height : Surface.Height; }
```

#### GetIndex
```angelscript
int GetIndex()  { return Index; }
```

### GUIElement

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| id | `int` |  | Data |
| elementWidth | `uint` |  |  |
| elementHeight | `uint` |  |  |
| posX | `int` |  |  |
| posY | `int` |  |  |
| mousePosX | `int` |  |  |
| mousePosY | `int` |  |  |
| screenX | `int` |  |  |
| screenY | `int` |  |  |
| isFocused | `bool` |  |  |
| visible | `bool` |  |  |
| collisionTransparent | `bool` |  |  |
| absolutePosition | `bool` |  |  |
| readyForClickEvent | `bool` |  |  |
| callbackInit | `IGUIElementCallbackInit@` |  |  |
| callbackDraw | `IGUIElementCallbackDraw@` |  |  |
| callbackMouseDown | `IGUIElementCallbackMouseDown@` |  |  |
| callbackMouseClick | `IGUIElementCallbackMouseClick@` |  |  |
| callbackKeyPress | `IGUIElementCallbackKeyPress@` |  |  |
| callbackMouseMove | `IGUIElementCallbackMouseMove@` |  |  |
| callbackValueChange | `IGUIElementCallbackValueChange@` |  |  |
| callbackStateChange | `IGUIElementCallbackStateChange@` |  |  |

**Methods**

#### InitGUIElement
```angelscript
void InitGUIElement(int x, int y, int width, int height)
```

#### Draw
```angelscript
void Draw(int screenX, int screenY)
```

#### Update
```angelscript
void Update(uint dt)
```

#### MouseDown
```angelscript
void MouseDown(int click)
```

#### MouseUp
```angelscript
void MouseUp(int click, bool isCollision)
```

#### MouseMove
```angelscript
void MouseMove(int x, int y)
```

#### KeyPress
bool KeyPress(uint8 key)

```angelscript
bool KeyPress( uint8 key, string& keyText )
```

#### KeyUp
```angelscript
void KeyUp(uint8 key)
```

#### InputLost
```angelscript
void InputLost()
```

#### GetNewInstance
```angelscript
IGUIElementOpt@ GetNewInstance()
```

#### CallbackInit
Options

```angelscript
void CallbackInit(IGUIElementCallbackInit@ callback) { @callbackInit=callback;  }
```

#### CallbackDraw
```angelscript
void CallbackDraw(IGUIElementCallbackDraw@ callback) { @callbackDraw=callback;  }
```

#### CallbackMouseDown
```angelscript
void CallbackMouseDown(IGUIElementCallbackMouseDown@ callback) { @callbackMouseDown=callback;  }
```

#### CallbackMouseClick
```angelscript
void CallbackMouseClick(IGUIElementCallbackMouseClick@ callback) { @callbackMouseClick=callback;  }
```

#### CallbackKeyPress
```angelscript
void CallbackKeyPress(IGUIElementCallbackKeyPress@ callback) { @callbackKeyPress=callback;  }
```

#### CallbackMouseMove
```angelscript
void CallbackMouseMove(IGUIElementCallbackMouseMove@ callback) { @callbackMouseMove=callback;  }
```

#### Position
```angelscript
void Position(int x, int y)
```

#### Position
```angelscript
void Position(int x, int y, int w, int h)
```

#### Position
```angelscript
void Position(string& iniKey)
```

#### Visible
```angelscript
void Visible(bool visible)
```

#### AbsolutePosition
```angelscript
void AbsolutePosition(bool absolutePosition)
```

#### AbsolutePosition
```angelscript
void AbsolutePosition(int x, int y)
```

#### CollisionTransparent
```angelscript
void CollisionTransparent(bool collisionTransparent)
```

#### AddText
```angelscript
void AddText(int id, string@ text, int x, int y, int width, int height, int font, uint color, int flags)
```

#### AddImage
```angelscript
void AddImage(int id, string@ sprName, int x, int y)
```

#### AddImage
```angelscript
void AddImage(int id, int patch, string@ sprName, int x, int y)
```

#### SetFocused
```angelscript
void SetFocused(bool state)
```

#### SetVisible
```angelscript
void SetVisible(bool visible)
```

#### SetAbsolutePosition
```angelscript
void SetAbsolutePosition(bool absolutePosition)
```

#### SetCollisionTransparent
```angelscript
void SetCollisionTransparent(bool collisionTransparent)
```

#### GetCallbackInit
```angelscript
IGUIElementCallbackInit@ GetCallbackInit()
```

#### GetId
Info

```angelscript
int GetId() { return id; }
```

#### GetPosX
```angelscript
int GetPosX() { return posX; }
```

#### GetPosY
```angelscript
int GetPosY() { return posY; }
```

#### GetWidth
```angelscript
int GetWidth() { return elementWidth; }
```

#### GetHeight
```angelscript
int GetHeight() { return elementHeight; }
```

#### IsFocused
```angelscript
bool IsFocused() { return isFocused; }
```

#### IsAbsolutePosition
```angelscript
bool IsAbsolutePosition() { return absolutePosition; }
```

#### IsCollisionTransparent
```angelscript
bool IsCollisionTransparent() { return collisionTransparent; }
```

#### IsCollision
```angelscript
bool IsCollision(int screenX, int screenY, int mouseX, int mouseY)
```

#### IsVisible
```angelscript
bool IsVisible()
```

### GUIElementText

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| text | `string` |  |  |
| font | `int` |  |  |
| dX | `int` |  |  |
| dY | `int` |  |  |
| upDX | `int` |  |  |
| upDY | `int` |  |  |
| downDX | `int` |  |  |
| downDY | `int` |  |  |
| textColor | `uint` |  |  |
| textColorUp | `uint` |  |  |
| textColorFocused | `uint` |  |  |
| textColorDown | `uint` |  |  |
| textFlags | `int` |  |  |

**Methods**

#### InitText
```angelscript
void InitText(int id, string@ text, int x, int y, int width, int height, int font, uint color, uint colorDown, int flags)
```

#### Draw
```angelscript
void Draw(int screenX, int screenY)
```

#### Position
```angelscript
void Position(int x, int y)
```

#### Position
```angelscript
void Position(int x, int y, int w, int h)
```

#### Position
```angelscript
void Position(string& iniKey)
```

#### AbsolutePosition
```angelscript
void AbsolutePosition(int x, int y)
```

#### AbsolutePosition
```angelscript
void AbsolutePosition(bool absolutePosition)
```

#### Visible
```angelscript
void Visible(bool visible)
```

#### Text
```angelscript
void Text(string@ text)
```

#### Text
```angelscript
void Text(string@ text, int font, uint color)
```

#### Text
```angelscript
void Text(string@ text, int font, uint color, int flags)
```

#### Text
```angelscript
void Text(string@ text, int font, uint color, uint downColor, int flags)
```

#### TextBoxSize
```angelscript
void TextBoxSize(int width, int height)
```

#### TextOptions
```angelscript
void TextOptions(int font, uint color)
```

#### TextOptions
```angelscript
void TextOptions(int font, uint color, int flags)
```

#### TextOptions
```angelscript
void TextOptions(int font, uint color, uint colorDown, int flags)
```

#### TextColor
```angelscript
void TextColor(uint color)
```

#### SetTextShift
```angelscript
void SetTextShift(int deltaX, int deltaY, int deltaDownX, int deltaDownY)
```

#### SetTextWidth
```angelscript
void SetTextWidth(int width)
```

#### SetTextDown
```angelscript
void SetTextDown(bool down)
```

#### SetText
```angelscript
void SetText(string& text)
```

#### SetVisible
```angelscript
void SetVisible(bool visible)
```

#### SetFocused
```angelscript
void SetFocused(bool state)
```

#### GetId
```angelscript
int GetId()
```

#### GetText
```angelscript
string@ GetText()
```

#### GetFont
```angelscript
int GetFont()
```

#### GetTextColor
```angelscript
uint GetTextColor()
```

#### IsVisible
```angelscript
bool IsVisible()
```

#### CallbackMouseMove
```angelscript
void CallbackMouseMove(IGUIElementCallbackMouseMove@ callback) { @callbackMouseMove=callback;  }
```

#### CallbackInit
```angelscript
void CallbackInit(IGUIElementCallbackInit@ callback) { @callbackInit=callback;  }
```

#### CallbackDraw
```angelscript
void CallbackDraw(IGUIElementCallbackDraw@ callback) { @callbackDraw=callback;  }
```

#### CallbackMouseDown
```angelscript
void CallbackMouseDown(IGUIElementCallbackMouseDown@ callback) { @callbackMouseDown=callback;  }
```

#### CallbackMouseClick
```angelscript
void CallbackMouseClick(IGUIElementCallbackMouseClick@ callback) { @callbackMouseClick=callback;  }
```

### GUIElementImage

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| image | `[Sprite](sprite.fos.md)` |  |  |
| patch | `int` |  |  |

**Methods**

#### InitImage
```angelscript
void InitImage(int id, string@ sprName, int patch, int x, int y)
```

#### Draw
```angelscript
void Draw(int screenX, int screenY)
```

#### Position
```angelscript
void Position(int x, int y)
```

#### Position
```angelscript
void Position(int x, int y, int w, int h)
```

#### Position
```angelscript
void Position(string& iniKey)
```

#### AbsolutePosition
```angelscript
void AbsolutePosition(bool absolutePosition)
```

#### Visible
```angelscript
void Visible(bool visible)
```

#### SetPosX
```angelscript
void SetPosX(int x)
```

#### SetPosY
```angelscript
void SetPosY(int y)
```

#### SetVisible
```angelscript
void SetVisible(bool visible)
```

#### SetFocused
```angelscript
void SetFocused(bool state)
```

#### GetPosX
```angelscript
int GetPosX()
```

#### GetPosY
```angelscript
int GetPosY()
```

#### GetImageWidth
```angelscript
int GetImageWidth()
```

#### GetImageHeight
```angelscript
int GetImageHeight()
```

#### IsCollision
```angelscript
bool IsCollision(int screenX, int screenY, int mouseX, int mouseY)
```

#### IsVisible
```angelscript
bool IsVisible()
```

#### CallbackInit
```angelscript
void CallbackInit(IGUIElementCallbackInit@ callback) { @callbackInit=callback;  }
```

#### CallbackDraw
```angelscript
void CallbackDraw(IGUIElementCallbackDraw@ callback) { @callbackDraw=callback;  }
```

#### CallbackMouseDown
```angelscript
void CallbackMouseDown(IGUIElementCallbackMouseDown@ callback) { @callbackMouseDown=callback;  }
```

#### CallbackMouseClick
```angelscript
void CallbackMouseClick(IGUIElementCallbackMouseClick@ callback) { @callbackMouseClick=callback;  }
```

### GUIElementButton

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| isDown | `bool` |  |  |

**Methods**

#### CallbackInit
```angelscript
void CallbackInit(IGUIElementCallbackInit@ callback) { @callbackInit=callback;  }
```

#### CallbackDraw
```angelscript
void CallbackDraw(IGUIElementCallbackDraw@ callback) { @callbackDraw=callback;  }
```

#### CallbackMouseDown
```angelscript
void CallbackMouseDown(IGUIElementCallbackMouseDown@ callback) { @callbackMouseDown=callback;  }
```

#### CallbackMouseClick
```angelscript
void CallbackMouseClick(IGUIElementCallbackMouseClick@ callback) { @callbackMouseClick=callback;  }
```

#### Draw
```angelscript
void Draw(int screenX, int screenY)
```

#### Position
```angelscript
void Position(int x, int y)
```

#### Position
```angelscript
void Position(int x, int y, int w, int h)
```

#### Position
```angelscript
void Position(string& iniKey)
```

#### AbsolutePosition
```angelscript
void AbsolutePosition(bool absolutePosition)
```

#### Visible
```angelscript
void Visible(bool visible)
```

#### Text
```angelscript
void Text(string@ text)
```

#### Text
```angelscript
void Text(string@ text, int font, uint color)
```

#### Text
```angelscript
void Text(string@ text, int font, uint color, int flags)
```

#### Text
```angelscript
void Text(string@ text, int font, uint color, uint downColor, int flags)
```

#### TextShift
```angelscript
void TextShift(int deltaX, int deltaY, int deltaDownX, int deltaDownY)
```

#### TextWidth
```angelscript
void TextWidth(int width)
```

#### UpPic
```angelscript
void UpPic(string@ sprName)
```

#### DownPic
```angelscript
void DownPic(string@ sprName)
```

#### ClickableZone
```angelscript
void ClickableZone(int width, int height)
```

#### ClickableZone
```angelscript
void ClickableZone(int x, int y, int width, int height)
```

#### SetVisible
```angelscript
void SetVisible(bool visible)
```

#### SetFocused
```angelscript
void SetFocused(bool state)
```

#### UpdateelementsPositions
private functions

```angelscript
void UpdateelementsPositions()
```

#### IsVisible
```angelscript
bool IsVisible()
```


## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| KeyPressed | `array<bool>` |  |  |
| LastScreenOpt | `IGUIScreenOpt@` | `null` |  |

## Functions

### GUI_IsKeyPressed

```angelscript
bool GUI_IsKeyPressed(uint8 key)
```

### GUI_GetIniCoords

```angelscript
void GUI_GetIniCoords(string& ini, int& left, int& top, int& right, int& bottom)
```

### GUI_CreateScreen

Create new screen

```angelscript
IGUIScreenOpt@ GUI_CreateScreen(int screenIndex, string@ sprName)
```

### GUI_DeleteScreen

Delete old screen, hardcoded screens included

```angelscript
void GUI_DeleteScreen(int screenIndex)
```

### GUI_GetScreenOptions

Valid only on IGUIScreenCallbackShow::OnShow callback

```angelscript
IGUIScreenOpt@ GUI_GetScreenOptions()
```

### GUI_Init

```angelscript
void GUI_Init()
```

### GUI_GetActiveMainScreen

```angelscript
int GUI_GetActiveMainScreen()
```

### GUI_GetActiveScreen

```angelscript
int GUI_GetActiveScreen()
```

### GUI_GetActiveScreens

```angelscript
void GUI_GetActiveScreens(array<int>& result)
```

### GUI_GetMainScreen

```angelscript
int GUI_GetMainScreen()
```

### GUI_GetScreen

```angelscript
IGUIScreenOpt@ GUI_GetScreen(int screenIndex)
```

### GUI_ShowScreen

```angelscript
void GUI_ShowScreen(int screenIndex, int p0, int p1, int p2)
```

### GUI_HideScreen

```angelscript
void GUI_HideScreen(int screenIndex, int p0, int p1, int p2)
```

### GUI_Render

```angelscript
void GUI_Render( bool mainScreen )
```

### GUI_Update

```angelscript
void GUI_Update(uint dt)
```

### GUI_MouseDown

```angelscript
bool GUI_MouseDown(int x, int y, int click)
```

### GUI_MouseUp

```angelscript
bool GUI_MouseUp(int x, int y, int click)
```

### GUI_MouseMove

```angelscript
void GUI_MouseMove(int fromX, int fromY, int toX, int toY)
```

### GUI_KeyDown

```angelscript
bool GUI_KeyDown(uint8 key,string& keyText)
```

### GUI_KeyUp

```angelscript
bool GUI_KeyUp(uint8 key,string& keyText)
```

### GUI_InputLost

```angelscript
void GUI_InputLost()
```

### CreateScreen

```angelscript
IGUIScreenOpt@ CreateScreen(int screenIndex, string@ sprName)
```

### DeleteScreen

```angelscript
void DeleteScreen(int screenIndex)
```

### GetScreen

```angelscript
GUIScreen@ GetScreen(int screenIndex)
```

### GetActiveScreen

```angelscript
GUIScreen@ GetActiveScreen(int screenIndex)
```

### ProcessKey

KeybData@ k = KbData[key]; if(!(k is null)) { bool shiftDown = (KeyPressed[DIK_LSHIFT] || KeyPressed[DIK_RSHIFT]); uint len = text.length(); text.resize(len + 1); text[len] = k.Char[::GetKeybLang() * 2 + (shiftDown ? 1 : 0)]; letter = text[len]; return true; } return false; } 

```angelscript
bool ProcessKey(uint8 key, string& keyText, string& text)
```

### GUI_AddText

```angelscript
IGUIElementTextOpt@ GUI_AddText(int screenIndex)
```

### GUI_AddText

```angelscript
IGUIElementTextOpt@ GUI_AddText(int screenIndex, string@ text, int x, int y)
```

### GUI_AddImage

```angelscript
IGUIElementImageOpt@	GUI_AddImage(int screenIndex)
```

### GUI_AddImage

```angelscript
IGUIElementImageOpt@ GUI_AddImage(int screenIndex, string@ sprName, int patch, int x, int y)
```

### GUI_AddButton

```angelscript
IGUIElementButtonOpt@ GUI_AddButton(int screenIndex)
```

### GUI_AddButton

```angelscript
IGUIElementButtonOpt@ GUI_AddButton(int screenIndex, int x, int y)
```


