---
title: client_critter_onhead.fos
---

# client_critter_onhead.fos

## Includes

- `_defines.fos`
- `_client_defines.fos`
- `_macros.fos`
- `_colors.fos`
- `lexems_h.fos`
- `MsgStr.h`
- `_basetypes.fos`
- `sprite.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| IsGM | `IsGMTEnabled() && GMToolsAccess` |  |

## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| crits | `array<uint>` |  |  |
| factionIcons | `array<[Sprite](sprite.fos.md)>` |  |  |
| factionCount | `uint` | `0` |  |
| mapPid | `uint` | `0` |  |

## Functions

### InitCritterOnHead

```angelscript
void InitCritterOnHead()
```

### InitFactionIcons

```angelscript
void InitFactionIcons()
```

### _SetFactionCount

```angelscript
void _SetFactionCount(int fc, int, int, string@, array<int>@ list)
```

### AddCritter

```angelscript
void AddCritter(uint id, uint pid)
```

### RemoveCritter

```angelscript
void RemoveCritter(uint id)
```

### ClearCritter

```angelscript
void ClearCritter()
```

### DrawCritterOnHead

```angelscript
void DrawCritterOnHead()
```

### ChangeOnHeadAwarenessPlayer

```angelscript
void ChangeOnHeadAwarenessPlayer()
```

### ChangeOnHeadAwarenessNPC

```angelscript
void ChangeOnHeadAwarenessNPC()
```


