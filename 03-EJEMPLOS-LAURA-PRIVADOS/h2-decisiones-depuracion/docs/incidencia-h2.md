# Incidencia — H2

Alumno/a o equipo: Laura García Martín  
Fecha: ejemplo docente  
Estado: Resuelta

---

## 1. Descripción

```text
El comando ayuda no funcionaba cuando escribía AYUDA en mayúsculas o con espacios alrededor.
```

---

## 2. Pasos para reproducir

1. Ejecutar el programa.
2. Escribir el nombre Laura.
3. Escribir ` AYUDA ` o `AYUDA`.

---

## 3. Resultado esperado

```text
El programa debería reconocer el comando ayuda aunque tenga mayúsculas o espacios simples alrededor.
```

---

## 4. Resultado obtenido

```text
Antes de corregirlo, el programa respondía: No entiendo ese comando. Escribe ayuda.
```

---

## 5. Causa probable

```text
El programa comparaba exactamente el texto escrito. Si el usuario escribía AYUDA o espacios, el texto no coincidía con ayuda.
```

---

## 6. Solución aplicada

```text
Cambié la lectura del comando a scanner.nextLine().trim().toLowerCase();
```

---

## 7. Verificación

```text
Probé ayuda, AYUDA y ayuda con espacios. Después de la corrección, el programa reconoció el comando.
```

---

## 8. Uso de IA, si procede

```text
Usé IA para entender la diferencia entre equals, trim y toLowerCase, pero adapté el cambio y lo probé manualmente.
```
