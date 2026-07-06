# Enunciados y entregables para el alumnado

## Programación + Entornos de Desarrollo — 1.º DAW — Curso 2026/2027

Versión: borrador 0.1
Documento complementario: `04B-modelo-entregables-laura.md`

---

## 1. Propósito

Este documento contiene los enunciados finales que recibirá el alumnado en cada hito del proyecto anual.

Proyecto guía:

> Construcción progresiva de un pequeño agente IA propio.

Cada hito indica:

- qué debe hacer el alumnado;
- qué debe entregar;
- relación con Programación;
- relación con Entornos de Desarrollo;
- uso permitido de IA;
- defensa oral prevista.

El modelo de entrega de Laura se separa en otro documento para evitar que el alumnado lo interprete como solución directa.

---

## 2. Criterios comunes para todos los entregables

Todo entregable evaluable debe dejar claro:

1. Qué se entrega.
2. Quién lo entrega: equipo o individual.
3. Dónde se entrega: Moodle, GitHub o formato mixto.
4. Qué evidencias mínimas debe contener.
5. Qué parte corresponde a Programación.
6. Qué parte corresponde a Entornos de Desarrollo.
7. Si se ha usado IA, cómo se registra.
8. Qué se puede preguntar en defensa oral.

Estructura mínima recomendada de repositorio:

```text
nombre-hito/
├── README.md
├── src/
│   └── ...
├── docs/
│   ├── portfolio.md
│   ├── registro-ia.md
│   ├── pruebas.md
│   └── retrospectiva.md
└── .gitignore
```

En hitos iniciales no hace falta que exista todo. La estructura crece progresivamente.

---

## 3. H0 — Bootcamp Scrum: torre de papel

### Enunciado para el alumnado

Durante esta actividad vais a vivir un sprint Scrum completo construyendo una torre de papel.

No se trata solo de construir la torre más alta. El objetivo principal es aprender a organizar el trabajo como equipo: definir roles, crear un backlog, planificar, ejecutar, revisar el resultado y hacer una retrospectiva.

Después conectaremos lo aprendido con el proyecto anual: construir progresivamente un pequeño agente IA propio.

### Qué debe hacer el equipo

1. Formar un equipo de 3-4 personas.
2. Asignar roles adaptados:
   - facilitador/a;
   - responsable de backlog;
   - responsable técnico/a;
   - responsable de documentación y defensa.
3. Crear un backlog de tareas para construir la torre.
4. Construir la torre en el tiempo indicado.
5. Presentar el resultado.
6. Hacer retrospectiva.
7. Traducir lo aprendido al proyecto del agente IA.

### Qué debe entregar el alumnado

| Entregable | Responsable | Formato |
|---|---|---|
| Contrato de equipo | Equipo | Markdown/PDF/Moodle |
| Tablero Scrum inicial | Equipo | Captura/foto/enlace |
| Retrospectiva | Equipo + reflexión individual | Markdown |
| Glosario Scrum mínimo | Individual o equipo | Markdown |
| Primer backlog del agente IA | Equipo | Markdown/tablero |

### Relación con módulos

Programación:

- diagnóstico inicial de resolución de problemas;
- preparación del proyecto del agente.

Entornos:

- ED RA1.b: fases de desarrollo;
- ED RA1.g: metodologías ágiles.

### Uso de IA

No es necesaria. Si se usa para preguntar qué es Scrum, debe registrarse brevemente.

### Defensa

Cada equipo deberá explicar:

- qué rol asumió cada persona;
- cómo organizaron el backlog;
- qué salió mal;
- qué cambiarían en un segundo sprint;
- cómo aplicarán Scrum al proyecto del agente IA.

---

## 4. H1 — Primer asistente básico

### Enunciado para el alumnado

Vais a crear la primera versión de vuestro asistente por consola en Java.

Debe ser una versión muy sencilla. Todavía no debe tener menú, bucles, `switch`, comandos avanzados ni inteligencia artificial real.

El objetivo es demostrar que comprendéis la estructura básica de un programa Java, el uso de variables, constantes, entrada por teclado y salida por pantalla.

### Qué debe hacer el alumnado

