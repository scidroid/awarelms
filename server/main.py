import os
from fastapi import FastAPI, Form, Response
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from deta import Deta
import uvicorn
from twilio.twiml.messaging_response import MessagingResponse

deta = Deta(os.environ['KEY'])

db = deta.Base("aware")

app = FastAPI()

class Message(BaseModel):
    name: str
    description: str

@app.post("/bot")
def bot(Body: str = Form(...)):
  Body = Body.lower()
  resp = MessagingResponse()
  msg = resp.message()
  if "hello" in Body:
    a = db.fetch()
    msg.body(f'Hello, welcome to AwareLMS, the LMS that reaches everyone, these are your tasks: {a._items}')
  elif "send task" in Body:
    msg.body('Great! your task is delivered.')
  elif "today lesson" in Body:
    msg.body('View the CD #3, chapter 4, then check the new homework.')
  else:
      msg.body('I can not understand you, sorry!')
  resp = str(resp)
  return Response(content=resp, media_type="application/xml")

@app.post("/ms", status_code=201)
def create(ms: Message):
    m = db.put(ms.dict())
    return m

@app.get("/ms")
def list():
    ms = db.fetch()
    return ms

@app.get("/ms/{uid}")
def get(uid: str):
    m = db.get(uid)
    if m:
        return m
    return JSONResponse({"message": "not found"}, status_code=404)

uvicorn.run(app,host="0.0.0.0",port="8080")