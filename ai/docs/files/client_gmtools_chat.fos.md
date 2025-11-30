---
title: client_gmtools_chat.fos
description: " FOnline: 2238 Rotators  client_gmtools_chat.fos ..."
---

# client_gmtools_chat.fos


FOnline: 2238
Rotators

client_gmtools_chat.fos


## Includes

- `client_interface_h.fos`

## Classes

### CGMTChat

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| tick | `uint` |  |  |
| access | `uint` |  |  |
| text | `string` |  |  |
| color | `uint` |  |  |

**Methods**

#### onCreate
```angelscript
void onCreate()
```


## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| GMTchat | `array<[CGMTChat](client_gmtools_chat.fos.md)>` |  |  |

## Functions

### GMToolsChat

* * send chat message to server * * @see question 

```angelscript
void GMToolsChat(string message)
```

### GMToolsProcessChat

* * Remove old chat messages, check * * @note called by @a @e loop() -> @a @e GMToolsProcess() 

```angelscript
void GMToolsProcessChat()
```

### GMToolsDrawChat

* * Display chat messages to client. * * @note called by: @a @e render_iface() -> @a @e GMToolsDraw() 

```angelscript
void GMToolsDrawChat()
```


