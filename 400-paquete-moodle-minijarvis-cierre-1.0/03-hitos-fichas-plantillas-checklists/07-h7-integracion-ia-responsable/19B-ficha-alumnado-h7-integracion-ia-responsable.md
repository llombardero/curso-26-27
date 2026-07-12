# H7 — Integración IA responsable o simulación robusta

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

