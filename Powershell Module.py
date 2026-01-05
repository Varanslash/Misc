import subprocess

def powershell(cmdlet):
    completed = subprocess.run(["powershell", "-Command", cmdlet], capture_output=True, text=True)
    print(completed.stdout.strip())

powershell(""" Write-Host "hi" """)
