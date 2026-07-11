public class ExitTool implements Tool {
    public String getCommand() {
        return "salir";
    }

    public String getDescription() {
        return "Termina el programa.";
    }

    public void execute(Agent agent) {
        System.out.println("Hasta pronto, " + agent.getUserName() + ".");
        agent.stop();
    }
}
