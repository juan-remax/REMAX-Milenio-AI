from src.agents.base import BaseAgent


class MarketingAgent(BaseAgent):
    async def handle(self, text: str, user_id: int) -> str:
        if "|" in text:
            return self._generate_description(text)

        return (
            "📢 *Marketing*\n\n"
            "Puedo ayudarte con:\n\n"
            "• *Descripción* para anuncio:\n"
            "  `Título | Dirección | Precio | m² | Hab | Baños | Extras`\n\n"
            "• *Checklist de publicación:*\n"
            "  `checklist | Idealista | Fotocasa | Milanuncios`\n\n"
            "• *Recordatorios:* di \"marketing recordatorio\"\n\n"
            "Ejemplo:\n"
            "`Piso reformado | Centro ciudad | 180000 | 90 | 3 | 2 | terraza y ascensor`"
        )

    def _generate_description(self, text: str) -> str:
        parts = [p.strip() for p in text.split("|")]

        title = parts[0] if len(parts) > 0 else "Propiedad"
        address = parts[1] if len(parts) > 1 else ""
        price = parts[2] if len(parts) > 2 else ""
        sqm = parts[3] if len(parts) > 3 else ""
        bedrooms = parts[4] if len(parts) > 4 else ""
        bathrooms = parts[5] if len(parts) > 5 else ""
        extras = parts[6] if len(parts) > 6 else ""

        desc = (
            f"✨ *{title}*\n\n"
            f"📍 {address}\n\n"
            f"🏠 *Características principales:*\n"
        )

        if bedrooms and bathrooms:
            desc += f"• {bedrooms} habitaciones / {bathrooms} baños\n"
        if sqm:
            desc += f"• {sqm} m² construidos\n"
        if price:
            desc += f"• Precio: €{price}\n"
        if extras:
            desc += f"• {extras}\n"

        desc += (
            "\n📞 *Contacto:*\n"
            "Para más información o visita, no dudes en contactarnos.\n"
            "REMAX Milenio — Tu agencia de confianza."
        )

        return desc
