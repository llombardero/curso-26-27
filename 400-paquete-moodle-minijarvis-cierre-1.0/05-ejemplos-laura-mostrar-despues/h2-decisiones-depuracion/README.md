# H2 — Agente con decisiones y depuración

Equipo o alumno/a: Laura García Martín  
Curso: 1.º DAW  
Módulos: Programación + Entornos de Desarrollo  
Fecha: ejemplo docente

---

## 1. Qué hace esta versión

MiniJarvis H2 mejora la versión H1 añadiendo un menú de comandos.

Ahora el programa:

- saluda y pide el nombre de la persona usuaria;
- mantiene el programa funcionando hasta escribir `salir`;
- reconoce comandos básicos;
- responde a comandos desconocidos;
- permite practicar decisiones, bucles, pruebas manuales y depuración.

```text
H2 convierte MiniJarvis en un agente por consola con interacción repetida, pero todavía sin memoria, ficheros, clases avanzadas ni IA real.
```

---

## 2. Comandos implementados

| Comando | Qué hace | Estado |
|---|---|---|
| `ayuda` | Muestra comandos disponibles. | Hecho |
| `saluda` | Saluda usando el nombre introducido. | Hecho |
| `estado` | Indica que MiniJarvis funciona en modo H2 sin memoria. | Hecho |
| `salir` | Termina el programa de forma controlada. | Hecho |
| comando desconocido | Muestra un mensaje de ayuda. | Hecho |

---

## 3. Cómo ejecutar

Desde IntelliJ:

```text
1. Abrir el proyecto.
2. Abrir src/Main.java.
3. Pulsar Run.
4. Escribir el nombre y después comandos.
```

Desde terminal:

```bash
javac src/Main.java
java -cp src Main
```

---

## 4. Ejemplo de ejecución

```text
Hola, soy MiniJarvis.
¿Cómo te llamas? Laura
Encantada, Laura.
Este curso vamos a crear un pequeño agente IA.
Curso de inicio: 2026.
Escribe ayuda para ver los comandos disponibles.
> ayuda
Comandos disponibles: ayuda, saluda, estado, salir
> saluda
Hola, Laura. Soy MiniJarvis.
> estado
Estoy funcionando en modo H2, con menú y sin memoria todavía.
> inventa
No entiendo ese comando. Escribe ayuda.
> salir
Hasta pronto, Laura.
```

---

## 5. Qué no incluye todavía

```text
[x] Memoria con colecciones.
[x] Ficheros.
[x] IA real.
[x] Patrones de diseño.
```

Explicación:

```text
H2 se centra en menú, bucles, decisiones, pruebas y depuración. La memoria se trabajará en H3, las clases propias en H4 y la integración IA mucho más adelante.
```

---

## 6. Documentación relacionada

```text
docs/evidencia-ejecucion-h2.md
docs/pruebas-h2.md
docs/depuracion-h2.md
docs/incidencia-h2.md
docs/comparacion-java-python-h2.md
docs/registro-ia.md
docs/defensa-h2.md
```

<!-- AJUSTE-COBERTURA-CONCEPTOS-32 -->

## Respuesta de Laura — cobertura de conceptos de Programación

Relación con `32-lista-conceptos-programacion-por-tema.md`:

```text
H2 trabaja principalmente: Temas 1 y 3.
Foco de aprendizaje: decisiones, menú, repetición y depuración.
```

Conceptos que Laura debe saber defender en este hito:

- if/else
- boolean
- comparaciones
- switch
- enhanced switch como ampliación
- while
- do-while como comparación
- for
- condición de salida
- bucle infinito
- pruebas manuales
- error de compilación
- error lógico
- eficiencia básica

Respuesta modelo de Laura:

> En H2 explico cómo mi agente decide qué hacer, cómo se mantiene funcionando en un bucle y cómo comprobé errores con pruebas concretas.

Evidencia que Laura debe señalar:

- una parte concreta del código o documento donde aparezca el concepto;
- una prueba, ejecución, captura o explicación que demuestre que no lo ha copiado sin entender;
- una mejora razonable que podría hacer si tuviera más tiempo.

