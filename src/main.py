import asyncio

from fastapi import FastAPI
from loguru import logger

from src.config.settings import settings
from src.telegram.router import setup_bot, dp
from src.database.models.base import Base
from src.database.session import engine

app = FastAPI(title=settings.app_name)

bot = setup_bot()
_polling_task: asyncio.Task | None = None


@app.on_event("startup")
async def startup():
    global _polling_task
    logger.info(f"Starting {settings.app_name}")

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    logger.info("Database tables ensured")

    _polling_task = asyncio.create_task(dp.start_polling(bot))


@app.on_event("shutdown")
async def shutdown():
    global _polling_task
    logger.info(f"Shutting down {settings.app_name}")
    if _polling_task:
        _polling_task.cancel()
    await bot.session.close()


@app.get("/health")
async def health():
    return {"status": "ok", "app": settings.app_name}