1. Crear un proyecto Java en IntelliJ.
2. Crear una clase `Main`.
3. Mostrar un saludo inicial.
4. Pedir el nombre de la persona usuaria.
5. Guardar el nombre en una variable.
6. Usar al menos una constante.
7. Mostrar varios mensajes relacionados con el futuro agente IA.
8. Preparar un README con instrucciones de ejecución.
9. Subir el proyecto a GitHub o entregarlo en formato alternativo si hay problemas.

### Qué debe entregar el alumnado

| Entregable | Responsable | Formato |
|---|---|---|
| Código Java básico | Equipo o individual, según organización | `src/Main.java` |
| README de ejecución | Equipo | `README.md` |
| Evidencia de ejecución | Equipo | Captura o bloque de salida |
| Portfolio H1 | Individual | `docs/portfolio-h1.md` |
| Registro de IA, si se usa | Individual | `docs/registro-ia.md` |

### Relación con módulos

Programación:

- PR RA1;
- PR RA2 inicial.

Entornos:

- ED RA1: relación entre programa, sistema, fuente y ejecutable;
- ED RA2: uso de IntelliJ y proyecto inicial.

### Uso de IA

Permitido en verde para:

- pedir explicación de conceptos;
- preguntar qué es `Scanner`;
- preguntar qué es `final`;
- pedir ejemplos pequeños que luego se adapten.

No permitido:

- entregar un programa completo generado por IA que no puedas explicar.

### Defensa

Preguntas posibles:

- ¿Dónde empieza el programa?
- ¿Qué variable guarda el nombre?
- ¿Qué constante has usado?
- ¿Qué hace `Scanner`?
- ¿Cómo se ejecuta desde IntelliJ?
- ¿Por qué todavía no hay menú?

---

## 5. H2 — Agente con decisiones y depuración

### Enunciado para el alumnado

Vais a evolucionar vuestro asistente básico para convertirlo en un agente con menú de comandos.

Ahora sí trabajaréis estructuras de control: decisiones, repetición, gestión de entradas no válidas y salida controlada del programa.

También aprenderéis a probar y depurar el programa usando IntelliJ.

### Qué debe hacer el alumnado

1. Añadir un menú de comandos.
2. Permitir que el programa siga funcionando hasta escribir `salir`.
3. Implementar al menos estos comandos:
   - `ayuda`;
   - `saluda`;
   - `estado`;
   - `salir`.
4. Gestionar comandos desconocidos.
5. Crear una tabla de pruebas manuales.
6. Documentar al menos una incidencia o error encontrado.
7. Usar el depurador de IntelliJ con un breakpoint.
8. Realizar en casa una comparación Java ↔ Python del menú.

### Qué debe entregar el alumnado

| Entregable | Responsable | Formato |
|---|---|---|
| Código Java con menú | Equipo | GitHub |
| Plan de pruebas | Equipo | `docs/pruebas-h2.md` |
| Informe de depuración | Individual/equipo | `docs/depuracion-h2.md` |
| Registro de incidencia | Equipo | GitHub issue o Markdown |
| Comparación Java ↔ Python | Individual, casa | `docs/comparacion-java-python-h2.md` |
| Registro de IA | Individual | `docs/registro-ia.md` |

### Relación con módulos

Programación:

- PR RA3;
- refuerzo PR RA1/RA2.

Entornos:

- ED RA3: pruebas, depuración e incidencias.

### Uso de IA

Permitido:

- pedir ayuda para entender errores;
- pedir ejemplos de casos de prueba;
- generar una versión Python para comparar.

Obligatorio:

- registrar el uso;
- verificar el resultado;
- poder explicar el código.

### Defensa

Preguntas posibles:

- ¿Cómo se repite el menú?
- ¿Qué ocurre si escribo un comando incorrecto?
- ¿Dónde pusiste el breakpoint?
- ¿Qué variable observaste en depuración?
- ¿Qué diferencia viste entre Java y Python?

---

## 6. H3 — Agente con memoria en colecciones

### Enunciado para el alumnado

Vais a añadir memoria temporal al agente.

El agente deberá recordar información durante la ejecución: mensajes escritos, comandos usados o preferencias simples.

El objetivo es aprender a elegir y usar estructuras de datos adecuadas.

### Qué debe hacer el alumnado

1. Elegir una estructura de datos adecuada: lista, mapa u otra colección.
2. Guardar información durante la ejecución.
3. Permitir consultar la memoria.
4. Añadir al menos un caso límite.
5. Crear pruebas de memoria.
6. Documentar por qué elegisteis esa colección.
7. Realizar en casa comparación Java ↔ Python: `ArrayList`/`HashMap` frente a `list`/`dict`.

