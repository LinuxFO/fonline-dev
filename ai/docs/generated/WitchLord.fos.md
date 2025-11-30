---
title: WitchLord.fos
description: "AngelScript bugs checker  (compiles, current revision)        // pass (doesn't compile, current revision) // r[revision] -- [error] (compiles, future ..."
---

# WitchLord.fos

AngelScript bugs checker

(compiles, current revision)        // pass
(doesn't compile, current revision) // r[revision] -- [error]
(compiles, future revision)         // r[revision] -- pass
(description)                       // [what it means for us]
void name(...) {...}

## Classes

### nsClass

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| mommy | `nsIface@` |  |  |

**Methods**

#### get_parent
```angelscript
nsIface@ get_parent()
```

### cfuncdef1_1

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| _events_ | `ifuncdef1_2@` |  |  |

**Methods**

#### get_events
```angelscript
ifuncdef1_2@ get_events()                    { return(this._events_); }
```

#### set_events
```angelscript
void         set_events(ifuncdef1_2@ events) { @this._events_ = events; }
```

#### crashme
```angelscript
void crashme()
```

### cfuncdef1_2

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| ff | `funcdef1@` |  |  |

**Methods**

#### get_f
```angelscript
funcdef1@ get_f()             { return(@this.ff); }
```

#### set_f
```angelscript
void      set_f(funcdef1@ _f) { @this.ff = _f; }
```


## Functions

### defaultArg1

pass

```angelscript
void defaultArg1(int x = 1) {}
```

### defaultArg2_1

pass

```angelscript
void defaultArg2_1(int x = (1))                                     {}
```

### defaultArg2_2

```angelscript
void defaultArg2_2(int x = (1))                                     {}
```

### defaultArg2_3

```angelscript
void defaultArg2_3(int x = (2 + 2))                                 {}
```

### defaultArg2_4

```angelscript
void defaultArg2_4(int x = (2 * 2 / 2 + 2 - 2) % 2 == 2 ? 22 : 222) {}
```

### nsMommy

```angelscript
nsIface@ nsMommy()
```

### start

```angelscript
void start()
```

### end

```angelscript
void end(ifuncdef1_1& i)
```


