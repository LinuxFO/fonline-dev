---
title: time.fos
description: " FOnline: 2238 Rotators  time.fos ..."
---

# time.fos


FOnline: 2238
Rotators

time.fos


## Includes

- `_macros.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| STR_MONTH | `# (m)               (20 + (m))` |  |
| STR_DAY_OF_WEEK | `# (dow)       (33 + (dow))` |  |

## Functions

### GetNearFullSecond

```angelscript
uint GetNearFullSecond(uint16 year, uint16 month, uint16 day, uint16 hour, uint16 minute, uint16 second)
```

### GetDaysInMonth

```angelscript
uint GetDaysInMonth(uint16 year, uint16 month)
```

### GetTimeString

```angelscript
string GetTimeString(uint fullsecond)
```

### GetTimeString

```angelscript
string@ GetTimeString(const string& format, uint fullSecond)
```

### GetTimeString

```angelscript
string@ GetTimeString(const string& format, int year, int month, int day, int dayOfWeek, int hour, int minute, int second)
```

### DateTimeToString

Возвращает представление времени в виде строки в формате dd.mm.yy hh:mm. rifleman17

```angelscript
string DateTimeToString(uint gameTime)
```


