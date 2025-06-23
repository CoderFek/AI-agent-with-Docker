from fastapi import FastAPI
from contextlib import asynccontextmanager
import os
from api.db import init_db
from api.chat.routing import router as chat_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(chat_router, prefix = "/api/chats")

MY_PROJECT = os.environ.get("MY_PROJECT") or "This is my project"
API_KEY = os.environ.get("API_KEY")
if not API_KEY:
    raise NotImplementedError("'API_KEY' is not set")

@app.get("/")
def get_index():
    return {"message": "Hello world", "project":MY_PROJECT, "api_key": API_KEY}