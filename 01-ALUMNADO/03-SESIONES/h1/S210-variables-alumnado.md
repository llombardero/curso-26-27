# H1.5 — Variables

## Variables

| Hoy vas a… | Al terminar debes poder… |
|---|---|
| Guardar y modificar datos mediante variables. | Declarar, inicializar, utilizar y cambiar variables sencillas explicando qué representa cada parte. |

**Tiempo previsto:** 45 minutos.
**Hito:** H1.
**Fase HEXA:** Planificar.
**Modalidad:** Individual.

---

## Material que necesitas

- Un ordenador con JDK e IntelliJ disponibles.
- El proyecto H1.
- El capítulo 02 del libro como referencia.

Utiliza únicamente datos ficticios en los ejemplos.

---

## 1. Punto de partida

Hasta ahora los mensajes de MiniJarvis estaban escritos directamente en el código.

Por ejemplo:

```java
System.out.println("Hola, Laura.");
```

Si queremos que un dato pueda cambiar sin reescribir todos los mensajes, necesitamos guardarlo.

Podemos utilizar una variable:

```java
String userName = "Laura";
```

y después:

```java
System.out.println("Hola, " + userName + ".");
```

---

## 2. Qué representa una variable

Observa:

```java
String userName = "Laura";
```

Podemos distinguir:

```text
String      userName      "Laura"
  ↓            ↓             ↓
tipo         nombre         valor
```

En esta instrucción estamos declarando e inicializando una variable.

La variable se llama:

```text
userName
```

y en este momento contiene:

```text
Laura
```

---

## 3. Declarar, inicializar y asignar

Estas acciones están relacionadas, pero no son exactamente lo mismo.

### Declarar

```java
String userName;
```

Aquí indicamos que existirá una variable llamada `userName` de tipo `String`.

### Inicializar

```java
userName = "Laura";
```

Le damos un primer valor.

### Declarar e inicializar a la vez

```java
String userName = "Laura";
```

Es una forma habitual de hacerlo cuando ya conocemos el valor inicial.

### Cambiar el valor

Más adelante podemos escribir:

```java
userName = "Álex";
```

No estamos creando otra variable.

Estamos asignando un nuevo valor a la que ya existe.

---

## 4. Predice antes de ejecutar

Observa:

```java
String userName = "Laura";

System.out.println(userName);

userName = "Álex";

System.out.println(userName);
```

Antes de ejecutarlo, responde:

```text
¿Qué mostrará la primera salida?

¿Qué mostrará la segunda?

¿Se han creado una o dos variables?
```

Después ejecútalo y comprueba tu predicción.

---

## 5. Utiliza una variable varias veces

Añade a tu programa una variable:

```java
String userName = "Laura";
```

Utilízala en varios mensajes.

Por ejemplo:

```java
System.out.println("Hola, " + userName + ".");
System.out.println(userName + ", estás utilizando MiniJarvis.");
```

Ejecuta.

Después cambia únicamente:

```java
"Laura"
```

por otro nombre ficticio.

Vuelve a ejecutar.

Comprueba qué mensajes cambian sin haber tenido que modificar cada texto por separado.

---

## 6. Elige nombres claros

Compara:

```java
String n = "Laura";
```

con:

```java
String userName = "Laura";
```

Ambos nombres pueden funcionar técnicamente.

Pero uno comunica mejor la intención del dato.

Revisa los nombres de tus variables con estas preguntas:

```text
¿Puedo saber qué representa sin buscar por todo el programa?

¿Describe el dato?

¿Es suficientemente concreto?

¿Mantiene una forma de escribir coherente?
```

En estos primeros programas utiliza nombres sencillos y descriptivos.

---

## 7. Otros tipos de datos

No todos los datos son texto.

Observa:

```java
String userName = "Laura";
int studyHours = 4;
double average = 7.5;
boolean active = true;
char initial = 'L';
```

Cada variable almacena un tipo de información diferente.

Relaciona:

| Dato | Tipo razonable |
|---|---|
| nombre de una persona | `String` |
| número entero de horas | `int` |
| valor con decimales | `double` |
| verdadero o falso | `boolean` |
| un único carácter | `char` |

