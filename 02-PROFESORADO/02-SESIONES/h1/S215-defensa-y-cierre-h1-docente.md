# S215 — Defensa y cierre de H1

| Dato | Valor |
|---|---|
| Hito | H1 — Primer asistente ejecutable |
| Duración prevista | 45 minutos |
| Fase HEXA del hito | Comunicar — evaluar y reflexionar |
| Modalidad combinada | Defensa **INDIVIDUAL**; ensayo y revisión por **PAREJAS**; review, retrospectiva y entrega en **EQUIPO** |

> Basada en `00-GUION-DOCENTE-H1-COMPLETO.md`.

## Finalidad del cierre

Al terminar, cada persona debe haber defendido una parte técnica de H1 mediante código y ejecución real. Cada equipo debe haber revisado su incremento, acordado una mejora concreta, comprobado sus enlaces y realizado la entrega oficial de H1 en Moodle.

La defensa tiene prioridad pedagógica sobre la preparación administrativa de la entrega.

## Antes de entrar en clase

- [ ] Preparar el orden breve de defensas y dejar visible qué hará el resto mientras espera.
- [ ] Abrir la tarea oficial de H1 en Moodle y verificar sus campos.
- [ ] Comprobar que se dispone de los enlaces a GitHub, README y, si corresponde, Scrum.
- [ ] Preparar una ventana privada o una cuenta distinta para comprobar permisos.
- [ ] Tener localizados el código y las pruebas sobre las que se defenderá.

## Apertura docente

Di en voz alta:

> Hoy cerramos H1. La defensa no es un castigo ni una exposición larga. Es la comprobación de que entendéis vuestro propio producto. Vais a señalar código, explicar, ejecutar, predecir y, cuando proceda, modificar algo pequeño. Mientras realizo defensas, el resto ensaya, revisa el incremento, hace retrospectiva y prepara la entrega.

## Organización simultánea de los 45 minutos

No organices la sesión como una única actividad para toda la clase. Mantén activas estas líneas de trabajo:

| Tiempo | Defensa docente | Trabajo paralelo del alumnado |
|---|---|---|
| 0–5 min | Explicar el protocolo y confirmar el orden. | Abrir código, README, Scrum y enlaces de entrega. |
| 5–15 min | Defensas individuales breves. | Ensayo y revisión por parejas: señalar, predecir, modificar y comprobar. |
| 15–28 min | Continuar defensas y recuperar respuestas vagas sobre el código. | Review del incremento y retrospectiva en equipo. |
| 28–38 min | Continuar defensas o una segunda comprobación breve cuando haga falta. | Preparar la entrega Moodle, revisar enlaces profundos y probar permisos. |
| 38–43 min | Resolver defensas pendientes sin convertirlas en exposiciones. | Un integrante realiza la entrega; el equipo verifica que abre correctamente. |
| 43–45 min | Cierre común y siguiente paso. | Reflexión individual breve y confirmación del cierre de equipo. |

Distribuye funciones dentro de cada equipo para que una defensa individual no detenga el review, la retrospectiva ni la entrega. El ensayo entre iguales prepara la defensa, pero no la sustituye.

## Defensa práctica individual

La defensa se realiza sobre código trabajado y con ejecución real. Debe ser breve: selecciona dos o tres comprobaciones adecuadas a lo que la persona ha construido, no todo el banco.

### Protocolo básico

```text
señalo → explico → ejecuto → compruebo
```

La persona:

1. señala una línea o fragmento concreto;
2. explica qué representa y qué hace;
3. ejecuta con una entrada o estado conocido;
4. contrasta el resultado con lo explicado.

Cuando la comprobación admite un cambio pequeño, utiliza:

```text
predigo → modifico → ejecuto → compruebo
```

La modificación puede ser un mensaje, un literal, el valor inicial de una variable o una entrada ficticia. No debe exigir contenido posterior a H1.

La defensa no es una presentación, un informe, un formulario ni una recitación del README. El producto del equipo no sustituye la comprensión individual.

## Banco de preguntas para seleccionar

Elige preguntas según el código de cada persona y la evidencia que necesites comprobar. No debe responderlas todas.

### Estructura y ejecución

