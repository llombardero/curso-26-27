# H1 — Primer asistente por consola

Alumna: Laura García Martín
Equipo: Equipo Ada
Módulo principal: Programación
Módulo coordinado: Entornos de Desarrollo

---

## 1. Qué entrega este hito

Este entregable contiene un primer asistente por consola hecho en Java.

El asistente:

- muestra un mensaje de bienvenida;
- pide el nombre de la persona usuaria;
- acepta comandos básicos;
- responde con reglas simples;
- permite salir del programa;
- está preparado en un proyecto sencillo que puede abrirse en IntelliJ.

---

## 2. Cómo ejecutar

Desde terminal:

```bash
javac src/Main.java
java -cp src Main
```

Desde IntelliJ:

1. Abrir la carpeta del proyecto.
2. Revisar que el SDK de Java está configurado.
3. Abrir `src/Main.java`.
4. Pulsar Run.

---

## 3. Comandos disponibles

| Comando | Respuesta |
|---|---|
| `ayuda` | Muestra comandos disponibles. |
| `saluda` | Saluda usando el nombre introducido. |
| `estado` | Indica que el asistente está funcionando. |
| `java` | Explica de forma sencilla qué es Java. |
| `salir` | Termina el programa. |

---

## 4. Ejemplo de ejecución

```text
Hola, soy MiniJarvis.
¿Cómo te llamas? Laura
Encantada, Laura. Escribe 'ayuda' para ver comandos.
> ayuda
Comandos disponibles: ayuda, saluda, estado, java, salir
> saluda
Hola Laura, estoy aprendiendo a ayudarte.
> java
Java es el lenguaje principal que estamos usando para construir este agente.
> salir
Hasta luego, Laura.
```

---

## 5. Qué he aprendido

- Que un programa Java empieza a ejecutarse en el método `main`.
- Que puedo guardar texto en variables de tipo `String`.
- Que `Scanner` sirve para leer datos introducidos por teclado.
- Que un bucle `while` puede mantener vivo el programa hasta que se escriba `salir`.
- Que `switch` permite responder de forma distinta según el comando.

---

## 6. Uso de IA

He usado IA solo para pedir una explicación de la diferencia entre `if` y `switch`.

No he copiado el programa completo generado por IA. He escrito y probado el código paso a paso.

El registro está en:

```text
docs/registro-ia.md
```
