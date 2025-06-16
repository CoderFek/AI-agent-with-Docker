from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get_index():
    return {"message": "Hello world"}