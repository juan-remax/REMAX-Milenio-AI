from sqlalchemy import Column, Integer, String, Text, BigInteger

from src.database.models.base import Base, TimestampMixin


class Conversation(Base, TimestampMixin):
    __tablename__ = "conversations"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, nullable=False, index=True)
    user_message = Column(Text, nullable=False)
    bot_response = Column(Text, nullable=False)
    intent = Column(String(50), nullable=True)
