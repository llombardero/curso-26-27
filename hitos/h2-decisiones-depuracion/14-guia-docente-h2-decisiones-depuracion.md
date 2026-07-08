# Guía docente — H2 Agente con decisiones y depuración

## Programación + Entornos de Desarrollo — 1.º DAW — Curso 2026/2027

Versión: borrador 0.1

Documento para uso del profesorado.

Documentos relacionados:

- `../../02-calendario-hitos-sprints-2026-2027.md`
- `../../04A-enunciados-y-entregables-alumnado.md`
- `../../06-rubricas-hitos.md`
- `README.md`
- `14B-ficha-alumnado-h2-decisiones-depuracion.md`
- `14C-checklist-correccion-h2.md`

---

## 1. Propósito del hito

H2 transforma MiniJarvis H1 en un agente con menú de comandos.

Producto esperado:

```text
MiniJarvis H2: agente por consola con menú, comandos básicos, repetición hasta salir, gestión de comandos desconocidos, pruebas manuales y evidencia de depuración.
```

El hito introduce:

- estructuras de selección;
- estructuras de repetición;
- salida controlada;
- entradas no válidas;
- pruebas manuales;
- depuración con breakpoint;
- comparación Java ↔ Python;
- registro de IA si se usa.

---

## 2. Qué añade H2 respecto a H1

| H1 | H2 |
|---|---|
| Programa lineal. | Programa que se repite hasta escribir `salir`. |
| Saludo y nombre. | Menú con comandos. |
| Variables y constantes. | Decisiones, bucles y control de entrada. |
| README básico. | README + pruebas + depuración + incidencia. |
| Defensa de conceptos básicos. | Defensa de flujo, menú, breakpoint y casos de prueba. |

---

## 3. Restricciones didácticas

En H2 sí debe aparecer:

- menú;
- bucle de repetición;
- selección con `if/else` o `switch`;
- comandos `ayuda`, `saluda`, `estado`, `salir`;
- gestión de comando desconocido;
- pruebas manuales;
- evidencia de depuración.

En H2 todavía NO debe aparecer:

- memoria en listas o mapas;
- persistencia en ficheros;
- varias clases propias obligatorias;
- interfaces o patrones;
- conexión con IA real;
- arquitectura extensible;
- base de conocimiento.

Motivo:

```text
H2 debe consolidar control de flujo antes de introducir memoria, diseño orientado a objetos o integración IA.
```

---

## 4. Fechas y duración

Fechas orientativas:

```text
13 octubre - 6 noviembre 2026
```

Carga estimada:

```text
Programación: 28 periodos de 45 min
Entornos: 8 periodos de 45 min
```

---

## 5. RA/CE y evidencias

### Programación

RA principales:

- PR RA3: estructuras de control, depuración y código con decisiones/repetición.
- Refuerzo PR RA1/RA2.

Evidencias:

- menú funcional;
- bucle hasta `salir`;
- comandos básicos;
- gestión de entrada no válida;
- defensa del flujo del programa.

### Entornos de Desarrollo

RA principales:

- ED RA3.a-b: tipos de pruebas y casos de prueba.
- ED RA3.c-e: depuración, breakpoints y seguimiento de variables.
- ED RA3.h: documentación de incidencias.

Evidencias:

- `docs/pruebas-h2.md`;
- `docs/depuracion-h2.md`;
- `docs/incidencia-h2.md`;
- evidencia de ejecución;
- defensa corta.

---

## 6. Producto mínimo esperado

Comandos mínimos:

| Comando | Comportamiento esperado |
|---|---|
| `ayuda` | Muestra comandos disponibles. |
| `saluda` | Saluda usando el nombre del usuario o del asistente. |
| `estado` | Muestra un mensaje simple de estado del agente. |
| `salir` | Termina el programa de forma controlada. |
| Otro texto | Muestra mensaje de comando desconocido. |

Ejemplo orientativo:

```text
Hola, soy MiniJarvis.
¿Cómo te llamas? Laura

Comandos disponibles: ayuda, saluda, estado, salir
> saluda
Hola, Laura. Soy MiniJarvis.
> estado
Estoy funcionando en modo H2, sin memoria todavía.
> inventa
No entiendo ese comando. Escribe ayuda.
> salir
Hasta pronto, Laura.
```

---

## 7. Secuencia didáctica sugerida

| Bloque | Foco | Producto parcial |
|---|---|---|
| 1 | Recordar H1 y presentar H2 | Diferencia H1/H2 clara. |
| 2 | Diseñar comandos mínimos | Tabla de comandos y respuestas. |
| 3 | Crear bucle principal | Programa se repite hasta `salir`. |
| 4 | Añadir selección | `if/else` o `switch` para comandos. |
| 5 | Gestionar entradas no válidas | Comando desconocido controlado. |
| 6 | Plan de pruebas manuales | Casos con esperado/obtenido. |
| 7 | Depuración en IntelliJ | Breakpoint y variable observada. |
| 8 | Comparación Java ↔ Python | Menú equivalente y diferencias. |
| 9 | Defensa y recuperación | Validación individual. |

---

## 8. Desarrollo docente paso a paso

### Bloque 1 — Reencuadrar desde H1

Mensaje docente:

```text
H1 era una secuencia lineal. H2 añade decisiones y repetición. MiniJarvis ahora podrá recibir comandos hasta que el usuario escriba salir.
```

Pregunta inicial:

```text
¿Qué tiene que cambiar en nuestro código para que el programa no termine después del primer mensaje?
```

Respuesta esperable:

