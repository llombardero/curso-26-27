# S213 - Ejecutar - Comparaciones, lógica y decisiones

| Dato | Valor |
|---|---|
| Hito | H1 — Primer asistente ejecutable |
| Duración prevista | 45 minutos |
| Fase HEXA del hito | Ejecutar — crear |

> Basada en `00-GUION-DOCENTE-H1-COMPLETO.md`. Selecciona y desarrolla los conceptos, ejemplos, actividades y evidencias útiles para esta sesión.

## Qué vas a aprender

Al terminar, debes construir booleanos, combinar condiciones y usar una decisión `if/else` con dos ramas probadas.

## Ideas y ejemplos

Úsala antes de `if/else` y antes de pedir las dos pruebas.

Una comparación produce un booleano: `true` o `false`. `=` asigna; `==` compara. `if` necesita una condición booleana. En H1 hacemos decisiones pequeñas; menús y decisiones encadenadas vendrán en H2.

Empieza con comparadores:

```text
5 > 3 -> true
2 < 1 -> false
5 == 5 -> true
5 == 4 -> false
5 != 4 -> true
```

Pregunta:

`5 > 3` devuelve 5, devuelve 3 o devuelve una respuesta lógica.

Contrasta asignar y comparar:

```java
int horas = 4;  // asignación
horas == 4      // comparación: true o false
```

Trabaja límites:

```java
int horas = 4;
horas > 4
horas >= 4
```

Pregunta:

Predice ambas expresiones.

**Recuerda:**

En esta sesión no usamos `==` para comparar `String`.

Ahora introduce `&&`, `||` y `!` desde lenguaje natural:

```java
boolean puedeEmpezar = tieneNombre && tieneObjetivo;
```

Di:

MiniJarvis puede comenzar si tiene nombre y tiene objetivo.

```java
boolean necesitaAyuda = faltaConfiguracion || hayError;
```

Di:

Necesita ayuda si falta configuración o existe un error.

```java
boolean terminada = false;
boolean pendiente = !terminada;
```

Resultado esperado:

```text
pendiente -> true
```

Traduce en ambos sentidos:

```text
Puede continuar si tiene nombre y objetivo -> tieneNombre && tieneObjetivo
No hay error -> !hayError
```

Pasa del booleano a la decisión:

```java
int horas = 5;
boolean suficiente = horas >= 4;

if (suficiente) {
    System.out.println("Objetivo alcanzado");
}
```

Y después condición directa:

```java
if (horas >= 4) {
    System.out.println("Objetivo alcanzado");
}
```

Pregunta:

Qué produce `horas >= 4`.

Contrasta con lo que no sirve:

```java
if (horas) {
    System.out.println("Objetivo alcanzado");
}
```

Pregunta:

`horas` contiene un `int`. La condición de `if` responde true/false.

Ahora trabaja dos caminos:

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

Otro ejemplo cercano a MiniJarvis:

```java
if (tieneNombre) {
    System.out.println("Nombre configurado");
} else {
    System.out.println("Falta configurar el nombre");
}
```

Dato sencillo para validar:

```java
if (horasEstudio >= 0) {
    System.out.println("Dato aceptado");
} else {
    System.out.println("Las horas no pueden ser negativas");
}
```

Predicción antes de ejecutar:

```java
int nota = 5;
if (nota >= 5) {
    System.out.println("Superado");
} else {
    System.out.println("Pendiente");
}
```

Pregunta:

Qué bloque se ejecutará. Cambia `nota` a 4 y vuelve a predecir.

Reconoce un `if` anidado sin profundizar:

```java
if (tieneNombre) {
    if (tieneObjetivo) {
        System.out.println("MiniJarvis está preparado");
    }
}
```

Pregunta:

Qué condición se comprueba primero y cuándo se llega a comprobar `tieneObjetivo`.

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
  si -> tareas >= 2?
          si -> mensaje
```

Di:

Aquí basta con reconocer y leer la idea. No vamos a convertir H1 en una sesión de condicionales complejos.

Por último, muestra la asignación condicional `?:` como elección sencilla de valor:

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

Qué valor termina almacenado en `mensaje`.

Pregunta al alumnado:

Qué pasa con `horas = 5`, qué pasa con `horas = 2`, qué rama se ejecuta y qué evidencia demuestra cada caso.

Error frecuente que debes cortar:

Probar solo el caso `true` no demuestra el `else`.

No presentes el operador ternario `?:` como sustituto de cualquier `if`. En H1 solo interesa leer una elección sencilla de valor.

## Actividad de la sesión

Construid una micropráctica defendible: dato, comparación, boolean, `if/else` y salida. Debéis probar dos casos: uno que entre por `if` y otro que entre por `else`.

## Evidencia de la sesión

La evidencia de hoy debe demostrar dos ramas. No basta con probar el caso favorable.

**Dónde y cómo conservar la evidencia:**

- GitHub: código con comparación e `if/else`.
- Diario individual: caso A, salida esperada, salida obtenida; caso B, salida esperada, salida obtenida.
- Moodle: no se entrega todavía.

Qué debe poder defender cada persona:

- Qué comparación se evalúa.
- Qué significa `true`.
- Qué significa `false`.
- Qué rama se ejecuta en cada caso.
- Qué mejora concreta hizo en el código o nombres.

Modelo de uso de evidencia S213:

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

## Comprueba lo aprendido

H1 ya tiene una decisión pequeña. Si hoy alguien solo puede decir `funciona`, todavía no basta. Debe poder señalar la condición, explicar las dos ramas y demostrar que ambas se han probado.
