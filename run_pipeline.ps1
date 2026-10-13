Set-Location $PSScriptRoot
python fetch.py; if ($LASTEXITCODE -eq 0) { python load.py }