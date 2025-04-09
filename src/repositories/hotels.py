from sqlalchemy import select, func, insert

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
    
    async def add(self, hotel_data):
        add_hotel_stmt = (
            insert(HotelsOrm)
            .values(**hotel_data.model_dump())
            .returning(HotelsOrm)
        )
        result = await self.session.execute(add_hotel_stmt)
        hotel = result.scalars().first()
        return hotel