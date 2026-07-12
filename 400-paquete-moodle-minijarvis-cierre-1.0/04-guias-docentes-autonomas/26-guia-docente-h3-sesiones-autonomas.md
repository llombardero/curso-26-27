# Guía docente completa — H3 sesión a sesión

## Agente con memoria en colecciones — MiniJarvis H3

## Programación + Entornos de Desarrollo — 1.º DAW — Curso 2026/2027

Versión: cierre curricular 1.0 — julio 2026

Documento autónomo para uso del profesorado.

Este documento permite impartir H3 completo sin abrir ningún otro material.

---

## 1. Propósito de H3

H3 añade memoria temporal a MiniJarvis.

Producto final:

```text
MiniJarvis H3: agente por consola que recuerda información durante la ejecución usando colecciones Java.
```

H3 introduce:

```text
- memoria temporal;
- ArrayList u otra colección;
- comando para guardar información;
- comando para consultar memoria;
- caso de memoria vacía;
- validación de entrada vacía;
- pruebas de memoria;
- justificación de colección;
- comparación Java ↔ Python;
- defensa de estructura de datos.
```

---

## 2. Restricciones de H3

En H3 sí entra:

```text
[x] Una colección Java.
[x] Guardar información durante la ejecución.
[x] Consultar la memoria.
[x] Gestionar memoria vacía.
[x] Probar casos límite.
[x] Justificar la colección elegida.
[x] Comparar Java ↔ Python.
```

En H3 todavía NO entra:

```text
[ ] Guardar en ficheros.
[ ] Base de datos.
[ ] Arquitectura orientada a objetos completa.
[ ] Interfaces.
[ ] Patrones de diseño.
[ ] API externa.
[ ] IA real.
```

Frase docente:

```text
H3 trata de memoria temporal con colecciones. Si cerramos el programa, la memoria desaparece. Guardar en ficheros será H6.
```

---

## 3. Secuencia de sesiones H3

Propuesta de 10 sesiones de 45 minutos.

| Sesión | Foco | Producto parcial |
|---|---|---|
| H3-S1 | Presentar H3 y memoria temporal | Diferencia H2/H3 clara. |
| H3-S2 | Elegir qué recordar | Decisión de memoria del agente. |
| H3-S3 | Introducir ArrayList | Colección creada y entendida. |
| H3-S4 | Comando recuerda | Guardar un recuerdo. |
| H3-S5 | Comando memoria | Consultar recuerdos. |
| H3-S6 | Casos límite | Memoria vacía y entrada vacía. |
| H3-S7 | Pruebas de memoria | `docs/pruebas-memoria-h3.md`. |
| H3-S8 | Justificación de colección | `docs/justificacion-coleccion-h3.md`. |
| H3-S9 | Comparación Java ↔ Python y documentación | Comparación + portfolio/registro IA. |
| H3-S10 | Defensa, revisión y cierre C1 | H3 validado. |

---

# H3-S1 — Presentar H3 y memoria temporal

## Duración

```text
45 minutos
```

## Objetivo

Que el alumnado entienda qué añade H3 respecto a H2: el agente recordará información mientras el programa está abierto.

## Resultado esperado

Cada alumno/a debe poder explicar:

```text
- qué es memoria temporal;
- qué diferencia hay entre recordar durante la ejecución y guardar en fichero;
- qué comandos nuevos aparecerán;
- qué no entra todavía.
```

## Guion docente

```text
En H2 MiniJarvis tenía menú y comandos, pero no recordaba nada.

En H3 vamos a añadir memoria temporal. Eso significa que el programa podrá guardar información mientras está abierto.

Pero atención: si cerramos el programa, esa memoria desaparece. Guardar en ficheros será otro hito posterior.
```

## Pizarra

```text
H2 = comandos + bucle + decisiones
H3 = H2 + memoria temporal con colección
```

## Ejemplo de comportamiento

```text
> memoria
No tengo recuerdos todavía.
> recuerda
¿Qué quieres que recuerde? Traer pendrive
He guardado: Traer pendrive
> memoria
1. Traer pendrive
> estado
Tengo 1 recuerdo en memoria temporal.
```

## Qué explicas tú

```text
- memoria temporal;
- diferencia entre RAM/fichero de forma informal;
- colección como estructura para guardar varios datos;
- límites de H3.
```

