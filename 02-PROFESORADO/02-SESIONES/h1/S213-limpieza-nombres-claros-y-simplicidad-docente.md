# H1.8 — Limpieza, nombres claros y simplicidad

| Dato | Valor |
|---|---|
| Hito | H1 — Primer asistente ejecutable |
| Duración prevista | 45 minutos |
| Fase HEXA del hito | Ejecutar — revisar y explicar |
| Modalidad de trabajo | **INDIVIDUAL → PAREJAS → comprobación INDIVIDUAL** |

> Alineada con la ficha del alumnado y con la frontera curricular H1/H2.

## Qué vas a aprender

Al terminar, debes revisar el incremento H1 para mejorar sus nombres significativos, conservar solo comentarios útiles y aplicar simplicidad eliminando complejidad innecesaria. Debes comprobar que el código sigue funcionando y defender cada decisión de limpieza sin cambiar el comportamiento observable.

## Contrato curricular de H1.8

### Núcleo — core

- nombres significativos para clases, variables y constantes;
- comentarios útiles que explican intención o contexto, no lo obvio;
- simplicidad y ausencia de complejidad innecesaria;
- revisión, limpieza, ejecución y explicación del código H1.

### Contexto para leer — recognition

- expresiones simples ya presentes en el incremento H1;
- comparación o resultado booleano solo cuando sea necesario para leer, explicar o renombrar código existente.

Estos elementos se reconocen en contexto. No se amplía su dificultad ni se convierten en una práctica evaluable propia.

### Fuera del alcance — out_of_scope

- construir o dominar `if/else`;
- decisiones anidadas;
- operador ternario como técnica;
- condiciones encadenadas;
- menús;
- control de flujo como contenido central.

Su consolidación corresponde a H2. No se introduce material nuevo de H2 para compensar lo que queda fuera de H1.8.

## Antes de entrar en clase

- [ ] Abrir y ejecutar el proyecto H1 que revisará el alumnado.
- [ ] Preparar una copia o rama de trabajo recuperable.
- [ ] Seleccionar un fragmento real con nombres mejorables, un comentario redundante o estructura innecesariamente complicada.
- [ ] Comprobar que el ejemplo no exige aprender control de flujo nuevo.
- [ ] Reservar los últimos minutos para una explicación individual.

## Material imprescindible

- Un ordenador por estudiante o pareja, con JDK e IntelliJ disponibles.
- Proyecto H1 accesible desde el repositorio del equipo.
- Una forma reproducible de ejecutar el comportamiento antes y después de la limpieza.

## Apertura docente

Di en voz alta:

> Hoy no añadimos funcionalidades. Revisamos el código H1 para que otra persona pueda leerlo, ejecutarlo y explicar por qué cada línea sigue ahí.

Aclara el límite:

> Limpiar no significa reescribir por gusto. Primero conservamos el comportamiento; después mejoramos nombres, comentarios y simplicidad con una razón comprobable.

## Temporalización orientativa

| Tiempo | Acción |
|---|---|
| 0–5 min | Presentar el propósito y ejecutar el incremento H1 antes de modificarlo. |
| 5–10 min | Detectar nombres vagos, comentarios redundantes y elementos difíciles de explicar. |
| 10–17 min | Contrastar ejemplos de nombres y comentarios útiles. |
| 17–25 min | Revisar individualmente el código H1 con la checklist. |
| 25–34 min | Aplicar una limpieza mínima y volver a ejecutar. |
| 34–40 min | Revisar en parejas la claridad y la conservación del comportamiento. |
| 40–44 min | Comprobación individual: señalar, justificar y ejecutar una decisión. |
| 44–45 min | Cerrar con una mejora concreta y una exclusión consciente. |

## Ideas y ejemplos

### Nombres que explican intención

Contrasta nombres vagos con nombres que permiten anticipar el propósito:

```java
int x = 4;
String s = "MiniJarvis";
boolean b = true;
```

