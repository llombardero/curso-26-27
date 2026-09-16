# Prompt — Presentación inicial de Programación y Entornos de Desarrollo

## 1.º DAW — Curso 2026/2027

Esta presentación se utiliza antes de S201. Su función es presentar los dos módulos, el método de trabajo, la evaluación basada en evidencias y el proyecto coordinado MiniJarvis.

No sustituye la presentación de S201 ni las presentaciones específicas de H0.

---

## 1. Fuentes que deben cargarse

### Fuentes principales

```text
01A-anexo-programacion-ra-ce.md
01B-anexo-entornos-ra-ce.md
02-calendario-hitos-sprints-2026-2027.md
05-politica-uso-ia-semaforo-registro-defensa.md
500-materiales-operativos-por-sesion/h0/S201-curso-narrativa-minijarvis-y-evidencias-docente.md
500-materiales-operativos-por-sesion/h0/S201-curso-narrativa-minijarvis-y-evidencias-alumnado.md
```

### Jerarquía de fuentes

Si las fuentes contienen formulaciones históricas diferentes, aplica este orden:

1. Las fichas operativas S201 son la referencia vigente para el inicio de H0.
2. `01A` y `01B` son la referencia para diferenciar Programación y Entornos.
3. El calendario se utiliza para la secuencia anual y la distribución semanal, no para reconstruir actividades antiguas de H0.
4. La política de IA es la referencia para permisos, registro, seguridad y defensa.

No utilices la autoevaluación antigua de 16 ítems ni la microprueba histórica. La secuencia vigente de H0 utiliza HADA en S202, pero esta presentación inicial solo debe anticiparlo brevemente.

---

## 2. Uso en NotebookLM

1. Crea un cuaderno llamado:

```text
Presentación inicial — Programación + Entornos — 1.º DAW
```

2. Carga las seis fuentes anteriores.
3. Abre `Studio → Slide Deck`.
4. Abre la personalización.
5. Pega el prompt completo del apartado 4.
6. Genera una presentación independiente de las presentaciones de H0.

---

## 3. Uso en Gemini

1. Abre un chat o Canvas nuevo.
2. Adjunta las seis fuentes.
3. Pega el prompt completo del apartado 4.
4. Solicita una presentación editable 16:9.
5. Después aplica el prompt de auditoría del apartado 6.

---

## 4. Prompt completo

