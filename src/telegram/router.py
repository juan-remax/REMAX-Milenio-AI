from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from src.config.settings import settings
from src.telegram.handlers import start, help, message
from src.telegram.middlewares.auth import AuthMiddleware


def setup_dispatcher() -> Dispatcher:
    bot = Bot(
        token=settings.bot_token,
        default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN),
    )
    dp = Dispatcher()

    dp.message.middleware(AuthMiddleware())

    dp.include_router(start.router)
    dp.include_router(help.router)
    dp.include_router(message.router)

    return dp
