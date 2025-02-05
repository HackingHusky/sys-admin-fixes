##powershell to install chrome

winget install -e --id Google.Chrome

## or Install-Module -Name Microsoft.WinGet.Client

##or $LocalTempDir = $env:TEMP; $ChromeInstaller "ChromeInstaller.exe"; (New-Object System.Net.WebClient).DownloadFile('http://dl.google.com/chrome/install/375.126/chrome_installer.exe', "$LocalTempDir\$ChromeInstaller"); & "$LocalTempDir\$ChromeInstaller" /silent /install; $Process2Monitor =  "ChromeInstaller"; Do { $ProcessesFound = Get-Process | ?{$Process2Monitor -contains $_.Name} | Select-Object -ExpandProperty Name; If ($ProcessesFound) { "Still running: $($ProcessesFound -join ', ')" | Write-Host; Start-Sleep -Seconds 2 } else { rm "$LocalTempDir\$ChromeInstaller" -ErrorAction SilentlyContinue -Verbose } } Until (!$ProcessesFound)

## you may have to run this as well
##$TLS12Protocol = [System.Net.SecurityProtocolType] 'Ssl3 , Tls12'
##[System.Net.ServicePointManager]::SecurityProtocol = $TLS12Protocol
## only in case of the tls needs to be updated to install