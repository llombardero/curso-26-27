# Pruebas de persistencia — H6

| ID | Caso | Pasos | Esperado | Obtenido | Estado |
|---|---|---|---|---|---|
| P01 | Cargar recuerdos | Ejecutar y escribir `memoria` | Muestra recuerdos iniciales | Muestra Traer pendrive y Repasar Scanner | Correcto |
| P02 | Guardar nuevo recuerdo | `recuerda` + `Preparar demo` + `guardar` | Fichero actualizado | Se guarda en `data/recuerdos.txt` | Correcto |
| P03 | Segunda ejecución | Volver a ejecutar y escribir `memoria` | Aparece el nuevo recuerdo | Aparece Preparar demo | Correcto |
| P04 | Fichero inexistente | Borrar `data/recuerdos.txt` en copia de prueba | Se crea vacío | Se crea sin romper | Correcto |
