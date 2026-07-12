# H7 — Integración IA responsable o simulación robusta

Alumna: Laura García Martín  
Equipo: Equipo Ada

---

## Tipo

```text
[x] Simulación robusta
[ ] Integración real autorizada
```

No se usa API real ni clave secreta.

---

## Cómo ejecutar

```bash
javac src/*.java
java -cp src Main
```

---

## Caso de uso

```text
Pedir una sugerencia breve de estudio o explicación conceptual sin enviar datos personales ni secretos.
```

---

## Seguridad

```text
.env real prohibido.
.env.example permitido.
No se introducen contraseñas, tokens, API keys, DNI ni teléfonos reales.
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

