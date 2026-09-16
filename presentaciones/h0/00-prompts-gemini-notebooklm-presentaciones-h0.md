# Prompts para crear las presentaciones de H0 con Gemini o NotebookLM

## Curso 2026/2027 — 1.º DAW — Programación + Entornos de Desarrollo

Este documento permite generar cinco presentaciones independientes:

1. S201 — Curso, narrativa MiniJarvis y reto H0.
2. S202 — Scrum mínimo y perfil HADA.
3. S203 — Composición HADA, equipos provisionales y funciones.
4. S204 — Torre de papel: dos ciclos Scrum.
5. S205 — De la torre a MiniJarvis.

Las presentaciones son apoyo visual para proyectar. No deben sustituir las guías docentes ni contener toda la ficha del alumnado.

---

## 1. Procedimiento recomendado en NotebookLM

NotebookLM permite generar una presentación desde el panel **Studio → Slide Deck**. Conviene crear un único cuaderno llamado:

`H0 — Equipos Scrum, HADA y torre de papel — 1.º DAW`

Carga estas fuentes:

```text
Scrum/HADA_Gazteleraz_2019-1.pdf
hitos/h0-torre-papel-scrum/10A-cuestionario-diagnostico-habilidades-equipos-scrum.md
500-materiales-operativos-por-sesion/h0/S201-curso-narrativa-minijarvis-y-evidencias-docente.md
500-materiales-operativos-por-sesion/h0/S201-curso-narrativa-minijarvis-y-evidencias-alumnado.md
500-materiales-operativos-por-sesion/h0/S202-scrum-minimo-y-autoevaluacion-de-habilidades-docente.md
500-materiales-operativos-por-sesion/h0/S202-scrum-minimo-y-autoevaluacion-de-habilidades-alumnado.md
500-materiales-operativos-por-sesion/h0/S203-microprueba-y-equipos-provisionales-de-3-o-4-docente.md
500-materiales-operativos-por-sesion/h0/S203-microprueba-y-equipos-provisionales-de-3-o-4-alumnado.md
500-materiales-operativos-por-sesion/h0/S204-sprint-de-torre-prueba-review-y-retrospectiva-docente.md
500-materiales-operativos-por-sesion/h0/S204-sprint-de-torre-prueba-review-y-retrospectiva-alumnado.md
500-materiales-operativos-por-sesion/h0/S205-transferencia-a-minijarvis-y-contrato-de-equipo-docente.md
500-materiales-operativos-por-sesion/h0/S205-transferencia-a-minijarvis-y-contrato-de-equipo-alumnado.md
```

Para cada presentación:

1. deja seleccionadas únicamente las fuentes indicadas en su apartado;
2. abre `Studio`;
3. selecciona `Slide Deck`;
4. abre la personalización mediante el icono de edición;
5. pega el prompt específico de la sesión;
6. genera una presentación independiente;
7. comprueba títulos, tiempos, reglas y atribución antes de proyectarla.

No generes las cinco presentaciones en una sola ejecución.

---

## 2. Procedimiento recomendado en Gemini

1. Abre Gemini y crea un chat o Canvas nuevo para cada sesión.
2. Adjunta las fuentes indicadas en el apartado correspondiente.
3. Pega primero el **bloque común**.
4. A continuación pega el **prompt específico** de la sesión.
5. Pide la creación en formato presentación o diapositivas 16:9.
6. Si Gemini solo entrega un guion, utiliza el prompt de corrección incluido al final.

No pegues datos reales del alumnado, puntuaciones HADA, observaciones privadas ni conflictos de los equipos.

---

## 3. Bloque común para las cinco presentaciones

Copia este bloque antes del prompt específico cuando utilices Gemini. En NotebookLM puede incorporarse al comienzo de cada personalización.

