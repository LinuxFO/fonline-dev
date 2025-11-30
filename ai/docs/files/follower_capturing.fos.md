---
title: follower_capturing.fos
description: " FOnline: 2238 Rotators  follower_capturing.fos ..."
---

# follower_capturing.fos


FOnline: 2238
Rotators

follower_capturing.fos


## Includes

- `_macros.fos`
- `follower_h.fos`
- `utils_h.fos`
- `_basetypes.fos`
- `npc_common_h.fos`
- `follower_common_h.fos`

## Included By

- [main.fos](main.fos.md)

## Functions

### CaptureRoll

```angelscript
bool CaptureRoll(Critter& capturer)
```

### CaptureBrahmin

```angelscript
bool CaptureBrahmin(Critter& capturer, Critter& target, bool& out sub)
```

### CaptureSlave

true - remove rope, false - not

```angelscript
bool CaptureSlave(Critter& capturer, Critter& target, bool& out sub)
```


