from typing import Any

from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import Select


class BaseRepository:

    model: Any = None

    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, new_obj: dict):
        """
        :param new_obj:
        :return:
        """
        query = insert(self.model).returning(self.model)

        response = await self.session.execute(query, new_obj)
        await self.session.commit()
        result = response.scalar()
        return result

    async def exists(self, query: Select):
        query = query.with_only_columns(self.model.id)
        response = await self.session.execute(query)

        result = response.first()
        return bool(result)

    async def get_one(self, query: Select):
        response = await self.session.execute(query)
        result = response.scalar()

        return result
