---
title: buffer_lazy.fos
description: " FOnline: 2238 Rotators  buffer_lazy.fos ..."
---

# buffer_lazy.fos


FOnline: 2238
Rotators

buffer_lazy.fos


## Includes

- `_defines.fos`
- `_macros.fos`
- `buffer_h.fos`
- `buffer_lazy_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __BUFFER_LAZY__ |  |  |
| BL_HANDSHAKE_QUESTION | `(0)` | handshake |
| BL_HANDSHAKE_OK | `(1)` |  |
| BL_HANDSHAKE_UNKNOWN | `(253)` |  |
| BL_HANDSHAKE_INVALID | `(254)` |  |
| BL_HANDSHAKE_DENIED | `(255)` |  |

## Classes

### CBufferLazy

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| id_source | `uint` |  |  |
| id_target | `uint` |  |  |
| funcName | `string` |  |  |
| p0 | `int` |  |  |
| p1 | `int` |  |  |
| p2 | `int` |  |  |
| p3 | `string@` |  |  |
| p4 | `array<int>` |  |  |


## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| data | `array<int32>` |  |  |
| buff | `Buffer@` | `NewBuffer()` |  |
| data | `array<int32>` |  |  |
| buff | `Buffer@` | `NewBuffer()` |  |
| buff | `Buffer@` | `NewBuffer(p4)` |  |
| handshake | `uint8` | `0` |  |
| id_source | `uint32` | `0` |  |
| funcName | `string` | `""` |  |
| unsafe | `bool` | `true` |  |
| id_target | `uint32` | `LazyBuffers.last().id_source` |  |
| id_target | `uint32` | `0` | target allows to send data, start the Run*Script chain |
| data | `array<int>` |  |  |
| dataEnd | `bool` | `false` |  |
| bufflazy | `[CBufferLazy](buffer_lazy.fos.md)@` | `GetBufferLazy(id_source)` |  |
| size | `uint` | `16 + bufflazy.funcName.length()` |  |
| positionMax | `int` | `bufflazy.p4.length()` |  |
| lazy | `[CBufferLazy](buffer_lazy.fos.md)@` | `GetBufferLazy(id_target)` |  |

## Functions

### CreateBufferLazyId

Create internal id, used during sending/receiving data

```angelscript
uint CreateBufferLazyId()
```

### GetBufferLazy

Retrieve BufferLazy with given id

```angelscript
CBufferLazy@ GetBufferLazy(uint id)
```

### RemoveBufferLazy

Remove BufferLazy with given id

```angelscript
bool RemoveBufferLazy(uint id)
```

### RunLazyScript

```angelscript
void RunLazyScript(string& funcName, int p0, int p1, int p2, string@ p3, array<int>@ p4)
```

### RunLazyScriptUnsafe

```angelscript
void RunLazyScriptUnsafe(string& funcName, int p0, int p1, int p2, string@ p3, array<int>@ p4)
```

### RunLazyScriptGeneric

```angelscript
void RunLazyScriptGeneric(string& funcName, int p0, int p1, int p2, string@ p3, array<int>@ p4, bool unsafe)
```

### RunLazyScript

```angelscript
void RunLazyScript(Critter& player, string& funcName, int p0, int p1, int p2, string@ p3, array<int>@ p4)
```

### handshake_result

```angelscript
void handshake_result(uint8 result, int id_source, int id_target = -1)
```

### handshake_result

```angelscript
void handshake_result(Critter& player, uint8 result, int id_source, int id_target = -1)
```

### handshake

```angelscript
void handshake(int p0, int p1, int p2, string@ p3, array<int>@ p4)
```

### unsafe_handshake

```angelscript
void unsafe_handshake(Critter& player, int p0, int p1, int p2, string@ p3, array<int>@ p4)
```

### request

```angelscript
void request(int id_source, int id_target, int position, string@, array<int>@)
```

### unsafe_request

```angelscript
void unsafe_request(Critter& player, int id_source, int id_target, int position, string@, array<int>@)
```

### receive

```angelscript
void receive(int id_source, int id_target, int position, string@ dataEnd, array<int>@ data)
```

### unsafe_receive

```angelscript
void unsafe_receive(Critter& player, int id_source, int id_target, int position, string@ dataEnd, array<int>@ data)
```