```text
Actúa como diseñador instruccional y diseñador de presentaciones para 1.º de Desarrollo de Aplicaciones Web en Andalucía.

Crea una presentación para proyectar durante una sesión presencial del proyecto anual MiniJarvis. Debes utilizar exclusivamente las fuentes adjuntas o seleccionadas. No inventes contenidos, tiempos, reglas, productos ni criterios que no aparezcan en ellas.

AUDIENCIA
- Alumnado de 1.º DAW.
- Primeros días del curso.
- Experiencia heterogénea y posible ansiedad ante programación, trabajo en equipo e inteligencia artificial.
- Lengua: español de España, claro, directo y respetuoso.

PROPÓSITO DE LA PRESENTACIÓN
- Guiar la sesión en tiempo real.
- Hacer visible el reto, los pasos, los tiempos y las evidencias.
- Provocar participación, decisiones y explicación.
- No sustituir la ficha de trabajo del alumnado.

DISEÑO VISUAL
- Formato panorámico 16:9.
- Estilo tecnológico, limpio, profesional y cercano; no infantil.
- Fondo claro o muy oscuro con contraste alto.
- Tipografía sans serif grande y legible desde el fondo del aula.
- Una idea principal por diapositiva.
- Máximo 5 viñetas y, salvo una tabla imprescindible, máximo 35 palabras visibles por diapositiva.
- Prioriza diagramas, líneas temporales, tarjetas, iconos sencillos y comparaciones visuales.
- Evita fotografías decorativas, robots humanoides, cerebros luminosos y arte genérico de IA.
- No uses texto pequeño, párrafos largos, tablas densas ni fondos con ruido visual.
- No dependas solo del color para transmitir significado.
- Mantén nombres, colores y símbolos consistentes durante todo H0.

MODELO DIDÁCTICO
- Haz visible la secuencia HEXA cuando corresponda: Hecho/reto, Exploración, eXplicación y Aplicación.
- Presenta una pregunta guía al inicio.
- Incluye pausas de actividad y comprobación, no solo explicación.
- Distingue producto, proceso y evidencia.
- Termina con un ticket o pregunta de salida y un puente a la sesión siguiente.

SCRUM
- No presentes las cuatro funciones educativas como cuatro roles oficiales de Scrum.
- Distingue, cuando sea necesario, las responsabilidades Scrum —Product Owner, Scrum Master y Developers— de las funciones operativas utilizadas en el aula.
- No conviertas Scrum en una lista extensa de teoría profesional.

HADA
- Presenta HADA como herramienta formativa para formular hipótesis sobre preferencias de contribución.
- No lo presentes como test psicológico, diagnóstico, identidad, nota o predictor infalible.
- No asignes automáticamente una función al perfil con puntuación mayor.
- No muestres puntuaciones nominales ni ejemplos que permitan comparar estudiantes.
- Mantén la atribución: “Tknika, HADA — Análisis de la composición del equipo, 2019”.

NOTAS DEL PRESENTADOR
Para cada diapositiva añade notas breves con:
1. finalidad;
2. tiempo aproximado;
3. frase de apertura o pregunta;
4. acción esperada del alumnado;
5. error o confusión que debe evitarse.

Si la herramienta no admite notas del presentador, entrega después de las diapositivas una tabla separada con esas cinco columnas.

SALIDA
- Genera el número de diapositivas indicado en el prompt específico.
- Numera las diapositivas.
- Proporciona título, contenido visible, sugerencia visual y notas del presentador.
- No incluyas bibliografía extensa en todas las diapositivas; añade una diapositiva final de fuentes cuando se solicite.
- Revisa que la suma de tiempos coincida con la duración real de la sesión.
```

---

# 4. Presentación S201

## Fuentes que deben estar seleccionadas

```text
S201-curso-narrativa-minijarvis-y-evidencias-docente.md
S201-curso-narrativa-minijarvis-y-evidencias-alumnado.md
```

## Prompt específico