```java
int horasEstudio = 4;
String nombreAsistente = "MiniJarvis";
boolean objetivoAlcanzado = true;
```

Pregunta:

> ¿Qué versión permite explicar el dato sin buscar todas sus apariciones?

No conviertas el ejercicio en una lista de nombres “correctos”. Un nombre debe ser coherente con lo que representa en ese programa.

### Renombrar sin cambiar el comportamiento

Trabaja una transformación pequeña y comprobable:

```java
final int MAX = 8;
int h = 5;
System.out.println(h + "/" + MAX);
```

```java
final int MAX_HORAS = 8;
int horasEstudio = 5;
System.out.println(horasEstudio + "/" + MAX_HORAS);
```

Antes de editar, registra la salida. Después de renombrar, ejecuta otra vez y comprueba que la salida no cambia.

### Comentarios útiles y comentarios redundantes

Un comentario redundante repite la instrucción:

```java
// Muestra el nombre
System.out.println(nombreAsistente);
```

Un comentario útil conserva una intención que no resulta obvia en la línea:

```java
// Se conserva este formato porque coincide con la evidencia del README.
System.out.println("Asistente: " + nombreAsistente);
```

Pregunta:

> Si eliminamos el comentario, ¿se pierde una decisión o solo una repetición?

No añadas comentarios para compensar nombres confusos. Primero intenta que el código se explique mediante nombres y estructura.

### Quitar adornos sin quitar significado

Revisa elementos que no aportan al incremento H1:

- variables intermedias que no aclaran ninguna idea;
- mensajes duplicados;
- comentarios que narran cada instrucción;
- código antiguo comentado;
- nombres distintos para la misma idea;
- líneas que nadie puede justificar.

Cada eliminación debe responder:

1. ¿Qué aportaba esta línea?
2. ¿Sigue existiendo el comportamiento necesario?
3. ¿Cómo lo hemos comprobado?

### Orden comprensible

Sin introducir funciones o estructuras nuevas, comprueba que el flujo de lectura de H1 sea reconocible:

```text
datos configurados
entrada, si la fuente H1 ya la utiliza
operaciones simples
salida observable
```

El orden no es una plantilla rígida. Debe permitir explicar el programa de arriba abajo sin saltos arbitrarios.

### Leer expresiones existentes — PARA RECONOCER

Puede aparecer una expresión ya presente en H1 para comprobar si el nombre conserva su significado:

```java
int minutosEstudio = horasEstudio * 60;
boolean tieneNombre = !nombreAsistente.isBlank();
```

La expresión o el booleano son contexto de lectura. La tarea consiste en explicar los nombres, la intención y la simplicidad del fragmento, no en construir condiciones nuevas.

### Evitar una falsa simplificación

No aceptes una modificación solo porque reduce líneas. Una versión más corta puede ser más difícil de explicar.

Criterio:

> La versión preferible conserva el comportamiento y permite justificar mejor sus nombres, comentarios y pasos.

## Secuencia de trabajo y modalidad

### Diagnosticar la limpieza — INDIVIDUAL

Cada estudiante identifica en el código H1:

- un nombre que ya sea significativo;
- un nombre que pueda mejorar;
- un comentario útil o redundante;
- una línea o elemento cuya necesidad deba justificarse;
- una comprobación para demostrar que el comportamiento se conserva.

No se modifica todavía el código.

### Acordar cambios mínimos — PAREJAS

La pareja compara los diagnósticos y elige cambios concretos. Para cada cambio anota:

```text
ANTES
CAMBIO PROPUESTO
MOTIVO
COMPROBACIÓN
```

No se acepta “queda mejor” como motivo suficiente.

### Limpiar y ejecutar — PAREJAS

Aplicad solo los cambios acordados:

1. ejecutad el estado anterior;
2. realizad una modificación pequeña;
3. ejecutad de nuevo;
4. comparad el comportamiento observable;
5. conservad o revertid el cambio según la evidencia.

