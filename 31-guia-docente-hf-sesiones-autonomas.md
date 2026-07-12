# Guía docente completa — HF sesión a sesión

## Presentación final, recuperación y mejora — MiniJarvis HF

## Programación + Entornos de Desarrollo — 1.º DAW — Curso 2026/2027

Versión: borrador 0.1

Documento autónomo para uso del profesorado.

Este documento permite impartir HF completo sin abrir ningún otro material durante la clase.

---

## 1. Propósito de HF

HF no es un hito técnico nuevo. Es el cierre docente del proyecto anual MiniJarvis.

Producto final:

```text
Cierre MiniJarvis HF: portfolio final, demo final, defensa individual, recuperación específica si procede, registro IA final, autoevaluación y plan de mejora.
```

HF sirve para:

```text
- ordenar evidencias H0-H7;
- distinguir evidencias de Programación y Entornos de Desarrollo;
- preparar una demo final realista;
- defender individualmente comprensión y aportación;
- recuperar RA/CE pendientes con evidencias focalizadas;
- cerrar el uso de IA con reflexión crítica;
- hacer autoevaluación honesta;
- proponer mejoras futuras sin inventar trabajo no hecho.
```

Idea docente central:

```text
Sin comprensión defendible, no hay evidencia completa de aprendizaje.
```

Esta regla debe repetirse durante HF. Un portfolio bonito, un repositorio grande o una demo grupal no sustituyen la defensa individual.

---

## 2. Restricciones de HF

En HF sí entra:

```text
[x] Portfolio final individual.
[x] Demo final de equipo o individual según organización del aula.
[x] Defensa individual.
[x] Recuperación específica si hay RA/CE pendientes.
[x] Registro IA final.
[x] Autoevaluación final.
[x] Plan de mejora si procede.
[x] Evidencias de Programación.
[x] Evidencias de Entornos de Desarrollo.
[x] Seguridad: sin secretos ni datos personales reales.
[x] Reflexión sobre errores, decisiones y aprendizaje.
```

En HF NO entra:

```text
[ ] Añadir un nuevo hito técnico.
[ ] Reescribir todo MiniJarvis desde cero.
[ ] Inventar evidencias que no existen.
[ ] Copiar ejemplos de Laura o de otros grupos.
[ ] Sustituir defensa por lectura de un texto generado por IA.
[ ] Subir API keys, `.env` real, tokens o datos personales.
[ ] Convertir recuperación en castigo genérico sin relación con RA/CE.
```

Frase docente:

```text
HF no premia haber llegado más lejos técnicamente, sino cerrar con evidencias claras, comprensión defendible y mejora honesta.
```

---

## 3. Entregables mínimos HF

Estructura esperada de cierre:

```text
hf-presentacion-final-recuperacion-mejora/
├── portfolio-final.md
├── demo-final.md
├── defensa-final.md
├── recuperacion-especifica.md       # solo si procede
├── registro-ia-final.md
├── autoevaluacion-final.md
└── plan-mejora-final.md             # si procede
```

Descripción de entregables:

| Entregable | Finalidad | Quién lo defiende |
|---|---|---|
| `portfolio-final.md` | Mostrar evolución H0-H7 con evidencias. | Individual. |
| `demo-final.md` | Preparar secuencia de demostración. | Equipo o individual. |
| `defensa-final.md` | Preparar explicación oral individual. | Individual. |
| `recuperacion-especifica.md` | Recuperar RA/CE pendientes. | Individual si procede. |
| `registro-ia-final.md` | Sintetizar uso de IA durante el curso. | Individual. |
| `autoevaluacion-final.md` | Reflexionar sobre aprendizaje y aportación. | Individual. |
| `plan-mejora-final.md` | Proponer mejoras realistas. | Individual si procede. |

Plantilla de portfolio final incluida en esta guía:

```markdown
# Portfolio final — MiniJarvis

## Datos

Nombre:
Equipo:

## Resumen del proyecto

## Evidencias por hito

| Hito | Evidencia | Qué demuestra | ¿Programación, Entornos o ambos? |
|---|---|---|---|
| H0 | | | |
| H1 | | | |
| H2 | | | |
| H3 | | | |
| H4 | | | |
| H5 | | | |
| H6 | | | |
| H7 | | | |

## Evidencias de Programación

## Evidencias de Entornos de Desarrollo

## Errores importantes y cómo los resolví

## Uso de IA durante el curso

## Qué puedo defender individualmente

## Qué necesito mejorar
```

Plantilla de demo final:

