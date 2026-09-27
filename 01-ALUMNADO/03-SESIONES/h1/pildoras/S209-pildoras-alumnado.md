# S209 — Píldoras: mensajes claros y concatenación

> Material de consulta de la sesión S209. Diseña primero lo que leerá la persona usuaria y programa después.

## 1. La consola también es una interfaz

Una interfaz permite que una persona entienda qué ocurre y qué debe hacer. Aunque la consola solo muestre texto, sus mensajes deben ser claros, ordenados y coherentes con el alcance real de H1.

### Ejemplo 1 — Saludo comprensible

Poco claro:

```text
MJ v1
ok
```

Más claro:

```text
Hola, soy MiniJarvis.
Estoy preparado para comenzar.
```

### Ejemplo 2 — Petición concreta

Ambiguo:

```text
Dato:
```

Más claro:

```text
Escribe un nombre ficticio:
```

La segunda versión indica qué dato se espera y recuerda que no necesitamos información personal real.

### Ejemplo 3 — Orden de la conversación

```text
Hola, soy MiniJarvis.
Escribe un nombre ficticio: Laura
Encantado, Laura.
Fin de la primera prueba.
```

El orden ayuda a distinguir presentación, petición, respuesta y cierre.

### Ejemplo 4 — No prometer funciones inexistentes

Evita mensajes como «Puedo recordar todo» o «Estoy conectado a una IA» si H1 todavía no implementa memoria ni IA real. La interfaz debe describir el programa que existe, no el que quizá construiremos después.

## 2. Literal y concatenación

Un literal de texto se escribe entre comillas dobles. El operador `+` permite unir texto y valores.

### Ejemplo 1 — Texto fijo y variable

```java
String userName = "Laura";
System.out.println("Hola, " + userName + ".");
```

Salida:

```text
Hola, Laura.
```

### Ejemplo 2 — Varias piezas

```java
String assistantName = "MiniJarvis";
int version = 1;
System.out.println("Soy " + assistantName + ", versión " + version + ".");
```

Salida:

```text
Soy MiniJarvis, versión 1.
```

### Ejemplo 3 — Espacios y signos

```java
String userName = "Álex";
System.out.println("Encantado," + userName);
```

Produce `Encantado,Álex`. El programa funciona, pero el mensaje no está bien cuidado. La corrección es:

```java
System.out.println("Encantado, " + userName + ".");
```

### Ejemplo 4 — Suma o concatenación

```java
System.out.println(2 + 3);        // 5
System.out.println("2" + "3");  // 23
System.out.println("Total: " + 2 + 3); // Total: 23
```

El tipo y el orden de las piezas cambian el resultado. En esta sesión basta con reconocerlo y predecir la salida.

## Errores frecuentes

- Olvidar espacios o signos dentro de los literales.
- Mostrar mensajes técnicos que la persona usuaria no necesita.
- Confundir `+` como suma numérica con `+` como concatenación.
- Programar la primera idea sin comparar alternativas.

## Comprueba que lo entiendes

1. Mejora un mensaje ambiguo de consola.
2. Predice la salida de los cuatro ejemplos de concatenación.
3. Diseña un saludo, una petición y un cierre coherentes.
4. Explica por qué tu salida no promete funciones ajenas a H1.
