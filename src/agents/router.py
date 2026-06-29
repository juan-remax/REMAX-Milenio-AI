from src.agents.lead_agent import LeadAgent
from src.agents.property_agent import PropertyAgent
from src.agents.marketing_agent import MarketingAgent
from src.memory.conversation_log import log_conversation

lead_agent = LeadAgent()
property_agent = PropertyAgent()
marketing_agent = MarketingAgent()


INTENT_RULES = {
    "lead": ["nuevo cliente", "nuevo lead", "registrar cliente", "captar", "lead", "cliente potencial", "interesado"],
    "property": ["nueva propiedad", "registrar propiedad", "alta propiedad", "listing", "propiedad", "inmueble", "casa", "piso"],
    "marketing": ["publicar", "marketing", "anuncio", "redes", "publicación", "promocionar", "difundir"],
    "task": ["tarea", "pendiente", "recordatorio", "hacer", "to-do"],
    "status": ["estado", "resumen", "balance", "cómo voy", "reporte"],
}


def classify_intent(text: str) -> str:
    text_lower = text.lower()
    for intent, keywords in INTENT_RULES.items():
        for keyword in keywords:
            if keyword in text_lower:
                return intent
    return "unknown"


async def route_intent(text: str, user_id: int) -> str:
    intent = classify_intent(text)

    if intent == "lead":
        response = await lead_agent.handle(text, user_id)
    elif intent == "property":
        response = await property_agent.handle(text, user_id)
    elif intent == "marketing":
        response = await marketing_agent.handle(text, user_id)
    elif intent == "task":
        response = "📋 *Tareas pendientes:*\n- Feature 001: Telegram Bot\n- Feature 002: Agent Router\n\nUsa /help para más opciones."
    elif intent == "status":
        response = "📊 *Resumen del día:*\n- Leads hoy: 0\n- Propiedades nuevas: 0\n- Tareas pendientes: 2"
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
