# Guía docente completa — H7 sesión a sesión

## Integración IA responsable o simulación robusta — MiniJarvis H7

## Programación + Entornos de Desarrollo — 1.º DAW — Curso 2026/2027

Versión: borrador 0.1

Documento autónomo para uso del profesorado.

Este documento permite impartir H7 completo sin abrir ningún otro material durante la clase.

---

## 1. Propósito de H7

H7 cierra la evolución técnica de MiniJarvis incorporando un modo IA responsable, limitado y defendible.

Producto final:

```text
MiniJarvis H7: agente por consola con modo IA responsable, preferentemente mediante simulación robusta local, con bloqueo de datos prohibidos, registro de prompts, análisis de riesgos, configuración segura, validación humana y defensa individual.
```

H7 introduce:

```text
- diferencia entre integración real y simulación robusta;
- caso de uso IA limitado y educativo;
- clase `SimulatedAiAssistant`;
- clase `PromptSafety`;
- clase `AiResponse`;
- comando o modo `ia`;
- bloqueo de secretos y datos personales;
- `.env.example` permitido y `.env` real prohibido;
- registro de prompts;
- documento de riesgos IA;
- validación humana de respuestas;
- comparación Java ↔ Python sobre integración IA;
- defensa H7.
```

Idea docente central:

```text
H7 no consiste en conectar cualquier IA a cualquier precio. H7 consiste en demostrar que MiniJarvis puede usar o simular IA de forma limitada, segura, trazable y validada por una persona.
```

---

## 2. Restricciones de H7

En H7 sí entra:

```text
[x] Simulación robusta local sin red como opción preferente.
[x] Integración real solo si el profesorado la autoriza expresamente.
[x] Caso de uso limitado: sugerencia de estudio o explicación conceptual.
[x] Entrada o prompt controlado.
[x] Bloqueo de secretos y datos personales.
[x] Registro de prompts usados.
[x] Documento de riesgos IA.
[x] Configuración segura.
[x] Validación humana de respuestas.
[x] Comparación Java ↔ Python.
[x] Defensa de qué hace, qué no hace y qué nunca debe recibir la IA.
```

En H7 NO entra:

```text
[ ] Subir API keys.
[ ] Subir `.env` real.
[ ] Pedir credenciales reales al alumnado.
[ ] Enviar datos personales reales a servicios externos.
[ ] Enviar contraseñas, tokens, DNI, teléfonos o direcciones reales.
[ ] Aceptar respuestas de IA sin revisión humana.
[ ] Sustituir la comprensión del alumnado por una respuesta generada.
[ ] Romper el cierre del proyecto por una integración externa frágil.
```

Frase docente:

```text
Una simulación robusta y bien defendida es mejor que una API real insegura, inestable o imposible de explicar.
```

---

## 3. Diseño mínimo de referencia

Partimos de H6:

```text
MiniJarvis ya puede guardar recuerdos, registrar eventos y documentar seguridad básica.
```

En H7 añadimos un modo IA responsable:

| Clase | Responsabilidad |
|---|---|
| `Main` | Crear y arrancar el agente. |
| `Agent` | Gestionar el menú y el modo IA. |
| `SimulatedAiAssistant` | Generar respuestas controladas sin API real. |
| `PromptSafety` | Bloquear prompts con secretos o datos personales. |
| `AiResponse` | Representar respuesta, bloqueo y mensaje de seguridad. |
| `HistoryLog` | Registrar evento técnico si se mantiene desde H6. |

Estructura esperada:

```text
h7-integracion-ia-responsable/
├── README.md
├── .gitignore
├── .env.example
├── src/
│   ├── Main.java
│   ├── Agent.java
│   ├── SimulatedAiAssistant.java
│   ├── PromptSafety.java
│   └── AiResponse.java
└── docs/
    ├── registro-prompts-h7.md
    ├── riesgos-ia-h7.md
    ├── configuracion-segura-h7.md
    ├── validacion-humana-h7.md
    ├── comparacion-java-python-h7.md
    ├── portfolio-h7.md
    └── defensa-h7.md
```

Código orientativo mínimo:

```java
public class AiResponse {
    private boolean allowed;
    private String message;
    private String safetyNote;

    public AiResponse(boolean allowed, String message, String safetyNote) {
        this.allowed = allowed;
        this.message = message;
        this.safetyNote = safetyNote;
    }

    public boolean isAllowed() {
        return allowed;
    }

    public String getMessage() {
        return message;
    }

    public String getSafetyNote() {
        return safetyNote;
    }
}
```

```java
public class PromptSafety {
    public boolean isSafe(String prompt) {
        if (prompt == null) {
            return false;
        }
        String lower = prompt.toLowerCase();
        return !lower.contains("password")
            && !lower.contains("contraseña")
            && !lower.contains("token")
            && !lower.contains("api key")
            && !lower.contains("dni")
            && !lower.contains("teléfono");
    }
}
```

```java
public class SimulatedAiAssistant {
    private PromptSafety safety;

    public SimulatedAiAssistant() {
        this.safety = new PromptSafety();
    }

    public AiResponse answer(String prompt) {
        if (!safety.isSafe(prompt)) {
            return new AiResponse(false, "Solicitud bloqueada.", "No introduzcas secretos ni datos personales.");
        }
        return new AiResponse(true,
            "Sugerencia simulada: divide el problema, revisa tus apuntes y valida la respuesta con tu propio criterio.",
            "Respuesta simulada. Requiere validación humana.");
    }
}
```

Nota didáctica:

