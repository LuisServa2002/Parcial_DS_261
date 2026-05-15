# Plan de Pruebas

## Objetivo
Verificar las funcionalidades de registro, consulta, actualización, eliminación y carga de archivos multimedia.

## Pruebas funcionales

### 1. Crear una incidencia
- Entrada: título, descripción, ubicación, nombre del reportante y media_urls.
- Resultado esperado: código HTTP 201 y objeto de incidencia registrado con categoría fija `Bache`.

### 2. Consultar incidencias
- Entrada: GET `/`.
- Resultado esperado: lista de incidencias con sus campos completos.

### 3. Consultar incidencia por ID
- Entrada: GET `/incidents/{id}`.
- Resultado esperado: detalle de la incidencia solicitada.

### 4. Actualizar incidencia
- Entrada: PUT `/incidents/{id}` con nuevo estatus.
- Resultado esperado: código HTTP 200 y datos actualizados.

### 5. Eliminar incidencia
- Entrada: DELETE `/incidents/{id}`.
- Resultado esperado: código HTTP 204 y la incidencia ya no aparece en la lista.

### 6. Subir archivo multimedia
- Entrada: POST `/media/upload` con un archivo válido.
- Resultado esperado: código HTTP 200 y URL retornada.

## Pruebas unitarias
- Archivo: `backend/tests/test_api.py`.
- Ejecutar: `pytest backend/tests`.
- Cobertura primaria: creación de incidencia, consulta de lista y error por incidencia inexistente.

## Pasos detallados para pruebas CRUD

### 1. Preparar el entorno
- Asegúrese de tener el backend ejecutando en `http://localhost:8000`.
- Abra la documentación interactiva en `http://localhost:8000/docs`.

### 2. Crear una incidencia (`POST /incidents`)
1. En Swagger abra `POST /incidents`.
2. Haga clic en `Try it out`.
3. Use este JSON de ejemplo:

```json
{
  "title": "Bache grande",
  "description": "Hay un bache profundo en la avenida.",
  "location": "Calle 5 con 12",
  "reporter_name": "Luis",
  "media_urls": ["/media/bache.jpg"]
}
```

4. Haga clic en `Execute`.
5. Verifique que la respuesta sea `201` y que devuelva el objeto creado.

### 3. Consultar todas las incidencias (`GET /`)
1. Abra `GET /` en Swagger.
2. Haga clic en `Try it out` y luego en `Execute`.
3. Verifique que la respuesta sea `200` y que la lista contenga las incidencias.

### 4. Consultar una incidencia por ID (`GET /incidents/{incident_id}`)
1. Abra `GET /incidents/{incident_id}`.
2. Haga clic en `Try it out`.
3. Ingrese el ID de una incidencia existente, por ejemplo `1`.
4. Haga clic en `Execute`.
5. Verifique que la respuesta sea `200` y muestre los detalles de la incidencia.

### 5. Actualizar una incidencia (`PUT /incidents/{incident_id}`)
1. Abra `PUT /incidents/{incident_id}`.
2. Haga clic en `Try it out`.
3. Ingrese el ID de una incidencia existente.
4. Use este cuerpo de ejemplo:

```json
{
  "status": "Resuelto",
  "description": "Se reparó el bache."
}
```

5. Haga clic en `Execute`.
6. Verifique que la respuesta sea `200` y que los cambios se hayan aplicado.

### 6. Eliminar una incidencia (`DELETE /incidents/{incident_id}`)
1. Abra `DELETE /incidents/{incident_id}`.
2. Haga clic en `Try it out`.
3. Ingrese el ID de la incidencia a eliminar.
4. Haga clic en `Execute`.
5. Verifique que la respuesta sea `204`.

### 7. Probar el upload de multimedia (`POST /media/upload`)
1. Abra `POST /media/upload`.
2. Haga clic en `Try it out`.
3. Seleccione un archivo válido (imagen, audio o video).
4. Haga clic en `Execute`.
5. Verifique que devuelva una URL en la respuesta, por ejemplo `/media/archivo.jpg`.

### 8. Probar con curl desde PowerShell
#### Crear incidencia
```powershell
curl -X POST http://localhost:8000/incidents `
  -H "Content-Type: application/json" `
  -d "{\"title\":\"Bache\",\"description\":\"Bache grande\",\"location\":\"Calle 5\",\"reporter_name\":\"Luis\",\"media_urls\":[\"/media/bache.jpg\"]}"
```

#### Listar incidencias
```powershell
curl http://localhost:8000/
```

#### Consultar por ID
```powershell
curl http://localhost:8000/incidents/1
```

#### Actualizar incidencia
```powershell
curl -X PUT http://localhost:8000/incidents/1 `
  -H "Content-Type: application/json" `
  -d "{\"status\":\"Resuelto\"}"
```

#### Eliminar incidencia
```powershell
curl -X DELETE http://localhost:8000/incidents/1
```