```markdown
# Demo final — MiniJarvis

## Objetivo de la demo

## Versión que se va a enseñar

## Secuencia de comandos

```text
ayuda
estado
recuerda
Preparar defensa final
memoria
ia
Explícame ArrayList para estudiar
salir
```

## Qué se demuestra en cada paso

## Riesgos de la demo

## Plan B si falla la ejecución

## Evidencias alternativas
```

Plantilla de defensa individual:

```markdown
# Defensa final — MiniJarvis

## Qué parte puedo explicar mejor

## Qué código o documento puedo enseñar

## Qué error resolví

## Qué decisión técnica tomé

## Qué evidencia demuestra Programación

## Qué evidencia demuestra Entornos

## Qué uso de IA puedo justificar

## Qué mejoraría con más tiempo
```

---

## 4. Secuencia de sesiones HF

Preparación docente antes de iniciar HF:

```text
1. Recordar que HF no añade un hito técnico nuevo.
2. Preparar una lista visible de entregables finales.
3. Decidir calendario de defensas y demos.
4. Tener claro qué alumnado necesita recuperación específica.
5. Preparar criterios de cierre: completo, válido con mejoras menores, recuperación, no cerrado.
6. Reforzar seguridad: no enseñar secretos, tokens, datos personales ni `.env` real.
7. Repetir la regla: sin comprensión defendible, no hay evidencia completa.
```

Material mínimo de aula:

```text
- ordenador con proyecto MiniJarvis;
- terminal para demo si procede;
- portfolio o repositorio del alumnado;
- plantilla de portfolio final;
- plantilla de defensa;
- checklist docente;
- registro IA final;
- tabla de recuperación específica.
```

Propuesta de 7 sesiones de 45 minutos.

| Sesión | Foco | Producto parcial |
|---|---|---|
| HF-S1 | Presentar cierre HF y mapa de evidencias | Índice H0-H7 personal. |
| HF-S2 | Portfolio final: Programación y Entornos | Portfolio final estructurado. |
| HF-S3 | Demo final y plan B | Demo ensayada y documentada. |
| HF-S4 | Defensa individual | Guion de defensa y preguntas. |
| HF-S5 | Recuperación específica | Evidencia focalizada por RA/CE pendiente. |
| HF-S6 | Registro IA final, autoevaluación y mejora | Reflexión final completa. |
| HF-S7 | Cierre, decisiones docentes y transición | HF cerrado o plan de recuperación claro. |

---

# HF-S1 — Presentar cierre HF y mapa de evidencias

## Duración

```text
45 minutos
```

## Objetivo

Que el alumnado entienda que HF sirve para cerrar, ordenar y defender el proyecto, no para añadir otro hito técnico.

## Resultado esperado

Cada alumno/a sale con un mapa inicial de evidencias H0-H7:

```text
H0: evidencia de trabajo ágil.
H1: primer asistente.
H2: decisiones y depuración.
H3: memoria temporal.
H4: orientación a objetos.
H5: extensibilidad y clean code.
H6: persistencia y trazabilidad.
H7: IA responsable o simulación robusta.
```

## Guion docente

```text
Hemos llegado al cierre del proyecto MiniJarvis.

HF no es H8. No vamos a pedir una función nueva. Vamos a ordenar lo construido, preparar una demo defendible, recuperar lo pendiente y demostrar qué entiende cada persona.

La regla central del cierre es esta: sin comprensión defendible, no hay evidencia completa de aprendizaje.
```

## Pizarra

```text
HF = cerrar + defender + recuperar + mejorar

No es:
- añadir otro hito;
- maquillar el proyecto;
- copiar ejemplos;
- ocultar fallos.

Sí es:
- elegir evidencias;
- explicar decisiones;
- demostrar aprendizaje;
- planificar mejora.
```

## Qué explicas tú

```text
- Qué entregables forman HF.
- Por qué el portfolio debe distinguir Programación y Entornos.
- Por qué una demo puede fallar y aun así haber evidencia si hay plan B.
- Por qué la defensa individual puede matizar la nota de una evidencia grupal.
```

## Actividad HEXA guiada

### H — Hecho

El alumnado tiene muchos documentos y versiones de MiniJarvis.

### E — Explorar

Pregunta:

```text
¿Qué evidencias elegirías para demostrar que realmente has aprendido y no solo entregado archivos?
```

Respuestas esperadas:

```text
- código que puedo explicar;
- prueba que puedo repetir;
- documento que conecta decisión y evidencia;
- error que resolví;
- defensa oral de una parte concreta;
- registro IA honesto.
```