```text
La simulación no pretende engañar al alumnado. Debe decir claramente que es simulada. Sirve para practicar flujos de seguridad, prompts, validación y defensa sin depender de credenciales reales.
```

---

## 4. Secuencia de sesiones H7

Preparación docente antes de iniciar H7:

```text
1. Decidir por defecto simulación robusta local.
2. No pedir claves API al alumnado.
3. Preparar ejemplos de prompts seguros e inseguros.
4. Preparar una explicación clara de validación humana.
5. Recordar que H7 es breve y no debe comprometer la defensa final.
6. Mantener visible la regla: ninguna credencial, ningún dato personal real, ninguna respuesta sin revisar.
7. Preparar el puente hacia HF: demo final, portfolio, recuperación y mejora.
```

Material mínimo de aula:

```text
- editor o IDE Java;
- terminal para compilar y ejecutar;
- pizarra para semáforo de IA;
- registro de prompts;
- tabla de riesgos;
- documento de validación humana;
- README reproducible.
```

Propuesta de 8 sesiones de 45 minutos, por ser un hito breve de cierre técnico.

| Sesión | Foco | Producto parcial |
|---|---|---|
| H7-S1 | Presentar IA responsable y simulación robusta | Caso de uso seguro. |
| H7-S2 | Diseñar prompts permitidos y prohibidos | Semáforo de prompts. |
| H7-S3 | Crear `PromptSafety` | Bloqueo básico de secretos/datos. |
| H7-S4 | Crear `SimulatedAiAssistant` y `AiResponse` | Respuesta simulada controlada. |
| H7-S5 | Integrar modo `ia` en `Agent` | Flujo seguro de consulta. |
| H7-S6 | Registro de prompts, riesgos y configuración segura | Documentos H7. |
| H7-S7 | Validación humana y comparación Java ↔ Python | Validación + comparación. |
| H7-S8 | Defensa H7 y cierre hacia HF | H7 validado y listo para presentación final. |

---

# H7-S1 — Presentar IA responsable y simulación robusta

## Duración

```text
45 minutos
```

## Objetivo

Que el alumnado entienda que H7 puede resolverse con una simulación robusta y que el valor del hito está en el uso responsable, no en consumir una API real.

## Resultado esperado

Caso de uso seguro redactado:

```text
MiniJarvis H7 ayudará a pedir una sugerencia breve de estudio o una explicación conceptual, sin enviar datos personales, secretos ni credenciales.
```

## Guion docente

```text
MiniJarvis se llama agente IA desde el inicio del proyecto, pero hasta ahora hemos construido sus bases: comandos, memoria, clases, extensibilidad, persistencia y trazabilidad.

En H7 añadimos un modo IA responsable. Puede ser real si existe autorización y configuración segura, pero por defecto usaremos una simulación robusta.

Una simulación robusta no es hacer trampa. Es practicar el flujo: entrada, filtro de seguridad, respuesta, aviso de limitación y validación humana.
```

## Pizarra

```text
H7 = IA responsable

No buscamos:
- API real a toda costa;
- claves compartidas;
- respuestas sin revisar.

Buscamos:
- caso limitado;
- seguridad;
- trazabilidad;
- validación humana;
- defensa.
```

## Qué explicas tú

```text
- Diferencia entre integración real y simulación robusta.
- Por qué una API real implica credenciales, costes, privacidad y red.
- Por qué para 1.º DAW es suficiente simular si el flujo está bien diseñado.
- Qué significa validación humana: comprobar, contrastar y no copiar ciegamente.
```

## Actividad HEXA guiada

### H — Hecho

Un alumno quiere preguntar a MiniJarvis: “Explícame ArrayList para estudiar”.

### E — Explorar

Pregunta:

```text
¿Es un uso razonable? ¿Qué riesgos tiene? ¿Qué debería hacer MiniJarvis después de responder?
```

Respuestas esperadas:

```text
- es razonable si no incluye datos sensibles;
- la respuesta puede ser incompleta o equivocada;
- debe avisar de que hay que validarla;
- debe registrarse el prompt de forma responsable.
```

### X — eXplicar

Conclusión:

```text
El caso de uso será ayuda de estudio limitada y validada, no toma de decisiones automática.
```

### A — Aplicar

Redactar caso de uso.

## Actividad

```text
1. Escribir qué hará el modo IA.
2. Escribir qué NO hará.
3. Elegir tres prompts seguros.
4. Elegir tres prompts prohibidos.
5. Escribir una frase de advertencia para el usuario.
```

Ejemplos seguros:

```text
Explícame ArrayList con un ejemplo sencillo.
Dame una estrategia para depurar un NullPointerException.
Sugiere pasos para preparar la defensa H7.
```

Ejemplos prohibidos:

```text
Mi contraseña es 1234, ¿la recuerdas?
Usa este token: abc123.
Analiza el DNI/teléfono real de una persona.
```

## Errores frecuentes

| Error | Señal | Intervención docente |
|---|---|---|
| Creer que simulación no vale | “Si no hay API real, no es IA” | Reencuadrar: evaluamos flujo responsable. |
| Querer meter una API sin permisos | Piden claves o cuentas | Bloquear: sin autorización no hay API real. |
| Caso de uso demasiado amplio | “Que responda cualquier cosa” | Limitar a estudio y explicación conceptual. |
| Olvidar validación humana | Respuesta se acepta sin revisar | Añadir aviso obligatorio. |

## Cierre

Ticket:

```text
1. ¿Por qué una simulación robusta es válida en H7?
2. Escribe un prompt seguro.
3. Escribe un dato que nunca debe recibir la IA.
```

