# Capítulo 09 — Ficheros, persistencia y logs

## Hitos relacionados

```text
H6
```

## Qué aprenderás

- persistencia
- Path
- Files
- createDirectories
- lectura/escritura
- logs
- seguridad básica

## 1. Punto de partida

MiniJarvis se construye por capas. Este capítulo trabaja una pieza concreta del proyecto y la conecta con evidencias reales: código, pruebas, documentación, defensa y uso responsable de IA si procede.

La regla de estudio es siempre la misma:

```text
Lee el concepto, ejecuta un ejemplo pequeño, aplícalo a MiniJarvis, documenta la evidencia y prepárate para defenderlo.
```

## 2. Conceptos básicos explicados

La memoria temporal desaparece al cerrar. La persistencia guarda información fuera del programa, normalmente en ficheros o bases de datos. En H6 usamos ficheros de texto para entender el proceso.

`data/recuerdos.txt` guarda recuerdos ficticios. `logs/historial.log` registra eventos técnicos. Antes de escribir hay que crear carpetas con `Files.createDirectories`. Los logs no deben guardar secretos.

## 3. Ejemplo guiado en Java

```java
Path path = Path.of("data/recuerdos.txt");
Files.createDirectories(path.getParent());
Files.write(path, memories);

Path log = Path.of("logs/historial.log");
Files.createDirectories(log.getParent());
Files.writeString(log, "Memory added
", StandardOpenOption.CREATE, StandardOpenOption.APPEND);
```

## 4. Caso práctico MiniJarvis

Crea `PersistentMemory` para cargar y guardar recuerdos. Prueba en dos ejecuciones: en la primera guardas, cierras; en la segunda abres y consultas.

Añade `HistoryLog` con eventos: Agent started, Memory added, Agent stopped.

## 5. Evidencia de Entornos de Desarrollo

Crea `docs/pruebas-persistencia.md`, `docs/seguridad.md` y `docs/logs-historial.md`. Incluye `.gitignore` con `.env`, `*.key`, `*.token`.

## 6. Errores frecuentes y cómo corregirlos

| Error | Síntoma | Corrección |
|---|---|---|
| Probar solo una ejecución | No demuestra persistencia | Cerrar y abrir de nuevo |
| No crear carpetas | Error al escribir | Usar createDirectories |
| Logs con datos sensibles | Se guardan secretos | Registrar eventos técnicos |

## 7. Preguntas de repaso

1. ¿Qué diferencia hay entre memoria temporal y persistencia?
2. ¿Qué demuestra una prueba en dos ejecuciones?
3. ¿Por qué un log puede ser peligroso?
4. ¿Qué debe incluir .gitignore?

## 8. Para tu portfolio

Copia y completa este bloque en tu portfolio:

```text
Capítulo 09: Ficheros, persistencia y logs
Qué he aprendido:
Código o documento que lo demuestra:
Prueba realizada:
Error que he corregido:
Qué puedo defender oralmente:
Uso de IA, si lo hubo, y cómo lo validé:
```

## 9. Estudio paso a paso

La persistencia se demuestra cerrando y abriendo. Si solo guardas en una lista, no has superado H6. El fichero debe poder inspeccionarse. La ruta debe ser relativa para que otra persona pueda ejecutar el proyecto sin depender de tu ordenador.

Caso de estudio: borra temporalmente `data/recuerdos.txt`, ejecuta MiniJarvis, guarda un recuerdo ficticio, sal, abre el fichero y comprueba el contenido. Después ejecuta de nuevo y consulta memoria. Documenta también qué aparece en el log. Si el log contiene un secreto o dato personal, corrígelo.
