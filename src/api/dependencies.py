from typing import Annotated

from pydantic import BaseModel
from fastapi import Depends, Query

class Pagination(BaseModel):
    page: Annotated[int | None, Query(description="Номер страницы", default=1, ge=1)]
    per_page: Annotated[int | None, Query(default=5, ge=1, lt=30, description="Количество элементов на странице")]

PaginationDep = Annotated[Pagination, Depends()]


