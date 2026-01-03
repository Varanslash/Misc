Add-Type -AssemblyName PresentationFramework
New-Item -Path "C:\Users\$env:USERNAME\Downloads\Placeholder.asm" -ItemType File
Set-Content -Path "C:\Users\$env:USERNAME\Downloads\Placeholder.asm" -Value "; This is a placeholder assembly file"