### Qué debe entregar el alumnado

| Entregable | Responsable | Formato |
|---|---|---|
| Código con memoria temporal | Equipo | GitHub |
| README actualizado | Equipo | Markdown |
| Pruebas de memoria | Equipo | `docs/pruebas-memoria-h3.md` |
| Justificación de colección | Individual/equipo | Markdown |
| Comparación Java ↔ Python | Individual, casa | Markdown + código si procede |
| Portfolio H3 | Individual | Markdown |
| Registro IA | Individual/equipo | Markdown |

### Relación con módulos

Programación:

- PR RA6;
- refuerzo PR RA3.

Entornos:

- ED RA3: casos de prueba, incidencias y pruebas iniciales.

### Defensa

Preguntas posibles:

- ¿Qué colección has usado y por qué?
- ¿Cómo recorres la memoria?
- ¿Qué ocurre si la memoria está vacía?
- ¿Qué cambia entre Java y Python?

---

## 7. H4 — Agente orientado a objetos

### Enunciado para el alumnado

Vais a rediseñar vuestro agente usando programación orientada a objetos.

El objetivo es dejar de tener todo el código concentrado en `Main` y empezar a repartir responsabilidades entre clases.

También crearéis diagramas que expliquen el diseño.

### Qué debe hacer el alumnado

1. Identificar clases necesarias para el agente.
2. Crear clases con responsabilidades claras.
3. Usar atributos, métodos y constructores.
4. Aplicar visibilidad adecuada.
5. Crear un diagrama de clases.
6. Crear al menos un diagrama de comportamiento.
7. Relacionar los diagramas con el código real.
8. Realizar comparación Java ↔ Python de clases y objetos en casa.

### Qué debe entregar el alumnado

| Entregable | Responsable | Formato |
|---|---|---|
| Código Java organizado en clases | Equipo | GitHub |
| Diagrama de clases | Equipo | Mermaid/PlantUML/draw.io |
| Diagrama de comportamiento | Equipo | Mermaid/PlantUML/draw.io |
| Documento diagrama-código | Equipo | Markdown |
| Comparación Java ↔ Python | Individual, casa | Markdown |
| Defensa de diseño | Individual | Oral |
| Registro IA | Individual/equipo | Markdown |

### Relación con módulos

Programación:

- PR RA4;
- refuerzo PR RA2.

Entornos:

- ED RA5: diagramas de clases;
- ED RA6: diagramas de comportamiento.

### Defensa

Preguntas posibles:

- ¿Qué responsabilidad tiene cada clase?
- ¿Qué clase no debería saber demasiado?
- ¿Qué relación del diagrama aparece en el código?
- ¿Qué diferencia hay entre constructor Java y `__init__` en Python?

---

## 8. H5 — Agente extensible, código limpio y patrones iniciales

### Enunciado para el alumnado

Vais a mejorar el diseño del agente para que pueda incorporar herramientas internas.

El objetivo no es usar patrones por usarlos, sino detectar cuándo el código empieza a necesitar una estructura más clara.

Trabajaréis refactorización, revisión de código, Git profesional y, si procede, algún patrón sencillo como Command, Strategy o Factory.

### Qué debe hacer el alumnado

1. Detectar una parte del código que pueda mejorar.
2. Refactorizar con una justificación clara.
3. Añadir herramientas internas al agente.
4. Usar ramas, commits claros y revisión de código.
5. Documentar un patrón si se usa.
6. Comparar Java ↔ Python en casa.

### Qué debe entregar el alumnado

| Entregable | Responsable | Formato |
|---|---|---|
| Código con herramientas extensibles | Equipo | GitHub |
| Evidencia de ramas/PR/revisión | Equipo | GitHub o Markdown |
| Informe de refactorización | Equipo | Markdown |
| Registro de patrón, si se usa | Equipo | Markdown |
| Comparación Java ↔ Python | Individual, casa | Markdown |
| Portfolio H5 | Individual | Markdown |
| Registro IA | Individual/equipo | Markdown |

### Relación con módulos

Programación:

- PR RA7 no imprescindible/evaluable;
- refuerzo PR RA4/RA6.

Entornos:

- ED RA4;
- ED RA6 si se usan diagramas de estados o comportamiento.

