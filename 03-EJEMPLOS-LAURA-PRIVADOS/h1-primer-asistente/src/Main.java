import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        final String ASSISTANT_NAME = "MiniJarvis";
        final int EXTRA_HOURS_NEXT_WEEK = 1;
        final int REFERENCE_HOURS = 3;

        Scanner scanner = new Scanner(System.in);

        System.out.println("Hola, soy " + ASSISTANT_NAME + ".");
        System.out.print("¿Cómo te llamas? ");
        String userName = scanner.nextLine();

        System.out.print("¿Cuántas horas has practicado Programación? ");
        String hoursText = scanner.nextLine();
        int studyHours = Integer.parseInt(hoursText);

        int nextWeekHours = studyHours + EXTRA_HOURS_NEXT_WEEK;
        boolean enoughPractice = studyHours >= REFERENCE_HOURS;

        System.out.println("Hola, " + userName + ".");
        System.out.println(
                "Si la próxima semana practicas una hora más, serán "
                        + nextWeekHours
                        + " horas."
        );
        System.out.println(
                "¿Has practicado al menos "
                        + REFERENCE_HOURS
                        + " horas? "
                        + enoughPractice
        );

        scanner.close();
    }
}
