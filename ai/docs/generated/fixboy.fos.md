---
title: fixboy.fos
description: " FOnline: 2238 Rotators  fixboy.fos ..."
---

# fixboy.fos


FOnline: 2238
Rotators

fixboy.fos


## Includes

- `_macros.fos`
- `buffer_h.fos`
- `fixboy_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __FIXBOY__ |  |  |

## Classes

### CraftingRequire

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| type | `CraftingRequirement` |  |  |
| check | `CraftingCheck` |  |  |
| require | `uint16` |  |  |
| count | `uint16` |  |  |

**Methods**

#### Add
```angelscript
bool Add(CraftingRequirement type, uint16 require, CraftingCheck check, uint16 count, CraftingCheck groupCheck = CHECK_AND)
```

#### IsGroup
```angelscript
bool IsGroup()
```

#### IsGroup
```angelscript
bool IsGroup(uint& length)
```

#### IsTrue
```angelscript
bool IsTrue(Critter& cr, uint16 multipler = 1)
```

#### Pack
```angelscript
void Pack(Buffer& buff)
```

#### Unpack
```angelscript
void Unpack(Buffer& buff)
```

#### Dump
```angelscript
void Dump(array<string>& arr)
```

### CraftingItem

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| id | `uint16` |  |  |
| name | `string` |  |  |
| description | `string` |  |  |
| minimum | `uint16` |  |  |
| maximum | `uint16` |  |  |
| step | `uint16` |  |  |
| requireShow | `[CraftingRequire](fixboy.fos.md)@` |  |  |
| requireParam | `[CraftingRequire](fixboy.fos.md)@` |  |  |
| requireTool | `[CraftingRequire](fixboy.fos.md)@` |  |  |
| requireMaterial | `[CraftingRequire](fixboy.fos.md)@` |  |  |
| result | `array<uint16>` |  |  |
| experience | `uint16` |  |  |
| script | `string` |  |  |
| packed | `array<uint16>` |  |  |

**Methods**

#### get_ID
```angelscript
uint16 get_ID()
```

#### get_Name
```angelscript
string get_Name()
```

#### get_Description
```angelscript
string get_Description()
```

#### get_Minimum
```angelscript
uint16 get_Minimum()
```

#### get_Maximum
```angelscript
uint16 get_Maximum()
```

#### get_Step
```angelscript
uint16 get_Step()
```

#### set_ID
```angelscript
void set_ID(uint16 id)
```

#### set_Name
```angelscript
void set_Name(string name)
```

#### set_Description
```angelscript
void set_Description(string description)
```

#### set_Minimum
```angelscript
void set_Minimum(uint16 minimum)
```

#### set_Maximum
```angelscript
void set_Maximum(uint16 maximum)
```

#### set_Step
```angelscript
void set_Step(uint16 step)
```

#### get_Experience
```angelscript
uint16 get_Experience()
```

#### set_Experience
```angelscript
void set_Experience(uint16 experience)
```

#### get_Script
```angelscript
string get_Script()
```

#### set_Script
```angelscript
void set_Script(string script)
```

#### get_Packed
```angelscript
array<uint16> get_Packed()
```

#### CanSee
```angelscript
bool CanSee(Critter& cr)
```

#### CanCraft
```angelscript
bool CanCraft(Critter& cr, uint16 multipler = 1)
```

#### HaveParams
```angelscript
bool HaveParams(Critter& cr)
```

#### HaveTools
```angelscript
bool HaveTools(Critter& cr)
```

#### HaveMaterials
```angelscript
bool HaveMaterials(Critter& cr, uint16 multipler = 1)
```

#### AddRequireShow
```angelscript
bool AddRequireShow(CraftingRequirement type, uint require, CraftingCheck check, uint16 count)
```

#### AddRequireParam
```angelscript
bool AddRequireParam(uint require, CraftingCheck check, uint16 count)
```

#### AddRequireParamBase
```angelscript
bool AddRequireParamBase(uint require, CraftingCheck check, uint16 count)
```

#### AddRequireTool
```angelscript
bool AddRequireTool(uint require, CraftingCheck check, uint16 count)
```

#### AddRequireMaterial
```angelscript
bool AddRequireMaterial(uint require, uint16 count)
```

#### GetResult
```angelscript
uint GetResult(array<uint16>& outResult)
```

#### GetResult
```angelscript
uint GetResult(array<array<uint16> >& outResult)
```

#### GetResult
```angelscript
uint GetResult(array<ProtoItem@>& proto, array<uint16>& count)
```

#### AddResult
```angelscript
bool AddResult(uint16 protoId, uint16 count = 1)
```

#### AddResult
```angelscript
bool AddResult(array<uint16> newResult)
```

#### AddResult
```angelscript
bool AddResult(ProtoItem& proto, uint16 count = 1)
```

#### SetResult
```angelscript
bool SetResult(array<uint16> newResult)
```

#### SetResult
```angelscript
bool SetResult(array<array<uint16> > newResult)
```

#### Pack
```angelscript
void Pack()
```

#### Unpack
```angelscript
void Unpack(array<uint16>& data)
```

#### Dump
```angelscript
string Dump()
```


## Functions

### NewCraftingItem

```angelscript
ICraftingItem@ NewCraftingItem()
```


