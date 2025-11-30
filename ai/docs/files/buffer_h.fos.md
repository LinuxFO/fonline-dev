---
title: buffer_h.fos
description: " * WHINE TEAM * We Had Ini, Now Engine * * RunClientScript/RunServerScript data \"packer\" * Partially based on Serializator (TLA scripts) and BufferM..."
---

# buffer_h.fos


* WHINE TEAM
* We Had Ini, Now Engine
*
* RunClientScript/RunServerScript data "packer"
* Partially based on Serializator (TLA scripts) and BufferManager (FOnline engine)
*
* server and client module


## Included By

- [buffer.fos](buffer.fos.md)
- [buffer_lazy.fos](buffer_lazy.fos.md)
- [cheats.fos](cheats.fos.md)
- [client_fef.fos](client_fef.fos.md)
- [client_interface.fos](client_interface.fos.md)
- [client_messages.fos](client_messages.fos.md)
- [fixboy.fos](fixboy.fos.md)
- [map_tent.fos](map_tent.fos.md)
- [pdata.fos](pdata.fos.md)
- [server_fixboy.fos](server_fixboy.fos.md)
- [utils.fos](utils.fos.md)

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __BUFFER_H__ |  |  |
| BUFFER_MODULE | `"buffer"` |  |
| BUFFER_LENTYPE | `uint16` | How length of string/arrays will be stored in buffer |
| BUFFER_UNICODE |  | Backward compatibility Undefine if using SDK older than revision 400 |
| _opBase |  |  |
| _opArray |  |  |
| _opDump |  |  |
| _newBuffer |  |  |

## Functions

### opShr

```angelscript
Buffer@ opShr( type& value );	\
```

### opShl

```angelscript
Buffer@ opShl( type  value );	\
```

### Get

```angelscript
Buffer@ Get( type& value );		\
```

### opShr

```angelscript
Buffer@ opShr( array<type>& value );	\
```

### opShl

```angelscript
Buffer@ opShl( array<type>& value );	\
```

### Get

```angelscript
Buffer@ Get( array<type>& value );		\
```

### opUShr

```angelscript
Buffer@ opUShr( array<type>& arr );			\
```

### opUShrAssign

```angelscript
Buffer@ opUShrAssign( array<type>& arr );	\
```


