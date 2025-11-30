---
title: pdata.fos
---

# pdata.fos

## Includes

- `_defines.fos`
- `_macros.fos`
- `_time.fos`
- `debug_h.fos`
- `utils_h.fos`
- `buffer_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __PDATA__ |  |  |
| WLog |  |  |
| PrintCallstack | `NOP` |  |
| NPC_BASE_ID | `(5000000)` |  |
| PDATA_CLEANUP_TIME | `REAL_MINUTE(10)` |  |
| PDATA_CLEANUP_TIME | `REAL_MINUTE(1)` |  |
| CHECK_ID | `if(id == 0) return(false);` |  |
| PERSONAL_DATA_RAW |  |  |
| PERSONAL_DATA_LIST |  |  |
| PERSONAL_DATA |  |  |

## Functions

### NOP

```angelscript
void NOP() {}
```

### PDataString

```angelscript
string PDataString(PDataType type)
```

### IsPData

 *PData() - *AnyData() wrappers none of them should be exported, ever 

```angelscript
bool IsPData(PDataType type, uint id)
```

### GetPData

```angelscript
bool GetPData(PDataType type, uint id, array<uint8>& raw)
```

### SetPData

```angelscript
bool SetPData(PDataType type, uint id, array<uint8>& raw)
```

### UnsetPData

```angelscript
bool UnsetPData(PDataType type, uint id)
```

### StartPersonalDataCleanup

```angelscript
void StartPersonalDataCleanup()
```

### e_CleanupPData

```angelscript
uint e_CleanupPData(array<uint>@)
```

### IsPersonalData

```angelscript
bool IsPersonalData(PDataType type, uint id, string& name)
```

### GetPersonalData

```angelscript
bool GetPersonalData(PDataType type, uint id, string& name, array<uint8>& data)
```

### GetPersonalData

```angelscript
uint GetPersonalData(PDataType type, uint id, array<string>& outNames, array<array<uint8>>& outValues)
```

### SetPersonalData

```angelscript
bool SetPersonalData(PDataType type, uint id, string& name, array<uint8>& value)
```

### UnsetPersonalData

```angelscript
bool UnsetPersonalData(PDataType type, uint id, string& name)
```

### UnsetPersonalDataWithPrefix

```angelscript
uint UnsetPersonalDataWithPrefix(PDataType type, uint id, string& prefix)
```

### AddToPersonalDataList

```angelscript
void AddToPersonalDataList( PDataType type, uint id, string& name, uint value )
```

### RemoveFromPersonalDataList

```angelscript
void RemoveFromPersonalDataList( PDataType type, uint id, string& name, uint value )
```

### GetPersonalDataList

```angelscript
uint GetPersonalDataList( PDataType type, uint id, string& name, array<uint>& list )
```

### GetPersonalDataListSize

```angelscript
uint GetPersonalDataListSize( PDataType type, uint id, string& name )
```

### IsInPersonalDataList

```angelscript
bool IsInPersonalDataList( PDataType type, uint id, string& name, uint value )
```

### PersonalDataAllowed

```angelscript
bool PersonalDataAllowed(Item& item)
```

### GetPersonalData

```angelscript
bool GetPersonalData( _gameType obj, string& name, array<uint8>& value )		\
```

### GetPersonalData

```angelscript
uint GetPersonalData( _gameType obj, array<string>& names, array<array<uint8>>& values )	\
```

### IsPersonalData

```angelscript
bool IsPersonalData( _gameType obj, string& name )								\
```

### SetPersonalData

```angelscript
bool SetPersonalData( _gameType obj, string& name, array<uint8>& value )		\
```

### UnsetPersonalData

```angelscript
bool UnsetPersonalData( _gameType obj, string& name )							\
```

### UnsetPersonalDataWithPrefix

```angelscript
uint UnsetPersonalDataWithPrefix( _gameType obj, string& prefix )				\
```

### AddToPersonalDataList

```angelscript
void AddToPersonalDataList( _gameType obj, string& name, uint value )			\
```

### GetPersonalDataList

```angelscript
uint GetPersonalDataList( _gameType obj, string& name, array<uint>& list )		\
```

### GetPersonalDataListSize

```angelscript
uint GetPersonalDataListSize( _gameType obj, string& name )					\
```

### IsInPersonalDataList

```angelscript
bool IsInPersonalDataList( _gameType obj, string& name, uint value )			\
```

### RemoveFromPersonalDataList

```angelscript
void RemoveFromPersonalDataList( _gameType obj, string& name, uint value )		\
```


