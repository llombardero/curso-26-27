import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        final String ASSISTANT_NAME = "MiniJarvis";
        Scanner scanner = new Scanner(System.in);

        System.out.println("Hola, soy " + ASSISTANT_NAME + ".");
        System.out.print("¿Cómo te llamas? ");
        String userName = scanner.nextLine();

        System.out.println("Encantada, " + userName + ". Escribe 'ayuda' para ver comandos.");

        boolean running = true;

        while (running) {
            System.out.print("> ");
            String command = scanner.nextLine().trim().toLowerCase();

            switch (command) {
                case "ayuda":
                    System.out.println("Comandos disponibles: ayuda, saluda, estado, java, salir");
                    break;
                case "saluda":
                    System.out.println("Hola " + userName + ", estoy aprendiendo a ayudarte.");
                    break;
                case "estado":
                    System.out.println(ASSISTANT_NAME + " está funcionando correctamente.");
                    break;
                case "java":
                    System.out.println("Java es el lenguaje principal que estamos usando para construir este agente.");
                    break;
                case "salir":
                    System.out.println("Hasta luego, " + userName + ".");
                    running = false;
                    break;
                default:
                    System.out.println("No entiendo ese comando. Escribe 'ayuda'.");
            }
        }

        scanner.close();
    }
}
