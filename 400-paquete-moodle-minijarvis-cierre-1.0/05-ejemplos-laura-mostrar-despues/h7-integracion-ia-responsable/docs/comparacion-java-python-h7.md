# Comparación Java ↔ Python — H7

## Java

```java
AiResponse response = aiAssistant.answer(prompt);
```

## Python

```python
response = ai_assistant.answer(prompt)
```

## Diferencias

```text
En este ejemplo ambos son simuladores. Java usa clases explícitas como AiResponse y métodos con tipos. Python podría hacerlo de forma más breve. En una integración real ambos necesitarían configuración segura.
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

