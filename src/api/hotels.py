from typing import Annotated

from fastapi import Query, Body, APIRouter, Depends

from schemas.hotels import Hotel, HotelPatch
from src.api.dependencies import PaginationDep

router = APIRouter(prefix="/hotels", tags=['Отели'])

hotels = [
    {"id": 1, "title": "Sochi", "name": "sochi"},
    {"id": 2, "title": "Dubai", "name": "dubai"},
    {"id": 3, "title": "London", "name": "london"},
    {"id": 4, "title": "New York", "name": "new york"},
    {"id": 5, "title": "Tokyo", "name": "tokyo"},
]


@router.get('')
def get_hotels(
    pagintation: PaginationDep,
    title: str | None = Query(None, description="Название отеля"),
    id: int | None = Query(None, description="айдишник"),
    hotels_ = []
):
    for hotel in hotels:
        if id and hotel["id"] != id:
            continue
        if title and hotel["title"] != title:
            continue
        hotels_.append(hotel)
    start_index = (pagintation.page - 1) * pagintation.per_page
    end_index = start_index + pagintation.per_page
    return hotels_[start_index:][:end_index]



@router.post('')
def create_hotel(hotel_data: Hotel):
    global hotels
    hotels.append({"id": hotels[-1]["id"] + 1, "title": hotel_data.title})


@router.put("/{hotel_id}")
def update_hotel(hotel_id: int, hotel_data: Hotel):
    global hotels
    for hotel in hotels:
        if hotel["id"] == hotel_id:
            hotel["title"] = hotel_data.title
            hotel["name"] = hotel_data.name
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
