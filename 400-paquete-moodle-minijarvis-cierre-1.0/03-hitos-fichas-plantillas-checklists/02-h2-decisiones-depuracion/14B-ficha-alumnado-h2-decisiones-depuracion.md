# H2 — Agente con decisiones y depuración

## Ficha para el alumnado

Curso: 1.º DAW — Programación + Entornos de Desarrollo

---

## 1. Reto

Vais a convertir MiniJarvis H1 en un agente con menú de comandos.

Ahora el programa no debe terminar después del primer saludo. Debe seguir funcionando hasta que la persona usuaria escriba:

```text
salir
```

---

## 2. Qué debe hacer MiniJarvis H2

Comandos mínimos:

| Comando | Qué debe hacer |
|---|---|
| `ayuda` | Mostrar comandos disponibles. |
| `saluda` | Saludar al usuario. |
| `estado` | Mostrar un estado simple del agente. |
| `salir` | Terminar el programa. |
| comando desconocido | Mostrar un mensaje de ayuda o error controlado. |

---

## 3. Qué entra en H2

```text
[x] Menú.
[x] Bucle hasta escribir salir.
[x] if/else o switch.
[x] Comandos básicos.
[x] Comando desconocido.
[x] Pruebas manuales.
[x] Depuración con breakpoint.
[x] Comparación Java ↔ Python.
```

---

## 4. Qué NO entra todavía

```text
[ ] Memoria con listas o mapas.
[ ] Ficheros.
[ ] Varias clases avanzadas.
[ ] Patrones de diseño.
[ ] Conexión con IA real.
[ ] Base de conocimiento.
```

Eso se trabajará en hitos posteriores.

---

## 5. Entregables

```text
h2-decisiones-depuracion/
├── README.md
├── src/
│   └── Main.java
└── docs/
    ├── evidencia-ejecucion-h2.md
    ├── pruebas-h2.md
    ├── depuracion-h2.md
    ├── incidencia-h2.md
    ├── comparacion-java-python-h2.md
    ├── registro-ia.md
    └── defensa-h2.md
```

Plantillas disponibles:

```text
plantillas/README-h2-template.md
plantillas/evidencia-ejecucion-h2-template.md
plantillas/pruebas-h2-template.md
plantillas/depuracion-h2-template.md
plantillas/incidencia-h2-template.md
plantillas/comparacion-java-python-h2-template.md
plantillas/registro-ia-h2-template.md
plantillas/defensa-h2-template.md
```

---

## 6. Pasos recomendados

1. Recuperar el código de H1.
2. Diseñar la tabla de comandos.
3. Crear un bucle `while`.
4. Leer comandos con `Scanner`.
5. Comparar comandos con `.equals()` o usar `switch`.
6. Añadir `salir` como salida controlada.
7. Gestionar comandos desconocidos.
8. Probar cada comando.
9. Usar un breakpoint.
10. Documentar pruebas, depuración e incidencias.

---

## 7. Uso de IA

Puedes usar IA para entender errores, pedir ejemplos de pruebas o comparar con Python.

Debes registrar el uso si afecta a la entrega.

No puedes entregar un menú completo generado por IA si no puedes explicarlo.

---

## 8. Preguntas de defensa

Prepárate para responder:

```text
¿Cómo se repite el menú?
¿Qué ocurre si escribo un comando incorrecto?
¿Qué variable controla la salida?
¿Qué diferencia hay entre == y equals en Java?
¿Dónde pusiste el breakpoint?
¿Qué variable observaste?
¿Qué pruebas hiciste?
¿Qué diferencia viste entre Java y Python?
```

---

## 9. Checklist antes de entregar

```text
[ ] El programa se ejecuta.
[ ] El menú se repite.
[ ] Existe el comando ayuda.
[ ] Existe el comando saluda.
[ ] Existe el comando estado.
[ ] Existe el comando salir.
[ ] Hay respuesta para comando desconocido.
[ ] Hay plan de pruebas.
[ ] Hay evidencia de depuración.
[ ] Hay incidencia documentada si apareció.
[ ] Hay comparación Java ↔ Python.
[ ] He registrado IA si la he usado.
[ ] Puedo defender el flujo del programa.
```

<!-- AJUSTE-COBERTURA-CONCEPTOS-32 -->

## Ajuste curricular — cobertura de conceptos de Programación

Este hito queda alineado con el mapa `32-lista-conceptos-programacion-por-tema.md`.

```text
Hito: H2
Temas de referencia: Temas 1 y 3
Foco: decisiones, menú, repetición y depuración
```

Conceptos que deben trabajarse o, como mínimo, quedar conectados con evidencias del alumnado:

- if/else
- boolean
- comparaciones
- switch
- enhanced switch como ampliación
- while
- do-while como comparación
- for
- condición de salida
- bucle infinito
- pruebas manuales
- error de compilación
- error lógico
- eficiencia básica

Criterio docente de cierre:

- El alumnado no solo entrega el producto; debe poder señalar dónde aparece cada concepto en su código, README, pruebas o defensa.
- Si un concepto se marca como ampliación, no penaliza al alumnado que alcance el mínimo, pero sí orienta mejora, recuperación o enriquecimiento.
- La defensa debe incluir al menos una pregunta de comprensión sobre los conceptos nuevos del hito.

