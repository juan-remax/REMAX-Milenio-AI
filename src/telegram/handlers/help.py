from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()


@router.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer(
        "*Comandos disponibles:*\n\n"
        "/start — Iniciar el bot\n"
        "/help — Mostrar esta ayuda\n"
        "/nuevolead — Registrar un nuevo lead\n"
        "/nuevapropiedad — Registrar una nueva propiedad\n"
        "/issue — Crear tarea en GitHub (`/issue Título | Descripción`)\n"
        "/tareas — Ver tareas pendientes en GitHub\n"
        "/estado — Resumen del día\n"
        "/cancelar — Cancelar operación actual\n\n"
        "También puedes escribir en lenguaje natural y te entenderé."
    )
