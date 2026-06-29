from src.agents.base import BaseAgent
from src.database.models.lead import Lead
from src.database.session import async_session_factory


class LeadAgent(BaseAgent):
    async def handle(self, text: str, user_id: int) -> str:
        if "|" in text:
            return await self._create_lead(text)

        return (
            "👤 *Gestión de Leads*\n\n"
            "Para registrar un lead, envíame los datos en este formato:\n\n"
            "`Nombre | Teléfono | Email | Tipo`\n\n"
            "*Tipos de lead:* comprador, vendedor, inversor\n\n"
            "Ejemplo:\n"
            "`María García | 612345678 | maria@email.com | compradora`"
        )

    async def _create_lead(self, text: str) -> str:
        parts = [p.strip() for p in text.split("|")]
        if len(parts) < 1:
            return "❌ Formato incorrecto. Usa: `Nombre | Teléfono | Email | Tipo`"

        name = parts[0]
        phone = parts[1] if len(parts) > 1 else ""
        email = parts[2] if len(parts) > 2 else ""
        lead_type = parts[3].lower() if len(parts) > 3 else ""

        type_map = {
            "comprador": "buyer", "compradora": "buyer",
            "vendedor": "seller", "vendedora": "seller",
            "inversor": "investor", "inversora": "investor",
        }
        lead_type_normalized = type_map.get(lead_type, "buyer")

        try:
            async with async_session_factory() as session:
                lead = Lead(
                    name=name, phone=phone, email=email,
                    lead_type=lead_type_normalized, source="telegram",
                )
                session.add(lead)
                await session.commit()
                await session.refresh(lead)

                return (
                    f"✅ *Lead registrado correctamente!*\n\n"
                    f"*ID:* #{lead.id}\n"
                    f"*Nombre:* {lead.name}\n"
                    f"*Teléfono:* {lead.phone or '—'}\n"
                    f"*Email:* {lead.email or '—'}\n"
                    f"*Tipo:* {lead_type_normalized}\n"
                    f"*Estado:* {lead.status}"
                )
        except Exception as e:
            return f"❌ Error al guardar el lead: {e}"
