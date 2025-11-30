---
title: tasks.fos
description: " FOnline: 2238 Rotators  tasks.fos ..."
---

# tasks.fos


FOnline: 2238
Rotators

tasks.fos


## Includes

- `_macros.fos`
- `utils_h.fos`
- `npc_common_h.fos`
- `npc_planes_h.fos`
- `entire.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __TASKS__ |  |  |
| _AddTaskTimer | `# (name, hours, minutes) { int[] data = { hours, minutes }; CreateTimeEvent(GetNearFullSecond(0, 0, 0, hours, minutes, 0), name, data, false);  }` |  |
| _AddTask | `\` |  |
| _ReturnTime | `\` |  |

## Functions

### MoveToTask

Macros are evil, so we're doing stuff here :)

```angelscript
void MoveToTask(uint id, uint mappid, uint role, uint entire, uint dir)
```

### GetCurrentTask

```angelscript
uint GetCurrentTask(Critter& npc)
```

### d_IsCurrentTask

```angelscript
bool d_IsCurrentTask(Critter& player, Critter@ npc, int val)
```

### d_IsNotCurrentTask

```angelscript
bool d_IsNotCurrentTask(Critter& player, Critter@ npc, int val)
```


