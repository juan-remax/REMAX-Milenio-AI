from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.models.lead import Lead


class LeadRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, lead: Lead) -> Lead:
        self.session.add(lead)
        await self.session.commit()
        await self.session.refresh(lead)
        return lead

    async def get_by_id(self, lead_id: int) -> Lead | None:
        return await self.session.get(Lead, lead_id)

    async def list_by_status(self, status: str) -> list[Lead]:
        result = await self.session.execute(select(Lead).where(Lead.status == status))
        return list(result.scalars().all())

    async def list_all(self) -> list[Lead]:
        result = await self.session.execute(select(Lead))
        return list(result.scalars().all())
