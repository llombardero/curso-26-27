# Capítulo 06 — Programación orientada a objetos

## Hitos relacionados

```text
H4
```

## Qué aprenderás

- clase
- objeto
- atributo
- método
- constructor
- sobrecarga de constructores
- this
- responsabilidad
- Main pequeño
- Javadoc mínimo

## 1. Punto de partida

MiniJarvis se construye por capas. Este capítulo trabaja una pieza concreta del proyecto y la conecta con evidencias reales: código, pruebas, documentación, defensa y uso responsable de IA si procede.

La regla de estudio es siempre la misma:

```text
Lee el concepto, ejecuta un ejemplo pequeño, aplícalo a MiniJarvis, documenta la evidencia y prepárate para defenderlo.
```

## 2. Conceptos básicos explicados

La programación orientada a objetos organiza el código en clases con responsabilidades. Una clase es un molde. Un objeto es una instancia creada a partir de ese molde. Un atributo guarda estado. Un método representa comportamiento. Un constructor prepara el objeto al nacer.

H4 aparece cuando `Main` empieza a hacerlo todo. La solución no es crear clases decorativas, sino separar responsabilidades reales.

Una clase puede tener varios constructores si hay varias formas razonables de crear objetos. Esto se llama sobrecarga de constructores. `this` permite referirse al objeto actual y distinguir atributos de parámetros. Además, las clases públicas deben poder documentarse: Javadoc ayuda a explicar qué hace una clase o método sin leer toda su implementación.

## 3. Ejemplo guiado en Java

```java
public class Agent {
    private String name;

    public Agent(String name) {
        this.name = name;
    }

    public void start() {
        System.out.println("Hola, soy " + name + ".");
    }
}

public class Main {
    public static void main(String[] args) {
        Agent agent = new Agent("MiniJarvis");
        agent.start();
    }
}
```

## 4. Caso práctico MiniJarvis

Extrae de tu H3 al menos dos clases: `Agent` y `Memory`. `Main` debe quedar reducido a crear el agente y arrancarlo. `Agent` coordina comandos. `Memory` guarda recuerdos.

Escribe una frase de responsabilidad para cada clase.

Refuerzo de cobertura del Tema 5:

- `Memory` debe tener un constructor por defecto.
- Si el grupo está preparado, añade otro constructor que reciba recuerdos iniciales ficticios.
- Usa `this` cuando inicialices atributos.
- Añade Javadoc mínimo a una clase y a dos métodos públicos.

## 5. Evidencia de Entornos de Desarrollo

Crea `docs/relacion-clases.md` con una tabla: clase, responsabilidad, atributos, métodos y qué otra clase la usa. Esto prepara los diagramas de Entornos.

## 6. Errores frecuentes y cómo corregirlos

| Error | Síntoma | Corrección |
|---|---|---|
| Clases sin responsabilidad | No se sabe para qué existen | Escribir una frase por clase |
| Main sigue enorme | No hay mejora real | Mover coordinación a Agent |
| Constructor mal definido | Usa void o no inicializa | Nombre igual que clase y sin tipo de retorno |
| Constructor que deja estado inválido | Fallos posteriores | Inicializar todos los atributos necesarios |
| Documentación inventada | README/Javadoc no coincide con código | Revisar documentación contra implementación real |

## 7. Preguntas de repaso

1. ¿Qué es un objeto?
2. ¿Para qué sirve un constructor?
3. ¿Por qué Main debe quedar pequeño?
4. ¿Qué responsabilidad tiene Agent?
5. ¿Qué diferencia hay entre dos constructores sobrecargados?
6. ¿Para qué sirve `this`?

## 8. Para tu portfolio

Copia y completa este bloque en tu portfolio:

```text
Capítulo 06: Programación orientada a objetos
Qué he aprendido:
Código o documento que lo demuestra:
Prueba realizada:
Error que he corregido:
Qué puedo defender oralmente:
Uso de IA, si lo hubo, y cómo lo validé:
```

## 9. Estudio paso a paso

La POO se entiende mejor si preguntas “qué sabe” y “qué hace” cada clase. `Agent` sabe su nombre y coordina comandos. `Memory` sabe qué recuerdos hay y cómo añadirlos o mostrarlos. `Main` no debería saber los detalles del menú ni de la lista.

Caso de estudio: mira tu `Main` de H3 y subraya responsabilidades distintas. Si una línea trata de recuerdos, probablemente pertenece a `Memory`. Si una línea trata de comandos o conversación, probablemente pertenece a `Agent`. Escribe antes de tocar código qué moverás y por qué.

Caso de estudio de refuerzo: documenta en tu portfolio qué constructor usa `Main`, qué constructor quedaría para pruebas o datos iniciales y dónde aparece `this` en tu código.
