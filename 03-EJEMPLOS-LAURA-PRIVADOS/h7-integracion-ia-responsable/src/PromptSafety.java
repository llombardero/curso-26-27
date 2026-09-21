public class PromptSafety {
    public static boolean containsForbiddenData(String text) {
        String lower = text.toLowerCase();
        return lower.contains("password")
            || lower.contains("contraseña")
            || lower.contains("token")
            || lower.contains("api_key")
            || lower.contains("apikey")
            || lower.contains("dni")
            || lower.contains("teléfono")
            || lower.contains("telefono");
    }
}
