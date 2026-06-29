from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from src.services.github_service import github_service

router = Router()


@router.message(Command("nuevolead"))
async def cmd_nuevo_lead(message: Message):
    await message.answer(
        "👤 *Nuevo Lead*\n\n"
        "Dime los datos del lead en este formato:\n\n"
        "`Nombre | Teléfono | Email | Tipo`\n\n"
        "*Tipos:* comprador, vendedor, inversor\n\n"
        "Ejemplo:\n"
        "`Juan Pérez | 612345678 | juan@email.com | comprador`"
    )


@router.message(Command("nuevapropiedad"))
async def cmd_nueva_propiedad(message: Message):
    await message.answer(
        "🏠 *Nueva Propiedad*\n\n"
        "Dime los datos en este formato:\n\n"
        "`Título | Dirección | Tipo | Precio | m² | Hab | Baños`\n\n"
        "*Tipos:* piso, casa, local, terreno\n\n"
        "Ejemplo:\n"
        "`Piso centro | Calle Mayor 10 | piso | 180000 | 90 | 3 | 2`"
    )


@router.message(Command("tareas"))
async def cmd_tareas(message: Message):
    issues = await github_service.list_open_issues()
    if not issues:
        await message.answer("📋 *Tareas*\n\nNo hay tareas pendientes en GitHub.")
        return

    lines = [f"• #{i['number']} - {i['title']}" for i in issues[:10]]
    await message.answer("📋 *Tareas pendientes:*\n\n" + "\n".join(lines))


@router.message(Command("estado"))
async def cmd_estado(message: Message):
    await message.answer(
        "📊 *Resumen del día*\n\n"
        "• Leads nuevos: 0\n"
        "• Propiedades activas: 0\n"
        "• Tareas pendientes: —\n"
        "• Última actividad: —\n\n"
        "_Los datos se mostrarán cuando la base de datos esté conectada._"
    )


@router.message(Command("cancelar"))
async def cmd_cancelar(message: Message):
    await message.answer("✅ Operación cancelada. ¿En qué más puedo ayudarte?")
