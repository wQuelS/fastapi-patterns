from pydantic import BaseModel

from app.models import Book


class AuthorBase(BaseModel):
    name: str
    bio: str


class AuthorCreate(AuthorBase):
    alias: str
    iban: str


class AuthorUpdate(BaseModel):
    name: str | None
    bio: str | None


class AuthorCreateResponse(AuthorBase):
    id: int

    class Config:
        orm_mode = True


class Author(AuthorBase):
    id: int
    books: list[Book] = []

    class Config:
        arbitrary_types_allowed = True
        orm_mode = True

