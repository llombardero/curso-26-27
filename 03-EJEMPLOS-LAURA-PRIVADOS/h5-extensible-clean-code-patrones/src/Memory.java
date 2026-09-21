import java.util.ArrayList;

public class Memory {
    private final ArrayList<String> memories;

    public Memory() {
        this.memories = new ArrayList<>();
    }

    public boolean add(String text) {
        if (text.isEmpty()) {
            return false;
        }

        memories.add(text);
        return true;
    }

    public int count() {
        return memories.size();
    }

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
