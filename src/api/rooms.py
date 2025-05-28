from fastapi import APIRouter, Body, HTTPException

from src.repositories.rooms import RoomsRepository
from src.repositories.hotels import HotelsRepository
from src.database import async_sessionmaker_maker
from src.schemas.rooms import RoomAdd, RoomAddRequest, RoomPatchRequest, RoomPatch

router = APIRouter(prefix="/hotels", tags=["Номера"])


@router.get("/{hotel_id}/rooms")
async def get_rooms(hotel_id: int):        
    async with async_sessionmaker_maker() as session:
        return await RoomsRepository(session).get_filtered(hotel_id=hotel_id)

@router.get("{hotel_id}/rooms/{room_id}", description="Получение номера по ID")
async def get_room(hotel_id: int, room_id: int):
    async with async_sessionmaker_maker() as session:
        return await RoomsRepository(session).get_one_or_none(id=room_id, hotel_id=hotel_id)

@router.post("/{hotel_id}/rooms")
async def create_room(
    hotel_id: int,
    room_data: RoomAddRequest = Body(
        openapi_examples={
            "1": {
                "summary": "Люкс",  
                "value": {
                    "title": "Номер на двоих",
                    "description": None,
                    "price": 4500,
                    "quantity": 5,
                },
            },
            "2": {
                "summary": "Эконом",
                "value": {
                    "title": "Номер на одного",
                    "description": None,
                    "price": 1500,
                    "quantity": 7,
                },
            },
        }
    )
):
    _room_data = RoomAdd(hotel_id=hotel_id, **room_data.model_dump())
    async with async_sessionmaker_maker() as session:
        room = await RoomsRepository(session).add(_room_data)
        await session.commit()
    return {"status": "OK", "data": room}



@router.put("/{hotel_id}/rooms/{room_id}")
async def update_room(hotel_id: int, room_id: int, room_data: RoomAddRequest=Body()):
    _room_data = RoomAdd(hotel_id=hotel_id, **room_data.model_dump())
    async with async_sessionmaker_maker() as session:
        await RoomsRepository(session).edit(_room_data, id=room_id, hotel_id=hotel_id)
        await session.commit()
    return {"status": "OK"}


@router.patch("/{hotel_id}/rooms/{room_id}")
async def update_patc_room(hotel_id: int, room_id: int, room_data: RoomPatchRequest):
    _room_data = RoomPatch(hotel_id=hotel_id, **room_data.model_dump(exclude_unset=True))
    async with async_sessionmaker_maker() as session:
        await RoomsRepository(session).edit(_room_data, exclude_unset=True, id=room_id, hotel_id=hotel_id)
        await session.commit()
    return {"status": "OK"}

@router.delete("/{hotel_id}/rooms/{room_id}")
async def delete_room(hotel_id: int, room_id: int):
    async with async_sessionmaker_maker() as session:
        await RoomsRepository(session).delete(id=room_id, hotel_id=hotel_id)
        await session.commit()
    return {"status": "OK"}
