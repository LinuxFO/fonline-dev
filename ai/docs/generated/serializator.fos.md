---
title: serializator.fos
description: " FOnline: 2238 Rotators  serializator.fos ..."
---

# serializator.fos


FOnline: 2238
Rotators

serializator.fos


## Included By

- [brahmin_pen_h.fos](brahmin_pen_h.fos.md)
- [car_seller.fos](car_seller.fos.md)
- [caravans_h.fos](caravans_h.fos.md)
- [cheats.fos](cheats.fos.md)
- [economy.fos](economy.fos.md)
- [economy_bank.fos](economy_bank.fos.md)
- [economy_bankaccount.fos](economy_bankaccount.fos.md)
- [faction_data.fos](faction_data.fos.md)
- [factions_bases.fos](factions_bases.fos.md)
- [factions_news.fos](factions_news.fos.md)
- [mercs_h.fos](mercs_h.fos.md)
- [quests.fos](quests.fos.md)
- [reinforcements.fos](reinforcements.fos.md)

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __SERIALIZATOR__ |  |  |
| DEFAULT_GROW | `(128)` |  |

## Classes

### Serializator

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| Array | `array<uint8>` |  |  |
| CurPos | `uint` |  |  |
| BufSize | `uint` |  |  |
| DataSize | `uint` |  |  |

**Methods**

#### GrowBuffer
```angelscript
void GrowBuffer()
```

#### GrowBuffer
```angelscript
void GrowBuffer(uint length)
```

#### Save
```angelscript
bool Save(string& name)
```

#### Load
```angelscript
bool Load(string& name)
```

#### Clear
```angelscript
void Clear()
```

#### SetCurPos
```angelscript
Serializator@ SetCurPos(uint pos)
```

#### Fill
```angelscript
Serializator@ Fill(uint8 value, uint length)
```

#### Set
```angelscript
Serializator@ Set(const int64& value)
```

#### opShl
```angelscript
Serializator@ opShl(const int64& value)
```

#### Set
```angelscript
Serializator@ Set(const int32& value)
```

#### opShl
```angelscript
Serializator@ opShl(const int32& value)
```

#### Set
```angelscript
Serializator@ Set(const int16& value)
```

#### opShl
```angelscript
Serializator@ opShl(const int16& value)
```

#### Set
```angelscript
Serializator@ Set(const int8& value)
```

#### opShl
```angelscript
Serializator@ opShl(const int8& value)
```

#### Set
```angelscript
Serializator@ Set(const uint64& value)
```

#### opShl
```angelscript
Serializator@ opShl(const uint64& value)
```

#### Set
```angelscript
Serializator@ Set(const uint32& value)
```

#### opShl
```angelscript
Serializator@ opShl(const uint32& value)
```

#### Set
```angelscript
Serializator@ Set(const uint16& value)
```

#### opShl
```angelscript
Serializator@ opShl(const uint16& value)
```

#### Set
```angelscript
Serializator@ Set(const uint8& value)
```

#### opShl
```angelscript
Serializator@ opShl(const uint8& value)
```

#### Set
```angelscript
Serializator@ Set(const bool& value)
```

#### opShl
```angelscript
Serializator@ opShl(const bool& value)
```

#### Set
```angelscript
Serializator@ Set(const string& value)
```

#### opShl
```angelscript
Serializator@ opShl(const string& value)
```

#### Set
```angelscript
Serializator@ Set(const float& value)
```

#### opShl
```angelscript
Serializator@ opShl(const float& value)
```

#### Set
```angelscript
Serializator@ Set(const array<int64>& values)
```

#### opShl
```angelscript
Serializator@ opShl(const array<int64>& values)
```

#### Set
```angelscript
Serializator@ Set(const array<int32>& values)
```

#### opShl
```angelscript
Serializator@ opShl(const array<int32>& values)
```

#### Set
```angelscript
Serializator@ Set(const array<int16>& values)
```

#### opShl
```angelscript
Serializator@ opShl(const array<int16>& values)
```

#### Set
```angelscript
Serializator@ Set(const array<int8>& values)
```

#### opShl
```angelscript
Serializator@ opShl(const array<int8>& values)
```

#### Set
```angelscript
Serializator@ Set(const array<uint64>& values)
```

#### opShl
```angelscript
Serializator@ opShl(const array<uint64>& values)
```

#### Set
```angelscript
Serializator@ Set(const array<uint32>& values)
```

#### opShl
```angelscript
Serializator@ opShl(const array<uint32>& values)
```

#### Set
```angelscript
Serializator@ Set(const array<uint16>& values)
```

#### opShl
```angelscript
Serializator@ opShl(const array<uint16>& values)
```

