# S211 — Constantes, literales, expresiones, operaciones y actualizaciones

| Dato | Valor |
|---|---|
| Hito | H1 — Primer asistente ejecutable |
| Duración prevista | 45 minutos |
| Fase HEXA del hito | Ejecutar — crear |
| Modalidad de trabajo | **INDIVIDUAL → PAREJAS** |

> Basada en `00-GUION-DOCENTE-H1-COMPLETO.md`.

## Qué vas a aprender

Al terminar, cada persona debe distinguir constante y variable, reconocer literales, predecir el valor y el tipo de una expresión, utilizar el resultado de una operación y seguir actualizaciones paso a paso. Los contrastes con división, precedencia y resto deben explicarse antes de ejecutarse.

## Antes de entrar en clase

- [ ] Abrir y ejecutar el proyecto o la micropráctica que utilizará el alumnado.
- [ ] Preparar los ejemplos para mostrarlos sin revelar inicialmente el resultado.
- [ ] Comprobar que la consola permite contrastar predicción y salida.
- [ ] Reservar el cierre para que cada persona explique de dónde procede un resultado.

## Apertura docente

Di en voz alta:

> Hoy entramos en Ejecutar. Ejecutar no significa escribir mucho código sin pensar. Significa construir, predecir, probar y explicar. Una operación no está comprobada solo porque el programa compile.

Pregunta inicial:

> Si dos datos empiezan siempre con el mismo valor, ¿son necesariamente constantes? ¿Qué tendríamos que saber sobre su función antes de decidirlo?

## Temporalización orientativa

| Tiempo | Acción |
|---|---|
| 0–4 min | Presentar la finalidad y activar la distinción entre constante y variable. |
| 4–12 min | Núcleo práctico guiado: `final`, mapa de literales y expresiones con resultado y tipo. |
| 12–23 min | Núcleo práctico individual: predecir operaciones, almacenar o mostrar resultados y justificar una constante. |
| 23–32 min | Contrastes guiados por parejas: división entera/real, precedencia, paréntesis y `%`. |
| 32–38 min | Aplicación breve: actualizaciones y traza `2 → 5 → 4 → 5`. |
| 38–43 min | Integrar constante, variable, operación, actualización y salida; ejecutar y explicar discrepancias. |
| 43–45 min | Comprobar la comprensión y cerrar. |

No conviertas cada ejemplo en un ejercicio independiente: la actividad practica el núcleo, los contrastes se razonan con guía y las actualizaciones se aplican brevemente.

## Ideas y ejemplos

### Constante frente a variable

Una variable almacena un dato cuyo valor puede cambiar durante la ejecución. Una constante representa un dato que no debe cambiar; en Java se declara con `final`.

Empieza con dos constantes que tienen sentido en el contexto:

```java
final String NOMBRE_ASISTENTE = "MiniJarvis";
final int ANIO_INICIO = 2026;
```

Pregunta:

> ¿Esperamos que el nombre del asistente o el año de inicio cambien mientras se ejecuta esta versión? ¿Qué expresa `final` sobre esa intención?

Contrasta una constante y una variable:

```java
final String NOMBRE_ASISTENTE = "MiniJarvis";
int horasEstudio = 3;
horasEstudio = 4;
```

`NOMBRE_ASISTENTE` no debe reasignarse. `horasEstudio` representa un dato que sí puede actualizarse.

Mantén este matiz:

> Que un dato empiece siempre con el mismo valor no significa automáticamente que conceptualmente sea una constante.

Por ejemplo:

```java
int tareas = 0;
```

`tareas` empieza en cero, pero está pensada para cambiar. Antes de decidir si usar `final`, pregunta si el dato puede o debe cambiar durante la ejecución, no solo cuál es su valor inicial.

### Literales: valores escritos directamente

Un literal es un valor que aparece escrito directamente en el código. Proyecta este mapa y pide que anticipen el tipo:

```text
5        -> entero
3.5      -> decimal
"Hola"   -> texto
'A'      -> carácter
true     -> booleano
false    -> booleano
```

Relaciona cada literal con una variable:

```java
int horas = 5;
double nota = 7.5;
String mensaje = "Hola";
char inicial = 'L';
boolean terminada = false;
```

Detente en el contraste:

```text
'L'  -> char: un carácter
"L"  -> String: texto de un carácter
```

Pregunta:

> Aunque ambos muestran la letra L, ¿qué tipo representa cada literal y qué delimitador permite distinguirlos?

No reduzcas la respuesta a «uno usa comillas simples y otro dobles»: deben relacionar el delimitador con `char` y `String`.

### Una expresión produce un resultado

Una expresión combina valores, variables u operadores y produce un resultado. Ese resultado también tiene un tipo.

```java
3 + 2
horas * 60
horas >= 4
tieneNombre && tieneObjetivo
"Hola, " + nombreUsuario
```

Relaciona cada expresión con su tipo de resultado:

```text
3 + 2                       -> int
5 / 2.0                     -> double
horas >= 4                  -> boolean
"Hola, " + nombreUsuario    -> String
```

