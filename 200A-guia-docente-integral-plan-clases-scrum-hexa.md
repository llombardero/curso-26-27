# Guía docente integral — Plan de clases, Scrum y HEXA

## Programación orientada a objetos — Proyecto MiniJarvis — Curso 2026/2027

Documento creado a partir del análisis de los materiales existentes en esta carpeta del curso.

Materiales base revisados:

- `00-mapa-maestro-curso-2026-2027.md`
- `01-matriz-integrada-ra-ce-evidencias-tareas.md`
- `02-calendario-hitos-sprints-2026-2027.md`
- `05-politica-uso-ia-semaforo-registro-defensa.md`
- `06-rubricas-hitos.md`
- `08-guia-alumnado-proyecto-agente-ia.md`
- `21-indice-cierre-itinerario-minijarvis.md`
- Guías docentes de los hitos `H0` a `HF`

---

## 1. Diagnóstico del material existente

El curso ya está muy bien orientado como itinerario anual basado en proyecto. No parte de unidades didácticas aisladas, sino de un producto incremental: MiniJarvis, un pequeño agente educativo en Java.

La estructura actual es coherente y progresiva:

| Hito | Foco principal | Sentido didáctico |
|---|---|---|
| H0 | Scrum y torre de papel | Aprender la dinámica de trabajo antes de programar. |
| H1 | Primer asistente básico | Estructura mínima de Java, entrada/salida, variables y constantes. |
| H2 | Decisiones y depuración | Menús, bucles, condicionales, pruebas manuales y depuración. |
| H3 | Memoria en colecciones | Listas/mapas, memoria temporal y casos límite. |
| C1 | Cierre 1.ª evaluación | Consolidación, defensa, recuperación y portfolio. |
| H4 | Agente orientado a objetos | Clases, objetos, responsabilidades, encapsulación y UML. |
| H5 | Extensibilidad y clean code | Refactorización, herramientas, Git, revisión y patrones iniciales. |
| C2 | Cierre 2.ª evaluación | Defensa técnica, revisión de repositorio y recuperación. |
| H6 | Persistencia y trazabilidad | Ficheros, logs, reproducibilidad y seguridad. |
| H7 | IA responsable | Integración real o simulada, prompts, validación y límites. |
| HF | Presentación final | Demo, portfolio, recuperación, mejora y defensa individual. |

Conclusión principal:

```text
El curso no necesita más contenidos; necesita una dirección docente clara para decidir cuándo explicar, cuándo practicar, cuándo construir y cuándo defender.
```

---

## 2. Principio rector del curso

El alumnado debe aprender programación orientada a objetos construyendo software funcional, defendible y trazable.

La idea central que debe repetirse durante todo el curso es:

```text
Cada incremento de MiniJarvis debe funcionar, poder probarse, poder documentarse y poder defenderse.
```

El curso debe evitar tres errores:

- Convertir MiniJarvis en una excusa para correr demasiado.
- Introducir POO, patrones o IA antes de que el alumnado domine fundamentos.
- Evaluar solo el producto final sin comprobar proceso, comprensión y autoría.

---

## 3. Metodología integrada

El curso combina ABP, Scrum adaptado al aula, modelo HEXA, evaluación competencial, DUA, código limpio e IA responsable.

La relación entre metodologías debe quedar así:

| Elemento | Función en el curso |
|---|---|
| ABP | Da sentido al curso mediante el proyecto MiniJarvis. |
| Scrum | Organiza el trabajo de los equipos en sprints, revisiones y retrospectivas. |
| HEXA | Ordena la secuencia didáctica de cada reto. |
| POO | Se introduce cuando el proyecto necesita organizar responsabilidades. |
| Clean code | Se trabaja desde H1, con exigencia progresiva. |
| Patrones | Solo aparecen cuando solucionan un problema real. |
| IA responsable | Acompaña el aprendizaje, pero exige registro, verificación y defensa. |
| Evaluación por evidencias | Permite calificar RA/CE mediante código, documentación, pruebas, Git y defensa. |

---

## 4. Modelo HEXA aplicado a cada hito

Cada hito debe impartirse con la misma lógica didáctica.

