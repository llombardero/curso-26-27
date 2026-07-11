public class SimulatedAiAssistant {
    public AiResponse answer(String prompt) {
        if (prompt.isEmpty()) {
            return new AiResponse("No puedo responder a una pregunta vacía.");
        }

        if (PromptSafety.containsForbiddenData(prompt)) {
            return new AiResponse("Solicitud bloqueada: no introduzcas secretos ni datos personales.");
        }

        if (prompt.toLowerCase().contains("arraylist")) {
            return new AiResponse("Sugerencia simulada: ArrayList sirve para guardar elementos en orden. Valida esta explicación con tus apuntes y tu código.");
        }

        return new AiResponse("Sugerencia simulada: divide el problema en pasos pequeños, prueba el código y documenta la decisión. Revisa siempre la respuesta.");
    }
}
