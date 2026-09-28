# Guía de entregables H1 — Qué, cómo, cuándo y dónde

> Esta guía resume todo lo que el alumnado debe entregar en H1, organizado por entregable, con indicaciones claras de qué rellenar, cuándo pedirlo y dónde entregarlo.

---

## Resumen rápido por sesión

| Sesión | Entregable | Qué se pide | Dónde se entrega | Moodle |
|---|---|---|---|---|
| S206 | Backlog inicial Scrum | Tareas de alcance, roles, frase de alcance | Sheet Scrum del equipo | No |
| S206 | Diario individual S206 | Frase "H1 consiste en...", duda sobre alcance | Sheet Diario individual | No |
| S207 | Primera ejecución | Código + salida + frase explicativa | GitHub, Drive (screenshot), diario, Scrum | No |
| S208 | Estructura mínima + error | Código con estructura + error provocado y corregido | GitHub, diario, Scrum | No |
| S209 | Decisión de mensaje | Alternativas, decisión, razón | Sheet Scrum, GitHub, diario si aplica | No |
| S210 | Plan de datos | Tabla: dato, tipo, nombre, cambia, uso | Scrum/documento enlazado, GitHub, diario | No |
| S211 | Constante, operación, predicción | Código con `final`, operación, predicción confirmada | GitHub, diario, Scrum | No |
| S212 | Entrada y conversión | Scanner, `parseInt()`, caso válido + caso error | GitHub, diario, Scrum | No |
| S213 | Comparación e if/else | Código con `if/else`, caso true + caso false | GitHub, diario, Scrum | No |
| S214 | README H1 | Qué hace, límites, cómo ejecutar, ejemplo real | Raíz del repositorio GitHub | Borrador |
| S214 | Evidencia de ejecución formal | Entrada, salida esperada, salida obtenida, enlace profundo | README, repositorio o Drive | Borrador |
| S214 | Diario individual revisado | Filas completas de todas las sesiones | Sheet Diario individual | No |
| S214 | Scrum de equipo actualizado | Backlog completo, decisiones, review, retrospectiva | Sheet Scrum del equipo | No |
| S214 | Site personal H1 | Reto, aportación, evidencia seleccionada, próximo paso | Página H1 del Site personal | No |
| S214 | Site de equipo H1 | Incremento, decisiones, pruebas, review, retrospectiva | Página H1 del Site de equipo | No |
| S215 | Defensa individual | Señalar, explicar, ejecutar, comprobar (oral) | En clase (oral) | No |
| S215 | Retrospectiva equipo Scrum | 4 frases: funcionó, no funcionó, mantener, cambiar | Sheet Scrum del equipo | No |
| S215 | Entrega Moodle H1 | Todos los enlaces profundos + declaración | Tarea Moodle | **SÍ, oficial** |

---

## Detalle de cada entregable

### 1. Backlog inicial Scrum (S206)

**Qué es:** Las primeras tareas del equipo para H1.

**Qué se pide:**
- Una tarea grande: `Entender alcance H1`
- Tres subtareas: `definir qué entra`, `definir qué queda fuera`, `escribir requisitos comprobables`
- Roles provisionales: facilitador, responsable de backlog, responsable técnico, responsable de documentación
- Frase de alcance H1
- Lista de lo que entra y lo que queda fuera

**Cuándo pedirlo:** Primeros 10 minutos de S206.

**Dónde:** Sheet Scrum del equipo.

**Cómo:** Filas concretas con: tarea, responsable o pareja responsable, estado inicial (pendiente), sesión S206.

**Qué NO vale:** Tareas vagas como "hacer Java" con estado "más o menos".

---

### 2. Diario individual S206 (S206)

**Qué es:** La primera entrada del diario personal del alumno/a.

**Qué se pide:**
- Una fila con: fecha, sesión (S206), hit (H1), objetivo, acción, prueba y resultado, evidencia enlazada, bloqueo (si aplica), uso de IA, próximo paso
- Frase personal: "H1 consiste en..."
- Marcar una duda sobre el alcance
- Enlace a la decisión del equipo en Scrum

**Cuándo pedirlo:** Durante S206, después de definir el alcance.

**Dónde:** Sheet Diario individual (no documento aparte).

**Qué NO vale:** Copiar la decisión del equipo sin reflexión personal.

---

### 3. Primera ejecución (S207)

**Qué es:** Evidencia de que el programa imprime algo por consola.

**Qué se pide:**
- Código con `System.out.println` en `Main.java`
- Salida visible por consola
- Frase explicativa: "Sé que se ha ejecutado porque..."
- Commit con mensaje útil (ej: "S207: primera ejecucion por consola"), NO solo "cambios"

**Cuándo pedirlo:** Durante S207.