## Actividad HEXA guiada

Pregunta:

```text
¿Qué podría recordar MiniJarvis durante una ejecución sin que sea peligroso ni demasiado complejo?
```

Opciones aceptables:

```text
- mensajes escritos;
- tareas sencillas;
- comandos usados;
- preferencias ficticias;
- recordatorios no personales.
```

Opciones no recomendables:

```text
- contraseñas;
- teléfonos reales;
- datos personales;
- claves API;
- información que debería persistir en fichero.
```

## Cierre

Ticket:

```text
1. ¿Qué significa memoria temporal?
2. ¿Qué NO haremos todavía en H3?
3. Escribe un ejemplo seguro de algo que MiniJarvis podría recordar.
```

---

# H3-S2 — Elegir qué recordar y diseñar comandos

## Duración

```text
45 minutos
```

## Objetivo

Definir qué guardará MiniJarvis y cómo se probará.

## Resultado esperado

Tabla de memoria y comandos:

```text
recuerda
memoria
estado
```

## Guion docente

```text
Antes de programar memoria, necesitamos decidir qué vamos a guardar y cómo sabremos que funciona.
```

## Tabla de diseño

| Comando | Qué hace | Qué dato usa | Cómo se prueba |
|---|---|---|---|
| recuerda | Guarda un texto | recuerdo escrito | Consultar memoria después. |
| memoria | Muestra recuerdos | lista de recuerdos | Probar con memoria vacía y con datos. |
| estado | Cuenta recuerdos | tamaño de lista | Guardar 2 y comprobar que dice 2. |

## Qué explicas tú

```text
- una memoria se diseña antes de programar;
- guardar y consultar son acciones distintas;
- las pruebas deben pensarse antes o durante el desarrollo.
```

## Actividad guiada

Cada equipo completa:

| Pregunta | Respuesta |
|---|---|
| ¿Qué guardará MiniJarvis? | |
| ¿Qué comando lo guarda? | |
| ¿Qué comando lo consulta? | |
| ¿Qué pasa si no hay nada guardado? | |
| ¿Qué entrada no deberíamos aceptar? | |

## Cierre

Pregunta:

```text
¿Qué caso de prueba aparece antes de guardar nada?
```

Respuesta esperada:

```text
memoria vacía
```

---

# H3-S3 — Introducir ArrayList

## Duración

```text
45 minutos
```

## Objetivo

Crear y entender una colección `ArrayList<String>`.

## Resultado esperado

El alumnado sabe crear una lista, añadir elementos y contar cuántos hay.

## Guion docente

```text
Si queremos guardar varios recuerdos, una variable String no basta.

Necesitamos una estructura que pueda contener varios textos. En Java podemos usar ArrayList.
```

## Código base

```java
import java.util.ArrayList;

ArrayList<String> memories = new ArrayList<>();
memories.add("Traer pendrive");
System.out.println(memories.size());
```

## Qué explicas tú

```text
ArrayList: lista que puede crecer.
<String>: la lista guarda textos.
new ArrayList<>(): crea la lista.
add: añade un elemento.
size: devuelve cuántos elementos hay.
```

## Comparación sencilla

```text
String userName = un texto.
ArrayList<String> memories = varios textos.
```

## Práctica guiada

En el código H2, añadir temporalmente:

```java
ArrayList<String> memories = new ArrayList<>();
```

Y probar:

```java
memories.add("Primer recuerdo de prueba");
System.out.println("Recuerdos: " + memories.size());
```

## Investigación HEXA guiada

Pregunta:

```text
¿ArrayList o HashMap para recuerdos simples en orden?
```

Respuesta esperada:

```text
ArrayList, porque queremos una lista ordenada de recuerdos, no una búsqueda por clave.
```

## Cierre

Ticket:

```text
1. ¿Qué guarda ArrayList<String>?
2. ¿Qué hace add?
3. ¿Qué hace size?
```

---

# H3-S4 — Comando recuerda

## Duración

```text
45 minutos
```

## Objetivo

Añadir el comando `recuerda` para guardar un texto en la colección.

## Resultado esperado

MiniJarvis puede guardar un recuerdo durante la ejecución.

## Código base

Dentro del `while`, añadir una rama:

