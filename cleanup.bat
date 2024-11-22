@echo off
dism.exe /online /cleanup-image /restorehealth
sfc /scannow
del C:\Windows\temp\*.*/s/q
del C:\Windows\prefetch\*.*/s/q
Cleanmgr /sagerun
Cleanmgr /verylowdisk/dc
net stop bits
net stop wuauserv
del C:\Windows\SoftwareDistribution\*.*/s/q
net start bits
net start wuauserv
del /f /s /q %systemroot%\memory.dmp
del /f /s /q %systemroot%\Minidump\*.*
defrag c:
Rem ipconfig/flushdns if needed
Rem wsrest.exe as well for windows store chache 
