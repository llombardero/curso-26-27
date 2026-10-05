# Introducción a Git y GitHub

## Programación — 1.º DAW

> **Reconocimiento de autoría y fuente principal**
>
> Este manual ha sido elaborado tomando como **fuente didáctica principal** el curso en vídeo **«Aprende Git y GitHub - Curso desde Cero»**, creado por **Estefania Cassingena Navone** y publicado por **freeCodeCamp Español**.
>
> Vídeo original:
>
> <https://www.youtube.com/watch?v=mBYSUUnMt9M>
>
> La progresión conceptual y numerosos ejemplos generales de Git y GitHub de este manual se apoyan en dicho curso.
>
> El contenido se ha reorganizado, resumido, adaptado y ampliado para su utilización en **Programación de 1.º DAW** y para aplicarlo al proyecto **MiniJarvis**.
>
> Las secciones específicas sobre MiniJarvis, organización de evidencias, seguridad del proyecto, `.gitignore`, identificación de versiones evaluadas y determinadas recomendaciones para el trabajo en el aula son **adaptaciones didácticas de este módulo** y no deben atribuirse necesariamente al curso original.
>
> Este manual no pretende sustituir al vídeo original. El vídeo constituye una fuente de estudio recomendada y reconocida expresamente en este material.

---

# 1. Para qué sirve este manual

Durante el curso vas a modificar MiniJarvis muchas veces.

Necesitamos poder responder preguntas como:

```text
¿Qué he cambiado?

¿Qué versión funcionaba?

¿Qué cambió entre dos versiones?

¿Quién realizó un cambio?

¿Puedo probar algo sin destruir la versión estable?

¿Cómo compartimos cambios?

¿Qué versión concreta estamos evaluando?
```

Git y GitHub nos ayudarán a responderlas.

Pero no necesitas aprender todo de una vez.

Este manual está organizado en tres niveles.

## Núcleo

Debes ir dominando progresivamente:

```text
repositorio
status
diff
add
commit
log
ramas
push
pull
```

## Trabajo colaborativo

Cuando el proyecto lo necesite aparecerán:

```text
merge
conflictos
remotos
fetch
pull requests
```

## Ampliación

No necesitas dominar desde el principio:

```text
forks
issues
operaciones avanzadas
recuperación compleja del historial
```

La regla es la misma que utilizamos en MiniJarvis:

> Primero comprende. Después utiliza.

---

# 2. El problema: trabajar sin control de versiones

Imagina que durante varias semanas guardas:

```text
Main.java
Main-bueno.java
Main-final.java
Main-final2.java
Main-final-ahora-si.java
Main-final-definitivo.java
```

Muy pronto aparecen problemas:

```text
¿Cuál es la versión correcta?

¿Qué diferencia hay entre ellas?

¿Qué archivo funcionaba ayer?

¿Quién hizo este cambio?

¿Puedo recuperar una versión anterior?
```

Copiar archivos manualmente no proporciona un historial fiable.

Para eso utilizamos un **sistema de control de versiones**.

---

# 3. ¿Qué es el control de versiones?

Un sistema de control de versiones permite conservar la evolución de un proyecto.

En lugar de guardar:

```text
versión1
versión2
versión3
versión-final
```

podemos conservar una historia:

```text
A
↓
B
↓
C
↓
D
```

Cada punto representa un estado significativo del proyecto.

Podemos saber:

- qué cambió;
- cuándo cambió;
- quién registró el cambio;
- qué existía antes;
- cómo ha evolucionado el proyecto.

---

# 4. ¿Qué es Git?

**Git** es un sistema de control de versiones.

Git puede trabajar en tu propio ordenador.

Permite:

- detectar cambios;
- seleccionar cambios;
- registrar versiones;
- consultar el historial;
- comparar estados;
- crear ramas;
- combinar trabajo;
- colaborar con otras personas.

Puedes utilizar Git sin utilizar GitHub.

Esta idea es fundamental:

```text
Git ≠ GitHub
```

---

# 5. ¿Qué es GitHub?

**GitHub** es un servicio que permite alojar repositorios Git y colaborar alrededor de ellos.

Podemos simplificar así:

```text
Git
│
├── controla versiones
├── crea commits
├── mantiene historial
└── gestiona ramas

GitHub
│
├── aloja repositorios Git
├── facilita colaboración
├── permite pull requests
├── permite issues
└── permite compartir el proyecto
```

Git trabaja con el repositorio.

GitHub puede alojar una copia remota de ese repositorio.

---

# 6. Git y GitHub: ejemplo

En tu ordenador:

```text
/mis-proyectos/minijarvis/
```

puedes tener un:

```text
REPOSITORIO LOCAL
```

En GitHub puede existir:

```text
REPOSITORIO REMOTO
```

Ambos pueden estar relacionados:

```text
TU ORDENADOR
repositorio local
      │
      │ Internet
      ▼
GITHUB
repositorio remoto
```

Un commit no se sube automáticamente a GitHub.

Primero se crea localmente.

---

# 7. Vocabulario fundamental

Antes de utilizar comandos debemos comprender algunas palabras.

---

## 7.1. Repositorio

Un **repositorio** es un proyecto cuyo historial está gestionado mediante Git.

