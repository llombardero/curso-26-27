# H1.7 — Entrada por teclado con Scanner

## Entrada por teclado con Scanner

| Hoy vas a… | Al terminar debes poder… |
|---|---|
| Recibir datos desde teclado, convertir texto a número y utilizarlos en expresiones sencillas. | Pedir un nombre y un dato numérico, almacenarlos, realizar un cálculo y comprobar una comparación sin utilizar todavía estructuras de decisión. |

**Tiempo previsto:** 45 minutos.
**Hito:** H1.
**Fase HEXA:** Ejecutar.
**Modalidad:** Individual → contraste por parejas.

---

## Material que necesitas

- Un ordenador con JDK e IntelliJ disponibles.
- El proyecto H1.
- El capítulo 02 del libro como referencia.

Utiliza datos ficticios para las pruebas.

---

## 1. Punto de partida

Hasta ahora `userName` tenía un valor escrito directamente en el código:

```java
String userName = "Laura";
```

Hoy MiniJarvis empezará a recibir información durante la ejecución.

Para leer desde teclado utilizaremos `Scanner`.

---

## 2. Importa Scanner

Antes de utilizar `Scanner`, añade al principio del archivo:

```java
import java.util.Scanner;
```

Después, dentro de `main`, crea un objeto:

```java
Scanner scanner = new Scanner(System.in);
```

Aunque todavía no hayamos estudiado en profundidad clases, objetos y constructores, puedes reconocer que estamos utilizando una clase que Java ya proporciona.

Por ahora debes saber para qué la usamos:

```text
teclado
   ↓
Scanner
   ↓
programa
```

---

## 3. Pide el nombre

Puedes mostrar una pregunta con:

```java
System.out.print("¿Cómo te llamas? ");
```

y leer la respuesta mediante:

```java
String userName = scanner.nextLine();
```

Después utiliza la variable:

```java
System.out.println("Hola, " + userName + ".");
```

Ejecuta varias veces con nombres ficticios diferentes.

Comprueba que ya no necesitas cambiar el código para modificar el nombre.

---

## 4. `print` y `println`

Compara:

```java
System.out.print("¿Cómo te llamas? ");
```

con:

```java
System.out.println("¿Cómo te llamas?");
```

`println` pasa a una nueva línea después de mostrar el texto.

`print` no lo hace.

Prueba ambas versiones y observa la diferencia en la consola.

Decide cuál resulta más adecuada para formular la pregunta.

---

## 5. Leer un número como texto

Ahora MiniJarvis preguntará:

```text
¿Cuántas horas has practicado Programación?
```

Utiliza:

```java
System.out.print("¿Cuántas horas has practicado Programación? ");
String hoursText = scanner.nextLine();
```

Aunque escribas:

```text
4
```

`nextLine()` devuelve texto.

En este momento:

```java
hoursText
```

es un `String`.

---

## 6. Convertir texto a número

Para realizar cálculos necesitamos convertir ese texto.

Utiliza:

```java
int studyHours = Integer.parseInt(hoursText);
```

Ahora podemos distinguir:

```text
"4"   → texto
 4    → número entero
```

La variable:

```java
hoursText
```

almacena texto.

La variable:

```java
studyHours
```

almacena un entero.

---

## 7. Realiza un cálculo sencillo

Utiliza el número convertido para calcular un nuevo valor.

Por ejemplo:

```java
int nextWeekGoal = studyHours + 1;
```

Después muestra el resultado:

```java
System.out.println(
        "Si la próxima semana practicas una hora más, serán "
        + nextWeekGoal
        + " horas."
);
```

Antes de ejecutar con:

```text
4
```

predice qué resultado aparecerá.

Después compruébalo.

Prueba también con otro número.

---

## 8. Comprueba una comparación

Una comparación puede producir un valor `boolean`.

Por ejemplo:

```java
boolean enoughPractice = studyHours >= 3;
```

Muestra el resultado:

```java
System.out.println(enoughPractice);
```

Prueba con:

```text
4
```

y después con:

```text
2
```

Antes de cada ejecución, predice si aparecerá:

```text
true
```

o:

```text
false
```

Hoy solo observamos el resultado de la comparación.

**No utilizamos todavía ese resultado para decidir qué instrucciones ejecutar.**

Eso llegará en H2.

---

## 9. Integra el diálogo de H1

Tu programa puede quedar conceptualmente así:

```text
presentación
     ↓
preguntar nombre
     ↓
leer nombre
     ↓
saludar
     ↓
preguntar horas
     ↓
leer texto
     ↓
convertir a número
     ↓
realizar cálculo
     ↓
mostrar resultado
```

Un ejemplo orientativo de ejecución:

```text
Hola, soy MiniJarvis.
¿Cómo te llamas? Laura
Hola, Laura.
¿Cuántas horas has practicado Programación? 4
Si la próxima semana practicas una hora más, serán 5 horas.
```

