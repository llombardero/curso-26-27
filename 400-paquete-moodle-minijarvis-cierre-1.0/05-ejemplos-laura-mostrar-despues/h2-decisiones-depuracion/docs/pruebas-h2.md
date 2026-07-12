# Plan de pruebas — H2

Equipo: Equipo Ada  
Alumna: Laura García Martín  
Fecha: ejemplo docente  
Producto probado: MiniJarvis H2

---

## 1. Objetivo

Comprobar que el menú, los comandos y la salida controlada funcionan correctamente.

---

## 2. Casos de prueba

| ID | Caso | Entrada / acción | Resultado esperado | Resultado obtenido | Estado |
|---|---|---|---|---|---|
| P01 | Mostrar ayuda | `ayuda` | Lista comandos | Muestra `ayuda, saluda, estado, salir` | Correcto |
| P02 | Saludar | `saluda` | Saludo personalizado | Muestra `Hola, Laura. Soy MiniJarvis.` | Correcto |
| P03 | Estado | `estado` | Estado del agente | Indica modo H2 sin memoria | Correcto |
| P04 | Comando desconocido | `xyz` | Mensaje controlado | Muestra `No entiendo ese comando. Escribe ayuda.` | Correcto |
| P05 | Salir | `salir` | Termina programa | Muestra despedida y termina | Correcto |

---

## 3. Casos límite

| Caso límite | Qué puede pasar | Cómo lo comprobamos |
|---|---|---|
| Mayúsculas | No reconoce comando | Probé `AYUDA`; funciona porque uso `toLowerCase()`. |
| Espacios antes/después | No reconoce comando | Probé ` ayuda `; funciona porque uso `trim()`. |
| Entrada vacía | Mensaje desconocido | Pulsé Enter sin comando y mostró mensaje controlado. |

---

## 4. Conclusión

```text
El producto está listo para demo H2 porque reconoce los comandos mínimos, gestiona entradas desconocidas y termina correctamente con salir.
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

