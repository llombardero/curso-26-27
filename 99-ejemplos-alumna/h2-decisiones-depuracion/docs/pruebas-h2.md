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
