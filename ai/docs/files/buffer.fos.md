---
title: buffer.fos
description: " * WHINE TEAM * We Had Ini, Now Engine * * RunClientScript/RunServerScript data \"packer\" * Partially based on Serializator (TLA scripts) and BufferM..."
---

# buffer.fos


* WHINE TEAM
* We Had Ini, Now Engine
*
* RunClientScript/RunServerScript data "packer"
* Partially based on Serializator (TLA scripts) and BufferManager (FOnline engine)
*
* server and client module


## Includes

- `_macros.fos`
- `buffer_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __BUFFER__ |  |  |
| STRING_GET |  |  |
| STRING_SET |  |  |
| STRING_LENGTH |  |  |
| STRING_RESIZE |  |  |
| STRING_GET |  |  |
| STRING_SET |  |  |
| STRING_LENGTH |  |  |
| STRING_RESIZE |  |  |
| IS_RAW |  | Check if buffer contains [len] elements, without changing reading position |
| _constructor |  |  |
| _opBase |  |  |
| _opArray |  |  |
| _opDump |  |  |
| _newBuffer |  |  |

## Classes

### CBuffer

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| buf | `array<uint8>` |  |  |
| readPos | `uint` |  |  |

**Methods**

#### Get
```angelscript
Buffer@ Get( type& value )	\
```

#### Set
```angelscript
Buffer@ Set( type& value )	\
```

#### opShr
```angelscript
Buffer@ opShr( array<type>& value )		\
```

#### opShl
```angelscript
Buffer@ opShl( array<type>& value )		\
```

#### Get
```angelscript
Buffer@ Get( array<type>& value )		\
```

#### Set
```angelscript
Buffer@ Set( array<type>& value )		\
```

#### opUShr
```angelscript
Buffer@ opUShr( array<type>& value )		\
```

#### opUShrAssign
```angelscript
Buffer@ opUShrAssign( array<type>& arr )	\
```

#### name
```angelscript
array<type> name()							\
```

#### opCom
Clear buffer, reset reading position ~Buffer;

```angelscript
Buffer@ opCom()
```

#### opNeg
Reset reading position -Buffer;

```angelscript
Buffer@ opNeg()
```

#### opShr
```angelscript
Buffer@ opShr( int8& value )
```

#### opShl
```angelscript
Buffer@ opShl( int8 value )
```

#### opShr
```angelscript
Buffer@ opShr( int16& value )
```

#### opShl
```angelscript
Buffer@ opShl( int16 value )
```

#### opShr
```angelscript
Buffer@ opShr( int32& value )
```

#### opShl
```angelscript
Buffer@ opShl( int32 value )
```

#### opShr
```angelscript
Buffer@ opShr( int64& value )
```

#### opShl
```angelscript
Buffer@ opShl( int64 value )
```

#### opShr
```angelscript
Buffer@ opShr( uint8& value )
```

#### opShl
```angelscript
Buffer@ opShl( uint8 value )
```

#### opShr
```angelscript
Buffer@ opShr( uint16& value )
```

#### opShl
```angelscript
Buffer@ opShl( uint16 value )
```

#### opShr
```angelscript
Buffer@ opShr( uint32& value )
```

#### opShl
```angelscript
Buffer@ opShl( uint32 value )
```

#### opShr
```angelscript
Buffer@ opShr( uint64& value )
```

#### opShl
```angelscript
Buffer@ opShl( uint64 value )
```

#### opShr
```angelscript
Buffer@ opShr( bool& value )
```

#### opShl
```angelscript
Buffer@ opShl( bool value )
```

#### opShr
```angelscript
Buffer@ opShr( string& value )
```

#### opShl
```angelscript
Buffer@ opShl( string value )
```

#### opShr
```angelscript
Buffer@ opShr( float& value )
```

#### opShl
```angelscript
Buffer@ opShl( float value )
```


## Functions

### NewBuffer

Create new Buffer object

```angelscript
Buffer@ NewBuffer()
```

### NewBuffer

```angelscript
Buffer@ NewBuffer( array<type>@ data )	\
```