```text
Crea la presentación de la sesión S201: “Curso, narrativa MiniJarvis y reto H0”.

DURACIÓN
45 minutos.

OBJETIVO
Que el alumnado comprenda qué construirá durante el curso, cómo se trabajará mediante hitos y evidencias y por qué H0 comienza diseñando y probando un equipo mediante una torre de papel.

PREGUNTA GUÍA
¿Cómo podremos demostrar que un producto es nuestro, funciona y refleja aprendizaje real?

GENERA 12 DIAPOSITIVAS CON ESTA SECUENCIA

1. Portada: “MiniJarvis empieza por el equipo”, pregunta guía y H0.
2. Qué construiremos: evolución progresiva de un programa pequeño; evita prometer una IA completa desde el inicio.
3. Qué no haremos todavía: delimita expectativas irreales y reduce ansiedad.
4. Mapa visual del proyecto MiniJarvis por hitos, usando solo la información de las fuentes.
5. Cómo aprenderemos: diagrama HEXA con reto, exploración, explicación y aplicación.
6. Reto central de H0: diseñar, probar y revisar una forma de trabajar en equipo.
7. Secuencia visual S201 → S202 → S203 → S204 → S205.
8. Por qué una torre de papel: producto sencillo para observar planificación, funciones, bloqueos, pruebas y mejora.
9. Producto, proceso y evidencia: comparación con ejemplos breves obtenidos de las fuentes.
10. IA responsable: semáforo verde/ámbar/rojo, privacidad, autoría y obligación de poder explicar.
11. Actividad del alumnado: reformular MiniJarvis y completar “H0 nos permitirá aprender a trabajar en equipo mediante…”.
12. Ticket de salida y puente a S202: Scrum mínimo y HADA como hipótesis, no como etiqueta.

REQUISITOS ESPECÍFICOS
- La torre debe aparecer desde esta primera sesión como el reto central de H0.
- No expliques aún cómo se puntúa HADA.
- No formes equipos ni sugieras perfiles.
- Incluye una única línea temporal visual clara para H0.
- El ticket final debe poder responderse individualmente en dos minutos.
```

## Qué debe comprobar el docente

- MiniJarvis no aparece como “chatbot inteligente completo” desde H1.
- La torre tiene finalidad pedagógica y no competitiva.
- H0 aparece como un reto completo, no como cinco actividades inconexas.
- IA responsable incluye privacidad, autoría y defensa.
- La presentación no adelanta resultados ni funciones HADA.

---

# 5. Presentación S202

## Fuentes que deben estar seleccionadas

```text
S202-scrum-minimo-y-autoevaluacion-de-habilidades-docente.md
S202-scrum-minimo-y-autoevaluacion-de-habilidades-alumnado.md
HADA_Gazteleraz_2019-1.pdf
10A-cuestionario-diagnostico-habilidades-equipos-scrum.md
```

## Prompt específico

```text
Crea la presentación de la sesión S202: “Scrum mínimo y perfil HADA”.

DURACIÓN
45 minutos.

OBJETIVO
Que cada estudiante comprenda el ciclo Scrum mínimo necesario para H0 y complete HADA correctamente como hipótesis privada de contribución.

PREGUNTA GUÍA
¿Qué puedo aportar inicialmente a un equipo y qué necesito practicar?

GENERA 12 DIAPOSITIVAS CON ESTA SECUENCIA

1. Portada y pregunta guía.
2. Recuperación de S201: H0 diseña, prueba y revisa un equipo.
3. Scrum mínimo como ciclo: objetivo → backlog → trabajo visible → prueba → review → retrospectiva → adaptación.
4. Vocabulario imprescindible: sprint, backlog, tarea, bloqueo, prueba, review y retrospectiva.
5. Review frente a retrospectiva mediante una comparación visual de dos columnas.
6. Responsabilidades Scrum frente a funciones educativas del aula; deja claro que no son equivalentes.
7. Qué es HADA y qué no es: herramienta formativa, no nota, personalidad ni etiqueta.
8. Instrucciones de cumplimentación: en cada fila deben utilizarse una vez 4, 3, 2 y 1.
9. Cálculo y autocontrol: seis filas, cuatro sumas entre 6 y 24 y total 60.
10. Diagrama HADA: objetivos-relaciones y continuidad-cambio; sitúa Gestor, Colaborador, Desarrollador y Analista.
11. Reflexión privada: dos tendencias que reconoce, una aportación inicial y una capacidad por practicar; no compartir números.
12. Ticket de salida, recogida segura y puente a S203.

REQUISITOS ESPECÍFICOS
- No copies los 24 enunciados en las diapositivas: están en la ficha.
- Puedes mostrar una fila esquemática sin respuestas para explicar el reparto 4–3–2–1.
- No inventes umbrales alto, medio o bajo.
- Explica visualmente que un empate es válido.
- Evita frases como “eres Gestor” o “tu rol será Analista”. Usa “tendencia”, “preferencia” o “hipótesis”.
- Incluye la atribución a Tknika en la diapositiva de HADA y una fuente final discreta.
```

