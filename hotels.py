from fastapi import Query, Body, APIRouter

router = APIRouter(prefix="/hotels", tags=['Отели'])

hotels = [
    {"id": 1, "title": "Sochi", "name": "sochi"},
    {"id": 2, "title": "Dubai", "name": "dubai"},
    {"id": 3, "title": "London", "name": "london"},
    {"id": 4, "title": "New York", "name": "new york"}
]


@router.get('')
def get_hotels(
    title: str | None = Query(None, description="Название отеля"),
    id: int | None = Query(None, description="айдишник"),
):
    hotels_ = []
    for hotel in hotels:
        if id and hotel["id"] != id:
            continue
        if title and hotel["title"] != title:
            continue
        hotels_.append(hotel)
    return hotels_


@router.post('')
def create_hotel(title: str = Body(embed=True)):
    global hotels
    hotels.append({"id": hotels[-1]["id"] + 1, "title": title})


@router.put("/{hotel_id}")
def update_hotel(
    hotel_id: int, title: str = Body(embed=True), name: str = Body(embed=True)
):
    global hotels
    for hotel in hotels:
        if hotel["id"] == hotel_id:
            hotel["title"] = title
            hotel["name"] = name
    return {"status": "OK"}


@router.patch("/{hotel_id}")
def update_patch_hotel(
    hotel_id: int,
    title: str | None = Body(None, embed=True),
    name: str | None = Body(None, embed=True),
):
    global hotels
    for hotel in hotels:
        if hotel["id"] == hotel_id:
            if title != "string":
                hotel["title"] = title
            if hotel != "string":
                hotel["name"] = name
    return {"status": "OK"}


@router.delete("/{hotel_id}")
def delete_hotel(hotel_id: int):
    global hotels
    hotels = [hotel for hotel in hotels if hotel["id"] != hotel_id]
    return {"status": "OK"}
