from src.agents.base import BaseAgent


class LeadAgent(BaseAgent):
    async def handle(self, text: str, user_id: int) -> str:
        return (
            "👤 *Gestión de Leads*\n\n"
            "Para registrar un nuevo lead necesito:\n"
            "1. Nombre completo\n"
            "2. Teléfono\n"
            "3. Email\n"
            "4. Tipo (comprador / vendedor / inversor)\n\n"
            "Puedes usar: `/nuevolead` para iniciar el formulario guiado."
        )
