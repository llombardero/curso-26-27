# S211 - Ejecutar - Constantes, literales y operaciones

| Dato | Valor |
|---|---|
| Hito | H1 — Primer asistente ejecutable |
| Duración prevista | 45 minutos |
| Fase HEXA del hito | Ejecutar — crear |

> Basada en `00-GUION-DOCENTE-H1-COMPLETO.md`. Selecciona y desarrolla los conceptos, ejemplos, actividades y evidencias útiles para esta sesión.

## Qué vas a aprender

Al terminar, debes usar constantes, literales y operaciones aritméticas con predicción y prueba.

## Ideas y ejemplos

Úsala antes de introducir `final`, división entera, `%` y actualización.

Una constante representa un dato que no debe cambiar durante la ejecución. Un literal es un valor escrito directamente. Una operación produce un resultado, pero ese resultado se pierde si no lo guardamos, mostramos o usamos.

Empieza con constantes y variables:

```java
final String NOMBRE_ASISTENTE = "MiniJarvis";
final int ANIO_INICIO = 2026;
```

Pregunta al alumnado:

Esperamos que estos datos cambien durante la ejecución.

Contrasta constante y variable:

```java
final String NOMBRE_ASISTENTE = "MiniJarvis";
int horasEstudio = 3;
horasEstudio = 4;
```

Aclara:

Un dato puede empezar siempre igual y no ser constante si está pensado para cambiar.

```java
int tareas = 0;
```

Presenta literales:

```text
5
3.5
"Hola"
'A'
true
false
```

Clasifica con ejemplos:

```java
int horas = 5;
double nota = 7.5;
String mensaje = "Hola";
char inicial = 'L';
boolean terminada = false;
```

Pregunta:

Qué diferencia hay entre `'L'` y `"L"`.

### Una expresión produce un resultado

Una expresión combina valores, variables u operadores y produce un resultado que también tiene un tipo.

```java
3 + 2
horas * 60
horas >= 4
tieneNombre && tieneObjetivo
"Hola, " + nombreUsuario
```

```text
3 + 2                       -> int
5 / 2.0                     -> double
horas >= 4                  -> boolean
"Hola, " + nombreUsuario    -> String
```

Antes de ejecutar una expresión, predice su valor y su tipo. Después comprueba si el resultado observado coincide.

Trabaja operaciones aritméticas:

```java
int horasTotales = 3 + 2;
```

```java
int dias = 5;
int horasPorDia = 2;
int horasTotales = dias * horasPorDia;
```

```java
int minutos = 4 * 60;
System.out.println(minutos);
```

Contrasta con resultado ignorado:

```java
4 * 60;
```

Pregunta:

Dónde queda guardado el resultado para utilizarlo después.

Predice división entera y real:

```java
int divisionEntera = 5 / 2;
double divisionReal = 5 / 2.0;
```

Pregunta:

Qué vale `divisionEntera` y qué vale `divisionReal`.

Compara también el efecto de los paréntesis:

```java
int resultadoSinParentesis = 2 + 3 * 4;      // 14
int resultadoConParentesis = (2 + 3) * 4;    // 20
double resultado = 10 + 6 / 2.0; // 13.0
```

Java aplica la precedencia de los operadores; no siempre evalúa simplemente de izquierda a derecha. Los paréntesis cambian o hacen explícito el orden de cálculo.

Explica `%` como resto, no como porcentaje:

```text
10 / 4 -> 2
10 % 4 -> 2

8 % 2 -> 0
9 % 2 -> 1

17 / 5 -> 3
17 % 5 -> 2
```

Di:

Diez caramelos entre cuatro personas: dos para cada una y sobran dos. `%` expresa lo que sobra.

Termina con actualización:

```java
int tareas = 3;
tareas = tareas + 2;
tareas += 2;
tareas -= 1;
tareas++;
tareas--;
```

Traza paso a paso:

```java
int tareas = 2;
tareas += 3;
tareas--;
tareas++;
```

Resultado esperado:

```text
2 -> 5 -> 4 -> 5
```

Error frecuente que debes cortar:

`5 / 2` con enteros da `2`, no `2.5`.

La **precedencia** determina qué operación se calcula antes. Multiplicación, división y resto tienen prioridad sobre suma y resta. Usa paréntesis cuando quieras cambiar ese orden o hacer explícita la intención.

## Actividad de la sesión

En vuestro MiniJarvis o en un ejercicio, usad una constante, una variable, una operación, una actualización y una salida que permita comprobar el resultado.

## Evidencia de la sesión

Conservad el ejercicio o el código integrado y registrad una predicción que haya sido confirmada o corregida.

**Dónde y cómo conservar la evidencia:**

- GitHub: código de ejercicio o `Main.java` actualizado.
- Diario individual: predicción, resultado observado y explicación breve.
- Moodle: no se entrega todavía.

Qué debe contener:

- Uso de `final`.
- Una operación comprobable.
- Evidencia de resultado.

Modelo de uso de predicción S211:

```text
Predicción: si horas vale 5, minutos será 300.
Código probado: int minutos = horas * 60;
Resultado observado: la consola muestra 300.
Explicación: la operación multiplica horas por 60 y guarda el resultado.
```

## Comprueba lo aprendido

Una operación no está demostrada porque el código compile. Está demostrada cuando puedo predecir el resultado, ejecutarlo y explicar si coincide.
