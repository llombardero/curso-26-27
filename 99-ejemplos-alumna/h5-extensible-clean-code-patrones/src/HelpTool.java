public class HelpTool implements Tool {
    public String getCommand() {
        return "ayuda";
    }

    public String getDescription() {
        return "Muestra herramientas disponibles.";
    }

    public void execute(Agent agent) {
        System.out.println("Herramientas disponibles:");
        for (Tool tool : agent.getTools()) {
            System.out.println("- " + tool.getCommand() + ": " + tool.getDescription());
        }
    }
}