### X — eXplicar

Conclusión:

```text
Una evidencia final debe ser localizable, comprensible y defendible.
```

### A — Aplicar

Crear mapa personal de evidencias.

## Actividad

Tabla inicial:

| Hito | Evidencia que tengo | Qué demuestra | ¿Puedo defenderla? |
|---|---|---|---|
| H0 | | | |
| H1 | | | |
| H2 | | | |
| H3 | | | |
| H4 | | | |
| H5 | | | |
| H6 | | | |
| H7 | | | |

Consigna:

```text
No vale poner “todo el proyecto”. Hay que elegir evidencias concretas.
```

## Errores frecuentes

| Error | Señal | Intervención docente |
|---|---|---|
| Querer añadir funciones nuevas | “Voy a rehacer H7” | Reencuadrar: cerrar antes que ampliar. |
| Evidencias vagas | “Mi repositorio” | Pedir archivo, clase, prueba o documento concreto. |
| Ocultar hitos débiles | Dejan huecos sin explicar | Convertir en recuperación o mejora. |
| Copiar el portfolio de otro | Estructura idéntica sin voz propia | Preguntar aportación individual. |

## Cierre

Ticket:

```text
1. ¿Por qué HF no es un hito técnico nuevo?
2. Escribe una evidencia concreta que puedes defender.
3. Escribe un hito donde necesitas revisar o recuperar algo.
```

## Criterio de éxito

```text
El alumnado comprende el propósito de HF y empieza a ordenar evidencias concretas y defendibles.
```

---

# HF-S2 — Portfolio final: Programación y Entornos

## Duración

```text
45 minutos
```

## Objetivo

Construir el portfolio final diferenciando evidencias de Programación y Entornos de Desarrollo.

## Resultado esperado

Borrador sólido de `portfolio-final.md` con evidencias H0-H7 y separación por módulos.

## Guion docente

```text
El portfolio final no es una carpeta con enlaces. Es una narración técnica de aprendizaje.

Debe responder a tres preguntas: qué construí, qué evidencia lo demuestra y qué puedo explicar yo.

Además, como este proyecto une Programación y Entornos, debemos nombrar ambos módulos de forma visible.
```

## Pizarra

```text
Programación:
- código;
- estructuras;
- clases;
- ficheros;
- pruebas de ejecución.

Entornos:
- README;
- Git o registro;
- diagramas;
- pruebas;
- incidencias;
- seguridad;
- revisión;
- defensa.
```

## Qué explicas tú

```text
- Que una misma evidencia puede servir para ambos módulos, pero debe explicarse.
- Que el portfolio debe tener voz individual.
- Que las evidencias deben estar ordenadas temporalmente.
- Que no hay que esconder errores: los errores resueltos son aprendizaje defendible.
```

## Actividad HEXA guiada

### H — Hecho

Un alumno escribe: “H6 demuestra persistencia”.

### E — Explorar

Pregunta:

```text
¿Qué tendría que añadir para que sea una evidencia completa?
```

### X — eXplicar

Respuesta esperada:

```text
Ruta del fichero, prueba en dos ejecuciones, explicación de seguridad y qué puede defender.
```

### A — Aplicar

Completar secciones del portfolio.

## Actividad

Completar este bloque:

```markdown
## Evidencias de Programación

| Evidencia | Hito | Qué demuestra | Qué puedo explicar |
|---|---|---|---|
| | | | |

## Evidencias de Entornos de Desarrollo

| Evidencia | Hito | Qué demuestra | Qué puedo explicar |
|---|---|---|---|
| | | | |
```

Preguntas de apoyo:

```text
¿Qué clase Java puedes explicar?
¿Qué prueba puedes repetir?
¿Qué diagrama coincide con código?
¿Qué README permite reproducir?
¿Qué incidencia resolviste?
¿Qué decisión de seguridad tomaste?
```

## Errores frecuentes

| Error | Señal | Intervención docente |
|---|---|---|
| Portfolio como índice sin reflexión | Solo enlaces | Añadir qué demuestra y defensa. |
| Entornos invisible | Solo habla de código | Pedir README, pruebas, diagramas, seguridad. |
| Programación invisible | Solo reflexiones | Pedir clase, método, ejecución o fichero. |
| Frases genéricas | “He aprendido mucho” | Pedir ejemplo concreto. |

## Cierre

Ticket:

```text
1. Escribe una evidencia clara de Programación.
2. Escribe una evidencia clara de Entornos.
3. ¿Qué evidencia te cuesta defender todavía?
```

