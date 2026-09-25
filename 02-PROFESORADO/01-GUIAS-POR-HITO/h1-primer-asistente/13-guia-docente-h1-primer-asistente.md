# Guía docente H1 — Primer MiniJarvis

## 1. Decisión pedagógica vigente

H1 cubre el Tema 1 completo con dos niveles de evidencia:

- **producto mínimo:** programa lineal, pequeño, ejecutable y defendible;
- **microprácticas:** demostraciones separadas de los conceptos que sobrecargarían `Main.java`.

Las comparaciones, booleanos y un `if/else` básico se introducen en H1. H2 no vuelve a presentarlos como novedad: los aplica a menú, comandos, repetición, validación de entradas, pruebas y depuración.

## 2. Alcance del producto

El incremento principal debe incluir clase `Main`, método `main`, salida clara, `Scanner`, variables tipadas, al menos una constante, una operación sencilla y ejecución repetible.

No se exige integrar en el producto todas las conversiones, comparaciones o decisiones. Su evidencia puede ser una micropráctica defendible. H1 no incorpora todavía menú, bucle principal, `switch`, colecciones, persistencia, clases de dominio ni IA real.

## 3. Cobertura curricular

| Núcleo | Tratamiento en H1 | Continuidad en H2 |
|---|---|---|
| entorno, JDK, compilación y JVM | comprensión y ejecución | uso autónomo |
| sintaxis, clase y `main` | construcción mínima | consolidación |
| tipos, variables, constantes y literales | uso y explicación | aplicación |
| operaciones y precedencia | predicción y micropráctica | aplicación |
| `Scanner`, conversiones y casting | lectura, prueba y error básico | entradas de comandos y validación |
| comparaciones y booleanos | producción y lectura | combinación en lógica de menú |
| `if/else`, anidamiento y `?:` | lectura y decisión elemental | diseño, pruebas y depuración de flujo |

La evaluación fuerte de control de flujo pertenece a RA3/H2. En H1 estas decisiones aportan evidencia inicial de comprensión del Tema 1 y no deben duplicar la calificación de H2.

## 4. Temporalización canónica

| Sesión | Periodos | HEXA | Puerta de avance |
|---|---:|---|---|
| S206 | 2 | Activar | alcance clasificado y salida esperada |
| S207 | 3 | Investigar | proyecto mínimo ejecutado y error interpretado |
| S208 | 2 | Investigar | estructura Java reconstruida y explicada |
| S209 | 2 | Idear | alternativa elegida y salida diseñada |
| S210 | 2 | Planificar | variables tipadas y plan viable |
| S211 | 2 | Ejecutar | operaciones predichas y comprobadas |
| S212 | 3 | Ejecutar | entrada convertida y error comprendido |
| S213 | 3 | Ejecutar | booleanos y dos ramas probadas |
| S214 | 3 | Comunicar | README probado, evidencias enlazadas y permisos comprobados |
| S215 | 2 | Comunicar | defensa, modificación y siguiente paso |
| **Total** | **24** |  |  |

Las presentaciones organizan checkpoints de 45 minutos. Los periodos adicionales son talleres asociados; no deben convertirse en nuevas evidencias obligatorias.

<!-- HEXA-CICLO-COMPLETO-POR-HITO:START -->

### Ciclo HEXA canónico de H1

1. **1 — Activar** — entender el reto y delimitar el producto.
2. **2 — Investigar** — aprender lo necesario sobre entorno, estructura y salida.
3. **3 — Idear** — proponer mensajes y comportamiento mínimo.
4. **4 — Planificar** — organizar datos, operaciones, tareas y pruebas.
5. **5 — Ejecutar** — crear, convertir, comparar, decidir y comprobar.
6. **6 — Comunicar** — documentar, enlazar, defender y reflexionar.

<!-- HEXA-CICLO-COMPLETO-POR-HITO:END -->

## 5. Patrón de cada checkpoint

1. Activación o predicción breve.
2. Micropíldora docente acotada.
3. Micropráctica con resultado observable.
4. Prueba o explicación.
5. Registro único en el diario al cerrar el checkpoint.

Si falta tiempo, se reduce la cantidad de ejemplos o se realiza una demostración colectiva. No se elimina el núcleo conceptual de la sesión.

## 6. Evidencia única

