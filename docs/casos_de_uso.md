# Casos de Uso / Historias de Usuario

## Historia 1: Reportar un bache
**Actor:** Ciudadano

### Precondición
El ciudadano accede a la aplicación desde el navegador.

### Flujo principal
1. El ciudadano completa el formulario de incidencia.
2. Adjunta una imagen del bache.
3. Envía el reporte.
4. El sistema almacena la incidencia y devuelve confirmación.

### Resultado esperado
La incidencia queda registrada en la base de datos y puede visualizarse desde la lista de incidencias.

## Historia 2: Consultar un bache registrado
**Actor:** Operador municipal

### Precondición
El operador tiene acceso al frontend y a la API.

### Flujo principal
1. El operador abre la lista de incidencias.
2. Selecciona un registro de bache existente.
3. Consulta los detalles y las imágenes adjuntas.

### Resultado esperado
El operador visualiza el bache, su ubicación y los medios asociados.

## Historia 3: Actualizar el estado de un bache
**Actor:** Inspector de servicio

### Precondición
Existe un bache registrado en el sistema.

### Flujo principal
1. El inspector consulta la incidencia por su ID.
2. Actualiza el estado a `Resuelto`.
3. El sistema guarda la actualización.

### Resultado esperado
El estado de la incidencia se actualiza y queda disponible en la API.

## Desde ejecución

Inicia reporte: 

![alt text](iniciar_reporte.png)

Verificamos que se ha enviado:

![alt text](reporte_almacenado.png)

Verificamos la imagen:

![alt text](resultado_imagen.png)

Además el operador municipal podrá visualizar los reportes generados y decidi si lo resuelvo o no.

![alt text](put_incidente.png)


![alt text](resultado_put.png)

