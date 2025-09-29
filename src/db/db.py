from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from src.core import settings


engine = create_async_engine(settings.DB_URL, echo=True)
async_session = async_sessionmaker(engine, expire_on_commit=False)


async def create_tables():
    from src.db.models import CurrencyModel
    from src.core import BaseModel

    print("Creating database tables...")
    print(CurrencyModel.__tablename__)

    async with engine.begin() as conn:
        await conn.run_sync(BaseModel.metadata.create_all)
    await conn.commit()


async def get_session():
    async with async_session() as session:
        try:
            yield session
        finally:
            await session.close()
