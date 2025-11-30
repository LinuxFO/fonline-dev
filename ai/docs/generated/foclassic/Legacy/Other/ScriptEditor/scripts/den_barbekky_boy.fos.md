---
title: den_barbekky_boy.fos
---

# den_barbekky_boy.fos

## Includes

- `.\scripts\_defines.fos`
- `.\scripts\_time_events.fos`

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| EVENT_WHOM_RADIO | `0` | ���� ����� ��������, ����� �� ���������� ������ |
| EVENT_GOOD_MORNING | `1` |  |

## Variables

| Name | Type | Value | Description |
| :--- | :--- | :--- | :--- |
| pos | `int` | `Random(0,4)` |  |
| key_id | `DWORD` | `Random(10000,50000)` |  |
| car | `Object@` | `master.AddItemHex(x[pos],y[pos],PID_HUMMER1,1)` |  |
| key | `Object@` | `master.AddItem(PID_KEY,1)` |  |

## Functions

### init

������������� ���, ���������� ��� ����� ��� � ����

```angelscript
void init(Critter& npc, int first_time)
```

### on_steal

���������������� �������, �����������, ����� � ��� ������

```angelscript
void on_steal(Critter& npc, Critter& thief, int steal)
```

### Announcement

������� 1

```angelscript
void Announcement(Critter& npc)
```

### Announcement2

������� 2

```angelscript
void Announcement2(Critter& npc)
```

### CreateHummer

�������� �������. ���� ������� ������. ���������� �� �������, � ����������. ��� ������ �������� ������� ���������� ����� ��������� �� �9 (GameForceDialog). master - ����� slave - ��� ��������� ����� �������.

```angelscript
void CreateHummer(Critter& master, Critter& slave, int val)
```


