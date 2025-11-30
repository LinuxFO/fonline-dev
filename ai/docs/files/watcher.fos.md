---
title: watcher.fos
description: " FOnline: 2238 Rotators  watcher.fos ..."
---

# watcher.fos


FOnline: 2238
Rotators

watcher.fos


## Includes

- `_macros.fos`
- `utils_h.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| WATCHER_IDENT | `(5414)` |  |
| WATCHER_SINGLE | `(0)` |  |
| WATCHER_MAP | `(1)` |  |
| WATCHER_EVENT | `(2)` |  |
| VAR_MASTER | `(ST_VAR0)` |  |
| VAR_VICTIM | `(ST_VAR1)` |  |
| VAR_MODE | `(ST_VAR8)` |  |
| VAR_IDENT | `(ST_VAR9)` |  |
| ServerScriptFunc | `# (name, pX, p0, p1, p2, p3, p4) void name(Critter & pX, int p0, int p1, int p2, string@ p3, int[] @ p4) { name(pX, p0, p1, p2); } void name(Critter & pX, int p0, int p1, int p2)` | gmtools: compatibility with runscript / runscript_unsafe |

## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| allmaps | `uint` | `GetAllMaps(0, maps)` |  |
| found | `bool` | `false` |  |
| info | `string` |  |  |

## Functions

### __watcher

```angelscript
void __watcher(Critter& player, int p0, int p1)
```

### watcher_init

```angelscript
void watcher_init(Critter& npc, bool firstTime)
```

### watcher_report

```angelscript
void watcher_report(Critter& npc, string what)
```

### watcher_ontext

```angelscript
string watcher_ontext(Critter@ onCritter, Item@ onItem, Scenery@ onScenery)
```

### watcher_finish

```angelscript
void watcher_finish(Critter& npc, bool deleted)
```

### watcher_attack

```angelscript
bool watcher_attack(Critter& npc, Critter& victim)
```

### watcher_someone_attack

```angelscript
void watcher_someone_attack(Critter& npc, Critter& sadist, Critter& victim)
```

### watcher_someone_dead

```angelscript
void watcher_someone_dead(Critter& npc, Critter& victim, Critter@ sadist)
```

### watcher_someone_dropitem

```angelscript
void watcher_someone_dropitem(Critter& npc, Critter& fromCr, Item& item)
```

### watcher_someone_useitem

```angelscript
void watcher_someone_useitem(Critter& npc, Critter& fromCr, Item& item, Critter@ onCritter, Item@ onItem, Scenery@ onScenery)
```

### watcher_someone_useskill

```angelscript
void watcher_someone_useskill(Critter& npc, Critter& fromCr, int skill, Critter@ onCritter, Item@ onItem, Scenery@ onScenery)
```


