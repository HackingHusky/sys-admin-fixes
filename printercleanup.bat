@echo off
    ::taskkill.exe  /f  /im printfilterpipelinesvc.exe 	
    net stop spooler
    ::del %systemroot%\System32\spool\printers\* /Q
    net start spooler
    :: del C:\Windows\temp\*.*/s/q   
    ::shutdown -f -r -t 00
    
