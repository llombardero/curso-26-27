# Sesión 211 — Ficha de trabajo del alumnado

## Constantes

| Hoy vas a… | Al terminar debes poder… |
|---|---|
| Diferenciar variables, constantes y literales. | Crear y utilizar una constante con `final`, justificar por qué no debe cambiar y distinguirla de una variable. |

**Tiempo previsto:** 45 minutos.
**Hito:** H1.
**Fase HEXA:** Ejecutar.
**Modalidad:** Equipo.

---

## Material que necesitas

- Un ordenador con JDK e IntelliJ disponibles.
- El proyecto H1.
- El capítulo 02 del libro como referencia.

Utiliza únicamente datos ficticios en los ejemplos.

---

## 1. Punto de partida

En la sesión anterior utilizaste variables.

Por ejemplo:

```java
String userName = "Laura";
```

El valor de `userName` puede cambiar:

```java
userName = "Álex";
```

Pero no todos los datos de un programa deberían cambiar durante la ejecución.

Por ejemplo, podemos decidir que el nombre de esta versión del asistente permanezca fijo:

```java
final String AGENT_NAME = "MiniJarvis";
```

---

## 2. Variable y constante

Compara:

```java
String userName = "Laura";
```

con:

```java
final String AGENT_NAME = "MiniJarvis";
```

En ambos casos tenemos:

```text
tipo
nombre
valor
```

La diferencia importante es `final`.

Cuando declaramos:

```java
final String AGENT_NAME = "MiniJarvis";
```

estamos expresando que ese valor no debe cambiar después de inicializarse.

---

## 3. Comprueba la diferencia

Prueba primero:

```java
String userName = "Laura";
userName = "Álex";
```

Ejecuta y comprueba que puedes cambiar el valor.

Después observa:

```java
final String AGENT_NAME = "MiniJarvis";
AGENT_NAME = "Otro nombre";
```

Antes de probarlo, predice:

```text
¿Permitirá Java la segunda asignación?

¿Por qué?
```

Comprueba qué ocurre.

Después elimina la asignación incorrecta y deja el programa funcionando de nuevo.

---

## 4. El nombre también comunica

En estos primeros programas utilizaremos una convención sencilla:

```text
variables  → camelCase

constantes → MAYÚSCULAS_CON_GUIONES_BAJOS
```

Por ejemplo:

```java
String userName = "Laura";
int studyHours = 4;

final String AGENT_NAME = "MiniJarvis";
```

El nombre ayuda a reconocer rápidamente la intención del dato.

La mayúscula no convierte por sí sola una variable en constante.

Lo que impide reasignar el valor es:

```java
final
```

---

## 5. No todo debe ser constante

Decide si cada dato debería ser normalmente variable o constante en esta versión de MiniJarvis:

```text
nombre del asistente
nombre de la persona usuaria
horas practicadas esta semana
mensaje temporal escrito para una prueba
```

Explica por qué.

No conviertas un dato en constante solo porque ahora mismo no lo estés modificando.

La pregunta importante es:

```text
¿Tiene sentido que este dato pueda cambiar durante la ejecución?
```

---

## 6. Constante y literal

Observa:

```java
final String AGENT_NAME = "MiniJarvis";
```

Aquí podemos distinguir:

```text
AGENT_NAME
```

es el nombre de la constante.

Mientras que:

```text
"MiniJarvis"
```

es el literal que utilizamos para inicializarla.

Una constante y un literal no son lo mismo.

---

## 7. Evita repetir un dato importante

Compara este código:

```java
System.out.println("Hola, soy MiniJarvis.");
System.out.println("MiniJarvis está empezando.");
System.out.println("Esta versión de MiniJarvis funciona por consola.");
```

con:

```java
final String AGENT_NAME = "MiniJarvis";

System.out.println("Hola, soy " + AGENT_NAME + ".");
System.out.println(AGENT_NAME + " está empezando.");
System.out.println("Esta versión de " + AGENT_NAME + " funciona por consola.");
```

