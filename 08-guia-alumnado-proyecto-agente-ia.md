# Guía del alumnado — Proyecto Agente IA

## Programación + Entornos de Desarrollo — 1.º DAW — Curso 2026/2027

Versión: borrador 0.1

Documentos relacionados:

- `00-mapa-maestro-curso-2026-2027.md`
- `02-calendario-hitos-sprints-2026-2027.md`
- `04A-enunciados-y-entregables-alumnado.md`
- `05-politica-uso-ia-semaforo-registro-defensa.md`
- `06-rubricas-hitos.md`
- `07-plantillas-entregables.md`
- carpeta `plantillas/`

---

## 1. Qué vamos a hacer durante el curso

Durante el curso vais a construir poco a poco un pequeño agente IA propio.

No empezaremos usando inteligencia artificial real desde el primer día. Primero aprenderemos las bases necesarias para poder construir, entender, probar y defender el proyecto.

La idea general es esta:

> Seremos equipos de desarrollo que construyen, documentan, prueban y defienden un asistente inteligente propio, usando Java, herramientas profesionales, Scrum e IA responsable.

El proyecto se llama de forma orientativa:

```text
MiniJarvis
```

Al final del curso, el proyecto podrá tener:

- un agente por consola en Java;
- comandos o herramientas internas;
- memoria temporal;
- clases y objetos bien organizados;
- pruebas y depuración;
- documentación clara;
- uso de Git/GitHub;
- diagramas;
- persistencia en ficheros o base de conocimiento simple;
- registro de uso de IA;
- defensa individual;
- integración real con Gemini/Jarvis o simulación robusta, si el grupo llega preparado.

Lo importante no es que la IA “haga” el proyecto.

Lo importante es que aprendáis a construir software, verificarlo, explicarlo y usar IA con criterio.

---

## 2. Cómo se trabaja por hitos

El curso se organiza por hitos. Cada hito añade una capacidad nueva al agente.

Un hito es una entrega parcial con un objetivo claro.

No se espera que el proyecto final aparezca de golpe. Se irá construyendo por versiones.

| Hito | Fechas orientativas | Qué construiremos |
|---|---|---|
| H0. Bootcamp Scrum | 15-18 septiembre | Aprenderemos Scrum con la torre de papel y prepararemos equipos, roles y tablero. |
| H1. Primer asistente básico | 21 septiembre - 9 octubre | Programa Java básico por consola: saludo, nombre, variables, constantes y README. |
| H2. Decisiones y depuración | 13 octubre - 6 noviembre | Agente con menú, comandos, bucles, gestión de errores, pruebas y depuración. |
| H3. Memoria en colecciones | 9 noviembre - 4 diciembre | Agente que recuerda información durante la ejecución usando colecciones. |
| C1. Cierre 1.ª evaluación | 9-22 diciembre | Demo parcial, portfolio, revisión de evidencias y recuperación si procede. |
| H4. Agente orientado a objetos | 7 enero - 5 febrero | Rediseño con clases, objetos, responsabilidades y diagramas UML. |
| H5. Herramientas, código limpio y patrones iniciales | 8 febrero - 19 marzo | Agente extensible, refactorización, Git profesional y patrones si tienen sentido. |
| C2. Cierre 2.ª evaluación | 29-31 marzo | Demo parcial, revisión de repositorio, defensa y recuperación. |
| H6. Persistencia y trazabilidad | 1-23 abril | Ficheros, logs, base de conocimiento simple, README reproducible y seguridad. |
| H7. IA responsable opcional | 26-29 abril | Integración con Gemini/Jarvis o simulación robusta y defendible. |
| FFEOE | 30 abril - 28 mayo | No hay clases ni entregas. El proyecto base debe quedar cerrado antes. |
| HF. Presentación final | 31 mayo - 22 junio | Defensa final, portfolio final, demo, recuperación y mejora. |

Cada hito tendrá:

1. una explicación del reto;
2. una lista de tareas;
3. entregables concretos;
4. relación con Programación;
5. relación con Entornos de Desarrollo;
6. normas de uso de IA;
7. defensa oral o revisión técnica.

---

## 3. Qué se entrega

Las entregas combinan trabajo de equipo y trabajo individual.

### 3.1. Entregas de equipo

Normalmente el equipo entregará:

- código del proyecto;
- repositorio GitHub o entrega equivalente;
- README;
- pruebas o checklist;
- documentación técnica;
- diagramas cuando correspondan;
- evidencias de tablero, roles o Scrum;
- informes de depuración, incidencias o refactorización;
- registro de decisiones técnicas;
- demo del producto.

### 3.2. Entregas individuales

Cada persona deberá entregar o defender evidencias propias, por ejemplo:

- portfolio individual;
- registro de uso de IA;
- comparación Java ↔ Python;
- reflexión de aprendizaje;
- defensa de una parte del código;
- explicación de una decisión técnica;
- recuperación individual si algún RA queda pendiente.