## Criterio de éxito

```text
El alumnado entiende el objetivo responsable de H7 y define un caso de uso limitado, seguro y defendible.
```

---

# H7-S2 — Diseñar prompts permitidos y prohibidos

## Duración

```text
45 minutos
```

## Objetivo

Crear una política de prompts con semáforo: usos permitidos, usos con cuidado y usos prohibidos.

## Resultado esperado

Primer borrador de `docs/registro-prompts-h7.md` y tabla de semáforo IA.

## Guion docente

```text
Antes de escribir código de IA, decidimos las reglas de uso.

Si no sabemos qué prompts permitimos y cuáles bloqueamos, el código será improvisado.

Usaremos un semáforo: verde permitido, ámbar requiere cuidado y rojo prohibido.
```

## Pizarra

```text
Verde:
explicaciones conceptuales, ayuda de estudio, preguntas técnicas sin datos sensibles.

Ámbar:
código generado, respuestas largas, dudas que requieren verificación.

Rojo:
secretos, datos personales, credenciales, sustitución de defensa, copiar sin entender.
```

## Qué explicas tú

```text
- Qué es un prompt.
- Que un prompt también puede contener información sensible.
- Que no todo lo técnicamente posible es didácticamente aceptable.
- Que el registro de prompts debe permitir reflexionar, no vigilar por vigilar.
```

## Actividad HEXA guiada

### H — Hecho

Prompt: “Mi password es 1234, recuérdamela”.

### E — Explorar

Pregunta:

```text
¿Qué debería hacer MiniJarvis: responder, avisar o bloquear?
```

### X — eXplicar

Respuesta esperada:

```text
Debe bloquear y explicar que no se introducen secretos.
```

### A — Aplicar

Clasificar prompts.

## Actividad

Tabla:

| Prompt | Verde/Ámbar/Rojo | Motivo | Acción de MiniJarvis |
|---|---|---|---|
| Explícame ArrayList | Verde | Estudio sin datos sensibles | Responder + recordar validar |
| Hazme toda la defensa | Ámbar/Rojo | Sustituye comprensión | Reencuadrar o bloquear |
| Mi token es... | Rojo | Secreto | Bloquear |
| Revisa este error de compilación | Verde/Ámbar | Técnico, verificar | Responder con cautela |

## Plantilla de registro de prompts

```markdown
# Registro de prompts H7

| Fecha | Prompt resumido | Semáforo | Respuesta/acción | Validación humana | Aprendizaje |
|---|---|---|---|---|---|
| | | | | | |
```

## Errores frecuentes

| Error | Señal | Intervención docente |
|---|---|---|
| Registrar prompts con datos sensibles completos | Copian el secreto | Resumir sin reproducir el dato. |
| Todo verde | No detectan riesgos | Volver a secretos, datos personales y copia. |
| Todo rojo | Bloquean usos educativos razonables | Permitir ayuda de estudio con validación. |
| No explicar motivo | Solo ponen color | Exigir motivo y acción. |

## Cierre

Ticket:

```text
1. ¿Qué significa semáforo rojo?
2. ¿Qué prompt verde usarías para estudiar?
3. ¿Por qué no se debe copiar un secreto en el registro?
```

## Criterio de éxito

```text
El alumnado clasifica prompts y entiende que la seguridad empieza antes del código.
```

---

# H7-S3 — Crear PromptSafety

## Duración

```text
45 minutos
```

## Objetivo

Implementar una clase sencilla que bloquee prompts con señales de secretos o datos personales.

## Resultado esperado

Archivo `src/PromptSafety.java` con método `isSafe(String prompt)` y prueba manual con un prompt seguro y uno bloqueado.

## Guion docente

```text
Hoy convertimos la política de prompts en una primera regla de código.

PromptSafety no será perfecto. Es una barrera didáctica inicial para detectar palabras de riesgo y obligarnos a pensar antes de responder.
```

## Pizarra

```text
PromptSafety:
- recibe texto;
- normaliza a minúsculas;
- busca señales de riesgo;
- devuelve true o false.
```

## Qué explicas tú

```text
- Que un filtro simple no sustituye el criterio humano.
- Que buscar palabras como password, token o DNI es un primer paso.
- Que habrá falsos positivos y falsos negativos.
- Que por eso H7 exige validación humana.
```

## Actividad HEXA guiada

### H — Hecho

PromptSafety ve el texto: “Mi token es abc123”.

### E — Explorar

Pregunta:

```text
¿Qué palabra debería activar el bloqueo?
```

### X — eXplicar

Respuesta esperada:

```text
La palabra token.
```

### A — Aplicar

Crear reglas iniciales.

## Código base guiado

```java
public class PromptSafety {
    public boolean isSafe(String prompt) {
        if (prompt == null || prompt.trim().isEmpty()) {
            return false;
        }

        String lower = prompt.toLowerCase();

        if (lower.contains("password")) {
            return false;
        }
        if (lower.contains("contraseña")) {
            return false;
        }
        if (lower.contains("token")) {
            return false;
        }
        if (lower.contains("api key")) {
            return false;
        }
        if (lower.contains("dni")) {
            return false;
        }
        if (lower.contains("teléfono")) {
            return false;
        }

        return true;
    }
}
```

## Actividad

```text
1. Crear PromptSafety.java.
2. Añadir palabras prohibidas.
3. Probar mentalmente cinco prompts.
4. Escribir dos limitaciones del filtro.
5. Compilar.
```