En el segundo caso el dato importante tiene un nombre propio dentro del programa.

Si necesitáramos cambiarlo durante el desarrollo, sabríamos dónde hacerlo.

---

## 8. Llévalo a MiniJarvis

En vuestro proyecto H1:

1. localizad el nombre del asistente;
2. cread una constante para representarlo;
3. utilizadla en varios mensajes;
4. ejecutad;
5. comprobad que la salida sigue siendo correcta.

Por ejemplo:

```java
final String AGENT_NAME = "MiniJarvis";

System.out.println("Hola, soy " + AGENT_NAME + ".");
```

Podéis crear otra constante únicamente si existe un dato que realmente tenga sentido mantener fijo.

No añadáis constantes solo para cumplir una cantidad.

---

## 9. Comprueba un error

Después de declarar:

```java
final String AGENT_NAME = "MiniJarvis";
```

intenta temporalmente:

```java
AGENT_NAME = "Jarvis";
```

Observa qué ocurre.

Después corrige el programa.

Debes poder explicar:

```text
qué intentaste cambiar
por qué Java no lo permite
qué función cumple final
```

---

## 10. Resultado observable

Al terminar debéis poder demostrar directamente:

```text
[ ] El programa contiene al menos una constante útil.
[ ] La constante utiliza final.
[ ] Su nombre comunica que es una constante.
[ ] Puedo señalar su tipo.
[ ] Puedo señalar su valor.
[ ] Puedo distinguir constante, variable y literal.
[ ] Puedo justificar por qué ese dato no debe cambiar.
[ ] He comprobado qué ocurre si intento reasignarlo.
[ ] La constante se utiliza realmente en el programa.
```

La comprobación se realiza sobre el propio código.

No necesitáis capturas ni una ficha adicional.

---

## 11. Fuente canónica

El resultado de esta sesión permanece en el proyecto H1.

No creéis:

- una tabla independiente de constantes;
- una captura del código;
- un informe sobre `final`;
- una copia del programa en otro documento.

Si el equipo toma una decisión significativa sobre qué datos deben permanecer fijos, puede conservarla en Scrum si resulta útil.

Si aparece un aprendizaje individual especialmente significativo, puede anotarse brevemente en el diario.

---

## 12. Uso de IA

Antes de consultar una IA, intenta razonar:

```text
¿este dato debe cambiar?

¿por qué?

¿es una variable, una constante o un literal?

¿qué nombre expresa mejor su intención?
```

Puedes utilizar IA para:

- pedir una explicación de `final`;
- comprender un error al intentar reasignar una constante;
- comparar dos posibles nombres;
- revisar un razonamiento que ya hayas realizado.

No la utilices para decidir automáticamente qué debe ser constante sin comprender el motivo.

Si su intervención es significativa, deja una anotación breve en la fuente correspondiente.

No es necesario registrar consultas triviales.

Nunca introduzcas datos personales, contraseñas, tokens ni claves API.

---

## 13. Si os bloqueáis

Antes de pedir ayuda, responded:

```text
¿Qué dato queremos representar?

¿Debe poder cambiar?

¿Es variable o constante?

¿Hemos utilizado final?

¿Qué error aparece?

¿Qué intentábamos hacer?
```

Después formulad una pregunta concreta.

---

## 14. Cierre

Sobre vuestro propio programa, explicad:

1. qué constante habéis creado;
2. qué valor contiene;
3. por qué ese dato debe permanecer fijo;
4. qué función cumple `final`;
5. en qué se diferencia de `userName`;
6. en qué se diferencia la constante del literal que la inicializa;
7. qué ocurrió al intentar cambiarla.

La sesión está completada cuando podéis utilizar una constante real de MiniJarvis y justificar por qué ese dato no debe modificarse durante la ejecución.
