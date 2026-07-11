import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.StandardOpenOption;
import java.util.ArrayList;
import java.util.List;

public class PersistentMemory {
    private final Path filePath;
    private final ArrayList<String> memories;

    public PersistentMemory(String fileName) {
        this.filePath = Path.of(fileName);
        this.memories = new ArrayList<>();
    }

    public void load() {
        try {
            Files.createDirectories(filePath.getParent());
            if (!Files.exists(filePath)) {
                Files.createFile(filePath);
            }
            memories.clear();
            List<String> lines = Files.readAllLines(filePath);
            for (String line : lines) {
                String clean = line.trim();
                if (!clean.isEmpty()) {
                    memories.add(clean);
                }
            }
        } catch (IOException error) {
            System.out.println("No he podido cargar la memoria: " + error.getMessage());
        }
    }

    public boolean add(String text) {
        if (text.isEmpty()) {
            return false;
        }
        memories.add(text);
        return true;
    }

    public void save() {
        try {
            Files.createDirectories(filePath.getParent());
            Files.write(filePath, memories, StandardOpenOption.CREATE, StandardOpenOption.TRUNCATE_EXISTING);
        } catch (IOException error) {
            System.out.println("No he podido guardar la memoria: " + error.getMessage());
        }
    }

    public int count() { return memories.size(); }

    public String formatMemories() {
        if (memories.isEmpty()) {
            return "No tengo recuerdos todavía.";
        }
        String result = "Recuerdos guardados:";
        for (int i = 0; i < memories.size(); i++) {
            result += System.lineSeparator() + (i + 1) + ". " + memories.get(i);
        }
        return result;
    }
}
