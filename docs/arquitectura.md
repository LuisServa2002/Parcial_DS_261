# Arquitectura del Sistema

## Visión general
La solución está dividida en tres capas:

1. **Frontend**: Interfaz web simple en HTML/CSS/JavaScript que consume la API.
2. **Backend**: API REST construida con FastAPI y patrones de diseño como repositorio y inyección de dependencias.
3. **Base de datos**: SQLite local por defecto.
4. **Dominio**: la aplicación maneja un único tipo de incidencia: `Bache`.

## Componentes principales

- `backend/app/main.py`: controla las rutas y la lógica de la API.
- `backend/app/crud.py`: capa de acceso a datos que representa el patrón Repository.
- `backend/app/models.py`: define el modelo de dominio `Incident`.
- `backend/app/schemas.py`: define los DTOs de entrada y salida con Pydantic.
- `backend/app/database.py`: establece la conexión con la base de datos configurada en `backend/.env`.

## Patrones de diseño usados

- **Repository**: interioriza operaciones de lectura/escritura de la base de datos en `crud.py`.
- **Dependency Injection**: con FastAPI y `Depends(get_db)` para inyectar sesiones.
- **DTO / Data Transfer Object**: con Pydantic en `schemas.py` para separar el modelo de datos de la API.
- **Separación de capas**: separación clara de presentación, dominio y persistencia.

## Despliegue y ejecución

- `run.ps1`: automatiza la ejecución local del backend y frontend.
- `backend/.env.example`: muestra la configuración de SQLite local y una opción comentada para PostgreSQL.

## Flujo de datos

1. El frontend envía una petición HTTP a la API.
2. FastAPI valida la petición mediante Pydantic.
3. El backend utiliza `crud.py` para operar en la base de datos.
4. Los registros quedan guardados en la base de datos local (SQLite) como incidencias de tipo `Bache`.
5. Los medios se almacenan en `backend/media` y se sirven desde `/media/{filename}`.
