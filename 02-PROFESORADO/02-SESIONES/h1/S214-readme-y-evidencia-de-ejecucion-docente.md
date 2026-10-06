# S214 — README, pruebas reproducibles y preparación del cierre

| Dato | Valor |
|---|---|
| Hito | H1 — Primer asistente ejecutable |
| Duración prevista | 45 minutos |
| Fase HEXA del hito | Comunicar — evaluar y reflexionar |
| Modalidad de trabajo | **INDIVIDUAL → EQUIPO → PAREJAS** |

> Basada en `00-GUION-DOCENTE-H1-COMPLETO.md`.

## Finalidad de la sesión

H1 debe quedar comprensible, reproducible, documentado, verificable y enlazable. La comprobación que orienta toda la sesión es:

> Otra persona debe poder entender, ejecutar y comprobar H1 sin depender de una explicación oral del equipo.

S214 prepara el cierre mediante documentación y pruebas accesibles. Documentar bien no sustituye la defensa práctica posterior.

## Antes de entrar en clase

- [ ] Abrir el repositorio y comprobar si ya existe un README H1: localizarlo o, si no existe, preparar su creación.
- [ ] Ejecutar el incremento para contrastar las instrucciones y los casos documentados.
- [ ] Preparar el modelo de README y de prueba reproducible.
- [ ] Comprobar cómo abrir un enlace técnico en ventana privada o mediante otra cuenta.
- [ ] Organizar el intercambio para que una persona externa pruebe la documentación sin explicación previa.

## Apertura docente

Di en voz alta:

> Hoy pasamos a Comunicar. Comunicar no es decorar el proyecto al final. Significa que otra persona puede entender qué hace H1, ejecutarlo, comprobar una prueba y reconocer sus límites sin que el equipo tenga que explicárselo paso a paso.

Contrasta dos afirmaciones:

```text
Funciona.
```

```text
Con esta entrada esperábamos este resultado; lo obtuvimos y eso demuestra este comportamiento concreto.
```

Pregunta:

> ¿Cuál de las dos permitiría a otra persona comprobar el proyecto y por qué?

## Qué debe comunicar el README de H1

El README debe responder claramente a cuatro preguntas:

```text
1. ¿Qué hace?
2. ¿Qué límites tiene?
3. ¿Cómo se ejecuta?
4. ¿Qué pruebas demuestran que funciona?
```

### Qué hace

Describe únicamente comportamientos presentes en el incremento. No atribuye a MiniJarvis memoria, ficheros, menú o inteligencia artificial si todavía no existen.

### Qué límites tiene

Explica de forma honesta lo que queda fuera de H1. Un límite bien documentado evita que la persona lectora espere capacidades que el programa no ofrece.

### Cómo se ejecuta

Da pasos concretos y ordenados. Deben permitir localizar el proyecto, ejecutar el punto de entrada e introducir datos ficticios sin depender de instrucciones orales.

### Qué pruebas demuestran que funciona

No basta con pegar una salida. Cada prueba debe indicar la entrada, lo esperado, lo obtenido y el comportamiento que permite verificar.

## Modelo pedagógico de README

Presenta este modelo como ejemplo de información necesaria, no como texto para copiar. El equipo debe ajustarlo al incremento que realmente tiene:

```markdown
# MiniJarvis H1

## Qué hace
MiniJarvis saluda, pide un nombre ficticio, calcula minutos a partir de horas y muestra el resultado booleano de comparar las horas con una referencia.

## Límites de H1
No incluye `if/else`, bifurcaciones, menú, memoria, ficheros ni IA real.

## Cómo ejecutar
1. Abrir el proyecto en IntelliJ.
2. Ejecutar `Main.java`.
3. Introducir datos ficticios.

## Pruebas
Caso A: horas = 5 -> minutos = 300; comparación `horas >= 4` = true.
Caso B: horas = 2 -> minutos = 120; comparación `horas >= 4` = false.
Entrada no convertible: "hola" falla durante la ejecución con parseInt.
```

Antes de aceptar una formulación, pregunta:

- ¿describe el programa real?
- ¿permite actuar o solo ofrece una descripción general?
- ¿se puede seguir sin haber estado en clase?
- ¿distingue capacidad actual y límite?

