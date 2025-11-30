---
title: blueprints.fos
description: " FOnline: 2238 Rotators  blueprints.fos ..."
---

# blueprints.fos


FOnline: 2238
Rotators

blueprints.fos


## Includes

- `_macros.fos`
- `debug_h.fos`

## Functions

### ConsumedBlueprintForPid

```angelscript
bool ConsumedBlueprintForPid(Critter& player, uint pid)
```

### ConsumedBlueprint

```angelscript
bool ConsumedBlueprint(Critter& player, uint pid)
```

### ConsumeBlueprint

```angelscript
void ConsumeBlueprint(Critter& player, Item& item)
```

### AddBlueprint

```angelscript
void AddBlueprint(uint16 type, uint level, int pid)
```

### InitBlueprints

Scan protos for blueprints

```angelscript
void InitBlueprints()
```

### GetRandomBlueprintPid

```angelscript
uint16 GetRandomBlueprintPid(uint8 level)
```

### GetRandomTypeBlueprintPid

```angelscript
uint16 GetRandomTypeBlueprintPid(int8 type, uint8 level)
```


