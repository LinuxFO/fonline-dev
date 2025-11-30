---
title: car_seller.fos
description: " FOnline: 2238 Rotators  car_seller.fos ..."
---

# car_seller.fos


FOnline: 2238
Rotators

car_seller.fos


## Includes

- `_entires.fos`
- `_macros.fos`
- `economy_h.fos`
- `entire.fos`
- `logging_h.fos`
- `MsgStr.h`
- `serializator.fos`
- `utils_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| FD_NO_MONEY | `(5)` |  |
| FD_NO_PLACES | `(6)` |  |
| FD_BUY_SUCCESS_WORKSHOP | `(7)` |  |
| FD_BUY_SUCCESS_CARSTOP | `(8)` |  |
| FD_MODIFY_NO_MONEY | `(37)` |  |
| FD_MODIFY_NO_NEED | `(38)` |  |
| FD_GENERIC_ERROR | `(100)` |  |
| FD_TAKE_KEY_IN_HAND | `(101)` |  |
| FD_CAR_NOT_FOUND | `(102)` |  |
| FD_TAKE_KEY_IN_HAND2 | `(103)` |  |
| STR_BUY_LIST | `(2100)` |  |
| STR_COST_HUMMER | `(2101)` |  |
| STR_COST_BUGGY | `(2102)` |  |
| STR_COST_SCOUT | `(2103)` |  |
| STR_COST_HIGHWAYMAN | `(2104)` |  |
| STR_COST_COCKROACH | `(2105)` |  |
| CAR_HUMMER | `(0)` |  |
| CAR_BUGGY | `(1)` |  |
| CAR_SCOUT | `(2)` |  |
| CAR_HIGHWAYMAN | `(3)` |  |
| CAR_COCKROACH | `(4)` |  |
| CAR_CARAVAN_ORANGE | `(5)` |  |
| CAR_CARAVAN_WHITE | `(6)` |  |
| CAR_POLICE_CAR | `(7)` |  |
| CAR_MOTORCYCLE | `(8)` |  |
| CAR_FIRETRUCK | `(9)` |  |
| CAR_TRUCK | `(10)` |  |
| CAR_CORVEGA | `(11)` |  |
| CAR_COUNT | `(12)` |  |
| CAR_PRICE_UPDATE_INTERVAL | `(REAL_MINUTE(30))` |  |
| CAR_MINIMUM_PRICE | `(5000)` |  |
| KEY_COPY_COST | `(1000)` |  |
| CARS_INIT_ID | `(50000)` |  |
| CARS_SOLD | `(GetGvar(GVAR_car_id) - CARS_INIT_ID)` |  |

## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| CarPrices | `array<int>` |  |  |
| serializer | `[Serializator](serializator.fos.md)` |  |  |

## Functions

### InitCars

```angelscript
void InitCars()
```

### SetPrice

```angelscript
void SetPrice(uint index, int value)
```

### GetPrice

```angelscript
int GetPrice(uint index)
```

### e_UpdateCarPrices

```angelscript
uint e_UpdateCarPrices(array<uint>@ values)
```

### PidToIndex

```angelscript
uint PidToIndex(uint16 protoCar)
```

### ChangeCarPrice

```angelscript
void ChangeCarPrice(uint16 protoCar, int sum)
```

### LoadCarPriceData

```angelscript
void LoadCarPriceData()
```

### SaveCarPriceData

```angelscript
void SaveCarPriceData()
```

### PidToStr

```angelscript
string PidToStr(uint16 protoCar)
```

### GetCarCost

```angelscript
uint GetCarCost(uint16 protoCar)
```

### GetFuelCost

```angelscript
int GetFuelCost(Item@ car)
```

### GetWearCost

```angelscript
int GetWearCost(Item@ car)
```

### GetBioCost

```angelscript
int GetBioCost(Item@ car)
```

### dlg_PrepareBuy

```angelscript
void dlg_PrepareBuy(Critter& player, Critter@ tray, string@ lexems)
```

### r_BuyHummer

```angelscript
uint r_BuyHummer(Critter& player, Critter@ tray, int val)
```

### r_BuyBuggy

```angelscript
uint r_BuyBuggy(Critter& player, Critter@ tray, int val)
```

### r_BuyScout

```angelscript
uint r_BuyScout(Critter& player, Critter@ tray, int val)
```

### r_BuyHighwayman

```angelscript
uint r_BuyHighwayman(Critter& player, Critter@ tray, int val)
```

### r_BuyCockroach

```angelscript
uint r_BuyCockroach(Critter& player, Critter@ tray, int val)
```

### r_BuyCaravanWhite

```angelscript
uint r_BuyCaravanWhite(Critter& player, Critter@ tray, int val)
```

### r_BuyCaravanOrange

```angelscript
uint r_BuyCaravanOrange(Critter& player, Critter@ tray, int val)
```

### r_BuyPoliceCar

```angelscript
uint r_BuyPoliceCar(Critter& player, Critter@ tray, int val)
```

### r_BuyMotorcycle

```angelscript
uint r_BuyMotorcycle(Critter& player, Critter@ tray, int val)
```

### r_BuyFiretruck

```angelscript
uint r_BuyFiretruck(Critter& player, Critter@ tray, int val)
```

### r_BuyTruck

```angelscript
uint r_BuyTruck(Critter& player, Critter@ tray, int val)
```

### r_BuyCorvega

```angelscript
uint r_BuyCorvega(Critter& player, Critter@ tray, int val)
```

### d_CanAffordCockroach

```angelscript
bool d_CanAffordCockroach(Critter& player, Critter@ someone)
```

### d_CanAffordPoliceCar

```angelscript
bool d_CanAffordPoliceCar(Critter& player, Critter@ someone)
```

### d_CanAffordMotorcycle

```angelscript
bool d_CanAffordMotorcycle(Critter& player, Critter@ someone)
```

### d_CanAffordFiretruck

```angelscript
bool d_CanAffordFiretruck(Critter& player, Critter@ someone)
```

### d_CanAffordTruck

```angelscript
bool d_CanAffordTruck(Critter& player, Critter@ someone)
```

### d_CanAffordCorvega

```angelscript
bool d_CanAffordCorvega(Critter& player, Critter@ someone)
```

### d_CanNotAffordCockroach

```angelscript
bool d_CanNotAffordCockroach(Critter& player, Critter@ someone)
```

### d_CanAffordCaravanWhite

```angelscript
bool d_CanAffordCaravanWhite(Critter& player, Critter@ tray)
```

### d_CanAffordCaravanOrange

```angelscript
bool d_CanAffordCaravanOrange(Critter& player, Critter@ tray)
```

### d_CanNotAffordCaravanWhite

```angelscript
bool d_CanNotAffordCaravanWhite(Critter& player, Critter@ tray)
```

### d_CanNotAffordCaravanOrange

```angelscript
bool d_CanNotAffordCaravanOrange(Critter& player, Critter@ tray)
```

### TryCreateCar

```angelscript
uint TryCreateCar(Critter& player, uint16 protoCar)
```

### GetPlayerKey

```angelscript
Item@ GetPlayerKey(Critter@ player)
```

### GetPlayerCar

```angelscript
Item@ GetPlayerCar(Critter@ player)
```

### GetPlayerCar

```angelscript
Item@ GetPlayerCar(Critter@ player, uint& force)
```

### r_CheckCar

```angelscript
uint r_CheckCar(Critter& player, Critter@ tray, int val)
```

### dlg_SellCar

```angelscript
void dlg_SellCar(Critter& player, Critter@ tray, string@ lexems)
```

### r_SellCar

```angelscript
void r_SellCar(Critter& player, Critter@ tray, int val)
```

### dlg_Fuel

```angelscript
void dlg_Fuel(Critter& player, Critter@ tray, string@ lexems)
```

### dlg_Wear

```angelscript
void dlg_Wear(Critter& player, Critter@ tray, string@ lexems)
```

### dlg_Bio

```angelscript
void dlg_Bio(Critter& player, Critter@ tray, string@ lexems)
```

### r_DoFuel

```angelscript
uint r_DoFuel(Critter& player, Critter@ tray, int val)
```

### r_DoWear

```angelscript
uint r_DoWear(Critter& player, Critter@ tray, int val)
```

### r_DoBio

```angelscript
uint r_DoBio(Critter& player, Critter@ tray, int val)
```

### r_CopyKey

```angelscript
uint r_CopyKey(Critter& player, Critter@ tray, int val)
```


