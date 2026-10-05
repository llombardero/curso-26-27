# Sesión 214 — Ficha de trabajo del alumnado

## README y ejecución reproducible

| Hoy vas a… | Al terminar debes poder… |
|---|---|
| Documentar la versión H1 para que otra persona pueda entenderla y ejecutarla. | Tener un README útil, una versión estable de H1 comprobada y una ejecución reproducible por otra persona. |

**Tiempo previsto:** 45 minutos.
**Hito:** H1.
**Fase HEXA:** Comunicar.
**Modalidad:** Equipo → comprobación cruzada.

---

## Material que necesitas

- Un ordenador con JDK e IntelliJ disponibles.
- El proyecto H1 funcionando.
- El `README.md` del proyecto.
- La ficha de H1 como referencia para comprobar su alcance.

---

## 1. Punto de partida

Un programa no queda preparado para compartirlo solo porque funcione en el ordenador de quien lo ha creado.

Otra persona debería poder:

```text
localizar el proyecto
       ↓
entender qué versión es
       ↓
saber qué hace
       ↓
ejecutarlo
       ↓
comprobar su comportamiento
       ↓
reconocer sus límites
```

El README sirve para facilitar ese recorrido.

No es un informe de todo lo que habéis hecho durante el hito.

---

## 2. Qué debe resolver el README

Una persona que llegue por primera vez al proyecto debería poder responder leyendo el README:

```text
¿Qué es este proyecto?

¿Qué hace esta versión?

¿Cómo se ejecuta?

¿Cómo puedo comprobar que funciona?

¿Qué todavía no hace?
```

Si una información no ayuda a entender, ejecutar o comprobar el proyecto, probablemente no necesita estar en el README de H1.

---

## 3. Estructura mínima suficiente

Una estructura adecuada para H1 es:

```markdown
# H1 — Primer asistente por consola

## Qué hace

Breve explicación de esta versión de MiniJarvis.

## Cómo ejecutar

Pasos necesarios para abrir y ejecutar el programa.

## Comprobación

Un ejemplo breve de entrada y salida que permita reconocer que funciona.

## Límites de H1

Funciones que todavía no incorpora esta versión.
```

Podéis adaptar los títulos si el contenido sigue siendo claro.

No añadáis apartados únicamente para hacer el README más largo.

---

## 4. Describe qué hace realmente

La descripción debe corresponder con el programa actual.

Por ejemplo, una versión H1 puede indicar que MiniJarvis:

- se ejecuta por consola;
- muestra una presentación;
- pide un nombre;
- utiliza el dato introducido;
- solicita un valor numérico;
- convierte texto a número;
- realiza un cálculo sencillo;
- muestra resultados.

No describáis funciones que todavía no existen.

Evita frases como:

```text
MiniJarvis es una inteligencia artificial completa.

MiniJarvis aprende del usuario.

MiniJarvis recuerda conversaciones.
```

si vuestra versión H1 no hace esas cosas.

---

## 5. Explica cómo ejecutarlo

El README debe permitir localizar y arrancar el programa.

Una explicación desde IntelliJ puede ser tan sencilla como:

```text
1. Abrir el proyecto.
2. Localizar src/Main.java.
3. Ejecutar la clase Main.
4. Introducir los datos solicitados en la consola.
```

Si vuestro proyecto permite además una ejecución por terminal y ya sabéis utilizarla, podéis documentarla.

Por ejemplo:

```bash
javac src/Main.java
java -cp src Main
```

No incluyáis instrucciones que no hayáis comprobado.

---

## 6. Añade una comprobación reproducible

No basta con escribir:

```text
El programa funciona.
```

Incluid un ejemplo pequeño que permita reconocer el comportamiento esperado.

Por ejemplo:

```text
Hola, soy MiniJarvis.
¿Cómo te llamas? Laura
Hola, Laura.
¿Cuántas horas has practicado Programación? 4
Si la próxima semana practicas una hora más, serán 5 horas.
```

El ejemplo debe coincidir con vuestra versión real.

No tiene que ser idéntico al de esta ficha.

---

## 7. Explica los límites de H1

El README también debe evitar crear expectativas falsas.

Podéis indicar que esta versión todavía no incorpora, por ejemplo:

```text
menús
bucles
memoria persistente
varias clases propias
servicios externos
IA real
```

No hace falta enumerar todo el curso futuro.

Incluid únicamente los límites que ayuden a entender esta versión.

---

## 8. Comprueba primero vuestra propia versión

Antes del intercambio con otro equipo:

1. guardad todos los cambios;
2. comprobad que estáis trabajando sobre la versión correcta;
3. ejecutad MiniJarvis;
4. utilizad datos ficticios;
5. comprobad que la ejecución coincide con lo explicado en el README.

Realizad, al menos:

```text
una ejecución con un nombre ficticio
otra ejecución con otro nombre
una entrada numérica válida
otra entrada numérica válida diferente
```

Podéis observar también una entrada no numérica si forma parte de la comprobación realizada en S212.

