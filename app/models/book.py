

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.functions import now

from app.core.database import Base

__all__ = ['Book']


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(120), index=True)
    summary = Column(String(1000))
    created_at = Column(DateTime(), server_default=now(), nullable=False)
    author_id = Column(Integer, ForeignKey("authors.id"))

    author = relationship("Author", back_populates="books")