Puede ser:

```text
local
```

o:

```text
remoto
```

---

## 7.2. Directorio de trabajo

Es donde están los archivos que estás editando.

Por ejemplo:

```text
minijarvis/
├── README.md
└── src/
    └── Main.java
```

Cuando modificas `Main.java`, estás modificando tu directorio de trabajo.

---

## 7.3. Área de preparación o staging

Git permite seleccionar qué cambios formarán parte del próximo commit.

Ese espacio se denomina:

```text
staging area
```

o:

```text
área de preparación
```

Puedes imaginarlo como una bandeja.

```text
ARCHIVOS MODIFICADOS
       │
       │ git add
       ▼
STAGING
cambios seleccionados
       │
       │ git commit
       ▼
HISTORIAL
```

---

## 7.4. Commit

Un **commit** registra un estado significativo del proyecto.

Ejemplos:

```text
Añade saludo inicial de MiniJarvis

Lee el nombre mediante Scanner

Corrige cálculo del objetivo semanal

Documenta ejecución de H1
```

Un commit debe ayudar a comprender la evolución del proyecto.

---

## 7.5. Rama

Una **rama** o *branch* representa una línea de desarrollo.

Permite trabajar sin modificar inmediatamente otra línea del proyecto.

Ejemplo:

```text
A---B---C  main
     \
      D---E  mejora-saludo
```

---

## 7.6. Merge

Un **merge** combina trabajo de distintas ramas.

---

## 7.7. Conflicto

Un conflicto aparece cuando Git no puede decidir automáticamente cómo combinar algunos cambios.

No significa que Git esté roto.

Significa:

```text
hay cambios incompatibles
        ↓
una persona debe revisar
        ↓
decidir el resultado correcto
```

---

## 7.8. Repositorio remoto

Es un repositorio accesible mediante una ubicación remota.

En este curso puede estar alojado en GitHub.

---

## 7.9. Clone

**Clonar** significa obtener una copia local de un repositorio existente.

---

## 7.10. Push

`push` envía commits locales al repositorio remoto.

---

## 7.11. Pull

`pull` obtiene cambios del remoto e intenta incorporarlos a tu trabajo local.

---

## 7.12. Fetch

`fetch` obtiene información del remoto sin integrarla automáticamente en tu rama actual.

---

## 7.13. Fork

Un **fork** crea en GitHub una copia de otro repositorio bajo otro espacio.

No es lo mismo que clonar.

```text
fork
→ copia en GitHub

clone
→ copia en tu ordenador
```

---

## 7.14. Pull request

Un **pull request** es una propuesta para revisar e incorporar cambios.

No confundas:

```text
git pull
```

con:

```text
pull request
```

Son conceptos diferentes.

---

## 7.15. Issue

Un **issue** permite registrar y discutir:

- errores;
- tareas;
- propuestas;
- preguntas;
- mejoras.

En MiniJarvis ya utilizamos Scrum para organizar el trabajo del equipo.

Por eso no duplicaremos automáticamente cada tarea de Scrum como un issue.

---

# 8. Las tres áreas fundamentales de Git

Este esquema es especialmente importante:

```text
DIRECTORIO DE TRABAJO
archivos que modificas
          │
          │ git add
          ▼
STAGING AREA
cambios seleccionados
          │
          │ git commit
          ▼
REPOSITORIO LOCAL
historial de commits
```

Si además existe un remoto:

```text
REPOSITORIO LOCAL
       │
       │ git push
       ▼
REPOSITORIO REMOTO
       GitHub
```

Recuerda:

```text
editar ≠ add ≠ commit ≠ push
```

---

# 9. Comprobar que Git está disponible

En una terminal:

```bash
git --version
```

Debería aparecer una versión de Git.

La instalación y configuración concreta dependerán de los equipos utilizados en el aula.

Sigue las indicaciones del profesorado cuando sea necesario instalar o configurar herramientas.

---

# 10. Terminal: cuatro comandos útiles

Antes de utilizar Git debes saber dónde estás.

## Directorio actual

```bash
pwd
```

## Ver archivos

```bash
ls
```

## Entrar en una carpeta

```bash
cd nombre-carpeta
```

Ejemplo:

```bash
cd minijarvis
```

## Subir un nivel

```bash
cd ..
```

Muchos errores con Git empiezan porque estamos trabajando en una carpeta distinta de la que creemos.

---

# 11. Configurar identidad

Git asocia cada commit con una identidad.

Ejemplo:

```bash
git config --global user.name "Nombre Apellidos"
```

```bash
git config --global user.email "correo@example.com"
```

Puedes consultar:

```bash
git config --global --list
```

Utiliza la identidad que corresponda según las indicaciones del aula y de la cuenta utilizada.

No compartas contraseñas, tokens ni credenciales.

---

# 12. Crear un repositorio

Supongamos que tenemos:

```text
minijarvis/
├── README.md
└── src/
    └── Main.java
```

Entramos:

```bash
cd minijarvis
```

Si todavía no es un repositorio Git y la actividad indica que debemos crearlo:

```bash
git init
```

A partir de ese momento Git puede empezar a seguir la evolución del proyecto.