No añadáis funcionalidades nuevas durante esta revisión.

### Revisar claridad y simplicidad — PAREJAS

Otra pareja comprueba:

- si los nombres expresan lo que representan;
- si los comentarios conservados aportan intención o contexto;
- si existe complejidad innecesaria;
- si cada integrante puede explicar las líneas modificadas;
- si la evidencia demuestra que H1 sigue funcionando.

La pareja revisora pregunta antes de proponer una reescritura.

### Comprobar comprensión — INDIVIDUAL

Cada persona debe poder:

- señalar una mejora de nombre y justificarla;
- distinguir un comentario útil de uno redundante;
- explicar qué se simplificó y qué se conservó;
- ejecutar una comprobación observable;
- defender por qué no añadió una funcionalidad nueva.

Para reconocer:

- leer una expresión simple o un booleano ya existente sin convertirlo en el núcleo de la explicación.

## Evidencia que permanece

- **GitHub:** incremento H1 limpio, simple, ejecutable y con cambios revisables.
- **README:** solo se modifica si la limpieza cambia una explicación técnica que ya debía mantenerse allí.
- **Scrum:** solo si existe una tarea, decisión, mejora o bloqueo real del equipo.
- **Diario individual:** solo si la revisión produjo un aprendizaje o decisión significativa.
- **Moodle / Drive / Site:** sin nueva entrega específica en H1.8.

No se crean capturas rutinarias, formularios ni documentos paralelos de limpieza.

## Observación docente

Observa específicamente:

- que el alumnado ejecuta antes y después de modificar;
- que conserva el comportamiento del incremento;
- que elige nombres vinculados a la intención real;
- que no conserva comentarios redundantes por inercia;
- que no elimina una línea que no comprende sin investigarla;
- que evita reescrituras amplias sin evidencia;
- que puede explicar individualmente una decisión de limpieza;
- que las expresiones o booleanos existentes permanecen como contexto de lectura;
- que no introduce `if/else`, anidados, ternarios, menús ni control de flujo como contenido nuevo.

## Andamiaje ante bloqueos

- **No sabe renombrar:** pregunta qué representa el dato y en qué unidad se expresa.
- **Quiere comentarlo todo:** pide separar intención de repetición literal.
- **Quiere borrar una línea que no entiende:** exige localizar primero su efecto observable.
- **Hace muchos cambios a la vez:** vuelve a una modificación pequeña y una ejecución.
- **La salida cambia:** compara el último cambio y decide si alteró el comportamiento.
- **Propone una técnica de H2:** vuelve al objetivo de limpieza del código H1 existente.
- **El código funciona pero no se entiende:** pide señalar el nombre, comentario u orden que dificulta explicarlo.

No proporciones una solución completa. Devuelve la decisión a la intención del código y a la evidencia de ejecución.

## Comprueba lo aprendido

Pregunta de control:

> ¿Qué nombre, comentario o elemento simplificaste, por qué mejora la lectura y qué ejecución demuestra que el comportamiento sigue siendo el mismo?

Pregunta de límite:

> ¿Qué cambio decidiste no hacer porque añadía complejidad o contenido propio de otro hito?

Criterio para cerrar:

- existe al menos una mejora justificada;
- el comportamiento H1 permanece comprobado;
- no se ha añadido funcionalidad;
- cada persona puede explicar una decisión y una exclusión.

Di en voz alta:

> Código limpio no significa código decorado ni código más corto. Significa código que cumple H1 y puede leerse, comprobarse y defenderse.

## Al terminar

Anota solo lo operativo para preparar la siguiente intervención docente:

- alumnado que necesita apoyo para explicar su código;
- nombre, comentario o estructura que causó confusión frecuente;
- bloqueo técnico pendiente y siguiente paso;
- ajuste de tiempo necesario.