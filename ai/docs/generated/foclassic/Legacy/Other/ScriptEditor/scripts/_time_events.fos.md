---
title: _time_events.fos
---

# _time_events.fos

## Included By

- [_all_defines.fos](_all_defines.fos.md)
- [den_barbekky_boy.fos](den_barbekky_boy.fos.md)

## Defines

| Name | Value | Description |
| :--- | :--- | :--- |
| __TIME_EVENTS__ |  |  |
| TE_EveryHour | `#(cr,num,minute,module,func) cr.CreateTimeEvent(num,0,0,0,minute,0,module,func)` |  |
| TE_EveryDay | `#(cr,num,hour,minute,module,func) cr.CreateTimeEvent(num,0,0,hour+1,minute,0,module,func)` |  |
| TE_EveryMonth | `#(cr,num,day,hour,minute,module,func) cr.CreateTimeEvent(num,0,day,hour+1,minute,0,module,func)` |  |
| TE_EveryYear | `#(cr,num,month,day,hour,minute,module,func) cr.CreateTimeEvent(num,month,day,hour+1,minute,0,module,func)` |  |
| TE_ChangeModule | `#(cr,num,module) cr.ChangeTimeEventA(num,module,"")` |  |
| TE_ChangeFunc | `#(cr,num,func) cr.ChangeTimeEventA(num,"",func)` |  |
| TE_ChangeMinute | `#(cr,num,minute) cr.ChangeTimeEventB(num,0,0,0,minute)` |  |
| TE_ChangeHour | `#(cr,num,hour) cr.ChangeTimeEventB(num,0,0,hour+1,-1)` |  |
| TE_ChangeDay | `#(cr,num,day) cr.ChangeTimeEventB(num,0,day,0,-1)` |  |
| TE_ChangeMonth | `#(cr,num,month) cr.ChangeTimeEventB(num,month,0,0,-1)` |  |
| TE_ChangeLoop | `#(cr,num,loop) cr.ChangeTimeEventC(num,loop)` |  |
| TE_Erase | `#(cr,num) cr.EraseTimeEvent(num)` |  |
| TE_EveryHour_LogErr | `#(cr,num,minute,module,func) do{int err=cr.CreateTimeEvent(num,0,0,0,minute,0,module,func); if(err<0) TE_LogError(err);}while(false)` |  |
| TE_EveryDay_LogErr | `#(cr,num,hour,minute,module,func) do{int err=cr.CreateTimeEvent(num,0,0,hour+1,minute,0,module,func); if(err<0) TE_LogError(err);}while(false)` |  |
| TE_EveryMonth_LogErr | `#(cr,num,day,hour,minute,module,func) do{int err=cr.CreateTimeEvent(num,0,day,hour+1,minute,0,module,func); if(err<0) TE_LogError(err);}while(false)` |  |
| TE_EveryYear_LogErr | `#(cr,num,month,day,hour,minute,module,func) do{int err=cr.CreateTimeEvent(num,month,day,hour+1,minute,0,module,func); if(err<0) TE_LogError(err);}while(false)` |  |
| TE_ChangeModule_LogErr | `#(cr,num,module) do{int err=cr.ChangeTimeEventA(num,module,""); if(err<0) TE_LogError(err);}while(false)` |  |
| TE_ChangeFunc_LogErr | `#(cr,num,func) do{int err=cr.ChangeTimeEventA(num,"",func); if(err<0) TE_LogError(err);}while(false)` |  |
| TE_ChangeMinute_LogErr | `#(cr,num,minute) do{int err=cr.ChangeTimeEventB(num,0,0,0,minute); if(err<0) TE_LogError(err);}while(false)` |  |
| TE_ChangeHour_LogErr | `#(cr,num,hour) do{int err=cr.ChangeTimeEventB(num,0,0,hour+1,-1); if(err<0) TE_LogError(err);}while(false)` |  |
| TE_ChangeDay_LogErr | `#(cr,num,day) do{int err=cr.ChangeTimeEventB(num,0,day,0,-1); if(err<0) TE_LogError(err);}while(false)` |  |
| TE_ChangeMonth_LogErr | `#(cr,num,month) do{int err=cr.ChangeTimeEventB(num,month,0,0,-1); if(err<0) TE_LogError(err);}while(false)` |  |
| TE_ChangeLoop_LogErr | `#(cr,num,loop) do{int err=cr.ChangeTimeEventC(num,loop); if(err<0) TE_LogError(err);}while(false)` |  |
| TE_Erase_LogErr | `#(cr,num) do{int err=cr.EraseTimeEvent(num); if(err<0) TE_LogError(err);}while(false)` |  |

## Functions

### TE_LogError

```angelscript
void TE_LogError(int err)
```