```java
} else if (command.equals("recuerda")) {
    System.out.print("¿Qué quieres que recuerde? ");
    String memory = scanner.nextLine().trim();
    memories.add(memory);
    System.out.println("He guardado: " + memory);
}
```

## Qué explicas tú

```text
La lista debe crearse antes del while.
El comando recuerda pide un segundo texto.
Ese texto se añade con add.
Todavía falta validar memoria vacía; lo haremos después.
```

## Práctica guiada

Secuencia de prueba:

```text
recuerda
Traer pendrive
estado
salir
```

Si `estado` todavía no cuenta recuerdos, puede mostrar temporalmente `memories.size()`.

## Error frecuente

| Error | Intervención |
|---|---|
| Crea ArrayList dentro del while | Explicar que se reinicia en cada vuelta. |
| Añade command en vez de memory | Revisar qué variable contiene el recuerdo. |
| No importa ArrayList | Añadir import. |

## Cierre

Pregunta:

```text
¿Dónde debe crearse la lista para que no se borre en cada vuelta del while?
```

Respuesta esperada:

```text
Antes del while.
```

---

# H3-S5 — Comando memoria

## Duración

```text
45 minutos
```

## Objetivo

Añadir el comando `memoria` para consultar recuerdos guardados.

## Resultado esperado

MiniJarvis muestra recuerdos guardados en orden.

## Código base

```java
} else if (command.equals("memoria")) {
    System.out.println("Recuerdos guardados:");
    for (int i = 0; i < memories.size(); i++) {
        System.out.println((i + 1) + ". " + memories.get(i));
    }
}
```

## Qué explicas tú

```text
for: repite un número conocido de veces.
i empieza en 0 porque las listas en Java empiezan en índice 0.
memories.get(i): obtiene el elemento en posición i.
i + 1: muestra numeración humana empezando en 1.
```

## Práctica guiada

Secuencia:

```text
recuerda
Traer pendrive
recuerda
Repasar Scanner
memoria
salir
```

Salida esperada:

```text
1. Traer pendrive
2. Repasar Scanner
```

## Error frecuente

| Error | Intervención |
|---|---|
| Muestra desde 0 | Explicar índice interno vs numeración visible. |
| Usa `<= memories.size()` | Explicar límite estricto `<`. |
| Confunde get con add | add guarda, get consulta. |

## Cierre

Ticket:

```text
1. ¿Por qué usamos i + 1 al mostrar?
2. ¿Qué hace memories.get(i)?
```

---

# H3-S6 — Casos límite: memoria vacía y entrada vacía

## Duración

```text
45 minutos
```

## Objetivo

Gestionar casos límite básicos.

## Resultado esperado

MiniJarvis:

```text
- avisa si la memoria está vacía;
- no guarda recuerdos vacíos.
```

## Guion docente

```text
Un programa no solo debe funcionar cuando todo va bien. También debe responder bien cuando no hay datos o cuando la entrada no sirve.
```

## Memoria vacía

```java
if (memories.isEmpty()) {
    System.out.println("No tengo recuerdos todavía.");
} else {
    System.out.println("Recuerdos guardados:");
    for (int i = 0; i < memories.size(); i++) {
        System.out.println((i + 1) + ". " + memories.get(i));
    }
}
```

## Entrada vacía

```java
if (memory.isEmpty()) {
    System.out.println("No puedo guardar un recuerdo vacío.");
} else {
    memories.add(memory);
    System.out.println("He guardado: " + memory);
}
```

## Qué explicas tú

```text
isEmpty en lista: comprueba si no hay elementos.
isEmpty en String: comprueba si el texto está vacío.
Caso límite: situación especial que puede romper o confundir el programa.
```

## Pruebas

```text
memoria
recuerda
[pulsar Enter sin escribir nada]
estado
```

## Cierre

Pregunta:

```text
¿Por qué es importante probar memoria vacía antes de guardar nada?
```

---

# H3-S7 — Pruebas de memoria

## Duración

```text
45 minutos
```

## Objetivo

Documentar pruebas de memoria con casos normales y casos límite.

## Resultado esperado

Documento `docs/pruebas-memoria-h3.md` o equivalente.

## Tabla mínima

