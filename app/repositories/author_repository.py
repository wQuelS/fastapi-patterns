from app.models import Author
from app.repositories.base import BaseRepository


class AuthorRepository(BaseRepository):

    model = Author
