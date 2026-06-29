from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import Message, TelegramObject

from src.config.settings import settings


class AuthMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:
        if isinstance(event, Message):
            if event.from_user and event.from_user.id not in settings.allowed_user_ids:
                await event.answer(
                    "Lo siento, no estás autorizado para usar este bot."
                )
                return

        return await handler(event, data)
