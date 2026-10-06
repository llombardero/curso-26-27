# H1 — Primer asistente por consola

## Ficha para el alumnado

**Curso:** 1.º DAW — Programación

**Proyecto anual:**

```text
MiniJarvis: programa Java progresivo que crecerá por hitos durante el curso
```

---

## 1. Reto

Vas a construir la primera versión técnica de MiniJarvis.

Será un programa Java pequeño que se ejecutará por consola y que debes poder comprender completamente.

Al terminar H1 debes ser capaz de:

- localizar la estructura básica del programa;
- explicar dónde comienza la ejecución;
- mostrar mensajes por consola;
- utilizar variables, constantes y literales;
- recibir datos mediante `Scanner`;
- convertir una entrada textual a un valor numérico;
- realizar un cálculo sencillo;
- producir y mostrar una comparación booleana sin cambiar el flujo del programa;
- ejecutar y comprobar el programa;
- localizar y corregir errores básicos;
- explicar cómo se ejecuta y qué hace.

El objetivo no es crear un asistente avanzado.

El objetivo es construir una primera versión **pequeña, ejecutable, comprobable y defendible**.

---

## 2. Qué NO entra todavía

En H1 todavía no debes incorporar:

```text
[ ] Menús.
[ ] Bucles.
[ ] Decisiones con if o if/else.
[ ] Bifurcaciones.
[ ] switch.
[ ] Memoria.
[ ] Listas, sets o mapas.
[ ] Varias clases propias.
[ ] Ficheros.
[ ] Persistencia.
[ ] Patrones de diseño.
[ ] Conexiones con servicios externos.
[ ] Gemini, Jarvis u otra IA real integrada en el programa.
```

Todo eso llegará cuando hayamos aprendido los conceptos necesarios.

No mejores MiniJarvis adelantando técnicas que todavía no puedes explicar.

---

## 3. Resultado observable

Tu programa debe realizar un diálogo sencillo.

Por ejemplo:

```text
Hola, soy MiniJarvis.
¿Cómo te llamas? Laura
Encantado de conocerte, Laura.
¿Cuántas horas has practicado Programación? 4
Si la próxima semana practicas una hora más, serán 5 horas.
¿Has alcanzado 4 horas de práctica? true
```

La salida concreta puede ser diferente.

Lo importante es que puedas explicar de dónde sale cada dato y cada mensaje.

No necesitas todavía decidir si una cantidad es «buena» o «mala», repetir preguntas ni ejecutar acciones diferentes según la respuesta.

---

## 4. Cómo trabajaremos el hito

H1 recorre un ciclo HEXA completo.

### Equipos — Durante todo el hito

El equipo mantiene organizado el trabajo, las tareas y las decisiones significativas.

Cada persona debe poder explicar y modificar el código aunque el producto sea compartido.

### Activar — Entender el reto

Antes de programar debes tener claro:

- qué debe hacer esta primera versión;
- qué no debe hacer todavía;
- qué resultado podremos observar al ejecutarla.

Pregunta clave:

```text
¿Cuál es la versión más pequeña de MiniJarvis
que podemos construir, comprobar y explicar?
```

### Investigar — Aprender lo necesario

Trabajaremos progresivamente:

- proyecto Java;
- `Main.java`;
- clase `Main`;
- método `main`;
- instrucciones;
- salida por consola;
- variables;
- tipos básicos;
- constantes y literales;
- operadores;
- `Scanner`;
- entrada por teclado;
- conversión de texto a número;
- errores iniciales de compilación y ejecución.

No necesitas estudiar contenidos de hitos posteriores para completar H1.

### Idear — Decidir tu primera versión

Antes de escribir todo el programa, decide:

- qué saludo mostrará;
- qué datos preguntará;
- qué nombres tendrán las variables;
- qué dato será constante;
- qué cálculo sencillo realizará;
- qué mensajes formarán la salida.

Mantén la solución pequeña.

### Planificar — Organizar el trabajo

Convierte lo anterior en tareas pequeñas.

Por ejemplo:

```text
Crear proyecto.
        ↓
Conseguir que Main se ejecute.
        ↓
Mostrar mensajes.
        ↓
Añadir variables y constantes.
        ↓
Leer datos.
        ↓
Convertir un dato numérico.
        ↓
Realizar un cálculo y mostrar una comparación booleana.
        ↓
Comprobar.
        ↓
Limpiar el código.
        ↓
Completar README.
        ↓
Preparar demo y defensa.
```

El equipo mantiene las tareas en su Scrum.

No necesitas crear otro documento para repetir esta planificación.

### Ejecutar — Construir y comprobar

Implementa el programa de forma incremental.

