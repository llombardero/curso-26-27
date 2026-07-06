# Portfolio individual — H1

Alumna: Laura García Martín
Equipo: Equipo Ada

---

## Qué he hecho

He creado un primer asistente por consola llamado MiniJarvis.

El programa pregunta mi nombre y después permite escribir comandos. Según el comando, responde con un mensaje distinto.

---

## Partes importantes del código

- `Scanner`: lo uso para leer lo que escribe la persona usuaria.
- `String userName`: guarda el nombre.
- `boolean running`: controla si el programa sigue funcionando.
- `while`: repite el menú hasta que se escribe `salir`.
- `switch`: decide qué respuesta dar según el comando.
- `final String ASSISTANT_NAME`: constante con el nombre del asistente.

---

## Problema que tuve

Al principio escribí `Salir` con mayúscula y el programa no salía.

Lo solucioné usando:

```java
String command = scanner.nextLine().trim().toLowerCase();
```

Así el comando se convierte a minúsculas y también se quitan espacios al principio o al final.

---

## Qué puedo mejorar

- Separar algunas respuestas en métodos.
- Añadir más comandos.
- Guardar un historial de comandos en el siguiente hito.
- Hacer pruebas más ordenadas en una tabla.

---

## Preguntas que sé responder

1. ¿Dónde empieza el programa?
   - En `public static void main(String[] args)`.

2. ¿Para qué sirve el bucle `while`?
   - Para que el asistente siga preguntando comandos hasta que el usuario escriba `salir`.

3. ¿Qué ocurre si escribo un comando desconocido?
   - Entra en `default` y muestra un mensaje de ayuda.

4. ¿Qué parte me ayudó a entender la IA?
   - La diferencia entre `if` y `switch`, pero el código lo adapté y lo probé yo.
