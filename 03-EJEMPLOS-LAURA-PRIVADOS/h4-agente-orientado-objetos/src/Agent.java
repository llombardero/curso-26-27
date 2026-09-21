import java.util.Scanner;

public class Agent {
    private final String name;
    private final int courseYear;
    private final Memory memory;
    private final Scanner scanner;
    private String userName;
    private boolean running;

    public Agent(String name, int courseYear) {
        this.name = name;
        this.courseYear = courseYear;
        this.memory = new Memory();
        this.scanner = new Scanner(System.in);
        this.userName = "";
        this.running = true;
    }

    public void start() {
        greetUser();

        while (running) {
            System.out.print("> ");
            String command = scanner.nextLine().trim().toLowerCase();
            processCommand(command);
        }

        scanner.close();
    }

    private void greetUser() {
        System.out.println("Hola, soy " + name + ".");
        System.out.print("¿Cómo te llamas? ");
        userName = scanner.nextLine();
        System.out.println("Encantada, " + userName + ".");
        System.out.println("Curso de inicio: " + courseYear + ".");
        System.out.println("Escribe ayuda para ver los comandos disponibles.");
    }

    private void processCommand(String command) {
        if (command.equals("ayuda")) {
            showHelp();
        } else if (command.equals("saluda")) {
            System.out.println("Hola, " + userName + ". Soy " + name + ".");
        } else if (command.equals("recuerda")) {
            remember();
        } else if (command.equals("memoria")) {
            System.out.println(memory.formatMemories());
        } else if (command.equals("estado")) {
            System.out.println("Tengo " + memory.count() + " recuerdo(s) en memoria temporal.");
        } else if (command.equals("salir")) {
            System.out.println("Hasta pronto, " + userName + ".");
            running = false;
        } else {
            System.out.println("No entiendo ese comando. Escribe ayuda.");
        }
    }

    private void showHelp() {
        System.out.println("Comandos disponibles: ayuda, saluda, recuerda, memoria, estado, salir");
    }

    private void remember() {
        System.out.print("¿Qué quieres que recuerde? ");
        String text = scanner.nextLine().trim();

        if (memory.add(text)) {
            System.out.println("He guardado: " + text);
        } else {
            System.out.println("No puedo guardar un recuerdo vacío.");
        }
    }
}