## Qué debe comprobar el docente

- Cada fila exige exactamente `4, 3, 2 y 1`.
- Cada columna queda entre 6 y 24.
- El total es 60.
- No aparecen umbrales inventados.
- Las puntuaciones permanecen privadas.
- HADA no se confunde con los roles oficiales de Scrum.

---

# 6. Presentación S203

## Fuentes que deben estar seleccionadas

```text
S203-microprueba-y-equipos-provisionales-de-3-o-4-docente.md
S203-microprueba-y-equipos-provisionales-de-3-o-4-alumnado.md
10A-cuestionario-diagnostico-habilidades-equipos-scrum.md
HADA_Gazteleraz_2019-1.pdf
```

## Prompt específico

```text
Crea la presentación de la sesión S203: “Composición HADA, equipos provisionales y funciones para la torre”.

DURACIÓN
45 minutos.

OBJETIVO
Que cada equipo provisional utilice HADA sin publicar puntuaciones, identifique capacidades presentes o por compensar y deje preparadas funciones, participación, backlog y definición de terminado para la torre.

PREGUNTA GUÍA
¿Cómo convertimos preferencias distintas en una organización que podamos probar?

GENERA 11 DIAPOSITIVAS CON ESTA SECUENCIA

1. Portada y pregunta guía.
2. De perfil individual a hipótesis de equipo: HADA no dicta la composición ni el destino de nadie.
3. Reglas de privacidad: compartir aportaciones es voluntario; no se comparan números.
4. Lectura del equipo: capacidad presente, parcialmente presente o por compensar.
5. Cuatro funciones operativas: valor/backlog, facilitación/tiempo, calidad/pruebas y evidencias/comunicación.
6. Advertencia visual: funciones educativas ≠ roles oficiales de Scrum; todo el equipo participa en la construcción.
7. Asignación razonada: responsable, sustituto, conducta observable y capacidad que se desea practicar.
8. Regla de participación: ejemplo de formulación observable y mecanismo de recuperación.
9. Backlog inicial de la torre: pendiente, en curso y terminado; pocas tareas y responsables visibles.
10. Definición de terminado: criterios mínimos de estabilidad, materiales, prueba y evidencia tomados de las fuentes.
11. Lista de comprobación y ticket individual para llegar a S204 preparados.

REQUISITOS ESPECÍFICOS
- No relaciones de forma automática Gestor con mando, Colaborador con secretario, Desarrollador con constructor o Analista con calidad.
- Sí puedes presentar afinidades como hipótesis discutibles y acompañarlas de oportunidades de aprendizaje.
- No llames “jefe” a ninguna función.
- Los equipos son provisionales.
- No se construye todavía la torre.
- Debe quedar visible qué ocurrirá si una capacidad está menos representada: se compensa con una función y una conducta observable.
```

## Qué debe comprobar el docente

- No aparecen puntuaciones personales.
- Las cuatro funciones tienen responsable y sustituto.
- Todo el equipo sigue participando en el producto.
- La regla de participación es observable.
- El backlog y la definición de terminado quedan preparados antes de S204.

---

# 7. Presentación S204

## Fuentes que deben estar seleccionadas

```text
S204-sprint-de-torre-prueba-review-y-retrospectiva-docente.md
S204-sprint-de-torre-prueba-review-y-retrospectiva-alumnado.md
10A-cuestionario-diagnostico-habilidades-equipos-scrum.md
```

## Prompt específico

