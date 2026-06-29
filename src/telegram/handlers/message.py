from aiogram import Router
from aiogram.types import Message

from src.agents.router import route_intent

router = Router()


@router.message()
async def handle_message(message: Message):
    if not message.text:
        await message.answer("Solo entiendo mensajes de texto por ahora.")
        return

    response = await route_intent(message.text, message.from_user.id)
    await message.answer(response)
