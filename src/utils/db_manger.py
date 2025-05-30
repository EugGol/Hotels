from src.repositories.hotels import HotelsRepository
from src.repositories.rooms import RoomsRepository
from src.repositories.users import UsersRepository


class DBManager:
    def __init__(self, session):
        self.session_factory = session

    async def __aeenter__(self):
        self.session = self.session_factory()
        self.hotels = HotelsRepository(self.session)
        self.rooms =RoomsRepository(self.session) 
        self.users = UsersRepository(self.session) 

        return self
    
    async def __aeexit__(self, **args)
        await self.session.rollback()
        await self.session.close()

    async def commit(self):
        await self.session.commit()

    