Add-Type -AssemblyName presentationCore

$filepath = Read-Host -Prompt "File path of song?"

$mediaPlayer = New-Object system.windows.media.mediaplayer
$mediaPlayer.open($filepath)
$mediaPlayer.Play()

Write-Host "Song Selected: $filepath"
Write-Host "Playing!"

do {
    Start-Sleep -Milliseconds 100
} until ($mediaPlayer.CurrentState -eq 'Stopped')