No ejecutes `git init` dentro de otro repositorio sin comprender qué estás haciendo.

---

# 13. El comando más importante para empezar: `git status`

Ejecuta:

```bash
git status
```

Git puede informarte sobre:

- rama actual;
- archivos nuevos;
- archivos modificados;
- cambios preparados;
- cambios no preparados;
- estado respecto al remoto.

Cuando algo no esté claro:

```text
Primera pregunta:

¿Qué dice git status?
```

No intentes arreglar el problema antes de leer el estado.

---

# 14. Primer ejemplo con MiniJarvis

Supongamos:

```java
public class Main {
    public static void main(String[] args) {
        System.out.println("Hola, soy MiniJarvis.");
    }
}
```

Ejecuta:

```bash
git status
```

Si `Main.java` aparece como archivo nuevo o modificado, Git ha detectado el cambio.

---

# 15. Preparar un cambio con `git add`

Para preparar únicamente `Main.java`:

```bash
git add src/Main.java
```

Ahora:

```bash
git status
```

debería mostrar el cambio preparado.

Pero todavía no existe un nuevo commit.

---

# 16. `git add` no significa hacer commit

Este recorrido debe quedar claro:

```text
MODIFICO UN ARCHIVO
       ↓
git add
       ↓
PREPARO EL CAMBIO
       ↓
git commit
       ↓
REGISTRO UNA VERSIÓN
```

Mientras estás aprendiendo, es preferible seleccionar conscientemente los archivos.

Ejemplo:

```bash
git add src/Main.java
```

o:

```bash
git add README.md
```

Antes de preparar muchos archivos a la vez, comprueba qué cambios existen.

---

# 17. Crear un commit

Una vez preparado el cambio:

```bash
git commit -m "Añade saludo inicial de MiniJarvis"
```

El commit queda registrado en el repositorio local.

Todavía no significa que se haya enviado a GitHub.

---

# 18. Mensajes de commit

Evita:

```text
cambios

cosas

final

prueba

ahora funciona
```

Prefiere:

```text
Añade saludo inicial

Lee nombre mediante Scanner

Corrige conversión de horas

Actualiza instrucciones de ejecución

Mejora nombres de variables
```

Un buen mensaje ayuda a reconstruir la evolución.

---

# 19. Consultar el historial

Puedes usar:

```bash
git log
```

Una vista más breve:

```bash
git log --oneline
```

Ejemplo:

```text
c142e5a Documenta ejecución de H1
a39e172 Añade cálculo de horas
ff82190 Lee nombre mediante Scanner
81245aa Añade saludo inicial
```

Cada commit tiene un identificador.

---

# 20. Revisar qué has cambiado

## Cambios todavía no preparados

```bash
git diff
```

Esto permite revisar diferencias antes de hacer `git add`.

## Cambios ya preparados

```bash
git diff --staged
```

Pregunta:

```text
¿Es esto realmente lo que quiero incluir
en el próximo commit?
```

---

# 21. Flujo básico recomendable

Antes de un commit:

```text
modifico
   ↓
ejecuto
   ↓
compruebo
   ↓
git status
   ↓
git diff
   ↓
git add archivo
   ↓
git status
   ↓
git diff --staged
   ↓
git commit
```

No necesitas ejecutar mecánicamente todos los comandos en todas las situaciones.

Lo importante es comprender el estado antes de registrar cambios.

---

# 22. Ramas

Un proyecto puede tener varias líneas de trabajo.

Comprueba las ramas:

```bash
git branch
```

La actual aparece marcada.

También puedes consultar:

```bash
git branch --show-current
```

---

# 23. Crear una rama

En este manual utilizaremos:

```bash
git switch -c mejora-saludo
```

Eso crea la rama y cambia a ella.

Puedes comprobar:

```bash
git branch --show-current
```

Resultado esperado:

```text
mejora-saludo
```

> En otros materiales, incluido el aprendizaje tradicional de Git, puedes encontrar `git checkout` para operaciones relacionadas con ramas. No memorices comandos alternativos sin comprender primero qué operación estás realizando.

---

# 24. Ejemplo de trabajo en una rama

Creamos:

```bash
git switch -c mejora-saludo
```

Modificamos:

```java
System.out.println("Bienvenido a MiniJarvis.");
```

Comprobamos el programa.

Después:

```bash
git status
```

```bash
git diff
```

```bash
git add src/Main.java
```

```bash
git commit -m "Mejora mensaje de bienvenida"
```

Ahora ese commit pertenece a la rama:

```text
mejora-saludo
```

---

# 25. Cambiar de rama

Para ir a una rama existente:

```bash
git switch nombre-rama
```

Por ejemplo, si la rama principal de tu repositorio se llama `main`:

```bash
git switch main
```

No todos los repositorios utilizan necesariamente el mismo nombre para su rama principal.

Antes de cambiar de rama puedes consultar cuáles existen:

```bash
git branch
```

La rama actual aparecerá marcada.

También puedes consultar directamente su nombre:

```bash
git branch --show-current
```

Antes de cambiar de rama comprueba el estado:

```bash
git status
```

No cambies de rama a ciegas si tienes modificaciones que todavía no has revisado.

---

# 26. Comprender las ramas gráficamente

Ejemplo:

