from sqlalchemy.ext.asyncio import AsyncSession

from src.services import AwesomeAPIService
from src.schemas import CurrencyResponseSchema


class CurrencyController:
    """
    Controller for currency operations

    Methods:
        update_currency: Updates or creates the currency record in the database
    """

    def __init__(self, db_session: AsyncSession):
        self.__service = AwesomeAPIService(db_session)

    async def update_currency(self) -> CurrencyResponseSchema:
        return await self.__service.update_currency()

    async def get_currency(self) -> CurrencyResponseSchema:
        return await self.__service.get_currency()