- Señala dónde comienza la ejecución y explica el papel de `main`.
- Señala una instrucción que produzca salida y predice qué mostrará.
- ¿Qué prueba reproducible demuestra que esta parte funciona?

### Variables, constantes y literales

- Señala una variable y explica su tipo, nombre, valor actual y una posible reasignación.
- Señala una constante y justifica por qué ese dato no debe cambiar.
- Señala un literal e identifica su tipo.
- Cambia un literal o valor inicial sencillo y predice el efecto antes de ejecutar.

### Expresiones, operaciones y actualizaciones

- Señala una expresión u operación y explica de dónde sale el resultado.
- Si aparece una división, ¿esperas división entera o real? ¿Por qué?
- Si aparece `%`, ¿qué resto produce?
- Si aparece `+=`, `-=`, `++` o `--`, recorre el valor paso a paso.

### Entrada y conversiones

- Señala dónde se crea o reutiliza `Scanner`.
- ¿Qué devuelve `nextLine()` y dónde se almacena?
- Si el dato debe convertirse, señala el parseo y explica el tipo resultante.
- Explica qué entrada podría provocar un error de ejecución y por qué.
- Recorre el flujo desde teclado hasta el uso del dato en la salida.

### Comparaciones y decisiones

- Señala una comparación y predice su resultado para un valor concreto.
- Señala la condición de una decisión.
- Ejecuta o explica un caso que recorra la rama `true` y otro que recorra la rama `false`.
- Cambia un valor sencillo, predice qué rama se recorrerá y compruébalo.

### Alcance de H1

- ¿Qué hace MiniJarvis al cerrar H1?
- ¿Qué limitación conserva deliberadamente?
- ¿Qué idea queda fuera de H1 y corresponde trabajar más adelante?
- ¿Qué parte puedes explicar sin ayuda y cuál necesitas practicar todavía?

## Recuperación ante una defensa insuficiente

Si una respuesta es vaga, vuelve a una evidencia concreta:

1. pide señalar la línea;
2. aísla los valores y solicita una predicción;
3. ejecuta;
4. modifica un valor sencillo;
5. comprueba el nuevo resultado;
6. pide volver a explicar.

No sustituyas esta recuperación por una respuesta memorizada. Si persiste una laguna, registra para el seguimiento docente la persona, el concepto no defendido, la recuperación concreta y el momento de revisión.

## Ensayo y revisión por parejas

Mientras esperan su defensa, las parejas pueden:

- ensayar una explicación breve sobre una línea concreta;
- pedir que la otra persona señale el código del que habla;
- solicitar una predicción antes de ejecutar;
- proponer una modificación pequeña;
- ejecutar y contrastar el resultado;
- comprobar que ambas personas entienden lo que explican;
- revisar mutuamente enlaces profundos y permisos.

No preparan respuestas idénticas. La finalidad es descubrir lagunas y mejorar la explicación antes de la defensa docente individual.

## Review del incremento H1 — EQUIPO

El equipo revisa el incremento real, no una lista de documentos. Debe poder responder brevemente:

- ¿Qué hace MiniJarvis al finalizar H1?
- ¿Qué estaba previsto para el hito?
- ¿Qué funciona realmente?
- ¿Qué pruebas reproducibles lo demuestran?
- ¿Qué límites conserva?
- ¿Qué queda deliberadamente fuera?

La revisión utiliza el repositorio, el README y las pruebas existentes. No crea un informe adicional.

## Retrospectiva H1 — EQUIPO

La retrospectiva identifica una mejora aplicable a H2. Utiliza cuatro preguntas:

- ¿Qué ayudó al equipo?
- ¿Qué dificultó el trabajo?
- ¿Qué conviene mantener?
- ¿Qué conviene cambiar en H2?

El equipo acuerda al menos una mejora concreta y realizable. La decisión o mejora real queda en la retrospectiva Scrum; no se crea un informe paralelo.

## Reflexión individual

Pide una reflexión breve, oral o de trabajo:

- ¿Qué puedo hacer ya sin ayuda?
- ¿Qué necesito practicar?
- ¿Qué evidencia demuestra mi aprendizaje?
- ¿Cuál es mi siguiente paso en H2?