No necesitáis controlar todavía ese error.

---

## 9. Intercambio: otra persona prueba vuestro README

Ahora viene la prueba importante.

Otro equipo debe intentar ejecutar vuestra versión siguiendo el README.

Durante el primer intento:

**no expliquéis oralmente los pasos que faltan.**

Observad.

La otra persona debe intentar:

```text
localizar Main.java
ejecutar el programa
introducir datos
reconocer el resultado esperado
identificar qué hace H1
identificar qué todavía no hace
```

Si necesita una explicación que no aparece en el README, habéis encontrado una posible mejora.

---

## 10. Mejorad únicamente lo necesario

Después del intercambio, preguntad al otro equipo:

```text
¿Qué parte se entendió bien?

¿Dónde dudaste?

¿Qué instrucción faltaba?

¿Había información innecesaria?

¿La ejecución coincidió con el ejemplo?
```

Modificad el README únicamente cuando la observación revele una mejora útil.

Después de modificarlo, comprobad de nuevo el resultado.

---

## 11. README no significa duplicar evidencias

El README puede incluir:

- qué hace la versión;
- cómo ejecutarla;
- una comprobación breve;
- límites relevantes;
- alguna decisión técnica necesaria para comprenderla.

No necesita contener:

- una copia completa del código;
- capturas rutinarias de la consola;
- un diario de cada sesión;
- una tabla separada de todas las pruebas;
- el contenido del Scrum;
- una defensa escrita;
- un registro independiente de IA;
- una copia de documentos ya conservados en otra fuente.

La ejecución reproducible es más útil que una captura rutinaria.

---

## 12. Identifica la versión que se va a presentar

Antes de cerrar la sesión debéis saber qué versión concreta de H1 vais a presentar.

La versión debe:

```text
compilar
ejecutarse
corresponder con el README
estar dentro del alcance de H1
ser localizable en el repositorio
```

Según el mecanismo de entrega utilizado, podrá identificarse mediante:

```text
un tag de entrega, como h1-entrega

o

un commit estable claramente identificable
```

No necesitáis crear dos mecanismos distintos.

Lo importante es que pueda localizarse exactamente la versión evaluada.

---

## 13. Resultado observable

Al terminar debéis poder demostrar:

```text
[ ] Existe un README del proyecto.
[ ] Explica brevemente qué hace H1.
[ ] Permite saber cómo ejecutar el programa.
[ ] Incluye una comprobación breve y reproducible.
[ ] Describe límites relevantes de esta versión.
[ ] Lo escrito coincide con el programa real.
[ ] Otra persona ha intentado seguir el README.
[ ] Hemos corregido únicamente las instrucciones que lo necesitaban.
[ ] MiniJarvis sigue compilando y ejecutándose.
[ ] Podemos identificar la versión estable que se va a presentar.
```

No necesitáis una captura como prueba rutinaria de ejecución.

La comprobación consiste en poder volver a ejecutar la versión indicada.

---

## 14. Fuente canónica

Cada elemento permanece donde corresponde:

```text
código y versiones       → repositorio

ejecución y límites      → README cuando sea necesario documentarlos

tareas y decisiones
significativas del equipo → Scrum

aprendizajes personales
significativos            → diario

versión evaluada          → identificada en la entrega de Moodle
```

No creéis otro documento para resumir esta sesión.

---

## 15. Uso de IA

La IA puede ayudar a revisar:

- si una instrucción del README resulta ambigua;
- si una explicación técnica puede expresarse con mayor claridad;
- si falta información necesaria para reproducir una ejecución.

No le pidáis que invente pasos que no habéis comprobado.

Cualquier propuesta debe contrastarse ejecutando realmente el proyecto.

Si la intervención de la IA es significativa, registradla en la fuente correspondiente.

No es necesario registrar consultas triviales.

Nunca incluyáis datos personales, contraseñas, tokens ni claves API en el README ni en una consulta a IA.

---

## 16. Si os bloqueáis

Ante un problema de reproducibilidad, separad:

```text
¿El problema está en el código?

¿El problema está en la configuración?

¿El README omite un paso?

¿La instrucción existe pero no se entiende?

¿Estamos probando la versión correcta?

¿El ejemplo del README coincide con el programa?
```

Corregid el problema en su fuente real.

No añadáis una explicación extra en otro documento para compensar un README incompleto.

---

## 17. Cierre

Otro equipo debe intentar ejecutar vuestra versión una última vez.

Después debéis poder responder:

1. ¿qué necesita saber una persona para ejecutar H1?
2. ¿qué parte del README habéis mejorado después de la prueba?
3. ¿qué ejemplo permite comprobar el comportamiento?
4. ¿qué límite de H1 resulta importante explicar?
5. ¿qué versión exacta vais a presentar?
6. ¿podríais volver a localizar y ejecutar esa misma versión?

La sesión está completada cuando otra persona puede entender y ejecutar H1 utilizando el README y el equipo puede identificar sin ambigüedad la versión estable que va a presentar.