#### Set
```angelscript
Serializator@ Set(const array<uint8>& values)
```

#### opShl
```angelscript
Serializator@ opShl(const array<uint8>& values)
```

#### Set
```angelscript
Serializator@ Set(const array<bool>& values)
```

#### opShl
```angelscript
Serializator@ opShl(const array<bool>& values)
```

#### Set
```angelscript
Serializator@ Set(const array<string>& values)
```

#### opShl
```angelscript
Serializator@ opShl(const array<string>& values)
```

#### Set
```angelscript
Serializator@ Set(const array<float>& values)
```

#### opShl
```angelscript
Serializator@ opShl(const array<float>& values)
```

#### Set
```angelscript
Serializator@ Set(const Critter& cr)
```

#### opShl
```angelscript
Serializator@ opShl(const Critter& cr)
```

#### Set
```angelscript
Serializator@ Set(const Item& item)
```

#### opShl
```angelscript
Serializator@ opShl(const Item& item)
```

#### Get
```angelscript
Serializator@ Get(int64& value)
```

#### opShr
```angelscript
Serializator@ opShr(int64& value)
```

#### Get
```angelscript
Serializator@ Get(int32& value)
```

#### opShr
```angelscript
Serializator@ opShr(int32& value)
```

#### Get
```angelscript
Serializator@ Get(int16& value)
```

#### opShr
```angelscript
Serializator@ opShr(int16& value)
```

#### Get
```angelscript
Serializator@ Get(int8& value)
```

#### opShr
```angelscript
Serializator@ opShr(int8& value)
```

#### Get
```angelscript
Serializator@ Get(uint64& value)
```

#### opShr
```angelscript
Serializator@ opShr(uint64& value)
```

#### Get
```angelscript
Serializator@ Get(uint32& value)
```

#### opShr
```angelscript
Serializator@ opShr(uint32& value)
```

#### Get
```angelscript
Serializator@ Get(uint16& value)
```

#### opShr
```angelscript
Serializator@ opShr(uint16& value)
```

#### Get
```angelscript
Serializator@ Get(uint8& value)
```

#### opShr
```angelscript
Serializator@ opShr(uint8& value)
```

#### Get
```angelscript
Serializator@ Get(bool& value)
```

#### opShr
```angelscript
Serializator@ opShr(bool& value)
```

#### Get
```angelscript
Serializator@ Get(string& str)
```

#### opShr
```angelscript
Serializator@ opShr(string& str)
```

#### Get
```angelscript
Serializator@ Get(float& value)
```

#### opShr
```angelscript
Serializator@ opShr(float& value)
```

#### Get
```angelscript
Serializator@ Get(array<int64>& values)
```

#### opShr
```angelscript
Serializator@ opShr(array<int64>& values)
```

#### Get
```angelscript
Serializator@ Get(array<int32>& values)
```

#### opShr
```angelscript
Serializator@ opShr(array<int32>& values)
```

#### Get
```angelscript
Serializator@ Get(array<float>& values)
```

#### opShr
```angelscript
Serializator@ opShr(array<float>& values)
```

#### Get
```angelscript
Serializator@ Get(array<int16>& values)
```

#### opShr
```angelscript
Serializator@ opShr(array<int16>& values)
```

#### Get
```angelscript
Serializator@ Get(array<int8>& values)
```

#### opShr
```angelscript
Serializator@ opShr(array<int8>& values)
```

#### Get
```angelscript
Serializator@ Get(array<uint64>& values)
```

#### opShr
```angelscript
Serializator@ opShr(array<uint64>& values)
```

#### Get
```angelscript
Serializator@ Get(array<uint32>& values)
```

#### opShr
```angelscript
Serializator@ opShr(array<uint32>& values)
```

#### Get
```angelscript
Serializator@ Get(array<uint16>& values)
```

#### opShr
```angelscript
Serializator@ opShr(array<uint16>& values)
```

#### Get
```angelscript
Serializator@ Get(array<uint8>& values)
```

#### opShr
```angelscript
Serializator@ opShr(array<uint8>& values)
```

#### Get
```angelscript
Serializator@ Get(array<bool>& values)
```

#### opShr
```angelscript
Serializator@ opShr(array<bool>& values)
```

#### Get
```angelscript
Serializator@ Get(array<string>& values)
```

#### opShr
```angelscript
Serializator@ opShr(array<string>& values)
```

#### Get
```angelscript
Serializator@ Get(Critter@& cr)
```

#### opShr
```angelscript
Serializator@ opShr(Critter@& cr)
```

#### Get
```angelscript
Serializator@ Get(Item@& item)
```

#### opShr
```angelscript
Serializator@ opShr(Item@& item)
```


