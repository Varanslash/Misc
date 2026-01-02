$counter = 0 # variable
Add-Type -AssemblyName PresentationFramework # load assembly for message box
Add-Type -AssemblyName System.Media # load assembly for sound
do {
    [System.Windows.MessageBox]::Show("you are an idiot") # lol
    [System.Media.SystemSounds]::Exclamation.Play() # play sound
    New-Item -Path "C:\Users\$env:USERNAME\Downloads\YOUR COMPUTER HAS BEEN INFECTED $counter.txt" -ItemType File # spawns new file to scare recipient
    Set-Content -Path "C:\Users\$env:USERNAME\Downloads\YOUR COMPUTER HAS BEEN INFECTED $counter.txt" -Value "you are an idiot" # lol
    $counter++ # increment counter
} while ($counter -lt 20) # repeat 20 times