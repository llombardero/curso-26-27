# Guía docente — H6 Agente persistente y trazable

<!-- HEXA-CICLO-COMPLETO-POR-HITO:START -->

## Ciclo HEXA obligatorio del reto H6

**Reto del hito:** Conservar memoria e historial entre ejecuciones con ficheros, trazabilidad y tratamiento seguro de errores y datos.

**Base transversal — Fase 0 Equipos:** se mantienen roles, normas, colaboración y herramientas de organización durante todo el reto. El profesorado hace visible el avance de fase y sitúa la instrucción guiada principalmente en Investigar, sin reducir HEXA a una etiqueta.

| Fase | Pregunta que guía la fase | Acción del profesorado | Acción y evidencia del alumnado |
|---|---|---|---|
| **1 — Activar** | ¿Qué reto real debemos entender y con qué propósito, límites y criterios? | Presenta y contextualiza el reto sin anticipar la solución. | Reformula el reto y explicita objetivos, dudas y criterios. |
| **2 — Investigar** | ¿Qué necesitamos aprender para abordar el reto? | Facilita búsqueda guiada, micropíldoras y fuentes seguras. | Investiga, contrasta, practica y construye la base conceptual necesaria. |
| **3 — Idear** | ¿Qué soluciones posibles podemos proponer y cuál elegimos? | Abre alternativas y exige criterios de selección. | Genera, compara y argumenta una solución viable. |
| **4 — Planificar** | ¿Cómo convertimos la idea en tareas, tiempos y responsabilidades? | Ayuda a hacer visibles backlog, hitos, dependencias y criterios de seguimiento. | Organiza tareas, tiempos, responsabilidades y comprobaciones. |
| **5 — Ejecutar** | ¿Cómo construimos, probamos y mejoramos la solución? | Desbloquea sin sustituir la autoría y exige iteración y pruebas. | Crea el producto, lo prueba, corrige y conserva evidencias. |
| **6 — Comunicar** | ¿Cómo presentamos, evaluamos y reflexionamos sobre producto y proceso? | Facilita defensa, evaluación formativa, coevaluación y mejora. | Presenta, defiende, evalúa, reflexiona y formula el siguiente paso. |

### Temporalización explícita sobre las sesiones operativas

Las fases siguen el orden canónico y pueden solaparse cuando una sesión cierra una y abre la siguiente.

| Fase | Sesiones de referencia | Puerta de salida |
|---|---|---|
| 1 — Activar | S279 | Reto comprendido y criterios visibles. |
| 2 — Investigar | S280–S282 | Conocimientos necesarios contrastados. |
| 3 — Idear | S283 | Solución seleccionada y argumentada. |
| 4 — Planificar | S284 | Plan, responsabilidades y comprobaciones visibles. |
| 5 — Ejecutar | S285–S288 | Producto construido, probado y mejorado. |
| 6 — Comunicar | S289–S291 | Defensa, evaluación, reflexión y mejora. |

**Expediente HEXA mínimo del hito:** problema reproducido, decisiones de ruta/formato, explicación de persistencia/excepciones/logs, código, prueba en dos ejecuciones, seguridad y defensa.

Regla de avance: puede haber prototipos durante Investigar o Idear, pero Ejecutar no se considera completada si faltan evidencias de Activar, Investigar, Idear o Planificar. Comunicar exige presentar, evaluar y reflexionar. Si falta una fase, se recuperan esa fase y su evidencia; no se repite automáticamente todo el hito.

<!-- HEXA-CICLO-COMPLETO-POR-HITO:END -->


## Programación + Entornos de Desarrollo — 1.º DAW — Curso 2026/2027

Edición final para Moodle — septiembre de 2026

Documentos relacionados:

- `../../02-calendario-hitos-sprints-2026-2027.md`
- `../../04A-enunciados-y-entregables-alumnado.md`
- `../../06-rubricas-hitos.md`
- `README.md`
- `18B-ficha-alumnado-h6-persistente-trazable.md`
- `18C-checklist-correccion-h6.md`

---

## 1. Propósito del hito

H6 hace que MiniJarvis deje de depender solo de la memoria temporal.

Producto esperado:

```text
MiniJarvis H6: agente con memoria persistente en ficheros, historial/logs simples, ejecución reproducible y decisiones de seguridad documentadas.
```

---

## 2. Qué añade H6 respecto a H5

| H5 | H6 |
|---|---|
| Herramientas internas extensibles. | Herramientas que leen/escriben ficheros. |
| Memoria temporal. | Memoria persistente entre ejecuciones. |
| Revisión/refactorización. | Reproducibilidad y pruebas de persistencia. |
| Decisión sobre patrón. | Decisiones de seguridad y trazabilidad. |

---

## 3. Restricciones didácticas y seguridad

