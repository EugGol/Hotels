from sqlalchemy import select, func

from repositories.base import BaseRopository
from src.models.hotels import HotelsOrm


class HotelsRepository(BaseRopository):
    model = HotelsOrm

    async def get_all(self, location, title, limit, offset):
        query = select(HotelsOrm)
        if title:
            query = query.where(HotelsOrm.title.ilike(f"%{title}%"))
        if location:
            query = query.where(HotelsOrm.location.ilike(f"%{location}%"))
        query = query.limit(limit).offset(offset)
        result = await self.session.execute(query)
        return result.scalars().all()