```text
Actúa como diseñador instruccional y diseñador de presentaciones para Formación Profesional de Grado Superior en Andalucía.

Crea una presentación inicial para alumnado de 1.º de Desarrollo de Aplicaciones Web. Debe presentar conjuntamente los módulos de Programación y Entornos de Desarrollo, pero dejando muy clara su identidad, sus aprendizajes y su evaluación separada.

Utiliza exclusivamente las fuentes adjuntas. No inventes porcentajes de calificación, normas de asistencia, penalizaciones, fechas, herramientas obligatorias o criterios que no estén confirmados en ellas.

CONTEXTO
- Curso: 2026/2027.
- Nivel: 1.º DAW.
- Módulos coordinados: Programación y Entornos de Desarrollo.
- Proyecto guía común: MiniJarvis.
- Programación: 8 periodos semanales de 45 minutos.
- Entornos de Desarrollo: 3 periodos semanales de 45 minutos.
- Los dos módulos comparten proyecto y evidencias, pero mantienen resultados de aprendizaje, criterios y calificación separados.
- Esta es una sesión inicial de 45 minutos anterior a S201.

OBJETIVO DE LA SESIÓN
Que el alumnado comprenda:
1. qué aprenderá en cada módulo;
2. por qué ambos módulos se coordinan;
3. qué construirá durante el curso;
4. cómo se trabajará mediante retos y evidencias;
5. cómo se evaluará sin reducir la evaluación al producto final;
6. qué responsabilidad tiene ante el uso de IA;
7. cuál será el primer reto del curso.

PREGUNTA GUÍA
¿Qué significa aprender a desarrollar software que funciona, se puede comprobar y somos capaces de explicar?

AUDIENCIA Y TONO
- Alumnado que acaba de incorporarse a 1.º DAW.
- Experiencia previa heterogénea.
- Puede haber personas que nunca hayan programado.
- Español de España, claro, directo y profesional.
- Tono acogedor y exigente, sin infantilizar ni prometer que todo será fácil.
- Evita siglas sin explicación y listados normativos de RA/CE.
- Traduce los resultados de aprendizaje a acciones comprensibles para el alumnado.

DISEÑO VISUAL
- Formato 16:9.
- Estilo tecnológico, limpio y profesional.
- Alto contraste y tipografía sans serif legible desde el fondo del aula.
- Una idea principal por diapositiva.
- Máximo 35 palabras visibles y 5 viñetas por diapositiva.
- Utiliza diagramas, líneas temporales, tarjetas, iconos y comparaciones visuales.
- No uses tablas curriculares densas.
- No uses fotografías de relleno, robots humanoides ni cerebros luminosos.
- No dependas únicamente del color para distinguir Programación y Entornos.
- Asigna a cada módulo un color y un símbolo constantes, acompañados siempre de su nombre.

GENERA 16 DIAPOSITIVAS

1. BIENVENIDA
Título sugerido: “Aprender a construir software que puedas explicar”.
Incluye la pregunta guía y los nombres completos de ambos módulos.
Tiempo: 2 minutos.

2. DOS MÓDULOS, UN MISMO PRODUCTO
Diagrama de dos carriles que confluyen en MiniJarvis:
- Programación: construir el comportamiento del software.
- Entornos: hacerlo trazable, comprobable, colaborativo y mantenible.
Aclara que ninguno queda subordinado al otro.
Tiempo: 2 minutos.

3. QUÉ APRENDERÁS EN PROGRAMACIÓN
Traduce los RA principales a seis acciones comprensibles:
- escribir y ejecutar programas Java;
- usar variables, operaciones y entrada/salida;
- tomar decisiones y repetir acciones;
- depurar y tratar errores;
- organizar información en colecciones;
- diseñar clases, objetos y persistencia.
Indica que algunos contenidos avanzados dependerán del progreso real del grupo.
Tiempo: 3 minutos.

4. QUÉ APRENDERÁS EN ENTORNOS DE DESARROLLO
Presenta seis acciones profesionales:
- comprender las fases del desarrollo;
- configurar y utilizar IntelliJ;
- usar Git y GitHub con trazabilidad;
- diseñar pruebas y depurar;
- documentar y representar diseños con UML;
- revisar, refactorizar y automatizar cuando proceda.
Tiempo: 3 minutos.

5. EL PROYECTO GUÍA: MINIJARVIS
Explica que será un asistente por consola en Java que crecerá por versiones.
No lo presentes como una IA completa desde el primer día.
Incluye la idea central: “La meta no es que una IA programe por ti; es aprender a construir software que entiendes, pruebas y mejoras”.
Tiempo: 3 minutos.

6. MAPA DEL CURSO POR VERSIONES
Crea una línea temporal visual H0 → H1 → H2 → H3 → H4 → H5 → H6 → H7 → HF.
Usa una frase breve por hito obtenida de las fuentes.
Señala H7 como adaptable u opcional según el progreso.
No incluyas fechas pequeñas ni tablas de RA.
Tiempo: 3 minutos.

7. RITMO SEMANAL
Representa visualmente:
- Programación: 8 periodos de 45 minutos.
- Entornos: 3 periodos de 45 minutos.
- Un proyecto coordinado y dos evaluaciones separadas.
No inventes distribución de tareas para días concretos más allá de lo confirmado.
Tiempo: 2 minutos.

8. CÓMO APRENDEREMOS
Presenta tres capas conectadas:
- ABP: un proyecto que crece;
- HEXA: reto, exploración, explicación y aplicación;
- Scrum adaptado: trabajo visible, revisión y mejora.
Evita convertir la diapositiva en una clase teórica sobre metodologías.
Tiempo: 3 minutos.

9. QUÉ OCURRE EN CADA HITO
Diagrama de ciclo:
reto → explorar → comprender → construir → probar → documentar → explicar → mejorar.
Aclara que “terminado” no significa únicamente “el programa se ejecuta”.
Tiempo: 2 minutos.

10. TRABAJO DE EQUIPO Y RESPONSABILIDAD INDIVIDUAL
Compara visualmente:
- evidencias de equipo: producto, tablero, repositorio, README, pruebas y demo;
- evidencias individuales: portfolio, decisiones, registro de IA, defensa y capacidad de modificar.
Aclara que trabajar en equipo no oculta la aportación individual.
Tiempo: 3 minutos.

11. QUÉ CONVIERTE UNA ENTREGA EN EVIDENCIA
Destaca tres condiciones:
- funciona o muestra con honestidad qué falla;
- está documentada y trazable;
- puedes explicarla, probarla y modificarla.
Incluye: “Un archivo entregado no es automáticamente una evidencia completa”.
Tiempo: 3 minutos.

12. CÓMO SE EVALUARÁ
Explica sin porcentajes:
- Programación y Entornos se evalúan por separado;
- se comprueban resultados de aprendizaje y criterios de cada módulo;
- se usan código, repositorio, pruebas, documentación, portfolio, observación y defensa;
- el producto final no acredita por sí solo todo el proceso;
- una evidencia incompleta puede revisarse o recuperarse de forma específica.
No afirmes que todo tiene el mismo peso.
Tiempo: 2 minutos.

13. IA: COPILOTO, NO AUTOR OCULTO
Crea un semáforo visual:
- verde: comprender, practicar, revisar y proponer pruebas;
- amarillo: generar o refactorizar fragmentos con registro, verificación y defensa;
- rojo: copiar sin entender, ocultar el uso, introducir datos, contraseñas, claves o secretos.
Incluye la obligación de poder explicar y modificar cualquier aportación incorporada.
Tiempo: 3 minutos.

14. HERRAMIENTAS QUE IREMOS INCORPORANDO
Muestra un ecosistema progresivo, no una lista de requisitos para el primer día:
Java, IntelliJ, Git, GitHub, Markdown/README, pruebas y depuración, UML, Moodle y herramientas de IA autorizadas.
No afirmes que todas se usarán desde la primera semana.
Tiempo: 2 minutos.

15. ACTIVIDAD INICIAL
Plantea una actividad individual de 5 minutos con tres preguntas:
- ¿Qué te gustaría ser capaz de construir al final del curso?
- ¿Qué parte te genera más incertidumbre ahora mismo?
- ¿Qué necesitarías del grupo y del profesorado para aprender de forma segura?
Después pide contraste breve por parejas, sin obligar a compartir experiencias personales.
Tiempo: 7 minutos.

16. PRIMER RETO Y TICKET DE SALIDA
Presenta H0 como el reto para diseñar y probar una forma de trabajar antes de desarrollar MiniJarvis.
Anticipa la secuencia:
comprender el reto → HADA como hipótesis → equipo provisional → funciones → torre → retrospectiva → contrato.
No expliques todavía el cuestionario ni formes equipos.
Ticket individual:
- una diferencia entre Programación y Entornos;
- una evidencia que permitirá demostrar aprendizaje;
- una duda concreta para comenzar.
Tiempo: 2 minutos.

NOTAS DEL PRESENTADOR
Para cada diapositiva añade:
1. finalidad;
2. tiempo;
3. explicación oral sugerida;
4. pregunta al alumnado;
5. respuesta o idea esperada;
6. error que debe evitarse;
7. transición a la siguiente diapositiva.

Si no puedes generar notas del presentador, crea después una tabla separada con esas siete columnas.

RESTRICCIONES IMPORTANTES
- No inventes porcentajes de calificación.
- No presentes las ponderaciones históricas de los RA como sistema vigente.
- No confundas evaluación compartida con una nota única para ambos módulos.
- No prometas que H7 o una integración real de IA se realizará obligatoriamente.
- No uses HADA como test de personalidad ni adelantes perfiles.
- No presentes las funciones educativas de H0 como roles oficiales de Scrum.
- No uses mensajes amenazantes sobre evaluación o IA.
- No incluyas datos de alumnado real.
- No sobrecargues la presentación con legislación o códigos de RA/CE.

SALIDA
Entrega una presentación terminada, no un esquema abstracto. Para cada diapositiva proporciona:
- número;
- título;
- texto visible definitivo;
- composición visual concreta;
- notas del presentador;
- tiempo.

La suma del tiempo debe ser exactamente 45 minutos.
```

