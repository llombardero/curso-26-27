# Plan de pruebas — H2

Equipo:
Fecha:
Producto probado: MiniJarvis H2

---

## 1. Objetivo

Comprobar que el menú, los comandos y la salida controlada funcionan correctamente.

---

## 2. Casos de prueba

| ID | Caso | Entrada / acción | Resultado esperado | Resultado obtenido | Estado |
|---|---|---|---|---|---|
| P01 | Mostrar ayuda | `ayuda` | Lista comandos | | Correcto / Error |
| P02 | Saludar | `saluda` | Saludo personalizado | | Correcto / Error |
| P03 | Estado | `estado` | Estado del agente | | Correcto / Error |
| P04 | Comando desconocido | `xyz` | Mensaje controlado | | Correcto / Error |
| P05 | Salir | `salir` | Termina programa | | Correcto / Error |

---

## 3. Casos límite

| Caso límite | Qué puede pasar | Cómo lo comprobamos |
|---|---|---|
| Mayúsculas | No reconoce comando | |
| Espacios antes/después | No reconoce comando | |
| Entrada vacía | Mensaje desconocido | |

---

## 4. Conclusión

```text

```