Solo se conserva en el diario si contiene un aprendizaje, dificultad, decisión o siguiente paso significativo. No se crea una fila S215 por rutina.

## Entrega oficial Moodle y evidencias que permanecen

S215 contiene la única entrega oficial de H1. Si no está en la tarea Moodle de H1, no está entregado oficialmente.

### Contenido de la entrega

Pega enlaces profundos, no carpetas genéricas, e incluye únicamente los campos canónicos:

```text
Equipo:
Integrantes:

Repositorio GitHub:
README H1:
Scrum equipo H1, si corresponde:

Permisos comprobados: sí/no
Observaciones o bloqueo pendiente:
```

Añade la confirmación:

```text
Confirmo que los enlaces llevan a evidencias concretas de H1 y que he comprobado los permisos de acceso.
```

- **GitHub y README:** localizan el código, las pruebas reproducibles y la explicación técnica.
- **Scrum:** se enlaza solo cuando la tarea lo necesita para localizar review, retrospectiva, una decisión, un cambio o un bloqueo real.
- **Diario individual:** se usa solo para aprendizaje o siguiente paso significativo; no forma parte rutinaria de la entrega.
- **Moodle:** contiene la entrega oficial breve con los enlaces canónicos y la confirmación de permisos.
- **Site:** no se actualiza ni se enlaza en S215; H1 podrá seleccionarse posteriormente durante C1.
- **Drive:** no sustituye GitHub ni README y no se usa para copiar código o ejecución rutinaria.

No se adjuntan capturas, formularios, portfolios, documentos de ejecución ni copias separadas de pruebas cuando GitHub y README ya permiten localizarlas.

### Comprobación de enlaces y permisos

Antes de enviar:

1. abre cada enlace profundo, no solo la carpeta o página inicial;
2. pruébalo en una ventana privada, con otra cuenta o mediante otra persona;
3. comprueba que el repositorio y el README son accesibles;
4. verifica el enlace a Scrum únicamente si se incluye;
5. marca `Permisos comprobados: sí` solo después de la prueba.

Esta comprobación es una acción, no un documento nuevo.

## Observación docente

Durante la defensa y el trabajo paralelo, observa específicamente:

- que la persona demuestra autoría y comprensión individual;
- que localiza en el código aquello que explica;
- que formula una predicción concreta;
- que explica valores, tipos, operaciones o condiciones con precisión suficiente;
- que realiza una modificación sencilla cuando procede;
- que ejecuta y contrasta el resultado;
- que distingue lo logrado en H1 de contenidos posteriores;
- que identifica qué necesita practicar después;
- que el equipo fundamenta la review en pruebas existentes;
- que la retrospectiva produce una mejora concreta;
- que los enlaces entregados son profundos y accesibles.

## Andamiaje durante la defensa

No des la explicación en lugar del alumnado. Utiliza la ayuda mínima:

- **Respuesta vaga:** pide volver a una línea concreta.
- **No sabe predecir:** aísla los valores y la expresión antes de ejecutar.
- **No sabe explicar una variable:** pide tipo, nombre, valor actual y posible cambio.
- **No entiende una decisión:** prueba un valor para cada rama y pide anticipar el recorrido.
- **No sabe explicar la entrada:** recorre teclado → `String` → conversión, si procede → uso.
- **No justifica una constante:** pregunta qué ocurriría si cambiara durante la ejecución.
- **Dice solo «funciona»:** pide entrada, salida esperada, salida obtenida y lugar donde se comprueba.
- **Se bloquea:** permite un ensayo breve y vuelve después a la defensa individual.

## Cierre de H1

Pregunta a cada persona:

> ¿Qué evidencia demuestra mejor tu aprendizaje en H1 y qué necesitas mejorar primero en H2?

Cierra en voz alta:

> H1 queda cerrado con código y pruebas localizables, comprensión individual defendida, review y retrospectiva reales y entrega oficial en Moodle. Hemos comunicado lo aprendido sin duplicar evidencias ni convertir el cierre en burocracia.

## Al terminar

Registra solo lo necesario para la continuidad: defensa pendiente, concepto no defendido, recuperación acordada, enlace inaccesible, bloqueo real o mejora que deba retomarse en H2.
