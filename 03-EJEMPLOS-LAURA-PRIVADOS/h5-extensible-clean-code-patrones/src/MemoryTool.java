public class MemoryTool implements Tool {
    public String getCommand() {
        return "memoria";
    }

    public String getDescription() {
        return "Muestra recuerdos guardados.";
    }

    public void execute(Agent agent) {
        System.out.println(agent.getMemory().formatMemories());
    }
}
