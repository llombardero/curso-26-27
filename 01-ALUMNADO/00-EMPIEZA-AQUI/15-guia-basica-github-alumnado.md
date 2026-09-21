# Guía básica de GitHub para MiniJarvis

Esta guía sirve para empezar desde cero. GitHub puede parecer difícil al principio, pero en MiniJarvis lo usaremos de forma progresiva.

## 1. Para qué usaremos GitHub

GitHub será el lugar principal del código desde H1.

Lo usaremos para:

- guardar el código del proyecto;
- conservar el historial de cambios;
- escribir el `README`;
- identificar qué versión se entrega;
- revisar trabajo del equipo;
- demostrar evolución y trazabilidad.

Drive no sustituye a GitHub para el código.

## 2. Vocabulario mínimo

Repositorio:

```text
Carpeta del proyecto en GitHub.
```

Commit:

```text
Foto guardada de un cambio concreto.
```

README:

```text
Archivo que explica qué es el proyecto, cómo se ejecuta y qué contiene.
```

Issue:

```text
Tarea, error o mejora registrada.
```

Branch o rama:

```text
Línea de trabajo separada para desarrollar algo sin romper la versión principal.
```

Pull request:

```text
Propuesta para revisar e incorporar cambios de una rama.
```

Tag:

```text
Marca estable para identificar una versión entregada.
```

## 3. Crear una cuenta o iniciar sesión

1. Entra en `https://github.com`.
2. Inicia sesión o crea una cuenta si el profesorado lo autoriza.
3. Usa un correo y nombre de usuario adecuados para clase.
4. Activa la verificación que GitHub pida.
5. No compartas tu contraseña con nadie.

Si ya tienes cuenta, revisa que puedes entrar antes de H1.

## 4. Crear o recibir el repositorio

El profesorado indicará si el repositorio lo crea el equipo o si se entrega ya preparado.

Si tienes que crearlo:

1. Pulsa `New repository`.
2. Escribe un nombre claro.
3. Usa un nombre parecido a:

```text
minijarvis-equipo-03
```

4. Elige la visibilidad indicada por el profesorado.
5. Añade un `README` si el profesorado lo pide.
6. Crea el repositorio.
7. Copia la URL y guárdala donde indique el equipo.

No crees repositorios con nombres ofensivos, datos personales o información privada.

## 5. Estructura inicial recomendada

Al principio la estructura será pequeña. Puede crecer así:

```text
minijarvis-equipo-03/
├── README
├── src/
│   └── Main.java
└── docs/
    ├── pruebas
    ├── registro-ia
    └── portfolio
```

No hace falta crear todas las carpetas el primer día. Cada hito indicará qué hace falta.

## 6. Qué debe explicar el README

El `README` debe permitir que otra persona entienda el proyecto.

Contenido mínimo:

1. Nombre del proyecto.
2. Equipo o autores, según indique el profesorado.
3. Hito actual.
4. Qué hace el programa.
5. Cómo se ejecuta.
6. Qué se ha probado.
7. Qué falta o qué limitaciones tiene.
8. Versión entregada.

Ejemplo corto:

```text
# MiniJarvis Equipo 03

Hito: H1

MiniJarvis saluda al usuario, pide su nombre y muestra mensajes por consola.

Para ejecutar:
1. Abrir el proyecto en IntelliJ.
2. Ejecutar Main.java.

Pruebas realizadas:
- Nombre normal.
- Nombre vacío.
- Ejecución repetida.
```

## 7. Subir cambios desde la web de GitHub

En los primeros pasos, si el profesorado lo permite, puedes usar la web de GitHub.

Para crear o modificar un archivo:

1. Abre el repositorio.
2. Pulsa `Add file` o abre el archivo que quieres editar.
3. Escribe o pega el contenido.
4. Baja hasta `Commit changes`.
5. Escribe un mensaje claro.
6. Confirma el cambio.

Mensajes de commit recomendados:

```text
Añade primer saludo de MiniJarvis
Documenta ejecución de H1
Corrige mensaje cuando el nombre está vacío
```

Mensajes poco útiles:

```text
cambios
final
arreglo
aaa
```

## 8. Subir cambios desde IntelliJ o Git

Cuando el profesorado lo indique, trabajarás con Git desde el entorno de desarrollo.

La idea básica siempre es la misma:

1. Cambiar archivos.
2. Revisar qué ha cambiado.
3. Hacer commit con mensaje claro.
4. Subir los cambios a GitHub.

No memorices comandos sin entender qué guardan. Lo importante es que puedas explicar qué cambio hiciste y por qué.

## 9. Identificar la versión entregada

Desde H1, cada entrega debe apuntar a una versión concreta.

Puede ser:

- un commit concreto;
- un tag como `h1-entrega`;
- una release si el profesorado lo pide.

Si entregas solo el enlace general del repositorio, puede cambiar después y no quedar claro qué versión se corrige.

## 10. Qué no debe subirse a GitHub

Nunca subas:

- contraseñas;
- tokens;
- claves API;
- archivos `.env` reales;
- datos personales;
- capturas con cuentas abiertas;
- trabajos completos de otros equipos;
- soluciones copiadas que no puedes defender.

Si subes un secreto por error, avisa al profesorado. No intentes ocultarlo con más commits.

## 11. Relación entre GitHub, Drive y Moodle

GitHub:

```text
Código, README, historial y versión evaluada.
```

Drive:

```text
Evidencias no-code, exportaciones y documentos de apoyo.
```

Moodle:

```text
Entrega oficial, fecha, rúbrica y feedback.
```

En Moodle normalmente entregarás enlaces, no todo el contenido copiado.

## 12. Checklist antes de entregar en Moodle

- [ ] El repositorio correcto está enlazado.
- [ ] El código está actualizado.
- [ ] El `README` explica cómo ejecutar el proyecto.
- [ ] La versión entregada está identificada con commit o tag.
- [ ] No hay contraseñas, tokens ni `.env` reales.
- [ ] El equipo sabe qué ha cambiado.
- [ ] Cada persona puede defender su aportación.
- [ ] Los enlaces funcionan con una cuenta autorizada.
