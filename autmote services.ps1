   $files = Get-ChildItem -Path "C:\Logs" -Filter "*.log"
   foreach ($file in $files) {
       if ($file.LastWriteTime -lt (Get-Date).AddDays(-7)) {
           Remove-Item $file.FullName -Force
       }
   }