Comando:

```bash
javac src/*.java
```

Limitaciones esperadas:

```text
- puede no detectar un secreto escrito de otra forma;
- puede bloquear una pregunta legítima sobre qué es una contraseña;
- necesita validación humana;
- no sustituye una política de uso.
```

## Errores frecuentes

| Error | Señal | Intervención docente |
|---|---|---|
| Vender el filtro como perfecto | “Ya es seguro” | Reforzar limitaciones. |
| No comprobar null/vacío | Errores o respuestas absurdas | Añadir validación inicial. |
| Bloquear solo inglés | No detecta contraseña | Añadir términos en español. |
| Guardar el prompt sensible completo | Queda en docs/logs | Resumir sin secreto. |

## Cierre

Ticket:

```text
1. ¿Qué hace PromptSafety?
2. ¿Por qué no es suficiente por sí solo?
3. Escribe una palabra que debería bloquear.
```

## Criterio de éxito

```text
Existe un filtro básico de prompts y el alumnado puede explicar sus límites.
```

---

# H7-S4 — Crear SimulatedAiAssistant y AiResponse

## Duración

```text
45 minutos
```

## Objetivo

Crear una simulación local de asistente IA que responda de forma controlada y bloquee prompts inseguros.

## Resultado esperado

Archivos:

```text
src/AiResponse.java
src/SimulatedAiAssistant.java
```

con respuesta segura y respuesta bloqueada.

## Guion docente

```text
Hoy creamos el corazón de la simulación.

SimulatedAiAssistant no llama a Internet. Usa reglas locales y responde de forma limitada. Esto permite practicar seguridad, validación y defensa sin claves reales.
```

## Pizarra

```text
Prompt -> PromptSafety -> SimulatedAiAssistant -> AiResponse

Si seguro:
respuesta simulada + aviso de validación

Si inseguro:
bloqueo + motivo
```

## Qué explicas tú

```text
- Qué ventaja tiene devolver un objeto AiResponse en vez de solo un String.
- Que una respuesta puede estar permitida o bloqueada.
- Que siempre debe aparecer una nota de seguridad o validación.
- Que la simulación debe ser transparente.
```

## Actividad HEXA guiada

### H — Hecho

El prompt es seguro: “Explícame bucles while”.

### E — Explorar

Pregunta:

```text
¿Qué debería contener la respuesta además de la explicación?
```

### X — eXplicar

Respuesta esperada:

```text
Debe incluir aviso de que es simulada y debe validarse.
```

### A — Aplicar

Crear clases de respuesta y simulador.

## Código base guiado

```java
public class AiResponse {
    private boolean allowed;
    private String message;
    private String safetyNote;

    public AiResponse(boolean allowed, String message, String safetyNote) {
        this.allowed = allowed;
        this.message = message;
        this.safetyNote = safetyNote;
    }

    public boolean isAllowed() {
        return allowed;
    }

    public String getMessage() {
        return message;
    }

    public String getSafetyNote() {
        return safetyNote;
    }
}
```

```java
public class SimulatedAiAssistant {
    private PromptSafety safety;

    public SimulatedAiAssistant() {
        this.safety = new PromptSafety();
    }

    public AiResponse answer(String prompt) {
        if (!safety.isSafe(prompt)) {
            return new AiResponse(
                false,
                "Solicitud bloqueada.",
                "No introduzcas secretos, credenciales ni datos personales."
            );
        }

        return new AiResponse(
            true,
            "Respuesta simulada: identifica el concepto, busca un ejemplo pequeño y verifica el resultado con tu código.",
            "Esta respuesta es simulada y requiere validación humana."
        );
    }
}
```

## Actividad

```text
1. Crear AiResponse.java.
2. Crear SimulatedAiAssistant.java.
3. Conectar con PromptSafety.
4. Compilar.
5. Escribir en el registro qué ocurre con un prompt seguro y uno inseguro.
```

Prueba conceptual:

```text
Seguro: Explícame ArrayList para estudiar.
Inseguro: Mi password es 1234.
```

## Errores frecuentes

| Error | Señal | Intervención docente |
|---|---|---|
| Ocultar que es simulación | Parece API real | Exigir nota explícita de simulación. |
| Devolver solo String | No distingue bloqueo | Usar AiResponse con allowed. |
| No incluir safety note | Falta validación | Añadir aviso obligatorio. |
| Respuestas demasiado ambiciosas | Simula cualquier tema | Mantener ayuda de estudio limitada. |

## Cierre

Ticket:

```text
1. ¿Por qué AiResponse tiene `allowed`?
2. ¿Qué devuelve la simulación ante un prompt inseguro?
3. ¿Por qué debe decir que es simulada?
```

## Criterio de éxito

```text
La simulación responde de forma controlada, bloquea prompts inseguros y comunica sus límites.
```

---

# H7-S5 — Integrar modo ia en Agent

## Duración

```text
45 minutos
```

## Objetivo

Integrar el asistente simulado en el flujo de MiniJarvis mediante un comando o modo `ia`.

## Resultado esperado

MiniJarvis acepta:

```text
ia
Explícame ArrayList para estudiar
```

Y también bloquea:

```text
ia
Mi password es 1234
```

## Guion docente

```text
Ya tenemos el filtro y el asistente simulado. Ahora MiniJarvis debe usarlos.

El modo ia debe pedir una consulta, pasarla por la simulación y mostrar respuesta o bloqueo. Además debe recordar que la persona valida la respuesta.
```

## Pizarra