---

## 5. Resultado esperado

La presentación debe dejar esta idea:

```text
Programación enseña a construir el comportamiento del software.
Entornos enseña a desarrollarlo de manera profesional, comprobable y sostenible.
MiniJarvis conecta ambos aprendizajes, pero cada módulo conserva su evaluación.
```

No debe intentar enseñar los contenidos técnicos en la primera sesión.

---

## 6. Prompt de auditoría

```text
Audita la presentación inicial contra las fuentes adjuntas.

Comprueba:
1. que diferencia claramente Programación y Entornos;
2. que ambos módulos aparecen coordinados, pero con evaluación separada;
3. que no hay porcentajes, penalizaciones o normas inventadas;
4. que los aprendizajes se expresan como acciones comprensibles y no como una lista de códigos RA/CE;
5. que MiniJarvis se presenta como proyecto progresivo y no como IA completa desde el inicio;
6. que H7 aparece como adaptable según progreso;
7. que el producto, el proceso y la evidencia individual están diferenciados;
8. que la política de IA coincide con verde, amarillo y rojo de la fuente;
9. que HADA solo se anticipa como hipótesis y no como test de personalidad;
10. que la actividad permite participar sin revelar información personal;
11. que la suma de tiempos es exactamente 45 minutos;
12. que ninguna diapositiva supera 35 palabras visibles o 5 viñetas.

Devuelve una tabla con criterio, cumple/no cumple, diapositiva y corrección. Después regenera únicamente las diapositivas que no cumplan.
```

---

## 7. Prompt para Google Slides editable

```text
Convierte la presentación aprobada en diapositivas editables 16:9. Mantén los textos, el orden y las notas. Utiliza texto, formas, líneas e iconos editables; no conviertas cada diapositiva en una imagen plana. Conserva alto contraste, tipografía grande y símbolos además de colores para diferenciar Programación y Entornos. No añadas información nueva.
```

---

## 8. Comprobación docente antes de proyectar

- [ ] Programación y Entornos están diferenciados.
- [ ] Se explica que se califican por separado.
- [ ] No aparecen porcentajes sin confirmar.
- [ ] MiniJarvis se presenta como producto progresivo.
- [ ] H7 aparece condicionado al progreso.
- [ ] Se distinguen trabajo de equipo y evidencia individual.
- [ ] La política de IA coincide con el documento vigente.
- [ ] No se muestran RA/CE como tablas normativas densas.
- [ ] La actividad inicial dura 5 minutos más contraste breve.
- [ ] H0 queda presentado como el siguiente reto.
- [ ] Los tiempos suman 45 minutos.
