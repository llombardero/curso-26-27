public class StatusTool implements Tool {
    public String getCommand() { return "estado"; }
    public String getDescription() { return "Muestra estado de memoria y curso."; }
    public void execute(Agent agent) {
        System.out.println("Curso " + agent.getCourseYear() + ": " + agent.getMemory().count() + " recuerdo(s) cargados.");
    }
}
