# S209 - Idear - Salida por pantalla y mensajes del asistente

| Dato | Valor |
|---|---|
| Hito | H1 — Primer asistente ejecutable |
| Duración prevista | 45 minutos |
| Fase HEXA del hito | Idear — proponer soluciones |

> Basada en `00-GUION-DOCENTE-H1-COMPLETO.md`. Selecciona y desarrolla los conceptos, ejemplos, actividades y evidencias útiles para esta sesión.

## Qué vas a aprender

Al terminar, debes idear mensajes claros antes de programarlos y usar literales y concatenación cuando sea necesario.

## Ideas y ejemplos

Úsala antes de abrir el IDE, para obligar a idear la salida.

La consola también es una interfaz. Aunque sea texto, la persona usuaria debe entender qué ocurre, qué se le pide y qué resultado obtiene. Además, no debemos prometer funciones que H1 no tiene.

Compara estos mensajes con el alumnado:

```text
correcto
```

Frente a:

```text
MiniJarvis se ha iniciado correctamente.
```

```text
Dato:
```

Frente a:

```text
Escribe tu nombre:
```

```text
5
```

Frente a:

```text
Horas de estudio registradas: 5
```

```text
String nombreUsuario initialized successfully.
```

Frente a:

```text
Hola, Laura.
```

```text
Analizando tus datos con inteligencia artificial...
```

Frente a:

```text
Hola, soy MiniJarvis. Esta es mi primera versión por consola.
```

Pregunta al alumnado:

Qué salida ayuda más, qué dato cambia y dónde hacen falta espacios o signos.

Error frecuente que debes cortar:

No escribáis `Puedo recordar todo` si H1 no tiene memoria.

Di también:

El mensaje debe estar pensado para quien usa el programa, no para demostrarle que sabemos Java.

Trabaja ahora literal de texto y concatenación con predicción:

```java
System.out.println("Hola");
```

Pregunta:

Qué parte ha escrito exactamente quien programa.

```java
String nombreUsuario = "Laura";
System.out.println("Hola, " + nombreUsuario);
```

Salida esperada:

```text
Hola, Laura
```

```java
String nombreUsuario = "Laura";
String nombreAsistente = "MiniJarvis";
System.out.println("Hola, " + nombreUsuario + ". Soy " + nombreAsistente + ".");
```

```java
int horasEstudio = 4;
System.out.println("Has estudiado " + horasEstudio + " horas.");
```

Predicción obligatoria:

```java
System.out.println(2 + 3);
System.out.println("Resultado: " + 2 + 3);
```

Pregunta:

Predice ambas salidas antes de ejecutar y explica por qué el signo `+` no se comporta igual en las dos líneas.

## Actividad de la sesión

Todavía no abráis el IDE. Primero escribid dos versiones de saludo, propósito y mensaje final. Después elegid una y justificadla. Solo entonces programadla.

Después:

Programad la salida elegida. Ejecutadla. Pedid a otra persona que lea solo la consola y os diga si entiende qué hace MiniJarvis.

## Evidencia de la sesión

Registrad la decisión de diseño de mensajes y guardad la versión programada.

**Dónde y cómo conservar la evidencia:**

- GitHub: código con mensajes implementados.
- Diario individual: fila breve si la persona ha cambiado o defendido una decisión.
- Moodle: no se entrega todavía.

Qué debe aparecer:

- Mensaje elegido.
- Por qué se elige.
- Qué se cambió después de verlo ejecutado.

Modelo de uso de decisión de mensajes:

```text
Decisión S209:
Elegimos "Hola, soy MiniJarvis" y "Escribe un nombre ficticio" porque son claros y no piden datos personales reales.
Descartamos "MJ v1 correcto" porque no explica qué ocurre.
Después de ejecutar añadimos un punto final y un espacio tras la coma para mejorar la lectura.
```

## Comprueba lo aprendido

Hemos ideado antes de programar. Esa es la clave de hoy. La salida de consola no se improvisa al final: se diseña para que alguien entienda qué ocurre.