Tu redacción puede ser diferente.

---

## 10. Prueba con varios datos válidos

Realiza al menos estas comprobaciones.

### Prueba A

```text
Nombre: Laura
Horas: 4
```

Predice el resultado del cálculo antes de ejecutar.

### Prueba B

Utiliza otro nombre ficticio y otro número.

Comprueba que:

- cambia el saludo;
- cambia el cálculo;
- no has dejado esos valores escritos directamente en los mensajes.

---

## 11. Prueba con una entrada no numérica

Cuando MiniJarvis pregunte las horas, escribe:

```text
cuatro
```

Observa qué ocurre al ejecutar:

```java
Integer.parseInt(hoursText);
```

No necesitas controlar todavía este error.

No añadas `try/catch` si aún no lo has estudiado.

En este momento debes poder explicar:

```text
qué dato recibió el programa
qué conversión intentó realizar
por qué no pudo obtener un int
```

---

## 12. Qué NO hacemos todavía

En H1.7 no necesitas:

```text
[ ] usar if;
[ ] mostrar mensajes distintos según las horas;
[ ] repetir la pregunta cuando hay un error;
[ ] construir un menú;
[ ] utilizar bucles;
[ ] controlar excepciones;
```

No adelantes H2 para hacer que el programa parezca más completo.

El objetivo es comprender cada paso de H1.

---

## 13. Resultado observable

Al terminar debes poder demostrar directamente:

```text
[ ] He importado Scanner.
[ ] He creado un Scanner asociado a System.in.
[ ] Pido un nombre.
[ ] Leo el nombre con nextLine().
[ ] Utilizo el nombre en una salida.
[ ] Pido un dato numérico.
[ ] Leo inicialmente ese dato como texto.
[ ] Convierto el texto mediante Integer.parseInt().
[ ] Realizo un cálculo sencillo.
[ ] Muestro el resultado.
[ ] Puedo realizar una comparación y obtener un boolean.
[ ] He probado al menos dos entradas numéricas válidas.
[ ] He observado qué ocurre con una entrada no numérica.
[ ] No he utilizado todavía estructuras de decisión ni repetición.
```

La propia ejecución permite comprobar el comportamiento.

No necesitas capturas ni una tabla independiente de pruebas.

---

## 14. Fuente canónica

El resultado técnico permanece en el proyecto H1.

No crees:

- capturas rutinarias de la consola;
- una tabla independiente de entradas y salidas;
- un informe sobre `Scanner`;
- un informe sobre conversiones;
- una ficha específica del error observado;
- una copia del código en otro documento.

Si aparece un aprendizaje individual especialmente significativo, puede anotarse brevemente en el diario.

Si surge una decisión o bloqueo relevante para el equipo, puede registrarse en Scrum.

---

## 15. Uso de IA

Antes de consultar una IA, intenta identificar:

```text
qué has introducido
qué tipo tiene ahora
qué tipo necesitas
qué operación estás intentando realizar
qué resultado esperabas
qué ocurrió realmente
```

Puedes utilizar IA para:

- comprender qué hace `Scanner`;
- comprender `nextLine()`;
- entender `Integer.parseInt`;
- interpretar el error producido por una entrada no numérica;
- revisar una explicación que ya hayas razonado.

No utilices IA para añadir `if`, bucles, excepciones u otras soluciones que todavía no has estudiado.

Si su intervención es significativa, deja una anotación breve en la fuente correspondiente.

No es necesario registrar consultas triviales.

Nunca introduzcas datos personales, contraseñas, tokens ni claves API.

---

## 16. Si te bloqueas

Antes de pedir ayuda, responde:

```text
¿Qué pregunta muestra el programa?

¿Qué he escrito en la consola?

¿En qué variable se ha guardado?

¿Qué tipo tiene esa variable?

¿Estoy intentando convertirla?

¿Qué esperaba obtener?

¿Qué ha ocurrido realmente?
```

Después formula una pregunta concreta.

Cambia una sola cosa cada vez.

---

## 17. Cierre

Sobre tu propio programa, explica:

1. para qué utilizas `Scanner`;
2. qué hace `nextLine()`;
3. por qué el nombre puede guardarse directamente en un `String`;
4. por qué las horas necesitan convertirse para realizar cálculos;
5. qué hace `Integer.parseInt`;
6. qué cálculo has realizado;
7. qué produce una comparación como `studyHours >= 3`;
8. qué ocurre si introduces `cuatro`;
9. por qué todavía no utilizamos `if` para mostrar una recomendación.

La sesión está completada cuando puedes introducir datos diferentes, comprobar cómo cambian los resultados y explicar el recorrido desde la entrada por teclado hasta la salida por consola.