**Dónde:**
- GitHub: código (`Main.java`)
- Drive: screenshot si se usa (debe mostrar código + consola, no solo consola)
- Diario individual: enlace a evidencia + frase explicativa
- Scrum: marcar tarea "primera ejecucion" como done o blocked

**Qué NO vale:** Screenshot de consola sola sin código. Frase "funciona" sin explicación.

---

### 4. Estructura mínima + error corregido (S208)

**Qué es:** Evidencia de que el alumno/a entiende la estructura de Java y puede corregir errores de sintaxis.

**Qué se pide:**
- Código con estructura mínima: `class`, `main`, `System.out.println`, `;`
- Nota en el diario sobre un error provocado y corregido
- Explicación de una regla sintáctica cuya ruptura impide la compilación

**Cuándo pedirlo:** Durante S208.

**Dónde:**
- GitHub: código o micropráctica
- Diario individual: fila S208 con error, hipótesis, corrección, resultado
- Scrum: si el equipo detecta un error común, registrarlo como decisión

**Qué se debe demostrar:** Comprensión de clase, punto de entrada, instrucción que muestra texto, regla sintáctica.

---

### 5. Decisión de mensaje (S209)

**Qué es:** Registro de la decisión sobre el mensaje de saludo del asistente.

**Qué se pide:**
- Al menos dos alternativas de mensaje
- Una razón para elegir una sobre la otra
- Código con el mensaje elegido implementado

**Cuándo pedirlo:** Durante S209.

**Dónde:**
- Sheet Scrum: alternativa elegida, alternativa descartada, razón
- GitHub: código con mensaje implementado
- Diario individual: fila si el alumno/a cambió o defendió una decisión

**Qué se debe demostrar:** Capacidad de tomar decisiones técnicas con justificación.

---

### 6. Plan de datos (S210)

**Qué es:** Tabla que organiza los datos que el programa va a usar antes de escribir código.

**Qué se pide:**
- Tabla con columnas: dato, tipo, nombre, cambia (sí/no), uso
- Nombres claros y descriptivos (NO `x`, `dato1`, `valor`)
- Código con variables implementadas según el plan

**Cuándo pedirlo:** Durante S210, antes de escribir más código.

**Dónde:**
- Scrum o documento enlazado desde Scrum
- GitHub: código con variables usadas
- Diario individual: fila S210 con una variable explicada y prueba de salida

**Qué se debe demostrar:** Diferencia entre variable y valor. Cada alumno/a debe poder señalar una variable y explicar su tipo, nombre, valor inicial y una asignación posterior.

---

### 7. Constante, operación y predicción (S211)

**Qué es:** Evidencia de uso de `final`, operaciones aritméticas y capacidad de predecir resultados.

**Qué se pide:**
- Código con `final` (constante)
- Operación aritmética verificable
- Predicción escrita antes de ejecutar
- Resultado comparado con la predicción

**Cuándo pedirlo:** Durante S211.

**Dónde:**
- GitHub: código con `final`, operación y salida
- Diario individual: predicción, resultado observado, explicación breve
- Scrum: marcar tareas de constante/operación/prueba

**Qué se debe demostrar:** Predicción, ejecución, comparación y corrección si es necesario.

---

### 8. Entrada y conversión (S212)

**Qué es:** Evidencia de lectura de entrada por teclado y conversión de tipos.

**Qué se pide:**
- Código con `Scanner` y `nextLine()`
- Código con `Integer.parseInt()` o conversión similar
- Caso de prueba válido: entrada, resultado esperado, resultado obtenido
- Caso de prueba con entrada no convertible: explicación del error

**Cuándo pedirlo:** Durante S212.

**Dónde:**
- GitHub: código con `Scanner` o micropráctica de conversión
- README: puede ir recogiendo ejemplos (se pedirá formalmente en S214)
- Diario individual: fila S212 con caso válido y error de conversión explicado
- Scrum: tarea de entrada/conversión actualizada

**Qué se debe demostrar:** Flujo pedir → leer → guardar → convertir → mostrar.

**Qué NO vale:** Screenshot sin indicar qué entrada se usó. Código que lee una variable pero no la usa. Decir "no funciona" sin distinguir entre error de compilación y error de ejecución.

---

### 9. Comparación e if/else con dos ramas (S213)

**Qué es:** Evidencia de uso de comparaciones y estructura condicional.

**Qué se pide:**
- Código con comparación y `if/else`
- Caso de prueba con resultado `true` (rama if)
- Caso de prueba con resultado `false` (rama else)
- Mejora concreta aplicada a nombres o código

**Cuándo pedirlo:** Durante S213.

**Dónde:**
- GitHub: código con comparación y `if/else`
- Diario individual: Caso A (expected/obtained) + Caso B (expected/obtained)
- Scrum: marcar pruebas true/false y registrar mejora

