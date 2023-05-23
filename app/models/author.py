__all__ = ['Author']

from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from app.core.database import Base


class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(63), unique=True, index=True)
    alias = Column(String(255))
    iban = Column(String(255), nullable=False)
    bio = Column(String(1000))

    books = relationship("Book", back_populates="author")