```text
Usuario -> Agent -> SimulatedAiAssistant -> PromptSafety -> AiResponse -> Usuario
```

## Qué explicas tú

```text
- Dónde vive el asistente simulado.
- Cómo Agent recoge el prompt.
- Cómo mostrar respuesta y nota de seguridad.
- Por qué se registran prompts resumidos, no secretos completos.
```

## Actividad HEXA guiada

### H — Hecho

El usuario escribe `ia` y después una pregunta.

### E — Explorar

Pregunta:

```text
¿Qué pasos debe seguir el programa antes de mostrar respuesta?
```

### X — eXplicar

Secuencia esperada:

```text
1. Pedir prompt.
2. Evaluar seguridad.
3. Responder o bloquear.
4. Mostrar nota de validación.
5. Registrar uso de forma responsable.
```

### A — Aplicar

Integrar en Agent.

## Código orientativo

```java
private SimulatedAiAssistant aiAssistant;

public Agent() {
    this.aiAssistant = new SimulatedAiAssistant();
}
```

Método de comando:

```java
private void useAiMode() {
    System.out.print("Consulta IA segura: ");
    String prompt = scanner.nextLine();

    AiResponse response = aiAssistant.answer(prompt);
    System.out.println(response.getMessage());
    System.out.println("Nota: " + response.getSafetyNote());

    if (!response.isAllowed()) {
        System.out.println("La consulta ha sido bloqueada por seguridad.");
    }
}
```

Si el grupo mantiene herramientas `Tool`, puede crear:

```text
AiTool implementa Tool y llama a SimulatedAiAssistant.
```

## Actividad

```text
1. Añadir SimulatedAiAssistant como atributo.
2. Crear comando `ia` o AiTool.
3. Probar prompt seguro.
4. Probar prompt inseguro.
5. Registrar ambos casos sin copiar secretos completos.
```

Prueba mínima:

```text
ayuda
ia
Explícame ArrayList para estudiar
ia
Mi password es 1234
salir
```

## Errores frecuentes

| Error | Señal | Intervención docente |
|---|---|---|
| No bloquear prompt inseguro | Responde a password/token | Revisar PromptSafety. |
| No mostrar nota de validación | Parece respuesta definitiva | Añadir safetyNote. |
| Registrar secreto completo | Queda en docs/logs | Registrar resumen: “prompt con contraseña bloqueado”. |
| Romper comandos anteriores | ayuda/salir fallan | Probar flujo mínimo completo. |

## Cierre

Ticket:

```text
1. ¿Qué comando activa el modo IA?
2. ¿Qué ocurre con un prompt inseguro?
3. ¿Qué debe hacer una persona antes de aceptar la respuesta?
```

## Criterio de éxito

```text
MiniJarvis integra un modo IA simulado que responde a consultas seguras, bloquea consultas peligrosas y recuerda la validación humana.
```

---

# H7-S6 — Registro de prompts, riesgos y configuración segura

## Duración

```text
45 minutos
```

## Objetivo

Documentar el uso de prompts, los riesgos de IA y la configuración segura del proyecto.

## Resultado esperado

Documentos:

```text
docs/registro-prompts-h7.md
docs/riesgos-ia-h7.md
docs/configuracion-segura-h7.md
```

## Guion docente

```text
Un modo IA responsable no se defiende solo con código.

Necesitamos evidencias: qué prompts se probaron, qué riesgos conocemos y cómo está configurado el proyecto para no exponer secretos.
```

## Pizarra

```text
Evidencias H7:
- registro de prompts;
- riesgos IA;
- configuración segura;
- validación humana.
```

## Qué explicas tú

```text
- Que registrar no es copiar secretos, sino resumir de forma segura.
- Qué riesgos básicos existen: alucinación, sesgo, privacidad, dependencia, seguridad.
- Que `.env.example` puede mostrar nombres de variables sin valores reales.
- Que `.env` real debe estar en .gitignore y no subirse.
```

## Actividad HEXA guiada

### H — Hecho

MiniJarvis bloquea “Mi token es...”.

### E — Explorar

Pregunta:

```text
¿Cómo lo registramos sin copiar el token?
```

### X — eXplicar

Respuesta esperada:

```text
Se registra como “prompt con token bloqueado”, sin valor del token.
```

### A — Aplicar

Completar documentos.

## Plantilla de riesgos IA

```markdown
# Riesgos IA H7

| Riesgo | Ejemplo | Medida aplicada | Cómo lo defenderé |
|---|---|---|---|
| Alucinación | Respuesta incorrecta | Validación humana | No aceptar sin comprobar |
| Privacidad | Dato personal en prompt | PromptSafety | Bloqueo y aviso |
| Secreto | Token/API key | .gitignore + bloqueo | No introducir secretos |
| Dependencia | Copiar sin entender | Defensa oral | Explicar con palabras propias |
```

## Plantilla de configuración segura

```markdown
# Configuración segura H7

## Tipo de solución

[x] Simulación robusta local
[ ] Integración real autorizada

## Ficheros permitidos

- `.env.example` sin valores reales

## Ficheros prohibidos

- `.env` real
- claves `.key`
- tokens `.token`

## .gitignore mínimo

```text
.env
*.key
*.token
```

## Decisión de seguridad

No usamos API real en H7 porque la simulación permite practicar el flujo sin gestionar credenciales.
```

## Actividad

```text
1. Completar registro de prompts con un seguro y un bloqueado.
2. Completar tabla de riesgos.
3. Crear o revisar .env.example si procede.
4. Verificar que .env real está prohibido.
5. Escribir decisión final: simulación o integración autorizada.
```

