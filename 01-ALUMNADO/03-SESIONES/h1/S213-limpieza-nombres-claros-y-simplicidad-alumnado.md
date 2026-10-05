# Sesión 213 — Ficha de trabajo del alumnado

## Limpieza, nombres claros y simplicidad

| Hoy vas a… | Al terminar debes poder… |
|---|---|
| Revisar la versión H1 para hacerla más clara sin cambiar innecesariamente su comportamiento. | Tener un programa H1 sencillo, ejecutable y comprensible, y poder justificar al menos una mejora realizada. |

**Tiempo previsto:** 45 minutos.
**Hito:** H1.
**Fase HEXA:** Ejecutar.
**Modalidad:** Equipo → comprobación individual.

---

## Material que necesitas

- Un ordenador con JDK e IntelliJ disponibles.
- El proyecto H1 funcionando.
- La ficha de H1.
- Los capítulos 01 y 02 del libro como referencia.

---

## 1. Punto de partida

MiniJarvis ya ha crecido durante H1.

La versión actual puede contener:

- mensajes por consola;
- variables;
- tipos básicos;
- una constante;
- `Scanner`;
- entrada de texto;
- conversión de texto a número;
- un cálculo sencillo;
- una comparación booleana.

Hoy no vamos a añadir una nueva capacidad.

Vamos a revisar lo que ya existe.

La idea es:

```text
funciona
   ↓
reviso
   ↓
cambio una cosa
   ↓
vuelvo a ejecutar
   ↓
compruebo
```

---

## 2. Primero comprueba la versión actual

Antes de limpiar nada, ejecuta MiniJarvis.

Utiliza datos ficticios y comprueba que:

```text
[ ] aparece la presentación;
[ ] pide el nombre;
[ ] utiliza el nombre introducido;
[ ] pide el dato numérico previsto;
[ ] realiza la conversión;
[ ] realiza el cálculo;
[ ] muestra el resultado esperado.
```

Esta ejecución es tu punto de referencia.

Si el programa no funciona antes de empezar la revisión, resuelve primero ese problema.

---

## 3. Revisa los nombres

Localiza las variables y constantes de vuestro programa.

Pregúntate:

```text
¿El nombre explica qué dato contiene?

¿Podría entenderlo otra persona?

¿Mantiene una forma de escritura coherente?

¿Hay nombres demasiado cortos o ambiguos?
```

Compara:

```java
String n = scanner.nextLine();
int h = Integer.parseInt(hoursText);
```

con nombres como:

```java
String userName = scanner.nextLine();
int studyHours = Integer.parseInt(hoursText);
```

No cambies nombres solo por cambiarlos.

Hazlo cuando el nuevo nombre exprese mejor la intención.

---

## 4. Revisa variables y constantes

Comprueba:

```text
¿Los datos que cambian son variables?

¿La constante representa realmente un dato que debe permanecer fijo?

¿La constante utiliza final?

¿Su nombre permite reconocerla fácilmente?
```

Por ejemplo:

```java
final String AGENT_NAME = "MiniJarvis";
```

No conviertas datos en constantes únicamente para aumentar su número.

---

## 5. Revisa los mensajes

Ejecuta y lee la salida como si fueras una persona que utiliza MiniJarvis por primera vez.

Comprueba:

```text
¿Las preguntas se entienden?

¿Los mensajes aparecen en un orden lógico?

¿Hay frases repetidas sin necesidad?

¿Los mensajes describen capacidades que realmente existen?

¿La salida permite saber qué debe introducir la persona usuaria?
```

Cambia únicamente los mensajes que realmente necesiten una mejora.

---

## 6. Revisa la estructura visual del código

Observa `Main.java`.

Comprueba:

```text
[ ] Las llaves permiten reconocer los bloques.
[ ] Las instrucciones dentro de main están indentadas.
[ ] Hay separación suficiente para leer el código.
[ ] No hay líneas colocadas de forma que oculten la estructura.
```

La forma visual del código debe ayudarte a comprenderlo.

No necesitas aplicar reglas avanzadas de estilo.

---

## 7. Revisa los comentarios

Un comentario debe aportar información útil.

Por ejemplo, normalmente no necesitamos:

```java
// Mostramos un mensaje
System.out.println("Hola.");
```

porque la instrucción ya permite comprenderlo.

Un comentario puede tener sentido cuando explica una decisión que no resulta evidente.

Revisa los comentarios existentes y pregúntate:

```text
¿Aporta información?

¿Explica algo que el código no deja claro?

¿O simplemente repite la instrucción?
```

No añadas comentarios solo para cumplir una cantidad.

---

## 8. Busca complejidad que no pertenece a H1

Comprueba que no habéis añadido por iniciativa propia elementos que todavía no corresponden.

