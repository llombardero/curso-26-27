# Checklist de corrección — H2 Agente con decisiones y depuración

Documento para uso docente.

Relacionado con:

- `14-guia-docente-h2-decisiones-depuracion.md`
- `14B-ficha-alumnado-h2-decisiones-depuracion.md`
- `../../06-rubricas-hitos.md`

---

## 1. Datos de la entrega

Alumno/a o equipo:

```text

```

Repositorio o ubicación:

```text

```

---

## 2. Mínimos técnicos

| Ítem | Sí | Parcial | No | Observaciones |
|---|---|---|---|---|
| Existe `src/Main.java` | | | | |
| El programa se ejecuta | | | | |
| Hay menú o prompt de comandos | | | | |
| El programa se repite hasta `salir` | | | | |
| Implementa `ayuda` | | | | |
| Implementa `saluda` | | | | |
| Implementa `estado` | | | | |
| Implementa `salir` | | | | |
| Gestiona comando desconocido | | | | |

---

## 3. Control de flujo

| Ítem | Sí | Parcial | No | Observaciones |
|---|---|---|---|---|
| Usa bucle correctamente | | | | |
| Usa `if/else` o `switch` de forma comprensible | | | | |
| Compara texto correctamente (`equals` o equivalente) | | | | |
| La salida del programa está controlada | | | | |
| No introduce complejidad fuera de H2 | | | | |

---

## 4. Entornos: pruebas y depuración

| Ítem | Sí | Parcial | No | Observaciones |
|---|---|---|---|---|
| Incluye `docs/pruebas-h2.md` | | | | |
| Prueba comandos principales | | | | |
| Incluye esperado/obtenido | | | | |
| Incluye `docs/depuracion-h2.md` | | | | |
| Usa breakpoint | | | | |
| Observa al menos una variable | | | | |
| Documenta incidencia si apareció | | | | |

---

## 5. Comparación Java ↔ Python

| Ítem | Sí | Parcial | No | Observaciones |
|---|---|---|---|---|
| Incluye comparación | | | | |
| Compara bucle | | | | |
| Compara decisiones | | | | |
| Compara entrada de usuario | | | | |
| Explica diferencias con comprensión | | | | |

---

## 6. Uso de IA

| Ítem | Sí | Parcial | No / N.A. | Observaciones |
|---|---|---|---|---|
| Declara uso de IA | | | | |
| Registra prompts relevantes | | | | |
| Verifica lo aceptado | | | | |
| Puede defender código asistido | | | | |
| No hay uso oculto evidente | | | | |

---

## 7. Preguntas de defensa

| Pregunta | Adecuada | Dudas | No responde | Observaciones |
|---|---|---|---|---|
| ¿Cómo se repite el menú? | | | | |
| ¿Qué hace `salir`? | | | | |
| ¿Qué ocurre con comando desconocido? | | | | |
| ¿Dónde pusiste el breakpoint? | | | | |
| ¿Qué variable observaste? | | | | |
| ¿Qué prueba detectó un fallo? | | | | |
| ¿Qué diferencia viste con Python? | | | | |

---

## 8. Decisión docente

```text
[ ] Evidencia válida.
[ ] Válida con mejoras menores.
[ ] Necesita recuperación parcial.
[ ] No válida todavía.
```

Mejoras solicitadas:

```text

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

