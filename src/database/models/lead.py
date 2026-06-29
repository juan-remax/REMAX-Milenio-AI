from sqlalchemy import Column, Integer, String, Text, BigInteger

from src.database.models.base import Base, TimestampMixin


class Lead(Base, TimestampMixin):
    __tablename__ = "leads"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(200), nullable=False)
    phone = Column(String(20), nullable=True)
    email = Column(String(200), nullable=True)
    lead_type = Column(String(50), nullable=True)  # buyer, seller, investor
    status = Column(String(50), default="new")  # new, contacted, qualified, lost, closed
    notes = Column(Text, nullable=True)
    source = Column(String(100), nullable=True)  # telegram, inmovilla, web, referral
