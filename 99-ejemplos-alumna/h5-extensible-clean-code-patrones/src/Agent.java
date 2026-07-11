import java.util.ArrayList;
import java.util.Scanner;

public class Agent {
    private final String name;
    private final int courseYear;
    private final Memory memory;
    private final Scanner scanner;
    private final ArrayList<Tool> tools;
    private String userName;
    private boolean running;

    public Agent(String name, int courseYear) {
        this.name = name;
        this.courseYear = courseYear;
        this.memory = new Memory();
        this.scanner = new Scanner(System.in);
        this.tools = new ArrayList<>();
        this.userName = "";
        this.running = true;
    }

    public void registerDefaultTools() {
        registerTool(new HelpTool());
        registerTool(new GreetTool());
        registerTool(new RememberTool());
        registerTool(new MemoryTool());
        registerTool(new StatusTool());
        registerTool(new CourseTool());
        registerTool(new ExitTool());
    }

    public void registerTool(Tool tool) {
        tools.add(tool);
    }

    public void start() {
        greetUser();

        while (running) {
            System.out.print("> ");
            String command = scanner.nextLine().trim().toLowerCase();
            processCommand(command);
        }

        scanner.close();
    }

    private void greetUser() {
        System.out.println("Hola, soy " + name + ".");
        System.out.print("¿Cómo te llamas? ");
        userName = scanner.nextLine();
        System.out.println("Encantada, " + userName + ".");
        System.out.println("Escribe ayuda para ver las herramientas disponibles.");
    }

    private void processCommand(String command) {
        for (Tool tool : tools) {
            if (tool.getCommand().equals(command)) {
                tool.execute(this);
                return;
            }
        }

        System.out.println("No entiendo esa herramienta. Escribe ayuda.");
    }

    public String getName() {
        return name;
    }

    public int getCourseYear() {
        return courseYear;
    }

    public String getUserName() {
        return userName;
    }

    public Memory getMemory() {
        return memory;
    }

    public Scanner getScanner() {
        return scanner;
    }

    public ArrayList<Tool> getTools() {
        return tools;
    }

    public void stop() {
        running = false;
    }
}
