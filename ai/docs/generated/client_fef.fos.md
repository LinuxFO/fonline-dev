---
title: client_fef.fos
---

# client_fef.fos

## Includes

- `_defines.fos`
- `_client_defines.fos`
- `_macros.fos`
- `_colors.fos`
- `lexems_h.fos`
- `MsgStr.h`
- `_basetypes.fos`
- `sprite.fos`
- `buffer_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __FEF__ |  |  |
| ZONE_IDX | `# (zx, zy)((zy) * __GlobalMapWidth + (zx))` |  |
| CARAVAN_ENC_MIN | `135` |  |
| CARAVAN_ENC_MAX | `144` |  |

## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| GmapEncStr | `string` |  |  |
| isInitialized | `bool` | `false` |  |
| groups | `array<array<uint8>>` |  |  |
| mzxOld | `uint` | `uint(-1), mzyOld = uint(-1)` |  |
| encounters | `array<array<string>>` |  |  |

## Functions

### InitDrawEncounters

```angelscript
void InitDrawEncounters()
```

### EncountersProcess

```angelscript
void EncountersProcess()
```

### EncountersDraw

```angelscript
void EncountersDraw()
```