No necesitas utilizar todos estos tipos en MiniJarvis hoy.

Sí debes reconocer que elegir el tipo depende del dato que queremos guardar.

---

## 8. Practica la elección del tipo

Decide qué tipo utilizarías para:

```text
nombre del usuario
edad
nota media
programa activo o no
inicial de un nombre
número de intentos
```

Justifica al menos dos elecciones.

No basta con escribir el nombre del tipo.

Explica qué característica del dato te lleva a elegirlo.

---

## 9. Variable y literal

Observa:

```java
String userName = "Laura";
```

Aquí:

```text
userName
```

es el nombre de una variable.

Mientras que:

```text
"Laura"
```

es un valor escrito directamente en el código.

Ese valor es un literal.

Otro ejemplo:

```java
int studyHours = 4;
```

`4` es un literal entero.

Por ahora lo importante es distinguir:

```text
variable → tiene nombre y puede almacenar un valor

literal → valor escrito directamente en el código
```

---

## 10. Llévalo a MiniJarvis

En tu versión H1:

1. crea una variable `userName` con un nombre ficticio;
2. utilízala al menos en dos mensajes;
3. ejecuta;
4. cambia su valor;
5. vuelve a ejecutar;
6. comprueba qué ha cambiado.

Por ahora el valor seguirá escrito directamente en el código.

En una sesión posterior aprenderemos a recibirlo desde el teclado.

No adelantes todavía `Scanner`.

---

## 11. Resultado observable

Al terminar debes poder demostrar directamente:

```text
[ ] Tengo al menos una variable en el programa.
[ ] Puedo señalar su tipo.
[ ] Puedo señalar su nombre.
[ ] Puedo señalar su valor actual.
[ ] Sé distinguir declarar, inicializar y asignar.
[ ] Puedo modificar el valor de una variable.
[ ] Puedo utilizar una variable en varios mensajes.
[ ] Utilizo nombres comprensibles.
[ ] Reconozco varios tipos básicos.
[ ] Distingo variable y literal.
```

La comprobación se realiza sobre el propio programa.

No necesitas capturas ni una ficha adicional.

---

## 12. Fuente canónica

El código de esta sesión permanece en el proyecto H1.

No crees:

- una captura del código;
- una tabla independiente de variables;
- un informe de la sesión;
- una copia del programa en otro documento.

Si aparece un aprendizaje individual especialmente significativo, puede anotarse brevemente en el diario.

Si aparece un bloqueo técnico relevante para el equipo, puede registrarse en Scrum.

---

## 13. Uso de IA

Primero intenta identificar por ti mismo:

```text
qué dato necesito guardar
qué tipo tiene
qué nombre lo describe
qué valor contiene
```

Puedes utilizar IA para:

- pedir una explicación de una variable;
- entender un error de tipos;
- comparar dos nombres de variables;
- revisar una predicción que ya hayas razonado.

No la utilices para sustituir la lectura y modificación de tu propio código.

Si su intervención es significativa, deja una anotación breve en la fuente correspondiente.

No es necesario registrar consultas triviales.

Nunca introduzcas datos personales, contraseñas, tokens ni claves API.

---

## 14. Si te bloqueas

Antes de pedir ayuda, señala:

```text
¿Qué dato quiero guardar?

¿Qué tipo estoy utilizando?

¿Cómo se llama la variable?

¿Qué valor tiene ahora?

¿Qué esperaba que apareciera?

¿Qué aparece realmente?
```

Después formula una pregunta concreta.

Cambia una sola cosa cada vez.

---

## 15. Cierre

Sobre tu propio programa, explica:

1. qué variable has creado;
2. qué significa su tipo;
3. por qué has elegido ese nombre;
4. qué valor contiene;
5. en qué mensajes se utiliza;
6. qué ocurre al cambiar su valor;
7. cuál es la diferencia entre la variable y el literal que contiene.

La sesión está completada cuando puedes modificar el valor de una variable, volver a ejecutar MiniJarvis y explicar por qué cambia la salida.