| Fase HEXA | Qué hace el docente | Qué hace el alumnado | Producto de la fase |
|---|---|---|---|
| Fase 0. Equipos | Define roles, normas y expectativas. | Asume rol y acuerda forma de trabajo. | Equipo, contrato y tablero. |
| 1. Activar | Presenta el reto y conecta con lo anterior. | Explica qué sabe y qué necesita. | Preguntas iniciales y objetivo del hito. |
| 2. Investigar | Explica conceptos mínimos y propone mini-retos. | Practica conceptos fuera del proyecto principal. | Ejercicios cortos y ejemplos entendidos. |
| 3. Idear | Pide alternativas y decisiones justificadas. | Diseña solución antes de codificar. | Boceto, tabla de comandos, diagrama o decisión técnica. |
| 4. Planificar | Ayuda a convertir decisiones en backlog. | Crea tareas, criterios de aceptación y reparto. | Sprint backlog y tablero. |
| 5. Ejecutar | Acompaña programación, pruebas y depuración. | Construye, prueba, registra y corrige. | Incremento funcional. |
| 6. Comunicar | Organiza demo, defensa y retrospectiva. | Presenta, defiende y reflexiona. | Demo, portfolio, retro y evidencias. |

Regla práctica:

```text
No debe haber ejecución larga sin activación, investigación, planificación y criterios de aceptación.
```

---

## 5. Scrum adaptado al aula

Scrum no debe explicarse como teoría extensa. Debe vivirse desde H0 y repetirse en cada hito.

### Roles

Equipos recomendados: 3 o 4 personas.

| Rol | Responsabilidad |
|---|---|
| Facilitador/a | Cuida tiempos, turnos, bloqueos y acuerdos. |
| Responsable de backlog | Mantiene tareas, tablero y criterios de aceptación. |
| Responsable técnico/a | Coordina decisiones de código, pruebas y calidad. |
| Responsable de documentación y defensa | Mantiene portfolio, registro IA, README y demo. |

Los roles deben rotar al menos una vez por evaluación.

### Eventos mínimos

| Evento | Duración orientativa | Cuándo se hace | Resultado |
|---|---:|---|---|
| Sprint planning | 20-30 min | Inicio de cada hito o sprint corto | Sprint backlog y objetivo. |
| Daily de aula | 5-8 min | Inicio de sesiones de trabajo | Estado, bloqueo y siguiente paso. |
| Revisión docente | 10-15 min | Mitad del hito | Corrección temprana. |
| Sprint review | 20-30 min | Final del hito | Demo del incremento. |
| Retrospectiva | 15-20 min | Final del hito | Mejora concreta para el siguiente sprint. |
| Defensa individual | 5-10 min por alumno/a | Cierre del hito o muestra seleccionada | Verificación de comprensión. |

### Tablero mínimo

Columnas recomendadas:

```text
Pendiente | En curso | En revisión | Hecho | Bloqueado
```

Cada tarea debe tener:

- descripción breve;
- responsable;
- criterio de terminado;
- evidencia asociada.

Ejemplo de criterio de terminado:

```text
El comando memoria está terminado cuando guarda al menos un recuerdo, muestra memoria vacía correctamente, se ha probado con 3 casos y una persona del equipo puede explicarlo.
```

---

## 6. Ritmo semanal recomendado

Programación tiene 8 periodos semanales y Entornos 3 periodos semanales. Conviene diferenciar la función de cada módulo.

### Programación

Uso principal:

- explicación técnica;
- práctica guiada;
- construcción del código;
- pruebas de comportamiento;
- defensa de estructuras, clases y decisiones.

### Entornos de Desarrollo

Uso principal:

- IntelliJ, Git, GitHub y estructura de repositorio;
- README, documentación técnica y evidencias;
- pruebas, depuración e incidencias;
- diagramas UML;
- revisión de código;
- reproducibilidad, Docker guiado o CI si procede.

### Semana tipo

| Momento | Programación | Entornos |
|---|---|---|
| Inicio de semana | Activar, explicar concepto clave y mini-reto. | Revisar tablero, backlog y evidencias. |
| Mitad de semana | Construcción guiada del incremento. | Pruebas, depuración, Git o documentación. |
| Final de semana | Integración, revisión técnica y dudas. | README, portfolio, registro IA y defensa parcial. |

---

## 7. Plan detallado por hitos

### H0. Bootcamp Scrum y torre de papel

Fechas: 15-18 septiembre.

Objetivo docente:

```text
Que el alumnado viva Scrum antes de aplicarlo al software.
```

Conceptos clave a explicar:

