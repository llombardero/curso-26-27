import java.util.ArrayList;
import java.util.Scanner;

public class Agent {
    private final String name;
    private final int courseYear;
    private final PersistentMemory memory;
    private final HistoryLog historyLog;
    private final Scanner scanner;
    private final ArrayList<Tool> tools;
    private String userName;
    private boolean running;

    public Agent(String name, int courseYear) {
        this.name = name;
        this.courseYear = courseYear;
        this.memory = new PersistentMemory("data/recuerdos.txt");
        this.historyLog = new HistoryLog("logs/historial.log");
        this.scanner = new Scanner(System.in);
        this.tools = new ArrayList<>();
        this.userName = "";
        this.running = true;
    }

    public void registerDefaultTools() {
        registerTool(new HelpTool());
        registerTool(new RememberTool());
        registerTool(new MemoryTool());
        registerTool(new SaveTool());
        registerTool(new StatusTool());
        registerTool(new ExitTool());
    }

    public void registerTool(Tool tool) { tools.add(tool); }

    public void start() {
        memory.load();
        historyLog.write("Inicio de MiniJarvis H6");
        greetUser();
        while (running) {
            System.out.print("> ");
            String command = scanner.nextLine().trim().toLowerCase();
            processCommand(command);
        }
        historyLog.write("Fin de MiniJarvis H6");
        scanner.close();
    }

    private void greetUser() {
        System.out.println("Hola, soy " + name + ".");
        System.out.print("¿Cómo te llamas? ");
        userName = scanner.nextLine();
        System.out.println("Encantada, " + userName + ".");
        System.out.println("Memoria cargada: " + memory.count() + " recuerdo(s).");
        System.out.println("Escribe ayuda para ver las herramientas disponibles.");
    }

    private void processCommand(String command) {
        for (Tool tool : tools) {
            if (tool.getCommand().equals(command)) {
                historyLog.write("Comando ejecutado: " + command);
                tool.execute(this);
                return;
            }
        }
        System.out.println("No entiendo esa herramienta. Escribe ayuda.");
        historyLog.write("Comando desconocido");
    }

    public String getName() { return name; }
    public int getCourseYear() { return courseYear; }
    public String getUserName() { return userName; }
    public PersistentMemory getMemory() { return memory; }
    public HistoryLog getHistoryLog() { return historyLog; }
    public Scanner getScanner() { return scanner; }
    public ArrayList<Tool> getTools() { return tools; }
    public void stop() { running = false; }
}
