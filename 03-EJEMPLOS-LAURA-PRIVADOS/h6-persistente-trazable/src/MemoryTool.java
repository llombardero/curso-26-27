public class MemoryTool implements Tool {
    public String getCommand() { return "memoria"; }
    public String getDescription() { return "Muestra recuerdos cargados."; }
    public void execute(Agent agent) { System.out.println(agent.getMemory().formatMemories()); }
}