```text
A---B---C  main
     \
      D---E  mejora-saludo
```

Ambas ramas comparten:

```text
A
B
```

Después evolucionaron de manera diferente.

---

# 27. Fusionar ramas

Para fusionar dos ramas debes saber primero:

```text
qué rama contiene el cambio

qué rama debe recibirlo
```

Debes situarte en la rama que **recibirá** los cambios.

Por ejemplo, supongamos que:

```text
main
→ debe recibir la mejora

mejora-saludo
→ contiene la mejora
```

Primero comprobamos las ramas:

```bash
git branch
```

Si la rama principal de este repositorio se llama `main`, cambiamos a ella:

```bash
git switch main
```

Comprobamos:

```bash
git branch --show-current
```

y después incorporamos los cambios de `mejora-saludo`:

```bash
git merge mejora-saludo
```

La idea puede representarse así:

```text
mejora-saludo
      │
      │ git merge mejora-saludo
      ▼
rama actual
```

Por tanto:

> `git merge otra-rama` incorpora en la rama actual los cambios de `otra-rama`.

No hagas un `merge` sin saber qué rama está activa y cuál contiene los cambios que quieres incorporar.

---

# 28. Conflictos

Imagina que dos ramas modifican la misma línea.

Rama A:

```java
System.out.println("Bienvenido a MiniJarvis.");
```

Rama B:

```java
System.out.println("MiniJarvis está preparado.");
```

Git puede no saber automáticamente cuál de los dos cambios debe conservar.

Puede mostrar marcas como:

```text
 <<<<<<< HEAD
Bienvenido a MiniJarvis.
 =======
MiniJarvis está preparado.
 >>>>>>> otra-rama
```

Estas marcas indican las dos versiones que Git no ha podido combinar por sí solo.

No deben quedarse dentro del programa terminado.

## Paso 1. Consultar el estado

Empieza por:

```bash
git status
```

Git indicará qué archivos tienen conflictos.

## Paso 2. Revisar el archivo

Debes leer las alternativas y decidir cuál debe ser el resultado final.

Por ejemplo, podrías decidir conservar:

```java
System.out.println("Bienvenido a MiniJarvis.");
```

o escribir una tercera solución:

```java
System.out.println("Bienvenido. MiniJarvis está preparado.");
```

La decisión no la toma Git por ti.

## Paso 3. Eliminar las marcas del conflicto

Debes eliminar del archivo:

```text
 <<<<<<<
 =======
 >>>>>>>
```

y dejar únicamente el contenido correcto.

## Paso 4. Ejecutar y comprobar

En MiniJarvis no basta con que desaparezcan las marcas.

Debes comprobar que el programa sigue siendo correcto.

```text
compilar
   ↓
ejecutar
   ↓
comprobar resultado
```

## Paso 5. Marcar el archivo como resuelto

Cuando el archivo ya contiene el resultado correcto:

```bash
git add src/Main.java
```

Aquí `git add` indica a Git que has revisado ese archivo y que esa es la versión que quieres conservar para continuar la resolución.

## Paso 6. Volver a comprobar

```bash
git status
```

Si quedan más conflictos, deben resolverse antes de continuar.

## Paso 7. Finalizar el merge

Si el conflicto apareció durante un `merge`, cuando todos los archivos estén resueltos Git permitirá terminar la operación.

Una forma habitual es:

```bash
git merge --continue
```

Git puede solicitar completar o confirmar el mensaje correspondiente al merge.

Al terminar, vuelve a comprobar:

```bash
git status
```

El proceso completo puede resumirse así:

```text
aparece conflicto
       ↓
git status
       ↓
leer ambas versiones
       ↓
decidir
       ↓
editar
       ↓
eliminar marcas
       ↓
compilar y ejecutar
       ↓
git add archivo
       ↓
git status
       ↓
git merge --continue
       ↓
git status
```

Resolver un conflicto no consiste en aceptar automáticamente una versión.

Consiste en comprender los cambios y decidir cuál debe ser el resultado correcto.

---

# 29. Antes de intentar arreglar Git

Si aparece un problema:

```bash
git status
```

después:

```bash
git branch --show-current
```

y:

```bash
git log --oneline --decorate -10
```

Si hay cambios:

```bash
git diff
```

Primero recoge información.

Después decide.

---

# 30. GitHub: repositorio remoto

Cuando existe un proyecto en GitHub tenemos:

```text
REPOSITORIO LOCAL
en tu ordenador

        ↕

REPOSITORIO REMOTO
en GitHub
```

El remoto permite compartir commits.

---

# 31. Clonar un repositorio

Si el proyecto ya existe en GitHub, normalmente se obtiene mediante:

```bash
git clone URL_DEL_REPOSITORIO
```

Después:

```bash
cd nombre-del-repositorio
```

y:

```bash
git status
```

Un repositorio clonado ya conserva información sobre su remoto.

---

# 32. `origin` y la conexión con un remoto

Consulta los remotos configurados:

```bash
git remote -v
```

Es frecuente encontrar:

```text
origin
```

`origin` es el nombre habitual que recibe el remoto principal cuando clonamos un repositorio.

No significa:

```text
GitHub
```

GitHub es el servicio.

