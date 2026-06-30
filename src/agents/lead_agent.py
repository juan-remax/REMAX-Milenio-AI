from src.agents.base import BaseAgent
from src.database.models.lead import Lead
from src.database.session import async_session_factory
from src.services.inmovilla_client import inmovilla_client


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

        inmovilla_cod_cli = None
        if inmovilla_client.enabled:
            apellidos = ""
            nombre_parts = name.split(" ", 1)
            if len(nombre_parts) > 1:
                nombre = nombre_parts[0]
                apellidos = nombre_parts[1]
            else:
                nombre = name
            inmovilla_cod_cli = await inmovilla_client.create_client(
                nombre=nombre, apellidos=apellidos, telefono=phone, email=email,
            )

        try:
            async with async_session_factory() as session:
                lead = Lead(
                    name=name, phone=phone, email=email,
                    lead_type=lead_type_normalized, source="telegram",
                    inmovilla_cod_cli=inmovilla_cod_cli,
                )
                session.add(lead)
                await session.commit()
                await session.refresh(lead)

                lines = [
                    "✅ *Lead registrado correctamente!*",
                    f"*ID:* #{lead.id}",
                    f"*Nombre:* {lead.name}",
                    f"*Teléfono:* {lead.phone or '—'}",
                    f"*Email:* {lead.email or '—'}",
                    f"*Tipo:* {lead_type_normalized}",
                    f"*Estado:* {lead.status}",
                ]
                if inmovilla_cod_cli:
                    lines.append(f"*Inmovilla:* Cliente #{inmovilla_cod_cli}")
                elif inmovilla_client.enabled:
                    lines.append("_⚠️ No se pudo sincronizar con Inmovilla_")

                return "\n".join(lines)
        except Exception as e:
            return f"❌ Error al guardar el lead: {e}"
