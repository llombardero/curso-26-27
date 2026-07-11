public class CourseTool implements Tool {
    public String getCommand() {
        return "curso";
    }

    public String getDescription() {
        return "Muestra el curso de inicio del proyecto.";
    }

    public void execute(Agent agent) {
        System.out.println("Proyecto MiniJarvis iniciado en el curso " + agent.getCourseYear() + ".");
    }
}