`origin` es simplemente un nombre utilizado por Git para identificar un repositorio remoto.

Por ejemplo, conceptualmente:

```text
origin
   ↓
https://github.com/organizacion/minijarvis.git
```

## Si has utilizado `git clone`

Cuando haces:

```bash
git clone URL_DEL_REPOSITORIO
```

Git configura normalmente el remoto `origin` de forma automática.

Puedes comprobarlo:

```bash
git remote -v
```

Por tanto, normalmente no necesitas volver a añadirlo.

## Si has creado primero el repositorio local

La situación es diferente si has empezado en tu ordenador:

```bash
mkdir minijarvis
cd minijarvis
git init
```

En ese caso puedes tener un repositorio Git local pero todavía ningún repositorio remoto asociado.

Comprueba:

```bash
git remote -v
```

Si no aparece ningún remoto y la actividad indica que debes conectarlo con un repositorio de GitHub ya creado, una operación habitual es:

```bash
git remote add origin URL_DEL_REPOSITORIO
```

Después comprueba:

```bash
git remote -v
```

Podrías obtener algo parecido a:

```text
origin  URL_DEL_REPOSITORIO (fetch)
origin  URL_DEL_REPOSITORIO (push)
```

Esto indica que Git conoce un remoto llamado `origin`.

## Comprobar antes de modificar un remoto

No ejecutes `git remote add origin ...` sin comprobar antes:

```bash
git remote -v
```

Si `origin` ya existe, intentar añadir otro con el mismo nombre producirá un error.

Tampoco cambies ni elimines un remoto sin comprender para qué se está utilizando.

## Local y remoto siguen siendo cosas distintas

Aunque estén conectados:

```text
REPOSITORIO LOCAL
       │
       │ origin
       ▼
REPOSITORIO REMOTO
```

siguen siendo dos repositorios.

Por eso:

```text
git commit
→ modifica el historial local
```

mientras:

```text
git push
→ comparte commits con el remoto
```

---

# 33. `git push`

Después de crear commits:

```bash
git push
```

envía al remoto los commits que correspondan.

Recuerda:

```text
git commit
→ registra localmente

git push
→ envía al remoto
```

---

# 34. Primera publicación de una rama

Una rama nueva puede no tener todavía una rama remota asociada.

Git puede indicar algo parecido a:

```text
The current branch has no upstream branch
```

Una operación habitual es:

```bash
git push -u origin nombre-rama
```

Por ejemplo:

```bash
git push -u origin mejora-saludo
```

Antes comprueba:

```bash
git branch --show-current
```

No copies comandos de error sin entender los nombres que contienen.

---

# 35. `git pull`

Si el remoto tiene cambios que tu copia local todavía no incorpora:

```bash
git pull
```

puede obtenerlos e intentar incorporarlos.

Antes de hacerlo:

```bash
git status
```

Es importante saber si tienes trabajo local pendiente.

---

# 36. `git fetch`

`fetch` y `pull` no son exactamente lo mismo.

Simplificando:

```text
git fetch
→ consulta y descarga información
  sobre el remoto
  sin incorporar automáticamente
  esos cambios a tu rama actual
```

mientras:

```text
git pull
→ obtiene cambios
  e intenta incorporarlos
```

`fetch` puede ser útil cuando quieres observar antes de integrar.

---

# 37. Flujo sencillo con GitHub

Un flujo orientativo:

```text
git status
     ↓
actualizo si corresponde
     ↓
modifico
     ↓
ejecuto y compruebo
     ↓
git diff
     ↓
git add
     ↓
git commit
     ↓
git push
```

No existe una única secuencia válida para todas las situaciones.

Debes comprender qué estado tiene el repositorio.

---

# 38. Ejemplo completo con MiniJarvis

## Antes

```java
public class Main {
    public static void main(String[] args) {
        System.out.println("Hola.");
    }
}
```

### 1. Comprueba

```bash
git status
```

### 2. Modifica

```java
public class Main {
    public static void main(String[] args) {
        System.out.println("Hola, soy MiniJarvis.");
    }
}
```

### 3. Ejecuta el programa

Comprueba que el resultado es el esperado.

### 4. Revisa

```bash
git diff
```

### 5. Prepara

```bash
git add src/Main.java
```

### 6. Vuelve a comprobar

```bash
git status
```

### 7. Crea el commit

```bash
git commit -m "Presenta MiniJarvis por consola"
```

### 8. Consulta el historial

```bash
git log --oneline
```

### 9. Cuando corresponda

```bash
git push
```

Debes poder explicar qué ha hecho cada paso.

---

# 39. Pull requests

GitHub permite proponer la incorporación de cambios mediante un **pull request**.

Un flujo posible:

```text
crear rama
    ↓
modificar
    ↓
comprobar
    ↓
commit
    ↓
push
    ↓
pull request
    ↓
revisión
    ↓
incorporación
```

Un pull request permite revisar cambios antes de fusionarlos.

No todos los cambios de MiniJarvis requieren obligatoriamente un pull request.

Se utilizará cuando el flujo de trabajo del curso lo necesite.

---

# 40. Forks

Un fork crea otra copia del repositorio dentro de GitHub.

