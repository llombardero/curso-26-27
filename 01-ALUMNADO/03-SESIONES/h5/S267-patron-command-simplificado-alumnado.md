# Sesión 267 — Ficha de trabajo del alumnado

## Patrón Command simplificado o decisión de no patrón

| Hoy vas a… | Debe quedar… |
|---|---|
| Relacionar un problema real del diseño de herramientas con la idea de Command y decidir si conviene usarla. | `docs/registro-patron-h5.md` con problema, alternativa simple, decisión, semejanza o diferencia respecto a Command y riesgo de sobreingeniería. |

**Tiempo previsto:** 45 minutos.  
**Hito:** H5.

## Material que necesitas

- Un ordenador por estudiante o pareja, con JDK e IntelliJ disponibles y el proyecto H5 accesible.
- Pizarra o una hoja reutilizable para comparar alternativas.
- Datos ficticios; no utilices contraseñas, tokens, claves API ni datos personales reales.

## Trabajo de hoy

1. Localiza qué problema resolvió separar las acciones en clases que implementan `Tool`.
2. Compara la solución actual con esta idea: «Command encapsula una acción como objeto».
3. Identifica qué parte del proyecto se parece a Command y qué elementos de un patrón completo no necesitas.
4. Valora una alternativa más simple y el coste de añadir más infraestructura.
5. Decide si mantienes la expresión «Command simplificado» o si descartas el patrón.
6. Registra una justificación que puedas defender con código del proyecto.

## Registro de patrón

Completa `docs/registro-patron-h5.md`:

```markdown
# Registro de patrón H5

## Problema de diseño

## Alternativa simple

## Solución actual

## ¿En qué se parece a Command?

## ¿Qué parte no necesitamos?

## Ventaja comprobable

## Riesgo de sobreingeniería

## Decisión final y justificación
```

## Evidencia mínima antes de salir

- [ ] He nombrado el problema antes que el patrón.
- [ ] He relacionado la decisión con código real del proyecto.
- [ ] He explicado una semejanza y una diferencia respecto a Command.
- [ ] He identificado un riesgo de complicar innecesariamente el diseño.
- [ ] He decidido mantener, simplificar o descartar el patrón.
- [ ] Puedo defender la decisión sin limitarme a repetir una definición.

## Seguridad y uso de IA

- Trabaja únicamente con datos ficticios.
- No escribas contraseñas, tokens, claves API ni datos personales.
- Si utilizas IA para comprender el patrón, registra qué preguntaste y contrasta la explicación con el código real.
- No copies una implementación completa de Command si no puedes justificar cada elemento.
- Los ejemplos de Laura solo se consultan después del intento propio.

## Si te bloqueas

1. Escribe qué cambio sería difícil con el diseño actual.
2. Señala la clase o método donde aparece el problema.
3. Compara una solución simple con otra más compleja.
4. Si no existe un problema concreto, justifica por qué no conviene forzar el patrón.

## Cierre

Responde sin copiar: **¿Qué problema real resuelve aquí la idea de Command y qué parte sería sobreingeniería?**

La sesión está completada cuando la evidencia existe, está vinculada al proyecto y puedes defender la decisión.
