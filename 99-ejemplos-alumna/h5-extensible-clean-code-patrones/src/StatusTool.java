public class StatusTool implements Tool {
    public String getCommand() {
        return "estado";
    }

    public String getDescription() {
        return "Muestra estado del agente.";
    }

    public void execute(Agent agent) {
        System.out.println("Tengo " + agent.getMemory().count() + " recuerdo(s) y " + agent.getTools().size() + " herramienta(s) internas.");
    }
}
