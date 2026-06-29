from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from src.config.settings import settings
from src.telegram.handlers import commands, confirmation, help, issue, message, start
from src.telegram.middlewares.auth import AuthMiddleware

dp = Dispatcher()

dp.message.middleware(AuthMiddleware())

dp.include_router(start.router)
dp.include_router(help.router)
dp.include_router(issue.router)
dp.include_router(commands.router)
dp.include_router(confirmation.router)
dp.include_router(message.router)


def setup_bot() -> Bot:
    return Bot(
        token=settings.bot_token,
        default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN),
    )
