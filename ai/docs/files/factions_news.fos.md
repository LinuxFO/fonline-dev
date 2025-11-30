---
title: factions_news.fos
description: " FOnline: 2238 Rotators  factions_news.fos ..."
---

# factions_news.fos


FOnline: 2238
Rotators

factions_news.fos


## Includes

- `_macros.fos`
- `factions_h.fos`
- `serializator.fos`

## Included By

- [faction_data.fos](faction_data.fos.md)

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __FACTIONS_NEWS__ |  |  |

## Classes

### FactionNews

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| news | `array<uint>` |  | array layout: {master, slave, type, time, ...} |
| serialiser | `[Serializator](serializator.fos.md)` |  |  |
| factionName | `string` |  | name of the faction the news belong |

**Methods**

#### GetCount
 Number of news 

```angelscript
uint GetCount()
```

#### AddNews
 Add news at the end of the array 

```angelscript
void AddNews(uint master, uint slave, uint type)
```

#### UpdateData
 Updates AnyData 

```angelscript
bool UpdateData()
```


