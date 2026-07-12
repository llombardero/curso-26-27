# Defensa — H7

## ¿Qué datos recibe la IA?

```text
Recibe solo una pregunta de estudio escrita por el usuario. No debe recibir secretos ni datos personales reales.
```

## ¿Qué no debe recibir nunca?

```text
Contraseñas, tokens, API keys, DNI, teléfonos ni datos personales reales.
```

## ¿Cómo validaste la respuesta?

```text
Comparé la respuesta sobre ArrayList con el código y la documentación de H3. Además, probé que una entrada con password queda bloqueada.
```

<!-- AJUSTE-COBERTURA-CONCEPTOS-32 -->

## Respuesta de Laura — cobertura de conceptos de Programación

Relación con `32-lista-conceptos-programacion-por-tema.md`:

```text
H7 trabaja principalmente: Temas 5, 6 y 7.
Foco de aprendizaje: IA responsable, abstracción y mejora funcional opcional.
```

Conceptos que Laura debe saber defender en este hito:

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

Respuesta modelo de Laura:

> En H7 defiendo que la IA no es magia: filtro prompts, registro usos, bloqueo datos sensibles y valido humanamente cualquier respuesta.

Evidencia que Laura debe señalar:

- una parte concreta del código o documento donde aparezca el concepto;
- una prueba, ejecución, captura o explicación que demuestre que no lo ha copiado sin entender;
- una mejora razonable que podría hacer si tuviera más tiempo.

