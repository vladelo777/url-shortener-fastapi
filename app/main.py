from fastapi import FastAPI
from app.routes import shortener, async_api

app = FastAPI(title="URL Shortener")

app.include_router(shortener.router)
app.include_router(async_api.router)