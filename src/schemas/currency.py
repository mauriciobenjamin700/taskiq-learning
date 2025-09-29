from datetime import datetime

from src.core import BaseSchema


class CurrencyResponseSchema(BaseSchema):
    """
    Schema for currency response from DB

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

    id: int
    code: str
    codein: str
    name: str
    high: float
    low: float
    varBid: float
    pctChange: float
    bid: float
    ask: float
    timestamp: datetime
    create_date: datetime
    created_at: datetime
    updated_at: datetime
