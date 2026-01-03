# I'd like you to go read the README now.

$counter = 0 # variable
Add-Type -AssemblyName PresentationFramework # load assembly for message box
do {
    [System.Windows.MessageBox]::Show("you are an idiot") # lol
    New-Item -Path "C:\Users\$env:USERNAME\Downloads\YOUR COMPUTER HAS BEEN INFECTED $counter.txt" -ItemType File # spawns new file to scare recipient
    Set-Content -Path "C:\Users\$env:USERNAME\Downloads\YOUR COMPUTER HAS BEEN INFECTED $counter.txt" -Value "you are an idiot" # lol
    $counter++ # increment counter

} while ($counter -lt 20) # repeat 20 times

<#
Essentially what this virus does is show a message box with a message reminiscent of "you are an idiot" from a while ago, 
then spawns a .txt file with the title "YOUR COMPUTER HAS BEEN INFECTED" and text saying "you are an idiot". That's about it.

If you want further explanation on the script, ask a knowledgeable friend or paste it into ChatGPT, and if you don't feel safe running it, I won't mind! Just don't
run it and move on with your day.

Have fun nerds!
#>

