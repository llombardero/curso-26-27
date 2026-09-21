# Guía básica de Drive para MiniJarvis

Esta guía sirve para empezar desde cero. Si ya sabes usar Drive, úsala como lista de comprobación.

## 1. Para qué usaremos Drive

Drive no es el lugar principal del código. En MiniJarvis lo usaremos para guardar y localizar evidencias que no son código:

- capturas de ejecución;
- documentos de acuerdos o decisiones;
- exportaciones en PDF o XLSX;
- evidencias de trabajo en equipo;
- enlaces a Sheets, Sites o GitHub cuando el profesorado lo indique.

El código vive en GitHub desde H1. Drive no debe convertirse en una segunda copia editable del proyecto.

## 2. Entrar en Drive

1. Abre el navegador.
2. Entra en `https://drive.google.com`.
3. Inicia sesión con la cuenta indicada por el profesorado.
4. Comprueba que estás en la cuenta correcta antes de crear o subir nada.

Si tienes varias cuentas abiertas, revisa el icono de perfil de la esquina superior derecha.

## 3. Localizar la carpeta del curso

El profesorado compartirá una carpeta del curso. Su nombre será parecido a:

```text
PROGRAMACION_1DAW_MINIJARVIS_2026_2027
```

Dentro encontrarás una estructura parecida a esta:

```text
01_RECURSOS_COMUNES/
02_EQUIPOS/
  EQUIPO_01/
  EQUIPO_02/
  ...
03_ENLACES_Y_PLANTILLAS/
```

Entra solo en la carpeta de tu equipo. No necesitas acceder a carpetas de otros equipos.

## 4. Estructura de tu equipo

Tu carpeta de equipo tendrá subcarpetas por hito:

```text
EQUIPO_XX/
├── 00_ENLACES/
├── 01_SCRUM/
├── H0/
├── H1/
├── H2/
├── H3/
├── H4/
├── H5/
├── H6/
├── H7/
└── HF/
```

Regla práctica:

```text
Cada evidencia se guarda en la carpeta del hito al que pertenece.
```

Ejemplos:

- Evidencias de la torre de papel: `H0/`.
- Captura de ejecución del primer asistente: `H1/`.
- Exportación de una retrospectiva de H3: `H3/`.
- Evidencias finales: `HF/`.

## 5. Crear carpetas o archivos

Si el profesorado pide crear una carpeta:

1. Entra en la carpeta de tu equipo.
2. Entra en el hito correspondiente.
3. Pulsa `Nuevo`.
4. Elige `Carpeta` o el tipo de archivo que corresponda.
5. Usa un nombre claro.

Nombres recomendados:

```text
H1-evidencia-ejecucion-equipo-03.pdf
H2-pruebas-manuales-equipo-03.xlsx
H3-retrospectiva-equipo-03.pdf
```

Evita nombres como:

```text
documento nuevo
captura final final buena
sin titulo
trabajo terminado
```

## 6. Subir una evidencia

1. Entra en la carpeta correcta del hito.
2. Pulsa `Nuevo`.
3. Elige `Subir archivo`.
4. Selecciona el archivo de tu ordenador.
5. Espera a que termine la subida.
6. Abre el archivo una vez para comprobar que se ve bien.

Antes de subir una captura, revisa que no muestre contraseñas, datos personales, tokens, claves API ni información privada de otras personas.

## 7. Enlaces profundos

Un enlace profundo apunta al archivo, pestaña o página concreta que quieres que se corrija.

No es lo mismo entregar:

```text
Enlace general a toda la carpeta del equipo
```

que entregar:

```text
Enlace directo a la evidencia de H1 que quiero que se revise
```

Para copiar un enlace:

1. Abre el archivo o carpeta concreta.
2. Pulsa `Compartir` o `Copiar enlace`.
3. Pega el enlace en Moodle o en la plantilla de entrega.
4. Comprueba que el enlace apunta a lo que quieres entregar.

## 8. Permisos

La regla general del curso es:

```text
Acceso general: Restringido
```

No cambies permisos sin indicación del profesorado. No uses `Cualquier usuario con el enlace` salvo que el profesorado lo autorice expresamente.

Antes de entregar, comprueba:

- el profesorado puede abrir el enlace;
- tus compañeros de equipo pueden abrir lo que deben abrir;
- otros equipos no tienen acceso;
- el enlace no muestra datos privados;
- el archivo está en la carpeta correcta.

## 9. Qué no debe estar en Drive

No subas a Drive:

- contraseñas;
- tokens;
- claves API;
- archivos `.env` reales;
- datos personales innecesarios;
- calificaciones;
- resultados HADA de otras personas;
- incidencias privadas;
- copias completas del código si ya está en GitHub.

## 10. Checklist antes de entregar en Moodle

- [ ] Estoy usando la cuenta correcta.
- [ ] La evidencia está en la carpeta de mi equipo.
- [ ] La evidencia está en la carpeta del hito correcto.
- [ ] El nombre del archivo se entiende.
- [ ] El enlace abre el archivo concreto, no una carpeta genérica.
- [ ] El acceso general sigue restringido.
- [ ] No se ven datos personales ni secretos.
- [ ] Puedo explicar qué demuestra esta evidencia.
