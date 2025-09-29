from pydantic import BaseModel as PydanticBaseModel
from pydantic import ConfigDict
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase


class BaseModel(AsyncAttrs, DeclarativeBase):
    """
    Base class for all ORM models.
    """

    pass


class BaseSchema(PydanticBaseModel):
    """
    Base class for all Pydantic schemas.
    """

    model_config = ConfigDict(
        from_attributes=True,
        use_enum_values=True,
        str_strip_whitespace=True,
        arbitrary_types_allowed=True,
    )
    pass
