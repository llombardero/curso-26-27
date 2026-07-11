# Defensa — H5

## ¿Qué problema tenía el código antes?

```text
Agent tenía demasiadas decisiones sobre comandos. Cada comando nuevo hacía crecer processCommand.
```

## ¿Qué refactorización hiciste?

```text
Creé una interfaz Tool y moví cada comando a una clase propia.
```

## ¿Por qué usaste o descartaste un patrón?

```text
Usé Command simplificado porque cada herramienta representa una acción ejecutable. No añadí Factory ni plugins porque sería demasiado para H5.
```

## ¿Qué evidencia hay?

```text
CourseTool demuestra que se puede añadir una herramienta nueva registrándola en registerDefaultTools().
```
