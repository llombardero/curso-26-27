# S213 — Comparaciones, lógica y decisiones

| Dato | Valor |
|---|---|
| Hito | H1 — Primer asistente ejecutable |
| Duración prevista | 45 minutos |
| Fase HEXA del hito | Ejecutar — crear |
| Modalidad de trabajo | **INDIVIDUAL → PAREJAS → comprobación INDIVIDUAL** |

> Basada en `00-GUION-DOCENTE-H1-COMPLETO.md`.

## Qué vas a aprender

Al terminar, debes construir expresiones booleanas, combinar condiciones y usar una decisión `if/else` con las dos ramas probadas. También debes leer una decisión anidada sencilla y reconocer el operador ternario como una elección limitada de valor.

## Antes de entrar en clase

- [ ] Abrir y ejecutar el proyecto que utilizará el alumnado.
- [ ] Preparar una alternativa en pareja si falla un equipo.
- [ ] Dejar visibles dos valores de prueba que recorran ramas distintas.
- [ ] Reservar los últimos minutos para una comprobación individual real.
- [ ] Comprobar que el código inicial no adelanta menús, bucles ni decisiones complejas de H2.

## Material imprescindible

- Un ordenador por estudiante o pareja, con JDK e IntelliJ disponibles.
- Proyecto H1 accesible desde el repositorio del equipo.
- Pizarra o espacio proyectable para predicciones, expresiones y recorridos.

## Apertura docente

Di en voz alta:

> Hoy MiniJarvis empieza a decidir algo muy pequeño. No haremos menús ni bucles. Hoy queremos entender que una comparación produce `true` o `false`, y que `if/else` usa ese resultado para elegir una rama.

Aclara desde el principio:

> Antes de ejecutar, predice qué ocurrirá y qué rama se recorrerá.

## Temporalización orientativa

| Tiempo | Acción |
|---|---|
| 0–5 min | Presentar la finalidad: una comparación produce un booleano y una decisión usa ese resultado. |
| 5–12 min | Contrastar asignación/comparación, trabajar límites y predecir resultados. |
| 12–18 min | Traducir `&&`, `\|\|` y `!` entre lenguaje natural y Java. |
| 18–27 min | Practicar la decisión central con `if/else`, validación y dos ramas. |
| 27–29 min | Leer de forma introductoria una decisión anidada, sin profundizar. |
| 29–31 min | Presentar el ternario como elección sencilla y limitada de valor. |
| 31–39 min | Implementar en parejas la micropráctica y probar las dos ramas. |
| 39–43 min | Realizar la comprobación individual: señalar, predecir, modificar, ejecutar y explicar. |
| 43–45 min | Revisar claridad y cerrar con el criterio de prueba reproducible. |

## Ideas y ejemplos

### Comparaciones y resultados booleanos

Una comparación no devuelve uno de los operandos. Produce un valor booleano: `true` o `false`.

Empieza con comparadores:

```text
5 > 3 -> true
2 < 1 -> false
5 == 5 -> true
5 == 4 -> false
5 != 4 -> true
```

Amplía oralmente el mapa:

- `>`: mayor que;
- `<`: menor que;
- `==`: igual a;
- `!=`: distinto de;
- `>=`: mayor o igual que;
- `<=`: menor o igual que.

No lo presentes como una lista para memorizar. Para cada expresión, pide al alumnado que lea la relación en lenguaje natural y prediga el resultado.

Pregunta:

> ¿`5 > 3` devuelve 5, devuelve 3 o devuelve una respuesta lógica?

### Asignar no es comparar

Contrasta asignar y comparar:

```java
int horas = 4;  // asignación
horas == 4      // comparación: true o false
```

Di:

> `=` guarda o asigna un valor. `==` compara dos valores y produce `true` o `false`.

Pregunta:

> En `int horas = 4`, ¿qué se guarda? En `horas == 4`, ¿qué resultado se produce?

Trabaja límites:

```java
int horas = 4;
horas > 4
horas >= 4
```

Pregunta:

> Predice ambas expresiones. ¿Qué cambia exactamente cuando añadimos `=` al comparador?

Recuerda:

> En esta sesión no usamos `==` para comparar `String`.

### Operadores lógicos desde el lenguaje natural

Introduce `&&`, `||` y `!` partiendo de frases que puedan razonarse.

```java
boolean puedeEmpezar = tieneNombre && tieneObjetivo;
```

Di:

> MiniJarvis puede comenzar si tiene nombre **y** tiene objetivo. Con `&&`, las dos condiciones deben cumplirse.

