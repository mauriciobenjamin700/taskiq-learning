from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.models.currency import CurrencyModel


class CurrencyRepository:
    def __init__(self, session: AsyncSession):
        self.__session = session

    async def add(self, currency: CurrencyModel) -> CurrencyModel:
        self.__session.add(currency)
        await self.__session.commit()
        await self.__session.refresh(currency)
        return currency

    async def get_all(self) -> Sequence[CurrencyModel]:
        query = select(CurrencyModel)
        result = await self.__session.execute(query)
        return result.scalars().all()

    async def get_by_id(self, id: int) -> CurrencyModel | None:
        query = select(CurrencyModel).where(CurrencyModel.id == id)
        result = await self.__session.execute(query)
        return result.scalars().first()

    async def get_by_code(self, code: str) -> CurrencyModel | None:
        query = select(CurrencyModel).where(CurrencyModel.code == code)
        result = await self.__session.execute(query)
        return result.scalars().first()

    async def update(self, currency: CurrencyModel) -> CurrencyModel:
        await self.__session.commit()
        await self.__session.refresh(currency)
        return currency

    async def delete(self, currency: CurrencyModel) -> None:
        await self.__session.delete(currency)
        await self.__session.commit()