| ID | Caso | Entrada | Esperado | Obtenido | Estado |
|---|---|---|---|---|---|
| M01 | Memoria vacía | memoria | Aviso de vacío | | |
| M02 | Guardar recuerdo | recuerda + texto | Guarda texto | | |
| M03 | Mostrar memoria | memoria | Lista recuerdos | | |
| M04 | Estado | estado | Número recuerdos | | |
| M05 | Entrada vacía | recuerda + vacío | No guarda | | |

## Qué explicas tú

```text
Las pruebas de memoria no solo prueban comandos. Prueban cómo cambia la colección.
```

## Actividad

El alumnado ejecuta una secuencia completa y rellena la tabla.

Secuencia sugerida:

```text
memoria
recuerda
Traer pendrive
recuerda
Repasar Scanner
estado
memoria
recuerda
[pulsar Enter]
salir
```

## Cierre

Pregunta:

```text
¿Qué prueba demuestra que la memoria cambia?
```

Respuesta esperada:

```text
Guardar un recuerdo y después consultar memoria o estado.
```

---

# H3-S8 — Justificación de colección

## Duración

```text
45 minutos
```

## Objetivo

Justificar por qué se ha usado `ArrayList` u otra colección.

## Resultado esperado

Documento `docs/justificacion-coleccion-h3.md` o equivalente.

## Guion docente

```text
No basta con usar una colección. Hay que poder explicar por qué esa colección tiene sentido.
```

## Explicación mínima

```text
ArrayList: útil para guardar elementos en orden.
HashMap: útil para guardar pares clave-valor.
```

## Tabla de decisión

| Necesidad | Mejor opción inicial | Motivo |
|---|---|---|
| Guardar recuerdos en orden | ArrayList | Importa el orden de inserción. |
| Buscar por nombre o clave | HashMap | Importa acceder por clave. |
| Guardar solo un dato | String | No hace falta colección. |

## Plantilla de justificación

```text
He elegido ArrayList<String> porque...
No he elegido HashMap porque...
La colección se crea en...
Los datos se añaden con...
Los datos se muestran con...
```

## Investigación HEXA guiada

Pregunta:

```text
Busca o razona una diferencia entre ArrayList y HashMap y relaciónala con MiniJarvis.
```

Producto:

```text
3 frases, no copia larga.
```

## Cierre

Pregunta:

```text
Si quiero recuerdos en orden, ¿qué colección inicial tiene más sentido?
```

---

# H3-S9 — Comparación Java ↔ Python y documentación

## Duración

```text
45 minutos
```

## Objetivo

Comparar colecciones Java con estructuras Python y completar documentación H3.

## Resultado esperado

```text
- comparación Java ↔ Python;
- README H3 actualizado;
- portfolio H3;
- registro IA si se usó.
```

## Comparación mínima

| Necesidad | Java | Python |
|---|---|---|
| Lista ordenada | `ArrayList<String>` | `list` |
| Añadir | `memories.add(memory)` | `memories.append(memory)` |
| Tamaño | `memories.size()` | `len(memories)` |
| Acceso | `memories.get(i)` | `memories[i]` |

## Qué explicas tú

```text
Comparar lenguajes ayuda a entender la idea común: guardar varios datos y recorrerlos.
```

## Actividad

El alumnado completa:

```text
En Java uso...
En Python sería parecido a...
La diferencia que debo recordar es...
```

## IA

Uso permitido:

```text
Pedir una explicación sencilla de ArrayList vs list o HashMap vs dict.
```

Condición:

```text
Registrar, verificar y defender.
```

## Cierre

Pregunta:

```text
¿Qué cambia entre ArrayList y list aunque la idea sea parecida?
```

---

# H3-S10 — Defensa, revisión y cierre C1

## Duración

```text
45 minutos
```

## Objetivo

Validar H3 como evidencia técnica y preparar el cierre de la primera evaluación.

## Resultado esperado

```text
- código H3 revisado;
- pruebas documentadas;
- justificación de colección;
- defensa individual;
- recuperación si procede.
```

## Checklist docente

| Elemento | Sí | Parcial | No |
|---|---|---|
| Ejecuta | | | |
| Mantiene comandos H2 | | | |
| Usa colección | | | |
| Guarda recuerdo | | | |
| Muestra memoria | | | |
| Gestiona memoria vacía | | | |
| Gestiona entrada vacía | | | |
| Pruebas de memoria | | | |
| Justificación de colección | | | |
| Comparación Java/Python | | | |
| Defensa | | | |

