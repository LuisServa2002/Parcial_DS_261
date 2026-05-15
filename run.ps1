# Ejecuta el proyecto completo en Windows.
# Abre una terminal para el backend y otra para el frontend.

$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$backendPath = Join-Path $root 'backend'
$frontendPath = Join-Path $root 'frontend'
$venvPath = Join-Path $backendPath '.venv'
$envFile = Join-Path $backendPath '.env'
$envExample = Join-Path $backendPath '.env.example'

Write-Host "Iniciando automatización del proyecto..."

if (-not (Test-Path $venvPath)) {
    Write-Host "Creando entorno virtual..."
    python -m venv $venvPath
}

Write-Host "Instalando dependencias..."
& "$venvPath\Scripts\python.exe" -m pip install --upgrade pip
& "$venvPath\Scripts\python.exe" -m pip install -r "$backendPath\requirements.txt"

if (-not (Test-Path $envFile)) {
    Write-Host "Copiando archivo .env de ejemplo..."
    Copy-Item $envExample $envFile
}

Write-Host "Iniciando backend en nueva terminal..."
Start-Process powershell -ArgumentList '-NoExit', '-Command', "cd '$backendPath'; Remove-Item Env:DATABASE_URL -ErrorAction SilentlyContinue; . '.\.venv\Scripts\Activate.ps1'; uvicorn app.main:app --reload --host 0.0.0.0 --port 8000"

Write-Host "Iniciando frontend en nueva terminal..."
Start-Process powershell -ArgumentList '-NoExit', '-Command', "cd '$frontendPath'; python -m http.server 5500"

Start-Process 'http://localhost:5500'
Write-Host "Listo. El frontend debería abrirse en el navegador."