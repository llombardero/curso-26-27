public class ExitTool implements Tool {
    public String getCommand() { return "salir"; }
    public String getDescription() { return "Guarda y termina."; }
    public void execute(Agent agent) {
        agent.getMemory().save();
        System.out.println("Memoria guardada. Hasta pronto, " + agent.getUserName() + ".");
        agent.stop();
    }
}