### Defensa

Preguntas posibles:

- ¿Qué problema tenía el código antes?
- ¿Qué refactorización hiciste?
- ¿Por qué usaste o no usaste un patrón?
- ¿Qué evidencia hay en GitHub?

---

## 9. H6 — Agente persistente y trazable

### Enunciado para el alumnado

Vais a hacer que el agente pueda guardar y recuperar información.

El agente debe dejar de depender solo de la memoria temporal y empezar a trabajar con ficheros, logs o una pequeña base de conocimiento.

También debéis preparar una ejecución reproducible y cuidar la seguridad: nada de datos personales ni secretos.

### Qué debe hacer el alumnado

1. Guardar información en fichero.
2. Recuperar información al iniciar o mediante comando.
3. Crear logs o historial simple.
4. Documentar cómo se ejecuta el proyecto.
5. Añadir pruebas de persistencia.
6. Preparar Docker guiado si procede.
7. Comparar Java ↔ Python en casa.
8. Revisar que no se suben secretos ni datos personales.

### Qué debe entregar el alumnado

| Entregable | Responsable | Formato |
|---|---|---|
| Código con persistencia | Equipo | GitHub |
| Ficheros de ejemplo sin datos personales | Equipo | Carpeta `data/` o similar |
| README reproducible | Equipo | Markdown |
| Pruebas de persistencia | Equipo | Markdown/tests |
| Registro de decisiones de seguridad | Equipo | Markdown |
| Comparación Java ↔ Python | Individual, casa | Markdown |
| Registro IA | Individual/equipo | Markdown |

### Relación con módulos

Programación:

- PR RA5;
- PR RA8/RA9 si procede como ampliación.

Entornos:

- ED RA3;
- ED RA4.

### Defensa

Preguntas posibles:

- ¿Dónde se guarda la información?
- ¿Qué ocurre si el fichero no existe?
- ¿Qué datos no deberías guardar?
- ¿Cómo puedo ejecutar tu proyecto desde cero?

---

## 10. H7 — Integración IA responsable o simulación robusta

### Enunciado para el alumnado

Vais a preparar una integración responsable con Gemini/Jarvis o una simulación robusta si el grupo no está preparado para trabajar con una integración real.

El objetivo no es que la IA haga el proyecto, sino aprender a controlar, validar y documentar el uso de IA.

### Qué debe hacer el alumnado

1. Definir un caso de uso concreto para IA.
2. Preparar prompts o entradas controladas.
3. Evitar datos personales y secretos.
4. Validar la respuesta humana y técnicamente.
5. Registrar uso, riesgos y limitaciones.
6. Comparar Java ↔ Python en casa si procede.

### Qué debe entregar el alumnado

| Entregable | Responsable | Formato |
|---|---|---|
| Integración o simulación IA | Equipo | Código + README |
| Registro de prompts | Individual/equipo | Markdown |
| Documento de riesgos | Equipo | Markdown |
| Documento de configuración segura | Equipo | Markdown |
| Comparación Java ↔ Python | Individual, casa | Markdown |
| Defensa IA responsable | Individual | Oral |

### Relación con módulos

Programación:

- consolidación PR RA1-RA6;
- PR RA7/RA8/RA9 si procede.

Entornos:

- ED RA3;
- ED RA4;
- seguridad, documentación, configuración y validación.

### Defensa

Preguntas posibles:

- ¿Qué datos recibe la IA?
- ¿Qué no debe recibir nunca?
- ¿Cómo validaste la respuesta?
- ¿Qué harías si la IA entra en bucle o genera errores?
- ¿Qué parte puedes explicar sin ayuda?

---

## 11. HF — Presentación final, recuperación y mejora

### Enunciado para el alumnado

Vais a cerrar el proyecto, preparar una defensa final y completar o recuperar evidencias pendientes.

Cada persona debe poder explicar qué ha aprendido, qué ha aportado y qué partes del proyecto puede defender técnicamente.

### Qué debe entregar el alumnado

| Entregable | Responsable | Formato |
|---|---|---|
| Portfolio final | Individual | Markdown/GitHub o mixto |
| Demo final | Equipo | Ejecución + presentación |
| Defensa individual | Individual | Oral |
| Recuperación específica | Individual | Según RA pendiente |
| Registro IA final | Individual | Markdown |