| Función | Fuente de verdad |
|---|---|
| código y evolución | GitHub/repo y commits |
| instrucciones, ejecución y pruebas | README |
| proceso individual e IA personal | diario individual |
| planificación, decisiones, bloqueos, review, retrospectiva e IA de equipo | Sheet Scrum |
| selección personal | Site personal |
| comunicación del incremento | Site de equipo |
| índice de entrega | Moodle |
| autoría y comprensión | defensa y modificación |

Normas:

- una fila de diario por checkpoint o evidencia significativa, no una narración por cada actividad;
- una tarea, decisión o bloqueo de equipo se registra una sola vez en Scrum;
- Sites seleccionan y enlazan: no copian el diario ni Scrum;
- Moodle recibe enlaces profundos: no nuevas copias;
- las plantillas auxiliares son andamiajes opcionales, no entregables automáticos.

## 7. Uso de IA

El uso personal se registra en las columnas `Uso de IA` y `Cómo validé la IA` del diario. El uso colectivo se registra en `REGISTRO_IA_EQUIPO` de Scrum. Solo se solicita un registro ampliado cuando el uso sea complejo o exista una incidencia de autoría.

Toda evidencia debe mostrar finalidad, resultado aprovechado, cambios propios y validación. No se acepta código que la persona no pueda explicar y modificar.

## 8. Sites y permisos

- Site personal: una aportación, una evidencia profunda, un aprendizaje, un bloqueo y una mejora.
- Site de equipo: incremento, repo/README, decisión, prueba, review y retrospectiva.
- Comprobar permisos con una cuenta distinta antes de Moodle.
- Evitar datos personales, credenciales y observaciones privadas.

## 9. Evaluación

La rúbrica común H1 se aplica sobre estas fuentes:

- producto y funcionamiento: repo y README;
- Tema 1: producto más microprácticas;
- proceso: diario y Scrum;
- comunicación: Sites y defensa;
- IA: únicamente cuando haya uso, con verificación y autoría.

Una evidencia puede cubrir varios criterios. No se multiplica la calificación por repetirla en varios soportes.

La complejidad adelantada no se premia por sí misma: solo cuenta cuando respeta el alcance, mejora el producto y la persona puede explicarla, probarla y modificarla. La trazabilidad normativa se consulta en `02-PROFESORADO/00-PROGRAMACION-Y-COORDINACION/01-matriz-integrada-ra-ce-evidencias-tareas.md`; esta guía no mantiene una segunda copia de RA y criterios.

## 10. Recuperación

La recuperación debe ser mínima y específica:

- error de entorno: reconstruir y ejecutar un proyecto mínimo;
- concepto: predecir, ejecutar y explicar una micropráctica;
- producto: corregir el criterio incumplido;
- autoría: explicar y modificar en directo;
- evidencia: reparar el enlace o permiso, no rehacer el trabajo.

## 11. Riesgos a vigilar

- convertir las diez presentaciones en diez clases magistrales;
- forzar todos los conceptos dentro de `Main.java`;
- evaluar `if/else` dos veces, en H1 y H2;
- pedir captura, transcripción, ficha y Site para la misma ejecución;
- confundir registro de proceso con portfolio público;
- publicar datos personales o credenciales;
- conservar archivos generados sin actualizar sus fuentes.

## 12. Fuentes canónicas

- calendario: `02-PROFESORADO/00-PROGRAMACION-Y-COORDINACION/02-calendario-hitos-sprints-2026-2027.md`;
- alumnado: `01-ALUMNADO/02-HITOS/h1-primer-asistente/13B-ficha-alumnado-h1-primer-asistente.md` y `01-ALUMNADO/03-SESIONES/h1/`;
- profesorado: `02-PROFESORADO/02-SESIONES/h1/`;
- referencia integral de código docente: `02-PROFESORADO/00-PROGRAMACION-Y-COORDINACION/200C-material-teorico-practico-sesiones-201-306.md`;
- corrección y defensa: `02-PROFESORADO/01-GUIAS-POR-HITO/h1-primer-asistente/13C-checklist-correccion-h1.md`;
- ejemplo privado de calibración: `03-EJEMPLOS-LAURA-PRIVADOS/h1-primer-asistente/`;
- presentación: generada desde las guías docentes;
- HTML Moodle: generado desde las fuentes del alumnado;
- RA, criterios y rúbrica: documentos de coordinación del repositorio.
