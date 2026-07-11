import java.util.Scanner;

public class Agent {
    private final String name;
    private final Scanner scanner;
    private final SimulatedAiAssistant aiAssistant;
    private boolean running;

    public Agent(String name) {
        this.name = name;
        this.scanner = new Scanner(System.in);
        this.aiAssistant = new SimulatedAiAssistant();
        this.running = true;
    }

    public void start() {
        System.out.println("Hola, soy " + name + " H7.");
        System.out.println("Modo IA: simulación responsable sin API key real.");
        System.out.println("Comandos: ayuda, ia, riesgos, salir");

        while (running) {
            System.out.print("> ");
            String command = scanner.nextLine().trim().toLowerCase();
            processCommand(command);
        }

        scanner.close();
    }

    private void processCommand(String command) {
        if (command.equals("ayuda")) {
            showHelp();
        } else if (command.equals("ia")) {
            askSimulatedAi();
        } else if (command.equals("riesgos")) {
            showRisks();
        } else if (command.equals("salir")) {
            System.out.println("Cerrando modo IA responsable.");
            running = false;
        } else {
            System.out.println("Comando no reconocido. Escribe ayuda.");
        }
    }

    private void showHelp() {
        System.out.println("ayuda: muestra comandos");
        System.out.println("ia: pide una sugerencia segura a la IA simulada");
        System.out.println("riesgos: recuerda límites de seguridad");
        System.out.println("salir: termina");
    }

    private void askSimulatedAi() {
        System.out.print("Escribe una pregunta de estudio sin datos personales ni secretos: ");
        String prompt = scanner.nextLine().trim();
        AiResponse response = aiAssistant.answer(prompt);
        System.out.println(response.getMessage());
        System.out.println("Validación humana requerida: revisa si la respuesta es correcta antes de usarla.");
    }

    private void showRisks() {
        System.out.println("No introduzcas contraseñas, tokens, API keys ni datos personales reales.");
        System.out.println("La IA puede equivocarse: valida siempre la respuesta.");
    }
}