```java
boolean necesitaAyuda = faltaConfiguracion || hayError;
```

Di:

> MiniJarvis necesita ayuda si falta configuración **o** existe un error. Con `||`, basta con que se cumpla al menos una condición.

```java
boolean terminada = false;
boolean pendiente = !terminada;
```

Resultado esperado:

```text
pendiente -> true
```

Di:

> `!` niega el valor booleano: si `terminada` es `false`, `!terminada` es `true`.

Traduce en ambos sentidos:

```text
Puede continuar si tiene nombre y objetivo -> tieneNombre && tieneObjetivo
No hay error -> !hayError
```

Pide más traducciones breves:

- «Tiene nombre o tiene alias» → expresión con `||`.
- `horas >= 4 && tareas >= 2` → frase en lenguaje natural.
- `!hayError` → explicación sin símbolos.

### Guardar una condición o usarla directamente

Pasa del booleano a la decisión:

```java
int horas = 5;
boolean suficiente = horas >= 4;

if (suficiente) {
    System.out.println("Objetivo alcanzado");
}
```

Pregunta:

> ¿Qué valor queda guardado en `suficiente`? ¿Qué necesita recibir `if`?

Muestra después la condición directa:

```java
if (horas >= 4) {
    System.out.println("Objetivo alcanzado");
}
```

Pregunta:

> ¿Qué produce `horas >= 4`? ¿Qué tienen en común las dos versiones?

Aclara que ambas formas son válidas. Guardar la condición puede ayudar a nombrar una idea; usarla directamente puede ser suficiente cuando sigue siendo clara.

### Un contraejemplo que no compila

Contrasta con lo que no sirve:

```java
if (horas) {
    System.out.println("Objetivo alcanzado");
}
```

Pregunta:

> `horas` contiene un `int`. ¿La condición de `if` responde `true` o `false`?

Explica:

> Java exige que la condición de `if` sea una expresión booleana. Un número entero no se interpreta automáticamente como verdadero o falso.

### Dos caminos con `if/else`

Ahora trabaja dos ramas:

```java
if (horas >= 4) {
    System.out.println("Objetivo alcanzado");
} else {
    System.out.println("Objetivo pendiente");
}
```

Casos obligatorios:

```text
Caso A: horas = 5
Caso B: horas = 2
```

Antes de ejecutar cada caso, pide:

1. valor de entrada;
2. resultado previsto de la condición;
3. rama prevista;
4. salida prevista.

Después de ejecutar, deben contrastar la predicción y explicar cualquier discrepancia.

Otro ejemplo cercano a MiniJarvis:

```java
if (tieneNombre) {
    System.out.println("Nombre configurado");
} else {
    System.out.println("Falta configurar el nombre");
}
```

Pregunta:

> ¿Qué tendría que valer `tieneNombre` para llegar a cada mensaje?

### Validación sencilla de datos

Presenta una comprobación de horas no negativas:

```java
if (horasEstudio >= 0) {
    System.out.println("Dato aceptado");
} else {
    System.out.println("Las horas no pueden ser negativas");
}
```

Pide tres predicciones:

- `horasEstudio = 3`;
- `horasEstudio = 0`;
- `horasEstudio = -1`.

Pregunta:

> ¿Qué condición se comprueba? ¿Qué ocurre cuando se cumple? ¿Qué ocurre cuando no se cumple? ¿Por qué el cero pertenece al caso válido?

### Predicción y modificación de valores

```java
int nota = 5;
if (nota >= 5) {
    System.out.println("Superado");
} else {
    System.out.println("Pendiente");
}
```

Pregunta:

> ¿Qué bloque se ejecutará? Cambia `nota` a 4 y vuelve a predecir antes de ejecutar.

No aceptes que el alumnado modifique valores al azar hasta obtener otra salida. Debe anticipar el efecto del cambio.

### Lectura introductoria de decisiones anidadas

Reconoce un `if` anidado sin profundizar:

```java
if (tieneNombre) {
    if (tieneObjetivo) {
        System.out.println("MiniJarvis está preparado");
    }
}
```

Pregunta:

> ¿Qué condición se comprueba primero? ¿Cuándo se llega a comprobar `tieneObjetivo`?

Otro anidado:

```java
if (horas >= 4) {
    if (tareas >= 2) {
        System.out.println("Objetivo completo");
    }
}
```

Explica oralmente:

```text
horas >= 4?
  sí -> tareas >= 2?
          sí -> mensaje
```

Di:

> Aquí basta con reconocer y leer la idea. No vamos a convertir H1 en una sesión de condicionales complejos.

### Operador ternario como elección sencilla

Muestra primero una elección de valor con `if/else`:

```java
String mensaje;
if (horas >= 4) {
    mensaje = "Objetivo alcanzado";
} else {
    mensaje = "Objetivo pendiente";
}
```

Misma elección con `?:`:

```java
String mensaje = horas >= 4
        ? "Objetivo alcanzado"
        : "Objetivo pendiente";
```

Despieza:

```text
horas >= 4 -> condición
"Objetivo alcanzado" -> valor si true
"Objetivo pendiente" -> valor si false
```

Más ejemplos para leer, no para complicar:

```java
String estado = tareas > 0
        ? "Hay tareas"
        : "No hay tareas";

String resultado = nota >= 5
        ? "Superado"
        : "Pendiente";
```

Predicción:

```java
int horas = 2;
String mensaje = horas >= 4
        ? "Objetivo alcanzado"
        : "Objetivo pendiente";
```

Pregunta:

> ¿Qué valor termina almacenado en `mensaje`?

Advertencia expresa:

> El operador ternario no es un sustituto general de `if`. En H1 solo interesa leer y usar una elección sencilla de valor. Si la lógica deja de ser clara, vuelve a `if/else`.

### Errores frecuentes que debes cortar

- Confundir asignación `=` con comparación `==`.
- Creer que una comparación devuelve uno de los números en lugar de un booleano.
- Usar un `int` directamente como condición.
- Leer `&&` como si bastara una condición.
- Leer `||` como si tuvieran que cumplirse todas.
- Probar solo el caso `true` y afirmar que el `else` funciona.
- Cambiar datos al azar sin predecir la rama.
- Usar el ternario para ocultar una decisión que se entiende mejor con `if/else`.

## Secuencia de trabajo y modalidad

### Comprender, traducir y predecir — INDIVIDUAL

Antes de hablar con otra persona, cada estudiante debe:

- predecir comparaciones con `>`, `<`, `==`, `!=`, `>=` o `<=`;
- distinguir una asignación de una comparación;
- anticipar si una expresión será `true` o `false`;
- traducir una condición entre lenguaje natural y Java;
- completar o formular una decisión sencilla;
- escribir la predicción de una salida sin ejecutar todavía.

### Contrastar, implementar y probar — PAREJAS

Las parejas:

- comparan predicciones y explican discrepancias;
- contrastan expresiones lógicas;
- implementan o revisan una decisión `if/else`;
- ejecutan al menos un caso `true` y un caso `false`;
- contrastan salida prevista y salida observada;
- explican por qué se recorrió cada rama.

No basta con que una persona escriba mientras la otra observa. Ambas deben poder señalar la condición y anticipar el recorrido.

### Micropráctica defendible — PAREJAS

Construid una práctica pequeña que incluya:

- un dato;
- al menos una comparación;
- un resultado booleano guardado o utilizado directamente;
- una decisión `if/else`;
- una salida distinta por rama;
- dos casos de prueba;
- predicción, ejecución, contraste y explicación.

La práctica puede integrarse en MiniJarvis o realizarse como micropráctica técnica dentro del repositorio.

Secuencia mínima de comprobación:

```text
Predicción -> ejecución -> contraste -> explicación
```

Modelo para razonar durante la prueba:

```text
Prueba de decisión if/else
Condición: horasEstudio >= 4

Caso A:
Valor usado: horasEstudio = 5
Salida esperada: Objetivo alcanzado.
Salida obtenida: Objetivo alcanzado.
Demuestra: se ejecuta la rama true.

Caso B:
Valor usado: horasEstudio = 2
Salida esperada: Objetivo pendiente.
Salida obtenida: Objetivo pendiente.
Demuestra: se ejecuta la rama false.
```

### Revisar claridad y simplicidad — PAREJAS

Solo después de que la decisión funcione y ambas ramas estén comprobadas, revisad:

- nombres significativos;
- orden comprensible;
- comentarios que expliquen intención, no lo obvio;
- ausencia de adornos innecesarios;
- líneas o elementos que nadie sabe explicar.

Criterio de revisión:

> Primero correcto y explicable; después más claro y simple.

La limpieza es un criterio transversal de calidad. No sustituye comparaciones, booleanos, lógica, decisiones ni pruebas.

### Comprobar comprensión — INDIVIDUAL

Al terminar, cualquier persona debe poder, sin apoyo de la pareja:

- señalar una comparación y explicar qué produce;
- distinguir `=` de `==`;
- interpretar `true` y `false`;
- traducir una condición verbal a Java o a la inversa;
- explicar la condición de un `if`;
- predecir qué rama se ejecutará;
- justificar por qué entra en esa rama;
- modificar un valor y anticipar el efecto;
- ejecutar y comprobar un caso;
- explicar por qué se necesitan las dos pruebas;
- reconocer el flujo de un `if` anidado sencillo;
- explicar cuándo el ternario resulta adecuado y cuándo conviene volver a `if/else`.

El producto compartido no sustituye la comprensión individual.

## Evidencia que permanece

- **GitHub:** código con comparación, booleano, `if/else` y casos `true` y `false` reproducibles.
- **Scrum:** solo si existe realmente una tarea, decisión, mejora, cambio o bloqueo del equipo. No se actualiza por el mero hecho de terminar S213.
- **Diario individual:** solo si una discrepancia entre predicción y resultado, un error, una decisión o un bloqueo produjo aprendizaje individual significativo.
- **README / Moodle / Drive / Site:** sin actualización o entrega específica en S213.

No se crean capturas rutinarias, formularios, documentos paralelos de pruebas ni registros separados de IA.

## Observación docente

Durante la práctica y la comprobación individual, observa específicamente:

- que distingue `=` de `==` y puede decir si está asignando o comparando;
- que comprende que una comparación produce un booleano;
- que interpreta correctamente `true` y `false`;
- que explica `&&`, `||` y `!` mediante condiciones concretas;
- que traduce una condición verbal a Java y una expresión Java a lenguaje natural;
- que identifica la condición de un `if`;
- que predice la rama antes de ejecutar;
- que prueba deliberadamente un caso `true` y otro `false`;
- que contrasta la salida observada con su predicción;
- que modifica un valor y anticipa el efecto sin ensayo aleatorio;
- que puede explicar individualmente la decisión implementada;
- que solo revisa nombres, comentarios y simplicidad después de obtener una decisión correcta y explicable.
- que trabaja con datos ficticios y no introduce datos personales ni credenciales en el código o en las pruebas.

## Andamiaje ante bloqueos

No proporciones inmediatamente la solución completa. Utiliza la ayuda mínima necesaria:

- **Confunde `=` y `==`:** pregunta si pretende guardar un valor o comparar dos valores.
- **No comprende `true` y `false`:** aísla únicamente la expresión booleana y pide que la evalúe sin el `if`.
- **Falla con `&&`:** pide comprobar cada condición por separado y pregunta cuántas deben cumplirse.
- **Falla con `||`:** pregunta cuántas condiciones necesitan cumplirse para que el resultado sea `true`.
- **No entiende `!`:** parte de un valor booleano concreto y pregunta cuál es su negación.
- **No sabe qué rama se ejecuta:** exige una predicción antes de permitir la ejecución.
- **Modifica código al azar:** vuelve al valor de entrada y recorre la condición paso a paso.
- **Solo prueba una rama:** pregunta qué valor obligaría al programa a seguir el otro camino.
- **Se pierde en un `if` anidado:** recorre primero la condición exterior y pregunta si se llega a evaluar la interior.
- **Usa el ternario para lógica compleja:** vuelve a `if/else` y compara cuál permite explicar mejor la decisión.
- **El código funciona pero no se entiende:** pide señalar qué nombre, orden, comentario o adorno dificulta explicarlo, sin alterar todavía el comportamiento.

## Comprueba lo aprendido

Cierra con una comprobación individual breve. Pide señalar, predecir, modificar y ejecutar una parte de la decisión.

Pregunta de control:

> ¿Qué condición se evalúa, qué rama esperas con este valor y qué nuevo valor usarías para comprobar la otra rama?

Como revisión de claridad, pregunta también:

> ¿Qué línea de tu código no sabes explicar todavía?

Criterio para cerrar:

- ambas ramas se han probado;
- la predicción se ha contrastado con la ejecución;
- existe una explicación individual suficiente de la condición y del recorrido.

Di en voz alta:

> H1 ya tiene una decisión pequeña. Si hoy alguien solo puede decir `funciona`, todavía no basta. Debe poder señalar la condición, explicar las dos ramas y demostrar que ambas se han probado.

## Al terminar

Anota solo lo operativo para preparar la siguiente intervención docente:

- alumnado que necesita apoyo;
- confusión frecuente que conviene retomar;
- bloqueo técnico pendiente y siguiente paso;
- ajuste de tiempo necesario.