```text
Crea la presentación de la sesión S204: “Torre de papel: dos ciclos Scrum, prueba, review y retrospectiva”.

DURACIÓN
90 minutos.

OBJETIVO
Que los equipos pongan a prueba su organización, construyan un incremento verificable, inspeccionen producto y proceso y apliquen una mejora en un segundo ciclo.

PREGUNTA GUÍA
¿Nuestra forma de organizarnos nos ayuda a construir, comprobar y mejorar?

GENERA 14 DIAPOSITIVAS CON ESTA SECUENCIA

1. Portada y pregunta guía.
2. Qué cuenta como éxito: producir evidencia y aplicar una mejora; no ganar por altura.
3. Reto, materiales autorizados, límites y seguridad según las fuentes.
4. Definición de terminado de la torre en formato checklist visual.
5. Recordatorio de funciones y sustitutos; todo el equipo construye.
6. Tablero inicial y límite de trabajo en curso.
7. Ciclo 1: planificación breve y construcción, con temporizador e hitos temporales.
8. Prueba 1: protocolo de estabilidad, medición y registro; no reparar durante la prueba.
9. Review frente a retrospectiva: producto primero, proceso después.
10. Decisión de adaptación: qué cambia en diseño, backlog, prueba o coordinación y qué se mantiene.
11. Ciclo 2: construir la mejora acordada con temporizador visible.
12. Prueba 2: mismo protocolo para poder comparar resultados.
13. Review final: cumplimiento, altura válida, diferencias entre pruebas y evidencia mostrable.
14. Retrospectiva HADA-funciones, ticket individual y puente a S205.

REQUISITOS ESPECÍFICOS
- Mantén exactamente los materiales, límites y protocolo de prueba indicados en las fuentes.
- La prueba 1 y la prueba 2 deben usar el mismo procedimiento.
- Incluye una diapositiva que pueda permanecer proyectada durante cada intervalo de construcción, con tiempo y reglas esenciales.
- No conviertas la altura en clasificación pública.
- Distingue claramente resultado del producto y funcionamiento del equipo.
- Una torre que cae puede cerrar correctamente si hay dos intentos documentados y explicación causal.
- No uses HADA para culpar o explicar conflictos.
```

## Qué debe comprobar el docente

- Hay dos ciclos completos, no dos intentos improvisados.
- Existe prueba comparable después de cada ciclo.
- La mejora se decide antes del segundo ciclo.
- Review y retrospectiva no se mezclan.
- Se observan conductas y funciones, no identidades HADA.
- La altura no domina la presentación.

---

# 8. Presentación S205

## Fuentes que deben estar seleccionadas

```text
S205-transferencia-a-minijarvis-y-contrato-de-equipo-docente.md
S205-transferencia-a-minijarvis-y-contrato-de-equipo-alumnado.md
10A-cuestionario-diagnostico-habilidades-equipos-scrum.md
```

## Prompt específico

```text
Crea la presentación de la sesión S205: “De la torre a MiniJarvis: revisión del equipo, contrato y rotación”.

DURACIÓN
45 minutos.

OBJETIVO
Que cada equipo convierta las evidencias de la torre en una decisión razonada, un contrato observable, un plan de rotación y un primer backlog para MiniJarvis.

PREGUNTA GUÍA
¿Qué conservaremos, qué cambiaremos y cómo comprobaremos que la mejora funciona?

GENERA 11 DIAPOSITIVAS CON ESTA SECUENCIA

1. Portada y pregunta guía.
2. Cadena de evidencia: hipótesis HADA → conducta observada → aprendizaje → decisión.
3. Qué cuenta como evidencia: decisión, bloqueo, prueba, participación, adaptación y explicación; evita impresiones vagas.
4. Diferencia entre autopercepción y conducta: una diferencia aporta información y no invalida a la persona.
5. Tres decisiones posibles: mantener; mantener con ajustes; solicitar revisión docente razonada.
6. Qué no justifica por sí solo cambiar el equipo: caída, poca altura, amistad o coincidencia de perfiles.
7. Contrato observable: comunicación, bloqueos, participación, calidad, evidencias y conflicto.
8. Funciones iniciales para MiniJarvis y sustitutos, distinguiéndolas de los roles oficiales de Scrum.
9. Rotación: cuándo ocurre, qué cambia y qué capacidad distinta practicará cada persona.
10. Primer backlog de MiniJarvis con criterio de aceptación y evidencia individual.
11. Ticket final de H0 y puente a H1.

REQUISITOS ESPECÍFICOS
- El contrato debe usar conductas verificables; evita “trabajaremos bien” o “nos respetaremos”.
- Ninguna persona queda ligada durante el trimestre a la función asociada a su mayor valor HADA.
- Un cambio de composición requiere evidencia, conversación privada y decisión docente.
- Incluye al menos un ejemplo de transformar una regla vaga en una regla observable.
- El cierre debe pedir una conducta que se mantendrá y una función diferente que se practicará.
```