## Criterio de éxito

```text
El portfolio final empieza a mostrar evidencias concretas, separa ambos módulos y refleja comprensión individual.
```

---

# HF-S3 — Demo final y plan B

## Duración

```text
45 minutos
```

## Objetivo

Preparar una demo final breve, realista y con plan B por si falla la ejecución en directo.

## Resultado esperado

Documento `demo-final.md` con secuencia de comandos, explicación de evidencias, riesgos y alternativa si la demo falla.

## Guion docente

```text
Una demo final no es improvisar delante de la clase.

Una buena demo tiene objetivo, orden, comandos preparados, explicación técnica y plan B.

Si la ejecución falla, no se acaba la defensa: se usan capturas, logs, pruebas documentadas o explicación del fallo.
```

## Pizarra

```text
Demo final:
1. Qué voy a enseñar.
2. Qué comandos ejecutaré.
3. Qué demuestra cada paso.
4. Qué puede fallar.
5. Qué evidencia alternativa tengo.
```

## Qué explicas tú

```text
- Que la demo debe ser corta y defendible.
- Que conviene usar datos ficticios.
- Que no se deben mostrar secretos, rutas sensibles ni datos personales.
- Que el plan B demuestra profesionalidad, no fracaso.
```

## Actividad HEXA guiada

### H — Hecho

En una demo, el programa puede fallar por nervios, ruta incorrecta o fichero ausente.

### E — Explorar

Pregunta:

```text
¿Qué evidencias alternativas permiten demostrar aprendizaje si falla la ejecución?
```

Respuestas esperadas:

```text
- README reproducible;
- pruebas documentadas;
- capturas o logs;
- código que se puede explicar;
- incidencia registrada;
- plan de recuperación.
```

### X — eXplicar

Conclusión:

```text
La demo ideal ejecuta; la demo responsable también sabe qué hacer si falla.
```

### A — Aplicar

Redactar demo final.

## Actividad

Plantilla de secuencia:

```text
1. Mostrar README o estructura.
2. Compilar si procede.
3. Ejecutar MiniJarvis.
4. Mostrar ayuda.
5. Guardar recuerdo ficticio.
6. Mostrar memoria.
7. Mostrar persistencia/logs si procede.
8. Probar IA segura o simulada si procede.
9. Cerrar.
```

Tabla:

| Paso | Comando/acción | Qué demuestra | Riesgo | Plan B |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |

## Errores frecuentes

| Error | Señal | Intervención docente |
|---|---|---|
| Demo demasiado larga | Quieren enseñar todo | Limitar a 5-8 minutos. |
| Sin plan B | “Si falla, no sé” | Exigir evidencias alternativas. |
| Datos reales en demo | Recuerdos personales | Sustituir por datos ficticios. |
| No explicar lo que ocurre | Solo ejecutan comandos | Asociar cada paso a aprendizaje. |

## Cierre

Ticket:

```text
1. ¿Cuál será el primer comando o acción de tu demo?
2. ¿Qué riesgo puede fallar?
3. ¿Qué plan B tienes?
```

## Criterio de éxito

```text
El alumnado prepara una demo final breve, segura y defendible, con evidencia alternativa si falla la ejecución.
```

---

# HF-S4 — Defensa individual

## Duración

```text
45 minutos
```

## Objetivo

Preparar y ensayar la defensa individual para demostrar comprensión técnica, aportación propia y uso responsable de IA.

## Resultado esperado

Documento `defensa-final.md` con respuestas preparadas y una lista de evidencias que la persona puede explicar sin ayuda.

## Guion docente

```text
La defensa individual no es memorizar un discurso.

Es demostrar que puedes explicar tu proyecto, tus decisiones, tus errores y tus evidencias.

Puedes llevar un guion, pero debes hablar con tu código y documentos delante.
```

## Pizarra

```text
Defensa individual:
- qué hice yo;
- qué entiendo;
- qué evidencia lo demuestra;
- qué error resolví;
- qué IA usé y cómo la validé;
- qué mejoraría.
```

## Qué explicas tú

```text
- Que la defensa puede confirmar o matizar evidencias grupales.
- Que no se evalúa hablar perfecto, sino comprender y justificar.
- Que una respuesta honesta parcial es mejor que una explicación inventada.
- Que si se usó IA, debe declararse y validarse.
```

## Actividad HEXA guiada

### H — Hecho

Una alumna dice: “Esta parte la hizo mi equipo, pero yo no sé explicarla”.

### E — Explorar

