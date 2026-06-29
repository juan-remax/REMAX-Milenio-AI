from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from src.services.github_service import github_service

router = Router()


@router.message(Command("issue"))
async def cmd_issue(message: Message):
    args = message.text.removeprefix("/issue").strip()
    if not args:
        await message.answer(
            "📝 *Crear Issue en GitHub*\n\n"
            "Uso: `/issue Título | Descripción`\n\n"
            "Ejemplo:\n"
            "`/issue Revisar propiedad Calle Mayor 123 | El cliente quiere visitar el viernes`"
        )
        return

    parts = args.split(" | ", 1)
    title = parts[0].strip()
    body = parts[1].strip() if len(parts) > 1 else "Sin descripción"

    result = await github_service.create_issue(title, body, ["telegram"])
    await message.answer(result)
