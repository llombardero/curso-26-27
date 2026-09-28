# Ejemplos de entregables H2

## Para que sirve este documento

Este documento muestra ejemplos breves de como pueden quedar las evidencias de H2.

No copies los ejemplos literalmente. Usalos como modelo de claridad. Tus entregables deben hablar de tu codigo, tus comandos, tus pruebas, tu depuracion y tus decisiones reales.

Regla principal:

> En H2 no basta con que el menu funcione una vez. Debes demostrar que se repite, decide, sale de forma controlada, gestiona errores y puede depurarse.

## 1. Ejemplo de README H2

```markdown
# MiniJarvis H2 - Agente con decisiones y depuracion

## Que hace

MiniJarvis H2 es un programa de consola que muestra comandos, lee ordenes y se repite hasta escribir `salir`.

## Comandos disponibles

- `ayuda`: muestra comandos disponibles.
- `saluda`: saluda al usuario.
- `estado`: muestra el estado actual del agente.
- `salir`: termina el programa.
- cualquier otro texto: muestra un mensaje de comando desconocido.

## Como ejecutar

1. Abrir el proyecto en IntelliJ.
2. Ejecutar `Main.java`.
3. Escribir comandos en la consola.

## Ejemplo de ejecucion

```text
Hola, soy MiniJarvis H2.
Comandos: ayuda, saluda, estado, salir
> estado
Estoy funcionando en modo H2, sin memoria todavia.
> inventa
No entiendo ese comando. Escribe ayuda.
> salir
Hasta pronto.
```

## Limites de H2

- No guarda memoria todavia.
- No usa ficheros.
- No conecta con IA real.
- No usa datos personales reales.
```

Ejemplo demasiado pobre:

```text
Hemos hecho un menu y funciona.
```

Por que no sirve:

- No dice que comandos existen.
- No muestra como se ejecuta.
- No incluye entrada y salida real.

## 2. Ejemplo de pruebas H2

```markdown
# Pruebas H2

| Caso | Entrada | Esperado | Obtenido | Resultado |
|---|---|---|---|---|
| Ayuda | `ayuda` | Muestra ayuda, saluda, estado y salir | Muestra los cuatro comandos | PASA |
| Estado | `estado` | Muestra estado H2 sin memoria | Muestra "modo H2, sin memoria todavia" | PASA |
| Desconocido | `inventa` | Mensaje de comando desconocido | "No entiendo ese comando. Escribe ayuda." | PASA |
| Salir | `salir` | Termina el bucle | Muestra despedida y termina | PASA |
```

Ejemplo demasiado pobre:

```text
He probado ayuda y salir.
```

Por que no sirve:

- No incluye salida esperada.
- No incluye salida obtenida.
- No permite comprobar si paso o fallo.

## 3. Ejemplo de depuracion H2

```markdown
# Depuracion H2

## Breakpoint usado

Linea despues de leer el comando:

```java
String command = scanner.nextLine();
```

## Variables observadas

| Variable | Valor observado | Que demuestra |
|---|---|---|
| `command` | `estado` | El texto se lee correctamente desde consola. |
| `running` | `true` | El programa debe seguir tras `estado`. |

## Conclusion

El comando `estado` entra en la rama correcta y no cambia `running`, por eso el menu vuelve a aparecer.
```

Ejemplo demasiado pobre:

```text
Puse un breakpoint.
```

Por que no sirve:

- No dice donde.
- No indica variables.
- No explica que se aprendio.

## 4. Ejemplo de incidencia H2

```markdown
# Incidencia H2

## Sintoma

Al escribir `salir`, el programa mostraba "Hasta pronto", pero volvia a mostrar `>`.

## Como reproducir

1. Ejecutar `Main.java`.
2. Escribir `salir`.
3. Observar que el programa no termina.

## Esperado

El programa debe terminar.

## Obtenido

El programa sigue dentro del bucle.

## Causa

La rama `salir` imprimia el mensaje, pero no cambiaba `running` a `false`.

## Correccion

```java
} else if (command.equals("salir")) {
    running = false;
    System.out.println("Hasta pronto.");
}
```

## Verificacion

Tras corregirlo, ejecute `estado` y despues `salir`. El programa mostro despedida y termino.
```

## 5. Ejemplo de comparacion Java-Python H2

```markdown
# Comparacion Java-Python H2

## Idea comparada

Repetir el menu hasta escribir `salir`.

## Java

```java
boolean running = true;
while (running) {
    String command = scanner.nextLine();
    if (command.equals("salir")) {
        running = false;
    }
}
```

## Python

```python
running = True
while running:
    command = input("> ")
    if command == "salir":
        running = False
```

## Diferencias que entiendo

- Java declara el tipo de `running`; Python no lo escribe explicitamente.
- Java usa `scanner.nextLine()` para leer; Python usa `input()`.
- Java compara texto con `.equals()`; Python puede usar `==` para esta comparacion.
```

## 6. Ejemplo de defensa H2

```markdown
# Defensa H2

## Pregunta: donde se repite el programa?

Se repite dentro del `while (running)`. Mientras `running` vale `true`, el programa vuelve a mostrar el prompt y lee otro comando.

## Pregunta: como termina?

Termina cuando el comando es `salir`, porque esa rama cambia `running` a `false`.

## Pregunta: que prueba demuestra el comando desconocido?

La prueba `inventa` demuestra que el ultimo `else` responde con un mensaje controlado en lugar de quedarse sin salida.

## Pregunta: que depuraste?

Puse un breakpoint despues de leer `command` y observe que al escribir `estado`, `command` tenia valor `estado` y `running` seguia en `true`.
```

## 7. Checklist H2 antes de entregar

```text
[ ] El programa se ejecuta.
[ ] El menu se repite.
[ ] Existe ayuda.
[ ] Existe saluda.
[ ] Existe estado.
[ ] Existe salir.
[ ] Hay comando desconocido controlado.
[ ] Hay pruebas con esperado y obtenido.
[ ] Hay depuracion con breakpoint.
[ ] Hay incidencia documentada.
[ ] Hay comparacion Java-Python.
[ ] Hay README actualizado.
[ ] Hay registro IA si procede.
[ ] Puedo defender mi parte sin leer una respuesta generica.
```