Pregunta:

```text
¿Qué puede defender entonces de forma honesta?
```

Respuestas esperadas:

```text
- su aportación concreta;
- una clase o método que sí entiende;
- una prueba que ejecutó;
- una documentación que redactó;
- una mejora que propone.
```

### X — eXplicar

Conclusión:

```text
La defensa individual exige delimitar qué entiende cada persona.
```

### A — Aplicar

Ensayo por parejas.

## Preguntas de defensa final

```text
1. ¿Qué parte de MiniJarvis puedes explicar mejor?
2. ¿Qué clase o método puedes enseñar?
3. ¿Qué prueba demuestra que funciona?
4. ¿Qué problema técnico resolviste?
5. ¿Qué evidencia demuestra Programación?
6. ¿Qué evidencia demuestra Entornos?
7. ¿Qué aportaste al equipo?
8. ¿Qué uso de IA hiciste?
9. ¿Cómo validaste una respuesta de IA?
10. ¿Qué cambiarías con dos semanas más?
11. ¿Qué hito te hizo aprender más?
12. ¿Qué parte necesitas seguir practicando?
```

## Actividad

```text
1. Elegir tres preguntas de defensa.
2. Responderlas por escrito.
3. Ensayar con una pareja.
4. La pareja pide una evidencia concreta.
5. Mejorar la respuesta para que cite código, prueba o documento.
```

## Errores frecuentes

| Error | Señal | Intervención docente |
|---|---|---|
| Discurso memorizado | No sabe señalar evidencia | Pedir archivo o línea aproximada. |
| Culpar al equipo | “Yo no hice eso” | Pedir aportación propia defendible. |
| Ocultar IA | Registro no coincide | Reforzar declaración honesta. |
| Inventar respuestas | No conectan con proyecto | Reencuadrar a evidencias reales. |

## Cierre

Ticket:

```text
1. ¿Qué evidencia defenderás sí o sí?
2. ¿Qué pregunta te cuesta más?
3. ¿Qué necesitas revisar antes de la defensa?
```

## Criterio de éxito

```text
El alumnado prepara una defensa individual basada en evidencias reales y comprensión propia.
```

---

# HF-S5 — Recuperación específica

## Duración

```text
45 minutos
```

## Objetivo

Diseñar evidencias de recuperación focalizadas para RA/CE pendientes, evitando tareas genéricas o castigos sin relación con el aprendizaje.

## Resultado esperado

Documento `recuperacion-especifica.md` para quien lo necesite, con RA/CE pendiente, evidencia concreta, tarea, verificación y defensa.

## Guion docente

```text
Recuperar no significa repetir todo el proyecto.

Recuperar significa aportar una evidencia específica de aquello que todavía no está demostrado.

Cada recuperación debe responder a: qué falta, qué harás, cómo se comprobará y cómo lo defenderás.
```

## Pizarra

```text
Recuperación específica:
RA/CE pendiente -> evidencia necesaria -> tarea focalizada -> verificación -> defensa
```

## Qué explicas tú

```text
- Que no todo el alumnado necesitará la misma recuperación.
- Que recuperar Programación puede requerir código y ejecución.
- Que recuperar Entornos puede requerir pruebas, documentación, Git, seguridad o diagramas.
- Que una recuperación debe ser proporcional y defendible.
```

## Actividad HEXA guiada

### H — Hecho

Un alumno tiene código funcional, pero no documentó pruebas ni puede reproducir la ejecución.

### E — Explorar

Pregunta:

```text
¿Debe repetir todo MiniJarvis o aportar una evidencia concreta de pruebas/reproducibilidad?
```

### X — eXplicar

Respuesta esperada:

```text
Debe aportar evidencia específica: README, prueba reproducible y defensa de cómo verificó.
```

### A — Aplicar

Diseñar recuperación focalizada.

## Plantilla de recuperación

```markdown
# Recuperación específica — HF

## RA/CE o aspecto pendiente

## Qué evidencia falta

## Tarea concreta

## Entregable

## Cómo se verificará

## Preguntas de defensa

## Fecha límite

## Resultado docente
```

Ejemplos de recuperación:

| Pendiente | Evidencia de recuperación |
|---|---|
| No entiende bucles/decisiones | Explicar y modificar un comando H2. |
| No demuestra colecciones | Implementar/defender memoria H3 mínima. |
| No defiende POO | Explicar Main/Agent/Memory y diagrama H4. |
| No hay pruebas | Crear prueba manual reproducible. |
| No hay seguridad | Revisar `.gitignore`, registros y datos ficticios. |
| No declara IA | Completar registro IA y validación. |