| Momento | Concepto |
|---|---|
| Antes de construir | Producto, restricción, equipo, rol y backlog. |
| Durante la actividad | Sprint, tarea, bloqueo y responsabilidad. |
| Después de construir | Review, retrospectiva, mejora continua y transferencia al software. |

Secuencia de clases:

| Bloque | Qué hacer |
|---|---|
| Presentación | Explicar que el producto visible es la torre, pero el aprendizaje real es el proceso. |
| Equipos | Formar grupos de 3-4 y asignar roles. |
| Backlog | Pedir al menos 5 tareas antes de construir. |
| Sprint | Construir con tiempo limitado. |
| Review | Medir estabilidad, altura y cumplimiento de restricciones. |
| Retrospectiva | Identificar qué funcionó, qué no y qué cambiarán. |
| Transferencia | Relacionar torre con MiniJarvis: backlog, incrementos, pruebas y demo. |

Evidencias:

- foto o evidencia de torre;
- tablero inicial;
- contrato de equipo;
- retrospectiva;
- traducción a MiniJarvis.

Decisión docente importante:

```text
No calificar fuerte Programación en H0; usarlo como diagnóstico y como evidencia de Entornos.
```

---

### H1. Primer asistente básico

Fechas: 21 septiembre - 9 octubre.

Producto:

```text
MiniJarvis H1: programa Java básico que pide el nombre y muestra mensajes iniciales.
```

Cuándo explicar los elementos clave:

| Momento | Concepto | Forma de explicación |
|---|---|---|
| Inicio | Qué es un programa Java | Mostrar `Main` como punto de entrada. |
| Antes de codificar | Clase `Main` y método `main` | Dibujar dónde empieza la ejecución. |
| Primer código | `System.out.println` | Ejecutar mensajes simples. |
| Después | Variables y constantes | Diferenciar dato que cambia y dato fijo. |
| Cuando haga falta entrada | `Scanner` | Leer nombre y usarlo en una respuesta. |
| Cierre | README y ejecución | Explicar cómo reproducir el programa. |

Restricción clave:

```text
No introducir menú, bucles, listas, clases propias, ficheros ni IA real.
```

Secuencia de clases:

| Bloque | Producto parcial |
|---|---|
| Presentar H1 | Lista de lo que entra y no entra. |
| IntelliJ | Proyecto creado y primer mensaje ejecutado. |
| Variables y constantes | Mensajes que usan datos. |
| Entrada por teclado | Nombre leído con `Scanner`. |
| Limpieza | Código simple, nombres claros y sin complejidad prematura. |
| Entornos | README, estructura del proyecto y evidencia de ejecución. |
| Defensa | Explicar `main`, variable, constante, `Scanner` y ejecución. |

Intervención docente:

```text
Si un equipo trae código avanzado, pedir que lo reduzca o que demuestre comprensión. No premiar complejidad no defendible.
```

---

### H2. Decisiones, menús y depuración

Fechas: 13 octubre - 6 noviembre.

Producto:

```text
MiniJarvis H2: agente con menú, comandos, repetición hasta salir, pruebas manuales y depuración.
```

Cuándo explicar los elementos clave:

| Momento | Concepto | Forma de explicación |
|---|---|---|
| Inicio | Diferencia entre programa lineal y programa interactivo | Comparar H1 con un menú que se repite. |
| Antes de programar | Tabla de comandos | Diseñar `ayuda`, `saluda`, `estado`, `salir` y `otro`. |
| Primera implementación | Bucle `while` | Preguntar cómo evitar que el programa termine. |
| Después | `if/else` o `switch` | Elegir respuesta según comando. |
| Al aparecer errores | `.equals`, `trim`, `toLowerCase` | Resolver fallos reales de entrada. |
| Entornos | Casos de prueba | Definir esperado/obtenido. |
| Entornos | Breakpoints | Observar `command`, `running` y `userName`. |

Restricción clave:

```text
No introducir memoria en colecciones, clases complejas, patrones, ficheros ni IA real.
```

Secuencia de clases:

| Bloque | Producto parcial |
|---|---|
| Reencuadre desde H1 | Diferencia H1/H2 clara. |
| Diseño de comandos | Tabla de comandos y respuestas. |
| Bucle principal | El programa se repite. |
| Selección | Cada comando ejecuta una rama. |
| Entradas no válidas | Comando desconocido controlado. |
| Pruebas manuales | Tabla de casos. |
| Depuración | Captura o informe de breakpoint. |
| Comparación Java-Python | Menú equivalente en casa. |
| Defensa | Explicar flujo y modificar un comando. |

