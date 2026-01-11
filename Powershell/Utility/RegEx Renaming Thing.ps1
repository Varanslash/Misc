$filepath = Read-Host -Prompt "Enter File path"
$filename = Read-Host -Prompt "Enter New filename"
$pattern = Read-Host -Prompt "Enter RegEx Pattern"
$incid = 0

$subdirectories = Get-ChildItem -Path $filepath

foreach ($dir in $subdirectories) {
    if ($dir.Name -match $pattern) {
        $incid++
        $newName = "$filename - $incid"
        Rename-Item -Path $dir.FullName -NewName $newName
        Write-Host "Renamed '$($dir.Name)' to '$newName'"
    }
}

Write-Host "Renaming Complete! Press Ctrl + C to exit!"
while ($true) {}
