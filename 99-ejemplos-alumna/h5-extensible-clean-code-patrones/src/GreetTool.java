public class GreetTool implements Tool {
    public String getCommand() {
        return "saluda";
    }

    public String getDescription() {
        return "Saluda a la persona usuaria.";
    }

    public void execute(Agent agent) {
        System.out.println("Hola, " + agent.getUserName() + ". Soy " + agent.getName() + ".");
    }
}
