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