## Preguntas de defensa

```text
1. ¿Qué colección has usado?
2. ¿Por qué has elegido esa colección?
3. ¿Dónde se crea la lista?
4. ¿Cómo guardas un recuerdo?
5. ¿Cómo muestras la memoria?
6. ¿Qué pasa si la memoria está vacía?
7. ¿Qué pasa si intento guardar un recuerdo vacío?
8. ¿Qué diferencia hay entre ArrayList y list de Python?
9. ¿Por qué H3 todavía no guarda en fichero?
```

## Recuperación inmediata

Si falla guardar:

```text
Revisar memories.add(memory).
```

Si falla mostrar:

```text
Revisar for y memories.get(i).
```

Si falla memoria vacía:

```text
Revisar memories.isEmpty().
```

Si falla defensa:

```text
Explicar ArrayList, add, size, get e isEmpty.
```

## Cierre de H3

Guion:

```text
H3 cierra una etapa importante: MiniJarvis ya tiene menú y memoria temporal.

En la segunda evaluación rediseñaremos el agente con orientación a objetos. Eso será H4.
```

---

## 4. Evaluación formativa de H3

H3 debe servir para detectar:

```text
- quién entiende colecciones;
- quién sabe justificar una estructura;
- quién controla casos límite;
- quién documenta pruebas;
- quién confunde memoria temporal con persistencia;
- quién puede defender código con bucles y listas.
```

---

## 5. Atención a la diversidad

### Si el alumnado se bloquea con ArrayList

Reducir objetivo:

```text
Crear lista, añadir un recuerdo fijo y mostrar size.
```

### Si se bloquea con for

Primero mostrar sin numeración:

```java
for (String memory : memories) {
    System.out.println(memory);
}
```

Después volver a índice si el grupo está preparado.

### Si se adelanta a ficheros

Reencuadre:

```text
Eso será H6. H3 solo recuerda mientras el programa está abierto.
```

### Si usa IA para decidir colección

Pedir:

```text
Explícame con tus palabras por qué ArrayList y no HashMap.
```

---

## 6. Criterio de éxito de H3

H3 está consolidado si:

```text
[x] El programa ejecuta.
[x] Mantiene menú de H2.
[x] Usa una colección Java.
[x] Guarda recuerdos.
[x] Muestra recuerdos.
[x] Gestiona memoria vacía.
[x] Gestiona entrada vacía.
[x] Tiene pruebas de memoria.
[x] Justifica la colección.
[x] Compara Java con Python.
[x] El alumno puede defender add, size, get, isEmpty y la elección de colección.
[x] No hay persistencia ni complejidad prematura.
```

---

## 7. Conexión con H4

Pregunta final:

```text
Ahora MiniJarvis tiene cada vez más código en Main. ¿Qué problema puede aparecer si seguimos añadiendo funciones ahí?
```

Respuesta esperada:

```text
Main crecerá demasiado y será difícil de entender.
```

Puente a H4:

```text
En H4 aprenderemos a repartir responsabilidades entre clases: Agent, Memory y Main.
```

<!-- AJUSTE-COBERTURA-CONCEPTOS-32 -->

## Ajuste curricular — cobertura de conceptos de Programación

Este hito queda alineado con el mapa `32-lista-conceptos-programacion-por-tema.md`.

```text
Hito: H3
Temas de referencia: Tema 4
Foco: memoria temporal con estructuras de datos
```

Conceptos que deben trabajarse o, como mínimo, quedar conectados con evidencias del alumnado:

- colección
- genéricos
- List
- ArrayList
- índice
- recorrido
- for mejorado
- mutabilidad
- inmutabilidad
- clases envoltorio
- array
- tabla como ampliación
- Set para evitar repetidos
- Map para preferencias por clave

Criterio docente de cierre:

- El alumnado no solo entrega el producto; debe poder señalar dónde aparece cada concepto en su código, README, pruebas o defensa.
- Si un concepto se marca como ampliación, no penaliza al alumnado que alcance el mínimo, pero sí orienta mejora, recuperación o enriquecimiento.
- La defensa debe incluir al menos una pregunta de comprensión sobre los conceptos nuevos del hito.

