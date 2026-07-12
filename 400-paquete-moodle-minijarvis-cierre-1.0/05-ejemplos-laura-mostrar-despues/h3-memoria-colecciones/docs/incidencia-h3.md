# Incidencia — H3

Alumno/a o equipo: Laura García Martín  
Fecha: ejemplo docente  
Estado: Resuelta

---

## Descripción

```text
Al principio el programa permitía guardar un recuerdo vacío si pulsaba Enter después de recuerda.
```

---

## Causa

```text
No comprobaba si el texto leído con scanner.nextLine().trim() estaba vacío.
```

---

## Solución

```text
Añadí if (memory.isEmpty()) para mostrar un mensaje y no guardar el recuerdo vacío.
```

---

## Verificación

```text
Probé recuerda y pulsé Enter sin escribir nada. El programa mostró No puedo guardar un recuerdo vacío y el estado seguía indicando 0 recuerdos.
```
