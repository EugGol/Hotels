from pydantic import BaseModel, Field, ConfigDict

class RoomAdd(BaseModel):
    hotel_id: int
    title: str
    description: str | None = Field(None)
    price: int
    quantity: int

class RoomAddRequest(BaseModel):
    title: str
    description: str | None = None
    price: int
    quantity: int



class Room(RoomAdd):
    id: int
    model_config = ConfigDict(from_attributes=True)

class RoomPatch(BaseModel):
    hotel_id: int | None = None
    title: str | None = None
    description: str | None = None
    price: int | None = None
    quantity: int | None = None

class RoomPatchRequest(BaseModel):
    title: str | None = None
    description: str | None = None
    price: int | None = None
    quantity: int | None = None