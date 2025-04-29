from typing import Annotated

from pydantic import BaseModel
from fastapi import Depends, HTTPException, Query, Request

from src.services.auth import AuthService

class Pagination(BaseModel):
    page: Annotated[int | None, Query(description="Номер страницы", default=1, ge=1)]
    per_page: Annotated[int | None, Query(default=5, ge=1, lt=30, description="Количество элементов на странице")]

PaginationDep = Annotated[Pagination, Depends()]

def get_token(request: Request):
    token = request.cookies.get('access_token')
    if not token:
        raise HTTPException(status_code=401, detail="Вы не предоставили токен доступа")
    return token

def get_current_user_id(token: str = Depends(get_token)):
    
    data = AuthService().decode_token(token)
    return data['user_id']

UserIdDep = Annotated[int, Depends(get_current_user_id)]
