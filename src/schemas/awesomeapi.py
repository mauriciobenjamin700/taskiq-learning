from datetime import datetime

from src.core import BaseSchema


class AwesomeAPICurrencyResponse(BaseSchema):
    """
    Schema for currency response from AwesomeAPI

    Attributes:
        code (str): Currency code (e.g., "USD")
        codein (str): Currency code in (e.g., "BRL")
        name (str): Full name of the currency pair
        high (str): Highest value of the day
        low (str): Lowest value of the day
        varBid (str): Variation in bid price
        pctChange (str): Percentage change
        bid (str): Current bid price
        ask (str): Current ask price
        timestamp (datetime): Timestamp of the data
        create_date (datetime): Date of creation
    """

    code: str
    codein: str
    name: str
    high: str
    low: str
    varBid: str
    pctChange: str
    bid: str
    ask: str
    timestamp: datetime
    create_date: datetime
