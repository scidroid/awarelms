import os
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from deta import Deta

deta = Deta(os.environ['KEY'])

db = deta.Base("aware")

app = FastAPI()

class Message(BaseModel):
    name: str
    description: str

@app.post("/ms", status_code=201)
def create(ms: Message):
    m = db.put(ms.dict())
    return m

@app.get("/ms")
def list():
    ms = next(db.fetch())
    return ms

@app.get("/ms/{uid}")
def get(uid: str):
    m = db.get(uid)
    if m:
        return m
    return JSONResponse({"message": "not found"}, status_code=404)
