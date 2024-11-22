@echo off
netsh int ip reset
netsh advfirewall reset
netsh winsock reset
ipconfig /flushdns
ipconfig /release && ipconfig /renew