Es frecuente cuando quieres colaborar con un proyecto sobre el que no trabajas directamente.

```text
repositorio original
       ↓
      fork
       ↓
copia en tu GitHub
       ↓
     clone
       ↓
tu ordenador
```

En MiniJarvis no debes crear forks por rutina.

Utilízalos cuando la actividad lo requiera.

---

# 41. Issues

Un issue puede representar:

```text
error
mejora
tarea
pregunta
propuesta
```

Ejemplo:

```text
Título:
El cálculo de horas muestra un resultado incorrecto

Esperado:
Entrada 4 → resultado 5

Observado:
Entrada 4 → resultado 4
```

Pero MiniJarvis utiliza Scrum para organizar el trabajo del equipo.

No copies automáticamente todas las tareas de Scrum a GitHub Issues.

Una herramienta debe resolver un problema, no duplicar otra.

---

# 42. Adaptación MiniJarvis — `.gitignore`

Esta sección es una **ampliación específica del manual para MiniJarvis**.

Hay archivos que no deben entrar en el repositorio.

Git permite indicar patrones mediante:

```text
.gitignore
```

Ejemplo:

```text
.env
*.key
*.token
```

La configuración concreta dependerá del proyecto.

`.gitignore` ayuda a evitar que determinados archivos se añadan accidentalmente.

Pero:

> `.gitignore` no convierte un secreto publicado en seguro.

La mejor protección es:

```text
no subir nunca el secreto
```

---

# 43. Seguridad

Nunca subas a GitHub:

- contraseñas;
- claves API;
- tokens;
- credenciales;
- `.env` con valores reales;
- datos personales innecesarios;
- ficheros privados;
- información sensible de otras personas.

Tampoco pegues secretos en una IA.

Utiliza datos ficticios para ejemplos y pruebas.

---

# 44. Adaptación MiniJarvis — identificar la versión evaluada

En un hito debemos poder responder:

```text
¿Qué versión exacta se está evaluando?
```

Un commit permite identificar un estado concreto.

Consulta:

```bash
git log --oneline
```

Ejemplo:

```text
4a81bc2 Prepara H1 para defensa
```

`4a81bc2` identifica ese commit.

---

# 45. Tags

Un **tag** permite asignar un nombre a un punto del historial.

Por ejemplo:

```bash
git tag h1-entrega
```

Comprueba:

```bash
git tag
```

Puedes inspeccionarlo:

```bash
git show h1-entrega
```

Si la entrega requiere publicar también ese tag:

```bash
git push origin h1-entrega
```

No crees tags de entrega por rutina.

Utiliza el mecanismo indicado para cada hito.

En H1 consulta:

```text
ENTREGA-DIGITAL.md
```

La versión evaluada puede identificarse mediante el mecanismo allí establecido.

---

# 46. Qué pertenece al repositorio MiniJarvis

GitHub no es el lugar donde debemos copiar todas las evidencias.

El repositorio conserva principalmente:

- código;
- historial;
- versiones;
- README;
- pruebas técnicas cuando formen parte del proyecto;
- otros recursos técnicos cuando sean necesarios.

No necesitas crear por defecto:

```text
docs/
├── portfolio
├── registro-ia
├── diario
├── defensa
└── capturas
```

solo para duplicar información.

---

# 47. Fuentes canónicas de MiniJarvis

| Información | Fuente habitual |
|---|---|
| Código y versiones | Repositorio |
| Ejecución y documentación técnica necesaria | README |
| Tareas, decisiones y bloqueos significativos | Scrum |
| Aprendizaje individual significativo | Diario |
| Uso significativo de IA | Diario o Scrum según autoría |
| Selección periódica de evidencias | Site en los cierres establecidos |
| Evidencia no-code excepcional | Espacio previsto cuando no exista una fuente mejor |
| Versión evaluada | Entrega Moodle |
| Defensa | Producto real |

Si la información ya existe y puede comprobarse, no la copies a otro lugar únicamente para volver a entregarla.

---

# 48. README y Git

El README forma parte del repositorio.

Su función no es reproducir Scrum ni el diario.

Debe contener información técnica útil para comprender el proyecto.

Según el hito puede explicar:

- qué hace;
- cómo ejecutarlo;
- cómo comprobarlo;
- limitaciones;
- decisiones técnicas necesarias.

Por ejemplo:

```markdown
# H1 — Primer asistente por consola

## Qué hace

MiniJarvis pide información sencilla y muestra resultados.

## Cómo ejecutar

Abrir el proyecto y ejecutar Main.

## Comprobación

Introducir datos ficticios y observar el resultado.

## Límites

Esta versión todavía no incorpora menú, bucles ni IA real.
```

---

# 49. Errores frecuentes

## `not a git repository`

Probablemente Git no encuentra un repositorio en la ubicación actual.

Comprueba:

```bash
pwd
```

```bash
ls
```

y asegúrate de estar en la carpeta adecuada.

---

## `nothing to commit`

Git no encuentra un nuevo cambio preparado para registrar.

Consulta:

```bash
git status
```

No modifiques algo artificialmente solo para producir otro commit.

---

## Rama sin upstream

Antes de actuar:

```bash
git branch --show-current
```

Git puede sugerir una operación como:

```bash
git push -u origin nombre-rama
```

Comprueba siempre que los nombres son los que esperas.

---

## `push` rechazado

No utilices inmediatamente un envío forzado.

Primero:

```bash
git status
```

```bash
git branch --show-current
```

y comprueba si el remoto contiene trabajo que tu copia no tiene.

---

## Conflicto

Ejecuta:

```bash
git status
```

Localiza exactamente qué archivos están afectados.

Lee los cambios.

Decide cuál debe ser el resultado.

Después comprueba el programa.

---

## Rama equivocada

Antes de continuar creando más cambios:

```bash
git status
```

```bash
git branch --show-current
```

```bash
git log --oneline --decorate -10
```

Comprende primero dónde están tus cambios.

---

# 50. Comandos con los que debes tener especial cuidado

No utilices sin saber exactamente qué efecto tendrán operaciones capaces de eliminar trabajo o reescribir historia.

Por ejemplo:

```text
git reset --hard
git clean -fd
git push --force
```

Si aparece un problema, empieza por herramientas de observación:

```bash
git status
git diff
git log
git branch --show-current
```

Primero:

```text
observar
```

después:

```text
comprender
```

y finalmente:

```text
actuar
```

---

# 51. Recuperar cambios: introducción

Esta es una **ampliación didáctica**.

Si has modificado un archivo y quieres descartar una modificación local concreta, Git dispone de herramientas de restauración.

Pero antes de utilizar cualquier operación de recuperación:

```bash
git status
```

y:

```bash
git diff
```

Debes saber qué vas a perder.

La recuperación del historial puede ser sencilla o muy delicada según el estado del repositorio.

Si tienes dudas, conserva el estado y pide ayuda antes de ejecutar comandos destructivos.

---

# 52. Práctica 1 — Primer commit

Partiendo de MiniJarvis:

1. consulta:

```bash
git status
```

2. modifica un mensaje de `Main.java`;

3. ejecuta el programa;

4. revisa:

```bash
git diff
```

5. prepara:

```bash
git add src/Main.java
```

6. comprueba:

```bash
git status
```

7. crea:

```bash
git commit -m "Mejora mensaje inicial"
```

8. consulta:

```bash
git log --oneline
```

Debes poder explicar qué ocurrió en cada paso.

---

# 53. Práctica 2 — Tres commits con sentido

Realiza tres cambios independientes.

Por ejemplo:

```text
Commit 1
Añade presentación de MiniJarvis

Commit 2
Añade lectura del nombre

Commit 3
Documenta cómo ejecutar
```

Después:

```bash
git log --oneline
```

Compara ese historial con un único commit llamado:

```text
muchos cambios
```

¿Cuál permite comprender mejor la evolución?

---

# 54. Práctica 3 — Rama de prueba

1. comprueba la rama actual;

2. crea:

```bash
git switch -c prueba-mensaje
```

3. cambia un mensaje;

4. ejecuta;

5. crea un commit;

6. consulta el historial;

7. vuelve a la rama anterior;

8. observa la diferencia.

El objetivo no es crear muchas ramas.

El objetivo es comprender qué problema resuelven.

---

# 55. Práctica 4 — Trabajo colaborativo

Actividad guiada:

```text
Persona A
→ modifica
→ comprueba
→ commit
→ push

Persona B
→ obtiene cambios
→ localiza el nuevo commit
→ ejecuta
→ comprueba
```

Después intercambiad los papeles.

Pregunta:

```text
¿Qué operaciones pertenecen a Git?

¿Qué parte necesita el repositorio remoto?
```

---

# 56. Práctica 5 — Leer el historial de MiniJarvis

Ejecuta:

```bash
git log --oneline
```

Elige tres commits.

Para cada uno intenta explicar:

```text
¿Qué cambió?

¿Por qué tenía sentido registrarlo?

¿Podría localizar esa versión?

¿El mensaje permite entender la intención?
```

---

# 57. Chuleta básica

## Estado

```bash
git status
```

## Diferencias sin preparar

```bash
git diff
```

## Diferencias preparadas

```bash
git diff --staged
```

## Preparar archivo

```bash
git add archivo
```

## Crear commit

```bash
git commit -m "Mensaje"
```

## Historial breve

```bash
git log --oneline
```

## Ramas

```bash
git branch
```

## Rama actual

```bash
git branch --show-current
```

## Crear y cambiar a rama

```bash
git switch -c nombre-rama
```

## Cambiar de rama

```bash
git switch nombre-rama
```

## Fusionar

```bash
git merge nombre-rama
```

## Remotos

```bash
git remote -v
```

## Clonar

```bash
git clone URL
```

## Enviar

```bash
git push
```

## Asociar primera publicación de una rama

```bash
git push -u origin nombre-rama
```

## Incorporar cambios

```bash
git pull
```

## Consultar cambios remotos

```bash
git fetch
```

## Tags

```bash
git tag
```

---

# 58. El flujo que debes comprender

```text
MODIFICO
   ↓
EJECUTO
   ↓
COMPRUEBO
   ↓
git status
   ↓
git diff
   ↓
git add
   ↓
git status
   ↓
git commit
   ↓
git log
   ↓
git push
cuando corresponda
```