Antes de ejecutar, pregunta por el valor y el tipo esperado. Las expresiones booleanas se utilizan aquí solo para reconocer que una expresión produce un resultado tipado; la comparación obligatoria se integra en S212 y las decisiones con control de flujo comienzan en H2.

### Operar, almacenar y utilizar

Empieza con una expresión aritmética cuyo resultado se almacena:

```java
int horasTotales = 3 + 2;
```

Pregunta:

> ¿Qué expresión se evalúa, qué resultado produce, qué tipo tiene y dónde queda guardado?

Amplía a una operación con variables:

```java
int dias = 5;
int horasPorDia = 2;
int horasTotales = dias * horasPorDia;
```

Pide predecir `horasTotales` antes de ejecutar y explicar qué representa cada operando.

Muestra después un resultado utilizado en la salida:

```java
int minutos = 4 * 60;
System.out.println(minutos);
```

Recorrido esperado:

```text
literales -> expresión -> resultado -> variable -> salida
```

Contrasta con el caso histórico:

```java
4 * 60;
```

Pregunta:

> ¿Dónde se guardaría el resultado y para qué se utilizaría? ¿Aceptará Java esta expresión aritmética aislada como una instrucción completa?

Aclara que, tal como está escrito, Java no acepta esa expresión aislada como una instrucción válida. Además de provocar un error de compilación, revela el problema de diseño que se quiere analizar: un cálculo sin almacenamiento, salida ni uso posterior no aporta un resultado utilizable.

### División entera y división real

Pide predicción antes de ejecutar:

```java
int divisionEntera = 5 / 2;
double divisionReal = 5 / 2.0;
```

Preguntas:

- ¿Qué valor esperas en `divisionEntera`?
- ¿Qué valor esperas en `divisionReal`?
- ¿Qué diferencia hay entre los operandos de ambas expresiones?

Con enteros, `5 / 2` da `2`, no `2.5`. La parte decimal no aparece porque los dos operandos de esa división son enteros. En `5 / 2.0`, el literal decimal hace que la operación produzca un resultado real.

No adelantes casting ni conversión de entrada: se trabajarán en S212. Aquí basta con razonar sobre los tipos de los operandos escritos en la expresión.

### Precedencia y paréntesis

No conviertas este apartado en una tabla matemática extensa. Trabaja el orden con el ejemplo histórico:

```java
int resultadoSinParentesis = 2 + 3 * 4;      // 14
int resultadoConParentesis = (2 + 3) * 4;    // 20
double resultado = 10 + 6 / 2.0; // 13.0
```

Antes de ejecutar, pide que calculen cada paso manualmente:

- en la primera expresión, la multiplicación ocurre antes que la suma;
- en la segunda, los paréntesis cambian el orden;
- en la tercera, la división ocurre antes que la suma y produce un resultado real.

Pregunta:

> ¿Qué operación se realiza primero en cada línea? ¿Dónde cambian los paréntesis el resultado y dónde solo podrían hacer más explícita la intención?

Regla práctica para H1:

> Si el orden puede generar dudas, usa paréntesis para expresar la intención y contrasta el resultado con una predicción.

### `%` significa resto

Presenta `%` como el resto de una división, no como porcentaje:

```text
10 / 4 -> 2
10 % 4 -> 2

8 % 2 -> 0
9 % 2 -> 1

17 / 5 -> 3
17 % 5 -> 2
```

Di:

> Diez objetos entre cuatro personas: dos para cada una y sobran dos. `%` expresa lo que sobra.

Preguntas:

- ¿Qué significan el cociente y el resto en `10 / 4` y `10 % 4`?
- ¿Qué patrón observas en `8 % 2` y `9 % 2`?
- ¿Cuánto esperas que valga `17 % 5` antes de mirar el ejemplo?

### Actualizaciones y estado paso a paso

Muestra varias formas de actualización:

```java
int tareas = 3;
tareas = tareas + 2;
tareas += 2;
tareas -= 1;
tareas++;
tareas--;
```

Explica cada forma sobre el valor anterior:

- `tareas = tareas + 2` calcula con el valor actual y reasigna;
- `tareas += 2` suma y actualiza;
- `tareas -= 1` resta y actualiza;
- `tareas++` incrementa una unidad;
- `tareas--` decrementa una unidad.

No basta con ejecutar el bloque completo. Utiliza esta traza:

```java
int tareas = 2;
tareas += 3;
tareas--;
tareas++;
```

Antes de ejecutar, el alumnado debe anticipar cada estado:

```text
2 -> 5 -> 4 -> 5
```

Pregunta en cada flecha:

> ¿Qué instrucción se ha aplicado y sobre qué valor anterior?

## Secuencia de trabajo y modalidad

### Predecir y construir — INDIVIDUAL

Antes de contrastar con otra persona, cada estudiante:

1. decide si un dato propuesto debe ser constante o variable y justifica por qué;
2. clasifica al menos un literal entero, decimal, textual, carácter y booleano;
3. explica la diferencia entre `'L'` y `"L"`;
4. predice el valor y el tipo de una expresión;
5. anticipa `5 / 2` y `5 / 2.0`;
6. calcula el efecto de los paréntesis;
7. razona sobre un ejemplo con `%`;
8. completa la traza de una actualización sin ejecutar.

Núcleo práctico:

> En MiniJarvis o en una micropráctica, usa una constante con sentido, una variable, al menos un literal, una operación cuyo resultado se guarde o se muestre, una actualización y una salida que permita comprobarlo. Escribe primero la predicción y explica después el resultado.

### Contrastar, ejecutar e integrar — PAREJAS

Después del intento individual, las parejas:

- comparan qué datos han considerado constantes o variables;
- contrastan predicciones sin ejecutar primero;
- ejecutan los ejemplos seleccionados;
- explican las discrepancias entre predicción y resultado;
- revisan dónde se almacena o utiliza cada operación;
- comparan división entera y real;
- justifican el efecto de los paréntesis;
- explican `%` como resto;
- recorren las actualizaciones estado por estado;
- integran una solución técnica común cuando resulte útil.

El contraste por parejas no sustituye el intento individual. No todos los ejemplos necesitan convertirse en ejercicios: algunos sirven para explicación o contraste guiado.

## Evidencia que permanece

- **GitHub:** código integrado o micropráctica con resultado reproducible.
- **Scrum:** solo si existe una tarea, decisión, cambio o bloqueo real.
- **Diario individual:** solo si una predicción errónea, un error o un descubrimiento produjo aprendizaje individual significativo.
- **README / Moodle / Drive / Site:** sin actualización o entrega específica en S211.

La predicción es obligatoria como actividad pedagógica, no como documento. No se crean capturas rutinarias, documentos paralelos ni microentregas.

Modelo para explicar una comprobación:

```text
Predicción: si horas vale 5, minutos será 300.
Código probado: int minutos = horas * 60;
Resultado observado: la consola muestra 300.
Explicación: la operación multiplica horas por 60 y guarda el resultado.
```

## Observación docente

Durante el intento individual y el contraste por parejas, observa específicamente:

- que distingue constante y variable por su función, no solo por el valor inicial;
- que relaciona `final` con un dato que no debe reasignarse;
- que identifica el tipo de un literal;
- que diferencia `'L'` y `"L"`;
- que explica que una expresión produce un resultado con un tipo;
- que predice una operación antes de ejecutar;
- que reconoce la división entera y la división real;
- que utiliza paréntesis con intención;
- que interpreta `%` como resto y no como porcentaje;
- que sigue una actualización paso a paso;
- que señala dónde se almacena, muestra o utiliza un resultado;
- que puede explicar de dónde procede la salida observada.

## Andamiaje ante bloqueos

No des la solución completa de inmediato. Utiliza una pregunta o pista específica:

- **Confunde constante con valor inicial fijo:** pregunta si el dato puede o debe cambiar conceptualmente durante la ejecución.
- **Confunde `'L'` y `"L"`:** pregunta qué tipo representa cada literal y qué delimitador utiliza.
- **No identifica el resultado de una expresión:** separa operandos, operador, valor resultante y tipo.
- **Obtiene `2` en `5 / 2`:** pide revisar el tipo de ambos operandos antes de cambiar la expresión.
- **No entiende la precedencia:** pide hacer el cálculo manual, operación por operación, antes de ejecutar.
- **Interpreta `%` como porcentaje:** pide cociente y resto de una división concreta.
- **Pierde la pista con `+=` o `++`:** escribe el valor inicial y anota un estado después de cada instrucción.
- **Calcula pero no utiliza el resultado:** pregunta dónde queda almacenado, dónde se muestra y para qué sirve.
- **Una persona resuelve todo:** pide a la otra que justifique una predicción y recorra una actualización nueva.

## Comprueba lo aprendido

Pregunta principal:

> ¿Qué dato has tratado como constante y por qué, qué expresión has calculado, dónde queda su resultado y cómo sabes que la salida coincide con tu predicción?

Pregunta complementaria:

> ¿Por qué `5 / 2` produce `2`, qué cambian los paréntesis, qué significa `%` y cómo evoluciona una variable con `+=`, `-=`, `++` o `--`?

Cierra en voz alta:

> Una operación no está demostrada porque el código compile. Está demostrada cuando puedo predecir el resultado, ejecutarla y explicar de dónde sale. Una constante tampoco se decide solo por su valor inicial, sino por si el dato debe cambiar.

## Límite de la sesión

S211 parte de variables y tipos ya trabajados en S210. No introduce `Scanner`, parseo ni casting como contenido central; la entrada, las conversiones, el cálculo y la comparación booleana observable corresponden a S212. Las expresiones lógicas aparecen solo para reconocer resultados con tipo y no adelantan las decisiones con control de flujo de H2.

## Al terminar

Anota solo lo necesario para la continuidad docente: confusión que conviene retomar, alumnado que necesita apoyo, bloqueo pendiente con su siguiente paso y ajuste de tiempo necesario.
