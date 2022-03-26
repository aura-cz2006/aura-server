import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"isHealthy": True, "caresAboutYou": "❤️", }


@app.get("/buses")
def read_buses():
    return {"routes": []}


# debug
def start_dev():
    """Launched with `poetry run start_dev` at root level"""
    uvicorn.run("api.main:app", host="0.0.0.0", port=8000, reload=True)
