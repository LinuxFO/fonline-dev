---
title: npc_planes.fos
description: " FOnline: 2238 Rotators  npc_planes.fos ..."
---

# npc_planes.fos


FOnline: 2238
Rotators

npc_planes.fos


## Includes

- `_macros.fos`

## Functions

### AddMiscPlane

```angelscript
bool AddMiscPlane(Critter& npc, uint priority, uint waitSecond, string@ funcName)
```

### AddMiscPlane

```angelscript
bool AddMiscPlane(Critter& npc, uint priority, int identifier, uint identifierExt, uint waitSecond, string@ funcName)
```

### AddWalkPlane

```angelscript
bool AddWalkPlane(Critter& npc, uint priority, uint16 hexX, uint16 hexY, uint8 dir, bool run, uint cut)
```

### AddWalkPlane

```angelscript
bool AddWalkPlane(Critter& npc, uint priority, int identifier, uint identifierExt, uint16 hexX, uint16 hexY, uint8 dir, bool run, uint cut)
```

### AddAttackPlane

```angelscript
bool AddAttackPlane(Critter& npc, uint priority, Critter& target)
```

### AddAttackPlane

```angelscript
bool AddAttackPlane(Critter& npc, uint priority, uint critId)
```

### AddAttackPlane

```angelscript
bool AddAttackPlane(Critter& npc, uint priority, Critter& target, int minHp)
```

### AddAttackPlane

```angelscript
bool AddAttackPlane(Critter& npc, uint priority, uint critId, int minHp)
```

### AddAttackPlane

```angelscript
bool AddAttackPlane(Critter& npc, uint priority, Critter& target, bool run)
```

### AddAttackPlane

```angelscript
bool AddAttackPlane(Critter& npc, uint priority, uint critId, bool run)
```

### AddAttackPlane

```angelscript
bool AddAttackPlane(Critter& npc, uint priority, Critter& target, int minHp, bool run)
```

### AddAttackPlane

```angelscript
bool AddAttackPlane(Critter& npc, uint priority, uint critId, int minHp, bool run)
```

### AddPickPlane

```angelscript
bool AddPickPlane(Critter& npc, uint priority, uint16 hexX, uint16 hexY, uint16 protoId, uint useItemId, bool toOpen)
```

### AddPickPlane

```angelscript
bool AddPickPlane(Critter& npc, uint priority, Item@ item, uint useItemId, bool toOpen)
```

### AddPickPlane

```angelscript
bool AddPickPlane(Critter& npc, uint priority, Item@ item, uint useItemId, bool toOpen, bool run)
```

### EraseAttackPlane

```angelscript
uint EraseAttackPlane(Critter& npc, uint priority, Critter& target)
```

### EraseAttackPlane

```angelscript
uint EraseAttackPlane(Critter& npc, uint priority, uint critId)
```

### AddHealCritterPlane

```angelscript
bool AddHealCritterPlane(Critter& npc, uint priority, Critter@ target, bool run)
```

### AddDoctorCritterPlane

```angelscript
bool AddDoctorCritterPlane(Critter& npc, uint priority, Critter@ target, bool run)
```


