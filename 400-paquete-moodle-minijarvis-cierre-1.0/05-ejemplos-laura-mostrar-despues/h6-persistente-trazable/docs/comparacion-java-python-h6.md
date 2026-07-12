# Comparación Java ↔ Python — H6

## Java

```java
Files.write(filePath, memories, StandardOpenOption.CREATE, StandardOpenOption.TRUNCATE_EXISTING);
```

## Python

```python
with open("data/recuerdos.txt", "w", encoding="utf-8") as file:
    for memory in memories:
        file.write(memory + "
")
```

## Diferencias

```text
Java usa Path, Files y StandardOpenOption. Python usa open con un bloque with. En ambos casos hay que decidir ruta, formato y seguridad de los datos.
```

<!-- AJUSTE-COBERTURA-CONCEPTOS-32 -->

## Respuesta de Laura — cobertura de conceptos de Programación

Relación con `32-lista-conceptos-programacion-por-tema.md`:

```text
H6 trabaja principalmente: Temas 5, 6 y puente hacia Tema 8.
Foco de aprendizaje: persistencia, logs, errores y trazabilidad.
```

Conceptos que Laura debe saber defender en este hito:

- clases responsables
- excepciones checked y runtime
- throws
- validación
- invariantes
- repositorio como idea inicial
- ficheros
- logs
- seguridad
- Repository como patrón opcional
- pruebas de dos ejecuciones
- trazabilidad

Respuesta modelo de Laura:

> En H6 explico cómo demuestro persistencia cerrando y abriendo el programa, y por qué los logs no deben guardar secretos ni datos personales.

Evidencia que Laura debe señalar:

- una parte concreta del código o documento donde aparezca el concepto;
- una prueba, ejecución, captura o explicación que demuestre que no lo ha copiado sin entender;
- una mejora razonable que podría hacer si tuviera más tiempo.

