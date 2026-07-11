public class RememberTool implements Tool {
    public String getCommand() {
        return "recuerda";
    }

    public String getDescription() {
        return "Guarda un recuerdo en memoria temporal.";
    }

    public void execute(Agent agent) {
        System.out.print("¿Qué quieres que recuerde? ");
        String text = agent.getScanner().nextLine().trim();

        if (agent.getMemory().add(text)) {
            System.out.println("He guardado: " + text);
        } else {
            System.out.println("No puedo guardar un recuerdo vacío.");
        }
    }
}