Errores previsibles:

| Error | Respuesta docente |
|---|---|
| Usa `==` para comparar texto | Explicar `.equals()` con ejemplo mínimo. |
| Bucle infinito | Revisar variable `running`. |
| No contempla comando desconocido | Añadir `else` o `default`. |
| IA genera código avanzado | Pedir versión mínima H2 defendible. |

---

### H3. Memoria temporal con colecciones

Fechas: 9 noviembre - 4 diciembre.

Producto:

```text
MiniJarvis H3: agente que recuerda información durante la ejecución usando colecciones Java.
```

Cuándo explicar los elementos clave:

| Momento | Concepto | Forma de explicación |
|---|---|---|
| Inicio | Memoria temporal | Mostrar que H2 olvida todo al cerrar. |
| Antes de elegir colección | Qué se quiere guardar | Decidir recuerdos, preferencias o historial. |
| Investigación | `ArrayList` y `HashMap` | Comparar orden, clave y búsqueda. |
| Ejecución | Añadir comando `recuerda` | Guardar una entrada. |
| Ejecución | Añadir comando `memoria` | Recorrer y mostrar datos. |
| Calidad | Casos límite | Memoria vacía, entrada vacía y repetidos. |
| Entornos | Pruebas de memoria | Casos esperado/obtenido. |

Restricción clave:

```text
No introducir persistencia, base de datos, diseño OO fuerte, interfaces, patrones ni API externa.
```

Secuencia de clases:

| Bloque | Producto parcial |
|---|---|
| Revisar H2 | Menú funcional como base. |
| Definir memoria | Qué recordará MiniJarvis. |
| Colección inicial | `ArrayList` o `HashMap` justificado. |
| Comando `recuerda` | Guarda información. |
| Comando `memoria` | Lista o consulta información. |
| Comando `estado` | Muestra número de recuerdos. |
| Casos límite | Memoria vacía y entradas no válidas. |
| Comparación Java-Python | `ArrayList`/`HashMap` frente a `list`/`dict`. |
| Cierre C1 | Demo parcial, portfolio y recuperación. |

Momento clave del curso:

```text
Al terminar H3 el alumnado debe dominar programa lineal, control de flujo y colecciones antes de entrar en POO fuerte.
```

---

### C1. Cierre de la primera evaluación

Fechas: 9-22 diciembre.

Objetivo:

```text
Consolidar H1-H3 y detectar RA pendientes antes de iniciar POO en enero.
```

Actividades recomendadas:

| Actividad | Finalidad |
|---|---|
| Demo parcial | Ver MiniJarvis H3 funcionando. |
| Revisión de repositorio | Comprobar estructura, README y evidencias. |
| Defensa individual corta | Validar autoría y comprensión. |
| Portfolio | Recoger aprendizaje y problemas. |
| Recuperación específica | Cubrir RA no demostrados. |

Preguntas de defensa:

- ¿Dónde empieza el programa?
- ¿Qué variable controla el bucle?
- ¿Cómo se decide qué comando ejecutar?
- ¿Qué colección usas y por qué?
- ¿Cómo pruebas que la memoria funciona?
- ¿Qué parte hizo la IA y cómo la verificaste?

---

### H4. Agente orientado a objetos

Fechas: 7 enero - 5 febrero.

Producto:

```text
MiniJarvis H4: agente con clases propias, responsabilidades claras, diagramas y defensa de diseño.
```

Este es el hito central de programación orientada a objetos.

Cuándo explicar los elementos clave:

| Momento | Concepto | Forma de explicación |
|---|---|---|
| Inicio | Por qué todo en `Main` ya no escala | Mostrar síntomas: código largo, mezcla de responsabilidades. |
| Activar | Clase y objeto | Comparar plantilla y ejemplar. |
| Investigación | Atributos y métodos | Preguntar qué sabe y qué hace cada clase. |
| Investigación | Constructor | Crear objetos en estado inicial válido. |
| Investigación | Encapsulación | Usar `private` y métodos públicos con intención. |
| Idear | Responsabilidad única | Separar `Agent`, `Memory` y `Main`. |
| Entornos | Diagrama de clases | Dibujar clases antes o durante el rediseño. |
| Entornos | Diagrama de comportamiento | Explicar flujo real de un comando. |