Los casos del modelo muestran dos resultados observables de una comparación, sin ramas, y una entrada no convertible. Solo deben documentarse como pruebas del equipo si esos comportamientos existen realmente en su incremento y pueden reproducirse. S214 no vuelve a enseñar comparación, `Scanner` o conversiones.

## Qué convierte una prueba en reproducible

Una prueba verificable permite seguir esta relación:

```text
entrada → resultado esperado → resultado obtenido → qué demuestra
```

Cuando ayude a localizarla, añade un enlace profundo al archivo, prueba o sección concreta del repositorio.

Modelo:

```text
Prueba:
Entrada usada:
Resultado esperado:
Resultado obtenido:
Demuestra:
Dónde comprobarlo:
```

Ejemplo de prueba:

```text
Prueba: saludo con nombre ficticio.
Entrada usada: Laura.
Salida esperada: Encantado, Laura.
Salida obtenida: Encantado, Laura.
Demuestra: la entrada leída se guarda y se usa en la salida.
Enlace: archivo, prueba o sección concreta del repositorio, no carpeta general.
```

Pregunta siempre:

> ¿Qué demuestra exactamente esta prueba?

Distingue:

- **ejecutar algo:** poner el programa en marcha;
- **observar un resultado:** registrar qué ocurrió;
- **explicar una prueba:** relacionar entrada, predicción, resultado y propiedad comprobada.

Una salida coincidente no demuestra cualquier afirmación. El equipo debe nombrar el comportamiento concreto que el caso recorre.

## Enlace profundo y permiso útil

Un enlace profundo lleva directamente al archivo, prueba o sección relevante. Un enlace a la raíz de una carpeta obliga a buscar y puede ocultar la evidencia importante.

Antes de considerar preparado un enlace:

1. abrirlo en ventana privada, si procede;
2. probarlo con una cuenta no propietaria, cuando sea viable, o pedir a otra persona que lo abra;
3. confirmar que lleva al recurso concreto;
4. confirmar que no depende de permisos exclusivos de la persona propietaria.

Principio:

> Un enlace que solo abre la persona propietaria no está preparado para una entrega.

Esta comprobación es una acción, no un documento nuevo.

## Actividad central

Ubicación común: `README H1 → raíz del repositorio GitHub`.

### Localización y comprensión — INDIVIDUAL

Sin crear una ficha, cada persona localiza el código y las pruebas disponibles y comprueba si existe el README. Si existe, sabe encontrarlo; si no existe, sabe que el equipo deberá crearlo en esa ubicación durante la consolidación. Después debe poder responder:

- ¿qué parte del programa puedo señalar?
- ¿qué prueba demuestra que funciona?
- ¿qué entrada se utilizó?
- ¿qué resultado se esperaba?
- ¿qué resultado se obtuvo?
- ¿qué demuestra esa prueba?
- ¿qué límite de H1 puedo explicar?

La persona no necesita memorizar el README. Debe saber encontrar la evidencia y comprenderla.

### Consolidación — EQUIPO

El equipo:

1. crea o completa el README en esa ubicación y lo contrasta con el incremento real;
2. completa qué hace y qué límites conserva;
3. prueba las instrucciones de ejecución;
4. documenta casos reproducibles;
5. relaciona cada caso con lo que demuestra;
6. añade enlaces profundos cuando faciliten la localización;
7. comprueba que no hay credenciales ni datos personales;
8. corrige aquello que una persona externa no podría comprender o reproducir.

No se escribe documentación para aparentar más alcance. Si una prueba falla o un comportamiento no existe, se corrige el programa o la afirmación antes de presentarlo como evidencia.

### Comprobación externa — PAREJAS

Una persona o pareja externa al trabajo utiliza la documentación sin explicación oral previa. Debe intentar:

1. abrir el enlace;
2. encontrar el README;
3. entender qué hace H1;
4. entender sus límites;
5. seguir las instrucciones de ejecución;
6. localizar las pruebas;
7. comprender qué demuestra al menos una prueba.

La persona autora observa y anota mentalmente dónde aparece el bloqueo, pero no dirige cada paso. Al terminar puede preguntar qué resultó ambiguo y corregirlo con el equipo.

La pregunta de control es:

