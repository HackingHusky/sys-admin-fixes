custom log off script

$WaningMSG = "You have 5 minutes before you are logged off. Your data will not be saved, please print any documents or close any tabs before logging off. Thank you."
#AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup.
#needs to be saved in the this location on the machine that is bitlocked
#C:\*anywhere you place the script

#the folder must be hidden to work
$Path = 'C' + ':\$Recycle.Bin'
Get-ChildItem $Path -Force -Recourse -ErrorAction
Remove-Item -Recurse -Exclude *.ini -ErrorAction SilentlyContiue
del C:\Windows\temp\*.*/s/q
del C:\Windows\prefetch\*.*/s/q
del C:\Documents\*.*/s/q
del C:\music\*.*/s/q
del C:\videos\*.*/s/q
del C:\Downloads\*.*/s/q
net stop bits
net stop wuauserv
del C:\Windows\SoftwareDistribution\*.*/s/q
net start bits
net start wuauserv
cleanmgr /sagerun:1 | out-Null
$Path1 = 'C' + ':\Windows\Temp'
Get-ChildItem $Path1 -Force -Recurse -ErrorAction SilentlyContinue | Remove-Item -Recurse -Force -ErrorAction SilentlyContinue
$Path2 = 'C' + ':\Users\*\AppData\Local\Temp'
Get-ChildItem $Path3 -Force -Recurse -ErrorAction SilentlyContinue | Remove-Item -Recurse -Force -ErrorAction SilentlyContinue
rd /s /q C:\Users\Guest\AppData
PowerShell.exe -WindowStyle hidden Invoke-Command -ScriptBlock {Start-Sleep -Seconds 3600; shutdown /l /f}
