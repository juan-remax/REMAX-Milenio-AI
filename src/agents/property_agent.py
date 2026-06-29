from src.agents.base import BaseAgent


class PropertyAgent(BaseAgent):
    async def handle(self, text: str, user_id: int) -> str:
        return (
            "🏠 *Gestión de Propiedades*\n\n"
            "Para registrar una nueva propiedad necesito:\n"
            "1. Dirección\n"
            "2. Tipo (piso, casa, local, terreno)\n"
            "3. Precio\n"
            "4. Metros cuadrados\n"
            "5. Habitaciones / baños\n\n"
            "Usa: `/nuevapropiedad` para el formulario guiado."
        )