No escribas todo antes de ejecutarlo.

Utiliza este ciclo:

```text
cambio pequeño
     ↓
ejecución
     ↓
observación
     ↓
corrección si hace falta
     ↓
siguiente cambio
```

### Comunicar — Demostrar lo aprendido

Al cerrar H1 debes poder:

- ejecutar MiniJarvis;
- mostrar su funcionamiento;
- localizar las partes principales del código;
- explicar una variable y una constante;
- explicar cómo entra la información;
- explicar la conversión numérica;
- explicar el cálculo y el resultado `boolean` de la comparación;
- modificar una parte sencilla;
- explicar algún error que hayas encontrado y cómo lo resolviste.

La defensa se realiza sobre el producto y sus evidencias reales.

No necesitas crear un informe de defensa.

---

## 5. Producto esperado

La versión H1 debe contener como mínimo:

```text
h1-primer-asistente/
├── README.md
└── src/
    └── Main.java
```

`Main.java` debe incluir una solución adecuada al nivel del hito con:

- clase `Main`;
- método `main`;
- mensajes por consola;
- nombres claros;
- al menos una variable de texto;
- al menos una constante;
- uso de `Scanner`;
- entrada de texto;
- entrada que pueda convertirse a número;
- una conversión numérica;
- un cálculo sencillo;
- salida que muestre el resultado;
- una comparación sencilla cuyo resultado `boolean` se almacene o utilice de forma visible y se muestre;
- flujo secuencial, sin `if`, `if/else` ni bifurcaciones;
- comentarios útiles cuando aporten contexto, evitando comentar lo obvio.

---

## 6. Ruta técnica

### Paso 1 — Proyecto ejecutable

```text
[ ] Crear o abrir el proyecto Java.
[ ] Localizar src/Main.java.
[ ] Comprobar que Main se ejecuta.
```

### Paso 2 — Primera salida

```text
[ ] Mostrar un saludo.
[ ] Mostrar varios mensajes en orden.
[ ] Modificar uno y comprobar el cambio.
```

### Paso 3 — Variables y constantes

```text
[ ] Utilizar una variable con un nombre claro.
[ ] Crear una constante para un dato que no debe cambiar.
[ ] Reconocer los literales utilizados.
```

Ejemplos:

```java
final String AGENT_NAME = "MiniJarvis";
String userName;
```

### Paso 4 — Entrada por teclado

```text
[ ] Crear un Scanner.
[ ] Pedir el nombre.
[ ] Guardarlo.
[ ] Utilizarlo posteriormente en una salida.
```

### Paso 5 — Entrada numérica, cálculo y comparación

```text
[ ] Leer un número inicialmente como texto.
[ ] Convertirlo a un tipo numérico.
[ ] Realizar un cálculo sencillo.
[ ] Mostrar el resultado.
[ ] Realizar una comparación sencilla con el valor numérico.
[ ] Guardar o utilizar de forma visible su resultado booleano.
[ ] Mostrar `true` o `false` sin decidir qué instrucciones se ejecutan.
```

No necesitas todavía tomar decisiones mediante `if`.

### Paso 6 — Limpieza

Revisa:

```text
[ ] Nombres claros.
[ ] Indentación.
[ ] Mensajes comprensibles.
[ ] Comentarios útiles y no redundantes.
[ ] Código que pertenece realmente a H1.
```

### Paso 7 — Comprobación

Ejecuta la versión completa al menos con:

```text
un nombre
otro nombre
un número válido
otro número válido
una entrada no numérica para observar qué ocurre
```

En este momento no necesitas controlar todos los errores de entrada.

Sí debes poder explicar qué ha ocurrido.

---

## 7. README del hito

El README permite volver posteriormente al proyecto y saber qué versión es y cómo utilizarla.

Debe contener únicamente información útil.

Una estructura suficiente es:

```markdown
# H1 — Primer asistente por consola

## Qué hace

Breve explicación de esta versión.

## Cómo ejecutar

Pasos necesarios para ejecutar el programa.

## Comprobación

Un ejemplo breve de entrada y salida que permita reconocer el funcionamiento.

## Límites de H1

Qué funcionalidades todavía no incorpora.
```

No necesitas añadir capturas de consola si el comportamiento puede reproducirse ejecutando el programa.

---

## 8. Criterios de aceptación

H1 está técnicamente preparado para su cierre cuando puedes demostrar que:

