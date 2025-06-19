from fastapi import FastAPI
import os

app = FastAPI()

MY_PROJECT = os.environ.get("MY_PROJECT") or "This is my project"
API_KEY = os.environ.get("API_KEY")
if not API_KEY:
    raise NotImplementedError("'API_KEY' is not set")

@app.get("/")
def get_index():
    return {"message": "Hello world", "project":MY_PROJECT, "api_key": API_KEY}