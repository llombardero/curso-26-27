# H1 — Primer asistente por consola

Alumna: Laura García Martín
Equipo: Equipo Ada
Módulo principal: Programación
Módulo coordinado: Entornos de Desarrollo

---

## 1. Qué entrega este hito

Este entregable contiene una primera versión muy sencilla de un asistente por consola hecho en Java.

El asistente:

- muestra un mensaje de bienvenida;
- pide el nombre de la persona usuaria;
- guarda el nombre en una variable;
- usa una constante para el nombre del asistente;
- muestra varios mensajes por pantalla;
- está preparado en un proyecto sencillo que puede abrirse en IntelliJ.

Todavía no incluye menú, bucles, `switch`, excepciones ni comandos. Eso se trabajará en H2, cuando el hito se centre en estructuras de control y depuración.

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

## 3. Ejemplo de ejecución

```text
Hola, soy MiniJarvis.
¿Cómo te llamas? Laura
Encantada, Laura.
Este curso vamos a crear un pequeño agente IA.
Curso de inicio: 2026.
Primer objetivo: aprender la estructura básica de un programa Java.
```

---

## 4. Qué he aprendido

- Que un programa Java empieza a ejecutarse en el método `main`.
- Que puedo guardar texto en variables de tipo `String`.
- Que puedo guardar valores fijos en constantes con `final`.
- Que `Scanner` sirve para leer datos introducidos por teclado.
- Que `System.out.println` muestra información por pantalla.
- Que el código debe ser sencillo y claro antes de añadir más funcionalidades.

---

## 5. Código limpio aplicado

He intentado aplicar una primera idea de código limpio:

- nombres comprensibles: `ASSISTANT_NAME`, `COURSE_YEAR`, `userName`;
- programa corto y fácil de leer;
- sin añadir todavía funciones que no pertenecen a este hito;
- sin copiar código que no pueda explicar.

---

## 6. Uso de IA

He usado IA solo para pedir una explicación de qué es una constante en Java.

No he copiado el programa completo generado por IA. He escrito y probado el código paso a paso.

El registro está en:

```text
docs/registro-ia.md
```
