from aiogram import Router
from aiogram.types import Message

from src.services.notification import confirmation_guard

router = Router()


@router.message(lambda msg: msg.text and msg.text.strip().upper() in ("SÍ", "SI", "NO"))
async def handle_confirmation(message: Message):
    text = message.text.strip().upper()
    user_id = message.from_user.id

    if not confirmation_guard.has_pending(user_id):
        return

    if text in ("SÍ", "SI"):
        pending = await confirmation_guard.confirm(user_id)
        if pending:
            await message.answer(f"✅ *Acción confirmada:* {pending['action']}")
        else:
            await message.answer("⚠️ La confirmación expiró.")
    else:
        confirmation_guard._pending.pop(user_id, None)
        await message.answer("❌ Acción cancelada.")