```text
Necesitamos un bucle.
```

### Bloque 2 — Diseñar comandos antes de programar

Antes de escribir código, pedir una tabla:

| Comando | Respuesta esperada |
|---|---|
| ayuda | |
| saluda | |
| estado | |
| salir | |
| otro | |

Criterio:

```text
Un comando está bien definido si podemos probar qué debe ocurrir.
```

### Bloque 3 — Bucle principal

Idea base:

```java
boolean running = true;
while (running) {
    System.out.print("> ");
    String command = scanner.nextLine();
    // decisiones aquí
}
```

Evitar profundizar todavía en arquitecturas por clases o patrones.

### Bloque 4 — Selección

Opción con `if/else`:

```java
if (command.equals("ayuda")) {
    System.out.println("Comandos: ayuda, saluda, estado, salir");
} else if (command.equals("salir")) {
    running = false;
} else {
    System.out.println("No entiendo ese comando.");
}
```

Si se usa `switch`, mantenerlo simple y defendible.

### Bloque 5 — Pruebas manuales

Casos mínimos:

- comando `ayuda`;
- comando `saluda`;
- comando `estado`;
- comando desconocido;
- comando `salir`;
- mayúsculas/espacios si se decide gestionar con `trim()` o `toLowerCase()`.

### Bloque 6 — Depuración

Breakpoint recomendado:

```text
Línea posterior a leer command = scanner.nextLine();
```

Variable a observar:

```text
command
running
userName
```

Preguntas:

```text
¿Qué valor tiene command cuando escribes ayuda?
¿Qué rama del if/switch se ejecuta?
¿Cuándo cambia running a false?
```

---

## 9. Entregables H2

| Entregable | Responsable | Formato | Plantilla local |
|---|---|---|---|
| Código Java con menú | Equipo/individual según decisión docente | `src/Main.java` | No aplica. |
| README H2 | Equipo/individual | `README.md` | `plantillas/README-h2-template.md` |
| Evidencia de ejecución | Equipo/individual | `docs/evidencia-ejecucion-h2.md` | `plantillas/evidencia-ejecucion-h2-template.md` |
| Plan de pruebas | Equipo | `docs/pruebas-h2.md` | `plantillas/pruebas-h2-template.md` |
| Informe de depuración | Individual/equipo | `docs/depuracion-h2.md` | `plantillas/depuracion-h2-template.md` |
| Incidencia | Equipo/individual | `docs/incidencia-h2.md` | `plantillas/incidencia-h2-template.md` |
| Comparación Java ↔ Python | Individual, casa | `docs/comparacion-java-python-h2.md` | `plantillas/comparacion-java-python-h2-template.md` |
| Registro IA | Individual | `docs/registro-ia.md` | `plantillas/registro-ia-h2-template.md` |
| Defensa H2 | Individual | `docs/defensa-h2.md` | `plantillas/defensa-h2-template.md` |

---

## 10. Uso de IA en H2

Permitido:

- entender errores;
- pedir ejemplos de casos de prueba;
- pedir explicación de `while`, `if`, `switch`, `equals`, `trim` o `toLowerCase`;
- generar una versión Python para comparar;
- preparar preguntas de defensa.

Condiciones:

- registrar el uso;
- verificar manualmente;
- adaptar al nivel del hito;
- poder defender el código.

No permitido:

- entregar un menú completo generado por IA sin entender;
- añadir memoria, clases avanzadas o IA real por sugerencia de la herramienta;
- ocultar uso de IA;
- aceptar código que no se puede explicar.

---

## 11. Errores previsibles

| Error | Señal | Intervención docente |
|---|---|---|
| Usa `==` para comparar texto | Comandos no funcionan | Explicar `.equals()` en Java. |
| Bucle infinito sin salida | `salir` no termina | Revisar variable `running`. |
| No gestiona comando desconocido | No ocurre nada | Añadir rama `else` o `default`. |
| El menú solo se muestra una vez | Alumno no entiende el bucle | Dibujar flujo del programa. |
| Mezcla H3/H4 | Añade listas/clases complejas | Reencuadrar: H2 es control de flujo. |
| IA genera solución avanzada | No puede defender | Pedir versión mínima H2. |

---

## 12. Rúbrica H2 resumida

| Dimensión | Excelente | Adecuado | Básico | Insuficiente |
|---|---|---|---|---|
| Menú y control de flujo | Menú robusto y salida controlada. | Menú funcional básico. | Menú parcial o frágil. | No hay menú funcional. |
| Estructuras de control | Selección y repetición claras. | Uso correcto principal. | Uso confuso o limitado. | No aplica lo requerido. |
| Pruebas manuales | Casos variados con esperado/obtenido. | Pruebas básicas suficientes. | Pruebas escasas. | Sin pruebas. |
| Depuración | Breakpoint, variables y aprendizaje documentados. | Evidencia básica. | Evidencia superficial. | Sin depuración. |
| Comparación Java ↔ Python | Compara con comprensión. | Comparación suficiente. | Superficial. | No entregada/no defendible. |
| IA responsable | Registro, verificación y defensa. | Registro suficiente. | Incompleto. | Uso oculto/no defendible. |

---

## 13. Preparación para H3

Antes de pasar a H3, comprobar:

- si el menú se repite correctamente;
- si `salir` termina de forma controlada;
- si el alumnado entiende `equals`;
- si sabe probar comandos;
- si puede usar un breakpoint básico;
- si diferencia comando desconocido de error del programa.

H3 añadirá memoria temporal mediante colecciones.
