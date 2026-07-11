public class SaveTool implements Tool {
    public String getCommand() { return "guardar"; }
    public String getDescription() { return "Guarda la memoria en fichero."; }
    public void execute(Agent agent) {
        agent.getMemory().save();
        agent.getHistoryLog().write("Memoria guardada");
        System.out.println("Memoria guardada en data/recuerdos.txt.");
    }
}
