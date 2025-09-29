import uvicorn
import asyncio
from src.db import create_tables


def start_server():
    asyncio.run(create_tables())
    uvicorn.run("src.api:app", host="0.0.0.0", port=8080, log_level="info")