```text
[ ] Existe src/Main.java.
[ ] La clase Main es reconocible.
[ ] Existe el método main.
[ ] El programa compila y se ejecuta.
[ ] Muestra mensajes por consola.
[ ] Recibe información mediante Scanner.
[ ] Utiliza variables con nombres claros.
[ ] Utiliza al menos una constante.
[ ] Convierte una entrada textual a número.
[ ] Realiza al menos un cálculo sencillo.
[ ] Produce y muestra una comparación booleana sin bifurcación.
[ ] El cálculo y el resultado booleano pueden comprobarse ejecutando el programa.
[ ] El código se mantiene dentro del alcance de H1.
[ ] El README explica qué hace y cómo se ejecuta.
```

Cumplir la lista no sustituye comprender el programa.

---

## 9. Uso de IA en H1

La IA puede ayudarte a aprender, por ejemplo, para:

- pedir una explicación de un concepto;
- entender un mensaje de error;
- comparar dos fragmentos;
- revisar la claridad de una explicación;
- formular preguntas sobre código que ya estás estudiando.

No debes utilizarla para sustituir tu aprendizaje.

No es válido:

- generar el programa completo y entregarlo sin comprenderlo;
- incorporar técnicas que todavía no has estudiado;
- aceptar código sin probarlo;
- presentar como propio algo que no puedes explicar o modificar.

Si la IA ha tenido una **intervención significativa** en el producto evaluable, deja una anotación breve en la fuente correspondiente:

- diario individual, si afecta principalmente a tu aprendizaje o trabajo;
- Scrum, si forma parte de una decisión significativa del equipo.

Debes poder explicar:

```text
qué necesitabas
qué aportó la IA
qué aceptaste, modificaste o descartaste
cómo comprobaste el resultado
```

No necesitas registrar consultas triviales.

Nunca introduzcas datos personales, contraseñas, tokens, claves API ni otros secretos.

---

## 10. Defensa

La defensa se realiza sobre tu MiniJarvis.

Prepárate para cuestiones como:

```text
¿Dónde empieza la ejecución?
¿Qué representa Main?
¿Qué hace esta instrucción?
¿Qué variable almacena el nombre?
¿Por qué este dato es una constante?
¿Qué hace Scanner?
¿Qué devuelve nextLine()?
¿Por qué necesitas convertir este texto?
¿Qué cálculo estás realizando?
¿Qué comparación estás realizando y cuándo produce true o false?
¿Por qué esa comparación no decide el flujo en H1?
¿Qué ocurre si escribes texto donde esperabas un número?
¿Cómo ejecutas esta versión?
¿Por qué todavía no hay menú ni bucles?
```

También se te puede pedir una pequeña modificación.

Por ejemplo:

```text
cambia un mensaje
cambia el cálculo
renombra una variable
localiza una constante
explica el resultado antes de ejecutar
```

La finalidad es comprobar comprensión y autoría, no memorizar respuestas.

---

## 11. Checklist final

Antes de cerrar H1 comprueba:

```text
[ ] Puedo ejecutar la versión que voy a presentar.
[ ] Puedo mostrar su resultado directamente.
[ ] Puedo localizar Main y main.
[ ] Puedo explicar mis variables.
[ ] Puedo explicar mis constantes.
[ ] Puedo explicar cómo entra la información.
[ ] Puedo explicar la conversión numérica.
[ ] Puedo explicar el cálculo.
[ ] Puedo localizar la comparación y predecir el resultado booleano.
[ ] Puedo explicar que H1 no utiliza ese resultado para bifurcar el flujo.
[ ] Puedo modificar una parte sencilla.
[ ] No he adelantado contenidos de otros hitos.
[ ] El README permite saber qué hace y cómo ejecutar esta versión.
[ ] Si la IA tuvo una intervención significativa, está reflejada en diario o Scrum.
[ ] Puedo explicar el código importante sin depender de una respuesta generada.
```

---

## 12. Qué conservar

La fuente principal de la evidencia técnica es el propio proyecto.

Conserva:

- código y versiones en el repositorio;
- instrucciones de ejecución, límites y decisiones técnicas necesarias en el README;
- tareas, decisiones y bloqueos significativos de equipo en Scrum;
- aprendizajes individuales significativos en el diario.

No necesitas crear para H1:

- un informe de ejecución;
- capturas rutinarias;
- una tabla independiente de pruebas;
- un documento de defensa;
- un registro independiente de IA;
- un portfolio específico del hito.

La versión evaluada se identificará mediante el mecanismo de entrega indicado para el hito.

---

## 13. Idea clave

H1 no pretende impresionar por su complejidad.

Pretende establecer una forma de trabajar que repetiremos durante el curso:

```text
comprender
    ↓
construir
    ↓
ejecutar
    ↓
comprobar
    ↓
explicar
    ↓
mejorar
```

Una primera versión pequeña que puedes ejecutar, modificar y explicar es la base sobre la que crecerá MiniJarvis.