> ¿Podría otra persona ejecutar y comprobar el proyecto siguiendo únicamente la documentación?

## Arquitectura de evidencias y límite de S214

- **GitHub:** fuente canónica para código, README, evolución técnica, pruebas localizables y enlaces técnicos.
- **Scrum:** solo registra una tarea, decisión, cambio, bloqueo o planificación real; no se actualiza para demostrar que ocurrió S214.
- **Diario individual:** únicamente si surge un aprendizaje, dificultad o decisión personal significativa; no se exige fila S214 ni revisión administrativa.
- **Drive:** solo para una evidencia excepcional no-code sin una ubicación más natural; no duplica código, consola, capturas, pruebas técnicas o README.
- **Sites:** no se crean ni actualizan durante H1. Una evidencia significativa podrá seleccionarse posteriormente durante C1.
- **Moodle:** S214 prepara enlaces, permisos y documentación; S215 realiza la entrega oficial de H1.

No se crea una evidencia de ejecución separada cuando las pruebas y su explicación ya están localizadas desde GitHub o README.

## Observación docente

Durante la sesión, comprueba específicamente si:

- cada persona sabe localizar una evidencia técnica;
- el equipo documenta lo que H1 hace realmente;
- los límites están expresados con honestidad;
- las instrucciones permiten ejecutar sin ayuda oral;
- las pruebas indican entrada, resultado esperado, resultado obtenido y significado;
- el README permite actuar y no solo leer una descripción;
- los enlaces conducen al recurso concreto;
- otra persona puede abrirlos;
- no aparecen credenciales ni datos personales;
- una persona explica qué demuestra una prueba;
- el equipo distingue documentación y defensa.

## Andamiaje ante bloqueos

No reescribas el README por el equipo. Utiliza una pregunta específica:

- **README demasiado vago:** «¿Podría ejecutarlo alguien que no estuvo en clase?»
- **Solo aparece “funciona”:** «¿Qué entrada usaste y qué demuestra el resultado?»
- **Prueba sin resultado esperado:** pide una predicción antes de aceptarla.
- **Enlace a una carpeta raíz:** pide el enlace al recurso concreto.
- **Enlace que solo abre la persona propietaria:** compruébalo desde otra sesión, cuenta o persona.
- **Documentación extensa pero no ejecutable:** pide pasos concretos y en orden.
- **Prueba que no demuestra lo afirmado:** pregunta qué comportamiento se está verificando.
- **La persona autora explica continuamente:** pídele que deje de intervenir y observe dónde se atasca la otra persona.

## Temporalización orientativa

| Tiempo | Acción |
|---|---|
| 0–5 min | Presentar el criterio de documentación reproducible y localizar individualmente las evidencias. |
| 5–10 min | Analizar el modelo de README y la diferencia entre “funciona” y una prueba explicada. |
| 10–18 min | Comprobación individual: localizar código, entrada, esperado, obtenido, significado y límite. |
| 18–30 min | Consolidar en equipo README, instrucciones, límites, pruebas y enlaces profundos. |
| 30–38 min | Intercambiar por parejas y probar la documentación sin explicación oral previa. |
| 38–42 min | Corregir bloqueos, enlaces y permisos descubiertos. |
| 42–45 min | Comprobar el cierre y preparar la transición hacia la defensa. |

## Transición a S215

Documentar no sustituye defender. La documentación preparada debe permitir encontrar rápidamente aquello que después habrá que señalar, explicar, ejecutar y comprobar.

Modelo de conexión:

```text
señalar → explicar → ejecutar → comprobar
```

Cuando proceda:

```text
predecir → modificar → ejecutar → comprobar
```

Pregunta de cierre:

> Si en la defensa te pido que señales una prueba, ejecutes, predigas una salida o modifiques una parte pequeña, ¿sabes dónde está y qué demuestra?

Como reflexión breve, sin crear una tarea adicional:

> ¿Qué evidencia de H1 podría ser suficientemente significativa como para seleccionarla posteriormente durante C1?

## Al terminar

Anota únicamente lo necesario para la continuidad docente: documentación que otra persona no pudo seguir, enlace inaccesible, prueba débil, persona que no localiza su evidencia o ajuste temporal para la próxima aplicación.
