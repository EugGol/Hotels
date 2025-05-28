from sqlalchemy import select

from src.schemas.hotels import Hotel
from src.repositories.base import BaseRepository
from src.models.hotels import HotelsOrm


class HotelsRepository(BaseRepository):
    model = HotelsOrm
    schema = Hotel

    async def get_all(self, location, title, limit, offset) -> list[Hotel]:
        query = select(self.model)
        if title:
            query = query.where(self.model.title.ilike(f"%{title}%"))
        if location:
            query = query.where(self.model.location.ilike(f"%{location}%"))
        query = query.limit(limit).offset(offset)
        result = await self.session.execute(query)
        return [self.schema.model_validate(model, from_attributes=True) for model in result.scalars().all()]
