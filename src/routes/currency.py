from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends
from src.controllers import CurrencyController
from src.db import get_session
from src.schemas import CurrencyResponseSchema


router = APIRouter(prefix="/currency", tags=["Currency"])


@router.get("/")
async def get_currency(
    session: AsyncSession = Depends(get_session),
) -> CurrencyResponseSchema:
    """
    Get currency data from external API and store it in the database.

    Returns:
        CurrencyResponseSchema: The currency data stored in the database.
    """
    controller = CurrencyController(session)
    currency = await controller.get_currency()
    return currency


@router.get("/latest")
async def get_latest_currency(
    session: AsyncSession = Depends(get_session),
) -> CurrencyResponseSchema:
    """
    Get the latest currency data from the database.

    Returns:
        CurrencyResponseSchema: The latest currency on web.
    """
    controller = CurrencyController(session)
    currency = await controller.update_currency()
    return currency