### 3.3. Estructura recomendada del repositorio

La estructura crecerá poco a poco. Una estructura orientativa será:

```text
hN-nombre-del-hito/
├── README.md
├── src/
│   └── ...
├── docs/
│   ├── portfolio.md
│   ├── registro-ia.md
│   ├── pruebas.md
│   ├── depuracion.md
│   ├── retrospectiva.md
│   ├── comparacion-java-python.md
│   └── decisiones-tecnicas.md
└── .gitignore
```

En los primeros hitos no hará falta tener todos los archivos. Se añadirán cuando tengan sentido.

---

## 4. Qué se espera en cada entrega

Una entrega válida debe permitir comprobar tres cosas:

1. Que el producto funciona o se puede revisar.
2. Que el proceso está documentado.
3. Que cada alumno/a puede explicar lo que ha entregado.

Por eso, no basta con subir código.

Una buena entrega debe incluir:

- instrucciones para ejecutar;
- explicación de qué se ha implementado;
- pruebas realizadas;
- errores encontrados y cómo se han corregido;
- evidencias de Git o del proceso de trabajo;
- registro de uso de IA, si se ha usado;
- indicación de qué sabe defender cada integrante.

Regla práctica:

```text
Si no se puede ejecutar, revisar o defender, la evidencia queda incompleta.
```

---

## 5. Cómo se usa IA en este curso

La IA está permitida porque forma parte del trabajo profesional actual.

Pero se usará con reglas claras.

La IA puede ayudarte a:

- entender conceptos;
- pedir ejemplos pequeños;
- revisar errores;
- preparar pruebas;
- mejorar documentación;
- comparar Java con Python;
- proponer mejoras;
- preparar una defensa;
- revisar un README o portfolio.

La IA no puede sustituir tu aprendizaje.

Regla básica:

```text
Puedes usar IA como copiloto, tutor o revisor.
No puedes usarla como autor oculto de tu entrega.
```

### 5.1. Semáforo de IA

| Color | Significado | Ejemplos |
|---|---|---|
| Verde | Permitido y recomendado | Pedir explicaciones, entender errores, revisar claridad, pedir ejemplos pequeños, generar preguntas de repaso. |
| Amarillo | Permitido con registro, verificación y defensa | Generar fragmentos de código, proponer tests, refactorizar, traducir Java a Python, sugerir diagramas o patrones. |
| Rojo | No permitido | Copiar una solución completa sin entenderla, ocultar uso de IA, usar IA en pruebas no autorizadas, introducir datos personales, subir secretos o claves. |

### 5.2. Registro obligatorio

Si usas IA en una entrega evaluable, debes registrarlo.

Archivo recomendado:

```text
docs/registro-ia.md
```

El registro debe explicar:

- herramienta usada;
- fecha;
- objetivo;
- prompt o resumen fiel;
- resultado obtenido;
- qué aceptaste;
- qué modificaste tú;
- cómo lo verificaste;
- qué aprendiste;
- riesgos o errores detectados.

### 5.3. Seguridad

Nunca debes introducir en una IA ni subir a GitHub:

- contraseñas;
- tokens;
- claves API;
- archivos `.env` reales;
- datos personales;
- datos de compañeros/as;
- credenciales de GitHub, Moodle, Gemini o Jarvis.

Si hace falta simular datos, se usarán datos ficticios.

Ejemplo permitido:

```text
API_KEY_EJEMPLO
usuario_prueba
mensaje de ejemplo sin datos personales
```

---

## 6. Cómo se evalúa

La evaluación se apoya en Resultados de Aprendizaje y Criterios de Evaluación de Programación y Entornos de Desarrollo.

Aunque el proyecto sea común, los módulos se evalúan por separado.

Una misma evidencia puede servir para ambos módulos, pero se mirará desde puntos de vista distintos.

Por ejemplo:

- un menú en Java puede servir para Programación porque demuestra estructuras de control;
- el plan de pruebas del mismo menú puede servir para Entornos;
- una defensa puede confirmar si la evidencia grupal también demuestra aprendizaje individual.

### 6.1. Qué se valora

Se valorará especialmente:

- funcionamiento técnico;
- ajuste al hito;
- código limpio y comprensible;
- documentación;
- pruebas y verificación;
- uso de Git/GitHub y trazabilidad;
- uso responsable de IA;
- defensa oral;
- capacidad de corregir errores;
- mejora progresiva.

### 6.2. Rúbrica común

La escala general será:

| Nivel | Significado |
|---|---|
| 4 — Excelente | Cumple lo pedido con autonomía, claridad, calidad técnica y defensa sólida. |
| 3 — Adecuado | Cumple los requisitos principales con pequeños errores o aspectos mejorables. |
| 2 — Básico | Cumple parcialmente, pero necesita revisión o mejora. |
| 1 — Insuficiente | No cumple lo esencial, falta evidencia o no puede defenderse. |

Importante:

