from fastapi import APIRouter
from fastapi.params import Depends

from app.serializers.author import AuthorCreateResponse, AuthorCreate
from app.services.author_service import AuthorService
from app.utils.dependencies.services import get_author_service

router = APIRouter()


@router.post('', response_model=AuthorCreateResponse)
async def create_author(
        item: AuthorCreate,
        service: AuthorService = Depends(get_author_service)
):
    return await service.create_author(item)