Restricción clave:

```text
No forzar patrones, arquitectura hexagonal, sistema de plugins, persistencia ni IA real.
```

Diseño mínimo recomendado:

| Clase | Responsabilidad |
|---|---|
| `Main` | Arrancar el programa y delegar. |
| `Agent` | Gestionar interacción, menú y flujo principal. |
| `Memory` | Guardar y consultar recuerdos temporales. |
| `Message` | Opcional para representar un recuerdo o mensaje. |

Secuencia de clases:

| Bloque | Producto parcial |
|---|---|
| Diagnóstico de H3 | Detectar problemas de código concentrado. |
| Introducción POO | Clase, objeto, atributo, método y constructor. |
| Extraer `Memory` | Encapsular colección y operaciones. |
| Extraer `Agent` | Mover flujo principal fuera de `Main`. |
| Encapsulación | Revisar `private`, getters o métodos de intención. |
| UML | Diagrama de clases coherente con código. |
| Comportamiento | Diagrama de un comando real. |
| Defensa | Explicar una clase, una relación y un flujo. |

Intervención docente:

```text
Preguntar constantemente: qué sabe esta clase, qué hace esta clase, qué no debería hacer esta clase.
```

---

### H5. Agente extensible, clean code y patrones iniciales

Fechas: 8 febrero - 19 marzo.

Producto:

```text
MiniJarvis H5: agente con herramientas internas extensibles, refactorización documentada, revisión de código y decisión razonada sobre patrón.
```

Cuándo explicar los elementos clave:

| Momento | Concepto | Forma de explicación |
|---|---|---|
| Inicio | Extensibilidad | Preguntar qué hay que tocar para añadir un comando. |
| Antes de refactorizar | Código limpio | Nombres, duplicación, tamaño, responsabilidades. |
| Ejecución | Interfaz simple `Tool` | Introducir contrato común si el grupo está preparado. |
| Ejecución | Composición frente a herencia | Priorizar delegar en herramientas. |
| Después | Refactorización | Mostrar antes/después y motivo. |
| Cuando haya necesidad | Patrón Command simplificado | Nombrarlo solo si resuelve el problema real. |
| Entornos | Git profesional | Ramas, commits, PR o revisión documentada. |

Restricción clave:

```text
No forzar arquitectura hexagonal, frameworks, persistencia, IA real ni patrones múltiples.
```

Diseño posible:

| Elemento | Responsabilidad |
|---|---|
| `Tool` | Contrato común para herramientas. |
| `HelpTool` | Mostrar ayuda. |
| `RememberTool` | Guardar recuerdos. |
| `MemoryTool` | Mostrar memoria. |
| `StatusTool` | Mostrar estado. |
| `Agent` | Orquestar herramientas. |
| `Memory` | Gestionar recuerdos. |

Secuencia de clases:

| Bloque | Producto parcial |
|---|---|
| Revisar H4 | Detectar puntos rígidos del diseño. |
| Definir nueva herramienta | Caso real para añadir funcionalidad. |
| Refactorizar comando | Separar una responsabilidad. |
| Generalizar herramientas | Crear contrato común si procede. |
| Revisión de código | Detectar duplicación y nombres pobres. |
| Git | Evidencia de rama, commit, PR o revisión. |
| Patrón o no patrón | Justificar uso o descarte. |
| Defensa | Explicar refactor y añadir herramienta con bajo impacto. |

Regla docente:

```text
Un patrón solo se acepta si el alumnado puede explicar qué problema tenía antes y qué mejora después.
```

---

### C2. Cierre de la segunda evaluación

Fechas: 29-31 marzo.

Objetivo:

```text
Consolidar POO, diseño, extensibilidad, Git, revisión y evidencias antes de persistencia.
```

Actividades recomendadas:

| Actividad | Finalidad |
|---|---|
| Demo H5 | Ver agente extensible funcionando. |
| Defensa de diseño | Validar clases, responsabilidades y decisiones. |
| Revisión Git | Comprobar commits, trazabilidad y revisión. |
| Informe de refactorización | Ver mejora real antes/después. |
| Recuperación | Cubrir RA4 y RA de Entornos pendientes. |

Preguntas de defensa:

- ¿Qué responsabilidad tiene `Agent`?
- ¿Qué responsabilidad tiene `Memory`?
- ¿Qué cambia si añades una herramienta nueva?
- ¿Qué refactorización hiciste y por qué?
- ¿Has usado un patrón? ¿Qué problema resuelve?
- ¿Qué commit demuestra tu aportación?

