# Sesión 206 — Ficha de trabajo del alumnado

## Presentar H1 y delimitar su alcance

| Hoy vas a… | Al terminar debes poder… |
|---|---|
| Comprender el reto de H1 y distinguir qué pertenece a esta primera versión de MiniJarvis. | Explicar con tus palabras qué construiremos, qué dejaremos para más adelante y qué prácticas no son adecuadas. |

**Tiempo previsto:** 45 minutos.  
**Hito:** H1.
**Fase HEXA:** Activar.
**Modalidad:** Individual → puesta en común en equipo.

---

## Material que necesitas

- La ficha de H1.
- Los capítulos 01 y 02 del libro como referencia cuando sea necesario.
- Un ordenador por estudiante o pareja si necesitas consultar los materiales del curso.
- Datos ficticios para cualquier ejemplo.

No utilizarás contraseñas, tokens, claves API ni datos personales reales.

---

## 1. El reto de H1

H0 sirvió para preparar la forma de trabajar.

Ahora comienza la construcción técnica de MiniJarvis.

En H1 construiremos una primera versión Java por consola que debe ser:

```text
pequeña
   ↓
ejecutable
   ↓
comprobable
   ↓
comprensible
   ↓
defendible
```

No buscamos todavía un agente avanzado.

Buscamos una versión que podamos construir paso a paso y explicar completamente.

---

## 2. Reformula el reto

Trabaja primero de forma individual.

Completa con tus palabras:

```text
En H1 vamos a construir...

La persona usuaria podrá...

El programa podrá...

Todavía no podrá...
```

No copies literalmente la ficha.

El objetivo es comprobar que has entendido el reto.

---

## 3. Clasifica el alcance

Clasifica cada idea en una de estas tres columnas:

```text
H1
Más adelante
No adecuado
```

Ideas que debes clasificar:

1. Mostrar mensajes por consola.
2. Pedir el nombre de la persona usuaria.
3. Guardar el nombre en una variable.
4. Utilizar una constante.
5. Leer información con `Scanner`.
6. Convertir una entrada textual a número.
7. Realizar un cálculo sencillo.
8. Mostrar el resultado del cálculo.
9. Comparar el valor numérico y mostrar el resultado `boolean`.
10. Utilizar ese resultado en un `if/else` para elegir entre dos caminos.
11. Crear un menú con varias opciones.
12. Repetir acciones mediante bucles.
13. Utilizar `switch`.
14. Guardar varios datos en listas, sets o mapas.
15. Crear varias clases propias.
16. Guardar información en ficheros.
17. Conservar información entre ejecuciones.
18. Conectar MiniJarvis con un servicio externo.
19. Integrar Gemini, Jarvis u otra IA real.
20. Utilizar contraseñas o claves API reales en el código.
21. Introducir datos personales reales para hacer pruebas.
22. Incorporar código generado que no puedes explicar.

Antes de compararlo con otras personas, decide individualmente dónde colocarías cada idea.

---

## 4. Contrasta con tu equipo

Comparad vuestras clasificaciones.

No os limitéis a contar votos.

Cuando aparezca una diferencia, utilizad preguntas como:

```text
¿Tenemos ya los conocimientos necesarios?

¿Aparece dentro del producto H1?

¿Pertenece a un hito posterior?

¿Es una práctica insegura o contraria al aprendizaje?

¿Podríamos explicarlo y modificarlo?
```

Intentad alcanzar un acuerdo razonado.

---

## 5. Qué pertenece a H1

Al terminar la puesta en común debes reconocer que H1 trabaja, de forma progresiva:

- estructura básica de un programa Java;
- clase `Main` y método `main`;
- instrucciones;
- salida por consola;
- variables;
- tipos básicos;
- constantes y literales;
- operadores;
- entrada mediante `Scanner`;
- conversión de texto a número;
- un cálculo sencillo;
- una comparación sencilla que produce y muestra `true` o `false` sin bifurcar el flujo;
- comprobación mediante ejecución;
- errores iniciales de compilación y ejecución;
- README técnico básico.

No tienes que dominar hoy todos estos conceptos.

Los aprenderemos durante las siguientes sesiones de H1.

Hoy solo necesitas comprender el alcance.

---

## 6. Qué llegará más adelante

No forman parte de H1:

- decisiones con `if`, `if/else` y bifurcaciones;
- menús;
- `switch`;
- bucles;
- memoria mediante colecciones;
- varias clases propias;
- ficheros y persistencia;
- patrones de diseño;
- servicios externos;
- integración de una IA real.

Que algo quede fuera de H1 no significa que esté prohibido durante todo el curso.

Significa que **todavía no corresponde incorporarlo**.

---

## 7. Qué no es adecuado

Hay prácticas que no pertenecen ni a H1 ni a un hito posterior como forma normal de trabajo:

```text
usar contraseñas o tokens reales en el código
compartir claves API
utilizar datos personales reales sin necesidad
entregar código que no puedes explicar
ocultar una intervención significativa de IA
```

La seguridad, la autoría y la capacidad de explicar lo construido forman parte del proyecto desde el principio.

---

## 8. Resultado observable

Al final de la actividad debes poder explicar, sin leer una respuesta preparada:

1. qué producto construiremos en H1;
2. tres capacidades que sí pertenecen a H1;
3. tres capacidades que llegarán después;
4. una práctica que no sería adecuada;
5. por qué empezar directamente con una IA real dificultaría el aprendizaje.

La comprobación se realiza explicando y contrastando el resultado.

No necesitas crear un documento adicional para demostrar que has realizado la actividad.

Si del debate surge una decisión significativa del equipo que convenga conservar, puede integrarse en Scrum.

---

## 9. Uso de IA

Puedes utilizar IA como apoyo para comprender una palabra o concepto, pero primero debes realizar tu propia clasificación.

No la utilices para obtener directamente la tabla resuelta.

Si la IA interviene de forma significativa en tu aprendizaje o en una decisión del equipo, deja una anotación breve en la fuente correspondiente:

- diario individual, si afecta principalmente a tu aprendizaje;
- Scrum, si afecta a una decisión significativa del equipo.

No es necesario registrar consultas triviales.

Nunca introduzcas datos personales, contraseñas, tokens ni claves API.

---

## 10. Si te bloqueas

Antes de pedir una solución completa:

1. señala la idea que no sabes clasificar;
2. explica entre qué categorías dudas;
3. busca qué exige realmente H1;
4. identifica qué conocimiento necesitarías para implementarla;
5. formula una pregunta concreta.

Por ejemplo:

```text
No sé si guardar información en una lista pertenece a H1.
Sé que H1 trabaja variables.
Todavía no sé qué es una lista.
¿Ese contenido aparece en esta primera versión o más adelante?
```

---

## 11. Cierre

Responde individualmente y con tus palabras:

**¿Por qué MiniJarvis empieza con un programa pequeño por consola en lugar de comenzar directamente con una IA real?**

Respuesta:

................................................................................

................................................................................

La sesión está completada cuando puedes explicar el alcance de H1, distinguir lo que llegará después y justificar al menos una de tus decisiones de clasificación.

No necesitas subir una evidencia adicional de esta sesión.