## Errores frecuentes

| Error | Señal | Intervención docente |
|---|---|---|
| Recuperación genérica | “Haz un resumen” | Vincular a RA/CE y evidencia. |
| Demasiado amplia | Rehacer todo | Focalizar en lo pendiente. |
| Sin defensa | Solo entrega archivo | Añadir preguntas orales. |
| Sin verificación | No se sabe si funciona | Definir prueba o criterio. |

## Cierre

Ticket:

```text
1. ¿Qué evidencia concreta te falta, si procede?
2. ¿Qué tarea focalizada la demostraría?
3. ¿Cómo se verificará?
```

## Criterio de éxito

```text
Cada recuperación queda conectada con una carencia concreta y una evidencia verificable y defendible.
```

---

# HF-S6 — Registro IA final, autoevaluación y mejora

## Duración

```text
45 minutos
```

## Objetivo

Cerrar la reflexión final sobre uso de IA, aprendizaje personal y mejora futura.

## Resultado esperado

Documentos:

```text
registro-ia-final.md
autoevaluacion-final.md
plan-mejora-final.md si procede
```

## Guion docente

```text
La IA ha podido aparecer en varios momentos del curso: como explicación, ayuda de depuración, revisión o comparación.

El cierre no busca castigar su uso. Busca que sea visible, responsable y defendible.

También vamos a cerrar con autoevaluación: qué he aprendido, qué aporté, qué errores tuve y qué haría mejor.
```

## Pizarra

```text
Registro IA final:
- dónde la usé;
- para qué;
- qué acepté;
- qué rechacé;
- cómo validé;
- qué aprendí.

Autoevaluación:
- fortalezas;
- evidencias;
- dificultades;
- aportación;
- mejora.
```

## Qué explicas tú

```text
- Que el registro IA final sintetiza el curso, no cada prompt mínimo.
- Que no se deben copiar prompts con secretos ni datos personales.
- Que la autoevaluación debe ser honesta y concreta.
- Que el plan de mejora debe ser realista, no una lista imposible.
```

## Actividad HEXA guiada

### H — Hecho

Una persona usó IA para entender `ArrayList`, revisar un README y preparar preguntas de defensa.

### E — Explorar

Pregunta:

```text
¿Cómo lo declara de forma responsable?
```

### X — eXplicar

Respuesta esperada:

```text
Indicando uso, utilidad, validación y aprendizaje propio, sin fingir que no la usó ni copiar respuestas sin entender.
```

### A — Aplicar

Completar registro IA y autoevaluación.

## Plantilla registro IA final

```markdown
# Registro IA final — MiniJarvis

## Usos principales

| Hito | Uso de IA | Qué acepté | Qué rechacé | Cómo validé |
|---|---|---|---|---|
| | | | | |

## Riesgos detectados

## Normas que respeté

## Qué aprendí sobre IA responsable

## Qué puedo defender sin IA
```

## Plantilla autoevaluación

```markdown
# Autoevaluación final

## Mi progreso durante el curso

## Mi aportación al equipo

## Evidencias que mejor me representan

## Dificultades superadas

## Qué necesito seguir practicando

## Valoración honesta de mi defensa
```

## Plantilla plan de mejora

```markdown
# Plan de mejora final

## Aspecto a mejorar

## Por qué es importante

## Acción concreta

## Evidencia de mejora

## Plazo realista
```

## Errores frecuentes

| Error | Señal | Intervención docente |
|---|---|---|
| Registro IA vacío pero lenguaje sospechoso | Niega uso evidente | Reforzar que declarar no penaliza si se valida. |
| Autoevaluación genérica | “Me fue bien” | Pedir evidencia y ejemplo. |
| Plan de mejora irreal | “Aprender todo Java” | Convertir a acción concreta. |
| Copiar reflexión de IA | Voz impersonal | Pedir ejemplo propio del curso. |

## Cierre

Ticket:

```text
1. ¿Qué uso de IA puedes declarar y defender?
2. ¿Qué evidencia representa mejor tu aprendizaje?
3. ¿Qué mejora concreta harías después del curso?
```

## Criterio de éxito

```text
El alumnado cierra el curso con reflexión honesta, registro IA responsable y plan de mejora realista.
```

---

# HF-S7 — Cierre, decisiones docentes y transición final

## Duración

```text
45 minutos
```

## Objetivo

Cerrar HF con una decisión docente clara para cada estudiante y preparar la transición a publicación, archivo o mejora posterior del proyecto.

