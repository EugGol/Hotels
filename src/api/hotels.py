from fastapi import Query, Body, APIRouter

from sqlalchemy import insert, select, func, collate


from schemas.hotels import Hotel, HotelPatch
from src.api.dependencies import PaginationDep
from src.database import async_sessionmaker_maker, engine
from src.models.hotels import HotelsOrm
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
        add_hotel_stmt = insert(HotelsOrm).values(**hotel_data.model_dump())
        print(add_hotel_stmt.compile(engine, compile_kwargs={"literals_binds": True}))
        await session.execute(add_hotel_stmt)
        await session.commit()
    return {"status": "OK"}


@router.put("/{hotel_id}")
def update_hotel(hotel_id: int, hotel_data: Hotel):
    global hotels
    for hotel in hotels:
        if hotel["id"] == hotel_id:
            hotel["title"] = hotel_data.title
            hotel["name"] = hotel_data.location
    return {"status": "OK"}


@router.patch("/{hotel_id}")
def update_patch_hotel(hotel_id: int, hotel_data: HotelPatch):
    global hotels
    for hotel in hotels:
        if hotel["id"] == hotel_id:
            if hotel_data.title != "string":
                hotel["title"] = hotel_data.title
            if hotel != "string":
                hotel["name"] = hotel_data.name
    return {"status": "OK"}


@router.delete("/{hotel_id}")
def delete_hotel(hotel_id: int):
    global hotels
    hotels = [hotel for hotel in hotels if hotel["id"] != hotel_id]
    return {"status": "OK"}