En H1 no necesitamos:

```text
menús
switch
bucles
listas, sets o mapas
varias clases propias
ficheros
persistencia
try/catch
servicios externos
IA real integrada
patrones de diseño
```

Si aparece algo que no habéis estudiado y no podéis explicar, revisad por qué está ahí.

Una versión más compleja no es automáticamente una versión mejor.

---

## 9. Cambia una sola cosa cada vez

Para cada mejora:

```text
elige un cambio
     ↓
realízalo
     ↓
ejecuta
     ↓
comprueba
     ↓
continúa
```

Por ejemplo:

```text
renombrar una variable
        ↓
ejecutar
        ↓
comprobar

mejorar un mensaje
        ↓
ejecutar
        ↓
comprobar
```

No hagáis muchos cambios antes de volver a ejecutar.

Si algo deja de funcionar, será más fácil localizar qué cambio lo provocó.

---

## 10. Revisión del equipo

Como equipo, revisad esta lista:

```text
[ ] El programa sigue dentro del alcance de H1.
[ ] Los nombres ayudan a comprender los datos.
[ ] La constante tiene una función real.
[ ] Los mensajes son claros.
[ ] La indentación permite reconocer la estructura.
[ ] Los comentarios, si existen, aportan información.
[ ] No hay complejidad que no podamos explicar.
[ ] El programa sigue compilando y ejecutándose.
```

No tenéis que crear una copia de esta checklist.

Utilizadla para revisar el programa real.

---

## 11. Comprobación individual

Después de la revisión del equipo, cada persona debe realizar o explicar una pequeña modificación.

Por ejemplo:

```text
renombrar una variable
mejorar un mensaje
localizar una constante
explicar una conversión
cambiar el cálculo manteniendo el mismo nivel
```

Después debe:

1. predecir qué efecto tendrá;
2. realizar el cambio;
3. ejecutar;
4. comprobar el resultado;
5. explicar qué ha modificado.

El objetivo es comprobar que cada persona comprende el producto compartido.

---

## 12. Resultado observable

Al terminar debéis poder demostrar directamente:

```text
[ ] MiniJarvis compila y se ejecuta.
[ ] Los nombres principales son comprensibles.
[ ] Las variables y constantes tienen sentido.
[ ] La salida es clara.
[ ] El código mantiene una estructura visual legible.
[ ] Los comentarios no repiten lo obvio.
[ ] No hay complejidad innecesaria o adelantada.
[ ] Hemos realizado mejoras pequeñas y comprobables.
[ ] Cada persona puede explicar o modificar una parte.
```

La comprobación se realiza sobre el propio programa.

No necesitáis capturas ni un informe de revisión.

---

## 13. Fuente canónica

Las mejoras permanecen en el código del proyecto H1.

Si una decisión del equipo resulta realmente significativa para continuar el proyecto, puede registrarse en Scrum.

Si una persona identifica un aprendizaje especialmente significativo, puede anotarlo brevemente en su diario.

No creéis:

- un informe de limpieza;
- una checklist entregable;
- capturas del antes y el después;
- un documento de revisión;
- una copia del código fuera del repositorio.

---

## 14. Uso de IA

Antes de pedir una revisión a una IA, revisa tú mismo el código.

Puedes utilizar IA para:

- preguntar por qué un nombre resulta confuso;
- pedir explicación de una línea que no comprendes;
- comparar dos nombres posibles;
- revisar una mejora concreta que ya hayas planteado.

No aceptes una reescritura completa del programa.

No introduzcas técnicas que todavía no hayas estudiado.

Si la intervención de la IA es significativa, deja una anotación breve en la fuente correspondiente.

No es necesario registrar consultas triviales.

Nunca introduzcas datos personales, contraseñas, tokens ni claves API.

---

## 15. Si os bloqueáis

Ante una parte que no entendéis, preguntad:

```text
¿Qué hace esta línea?

¿Dónde se utiliza este dato?

¿Qué ocurriría si la elimino?

¿Puedo predecir el resultado antes de cambiarla?

¿Pertenece realmente a H1?

¿Puedo explicarla con mis palabras?
```

No eliminéis código al azar.

Realizad cambios pequeños y comprobadlos.

---

## 16. Cierre

Sobre vuestra versión real de H1, explicad:

1. qué mejora habéis realizado;
2. por qué mejora la comprensión del programa;
3. cómo habéis comprobado que no rompe el comportamiento;
4. qué nombre de variable o constante podéis justificar;
5. si habéis eliminado o evitado alguna complejidad innecesaria;
6. qué parte del programa todavía os cuesta explicar.

La sesión está completada cuando MiniJarvis sigue funcionando después de la revisión y cada persona puede explicar o modificar una parte concreta sin depender del resto del equipo.
