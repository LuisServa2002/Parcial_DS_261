# Ejecuta el backend localmente en Windows.

python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install -r requirements.txt
if (-not (Test-Path .env)) {
    Copy-Item .env.example .env
    Write-Host "Se copió .env.example a .env. Ajusta DATABASE_URL si es necesario."
}
Write-Host "Iniciando FastAPI..."
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
