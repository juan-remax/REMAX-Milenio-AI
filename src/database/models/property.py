from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey

from src.database.models.base import Base, TimestampMixin


class Property(Base, TimestampMixin):
    __tablename__ = "properties"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(300), nullable=False)
    address = Column(String(500), nullable=False)
    property_type = Column(String(50), nullable=False)  # apartment, house, commercial, land
    price = Column(Float, nullable=False)
    square_meters = Column(Float, nullable=True)
    bedrooms = Column(Integer, nullable=True)
    bathrooms = Column(Integer, nullable=True)
    description = Column(Text, nullable=True)
    status = Column(String(50), default="active")  # active, reserved, sold, rented
    lead_id = Column(Integer, ForeignKey("leads.id"), nullable=True)
