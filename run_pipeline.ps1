Set-Location $PSScriptRoot
.\.venv\Scripts\python.exe src\fetch.py
if ($LASTEXITCODE -eq 0) { .\.venv\Scripts\python.exe src\load.py }
if ($LASTEXITCODE -eq 0) { .\.venv\Scripts\python.exe src\transform.py}