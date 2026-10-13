Set-Location $PSScriptRoot
.\.venv\Scripts\python.exe fetch.py; if ($LASTEXITCODE -eq 0) { .\.venv\Scripts\python.exe load.py }