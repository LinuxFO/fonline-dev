---
title: client_recording.fos
description: " FOnline: 2238 Rotators  client_recording.fos ..."
---

# client_recording.fos


FOnline: 2238
Rotators

client_recording.fos


## Includes

- `_macros.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __CLIENT |  | Text messages recording Compile with -client switch |

## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| FileName | `string` | `""` |  |
| Active | `bool` | `false` |  |
| Curr | `int` | `-1` |  |

## Functions

### StartRecording

```angelscript
void StartRecording(const string& filename)
```

### IsRecording

```angelscript
bool IsRecording() { return Active; }
```

### Record

```angelscript
void Record(const string& message)
```

### StopRecording

```angelscript
void StopRecording()
```

### GetRecord

```angelscript
string@ GetRecord(const string& filename)
```

### StartReplay

```angelscript
void StartReplay(string@ record)
```

### Replay

```angelscript
void Replay()
```

### IsReplaying

```angelscript
bool IsReplaying()
```


