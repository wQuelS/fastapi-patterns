from fastapi import HTTPException
from sqlalchemy import or_, select
from starlette import status

from app.models import Author
from app.repositories.author_repository import AuthorRepository
from app.serializers.author import AuthorCreate


class AuthorService:

    def __init__(self, author_repo: AuthorRepository):
        self.repo = author_repo

    async def create_author(self, new_author: AuthorCreate):
        query = select(Author).where(
            or_(
                Author.iban == new_author.iban,
                Author.alias == new_author.alias
            )
        )

        await self.validate_fields(new_author, query)

        return await self.repo.create(new_author.dict())

    async def validate_fields(self, new_author: AuthorCreate, query):
        if await self.repo.exists(query):
            existing_authors = await self.repo.get_one(query)

            if any([
                existing_authors.iban == new_author.iban,
                existing_authors.alias == new_author.alias
            ]):
                raise HTTPException(
                    detail='should be unique',
                    status_code=status.HTTP_400_BAD_REQUEST
                )
