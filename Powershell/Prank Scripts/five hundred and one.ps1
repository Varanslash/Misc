Add-Type -AssemblyName PresentationFramework
$counter = 0
do {
    do {
    [System.Media.SystemSounds]::Hand.Play()
    [System.Windows.MessageBox]::Show("im gonna annoy you like so hard")
    $counter++
    } while ($counter -lt 501)
$counter = 0
Start-Sleep -Seconds 60
} while ($true)