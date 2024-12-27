# Function to prompt the user for confirmation
function Confirm-Action {
param (
[string]$Message
)
$confirmation = Read-Host "$Message (y/n)"
return $confirmation -eq 'y'
}
# Function to remove a given app
function Remove-App {
param (
[string]$AppName
)
if (Confirm-Action "Do you want to remove $AppName ?") {
Get-AppxPackage -Name $AppName | Remove-AppxPackage
Write-Output "$AppName removed."
} else {
Write-Output "Skipped removing $AppName"
}
}
# List apps to remove (The below example contains some default Windows apps, feel free to add your own, or remove entries)
$appsToRemove = @(
"Microsoft.3DBuilder",
"Microsoft.BingWeather",
"Microsoft.GetHelp",
"Microsoft.Getstarted",
"Microsoft.Microsoft3DViewer",
"Microsoft.MicrosoftOfficeHub",
"Microsoft.MicrosoftSolitaireCollection",
"Microsoft.MicrosoftStickyNotes",
"Microsoft.MixedReality.Portal",
"Microsoft.MSPaint",
"Microsoft.Office.OneNote",
"Microsoft.People",
"Microsoft.Print3D",
"Microsoft.SkypeApp",
"Microsoft.WindowsAlarms",
"Microsoft.WindowsCamera",
"Microsoft.WindowsFeedbackHub",
"Microsoft.WindowsMaps",
"Microsoft.WindowsSoundRecorder",
"Microsoft.XboxApp",
"Microsoft.XboxGameOverlay",
"Microsoft.XboxGamingOverlay",
"Microsoft.XboxIdentityProvider",
"Microsoft.XboxSpeechToTextOverlay",
"Microsoft.YourPhone"
)
# Loop through app list and prompt for removal
foreach ($app in $appsToRemove) {
Remove-App -AppName $app
}
# Function to set a registry key value
function Set-RegistryKey {
param (
[string]$Path,
[string]$Name,
[string]$Value
)
if (Confirm-Action "Do you want to set $Name in $Path to $Value ?") {
Set-ItemProperty -Path $Path -Name $Name -Value $Value
Write-Output "Set $Name in $Path to $Value"
} else {
Write-Output "Skipped setting $Name in $Path"
}
}
# Disable telemetry in using the registry
Set-RegistryKey -Path "HKLM:\SOFTWARE\Policies\Microsoft\Windows\DataCollection" -Name "AllowTelemetry" -Value 0
Write-Output "Windows Debloat completed"
