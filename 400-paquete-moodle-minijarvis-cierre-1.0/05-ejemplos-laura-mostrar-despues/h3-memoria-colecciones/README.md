# H3 — Agente con memoria en colecciones

Alumno/a o equipo: Laura García Martín  
Fecha: ejemplo docente

---

## 1. Qué añade H3

MiniJarvis H3 añade memoria temporal usando una colección Java.

Ahora el agente puede:

- guardar recuerdos durante la ejecución;
- consultar los recuerdos guardados;
- indicar cuántos recuerdos hay;
- gestionar memoria vacía;
- evitar guardar recuerdos vacíos.

---

## 2. Colección usada

Colección:

```text
ArrayList<String>
```

Motivo breve:

```text
Uso ArrayList porque quiero guardar una lista ordenada de recuerdos y mostrarlos en el mismo orden en que se han añadido.
```

---

## 3. Comandos de memoria

| Comando | Qué hace | Estado |
|---|---|---|
| `recuerda` | Pide un texto y lo guarda en memoria. | Hecho |
| `memoria` | Muestra los recuerdos guardados. | Hecho |
| `estado` | Indica cuántos recuerdos hay. | Hecho |

---

## 4. Cómo ejecutar

```bash
javac src/Main.java
java -cp src Main
```

---

## 5. Ejemplo de ejecución

```text
Hola, soy MiniJarvis.
¿Cómo te llamas? Laura
Encantada, Laura.
Curso de inicio: 2026.
Escribe ayuda para ver los comandos disponibles.
> memoria
No tengo recuerdos todavía.
> recuerda
¿Qué quieres que recuerde? Traer pendrive
He guardado: Traer pendrive
> estado
Tengo 1 recuerdo(s) en memoria temporal.
> memoria
Recuerdos guardados:
1. Traer pendrive
> salir
Hasta pronto, Laura.
```

<!-- AJUSTE-COBERTURA-CONCEPTOS-32 -->

## Respuesta de Laura — cobertura de conceptos de Programación

Relación con `32-lista-conceptos-programacion-por-tema.md`:

```text
H3 trabaja principalmente: Tema 4.
Foco de aprendizaje: memoria temporal con estructuras de datos.
```

Conceptos que Laura debe saber defender en este hito:

- colección
- genéricos
- List
- ArrayList
- índice
- recorrido
- for mejorado
- mutabilidad
- inmutabilidad
- clases envoltorio
- array
- tabla como ampliación
- Set para evitar repetidos
- Map para preferencias por clave

Respuesta modelo de Laura:

> En H3 defiendo por qué usé una lista para guardar recuerdos y qué cambiaría si necesitara evitar repetidos o buscar por clave.

Evidencia que Laura debe señalar:

- una parte concreta del código o documento donde aparezca el concepto;
- una prueba, ejecución, captura o explicación que demuestre que no lo ha copiado sin entender;
- una mejora razonable que podría hacer si tuviera más tiempo.