---

### H6. Persistencia y trazabilidad

Fechas: 1-23 abril.

Producto:

```text
MiniJarvis H6: agente con memoria persistente en ficheros, historial/logs simples, ejecución reproducible y seguridad documentada.
```

Cuándo explicar los elementos clave:

| Momento | Concepto | Forma de explicación |
|---|---|---|
| Inicio | Memoria temporal frente a persistente | Cerrar y abrir el programa para mostrar pérdida de datos. |
| Investigación | Ficheros | Leer y escribir `data/recuerdos.txt`. |
| Ejecución | Rutas y carpetas | Crear `data/` y `logs/`. |
| Ejecución | Errores de E/S | Gestionar fichero inexistente o permisos. |
| Calidad | Prueba de segunda ejecución | Guardar, cerrar, abrir y consultar. |
| Entornos | README reproducible | Ejecutar desde cero siguiendo instrucciones. |
| Seguridad | Secretos y datos personales | Prohibir `.env` real, tokens y datos reales. |

Restricción clave:

```text
No subir credenciales, datos personales, tokens ni `.env` real. No hacer obligatoria IA real ni base de datos compleja.
```

Diseño posible:

| Clase | Responsabilidad |
|---|---|
| `PersistentMemory` | Cargar y guardar recuerdos. |
| `HistoryLog` | Registrar eventos simples. |
| `Agent` | Orquestar herramientas. |
| `Tool` | Contrato para herramientas. |

Secuencia de clases:

| Bloque | Producto parcial |
|---|---|
| Revisar H5 | Agente extensible como base. |
| Definir formato | `data/recuerdos.txt` o similar. |
| Guardar | Escribir recuerdos. |
| Cargar | Recuperar al iniciar. |
| Log | Registrar eventos simples. |
| Pruebas | Guardar, cerrar, abrir y consultar. |
| Seguridad | Revisar datos y secretos. |
| README | Ejecución reproducible. |
| Defensa | Explicar persistencia, errores y seguridad. |

---

### H7. IA responsable real o simulada

Fechas: 26-29 abril.

Producto:

```text
MiniJarvis H7: modo IA responsable, limitado, validado, seguro y defendible.
```

Decisión docente previa:

```text
Si el grupo no llega preparado o no se quieren gestionar claves, usar simulación robusta. Es completamente válida.
```

Cuándo explicar los elementos clave:

| Momento | Concepto | Forma de explicación |
|---|---|---|
| Inicio | Qué hará y qué no hará la IA | Definir caso de uso limitado. |
| Antes de integrar | Seguridad de prompts | No enviar datos personales ni secretos. |
| Ejecución | Simulador o API | Priorizar robustez sobre espectacularidad. |
| Calidad | Validación humana | Revisar respuestas y límites. |
| Entornos | Configuración segura | `.env.example`, nunca `.env` real. |
| Cierre | Registro de prompts | Documentar uso, riesgos y verificación. |

Caso de uso recomendado:

```text
MiniJarvis ofrece una sugerencia breve de estudio o una explicación conceptual sin usar datos personales.
```

Diseño posible:

| Clase | Responsabilidad |
|---|---|
| `AiAssistant` | Contrato o clase que responde de forma controlada. |
| `SimulatedAiAssistant` | Simulación local sin claves. |
| `AiTool` | Herramienta que consulta la IA o simulación. |
| `PromptSafety` | Reglas básicas de seguridad. |

---

### HF. Presentación final, recuperación y mejora

Fechas: 31 mayo - 22 junio.

Objetivo:

```text
Cerrar el aprendizaje con demo, defensa individual, portfolio final y recuperación de RA pendientes.
```

Actividades recomendadas:

| Actividad | Finalidad |
|---|---|
| Demo final | Mostrar evolución H1-H7. |
| Portfolio final | Ordenar evidencias y reflexión. |
| Defensa individual | Verificar comprensión real. |
| Revisión de repositorio | Comprobar trazabilidad. |
| Recuperación específica | Cubrir RA/CE no demostrados. |
| Mejora opcional | Permitir profundización sin sustituir mínimos. |

Regla de cierre:

```text
Sin comprensión defendible, no hay evidencia completa de aprendizaje.
```

---