## Errores frecuentes

| Error | Señal | Intervención docente |
|---|---|---|
| Registro con secretos completos | Copia token | Sustituir por resumen seguro. |
| Riesgos genéricos | No conectan con código | Pedir medida concreta: PromptSafety. |
| `.env.example` con clave real | Valor secreto visible | Borrar y dejar placeholders. |
| Configuración insegura por ambición | API real sin autorización | Volver a simulación. |

## Cierre

Ticket:

```text
1. ¿Qué riesgo IA has documentado?
2. ¿Qué fichero está permitido: .env o .env.example?
3. ¿Cómo registras un prompt bloqueado sin copiar el secreto?
```

## Criterio de éxito

```text
El alumnado documenta prompts, riesgos y configuración segura sin exponer información sensible.
```

---

# H7-S7 — Validación humana y comparación Java ↔ Python

## Duración

```text
45 minutos
```

## Objetivo

Formalizar cómo se valida una respuesta de IA y comparar una integración/simulación IA en Java con una aproximación equivalente en Python.

## Resultado esperado

Documentos:

```text
docs/validacion-humana-h7.md
docs/comparacion-java-python-h7.md
docs/portfolio-h7.md
```

## Guion docente

```text
La respuesta de IA no es el final del trabajo. Es una propuesta que una persona debe revisar.

Validar significa comprobar si es correcta, segura, útil y adecuada al nivel. Si no puedo explicarla, no puedo entregarla como aprendizaje propio.
```

## Pizarra

```text
Validación humana:
1. ¿Es correcta?
2. ¿Es segura?
3. ¿La entiendo?
4. ¿La puedo contrastar?
5. ¿La he adaptado con mis palabras?
```

Comparación:

```text
Java:
clases SimulatedAiAssistant, PromptSafety, AiResponse

Python:
función o clase que valida prompt y devuelve dict/objeto

Idea común:
filtrar -> responder -> validar
```

## Qué explicas tú

```text
- Que validar no es solo leer por encima.
- Que una respuesta útil puede tener errores.
- Que Java estructura con clases y tipos explícitos.
- Que Python puede expresar la misma idea con menos código, pero necesita la misma responsabilidad.
```

## Actividad HEXA guiada

### H — Hecho

La simulación responde: “Revisa tus apuntes y prueba un ejemplo pequeño”.

### E — Explorar

Pregunta:

```text
¿Cómo validamos que esa respuesta es útil?
```

### X — eXplicar

Respuestas esperadas:

```text
- comprobar que no contiene datos sensibles;
- comprobar que no promete hacer la tarea por el alumno;
- contrastar con apuntes o código;
- escribir aprendizaje propio.
```

### A — Aplicar

Completar validación de una respuesta.

## Plantilla de validación humana

```markdown
# Validación humana H7

## Prompt resumido

## Respuesta recibida

## ¿Es segura?

## ¿Es correcta?

## ¿Qué he contrastado?

## Qué acepto

## Qué rechazo

## Qué escribo con mis palabras
```

## Plantilla comparación Java ↔ Python

```markdown
# Comparación Java ↔ Python — H7

| Concepto | Java | Python | Qué debo recordar |
|---|---|---|---|
| Filtro de seguridad | `PromptSafety.isSafe` | función `is_safe(prompt)` | La idea es bloquear entradas peligrosas. |
| Respuesta | `AiResponse` | diccionario u objeto | Conviene separar permitido, mensaje y nota. |
| Simulación | `SimulatedAiAssistant` | clase o función local | No requiere API real. |
| Configuración | `.env.example` sin secretos | `.env.example` sin secretos | Nunca subir `.env` real. |
| Validación | documento de validación | documento/checklist | La persona decide si acepta. |
```

## Actividad

```text
1. Elegir una respuesta segura generada o simulada.
2. Validarla con la plantilla.
3. Completar comparación Java/Python.
4. Completar portfolio H7.
5. Preparar tres frases de defensa.
```

Tres frases de defensa:

```text
Mi modo IA es seguro porque...
Mi modo IA es limitado porque...
Mi respuesta se valida porque...
```

## Errores frecuentes

| Error | Señal | Intervención docente |
|---|---|---|
| Validación vacía | “Está bien” | Pedir criterios concretos. |
| Comparación demasiado avanzada | APIs reales, frameworks, embeddings | Volver a filtro, respuesta y validación. |
| Copiar respuesta IA como portfolio | Lenguaje no propio | Reescribir con evidencias del código. |
| No reconocer límites | “La IA siempre acierta” | Introducir alucinación y contrastes. |

## Cierre

Ticket:

```text
1. ¿Qué significa validar una respuesta IA?
2. ¿Qué se parece entre Java y Python en este flujo?
3. ¿Qué frase usarás para defender la simulación?
```

## Criterio de éxito

```text
El alumnado valida respuestas con criterio y compara Java/Python sin perder el foco en seguridad y responsabilidad.
```

---

# H7-S8 — Defensa H7 y cierre hacia HF

## Duración

```text
45 minutos
```

## Objetivo

Validar H7 mediante ejecución, bloqueo de prompt inseguro, documentación de riesgos, configuración segura y defensa individual.

## Resultado esperado

H7 entregado con:

```text
- código Java compilable y ejecutable;
- modo IA simulado o integración real autorizada;
- filtro de prompts;
- respuesta segura o bloqueo;
- registro de prompts;
- documento de riesgos;
- configuración segura;
- validación humana;
- comparación Java ↔ Python;
- portfolio H7;
- defensa individual;
- puente hacia presentación final HF.
```

