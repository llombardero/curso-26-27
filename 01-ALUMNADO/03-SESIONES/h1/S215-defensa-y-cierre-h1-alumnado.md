# Sesión 215 — Ficha de trabajo del alumnado

## Defensa y cierre H1

| Hoy vas a… | Al terminar debes poder… |
|---|---|
| Demostrar individualmente que comprendes la versión H1 que habéis construido. | Ejecutar, explicar y modificar una parte sencilla de MiniJarvis, reconocer sus límites e identificar qué necesitas reforzar antes de continuar. |

**Tiempo previsto:** 45 minutos.
**Hito:** H1.
**Fase HEXA:** Comunicar.
**Modalidad:** Equipo → defensa individual.

---

## Material que necesitas

- Un ordenador con JDK e IntelliJ disponibles.
- La versión estable de H1 preparada en S214.
- El código real del proyecto.
- El `README.md` actualizado.

Utiliza únicamente datos ficticios durante las demostraciones.

---

## 1. Qué significa defender H1

Defender H1 no significa memorizar una explicación.

Significa poder trabajar sobre el producto real y demostrar:

```text
sé localizarlo
      ↓
sé ejecutarlo
      ↓
sé explicar qué hace
      ↓
sé señalar cómo lo hace
      ↓
sé comprobarlo
      ↓
puedo modificar una parte sencilla
```

El equipo ha construido un producto compartido.

Pero cada persona debe poder demostrar qué ha aprendido.

---

## 2. Producto, comprobación y defensa

En H1 tenemos tres ideas relacionadas, pero diferentes.

```text
PRODUCTO

el programa MiniJarvis que habéis construido


COMPROBACIÓN

ejecutarlo y observar que produce el comportamiento esperado


DEFENSA

explicar el código, justificar decisiones
y realizar una modificación sencilla
```

Que el programa funcione es necesario.

Pero poder ejecutarlo no sustituye comprenderlo.

---

## 3. Comprobación final del equipo

Antes de comenzar las defensas individuales, ejecutad una vez la versión estable de H1.

Comprobad que:

```text
[ ] abre y ejecuta correctamente;
[ ] muestra la presentación prevista;
[ ] pide información mediante Scanner;
[ ] utiliza el nombre introducido;
[ ] recibe el dato numérico;
[ ] realiza la conversión prevista;
[ ] realiza el cálculo;
[ ] muestra un resultado coherente;
[ ] coincide con lo explicado en el README;
[ ] sigue dentro del alcance de H1.
```

Si aparece un problema técnico, corregidlo y volved a comprobar.

---

## 4. Identifica la versión que estás defendiendo

Debes saber qué versión concreta estás mostrando.

Puede estar identificada mediante:

```text
un tag de entrega

o

un commit estable
```

No necesitas utilizar ambos mecanismos.

Debes poder localizar la versión que se presenta y distinguirla de cambios posteriores.

---

## 5. Localiza la estructura del programa

Sobre el código real, debes poder señalar:

```java
public class Main {
    public static void main(String[] args) {
        // ...
    }
}
```

Y explicar con tus palabras:

```text
qué es Main

dónde empieza la ejecución

qué instrucciones pertenecen a main

en qué orden se ejecutan
```

No necesitas recitar una definición de memoria.

Señala las partes directamente en tu código.

---

## 6. Explica una variable

Localiza una variable real del programa.

Por ejemplo:

```java
String userName = scanner.nextLine();
```

Debes poder explicar:

```text
qué tipo tiene

cómo se llama

qué dato guarda

de dónde procede su valor

dónde vuelve a utilizarse
```

Si otra variable de vuestro programa sirve mejor para explicarlo, utiliza esa.

---

## 7. Explica constante, variable y literal

Localiza una constante.

Por ejemplo:

```java
final String AGENT_NAME = "MiniJarvis";
```

Debes poder distinguir:

```text
AGENT_NAME   → constante

"MiniJarvis" → literal
```

y compararla con una variable como:

```java
String userName;
```

Debes poder explicar por qué un dato tiene sentido como constante y otro como variable.

---

## 8. Explica la entrada mediante Scanner

Localiza:

```java
Scanner scanner = new Scanner(System.in);
```

y alguna lectura como:

```java
String userName = scanner.nextLine();
```

Debes poder explicar:

```text
para qué utilizamos Scanner

qué información recibe el programa

qué devuelve nextLine()

en qué variable queda guardada
```

No necesitas explicar todavía en profundidad cómo está construida internamente la clase `Scanner`.

---

## 9. Explica la conversión

Localiza la conversión numérica de vuestro programa.

Por ejemplo:

```java
String hoursText = scanner.nextLine();
int studyHours = Integer.parseInt(hoursText);
```

Debes poder explicar:

```text
por qué hoursText es texto

por qué necesitamos un int para realizar determinados cálculos

qué hace Integer.parseInt

qué ocurre si intentamos convertir un texto como "cuatro"
```

No necesitas controlar todavía ese error mediante excepciones.

---

## 10. Explica un cálculo y una comparación

Localiza un cálculo real.

Por ejemplo:

```java
int nextWeekGoal = studyHours + 1;
```

Explica:

```text
qué valores intervienen

qué operador utilizas

qué resultado esperas
```

