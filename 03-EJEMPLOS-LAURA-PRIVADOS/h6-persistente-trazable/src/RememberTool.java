public class RememberTool implements Tool {
    public String getCommand() { return "recuerda"; }
    public String getDescription() { return "Añade un recuerdo a la memoria."; }
    public void execute(Agent agent) {
        System.out.print("¿Qué quieres que recuerde? ");
        String text = agent.getScanner().nextLine().trim();
        if (agent.getMemory().add(text)) {
            System.out.println("He guardado en memoria temporal: " + text);
        } else {
            System.out.println("No puedo guardar un recuerdo vacío.");
        }
    }
}