## 8. Cuándo explicar POO durante el curso

La POO no debe empezar como teoría abstracta en septiembre. Debe prepararse desde el principio y formalizarse en H4.

| Momento | Qué se trabaja | Nivel de profundidad |
|---|---|---|
| H1 | Uso de una clase `Main` y librerías como `Scanner` | Muy básico, sin clases propias. |
| H2 | Organización del flujo y comandos | Sin POO formal. |
| H3 | Datos y comportamiento alrededor de memoria | Preparación conceptual. |
| C1 | Diagnóstico de código difícil de mantener | Motivar necesidad de POO. |
| H4 | Clases, objetos, atributos, métodos, constructores, encapsulación | Núcleo fuerte. |
| H5 | Interfaces, composición, refactorización y patrón simple | POO aplicada. |
| H6 | Clases de persistencia y logs | POO para separar infraestructura. |
| H7 | Clase de IA/simulación como herramienta | Integración controlada. |

Secuencia conceptual recomendada:

```text
Problema de código largo → responsabilidad → clase → objeto → atributo → método → constructor → encapsulación → relación entre clases → composición → interfaz → patrón si procede.
```

---

## 9. Política de IA en la práctica docente

El semáforo de IA debe usarse desde la primera semana.

| Color | Uso | Condición |
|---|---|---|
| Verde | Explicar, repasar, entender errores, generar preguntas | Registrar si afecta a entrega evaluable. |
| Amarillo | Generar fragmentos, refactorizar, traducir a Python, proponer tests o diagramas | Registro, verificación y defensa. |
| Rojo | Entregar solución completa no entendida, ocultar uso, usar secretos, datos personales o `.env` real | Evidencia condicionada o invalidada. |

Preguntas obligatorias si hay IA:

- ¿Qué pediste a la IA?
- ¿Qué aceptaste?
- ¿Qué modificaste tú?
- ¿Cómo lo verificaste?
- ¿Qué errores o riesgos detectaste?
- ¿Puedes modificar ahora esa parte?

---

## 10. Evaluación y evidencias

Cada hito debe producir evidencias técnicas, de proceso y de comprensión.

| Evidencia | Tipo | Uso docente |
|---|---|---|
| Código funcional | Equipo o individual | Producto técnico. |
| Commits o trazabilidad | Individual/equipo | Autoría y proceso. |
| README | Equipo | Reproducibilidad. |
| Pruebas/checklist | Equipo | Verificación. |
| Informe de depuración | Individual/equipo | Comprensión de errores. |
| Diagramas | Equipo | Diseño y comunicación técnica. |
| Portfolio | Individual | Reflexión y aprendizaje. |
| Registro IA | Individual/equipo | Ética y trazabilidad. |
| Demo | Equipo | Comunicación del incremento. |
| Defensa oral | Individual | Comprensión real. |

Regla de evaluación:

```text
La evidencia grupal solo es plenamente válida para cada alumno/a si puede defender su parte y explicar decisiones clave.
```

---

## 11. Defensa individual

La defensa debe ser breve, frecuente y técnica. No debe reservarse solo para final de curso.

Formato recomendado:

| Momento | Duración | Qué preguntar |
|---|---:|---|
| H1-H2 | 3-5 min | Conceptos básicos y flujo. |
| H3 | 5 min | Colección, memoria y pruebas. |
| H4-H5 | 5-8 min | Clases, responsabilidades, refactorización y Git. |
| H6-H7 | 5-8 min | Persistencia, seguridad, IA y reproducibilidad. |
| HF | 8-10 min | Evolución completa y aportación individual. |

Tipos de preguntas:

- Explica este fragmento.
- Cambia este mensaje o comando.
- ¿Qué pasa si la entrada está vacía?
- ¿Por qué elegiste esta colección?
- ¿Qué responsabilidad tiene esta clase?
- ¿Qué prueba demuestra que funciona?
- ¿Qué harías si falla al cargar el fichero?
- ¿Qué parte hizo la IA y cómo la verificaste?

---

## 12. Uso de los ejemplos de Laura

Los ejemplos de `99-ejemplos-alumna/` son muy valiosos, pero deben usarse con cuidado.

Uso recomendado:

- mostrar nivel esperado de documentación;
- calibrar calidad de entregables;
- comparar entrega incompleta con entrega modelo;
- preparar defensas;
- enseñar cómo justificar decisiones.

Uso no recomendado:

