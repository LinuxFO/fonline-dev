---
title: pdata_h.fos
---

# pdata_h.fos

## Included By

- [main.fos](main.fos.md)
- [map_tent.fos](map_tent.fos.md)

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __PDATA_H__ |  |  |
| IMPORT_PERSONAL_DATA_RAW |  |  |
| IMPORT_PERSONAL_DATA_LIST |  |  |
| IMPORT_PERSONAL_DATA |  |  |

## Functions

### GetPersonalData

```angelscript
import bool GetPersonalData(_gameType obj, string& name, array<uint8>& value) from "pdata";					\
```

### GetPersonalData

```angelscript
import uint GetPersonalData(_gameType obj, array<string>& names, array<array<uint8>>& values) from "pdata";	\
```

### IsPersonalData

```angelscript
import bool IsPersonalData(_gameType obj, string& name) from "pdata";											\
```

### SetPersonalData

```angelscript
import bool SetPersonalData(_gameType obj, string& name, array<uint8>& value) from "pdata";					\
```

### UnsetPersonalData

```angelscript
import bool UnsetPersonalData(_gameType obj, string& name) from "pdata";										\
```

### AddToPersonalDataList

```angelscript
import void AddToPersonalDataList( _gameType obj, string& pdata, uint value ) from "pdata";		\
```

### GetPersonalDataList

```angelscript
import uint GetPersonalDataList( _gameType obj, string& pdata, array<uint>& list ) from "pdata";	\
```

### GetPersonalDataListSize

```angelscript
import uint GetPersonalDataListSize( _gameType obj, string& pdata ) from "pdata";					\
```

### IsInPersonalDataList

```angelscript
import bool IsInPersonalDataList( _gameType obj, string& pdata, uint value ) from "pdata";			\
```

### RemoveFromPersonalDataList

```angelscript
import void RemoveFromPersonalDataList( _gameType obj, string& pdata, uint value ) from "pdata";	\
```


