import datetime
from typing import Optional

from pydantic import BaseModel


class BookBase(BaseModel):
    title: str
    summary: str
    publication_date: datetime


class BookCreate(BookBase):
    pass


class BookUpdate(BaseModel):
    title: str | None
    summary: str | None
    publication_date: Optional[datetime]


class Book(BookBase):
    id: int
    author_id: int

    class Config:
        orm_mode = True
