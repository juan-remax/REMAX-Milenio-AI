from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from src.config.settings import settings

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        f"👋 *Bienvenido a {settings.app_name}*\n\n"
        "Soy tu asistente inmobiliario inteligente.\n"
        "Puedes enviarme mensajes para gestionar leads, propiedades, "
        "marketing y tareas.\n\n"
        "Usa /help para ver los comandos disponibles."
    )
