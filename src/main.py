from fastapi import FastAPI
from loguru import logger

from src.config.settings import settings
from src.telegram.router import setup_dispatcher

app = FastAPI(title=settings.app_name)

dispatcher = setup_dispatcher()


@app.on_event("startup")
async def startup():
    logger.info(f"Starting {settings.app_name}")
    await dispatcher.start_polling()


@app.on_event("shutdown")
async def shutdown():
    logger.info(f"Shutting down {settings.app_name}")
    await dispatcher.stop_polling()


@app.get("/health")
async def health():
    return {"status": "ok", "app": settings.app_name}
