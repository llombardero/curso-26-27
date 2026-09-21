public interface Tool {
    String getCommand();
    String getDescription();
    void execute(Agent agent);
}
