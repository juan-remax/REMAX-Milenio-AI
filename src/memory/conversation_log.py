from loguru import logger

from src.agents.intent_classifier import classify_intent
from src.database.models.conversation import Conversation
from src.database.session import async_session_factory


async def log_conversation(user_id: int, user_message: str, bot_response: str) -> None:
    intent = classify_intent(user_message)

    try:
        async with async_session_factory() as session:
            conversation = Conversation(
                user_id=user_id,
                user_message=user_message,
                bot_response=bot_response,
                intent=intent,
            )
            session.add(conversation)
            await session.commit()
    except Exception as e:
        logger.debug(f"Logging skipped (DB may be offline): {e}")
