del /S scripts\*.fosp
del /S scripts\*.fosb
del maps\*.fomapb

rd /S /Q ..\Client\data\cache

del save\*.fo
del save\bans\active.txt
del save\clients\*.client
del save\clients\last_id.txt

del cache_fail