## Guion docente

```text
Hoy defendemos el uso responsable de IA, no la espectacularidad de la respuesta.

Una defensa H7 válida debe demostrar dos cosas: que el modo IA puede ayudar en un caso limitado y que sabe bloquear o rechazar usos peligrosos.
```

## Pizarra

```text
Defensa H7:
1. Ejecuta.
2. Prompt seguro.
3. Respuesta + nota de validación.
4. Prompt inseguro.
5. Bloqueo.
6. Registro de prompts.
7. Riesgos.
8. Configuración segura.
9. Validación humana.
```

## Qué explicas tú

```text
- Que no se penaliza usar simulación si está bien defendida.
- Que se evalúa seguridad y comprensión.
- Que una integración real sin seguridad sería peor que una simulación clara.
- Que H7 prepara la defensa final del proyecto completo.
```

## Actividad HEXA guiada

### H — Hecho

El modo IA responde a un prompt seguro y bloquea uno inseguro.

### E — Explorar

Pregunta:

```text
¿Qué evidencia demuestra responsabilidad?
```

Respuestas esperadas:

```text
- bloqueo de secretos;
- aviso de validación humana;
- registro sin datos sensibles;
- riesgos documentados;
- configuración sin claves reales.
```

### X — eXplicar

Conclusión:

```text
La responsabilidad se demuestra con límites, evidencias y defensa, no con promesas.
```

### A — Aplicar

Defensa por turnos con checklist.

## Checklist docente de defensa

| Elemento | Sí | Parcial | No | Observación |
|---|---|---|---|---|
| Compila y ejecuta | | | | |
| Modo IA disponible | | | | |
| Simulación declarada o integración autorizada | | | | |
| Prompt seguro responde | | | | |
| Prompt inseguro se bloquea | | | | |
| No hay API key real | | | | |
| `.env` real no está presente | | | | |
| `.env.example` no contiene secretos | | | | |
| Registro de prompts seguro | | | | |
| Riesgos IA documentados | | | | |
| Validación humana documentada | | | | |
| Comparación Java/Python comprensible | | | | |
| Defensa individual suficiente | | | | |
| Proyecto listo para HF | | | | |

## Preguntas de defensa

```text
1. ¿Tu H7 usa simulación o integración real autorizada?
2. ¿Qué caso de uso permite el modo IA?
3. ¿Qué datos no debe recibir nunca?
4. ¿Qué hace PromptSafety?
5. ¿Qué limitaciones tiene PromptSafety?
6. ¿Qué ocurre con un prompt que contiene password o token?
7. ¿Qué contiene AiResponse?
8. ¿Por qué la respuesta debe validarse por una persona?
9. ¿Cómo registras prompts sin exponer secretos?
10. ¿Qué riesgos IA has documentado?
11. ¿Qué contiene tu configuración segura?
12. ¿Por qué `.env.example` sí y `.env` real no?
13. ¿Qué diferencia hay entre esta simulación en Java y una posible en Python?
14. ¿Qué parte puedes explicar sin ayuda de IA?
15. ¿Cómo conecta H7 con la presentación final HF?
```

## Errores frecuentes

| Error | Señal | Intervención docente |
|---|---|---|
| Defender API real sin permiso | Menciona claves o servicios | Parar y volver a simulación. |
| No bloquear prompt inseguro | Responde a password/token | Revisar PromptSafety. |
| `.env.example` con secreto | Valor real visible | Sustituir por placeholder. |
| Registro copia datos sensibles | Prompt rojo completo | Resumir sin secreto. |
| No validar respuesta | La acepta como verdad | Pedir documento de validación. |
| Simulación no declarada | Parece engaño | Añadir mensaje explícito. |

Intervención oral si la defensa se atasca:

```text
No defiendas toda la IA. Defiende esta cadena:
El usuario escribe un prompt.
PromptSafety decide si es seguro.
SimulatedAiAssistant responde o bloquea.
AiResponse guarda mensaje y nota.
La persona valida antes de aceptar.
```

Búsqueda guiada en el código:

```text
1. Busca `class PromptSafety`.
2. Busca `isSafe`.
3. Busca `class SimulatedAiAssistant`.
4. Busca `answer`.
5. Busca `class AiResponse`.
6. Busca el comando `ia`.
```

## Recuperación inmediata

Si no compila:

```text
Reducir a Main + SimulatedAiAssistant + PromptSafety con dos prompts fijos. Después reintegrar Agent.
```

Si no bloquea secretos:

```text
Añadir palabras mínimas: password, contraseña, token, api key, dni, teléfono.
```

Si no hay documentación:

```text
Completar registro de prompts, riesgos y validación con un caso seguro y uno bloqueado.
```

Si hay secreto real en ficheros:

```text
No mostrarlo públicamente. Eliminarlo, sustituir por placeholder y documentar la corrección. Si era una clave real, cambiarla fuera de la actividad.
```

Si la simulación no está clara:

```text
Añadir mensaje: “Respuesta simulada. Requiere validación humana”.
```

## Cierre de H7

Guion:

```text
H7 cierra la parte técnica de MiniJarvis con una idea clave: una IA responsable no es la que responde más, sino la que tiene límites claros, evita datos peligrosos y exige validación humana.

Ahora el proyecto está listo para HF: presentación final, demo, defensa individual, recuperación específica y plan de mejora.
```

## Criterio de éxito

