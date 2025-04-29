from fastapi import APIRouter

from src.database import async_sessionmaker_maker


router = APIRouter(prefix='/hotels', tags=['Номера'])

@router.get('/{hotel_id}/{rooms}')
async def get_rooms():
    async with async_sessionmaker_maker as session:
        

