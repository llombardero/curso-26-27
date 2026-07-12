# Capítulo 04 — Pruebas, depuración y errores

## Hitos relacionados

```text
H2-H3
```

## Qué aprenderás

- tipos de error
- compilación
- ejecución
- lógica
- pruebas manuales
- depuración con evidencias

## 1. Punto de partida

MiniJarvis se construye por capas. Este capítulo trabaja una pieza concreta del proyecto y la conecta con evidencias reales: código, pruebas, documentación, defensa y uso responsable de IA si procede.

La regla de estudio es siempre la misma:

```text
Lee el concepto, ejecuta un ejemplo pequeño, aplícalo a MiniJarvis, documenta la evidencia y prepárate para defenderlo.
```

## 2. Conceptos básicos explicados

Programar no es escribir todo bien a la primera. Hay errores de compilación, errores de ejecución y errores de lógica. Un error de compilación impide generar `.class`. Un error de ejecución aparece mientras el programa corre. Un error de lógica permite ejecutar, pero el resultado no es el esperado.

Depurar significa investigar con método: reproducir, aislar, observar, cambiar poco y volver a probar.

## 3. Ejemplo guiado en Java

```java
public class DebugExample {
    public static void main(String[] args) {
        int memories = 0;
        memories = memories + 1;
        System.out.println("Recuerdos: " + memories);
    }
}
```

## 4. Caso práctico MiniJarvis

Elige un fallo real de tu MiniJarvis: comando que no responde, mensaje incorrecto, entrada vacía, bucle que no sale. Documenta el fallo con cuatro pasos: qué esperaba, qué ocurrió, causa probable y corrección.

Después vuelve a ejecutar la prueba.

## 5. Evidencia de Entornos de Desarrollo

Crea `docs/informe-depuracion.md`. Debe incluir mensaje de error si existe, pasos para reproducir y evidencia de corrección. No borres el aprendizaje: un error bien explicado vale como evidencia.

## 6. Errores frecuentes y cómo corregirlos

| Error | Síntoma | Corrección |
|---|---|---|
| Cambiar muchas cosas a la vez | No sabes qué arregló o rompió | Un cambio pequeño por prueba |
| No copiar el error exacto | No se puede investigar | Guardar mensaje literal |
| Probar solo el caso feliz | Casos límite fallan | Añadir entrada vacía y comando desconocido |

## 7. Preguntas de repaso

1. ¿Qué diferencia hay entre error de compilación y de lógica?
2. ¿Por qué conviene reproducir antes de corregir?
3. ¿Qué debe tener un informe de depuración?
4. ¿Por qué un error corregido puede ser evidencia?

## 8. Para tu portfolio

Copia y completa este bloque en tu portfolio:

```text
Capítulo 04: Pruebas, depuración y errores
Qué he aprendido:
Código o documento que lo demuestra:
Prueba realizada:
Error que he corregido:
Qué puedo defender oralmente:
Uso de IA, si lo hubo, y cómo lo validé:
```

## 9. Estudio paso a paso

Una buena depuración empieza con una pregunta precisa: “¿qué esperaba y qué ha ocurrido?”. Después necesitas reproducir el problema. Si no puedes repetirlo, no puedes estar seguro de haberlo corregido. Evita cambiar muchas líneas a la vez: un cambio pequeño permite saber qué efecto tuvo.

Caso de estudio: provoca voluntariamente un error de compilación quitando un punto y coma. Copia el mensaje. Corrígelo. Después provoca un error lógico: cambia un comando esperado por otro texto y observa que el programa compila pero no responde como querías. Documenta la diferencia entre ambos errores.