```text
El alumnado entrega un H7 funcional o simulado de forma robusta, bloquea usos peligrosos y puede defender seguridad, límites, trazabilidad y validación humana.
```

---

## 5. Evaluación formativa de H7

H7 debe servir para detectar:

```text
- quién distingue simulación robusta de integración real;
- quién entiende que las credenciales son un riesgo;
- quién diseña casos de uso limitados;
- quién clasifica prompts seguros e inseguros;
- quién implementa un filtro básico y reconoce sus límites;
- quién registra prompts sin exponer datos sensibles;
- quién documenta riesgos de IA;
- quién entiende configuración segura;
- quién valida respuestas antes de aceptarlas;
- quién compara Java/Python a nivel de flujo responsable;
- quién puede defender el uso de IA sin delegar su comprensión.
```

Evidencias mínimas:

| Evidencia | Qué mirar |
|---|---|
| Código | Compila y ejecuta. |
| `PromptSafety.java` | Bloquea señales básicas de secreto/dato personal. |
| `SimulatedAiAssistant.java` | Responde de forma limitada y transparente. |
| `AiResponse.java` | Separa permitido, mensaje y nota. |
| Registro de prompts | Resume sin copiar secretos. |
| Riesgos IA | Conecta riesgo con medida. |
| Configuración segura | Prohíbe `.env` real y claves. |
| Validación humana | Explica qué se acepta y qué se rechaza. |
| Comparación Java/Python | Explica filtro, respuesta y validación. |
| Defensa | La persona entiende límites, seguridad y responsabilidad. |

---

## 6. Atención a la diversidad

### Si el alumnado se bloquea con varias clases

Reducir objetivo:

```text
Crear primero PromptSafety y probar dos strings.
Después crear SimulatedAiAssistant.
Después añadir AiResponse si el grupo ya entiende el flujo.
```

Secuencia reducida:

```text
1. Método isSafe.
2. Prompt seguro devuelve mensaje.
3. Prompt inseguro devuelve bloqueo.
4. Nota de validación humana.
```

### Si el alumnado insiste en API real

Reencuadre:

```text
Una API real necesita autorización, credenciales, coste, privacidad y configuración segura. Si eso no está controlado, la solución responsable es simulación.
```

No introducir claves reales en clase ni pedirlas por chat, documento o repositorio.

### Si el alumnado copia respuestas IA

Intervención:

```text
Pedir explicación oral con el código delante. Si no puede explicarlo, debe reescribir con palabras propias y reducir alcance.
```

### Si el alumnado no entiende validación humana

Usar checklist simple:

```text
¿Es correcta?
¿Es segura?
¿Es adecuada al nivel?
¿La entiendo?
¿La he contrastado?
```

### Si hay alumnado avanzado

Extensión permitida:

```text
Añadir categorías de riesgo o respuestas diferentes según tema, siempre sin red y sin secretos.
```

Extensiones no obligatorias:

```text
API real, streaming, embeddings, bases vectoriales, agentes autónomos, navegación web o herramientas externas.
```

---

## 7. Uso responsable de IA en H7

Usos permitidos:

```text
- pedir explicación de qué es un prompt;
- pedir ejemplos de riesgos IA;
- pedir ayuda para redactar una validación humana;
- comparar integración IA en Java y Python;
- generar preguntas de defensa, siempre revisadas.
```

Usos no permitidos:

```text
- pegar claves, tokens, contraseñas o `.env` reales;
- introducir datos personales reales;
- copiar código que no se entiende;
- afirmar que una simulación llama a una IA real;
- aceptar respuestas sin validación;
- inventar registros de prompts o pruebas no realizadas.
```

Registro mínimo de IA:

```text
Fecha:
Herramienta:
Prompt resumido:
Semáforo:
Respuesta útil:
Qué he aceptado:
Qué he rechazado:
Cómo lo he validado:
Qué entiendo ahora con mis palabras:
```

Frase docente:

```text
La IA puede ayudarte a pensar, pero H7 exige que tú pongas límites, valides y defiendas.
```

---

## 8. Criterios globales de éxito de H7

H7 está consolidado cuando:

```text
[x] El programa compila.
[x] El modo IA está disponible.
[x] La solución declara si es simulación o integración autorizada.
[x] No hay API keys reales.
[x] No hay `.env` real subido.
[x] `.env.example` no contiene secretos.
[x] Un prompt seguro recibe respuesta limitada.
[x] Un prompt inseguro se bloquea.
[x] La respuesta incluye nota de validación humana.
[x] El registro de prompts no expone secretos.
[x] Los riesgos IA están documentados.
[x] La configuración segura está documentada.
[x] La validación humana está documentada.
[x] La comparación Java ↔ Python es comprensible.
[x] El alumnado puede defender límites, seguridad y responsabilidad.
```

---

## 9. Puente hacia HF

Mensaje final al grupo:

```text
Hemos llegado al final técnico de MiniJarvis.

H1 nos dio el primer asistente. H2 añadió decisiones. H3 añadió memoria temporal. H4 organizó el código con objetos. H5 lo hizo más extensible. H6 lo hizo persistente y trazable. H7 añadió un modo IA responsable o una simulación robusta.

Ahora toca HF: preparar la presentación final, revisar evidencias, defender decisiones, recuperar lo pendiente y proponer mejoras realistas.
```

Preparación docente para la fase final:

```text
Selecciona evidencias de cada hito:
- una interacción por consola;
- una decisión técnica;
- una evidencia de pruebas;
- una evidencia de seguridad;
- una defensa individual.

Servirán para guiar la presentación final y la recuperación específica.
```
