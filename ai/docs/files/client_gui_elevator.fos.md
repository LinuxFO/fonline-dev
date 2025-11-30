---
title: client_gui_elevator.fos
description: " FOnline: 2238 Rotators  client_gui_elevator.fos ..."
---

# client_gui_elevator.fos


FOnline: 2238
Rotators

client_gui_elevator.fos


## Included By

- [client_main.fos](client_main.fos.md)

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __CLIENT |  | elevator winow override Compile with -client switch |

## Classes

### CElevatorButton

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| spriteDown | `[Sprite](sprite.fos.md)` |  |  |
| floor | `uint8` |  |  |

**Methods**

#### get_Floor
```angelscript
uint8 get_Floor() { return floor; }
```

#### Draw
 Draw only when pressed 

```angelscript
void Draw()
```

#### Click
```angelscript
void Click()
```

### CElevatorScreen

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| bos | `[Sprite](sprite.fos.md)` |  | pictures // intrface.lst index |
| mast1 | `[Sprite](sprite.fos.md)` |  |  |
| mast2 | `[Sprite](sprite.fos.md)` |  |  |
| mil1 | `[Sprite](sprite.fos.md)` |  |  |
| mil2 | `[Sprite](sprite.fos.md)` |  |  |
| vault | `[Sprite](sprite.fos.md)` |  |  |
| bos2 | `[Sprite](sprite.fos.md)` |  |  |
| mil3 | `[Sprite](sprite.fos.md)` |  |  |
| mil4 | `[Sprite](sprite.fos.md)` |  |  |
| mb | `[Sprite](sprite.fos.md)` |  |  |
| indicator | `[Sprite](sprite.fos.md)` |  |  |
| mainPic | `uint` |  |  |
| addPic | `uint` |  |  |
| type | `uint` |  | elevator type |
| currFloor | `uint` |  | current floor (the one showed when you enter lift) |
| floors | `uint` |  | level count |
| target | `uint` |  | target floor |
| indicatorPos | `uint` |  |  |
| lastUpdate | `uint` |  | last update time |
| running | `bool` |  |  |

**Methods**

#### set_Type
```angelscript
void set_Type(uint val)
```

#### get_Type
```angelscript
uint get_Type() { return type; }
```

#### set_CurrFloor
```angelscript
void set_CurrFloor(uint val)
```

#### get_CurrFloor
```angelscript
uint get_CurrFloor() { return currFloor; }
```

#### GetIndicatorPos
returns indicator position for given floor

```angelscript
uint GetIndicatorPos(uint floor)
```

#### GetFloorFromIndicator
gets curr floor basing on indicator, if in between, returns -1

```angelscript
int GetFloorFromIndicator()
```

#### Init
```angelscript
void Init()
```

#### OnShow
```angelscript
void OnShow()
```

#### KeyDown
```angelscript
bool KeyDown(uint8 key)
```

#### Draw
```angelscript
void Draw()
```

#### Update
run elev

```angelscript
void Update()
```

#### Goto
sets elev in motion

```angelscript
void Goto(int floor)
```


## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| ElevatorScreen | `[CElevatorScreen](client_gui_elevator.fos.md)` |  |  |

## Functions

### InitElevatorScreens

```angelscript
void InitElevatorScreens()
```

### ShowElevator

```angelscript
void ShowElevator(int type, int floor, int p2, string@ + p3, array<int>@ + p4)
```


