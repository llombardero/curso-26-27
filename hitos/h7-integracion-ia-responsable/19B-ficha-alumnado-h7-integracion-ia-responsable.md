# H7 — Integración IA responsable o simulación robusta

<!-- HEXA-CICLO-COMPLETO-POR-HITO:START -->

## Ciclo HEXA obligatorio del reto H7

**Reto del hito:** Integrar o simular una ayuda de IA con límites, seguridad, registro y validación humana.

Debes conservar evidencias de las cuatro fases. Entregar solo el producto final no demuestra el ciclo completo.

| Fase | Pregunta que guía la fase | Acción del profesorado | Acción y evidencia del alumnado |
|---|---|---|---|
| **H — Hecho / reto** | ¿Qué problema real debemos resolver y con qué límites? | Presenta contexto, producto, restricciones, criterios y diagnóstico; no da todavía la solución completa. | Reformula el reto, identifica lo que sabe/no sabe y deja una ficha inicial con criterios de éxito. |
| **E — Exploración** | ¿Qué alternativas, hipótesis o pruebas iniciales ayudan a entenderlo? | Propone preguntas, ejemplos mínimos, casos y límites seguros. | Observa, compara, predice, prueba alternativas y registra decisiones o bloqueos. |
| **X — eXplicación** | ¿Qué conceptos permiten explicar lo observado y decidir con criterio? | Formaliza vocabulario, sintaxis, modelo mental, errores frecuentes, seguridad y criterios de calidad. | Explica con palabras propias, conecta teoría y exploración y corrige sus hipótesis. |
| **A — Aplicación** | ¿Cómo construimos, comprobamos, documentamos y defendemos la solución? | Desbloquea, exige pruebas y comprueba autoría y transferencia. | Implementa el producto, lo prueba, documenta evidencias, realiza review/defensa y propone mejora. |

### Temporalización mínima explícita

H7-S1–S8; 360 min mínimos en la guía autónoma. Los tiempos de fases se reservan dentro de las sesiones indicadas; los rangos pueden solaparse cuando una sesión cierra una fase y abre la siguiente.

| Fase | Reserva y momento recomendado | Puerta de salida |
|---|---|---|
| H | H7-S1; 45 min | Reto reformulado, límites y criterio de éxito visibles. |
| E | H7-S1–S2; 75 min integrados | Hipótesis, comparación, prueba inicial o decisiones justificadas. |
| X | H7-S2–S4; 90 min integrados | Explicación individual breve y conexión con el producto. |
| A | H7-S3–S8; 150 min integrados | Producto comprobado, documentación, defensa y mejora. |

**Expediente HEXA mínimo del hito:** caso de uso y riesgos, clasificación de prompts, explicación de seguridad/validación, simulación o integración segura, registros y defensa.

Regla de avance: puede haber prototipos durante E, pero no se considera completada A si faltan evidencias de H, E o X. Si una fase falta, se recupera esa fase y su evidencia; no se repite automáticamente todo el hito.

<!-- HEXA-CICLO-COMPLETO-POR-HITO:END -->


## Ficha para el alumnado

---

## 1. Reto

Vais a añadir un modo IA responsable a MiniJarvis.

Puede ser:

```text
- integración real controlada, si el profesorado lo autoriza;
- simulación robusta, si no usamos API real.
```

La simulación es una opción válida.

---

## 2. Qué debe tener H7

```text
[x] Caso de uso concreto.
[x] Prompt o entrada controlada.
[x] Bloqueo de datos prohibidos.
[x] Registro de prompts.
[x] Documento de riesgos.
[x] Configuración segura.
[x] Validación humana.
[x] Defensa IA responsable.
```

---

## 3. Qué NO se puede hacer

```text
[ ] Subir API keys.
[ ] Subir .env real.
[ ] Usar datos personales reales.
[ ] Enviar contraseñas o tokens.
[ ] Aceptar respuestas sin revisar.
[ ] Decir que la IA sustituye tu comprensión.
```

---

## 4. Preguntas de defensa

```text
¿Qué datos recibe la IA?
¿Qué no debe recibir nunca?
¿Cómo validaste la respuesta?
¿Qué harías si la IA genera errores?
¿Qué parte puedes explicar sin ayuda?
¿Por qué tu simulación o integración es segura?
```

<!-- AJUSTE-COBERTURA-CONCEPTOS-32 -->

## Ajuste curricular — cobertura de conceptos de Programación

Este hito queda alineado con el mapa `32-lista-conceptos-programacion-por-tema.md`.

```text
Hito: H7
Temas de referencia: Temas 5, 6 y 7
Foco: IA responsable, abstracción y mejora funcional opcional
```

Conceptos que deben trabajarse o, como mínimo, quedar conectados con evidencias del alumnado:

- record AiResponse
- enum para niveles de riesgo
- interfaz AiAssistant como ampliación
- polimorfismo
- Strategy como patrón opcional
- Optional para respuesta bloqueada o ausente
- lambdas como ampliación
- streams para analizar registros
- funciones puras en PromptSafety
- validación humana

Criterio docente de cierre:

- El alumnado no solo entrega el producto; debe poder señalar dónde aparece cada concepto en su código, README, pruebas o defensa.
- Si un concepto se marca como ampliación, no penaliza al alumnado que alcance el mínimo, pero sí orienta mejora, recuperación o enriquecimiento.
- La defensa debe incluir al menos una pregunta de comprensión sobre los conceptos nuevos del hito.