No lo memorices como una receta automática.

Cada comando responde a una pregunta distinta.

---

# 59. Qué debes poder explicar

Al terminar esta introducción debes poder responder progresivamente:

1. ¿qué problema resuelve un sistema de control de versiones?
2. ¿qué es Git?
3. ¿qué es GitHub?
4. ¿por qué Git y GitHub no son lo mismo?
5. ¿qué es un repositorio?
6. ¿qué es el directorio de trabajo?
7. ¿qué es staging?
8. ¿qué hace `git add`?
9. ¿qué es un commit?
10. ¿qué diferencia hay entre commit y push?
11. ¿para qué sirve `git status`?
12. ¿qué permite observar `git diff`?
13. ¿qué muestra `git log`?
14. ¿qué es una rama?
15. ¿para qué sirve un merge?
16. ¿qué es un conflicto?
17. ¿qué es un repositorio remoto?
18. ¿qué significa clonar?
19. ¿qué hace push?
20. ¿qué hace pull?
21. ¿qué diferencia básica hay entre pull y fetch?
22. ¿qué es un pull request?
23. ¿qué diferencia hay entre fork y clone?
24. ¿qué puede representar un issue?
25. ¿qué utilidad puede tener un tag?
26. ¿por qué no deben aparecer secretos en Git?
27. ¿qué información de MiniJarvis pertenece al repositorio?
28. ¿cómo localizarías una versión evaluada?

---

# 60. Qué no necesitas aprender de memoria

No necesitas memorizar todos los comandos.

Debes aprender a razonar:

```text
¿Qué quiero hacer?

¿Dónde estoy?

¿En qué rama estoy?

¿Qué dice git status?

¿Qué ha cambiado?

¿Qué quiero conservar?

¿Qué quiero compartir?

¿Qué efecto tendrá el comando?
```

Aprender Git no consiste en lanzar comandos hasta que desaparezca el error.

Consiste en comprender el estado del repositorio.

---

# 61. Relación con MiniJarvis

Git acompañará la evolución del programa:

```text
H1
primera versión Java
        ↓
nuevos hitos
        ↓
nuevas capacidades
        ↓
versiones estables
        ↓
producto final
```

El historial debe ayudarnos a comprender esa evolución.

No necesitamos registrar cada pulsación de teclado.

Necesitamos conservar cambios significativos.

---

# 62. Idea clave

```text
Git conserva la historia.

GitHub permite compartirla.

status informa.

diff compara.

add prepara.

commit registra.

branch separa líneas de trabajo.

merge combina.

push envía.

pull incorpora.

fetch consulta el remoto.

README explica el proyecto.

El historial permite reconstruir su evolución.
```

Cuando algo no esté claro:

```bash
git status
```

Lee primero.

Decide después.

---

# 63. Reconocimiento y fuente principal

Este manual ha sido elaborado utilizando como **fuente didáctica principal**:

**«Aprende Git y GitHub - Curso desde Cero»**

**Autora del curso:** Estefania Cassingena Navone
**Publicado por:** freeCodeCamp Español
**Plataforma:** YouTube
**Vídeo:** <https://www.youtube.com/watch?v=mBYSUUnMt9M>

El curso original desarrolla progresivamente contenidos como:

```text
introducción a Git y GitHub
        ↓
conceptos básicos
        ↓
instalación y configuración
        ↓
repositorios
        ↓
tres áreas de Git
        ↓
status
        ↓
commits
        ↓
ramas
        ↓
merge
        ↓
conflictos
        ↓
GitHub
        ↓
clone
        ↓
push
        ↓
pull y fetch
        ↓
forks
        ↓
pull requests
        ↓
issues
```

Esta progresión se ha utilizado como base para estructurar una parte importante del presente manual.

El material original ha sido transformado didácticamente para:

- adaptarlo al nivel de 1.º DAW;
- utilizar ejemplos próximos al alumnado;
- relacionarlo con programas Java;
- aplicarlo al proyecto MiniJarvis;
- separar contenidos nucleares de contenidos que pueden introducirse posteriormente;
- incorporar prácticas de aula;
- integrar el trabajo con las fuentes canónicas de evidencias del módulo;
- incorporar recomendaciones específicas de seguridad;
- relacionar Git con la identificación de versiones evaluadas.

Las secciones específicas sobre:

```text
MiniJarvis
fuentes canónicas
Moodle
diario
Scrum
Site
seguridad del proyecto
.gitignore
tags de entrega
identificación de versiones evaluadas
```

son adaptaciones propias del diseño didáctico del módulo y no deben interpretarse como contenido atribuido necesariamente al vídeo original.

El reconocimiento de la fuente significa también que este manual **no pretende sustituir el curso original**.

El vídeo puede utilizarse como recurso complementario para ver demostraciones más extensas y estudiar Git y GitHub con mayor profundidad.

La relación entre ambos materiales puede resumirse así:

```text
FUENTE PRINCIPAL

Curso de Estefania Cassingena Navone
publicado por freeCodeCamp Español
             ↓
       estudio y análisis
             ↓
ADAPTACIÓN DIDÁCTICA

Introducción a Git y GitHub
Programación — 1.º DAW
Proyecto MiniJarvis
```
