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
        System.out.println("Primer objetivo: aprender la estructura básica de un programa Java.");

        scanner.close();
    }
}