En H6 sí debe aparecer:

- lectura/escritura de ficheros;
- carga inicial o comando de carga;
- guardado de recuerdos;
- logs o historial simple;
- pruebas de persistencia;
- README reproducible;
- documento de seguridad.

En H6 NO debe aparecer:

- credenciales reales;
- datos personales reales en ficheros de ejemplo;
- `.env` real subido;
- tokens/API keys;
- base de datos compleja obligatoria;
- IA real obligatoria.

---

## 4. Fechas y duración

Fechas orientativas:

```text
1-23 abril 2027
```

---

## 5. RA/CE y evidencias

### Programación

- PR RA5: entrada/salida y gestión de información persistente.
- PR RA8/RA9 como ampliación si procede.

### Entornos de Desarrollo

- ED RA3: pruebas e incidencias.
- ED RA4: documentación, repositorio, reproducibilidad y CI si procede.

Evidencias clave:

- `data/recuerdos.txt` o equivalente sin datos personales;
- `logs/historial.log` o equivalente;
- pruebas de persistencia;
- README para ejecutar desde cero;
- registro de seguridad.

---

## 6. Diseño mínimo recomendado

Clases posibles:

| Clase | Responsabilidad |
|---|---|
| `PersistentMemory` | Cargar y guardar recuerdos en fichero. |
| `HistoryLog` | Registrar eventos simples. |
| `Agent` | Orquestar herramientas. |
| `Tool` | Contrato para herramientas. |

Formato recomendado para empezar:

```text
data/recuerdos.txt
logs/historial.log
```

---

## 7. Entregables H6

| Entregable | Responsable | Formato | Plantilla local |
|---|---|---|---|
| Código persistente | Equipo/individual | `src/*.java` | No aplica. |
| README reproducible | Equipo | `README.md` | `plantillas/README-h6-plantilla.md` |
| Ficheros de ejemplo | Equipo | `data/`, `logs/` | No aplica. |
| Pruebas de persistencia | Equipo | `docs/pruebas-persistencia-h6.md` | `plantillas/pruebas-persistencia-h6-plantilla.md` |
| Seguridad | Equipo | `docs/seguridad-h6.md` | `plantillas/seguridad-h6-plantilla.md` |
| Logs/historial | Equipo | `docs/logs-historial-h6.md` | `plantillas/logs-historial-h6-plantilla.md` |
| Incidencia | Si procede | `docs/incidencia-h6.md` | `plantillas/incidencia-h6-plantilla.md` |
| Comparación Java ↔ Python | Individual | `docs/comparacion-java-python-h6.md` | `plantillas/comparacion-java-python-h6-plantilla.md` |
| Portfolio H6 | Individual | `docs/portfolio-h6.md` | `plantillas/portfolio-h6-plantilla.md` |
| Registro IA | Individual/equipo | `docs/registro-ia.md` | `plantillas/registro-ia-h6-plantilla.md` |
| Defensa H6 | Individual | `docs/defensa-h6.md` | `plantillas/defensa-h6-plantilla.md` |

---

## 8. Errores previsibles

| Error | Señal | Intervención docente |
|---|---|---|
| Guarda datos personales reales | Ficheros con nombres/teléfonos reales | Sustituir por datos ficticios. |
| Sube `.env` real | Riesgo de secreto | Borrar, rotar si procede, usar `.env.example`. |
| No crea carpetas | Error si `data/` no existe | Usar `Files.createDirectories`. |
| No prueba segunda ejecución | Persistencia no demostrada | Prueba: guardar, cerrar, abrir, consultar. |
| README no reproduce | Doc incompleta | Ejecutar desde cero siguiendo README. |

---

## 9. Preparación para H7

Antes de pasar a H7, comprobar:

- si el agente guarda y recupera;
- si los logs no contienen datos sensibles;
- si el README permite ejecutar desde cero;
- si no hay secretos;
- si las pruebas de persistencia son reproducibles.

H7 tratará integración IA responsable real o simulada.

## Cobertura curricular de Programación

Este hito queda alineado con el mapa `32-lista-conceptos-programacion-por-tema.md`.

```text
Hito: H6
Temas de referencia: Temas 5, 6 y puente hacia Tema 8
Foco: persistencia, logs, errores y trazabilidad
```

Conceptos que deben trabajarse o, como mínimo, quedar conectados con evidencias del alumnado:

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

Criterio docente de cierre:

- El alumnado no solo entrega el producto; debe poder señalar dónde aparece cada concepto en su código, README, pruebas o defensa.
- Si un concepto se marca como ampliación, no penaliza al alumnado que alcance el mínimo, pero sí orienta mejora, recuperación o enriquecimiento.
- La defensa debe incluir al menos una pregunta de comprensión sobre los conceptos nuevos del hito.

