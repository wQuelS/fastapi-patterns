from fastapi import APIRouter

from app.api.authors import router as author_router
from app.api.books import router as books_router


api_router = APIRouter()

api_router.include_router(author_router, prefix='/authors', tags=['Authors'])
api_router.include_router(books_router, prefix='/books', tags=['Books'])
