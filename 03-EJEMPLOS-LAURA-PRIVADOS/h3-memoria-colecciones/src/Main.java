import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        final String ASSISTANT_NAME = "MiniJarvis";
        final int COURSE_YEAR = 2026;

        Scanner scanner = new Scanner(System.in);
        ArrayList<String> memories = new ArrayList<>();

        System.out.println("Hola, soy " + ASSISTANT_NAME + ".");
        System.out.print("¿Cómo te llamas? ");
        String userName = scanner.nextLine();

        System.out.println("Encantada, " + userName + ".");
        System.out.println("Curso de inicio: " + COURSE_YEAR + ".");
        System.out.println("Escribe ayuda para ver los comandos disponibles.");

        boolean running = true;

        while (running) {
            System.out.print("> ");
            String command = scanner.nextLine().trim().toLowerCase();

            if (command.equals("ayuda")) {
                System.out.println("Comandos disponibles: ayuda, saluda, recuerda, memoria, estado, salir");
            } else if (command.equals("saluda")) {
                System.out.println("Hola, " + userName + ". Soy " + ASSISTANT_NAME + ".");
            } else if (command.equals("recuerda")) {
                System.out.print("¿Qué quieres que recuerde? ");
                String memory = scanner.nextLine().trim();

                if (memory.isEmpty()) {
                    System.out.println("No puedo guardar un recuerdo vacío.");
                } else {
                    memories.add(memory);
                    System.out.println("He guardado: " + memory);
                }
            } else if (command.equals("memoria")) {
                if (memories.isEmpty()) {
                    System.out.println("No tengo recuerdos todavía.");
                } else {
                    System.out.println("Recuerdos guardados:");
                    for (int i = 0; i < memories.size(); i++) {
                        System.out.println((i + 1) + ". " + memories.get(i));
                    }
                }
            } else if (command.equals("estado")) {
                System.out.println("Tengo " + memories.size() + " recuerdo(s) en memoria temporal.");
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