```text
Una entrega con buena apariencia técnica puede no ser válida si el alumno/a no puede explicarla, modificarla o defenderla.
```

---

## 7. Cómo usar las plantillas

Las plantillas están en dos lugares:

1. Documento general:

```text
07-plantillas-entregables.md
```

2. Carpeta de plantillas individuales:

```text
plantillas/
```

Plantillas disponibles:

| Plantilla | Para qué sirve |
|---|---|
| `README-template.md` | Explicar qué hace el proyecto y cómo se ejecuta. |
| `portfolio-template.md` | Reflexionar individualmente sobre aportaciones y aprendizaje. |
| `registro-ia-template.md` | Declarar y analizar el uso de IA. |
| `pruebas-template.md` | Diseñar y registrar pruebas. |
| `depuracion-template.md` | Documentar un proceso de depuración. |
| `incidencia-template.md` | Registrar errores o problemas detectados. |
| `retrospectiva-template.md` | Revisar cómo ha trabajado el equipo. |
| `comparacion-java-python-template.md` | Comparar una solución Java con Python. |
| `decision-tecnica-template.md` | Justificar una decisión técnica. |
| `patron-diseno-template.md` | Registrar un patrón usado o descartado. |
| `seguridad-datos-template.md` | Revisar riesgos de datos, secretos y configuración. |
| `defensa-individual-template.md` | Preparar la defensa técnica individual. |

### 7.1. Cómo copiar una plantilla

Para cada hito, copia solo las plantillas necesarias dentro de `docs/` y cambia el nombre para que se entienda.

Ejemplo para H2:

```text
docs/pruebas-h2.md
docs/depuracion-h2.md
docs/registro-ia.md
docs/comparacion-java-python-h2.md
```

### 7.2. Qué hacer si un apartado no aplica

No borres apartados importantes sin más.

Si algo no aplica, escribe:

```text
No aplica en este hito porque...
```

Esto ayuda a diferenciar entre:

- algo que no era necesario;
- algo que se ha olvidado.

---

## 8. Qué se espera en las defensas

Habrá defensas orales, revisiones técnicas o preguntas individuales durante el curso.

La defensa sirve para comprobar comprensión, no para pillar a nadie.

Pero si una entrega ha usado IA o es grupal, la defensa es especialmente importante.

En una defensa se puede pedir:

- explicar una función;
- explicar una clase;
- justificar una colección;
- explicar un diagrama;
- ejecutar el proyecto;
- modificar una línea;
- detectar un error;
- explicar una prueba;
- justificar un uso de IA;
- comparar Java y Python;
- explicar qué parte hizo cada persona.

Preguntas típicas:

```text
¿Qué hace esta parte del código?
¿Por qué elegisteis esta solución?
¿Qué error encontrasteis y cómo lo corregisteis?
¿Qué parte generó o sugirió la IA?
¿Qué modificaste tú?
¿Cómo comprobaste que funcionaba?
¿Qué pasaría si cambio este valor?
¿Qué datos no debe recibir nunca una IA?
```

Cada integrante debe saber defender su aportación y una parte razonable del producto común.

---

## 9. Qué hacer si el equipo se bloquea

Bloquearse forma parte del aprendizaje.

Cuando aparezca un problema:

1. anotad qué ocurre;
2. intentad reproducirlo;
3. revisad el mensaje de error;
4. buscad una hipótesis;
5. usad depuración o pruebas;
6. pedid ayuda si el bloqueo continúa;
7. registrad la incidencia o el aprendizaje.

No se penaliza tener errores.

Sí puede afectar negativamente:

- ocultarlos;
- no probar nada;
- no documentar;
- entregar código que nadie entiende;
- decir “lo hizo la IA” sin poder explicarlo.

---

## 10. Checklist rápido antes de entregar

Antes de entregar un hito, revisad:

```text
[ ] El proyecto se puede abrir o ejecutar.
[ ] El README explica qué hace y cómo se ejecuta.
[ ] El código corresponde al nivel del hito.
[ ] Hay pruebas o checklist si se piden.
[ ] Hay evidencias de depuración, incidencias o decisiones si corresponden.
[ ] El portfolio individual está actualizado si se pide.
[ ] El registro de IA existe si se ha usado IA.
[ ] No hay datos personales ni secretos.
[ ] Cada integrante sabe qué parte puede defender.
[ ] La entrega está subida o preparada en el lugar indicado.
```

---

## 11. Idea final

Este curso no consiste solo en “hacer un programa”.

Consiste en aprender a trabajar como desarrolladores/as en formación:

- entender un problema;
- construir una solución paso a paso;
- usar herramientas profesionales;
- colaborar;
- probar;
- depurar;
- documentar;
- usar IA con responsabilidad;
- defender técnicamente lo aprendido.

La meta no es tener un agente perfecto.

La meta es que puedas decir:

```text
Sé qué he construido, sé cómo funciona, sé cómo lo he comprobado y puedo mejorarlo.
```
