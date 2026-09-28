# S213 — Comparaciones, lógica y decisiones

## Objetivo

Construir comparaciones, guardar resultados booleanos, utilizar una condición en `if/else` y comprobar sus dos ramas. Como ampliación, reconocer combinaciones lógicas, anidamiento y operador ternario.

## 1. Comparar produce un `boolean`

```java
int horas = 5;
System.out.println(horas == 5); // true
System.out.println(horas != 5); // false
System.out.println(horas >= 4); // true
```

Una comparación no devuelve uno de los operandos: devuelve `true` o `false`.

Operadores habituales:

| Operador | Significado |
|---|---|
| `==` | igual que |
| `!=` | distinto de |
| `>` | mayor que |
| `<` | menor que |
| `>=` | mayor o igual que |
| `<=` | menor o igual que |

`=` asigna; `==` compara.

## 2. Guardar una comparación

```java
int horas = 5;
boolean suficiente = horas >= 4;
System.out.println(suficiente);
```

Prueba al menos dos valores para observar `true` y `false`.

## 3. De la condición a `if/else`

```java
int horas = 5;

if (horas >= 4) {
    System.out.println("Objetivo alcanzado");
} else {
    System.out.println("Objetivo pendiente");
}
```

- La condición debe producir un `boolean`.
- Si es `true`, se ejecuta el bloque `if`.
- Si es `false`, se ejecuta el bloque `else`.
- Solo se ejecuta una de las dos ramas.

Esto no es válido:

```java
if (horas) {
    System.out.println("No compila");
}
```

`horas` es un `int`, no una condición booleana.

## 4. Prueba las dos ramas

Antes de ejecutar, completa:

| Caso | Valor de `horas` | Condición esperada | Salida esperada |
|---|---:|---|---|
| A | 5 | `true` | `Objetivo alcanzado` |
| B | 2 | `false` | `Objetivo pendiente` |

Después registra la salida observada. Probar solo una rama no demuestra el comportamiento completo.

## 5. Ampliación: combinar y negar condiciones

### AND `&&`

Las dos condiciones deben cumplirse:

```java
boolean tieneNombre = true;
boolean tieneObjetivo = true;
boolean puedeEmpezar = tieneNombre && tieneObjetivo;
```

### OR `||`

Basta con que se cumpla una:

```java
boolean tienePregunta = false;
boolean hayError = true;
boolean necesitaAyuda = tienePregunta || hayError;
```

### NOT `!`

Invierte un booleano:

```java
boolean terminada = false;
boolean pendiente = !terminada; // true
```

Predice cada resultado antes de ejecutar.

## 6. Ampliación: reconocer un `if` anidado

Un `if` puede aparecer dentro de otro:

```java
if (horas >= 4) {
    if (horas >= 8) {
        System.out.println("Objetivo superado");
    } else {
        System.out.println("Objetivo alcanzado");
    }
} else {
    System.out.println("Objetivo pendiente");
}
```

En H1 basta con leerlo y explicar el camino para valores como `2`, `5` y `9`. No necesitas introducirlo en el producto principal si reduce su claridad.

## 7. Ampliación: leer un operador ternario

```java
String estado = horas >= 4 ? "alcanzado" : "pendiente";
```

Se lee así: si la condición es verdadera, usa `"alcanzado"`; en caso contrario, usa `"pendiente"`.

Es una forma compacta de elegir un valor. Para decisiones con varias instrucciones, `if/else` suele ser más claro.

## 8. Nota sobre textos

`==` es adecuado para comparar valores primitivos. Para comparar el contenido de dos `String` se utiliza normalmente `equals`:

```java
boolean mismoTexto = "hola".equals("hola");
```

Esta nota es de consulta; el núcleo de S213 son comparaciones primitivas y `if/else`.

## 9. Actividad

1. Crea una comparación con `horas`.
2. Guarda el resultado en un `boolean`.
3. Utilízalo directa o indirectamente en `if/else`.
4. Predice y ejecuta un caso verdadero y otro falso.
5. Como ampliación, explica una expresión con `&&`, otra con `||` y otra con `!`.
6. Traza un `if` anidado y un ternario sin necesidad de incorporarlos al producto final.

## Evidencia verificable

Registra la condición, cada entrada, el resultado booleano, la salida esperada y la observada. La evidencia debe demostrar las dos ramas y enlazar al código concreto.

## Errores frecuentes

- Confundir `=` con `==`.
- Escribir `if (horas)` cuando `horas` es `int`.
- Probar solo la rama verdadera.
- Confundir `&&` con `||`.
- Olvidar que `!` invierte el valor.
- Usar un ternario largo cuando `if/else` sería más legible.

## Autoevaluación

Comprueba que puedes:

- predecir seis comparaciones;
- explicar por qué una condición es booleana;
- señalar condición, rama `if` y rama `else`;
- demostrar los dos caminos con pruebas;
- leer `&&`, `||` y `!`;
- seguir un `if` anidado sencillo;
- interpretar un ternario.

## Seguridad y uso de IA

Usa datos ficticios. Si una IA propone una condición, prueba valores de frontera y las dos ramas antes de aceptarla.
