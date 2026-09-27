# S206 — Píldoras: alcance y calidad de H1

> Material de consulta de la sesión S206. Lee cada ejemplo y explica por qué cumple —o no— el criterio indicado. No necesitas añadir más funciones a tu MiniJarvis.

## 1. ¿Qué hace bueno a un primer programa?

Un primer programa debe ser **correcto**, **eficiente** y **mantenible**.

- **Correcto:** hace lo que se ha pedido y podemos comprobarlo.
- **Eficiente:** resuelve el reto sin trabajo ni complejidad innecesarios.
- **Mantenible:** se entiende y se puede modificar sin romperlo fácilmente.

### Ejemplo 1 — Correcto

Requisito: «Al ejecutar, muestra un saludo».

```java
System.out.println("Hola, soy MiniJarvis.");
```

Es correcto porque la salida permite comprobar el requisito. En cambio, un programa que compila pero no muestra el saludo todavía no cumple el requisito.

### Ejemplo 2 — Eficiente

Para H1 basta con pedir un nombre y responder. No necesitamos todavía un menú, un bucle, una base de datos ni una conexión con una IA real.

```java
String userName = "Laura";
System.out.println("Encantado, " + userName + ".");
```

Esta solución es adecuada al alcance. Añadir cinco clases y veinte opciones que nadie ha pedido produciría más código que mantener, pero no demostraría mejor el objetivo de H1.

### Ejemplo 3 — Mantenible

```java
String userName = "Laura";
System.out.println("Encantado, " + userName + ".");
```

Se entiende mejor que:

```java
String x = "Laura";
System.out.println("Encantado, " + x + ".");
```

Los dos ejemplos producen la misma salida, pero `userName` explica qué dato se guarda.

### Ejemplo 4 — Los tres criterios juntos

```java
final String ASSISTANT_NAME = "MiniJarvis";
String userName = "Álex";
System.out.println("Hola, soy " + ASSISTANT_NAME + ".");
System.out.println("Encantado, " + userName + ".");
```

- Es correcto si esos son los mensajes pedidos.
- Es eficiente porque no añade funciones ajenas a H1.
- Es mantenible porque los nombres explican la intención y el nombre fijo se guarda una sola vez.

## Errores frecuentes

- Confundir «compila» con «es correcto». Compilar solo significa que Java ha podido preparar el programa; aún falta comprobar el comportamiento.
- Confundir «eficiente» con «va muy rápido». En H1 importa sobre todo no añadir complejidad innecesaria.
- Pensar que más líneas o más funciones siempre significan mejor programa.
- Usar nombres como `x`, `dato1` o `a` cuando podemos expresar qué guardan.

## Comprueba que lo entiendes

1. ¿Qué requisito demuestra cada línea visible de tu programa?
2. ¿Qué parte quitarías si no pertenece al alcance de H1?
3. Señala un nombre que ayude a entender tu código.
4. Explica por qué «compila» no basta para afirmar que el programa es correcto.
