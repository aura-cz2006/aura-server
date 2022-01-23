from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"isHealthy": True, "caresAboutYou": "❤️", }