- mostrarlos antes de que el alumnado haya intentado resolver;
- permitir copia directa;
- sustituir la explicación docente;
- convertirlos en solución oficial.

Momento ideal:

```text
Mostrar el ejemplo después de una primera iteración del alumnado, nunca antes del primer intento serio.
```

---

## 13. Atención a la diversidad y DUA

El proyecto permite varios niveles de logro sin cambiar el objetivo común.

| Perfil | Adaptación |
|---|---|
| Alumnado con dificultad inicial | Producto mínimo claro, plantilla guiada y defensa de fragmentos pequeños. |
| Alumnado medio | Incremento completo, pruebas, documentación y defensa estándar. |
| Alumnado avanzado | Mejora opcional, pruebas automatizadas, CI/Docker o integración IA real. |
| Alumnado con baja participación grupal | Evidencias individuales y defensa reforzada. |
| Alumnado con alta dependencia de IA | Registro detallado, modificación en directo y preguntas de comprensión. |

Principio DUA:

```text
Mismo reto, varias formas de acceder, practicar, expresar y demostrar aprendizaje.
```

---

## 14. Riesgos del curso y cómo evitarlos

| Riesgo | Señal | Medida preventiva |
|---|---|---|
| Ir demasiado rápido | Código avanzado no defendible | Respetar restricciones de cada hito. |
| POO prematura | Muchas clases decorativas | Esperar a H4 y partir de problemas reales. |
| Scrum superficial | Tablero actualizado al final | Revisar tablero semanalmente. |
| IA como autor oculto | Alumno no explica su código | Registro, defensa y modificación en directo. |
| Entregas sin pruebas | Funciona solo en la demo | Exigir checklist desde H2. |
| Repositorio caótico | Archivos sin estructura | Plantilla mínima por hito. |
| Desigualdad en equipos | Una persona hace todo | Roles rotativos, commits y defensa individual. |
| Integración IA frágil | El proyecto deja de funcionar por API | Aceptar simulación robusta. |

---

## 15. Guion mínimo para cada clase

Para que el curso sea sostenible, cada sesión debe seguir una estructura repetible.

| Tiempo | Acción docente | Resultado |
|---:|---|---|
| 5 min | Recordar objetivo del hito y estado del tablero. | Dirección clara. |
| 10-20 min | Explicar un concepto o resolver un problema común. | Base técnica. |
| 15-25 min | Mini-reto guiado. | Práctica controlada. |
| 30-60 min | Trabajo de equipo o individual. | Incremento real. |
| 5-10 min | Cierre, commit, evidencia o ticket de salida. | Trazabilidad. |

Ticket de salida recomendado:

```text
1. Qué he avanzado hoy.
2. Qué problema tengo.
3. Qué evidencia he generado.
4. Qué necesito para la próxima sesión.
```

---

## 16. Decisiones finales recomendadas

1. Mantener la secuencia H0-HF tal como está diseñada.
2. No adelantar POO fuerte hasta H4.
3. No adelantar patrones hasta H5 y solo si hay necesidad real.
4. No hacer obligatoria la IA real; la simulación robusta es válida.
5. Usar Scrum de forma ligera pero constante.
6. Usar HEXA como estructura docente de cada hito.
7. Evaluar siempre producto, proceso, documentación, pruebas y defensa.
8. Reservar Entornos para profesionalizar el proceso: Git, pruebas, depuración, UML, README, reproducibilidad y seguridad.
9. Usar los ejemplos de Laura como calibración, no como solución previa.
10. Cerrar cada evaluación con recuperación específica por evidencias, no con tareas genéricas.

---

## 17. Resumen operativo del curso

```text
Septiembre: crear cultura de trabajo, Scrum y fundamentos mínimos.
Octubre: controlar flujo, menús, decisiones y depuración.
Noviembre: introducir memoria temporal y colecciones.
Diciembre: cerrar fundamentos y recuperar antes de POO.
Enero: introducir POO fuerte desde una necesidad real.
Febrero-marzo: mejorar diseño, extensibilidad, Git, refactorización y patrones simples.
Abril: persistencia, logs, seguridad e IA responsable o simulada.
Mayo-junio: defensa final, portfolio, recuperación y mejora.
```

Mensaje final para el docente:

```text
El éxito del curso no será que todos construyan el agente más complejo, sino que cada alumno pueda explicar, probar, mejorar y defender el software que ha construido.
```
