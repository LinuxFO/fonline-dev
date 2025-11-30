---
title: gmtools_csc.fos
description: " FOnline: 2238 Rotators  gmtools_csc.fos ..."
---

# gmtools_csc.fos


FOnline: 2238
Rotators

gmtools_csc.fos


## Classes

### CGMTQuestion

* * x 

**Properties**

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| tick | `int` |  |  |
| timer | `int` |  |  |
| old | `bool` |  |  |
| type | `uint` |  |  |
| flags | `uint` |  |  |
| status | `int` |  |  |
| question_text | `string` |  |  |
| answer_text | `string` |  |  |
| answer_data | `array<int>` |  |  |


## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| GMTquestion | `array<[CGMTQuestion](gmtools_csc.fos.md)>` |  |  |

## Functions

### question

```angelscript
void question(int timer, uint type)
```

### question

```angelscript
void question(uint timer, uint type, uint flags, string& text)
```

### answer

```angelscript
void answer(int tick, int status, int flags, string@ answer_text, array<int>@ data)
```

### get_answer

```angelscript
int get_answer(uint type)
```

### FindAnswerData

when you don't know question/answer id

```angelscript
int FindAnswerData(int type, string& identifier)
```

### GetAnswerData

when you know question/answer id

```angelscript
int GetAnswerData(int questionID, string& identifier)
```

### GMtools_CheckAccess

```angelscript
bool GMtools_CheckAccess(Critter& player, uint8 access, uint tick, bool send_answer)
```

### GMtools_SendAnswer

```angelscript
void GMtools_SendAnswer(Critter& player, int tick, int status, int flags, string& answer, array<int>@ data)
```