## Resultado esperado

Checklist final completada y decisión:

```text
[ ] Cierre completo.
[ ] Cierre válido con mejoras menores.
[ ] Necesita recuperación específica.
[ ] No permite cerrar todavía.
```

## Guion docente

```text
Hoy cerramos el itinerario MiniJarvis.

Cada persona debe salir sabiendo si su cierre está completo, si necesita mejoras menores o si debe hacer recuperación específica.

El objetivo es que nadie se marche con una indicación ambigua como “mejora el proyecto”. Debe quedar claro qué evidencia falta y cómo se demuestra.
```

## Pizarra

```text
Decisión final:
- completo;
- válido con mejoras menores;
- recuperación específica;
- no cerrado todavía.

Toda decisión necesita evidencia y siguiente paso claro.
```

## Qué explicas tú

```text
- Cómo se comunicará la decisión.
- Qué diferencia hay entre mejora menor y recuperación.
- Que no se añaden tareas nuevas sin relación con evidencias pendientes.
- Que el proyecto puede archivarse como portfolio personal si no contiene datos sensibles.
```

## Actividad HEXA guiada

### H — Hecho

Un portfolio tiene buena demo, pero no hay defensa individual suficiente.

### E — Explorar

Pregunta:

```text
¿Puede cerrarse completo? ¿Qué decisión sería justa?
```

### X — eXplicar

Respuesta esperada:

```text
No debería cerrarse completo si falta comprensión defendible. Puede requerir defensa o recuperación específica.
```

### A — Aplicar

Revisión final con checklist.

## Checklist docente final

| Elemento | Sí | Parcial | No | Observación |
|---|---|---|---|---|
| Portfolio H0-H7 ordenado | | | | |
| Evidencias de Programación | | | | |
| Evidencias de Entornos | | | | |
| Demo final preparada | | | | |
| Plan B de demo | | | | |
| Defensa individual suficiente | | | | |
| Registro IA final | | | | |
| Autoevaluación | | | | |
| Recuperación si procede | | | | |
| Sin secretos ni datos personales | | | | |
| Plan de mejora realista | | | | |

## Actividad

```text
1. Revisar checklist.
2. Anotar una fortaleza.
3. Anotar una evidencia clave.
4. Anotar una mejora o recuperación si procede.
5. Comunicar decisión y siguiente paso.
```

## Errores frecuentes

| Error | Señal | Intervención docente |
|---|---|---|
| Decisión ambigua | “Revísalo un poco” | Especificar evidencia faltante. |
| Confundir mejora con recuperación | Tarea extra sin RA | Vincular a criterio. |
| Cerrar sin defensa | Solo hay documentos | Aplicar regla de comprensión defendible. |
| Ignorar seguridad final | Hay datos reales | Corregir antes de publicar o archivar. |

## Cierre del itinerario

Guion final:

```text
MiniJarvis empezó con una idea sencilla: construir poco a poco un agente propio.

Durante el curso habéis pasado por trabajo ágil, Java básico, decisiones, colecciones, orientación a objetos, clean code, persistencia, seguridad e IA responsable.

El producto importa, pero más importante es que podáis explicar cómo habéis llegado hasta aquí.

Ese es el cierre real: evidencias, comprensión y mejora.
```

## Criterio de éxito

```text
HF queda cerrado cuando cada estudiante tiene una decisión clara, evidencias revisadas y, si procede, una recuperación específica verificable.
```

---

## 5. Evaluación formativa de HF

HF debe servir para detectar:

```text
- quién puede ordenar su aprendizaje;
- quién distingue evidencias de Programación y Entornos;
- quién puede hacer una demo realista;
- quién tiene plan B;
- quién defiende su aportación individual;
- quién necesita recuperación específica;
- quién declara y valida uso de IA;
- quién reflexiona con honestidad;
- quién propone mejoras realistas;
- quién evita secretos y datos personales en el cierre.
```

Evidencias mínimas:

| Evidencia | Qué mirar |
|---|---|
| Portfolio final | H0-H7 ordenados, evidencias concretas y reflexión. |
| Demo final | Secuencia breve, segura y con plan B. |
| Defensa final | Comprensión individual y aportación propia. |
| Recuperación | Solo si procede, focalizada y verificable. |
| Registro IA final | Uso declarado, validado y crítico. |
| Autoevaluación | Honesta, concreta y conectada con evidencias. |
| Plan de mejora | Realista y accionable. |
| Seguridad | Sin secretos ni datos personales reales. |

---

