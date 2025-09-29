from fastapi import HTTPException
import httpx
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.models import CurrencyModel
from src.db.repositories import CurrencyRepository
from src.schemas import AwesomeAPICurrencyResponse, CurrencyResponseSchema


class AwesomeAPIService:
    """
    Service to interact with AwesomeAPI for currency data

    Methods:
        get_currency_data: Fetches the current USD to BRL exchange rate
        get_currency: Retrieves the currency record from the database
        update_currency: Updates or creates the currency record in the database
    """

    def __init__(self, db_session: AsyncSession):
        self.__currency_repo = CurrencyRepository(db_session)

    async def update_currency(self) -> CurrencyResponseSchema:
        data = await AwesomeAPIService.get_currency_data()

        currency = await self.__currency_repo.get_by_code(data.code)
        if currency:
            for field, value in data.model_dump().items():
                if hasattr(currency, field):
                    setattr(currency, field, value)

            model = await self.__currency_repo.update(currency)
            return CurrencyResponseSchema.model_validate(model)

        new_currency = CurrencyModel(**data.model_dump())
        model = await self.__currency_repo.add(new_currency)
        return CurrencyResponseSchema.model_validate(model)

    async def get_currency(self) -> CurrencyResponseSchema:
        model = await self.__currency_repo.get_all()
        if not model:
            raise HTTPException(status_code=404, detail="Currency not found")
        return CurrencyResponseSchema.model_validate(model[0])

    @staticmethod
    async def get_currency_data() -> AwesomeAPICurrencyResponse:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                "https://economia.awesomeapi.com.br/json/last/USD-BRL"
            )
            data = response.json()
            schema = AwesomeAPICurrencyResponse(**data["USDBRL"])

            return schema
