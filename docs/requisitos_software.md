# Especificación de Requisitos de Software

## 1. Introducción

### 1.1 Propósito
Este documento describe los requisitos del sistema de reporte de baches en vía pública. El sistema permite al ciudadano registrar, consultar, actualizar y eliminar únicamente incidencias de tipo "Bache".

### 1.2 Alcance
El producto es una aplicación web local que contiene un backend en FastAPI y un frontend en HTML/CSS/JavaScript. La base de datos usa SQLite por defecto, con soporte para almacenamiento y entrega de archivos multimedia.

### 1.3 Visión general del producto
- Registro de baches con título, descripción, ubicación, reportante y multimedia.
- Consulta de lista de baches ordenada por fecha.
- Actualización de datos y estado de una incidencia.
- Eliminación de incidencias existentes.
- Gestión de archivos multimedia subidos.

### 1.4 Definiciones
- Incidencia/Bache: reporte de un daño en la vía pública.
- Reportante: persona que registra el bache.
- Multimedia: imagen, video o audio asociado a la incidencia.

## 2. Referencias
- FastAPI
- SQLite
- Pydantic
- Uvicorn
- pytest

## 3. Requisitos específicos

### 3.1 Interfaces externas
- Frontend web local que consume la API REST.
- API REST disponible en `http://localhost:8000`.
- Documentación interactiva Swagger en `/docs`.
- Ruta de archivos multimedia en `/media/{filename}`.

### 3.2 Funciones
1. RF001 - Registrar un bache.
   - El sistema debe aceptar título, descripción, ubicación, nombre del reportante y enlaces a medios.
   - La categoría de incidencia está fijada en `Bache` y no es editable.
   - Debe permitir subir archivos multimedia (imagen, video, audio).
2. RF002 - Consultar todas las incidencias.
   - Retorna la lista de baches ordenada por fecha de creación descendente.
3. RF003 - Consultar una incidencia por ID.
   - Retorna los detalles completos de la incidencia solicitada.
4. RF004 - Actualizar una incidencia.
   - Permite modificar título, descripción, ubicación, reportante, estatus y multimedia.
   - No permite cambiar la categoría.
5. RF005 - Eliminar una incidencia.
   - Permite borrar un registro existente.
6. RF006 - Servir archivos multimedia.
   - Expone las URL de acceso a los archivos subidos.

### 3.3 Requisitos de usabilidad
- Interfaz sencilla en español.
- Formulario claro para registrar un bache.
- Mensajes de estado para el envío y errores.
- Diseño responsive básico.

### 3.4 Requisitos de rendimiento
- Respuesta de API en tiempo razonable para uso local.
- Capacidad para manejar al menos 50 incidencias sin degradación visible.

### 3.5 Requisitos lógicos de base de datos
- Uso de SQLite local como almacenamiento primario.
- Tabla `incidents` con campos: id, título, descripción, categoría, ubicación, reportante, multimedia, estado, fecha de creación y actualización.
- Almacenamiento de rutas de medios en una columna de texto.

### 3.6 Restricciones de diseño
- La categoría de la incidencia es fija en `Bache`.
- El frontend y la API deben ejecutarse localmente sin depender de Docker.
- Separación de capas entre presentación, lógica de negocio y persistencia.

### 3.7 Atributos del sistema
- Aplicación local con CORS habilitado para el frontend.
- Documentación técnica en Markdown.
- Pruebas unitarias con `pytest`.
- Backend en Python con FastAPI.

### 3.8 Información de soporte
- `run.ps1` automatiza la ejecución local.
- Todos los documentos de soporte están en la carpeta `docs/`.

## 4. Verificación
- Validar cada requisito funcional con pruebas manuales y automáticas.
- Ejecutar pruebas unitarias `pytest backend/tests`.
- Comprobar la creación, consulta, actualización y eliminación de baches.
- Verificar la carga y acceso de archivos multimedia.