## Qué debe comprobar el docente

- Cada decisión cita evidencias de la torre.
- El contrato contiene verbos observables.
- Hay responsables, sustitutos y fecha o condición de rotación.
- El backlog de MiniJarvis no repite tareas de la torre.
- El resultado HADA no fija el rol permanente.

---

# 9. Prompt de revisión y corrección

Después de generar cualquier presentación, pega este prompt en Gemini o úsalo como nueva instrucción de personalización:

```text
Audita la presentación anterior contra las fuentes adjuntas.

Comprueba uno por uno:
1. duración y número de diapositivas;
2. correspondencia entre diapositivas y cronograma de la guía docente;
3. ausencia de contenidos inventados;
4. diferencia entre responsabilidades oficiales de Scrum y funciones educativas;
5. tratamiento no psicométrico, privado y no calificable de HADA;
6. ausencia de etiquetas, umbrales o asignaciones automáticas de perfil;
7. instrucciones y productos que debe producir el alumnado;
8. presencia de pausas activas, ticket y puente a la sesión siguiente;
9. legibilidad: máximo 35 palabras visibles por diapositiva y máximo 5 viñetas;
10. atribución correcta a Tknika cuando aparezca HADA.

Devuelve primero una tabla con:
- criterio;
- cumple/no cumple;
- diapositiva afectada;
- corrección concreta.

Después genera únicamente las diapositivas corregidas. No reescribas las que ya cumplen.
```

---

# 10. Prompt alternativo si la herramienta solo genera un guion

```text
Convierte el guion anterior en una presentación terminada y proyectable.

Para cada diapositiva entrega exactamente:
- número;
- título;
- texto visible final;
- composición visual concreta;
- notas del presentador;
- tiempo.

No describas lo que podría contener: escribe el contenido definitivo. Respeta 16:9, máximo 35 palabras visibles, máximo 5 viñetas y una idea principal por diapositiva. Incluye diagramas y cronogramas con textos exactos, no marcadores como “[añadir imagen]”.
```

---

# 11. Prompt para obtener una versión editable en Google Slides

```text
Genera esta presentación como diapositivas editables en formato 16:9. Conserva títulos, textos, diagramas, notas y orden aprobados. Utiliza elementos editables —texto, formas, líneas e iconos— en lugar de convertir cada diapositiva en una única imagen. Mantén alto contraste y tipografía legible. No añadas información nueva durante la conversión.
```

---

# 12. Control final antes de usar en clase

- [ ] La presentación corresponde a una sola sesión.
- [ ] Los tiempos suman la duración real.
- [ ] Las actividades coinciden con la ficha del alumnado.
- [ ] Las reglas de la torre coinciden con S204.
- [ ] No aparecen nombres ni resultados reales.
- [ ] HADA no se presenta como diagnóstico o etiqueta.
- [ ] Las funciones educativas no se presentan como roles oficiales de Scrum.
- [ ] Las instrucciones importantes también están escritas, no solo codificadas por color.
- [ ] Se incluye ticket o comprobación final.
- [ ] Hay puente hacia la sesión siguiente.
- [ ] Se ha revisado manualmente cualquier imagen, diagrama o dato generado.
