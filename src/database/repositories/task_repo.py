from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.models.conversation import Conversation


class ConversationRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, conversation: Conversation) -> Conversation:
        self.session.add(conversation)
        await self.session.commit()
        await self.session.refresh(conversation)
        return conversation

    async def get_by_user(self, user_id: int, limit: int = 20) -> list[Conversation]:
        result = await self.session.execute(
            select(Conversation)
            .where(Conversation.user_id == user_id)
            .order_by(Conversation.created_at.desc())
            .limit(limit)
        )
        return list(result.scalars().all())
