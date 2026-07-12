# Pruebas de persistencia — H6

| ID | Caso | Pasos | Esperado | Obtenido | Estado |
|---|---|---|---|---|---|
| P01 | Cargar recuerdos | Ejecutar y escribir `memoria` | Muestra recuerdos iniciales | Muestra Traer pendrive y Repasar Scanner | Correcto |
| P02 | Guardar nuevo recuerdo | `recuerda` + `Preparar demo` + `guardar` | Fichero actualizado | Se guarda en `data/recuerdos.txt` | Correcto |
| P03 | Segunda ejecución | Volver a ejecutar y escribir `memoria` | Aparece el nuevo recuerdo | Aparece Preparar demo | Correcto |
| P04 | Fichero inexistente | Borrar `data/recuerdos.txt` en copia de prueba | Se crea vacío | Se crea sin romper | Correcto |

<!-- AJUSTE-COBERTURA-CONCEPTOS-32 -->

## Respuesta de Laura — cobertura de conceptos de Programación

Relación con `32-lista-conceptos-programacion-por-tema.md`:

```text
H6 trabaja principalmente: Temas 5, 6 y puente hacia Tema 8.
Foco de aprendizaje: persistencia, logs, errores y trazabilidad.
```

Conceptos que Laura debe saber defender en este hito:

- clases responsables
- excepciones checked y runtime
- throws
- validación
- invariantes
- repositorio como idea inicial
- ficheros
- logs
- seguridad
- Repository como patrón opcional
- pruebas de dos ejecuciones
- trazabilidad

Respuesta modelo de Laura:

> En H6 explico cómo demuestro persistencia cerrando y abriendo el programa, y por qué los logs no deben guardar secretos ni datos personales.

Evidencia que Laura debe señalar:

- una parte concreta del código o documento donde aparezca el concepto;
- una prueba, ejecución, captura o explicación que demuestre que no lo ha copiado sin entender;
- una mejora razonable que podría hacer si tuviera más tiempo.

