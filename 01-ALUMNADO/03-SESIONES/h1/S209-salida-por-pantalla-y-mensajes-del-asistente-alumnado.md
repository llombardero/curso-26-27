# S209 — Salida por pantalla y mensajes de MiniJarvis

## Objetivo

Diseñar mensajes de consola claros, combinar texto y datos correctamente y evitar que MiniJarvis prometa funciones que H1 todavía no tiene.

## 1. Un mensaje debe informar

Compara:

```text
Dato:
```

```text
Escribe un nombre ficticio:
```

El segundo mensaje explica qué debe hacer la persona y qué tipo de dato se espera.

Otro contraste:

```text
Hecho.
```

```text
Horas registradas: 4
```

Una salida útil permite entender qué ocurrió sin leer el código.

## 2. `print` y `println`

```java
System.out.print("Nombre ficticio: ");
System.out.println("Laura");
System.out.println("Registro completado.");
```

- `print` deja el cursor en la misma línea.
- `println` añade un salto de línea al final.

Usa `print` para una pregunta cuando quieras que la respuesta aparezca a continuación. Usa `println` para mensajes completos.

## 3. Literales y concatenación

Un literal de texto se escribe entre comillas dobles:

```java
String nombreUsuario = "Laura";
System.out.println("Hola, " + nombreUsuario + ".");
```

El operador `+` concatena textos. Debes incluir los espacios y signos de puntuación dentro de los literales.

Incorrecto:

```java
System.out.println("Hola," + nombreUsuario + ".");
```

Salida:

```text
Hola,Laura.
```

Correcto:

```java
System.out.println("Hola, " + nombreUsuario + ".");
```

## 4. Texto y operaciones

Predice estas salidas:

```java
System.out.println(2 + 3);
System.out.println("Resultado: " + 2 + 3);
System.out.println("Resultado: " + (2 + 3));
```

Resultados:

```text
5
Resultado: 23
Resultado: 5
```

Java evalúa de izquierda a derecha cuando concatena con texto. Los paréntesis indican que la suma debe realizarse antes de concatenar.

## 5. No prometas funciones inexistentes

Mensaje adecuado para H1:

```text
Hola, soy MiniJarvis. Puedo registrar un dato y mostrar un cálculo sencillo.
```

Mensaje inadecuado:

```text
Recuerdo todas tus conversaciones y puedo responder cualquier pregunta.
```

H1 no tiene memoria persistente ni conexión con una IA real. La interfaz debe describir solo lo que el programa hace de verdad.

## 6. Diseña antes de programar

Propón al menos dos versiones del saludo y compáralas con estos criterios:

- claridad;
- brevedad;
- tono coherente;
- puntuación correcta;
- funciones descritas con precisión.

Registra la opción elegida y una justificación.

Ejemplo:

```text
Elegimos «Hola, soy MiniJarvis. Vamos a registrar tus horas de estudio.»
porque presenta el programa y anticipa la entrada sin prometer memoria ni IA.
```

## 7. Actividad

1. Implementa el saludo elegido.
2. Declara `String nombreUsuario` con un nombre ficticio.
3. Muestra un mensaje que combine texto y la variable.
4. Añade una operación sencilla con paréntesis.
5. Ejecuta y revisa espacios, tildes, mayúsculas y puntuación.
6. Pide a otra persona que interprete la salida sin ver el código.

## Evidencia verificable

Conserva:

- las dos propuestas iniciales;
- la decisión justificada;
- el fragmento de código final;
- la salida observada;
- la corrección realizada después de probarla.

## Errores frecuentes

- Mensajes como «Dato» o «Hecho» sin contexto.
- Olvidar espacios al concatenar.
- Esperar que `"Resultado: " + 2 + 3` sume antes de concatenar.
- Describir memoria, IA o funciones que no existen.
- Cambiar el código sin volver a leer la salida completa.

## Autoevaluación

Comprueba que puedes:

- distinguir `print` y `println`;
- construir una concatenación con puntuación correcta;
- predecir una expresión que mezcla texto y números;
- justificar un mensaje por su claridad;
- detectar una promesa que queda fuera de H1.

## Seguridad y uso de IA

Los nombres y datos de ejemplo deben ser ficticios. Si una IA propone mensajes, revisa que sean breves, verdaderos y coherentes con las funciones reales de H1.
