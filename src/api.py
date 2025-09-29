from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routes import currency_router


app = FastAPI(title="Currency API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(currency_router)


@app.get("/")
async def root():
    return {"message": "Welcome to the Currency API"}
