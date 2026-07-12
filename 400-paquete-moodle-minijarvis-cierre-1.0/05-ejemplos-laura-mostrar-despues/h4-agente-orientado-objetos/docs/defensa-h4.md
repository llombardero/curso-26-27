# Defensa — H4

## ¿Qué responsabilidad tiene cada clase?

```text
Main arranca, Agent gestiona el flujo y Memory guarda recuerdos.
```

## ¿Qué atributos son privados?

```text
En Agent son privados name, courseYear, memory, scanner, userName y running. En Memory es privado memories.
```

## ¿Qué relación aparece en el diagrama y en el código?

```text
Agent usa Memory. En el código aparece como private final Memory memory.
```

<!-- AJUSTE-COBERTURA-CONCEPTOS-32 -->

## Respuesta de Laura — cobertura de conceptos de Programación

Relación con `32-lista-conceptos-programacion-por-tema.md`:

```text
H4 trabaja principalmente: Temas 2 y 5.
Foco de aprendizaje: orientación a objetos y separación de responsabilidades.
```

Conceptos que Laura debe saber defender en este hito:

- clase
- objeto
- atributo
- método
- constructor
- referencia
- estado
- comportamiento
- responsabilidad
- private/public
- this
- diagrama de clases
- diagrama de comportamiento
- Javadoc como ampliación
- excepción básica

Respuesta modelo de Laura:

> En H4 explico por qué Main era demasiado grande y cómo Agent y Memory reparten responsabilidades con atributos privados y métodos públicos.

Evidencia que Laura debe señalar:

- una parte concreta del código o documento donde aparezca el concepto;
- una prueba, ejecución, captura o explicación que demuestre que no lo ha copiado sin entender;
- una mejora razonable que podría hacer si tuviera más tiempo.

