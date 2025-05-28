from pydantic import EmailStr
from sqlalchemy import select

from repositories.base import BaseRepository
from src.schemas.users import User, UserInDB
from src.models.users import UsersOrm


class UsersRepository(BaseRepository):
    model = UsersOrm
    schema = User

    async def get_user_with_hashed_password(self, email: EmailStr):
        query = select(self.model).filter_by(email=email)
        result = await self.session.execute(query)
        model = result.scalars().one_or_none()
        if not model:
            return None
        return UserInDB.model_validate(model)


    