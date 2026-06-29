from src.agents.base import BaseAgent
from src.database.models.property import Property
from src.database.session import async_session_factory


class PropertyAgent(BaseAgent):
    async def handle(self, text: str, user_id: int) -> str:
        if "|" in text:
            return await self._create_property(text)

        return (
            "🏠 *Gestión de Propiedades*\n\n"
            "Para registrar una propiedad, envíame los datos en este formato:\n\n"
            "`Título | Dirección | Tipo | Precio | m² | Habitaciones | Baños`\n\n"
            "*Tipos:* piso, casa, local, terreno\n\n"
            "Ejemplo:\n"
            "`Piso centro | Calle Mayor 10 | piso | 180000 | 90 | 3 | 2`"
        )

    async def _create_property(self, text: str) -> str:
        parts = [p.strip() for p in text.split("|")]
        if len(parts) < 3:
            return "❌ Formato incorrecto. Usa: `Título | Dirección | Tipo | Precio | m² | Hab | Baños`"

        title = parts[0]
        address = parts[1]
        property_type = parts[2].lower() if len(parts) > 2 else ""

        type_map = {
            "piso": "apartment", "apartamento": "apartment",
            "casa": "house", "chalet": "house",
            "local": "commercial", "comercial": "commercial",
            "terreno": "land", "solar": "land",
        }
        property_type_normalized = type_map.get(property_type, "apartment")

        try:
            price = float(parts[3].replace(".", "").replace(",", ".")) if len(parts) > 3 and parts[3] else 0
        except (ValueError, IndexError):
            price = 0

        try:
            sqm = float(parts[4]) if len(parts) > 4 and parts[4] else None
        except (ValueError, IndexError):
            sqm = None

        try:
            bedrooms = int(parts[5]) if len(parts) > 5 and parts[5] else None
        except (ValueError, IndexError):
            bedrooms = None

        try:
            bathrooms = int(parts[6]) if len(parts) > 6 and parts[6] else None
        except (ValueError, IndexError):
            bathrooms = None

        try:
            async with async_session_factory() as session:
                prop = Property(
                    title=title,
                    address=address,
                    property_type=property_type_normalized,
                    price=price,
                    square_meters=sqm,
                    bedrooms=bedrooms,
                    bathrooms=bathrooms,
                )
                session.add(prop)
                await session.commit()
                await session.refresh(prop)

                return (
                    f"✅ *Propiedad registrada correctamente!*\n\n"
                    f"*ID:* #{prop.id}\n"
                    f"*Título:* {prop.title}\n"
                    f"*Dirección:* {prop.address}\n"
                    f"*Tipo:* {prop.property_type}\n"
                    f"*Precio:* €{prop.price:,.0f}\n"
                    f"*Metros:* {prop.square_meters or '—'} m²\n"
                    f"*Estado:* {prop.status}"
                )
        except Exception as e:
            return f"❌ Error al guardar la propiedad: {e}"
