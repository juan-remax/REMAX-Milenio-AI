from src.agents.intent_classifier import classify_intent
from src.agents.lead_agent import LeadAgent
from src.agents.marketing_agent import MarketingAgent
from src.agents.property_agent import PropertyAgent
from src.memory.conversation_log import log_conversation

lead_agent = LeadAgent()
property_agent = PropertyAgent()
marketing_agent = MarketingAgent()


async def route_intent(text: str, user_id: int) -> str:
    intent = classify_intent(text)

    if intent == "lead":
        response = await lead_agent.handle(text, user_id)
    elif intent == "property":
        response = await property_agent.handle(text, user_id)
    elif intent == "marketing":
        response = await marketing_agent.handle(text, user_id)
    elif intent == "task":
        response = (
            "📋 *Tareas pendientes:*\n"
            "- Feature 001: Telegram Bot\n"
            "- Feature 002: Agent Router\n\n"
            "Usa /help para más opciones."
        )
    elif intent == "status":
        response = (
            "📊 *Resumen del día:*\n"
            "- Leads hoy: 0\n"
            "- Propiedades nuevas: 0\n"
            "- Tareas pendientes: 2"
        )
    else:
        response = (
            "No entendí tu mensaje. Puedes escribir cosas como:\n"
            "• \"Nuevo cliente\" para registrar un lead\n"
            "• \"Nueva propiedad\" para dar de alta un inmueble\n"
            "• \"Publicar\" para tareas de marketing\n\n"
            "O usa /help para ver los comandos."
        )

    await log_conversation(user_id, text, response)
    return response