**Qué se debe demostrar:** Ambas ramas están probadas. El alumno/a puede defender: qué comparación se evalúa, qué significa true/false, qué rama se ejecuta en cada caso.

**Qué NO vale:** Probar solo el caso favorable.

---

### 10. README H1 (S214)

**Qué es:** Documento que explica el producto H1 en la raíz del repositorio.

**Qué se pide:**
- Sección "Qué hace": 3 líneas describiendo el producto
- Sección "Límites de H1": qué NO incluye y por qué
- Sección "Cómo ejecutar": pasos exactos
- Sección "Ejemplo de ejecución" o "Pruebas": caso normal + caso alternativo con entrada, salida esperada y salida obtenida
- Sección "Decisiones técnicas": tabla con decisión, motivo, enlace a código
- Sección "Microprácticas del Tema 1": tabla con concepto, archivo/commit, prueba
- Sección "Limitaciones deliberadas"
- Sección "Versión evaluada": tag/commit, fecha, integrantes y aportación

**Cuándo pedirlo:** S214 (se empieza a construir desde S207, se completa en S214).

**Dónde:** Raíz del repositorio GitHub (`README.md`).

**Qué NO vale:** Prometer menú, memoria o IA real si no existen. Enlaces generales a carpetas (deben ser enlaces profundos).

---

### 11. Evidencia de ejecución formal (S214)

**Qué es:** Registro formal de la ejecución con todos los detalles.

**Qué se pide:**
- Entrada utilizada (valor concreto)
- Salida esperada (predicción)
- Salida obtenida (resultado real)
- Qué demuestra esta ejecución
- Enlace profundo al código, commit o prueba (NO enlace general a carpeta)

**Cuándo pedirlo:** S214.

**Dónde:** README, repositorio o Drive con enlace profundo.

**Qué NO vale:** Enlace general a carpeta. Solo "funciona" sin explicación.

---

### 12. Diario individual revisado (S214)

**Qué es:** Revisión completa de todas las filas del diario.

**Qué se pide:**
- Una fila por sesión (S206-S214)
- Cada fila con: objetivo, acción, prueba, resultado, evidencia enlazada, bloqueo, uso de IA, próximo paso
- Completar filas que estén incompletas

**Cuándo pedirlo:** S214.

**Dónde:** Sheet Diario individual (no documento aparte).

---

### 13. Scrum de equipo actualizado (S214)

**Qué es:** Tablero Scrum completo con todo el historial de H1.

**Qué se pide:**
- Backlog completo con todas las tareas
- Tareas con responsable, estado (pending/in progress/done/blocked)
- Sección de decisiones del equipo
- Sección de bloqueos
- Enlaces a evidencias
- Mini-review
- Retrospectiva final (se completa en S215)

**Cuándo pedirlo:** S214 (review), S215 (retrospectiva).

**Dónde:** Sheet Scrum del equipo.

---

### 14. Site personal H1 (S214-S215)

**Qué es:** Página H1 del Site personal del alumno/a.

**Qué se pide:**
- El reto en sus propias palabras
- Su aportación personal (qué hizo él/ella)
- Evidencia seleccionada (enlace profundo, NO copia del diario)
- Qué demuestra la evidencia
- Concepto del Tema 1 que ahora puede explicar
- Decisión o bloqueo significativo
- Uso de IA (solo si fue relevante)
- Próximo paso para H2
- Checklist de comprobación

**Cuándo pedirlo:** Se inicia en S214, se finaliza en S215.

**Dónde:** Página H1 del Site personal.

**Qué NO vale:** Copiar el diario. Duplicar información.

---

### 15. Site de equipo H1 (S214-S215)

**Qué es:** Página H1 del Site de equipo.

**Qué se pide:**
- Incremento logrado (qué hace MiniJarvis)
- Decisiones tomadas (qué se excluyó y por qué)
- Pruebas realizadas
- Review (¿el incremento cumple el alcance de S206?)
- Retrospectiva (qué mantener y qué cambiar en H2)

**Cuándo pedirlo:** Se inicia en S214, se finaliza en S215.

**Dónde:** Página H1 del Site de equipo.

---

### 16. Defensa individual (S215)

**Qué es:** Comprobación oral y práctica del alumno/a sobre su producto.

**Qué se pide (el alumno/a debe ser capaz de):**
1. Señalar dónde empieza la ejecución (`class`, `main`)
2. Señalar una variable y explicar tipo, nombre y valor
3. Señalar una constante y explicar por qué es constante
4. Ejecutar con una entrada ficticia y predecir la salida
5. Explicar una conversión
6. Provocar o explicar un error de conversión
7. Señalar una comparación
8. Ejecutar un caso `true` y un caso `false` de `if/else`
9. Explicar qué queda fuera de H1 y por qué
10. Cambiar un mensaje o valor pequeño y predecir el efecto

