from datetime import datetime

from sqlalchemy import TIMESTAMP, Integer, String, func
from sqlalchemy.orm import Mapped, mapped_column

from src.core import BaseModel


class CurrencyModel(BaseModel):
    """
    Currency model

    Attributes:
        id (int): Primary key
        code (str): Currency code
        codein (str): Currency code in BRL
        name (str): Currency name
        high (float): Highest value
        low (float): Lowest value
        varBid (float): Variation bid
        pctChange (float): Percentage change
        bid (float): Bid value
        ask (float): Ask value
        timestamp (datetime): Timestamp of the currency data
        create_date (datetime): Date of creation
        created_at (datetime): Date of creation
        updated_at (datetime): Date of last update
    """

    __tablename__ = "currencies"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True
    )
    code: Mapped[str] = mapped_column(String(10), unique=True, nullable=False)
    codein: Mapped[str] = mapped_column(String(10), nullable=False)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    high: Mapped[float] = mapped_column(nullable=False)
    low: Mapped[float] = mapped_column(nullable=False)
    varBid: Mapped[float] = mapped_column(nullable=False)
    pctChange: Mapped[float] = mapped_column(nullable=False)
    bid: Mapped[float] = mapped_column(nullable=False)
    ask: Mapped[float] = mapped_column(nullable=False)
    timestamp: Mapped[datetime] = mapped_column(nullable=False)
    create_date: Mapped[datetime] = mapped_column(TIMESTAMP, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP, nullable=False, default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        TIMESTAMP, nullable=False, default=func.now(), onupdate=func.now()
    )
