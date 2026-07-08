import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        final String ASSISTANT_NAME = "MiniJarvis";
        final int COURSE_YEAR = 2026;

        Scanner scanner = new Scanner(System.in);

        System.out.println("Hola, soy " + ASSISTANT_NAME + ".");
        System.out.print("¿Cómo te llamas? ");
        String userName = scanner.nextLine();

        System.out.println("Encantada, " + userName + ".");
        System.out.println("Este curso vamos a crear un pequeño agente IA.");
        System.out.println("Curso de inicio: " + COURSE_YEAR + ".");
        System.out.println("Escribe ayuda para ver los comandos disponibles.");

        boolean running = true;

        while (running) {
            System.out.print("> ");
            String command = scanner.nextLine().trim().toLowerCase();

            if (command.equals("ayuda")) {
                System.out.println("Comandos disponibles: ayuda, saluda, estado, salir");
            } else if (command.equals("saluda")) {
                System.out.println("Hola, " + userName + ". Soy " + ASSISTANT_NAME + ".");
            } else if (command.equals("estado")) {
                System.out.println("Estoy funcionando en modo H2, con menú y sin memoria todavía.");
            } else if (command.equals("salir")) {
                System.out.println("Hasta pronto, " + userName + ".");
                running = false;
            } else {
                System.out.println("No entiendo ese comando. Escribe ayuda.");
            }
        }

        scanner.close();
    }
}