Si vuestro programa contiene una comparación como:

```java
boolean enoughPractice = studyHours >= 3;
```

debes poder explicar por qué produce:

```text
true
```

o:

```text
false
```

En H1 no utilizamos todavía ese resultado para seleccionar caminos distintos del programa.

---

## 11. Realiza una modificación sencilla

Durante la defensa debes ser capaz de modificar una parte que ya comprendes.

Por ejemplo:

```text
cambiar un mensaje

renombrar una variable de forma coherente

cambiar el valor de una constante durante el desarrollo

cambiar el cálculo de +1 a +2

utilizar una variable en otro mensaje
```

Antes de ejecutar:

1. explica qué vas a cambiar;
2. predice qué efecto tendrá.

Después:

3. realiza el cambio;
4. ejecuta;
5. comprueba el resultado;
6. explica si ocurrió lo esperado.

No añadas contenidos de otros hitos para demostrar más.

---

## 12. Explica los límites de H1

Debes poder reconocer qué NO pretende hacer todavía esta versión.

Por ejemplo:

```text
menús
switch
bucles
memoria
colecciones
varias clases propias
ficheros
persistencia
tratamiento completo de excepciones
servicios externos
IA real integrada
```

No saber hacer todavía estas cosas no es un defecto de H1.

Forma parte de la progresión del proyecto.

Una buena defensa distingue entre:

```text
lo que el programa ya hace

y

lo que aprenderemos a incorporar más adelante
```

---

## 13. Si utilizaste IA

No necesitas preparar un discurso especial sobre IA.

Si su intervención fue significativa, debes poder explicar:

```text
para qué la utilizaste

qué propuesta recibiste

qué parte aceptaste o modificaste

cómo comprobaste que funcionaba

qué comprendiste antes de incorporarla
```

La existencia de una respuesta generada no sustituye tu explicación.

Las consultas triviales no necesitan un registro independiente.

Nunca muestres ni introduzcas datos personales, contraseñas, tokens ni claves API.

---

## 14. Resultado observable individual

Cada persona debe poder demostrar, sobre el producto real:

```text
[ ] Puedo localizar Main y main.
[ ] Puedo ejecutar la versión estable.
[ ] Puedo explicar el recorrido básico del programa.
[ ] Puedo explicar una variable.
[ ] Puedo distinguir variable, constante y literal.
[ ] Puedo explicar para qué usamos Scanner.
[ ] Puedo explicar nextLine().
[ ] Puedo explicar la conversión de texto a número.
[ ] Puedo explicar un cálculo sencillo.
[ ] Puedo interpretar una comparación booleana si aparece.
[ ] Puedo realizar una modificación pequeña.
[ ] Puedo comprobar el efecto de mi modificación.
[ ] Puedo reconocer los límites de H1.
[ ] Puedo explicar el código importante sin depender del resto del equipo.
```

No necesitas crear una ficha nueva para demostrarlo.

La defensa se realiza directamente sobre el producto.

---

## 15. Si algo todavía no puedes explicar

Que una parte no esté consolidada todavía no se resuelve memorizando una respuesta.

Identifica con precisión qué necesitas reforzar.

Por ejemplo:

```text
localizar main

diferenciar variable y constante

comprender nextLine()

comprender Integer.parseInt()

predecir un cálculo

interpretar una comparación

modificar código y volver a ejecutarlo
```

La mejora debe ser concreta.

No escribas simplemente:

```text
mejorar Java
```

o:

```text
estudiar más
```

Si este diagnóstico supone un aprendizaje individual significativo, puedes anotarlo brevemente en tu diario.

No necesitas crear un documento específico de recuperación de H1 en esta sesión.

---

## 16. Fuente canónica

Al cerrar H1:

```text
código y versiones        → repositorio

ejecución, uso y límites  → README cuando corresponda

tareas, decisiones y
bloqueos significativos   → Scrum

aprendizajes individuales
significativos             → diario

versión evaluada           → identificada mediante la entrega correspondiente
```

La defensa no genera un documento adicional.

No necesitas:

- una presentación específica para defender H1;
- una captura de cada prueba;
- un informe de defensa;
- un cuestionario copiado en el diario;
- una copia del código en otro documento;
- un registro independiente de IA.

---

## 17. Cierre del hito

Al terminar, debes poder responder con tus propias palabras:

1. ¿dónde empieza la ejecución de MiniJarvis?
2. ¿qué variable puedes explicar mejor?
3. ¿qué diferencia hay entre variable, constante y literal?
4. ¿cómo entra información desde el teclado?
5. ¿por qué convertimos una entrada textual a número?
6. ¿qué cálculo realiza vuestra versión?
7. ¿cómo has comprobado que funciona?
8. ¿qué pequeña modificación puedes realizar sin ayuda?
9. ¿qué no hace todavía H1?
10. ¿qué concepto necesitas reforzar antes de continuar?

H1 está cerrado cuando existe una versión pequeña y estable de MiniJarvis que puede ejecutarse y comprobarse, y cada persona puede explicar y modificar las partes fundamentales que ha trabajado.

La meta no es terminar con un programa complejo.

La meta es poder decir:

> Puedo ejecutarlo, comprobarlo, explicarlo y cambiar una parte porque comprendo lo que he construido.
