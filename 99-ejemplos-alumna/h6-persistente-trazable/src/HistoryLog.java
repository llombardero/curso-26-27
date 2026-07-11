import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.StandardOpenOption;

public class HistoryLog {
    private final Path filePath;

    public HistoryLog(String fileName) {
        this.filePath = Path.of(fileName);
    }

    public void write(String event) {
        try {
            Files.createDirectories(filePath.getParent());
            String safeLine = "EVENTO: " + event + System.lineSeparator();
            Files.writeString(filePath, safeLine, StandardOpenOption.CREATE, StandardOpenOption.APPEND);
        } catch (IOException error) {
            System.out.println("No he podido escribir el historial: " + error.getMessage());
        }
    }
}
