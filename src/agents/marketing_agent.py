from src.agents.base import BaseAgent


class MarketingAgent(BaseAgent):
    async def handle(self, text: str, user_id: int) -> str:
        return (
            "📢 *Marketing*\n\n"
            "Puedo ayudarte con:\n"
            "• Redactar descripciones de propiedades\n"
            "• Generar checklist de publicación\n"
            "• Recordatorios para redes sociales\n\n"
            "¿Qué necesitas exactamente?"
        )
