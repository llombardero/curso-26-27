# Defensa — H6

## ¿Dónde se guarda la información?

```text
Los recuerdos se guardan en data/recuerdos.txt y el historial en logs/historial.log.
```

## ¿Qué ocurre si el fichero no existe?

```text
PersistentMemory crea la carpeta y el fichero si no existen.
```

## ¿Cómo sé que persiste?

```text
Guardo un recuerdo, cierro el programa, lo ejecuto de nuevo y aparece al consultar memoria.
```

<!-- AJUSTE-COBERTURA-CONCEPTOS-32 -->

## Respuesta de Laura — cobertura de conceptos de Programación

Relación con `32-lista-conceptos-programacion-por-tema.md`:

```text
H6 trabaja principalmente: Temas 5, 6 y puente hacia Tema 8.
Foco de aprendizaje: persistencia, logs, errores, invariantes, excepciones y trazabilidad.
```

Conceptos que Laura debe saber defender en este hito:

- clases responsables: `PersistentMemory`, `HistoryLog` o equivalentes;
- excepciones checked y runtime;
- diferencia entre lanzar, capturar y declarar con `throws`;
- excepción propia de persistencia si el equipo la implementa, o justificación si usa una estándar;
- validación de entradas e invariantes de `Memory`;
- no exponer una lista interna modificable;
- ficheros, rutas relativas y creación de carpetas;
- logs técnicos sin secretos ni datos personales reales;
- Repository como idea inicial u opción de mejora;
- prueba de dos ejecuciones para demostrar persistencia;
- trazabilidad mediante pruebas, incidencia y README reproducible.

Respuesta modelo de Laura:

> En H6 explico cómo demuestro persistencia cerrando y abriendo el programa. También puedo defender qué ocurre cuando falla un fichero: sé distinguir entre una excepción que se lanza, una que se captura y una que se declara con `throws`. Si usamos una excepción propia como `MemoryStorageException`, explico qué error del dominio representa; si no la usamos, justifico por qué una excepción estándar era suficiente para nuestro nivel.

Evidencia que Laura debe señalar:

- código o pseudocódigo de carga/guardado con `Path`/`Files` o equivalente;
- prueba con dos ejecuciones: guardar, cerrar, abrir y consultar;
- documento de seguridad indicando qué no debe entrar en logs;
- incidencia H6 o prueba de error controlado de fichero;
- explicación de un invariante: por ejemplo, no guardar recuerdos vacíos ni permitir modificar la memoria interna desde fuera.

Pregunta de defensa aconsejada:

> Si falla la lectura de `data/recuerdos.txt`, ¿qué ve la persona usuaria, qué se registra y qué excepción se lanza o captura?