## 6. Atención a la diversidad

### Si el alumnado se bloquea con el portfolio

Reducir objetivo:

```text
Elegir una evidencia fuerte de Programación y una evidencia fuerte de Entornos. Después completar el resto.
```

Preguntas de apoyo:

```text
¿Qué archivo sabes explicar?
¿Qué prueba sabes repetir?
¿Qué documento escribiste tú?
```

### Si el alumnado tiene ansiedad ante la demo

Permitir demo estructurada:

```text
1. Leer objetivo.
2. Ejecutar solo comandos preparados.
3. Explicar una evidencia.
4. Usar plan B si falla.
```

No convertir la demo en improvisación pública innecesaria.

### Si el alumnado tiene dificultades de expresión oral

Permitir apoyo visual:

```text
- guion breve;
- código abierto;
- checklist;
- preguntas graduadas;
- defensa en pequeño grupo si procede.
```

Mantener exigencia de comprensión, pero ajustar forma de expresión.

### Si el alumnado tiene RA pendientes

No pedir “todo otra vez”. Diseñar recuperación específica:

```text
RA pendiente -> evidencia concreta -> verificación -> defensa breve.
```

### Si hay alumnado avanzado

Extensión permitida:

```text
Preparar una sección de mejoras futuras realistas: pruebas automatizadas, empaquetado, interfaz gráfica simple, API real segura o despliegue local.
```

No exigir esa extensión a todo el grupo.

---

## 7. Uso responsable de IA en HF

Usos permitidos:

```text
- pedir ayuda para organizar el portfolio;
- pedir preguntas de defensa;
- revisar claridad de una explicación;
- mejorar redacción de autoevaluación;
- generar una checklist de demo, siempre adaptada.
```

Usos no permitidos:

```text
- inventar evidencias;
- escribir una defensa que la persona no entiende;
- ocultar uso de IA;
- copiar portfolio de otro;
- introducir datos personales, claves, tokens o `.env` reales;
- entregar reflexión sin voz propia.
```

Registro IA final mínimo:

```text
Qué usé:
Para qué:
Qué cambié:
Qué rechacé:
Cómo validé:
Qué puedo defender sin IA:
```

Frase docente:

```text
La IA puede ayudarte a ordenar ideas, pero no puede vivir por ti el proceso ni defender por ti el aprendizaje.
```

---

## 8. Criterios globales de éxito de HF

HF está consolidado cuando:

```text
[x] El portfolio final existe.
[x] El portfolio cubre H0-H7.
[x] Hay evidencias explícitas de Programación.
[x] Hay evidencias explícitas de Entornos de Desarrollo.
[x] La demo final está preparada.
[x] Existe plan B de demo.
[x] La defensa individual está preparada y realizada.
[x] El registro IA final está completo.
[x] La autoevaluación es concreta y honesta.
[x] El plan de mejora existe si procede.
[x] La recuperación específica existe si procede.
[x] No hay secretos ni datos personales reales.
[x] La decisión docente final es clara.
[x] Se cumple la regla: sin comprensión defendible, no hay evidencia completa.
```

---

## 9. Cierre definitivo del proyecto MiniJarvis

Mensaje final para el grupo:

```text
MiniJarvis no termina porque el código sea perfecto.

Termina porque podéis explicar una evolución: de una idea inicial a un agente con comandos, memoria, clases, herramientas, persistencia, trazabilidad e IA responsable o simulada.

El resultado final no es solo un programa. Es un conjunto de evidencias que demuestra aprendizaje técnico, trabajo con herramientas, documentación, seguridad, reflexión y defensa.

Ese portfolio es el verdadero producto profesional de 1.º DAW.
```

Última comprobación docente:

```text
Antes de publicar, archivar o compartir cualquier ejemplo:
- revisar que no hay datos personales reales;
- revisar que no hay `.env` real;
- revisar que no hay tokens ni claves;
- revisar que los ejemplos de Laura se presentan como orientación, no como copia;
- revisar que cada estudiante conserva voz propia.
```

Criterio profesional de cierre:

```text
Un cierre excelente no es necesariamente el que tiene más funciones, sino el que permite reconstruir el aprendizaje completo: problema inicial, decisiones, pruebas, errores, mejoras, seguridad, uso responsable de IA y defensa individual.
```

Frase final para el alumnado:

```text
No te lleves solo un proyecto terminado. Llévate una forma de trabajar: dividir problemas, documentar evidencias, probar cambios, pedir ayuda con criterio, proteger datos y defender tus decisiones.
```
