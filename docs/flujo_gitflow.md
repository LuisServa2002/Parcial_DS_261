# Flujo de Trabajo GitFlow para el Proyecto

## Ramas principales
- `main`: Contiene la versión estable y lista para producción.
- `develop`: Contiene el desarrollo integrado y las nuevas características en curso (donde cada subrama al final de cada tarea creada en el Jira , pasara a realizar un merge con esta rama `develop`).
- 
## Ramas de soporte
- `SCRUM-(numero)/*`: Para desarrollar nuevas funciones , estás ramas fueron creadas para tareas especificas y además para conectarlo con Jira.


## Flujo básico
1. Crear una rama `SCRUM-(numero)/X` desde `develop`.
2. Implementar y probar la funcionalidad.
3. Hacer merge de la rama `SCRUM-(numero)` en `develop` una vez completa.
4. Al final de todo el proyecto hacer un merge desde `develop` a `main`.