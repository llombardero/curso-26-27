# Capítulo 10 — IA responsable en proyectos de programación

## Hitos relacionados

```text
H7
```

## Qué aprenderás

- simulación robusta
- prompt
- PromptSafety
- validación humana
- riesgos IA
- configuración segura

## 1. Punto de partida

MiniJarvis se construye por capas. Este capítulo trabaja una pieza concreta del proyecto y la conecta con evidencias reales: código, pruebas, documentación, defensa y uso responsable de IA si procede.

La regla de estudio es siempre la misma:

```text
Lee el concepto, ejecuta un ejemplo pequeño, aplícalo a MiniJarvis, documenta la evidencia y prepárate para defenderlo.
```

## 2. Conceptos básicos explicados

La IA responsable no significa conectar una API real a toda costa. En 1.º DAW es válido usar una simulación robusta para practicar el flujo: prompt, filtro de seguridad, respuesta limitada, registro y validación humana.

Un prompt puede contener información sensible. Por eso MiniJarvis debe bloquear contraseñas, tokens, API keys, DNI, teléfonos reales y datos personales. La respuesta de IA nunca sustituye tu comprensión.

## 3. Ejemplo guiado en Java

```java
public class PromptSafety {
    public boolean isSafe(String prompt) {
        if (prompt == null || prompt.trim().isEmpty()) return false;
        String lower = prompt.toLowerCase();
        return !lower.contains("password")
            && !lower.contains("contraseña")
            && !lower.contains("token")
            && !lower.contains("api key");
    }
}
```

## 4. Caso práctico MiniJarvis

Implementa un modo `ia` simulado. Prueba un prompt seguro: “Explícame ArrayList para estudiar”. Prueba uno inseguro: “Mi password es 1234”. El segundo debe bloquearse.

Documenta ambos sin copiar secretos completos.

## 5. Evidencia de Entornos de Desarrollo

Crea `docs/registro-prompts.md`, `docs/riesgos-ia.md`, `docs/configuracion-segura.md` y `docs/validacion-humana.md`. `.env.example` puede existir; `.env` real no.

## 6. Errores frecuentes y cómo corregirlos

| Error | Síntoma | Corrección |
|---|---|---|
| Simulación no declarada | Parece IA real | Mostrar aviso explícito |
| Registrar secreto completo | Riesgo de exposición | Resumir prompt bloqueado |
| Aceptar respuesta sin validar | Aprendizaje débil | Contrastar y reescribir con palabras propias |

## 7. Preguntas de repaso

1. ¿Por qué una simulación robusta puede ser válida?
2. ¿Qué no debe recibir nunca una IA?
3. ¿Qué es validación humana?
4. ¿Qué diferencia hay entre .env.example y .env real?

## 8. Para tu portfolio

Copia y completa este bloque en tu portfolio:

```text
Capítulo 10: IA responsable en proyectos de programación
Qué he aprendido:
Código o documento que lo demuestra:
Prueba realizada:
Error que he corregido:
Qué puedo defender oralmente:
Uso de IA, si lo hubo, y cómo lo validé:
```

## 9. Estudio paso a paso

La IA responsable empieza por limitar el caso de uso. MiniJarvis no debe responder cualquier cosa ni recibir cualquier dato. Un filtro básico no es seguridad perfecta, pero ayuda a practicar buenas decisiones. La validación humana sigue siendo obligatoria porque una respuesta puede sonar bien y estar equivocada.

Caso de estudio: prueba tres prompts: uno verde, uno ámbar y uno rojo. El verde puede recibir respuesta simulada. El ámbar debe pedir revisión cuidadosa. El rojo debe bloquearse. En el registro no copies el dato sensible: escribe “prompt con contraseña bloqueado”.
