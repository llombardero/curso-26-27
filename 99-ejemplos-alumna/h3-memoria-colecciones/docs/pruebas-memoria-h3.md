# Pruebas de memoria — H3

Equipo: Equipo Ada  
Alumna: Laura García Martín  
Fecha: ejemplo docente

---

## Casos de prueba

| ID | Caso | Entrada | Esperado | Obtenido | Estado |
|---|---|---|---|---|---|
| M01 | Memoria vacía | `memoria` | Aviso de vacío | `No tengo recuerdos todavía.` | Correcto |
| M02 | Guardar recuerdo | `recuerda` + `Traer pendrive` | Guarda texto | `He guardado: Traer pendrive` | Correcto |
| M03 | Mostrar memoria | `memoria` | Lista recuerdos | Muestra lista numerada | Correcto |
| M04 | Estado | `estado` | Número recuerdos | `Tengo 1 recuerdo(s)` | Correcto |
| M05 | Entrada vacía | `recuerda` + vacío | No guarda vacío | `No puedo guardar un recuerdo vacío.` | Correcto |
