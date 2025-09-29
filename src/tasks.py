from taskiq_redis import RedisStreamBroker,  RedisAsyncResultBackend

from taskiq.schedule_sources import LabelScheduleSource
from taskiq import TaskiqScheduler

from src.db import get_session
from src.controllers import CurrencyController
import logging

LOGGER = logging.getLogger(__name__)

# Redis como broker (fila) E como result backend
broker = RedisStreamBroker("redis://localhost:6379")

broker = broker.with_result_backend(RedisAsyncResultBackend(
    "redis://localhost:6379"
))

scheduler = TaskiqScheduler(
    broker=broker,
    sources=[LabelScheduleSource(broker)],
)


@broker.task(schedule=[{"cron": "*/1 * * * *"}])
async def heavy_task() -> None:
    async for session in get_session():
        controller = CurrencyController(session)
        try:
            currency = await controller.update_currency()
            LOGGER.info(f"Currency updated: {currency}")
        except Exception as e:
            LOGGER.error(f"Error updating currency: {e}")
