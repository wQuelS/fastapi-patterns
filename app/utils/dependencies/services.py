from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.author_repository import AuthorRepository
from app.services.author_service import AuthorService
from app.utils.dependencies.get_session import get_session


def get_author_service(
        session: AsyncSession = Depends(get_session)
) -> AuthorService:
    repo = AuthorRepository(session)
    service = AuthorService(author_repo=repo)

    return service
