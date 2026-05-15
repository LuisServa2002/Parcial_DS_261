# Informe del examen parcial

### 1. Preparar el entorno
- Asegúrese de tener el backend ejecutando en `http://localhost:8000`.
- Abra la documentación interactiva en `http://localhost:8000/docs`.

### 2. Crear una incidencia (`POST /incidents`)

Crearemos una incidencia que se almacenara con un **ID 4**.
![alt text](post_incidente.png)


### 3. Consultar todas las incidencias (`GET /`)

![alt text](get_inicial.png)

### 4. Consultar una incidencia por ID (`GET /incidents/

En este caso eligiremos el incidente 4.

![alt text](get_id_especifico.png)

### 5. Actualizar una incidencia (`PUT /incidents/

![alt text](put_incidente.png)

Además en la intefaz principal verificamos que paso de pendiente a resuelto.

![alt text](resultado_put.png)

### 6. Eliminar una incidencia (`DELETE /incidents/{incident_id}`)

Eliminamos este incidente (incidente 4).

![alt text](delete_incidente.png)