**Cuándo pedirlo:** S215, en clase (oral).

**Dónde:** En clase, oralmente.

**Formato:** Cada respuesta defendible tiene cuatro partes: señalo, explico, ejecuto, compruebo.

**Si aparece un hueco:** El alumno/a debe recuperar la evidencia concreta: investigar, corregir, probar y explicar de nuevo.

---

### 17. Retrospectiva equipo Scrum (S215)

**Qué es:** Cierre reflexivo del equipo sobre H1.

**Qué se pide:**
- Cuatro frases concretas:
  1. Qué funcionó bien
  2. Qué no funcionó bien
  3. Qué mantendremos en H2
  4. Qué cambiaremos en H2
- Evidencias enlazadas

**Cuándo pedirlo:** S215.

**Dónde:** Sheet Scrum de equipo, sección retrospectiva.

---

### 18. Entrega Moodle H1 (S215) — ENTREGA OFICIAL

**Qué es:** La entrega oficial de H1. "Si no está en Moodle, no está entregado oficialmente."

**Qué se pide:**
- Enlace al repositorio GitHub
- Enlace al README H1 o repositorio con README visible
- Enlace a la página H1 del Site personal (uno por miembro)
- Enlace a la página H1 del Site de equipo
- Enlace al Sheet Scrum del equipo o sección H1
- Enlace a evidencia concreta de ejecución (si Moodle lo solicita)
- Confirmación de permisos revisados
- Mini-declaración: "Confirmo que los enlaces llevan a evidencias concretas de H1 y que he comprobado los permisos de acceso."

**Formato si Moodle permite texto de entrega:**
```
Equipo: [nombre]
Integrantes: [nombres]

Repositorio GitHub: [enlace]
README H1: [enlace]
Site personal H1 - [nombre]: [enlace]
Site personal H1 - [nombre]: [enlace]
Site equipo H1: [enlace]
Scrum equipo H1: [enlace]
Evidencia de ejecución: [enlace]

Permisos comprobados: sí/no
Observaciones o bloqueo pendiente: [texto]
```

**Cuándo pedirlo:** S215 (cierre oficial).

**Dónde:** Tarea Moodle de H1.

**Qué NO vale:** "Está todo en Drive." Enlaces generales a carpetas. Enlaces que no se pueden abrir (permisos incorrectos).

---

## Resumen visual: flujo de entregas

```
S206 ──► Backlog Scrum + Diario S206
  │
S207 ──► Primera ejecución (GitHub + diario + Scrum)
  │
S208 ──► Estructura + error (GitHub + diario + Scrum)
  │
S209 ──► Decisión de mensaje (Scrum + GitHub)
  │
S210 ──► Plan de datos (Scrum + GitHub + diario)
  │
S211 ──► Constante + operación (GitHub + diario + Scrum)
  │
S212 ──► Entrada + conversión (GitHub + diario + Scrum)
  │
S213 ──► Comparación + if/else (GitHub + diario + Scrum)
  │
S214 ──► README + evidencias + Sites + diario revisado + Scrum actualizado
  │         (Moodle: borrador)
  │
S215 ──► Defensa oral + retrospectiva + entrega Moodle (OFICIAL)
```

---

## Espacios de entrega: qué va en cada sitio

| Espacio | Qué contiene |
|---|---|
| **Moodle** | Entrega final de enlaces y recepción de feedback. Solo al cierre. |
| **GitHub** | Código, README, historial de commits, microprácticas. |
| **Diario individual (Sheets)** | Proceso personal: objetivo, acción, prueba, resultado, bloqueo, uso de IA, próximo paso. |
| **Scrum de equipo (Sheets)** | Backlog, tareas, decisiones, bloqueos, review, retrospectiva, enlaces. |
| **Site personal** | Selección razonada de evidencias individuales al cierre del hito. |
| **Site de equipo** | Comunicación del incremento del equipo al cierre del hito. |
| **Drive** | Evidencias no código y recursos de equipo, siempre con enlaces profundos. |

---

## Reglas generales

1. **Una evidencia no es una captura suelta.** Debe permitir comprobar: qué entrada se usó, qué salida se obtuvo, dónde está el código/documento y qué demuestra.
2. **Enlaces profundos, no carpetas genéricas.** Cada enlace debe llevar a un archivo o página concreta, no a la carpeta raíz.
3. **Comprobar permisos.** Un enlace que solo abre el propietario no es una entrega válida.
4. **No duplicar información.** El diario cuenta el proceso; el README explica cómo ejecutar; el Site personal selecciona aprendizaje; el Site de equipo comunica el incremento; Moodle cierra la entrega oficial.
5. **Si no está en Moodle, no está entregado oficialmente.**
