from fastapi import HTTPException, Query, Body, APIRouter

from schemas.hotels import Hotel, HotelPatch
from src.api.dependencies import PaginationDep
from src.database import async_sessionmaker_maker
from repositories.hotels import HotelsRepository


router = APIRouter(prefix="/hotels", tags=["Отели"])


@router.get("")
async def get_hotels(
    pagintation: PaginationDep,
    title: str | None = Query(None, description="Название отеля"),
    location: str | None = Query(None, description="Адрес отеля"),
):

    async with async_sessionmaker_maker() as session:
        return await HotelsRepository(session).get_all(
            location=location,
            title=title,
            limit=pagintation.per_page,
            offset=(pagintation.page - 1) * pagintation.per_page
        )
    
@router.get("/{hotel_id}", description='Получение отеля по ID')    
async def get_hotel(hotel_id: int):
    async with async_sessionmaker_maker() as session:
        return await HotelsRepository(session).get_one_or_none(id=hotel_id)


@router.post("")
async def create_hotel(
    hotel_data: Hotel = Body(
        openapi_examples={
            "1": {
                "summary": "Сочи",
                "value": {
                    "title": "Отель 5 звезд у моря",
                    "location": "Ул. Пушкина дом Колотушкина",
                },
            },
            "2": {
                "summary": "Дубай",
                "value": {"title": "Отель в пустыне", "location": "Ул. Абу-Бандита 5"},
            },
        }
    )
):
    async with async_sessionmaker_maker() as session:
        hotel = await HotelsRepository(session).add(hotel_data)
        await session.commit()
    return {"status": "OK", 'data': hotel}


@router.put("/{hotel_id}")
async def update_hotel(hotel_id: int, hotel_data: Hotel):
    async with async_sessionmaker_maker() as session:
        await HotelsRepository(session).edit(hotel_data, id=hotel_id)
        await session.commit()
    return {"status": "OK"}


@router.patch("/{hotel_id}")
async def update_patch_hotel(hotel_id: int, hotel_data: HotelPatch):
    async with async_sessionmaker_maker() as session:
        await HotelsRepository(session).edit(hotel_data, exclude_unset=True, id=hotel_id)
        await session.commit()
    return {"status": "OK"}


@router.delete("/{hotel_id}")
async def delete_hotel(hotel_id: int):
    async with async_sessionmaker_maker() as session:
        await HotelsRepository(session).delete(id=hotel_id)
        await session.commit()
    return {"status": "OK"}
